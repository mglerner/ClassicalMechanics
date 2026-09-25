#!/usr/bin/env python3
"""Write 03-answers.html: one answer sheet per prep pack (PHY 317).

Michael's own sheet, so it quotes the solutions manual freely. What goes on
a screen or into a student deck is his call, not the generator's.

Two layers, both derived from `00-prep-notes.md` so there is no second copy
of an answer to drift:

1. The `Check:` lines under each plan row -- the answers, already curated
   per day, grouped by the `Groupwork:` line (playbook 3a).
2. The fully worked solution for each problem, cropped out of the pack's
   ISM solution PDF and shown directly under that problem's checks.

The crop comes from the optional `Solutions:` line, which maps a page to
the problems on it and where they sit vertically:

    Solutions: in-class#1 = 3.5@.11-.38, 3.10@.37-.54, 3.11@.53-.90

`in-class` is any substring of the PDF's filename, `#1` is the page, and
`@a-b` is the problem's band as a fraction of page height. A problem may
appear on several pages (3.11 runs over a page break); each gets its own
crop. A problem listed without a band still labels the page.

A chapter's solution PDF covers all of its days at once, so without the
bands every day's sheet carries the whole chapter. Pages that no crop
claims are shown whole at the end, labelled with what is on them.

    python make_answer_sheets.py            # all packs
    python make_answer_sheets.py 07 08      # just these
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import make_active_learning as M
import make_review_checklists as CHK
import make_fall2026_calendar as CAL

SOL_DPI = 110            # readable on screen, small enough to screenshot
SOL_GLOB = "*olution*.pdf"
HW_RE = re.compile(r"\bHW\s*0*(\d+)", re.I)
PAD = 0.004              # page-height fraction added above and below a crop

# Taylor's own problem statements. One shared scan for the whole course, so
# the band map is shared too rather than copied into 27 packs. Lines look
# like `3.10 = 115@.700-.756` -- PDF page (book page + 15), then the band.
TEXTBOOK = (Path.home() / "coding/courses/ClassicalMechanics/private/WillF2025"
            / "MoodleCourse/extracted/01_Course_Information/Classical_Taylor.pdf")
PROBLEM_BANDS = (Path.home() / "coding/courses/ClassicalMechanics/private"
                 / "F2026PrepPacks/_shared")   # taylor-bands-ch*.txt, one per chapter

CSS = """
body { background: #fff; margin: 0; padding: 16px 18px; color: #111;
       font-family: "Iowan Old Style", Palatino, Georgia, serif;
       font-variant-numeric: tabular-nums; }
h1 { font-size: 19px; margin: 0 0 2px 0; font-weight: normal; }
h1 .when { font-size: 14px; font-style: italic; color: #666; margin-left: 10px; }
h2 { font-size: 12px; letter-spacing: .12em; text-transform: uppercase;
     color: #6b6b6b; margin: 16px 0 6px 0; font-weight: normal;
     border-bottom: 1px solid #ccc; padding-bottom: 3px; }
.prob { margin: 0 0 14px 0; break-inside: avoid; }
.num { font-weight: bold; font-size: 15px; }
.num .when { font-weight: normal; font-style: italic; color: #777;
             font-size: 12.5px; margin-left: 6px; }
.task { font-size: 13.5px; color: #333; margin: 1px 0 2px 0; }
ul { margin: 0; padding-left: 17px; }
li { font-size: 14.5px; line-height: 1.4; }
.none { font-size: 13.5px; color: #777; font-style: italic; }
.stmt { margin: 3px 0 5px 0; }
.stmt img { width: 100%; border: 1px solid #e3e3e3; display: block;
            margin: 2px 0 0 0; background: #fcfcfa; }
.worked { margin: 5px 0 0 0; }
.worked img { width: 100%; border: 1px solid #ddd; display: block;
              margin: 3px 0 0 0; }
.cap { font-size: 12.5px; color: #666; font-style: italic; margin: 0; }
.sol { margin: 0 0 20px 0; break-inside: avoid; }
.sol img { width: 100%; border: 1px solid #ccc; display: block; }
.warn { background: #fff3cd; border: 1px solid #e0cd8a; padding: 7px 10px;
        font-size: 13px; margin: 14px 0 0 0; }
@media print { body { padding: 0; } h2 { break-after: avoid; } }
"""

SKIP_AS_TASK = ("Check:", "Read back:", "Next:", "Check ")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def segments(text):
    return [s.strip() for s in text.split("<br>") if s.strip()]


def row_entries(rows):
    """[(problem-or-None, when, task, [checks])] for rows that carry answers."""
    out = []
    for a, b, m, mode, _src, text in rows:
        segs = segments(text)
        checks = [s for s in segs if s.startswith("Check")]
        if not checks:
            continue
        body = [s for s in segs if not s.startswith(SKIP_AS_TASK)]
        # the number can sit in any non-Check line: many rows open with a
        # "We're about to find ..." frame.
        probs = [q for s in body for q in re.findall(r"\b(\d+\.\d+)\b", s)]
        task = next((s for s in body if re.search(r"\b\d+\.\d+\b", s)),
                    body[0] if body else "")
        out.append((probs[0] if probs else None, M.clock(a), task, checks))
    return out


def solutions_map(lines):
    """-> {(filename-substring, page): [(problem, band-or-None)]}."""
    raw = M.tagged_line(lines, "Solutions:")
    out = {}
    if not raw:
        return out
    for entry in raw.split(";"):
        if "=" not in entry or "#" not in entry.split("=")[0]:
            continue
        key, probs = entry.split("=", 1)
        sub, page = key.rsplit("#", 1)
        items = []
        for tok in probs.split(","):
            tok = tok.strip()
            if not tok:
                continue
            m = re.match(r"([\d.]+?)@([\d.]+)-([\d.]+)$", tok)
            if m:
                items.append((m.group(1), (float(m.group(2)), float(m.group(3)))))
            else:
                items.append((tok, None))
        out[(sub.strip().lower(), int(page.strip()))] = items
    return out


def problem_bands():
    """-> {problem: [(pdf_page, top, bottom), ...]}; a statement may span pages."""
    out = {}
    for f in sorted(PROBLEM_BANDS.glob("taylor-bands-ch*.txt")):
        for line in f.read_text().split("\n"):
            line = line.split("#")[0].strip()
            m = re.match(r"([\d.]+)\s*=\s*(\d+)@([\d.]+)-([\d.]+)$", line)
            if m:
                out.setdefault(m.group(1), []).append(
                    (int(m.group(2)), float(m.group(3)), float(m.group(4))))
    return out


def crop_statements(pack_dir, wanted, bands):
    """Cut each wanted problem's statement out of the textbook. -> {prob: [src]}."""
    try:
        from PIL import Image
    except ImportError:
        return {}
    todo = {q: bands[q] for q in wanted if q in bands}
    if not todo or not TEXTBOOK.exists() or not shutil.which("pdftoppm"):
        return {}
    out_dir = pack_dir / "03-answers-files"
    out_dir.mkdir(exist_ok=True)
    cache = Path(tempfile.gettempdir()) / "taylor-pages"
    cache.mkdir(exist_ok=True)
    out = {}
    for prob, spans in sorted(todo.items()):
      for i, (page, top, bot) in enumerate(spans):
        src = cache / f"p-{page}.png"
        if not src.exists():
            subprocess.run(["pdftoppm", "-png", "-r", str(SOL_DPI),
                            "-f", str(page), "-l", str(page),
                            str(TEXTBOOK), str(cache / "one")],
                           check=True, capture_output=True)
            made = sorted(cache.glob("one-*.png"))
            if not made:
                continue
            made[0].rename(src)
        im = Image.open(src)
        w, h = im.size
        y0, y1 = max(0, int((top - PAD) * h)), min(h, int((bot + PAD) * h))
        if y1 <= y0:
            continue
        name = f"taylor-{prob.replace('.', '_')}-{i + 1}.png"
        im.crop((0, y0, w, y1)).save(out_dir / name)
        out.setdefault(prob, []).append(f"03-answers-files/{name}")
    return out


def is_blank(png):
    """True for an all-but-empty scan page (Ch7's in-class p4)."""
    try:
        from PIL import Image
    except ImportError:
        return False
    im = Image.open(png).convert("L")
    lo, hi = im.getextrema()
    return lo > 235          # nothing darker than near-white anywhere


def render_pages(pack_dir):
    """Rasterise every solution PDF page once. -> [{path, src, file, page, hw}]."""
    if not shutil.which("pdftoppm"):
        return []
    out_dir = pack_dir / "03-answers-files"
    pages = []
    for pdf in sorted(pack_dir.glob(SOL_GLOB)):
        stem = re.sub(r"[^A-Za-z0-9]+", "-", pdf.stem).strip("-").lower()[:48]
        out_dir.mkdir(exist_ok=True)
        subprocess.run(["pdftoppm", "-png", "-r", str(SOL_DPI), str(pdf),
                        str(out_dir / stem)], check=True, capture_output=True)
        for png in sorted(out_dir.glob(stem + "-*.png")):
            n = re.search(r"-(\d+)\.png$", png.name)
            if not n:
                continue
            if is_blank(png):
                continue
            pages.append({"path": png, "src": f"03-answers-files/{png.name}",
                          "file": pdf.name, "stem": stem,
                          "page": int(n.group(1)),
                          "hw": bool(HW_RE.search(pdf.name))})
    return pages


def crop_problems(pages, smap):
    """Cut each banded problem out of its page.

    -> ({problem: [(src, caption)]}, {id(page) that a crop claimed}).
    """
    try:
        from PIL import Image
    except ImportError:
        return {}, set()
    crops, claimed = {}, set()
    for pg in pages:
        banded = [(q, b) for q, b in
                  (i for lst in [lst for (sub, page), lst in smap.items()
                                 if sub in pg["file"].lower() and page == pg["page"]]
                   for i in lst) if b]
        for (qa, ba), (qb, bb) in zip(banded, banded[1:]):
            if ba[1] + PAD > bb[0] - PAD:
                print(f"WARNING {pg['file']} p{pg['page']}: {qa} and {qb} overlap "
                      f"once PAD={PAD} is added ({ba[1]:.3f} vs {bb[0]:.3f}); "
                      f"tighten a band or lower PAD")
        items = []
        for (sub, page), lst in smap.items():
            if sub in pg["file"].lower() and page == pg["page"]:
                items = lst
                break
        im = None
        for prob, band in items:
            if band is None:
                continue
            if im is None:
                im = Image.open(pg["path"])
            w, h = im.size
            top, bot = max(0, int((band[0] - PAD) * h)), min(h, int((band[1] + PAD) * h))
            if bot <= top:
                continue
            name = f"{pg['stem']}-p{pg['page']}-{prob.replace('.', '_')}.png"
            im.crop((0, top, w, bot)).save(pg["path"].parent / name)
            crops.setdefault(prob, []).append(
                (f"03-answers-files/{name}", f"{pg['file']}, p{pg['page']}"))
            claimed.add(id(pg))
    return crops, claimed


def listed_on(smap, pg):
    for (sub, page), items in smap.items():
        if sub in pg["file"].lower() and page == pg["page"]:
            return [p for p, _ in items]
    return None


def render(n, date, topic, rows, groupwork, pcci, pages, smap, crops,
           claimed, stmts, lookat=()):
    gw, other, pcci_ent = [], [], []
    for prob, when, task, checks in row_entries(rows):
        if pcci and "PCCI" in task:
            pcci_ent.append((prob, when, task, checks))
        elif prob and prob in groupwork:
            gw.append((prob, when, task, checks))
        else:
            other.append((prob, when, task, checks))

    o = ["<!doctype html><meta charset=utf-8>",
         f"<title>PHY 317 answers -- class {n:02d}</title><style>{CSS}</style>",
         f"<h1>Class {n:02d} answers<span class=when>{date} &middot; "
         f"{esc(topic)}</span></h1>"]
    seen, shown_stmt = set(), set()

    def block(title, items):
        o.append(f"<h2>{title}</h2>")
        if not items:
            o.append("<p class=none>none</p>")
            return
        for prob, when, task, checks in items:
            o.append(f'<div class=prob><div class=num>{prob or "&mdash;"}'
                     f'<span class=when>{when}</span></div>')
            if task and task != prob:
                o.append(f"<div class=task>{esc(task)}</div>")
            if prob in stmts and prob not in shown_stmt:
                shown_stmt.add(prob)
                o.append(f'<div class=stmt><p class=cap>Taylor {esc(prob)}</p>'
                         + "".join(f'<img src="{esc(src)}" '
                                   f'alt="Taylor {esc(prob)}">'
                                   for src in stmts[prob])
                         + '</div>')
            o.append("<ul>" + "".join(f"<li>{esc(c)}</li>" for c in checks)
                     + "</ul>")
            if prob in crops and prob not in seen:
                seen.add(prob)
                o.append("<div class=worked>")
                for src, cap in crops[prob]:
                    o.append(f'<p class=cap>worked solution &middot; {esc(cap)}</p>'
                             f'<img src="{esc(src)}" alt="{esc(prob)}">')
                o.append("</div>")
            o.append("</div>")

    block(f"PCCI {esc(pcci) if pcci else ''}".strip(), pcci_ent)
    block("Groupwork " + (", ".join(groupwork) if groupwork else ""), gw)
    block("Everything else with an answer", other)
    # Look-at problems are posted to students but never worked in class, so
    # they are in no plan row; render whatever of them we cropped.
    rest = [(p, "solution posted; not worked in class", "", [])
            for p in lookat if p not in seen]
    if rest:
        block("Also on today's lists (posted, not worked in class)", rest)

    left = [p for p in pages if id(p) not in claimed]
    if left:
        o.append("<h2>Other solution pages</h2>")
        o.append("<p class=warn>Shown whole because no problem on them is "
                 "cropped for today.</p>")
        for pg in sorted(left, key=lambda g: (g["hw"], g["file"], g["page"])):
            listed = listed_on(smap, pg)
            bits = []
            if listed:
                bits.append("on this page: " + esc(", ".join(listed)))
            elif smap:
                bits.append("not listed on the <code>Solutions:</code> line")
            else:
                bits.append("no <code>Solutions:</code> line in the prep notes")
            if pg["hw"]:
                m = HW_RE.search(pg["file"])
                bits.append("homework set"
                            + (f" HW{int(m.group(1)):02d}" if m else ""))
            o.append(f'<div class=sol><p class=cap>{" &middot; ".join(bits)}</p>'
                     f'<p class=cap>{esc(pg["file"])}, page {pg["page"]}</p>'
                     f'<img src="{esc(pg["src"])}" alt="{esc(pg["file"])}"></div>')

    o.append("<footer>Generated by make_answer_sheets.py from the plan table "
             "in 00-prep-notes.md -- edit the plan, not this file.</footer>")
    return "\n".join(o)


def lookat_for(n, key="lookat"):
    """The day's look-at (or in-class) problems from Will's chapter lists.

    Both can appear in no plan row: look-at problems are never worked at the
    board, and Will's in-class list is a MENU, so our plan deliberately
    schedules only some of it. Either way the solution is posted and Michael
    can be asked about it, so it belongs on his sheet. Without this they were
    cropped, marked claimed, and then rendered nowhere (found 2026-09-24:
    17 packs were missing at least one).
    """
    for cn, _d, _topic, reading, ch, chday in CHK.class_rows():
        if cn != n:
            continue
        if ch is None or ch not in CAL.CHAPTER_PROBLEMS:
            return []
        lst = CAL.CHAPTER_PROBLEMS[ch][key]
        if len(lst) == 1:                      # chapter list not split by day
            return list(lst[0])
        return list(lst[chday - 1]) if chday - 1 < len(lst) else []
    return []


def posted_for(n):
    """Everything the day owns, in-class menu first, then look-at."""
    out = []
    for key in ("inclass", "lookat"):
        for p in lookat_for(n, key):
            if p not in out:
                out.append(p)
    return out


def pcci_number(rows):
    for _a, _b, _m, _mode, _src, text in rows:
        m = re.search(r"PCCI (\d+\.\d+)", text)
        if m:
            return m.group(1)
    return ""


def main(only=None):
    wrote = cropped = statements = 0
    bands = problem_bands()
    for n, date, path in M.pack_files():
        if only and f"{n:02d}" not in only:
            continue
        lines = path.read_text().split("\n")
        rows = M.plan_rows(lines, path)
        if not rows:
            continue
        gw = M.groupwork(lines) or []
        smap = solutions_map(lines)
        pages = render_pages(path.parent)
        crops, claimed = crop_problems(pages, smap)
        wanted = {q for q, *_ in row_entries(rows) if q} | set(posted_for(n))
        stmts = crop_statements(path.parent, wanted, bands)
        cropped += len(crops)
        statements += len(stmts)
        (path.parent / "03-answers.html").write_text(
            render(n, date, M.topic(lines, path), rows, gw, pcci_number(rows),
                   pages, smap, crops, claimed, stmts, posted_for(n)))
        wrote += 1
    print(f"wrote {wrote} answer sheets; {cropped} solution crops; "
          f"{statements} problem statements"
          + ("" if bands else "  (no taylor-problem-bands.txt yet)"))


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
