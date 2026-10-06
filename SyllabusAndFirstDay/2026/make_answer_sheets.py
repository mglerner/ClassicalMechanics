#!/usr/bin/env python3
"""Write crops.json (in the pack's build folder) per prep pack (PHY 317): the crops the pack page shows.

Taylor's own problem statement (from the textbook scan, bands in _shared/taylor-bands-ch<N>.txt)
and the ISM worked solution (from the pack's solution PDFs via the `Solutions:` line) for the
PCCI, for every problem named in the notes' In-class problems section, and for the day's posted
lists (Will's in-class menu and look-at problems); plus the solution pages nothing claimed.
shared/make_pack_html.py places each crop under its problem.

    Solutions: in-class#1 = 3.5@.132-.377, 3.10@.377-.541; look-at#1 = 3.32@.1-.4

    python make_answer_sheets.py            # all packs in the current format
    python make_answer_sheets.py 06 07      # just these
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Imported here, not per function: without Pillow the crops used to come back empty and every
# crops.json was overwritten with no crops, silently (2026-10-05).
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path.home() / "coding/courses/shared"))
import packnotes as P  # noqa: E402
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


def solutions_map(notes):
    """-> {(filename-substring, page): [(problem, band-or-None)]}."""
    raw = notes.tagged_line("Solutions:")
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


def trim_margins(im, pad=14, edge=0.03):
    """Cut blank margin off all four sides of a crop (Michael, 2026-10-03: the key crop had wide
    white margins). Ink = a few dark pixels in a row or column, ignoring the outer edges where
    crop marks and scan borders live."""
    a = np.asarray(im.convert("L"))
    h, w = a.shape
    inner = a[int(edge * h):h - int(edge * h), int(edge * w):w - int(edge * w)]
    dark = inner < 160
    rows = np.flatnonzero(dark.sum(axis=1) >= 3)
    cols = np.flatnonzero(dark.sum(axis=0) >= 3)
    if not len(rows) or not len(cols):
        return im
    y0 = max(0, rows[0] + int(edge * h) - pad); y1 = min(h, rows[-1] + int(edge * h) + pad)
    x0 = max(0, cols[0] + int(edge * w) - pad); x1 = min(w, cols[-1] + int(edge * w) + pad)
    return im.crop((x0, y0, x1, y1))


def crop_statements(pack_dir, wanted, bands):
    """Cut each wanted problem's statement out of the textbook. -> {prob: [src]}."""
    todo = {q: bands[q] for q in wanted if q in bands}
    if not todo or not TEXTBOOK.exists() or not shutil.which("pdftoppm"):
        return {}
    out_dir = P.layout(pack_dir)["build"] / "answer-images"
    out_dir.mkdir(parents=True, exist_ok=True)
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
        trim_margins(im.crop((0, y0, w, y1))).save(out_dir / name)
        out.setdefault(prob, []).append(f"answer-images/{name}")
    return out


def is_blank(png):
    """True for an all-but-empty scan page (Ch7's in-class p4)."""
    im = Image.open(png).convert("L")
    lo, hi = im.getextrema()
    return lo > 235          # nothing darker than near-white anywhere


def render_pages(pack_dir):
    """Rasterise every solution PDF page once. -> [{path, src, file, page, hw}]."""
    if not shutil.which("pdftoppm"):
        return []
    out_dir = P.layout(pack_dir)["build"] / "answer-images"
    pages = []
    for pdf in P.pdfs(pack_dir, SOL_GLOB):
        # the full slug, and only this PDF's own page files: a 48-char cut can give two PDFs the
        # same stem (it did in 210), and a prefix glob also matches longer stems
        stem = re.sub(r"[^A-Za-z0-9]+", "-", pdf.stem).strip("-").lower()
        out_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pdftoppm", "-png", "-r", str(SOL_DPI), str(pdf),
                        str(out_dir / stem)], check=True, capture_output=True)
        for png in sorted(out_dir.glob(stem + "-*.png")):
            n = re.fullmatch(rf"{re.escape(stem)}-(\d+)\.png", png.name)
            if not n:
                continue
            if is_blank(png):
                continue
            pages.append({"path": png, "src": f"answer-images/{png.name}",
                          "file": pdf.name, "stem": stem,
                          "page": int(n.group(1)),
                          "hw": bool(HW_RE.search(pdf.name))})
    return pages


def crop_problems(pages, smap):
    """Cut each banded problem out of its page.

    -> ({problem: [(src, caption)]}, {id(page) that a crop claimed}).
    """
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
            trim_margins(im.crop((0, top, w, bot))).save(pg["path"].parent / name)
            crops.setdefault(prob, []).append(
                (f"answer-images/{name}", f"{pg['file']}, p{pg['page']}"))
            claimed.add(id(pg))
    return crops, claimed


def listed_on(smap, pg):
    for (sub, page), items in smap.items():
        if sub in pg["file"].lower() and page == pg["page"]:
            return [p for p, _ in items]
    return None


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

def main(only=None):
    """Write crops.json (in the pack's build folder) per pack: Taylor's statement and the ISM crop for the PCCI, for every
    problem named in the In-class problems section, and for the day's posted lists (Will's
    in-class menu and look-at problems), plus the solution pages nothing claimed.
    shared/make_pack_html.py places them under the problems on the pack page."""
    wrote = cropped = statements = 0
    bands = problem_bands()
    for n, date, path in P.pack_files("317"):
        if only and f"{n:02d}" not in only:
            continue
        if not path.exists():
            continue
        notes = P.Notes(path)
        if notes.old_format:
            continue
        pack = P.pack_of(path)
        smap = solutions_map(notes)
        pages = render_pages(pack)
        crops, claimed = crop_problems(pages, smap)
        wanted = list(notes.all_problems())
        for q in posted_for(n):
            if q not in wanted:
                wanted.append(q)
        stmts = crop_statements(pack, set(wanted), bands)
        cropped += len(crops)
        statements += len(stmts)
        problems = {}
        for q in wanted:
            if q in stmts:
                problems.setdefault(q, {})["statement"] = stmts[q]
            if q in crops:
                problems.setdefault(q, {})["worked"] = crops[q]
        for q, lst in crops.items():          # a Solutions: crop for a problem no list named
            problems.setdefault(q, {}).setdefault("worked", lst)
        pcci = notes.pcci_problems()
        unclaimed = []
        for pg in pages:
            if id(pg) in claimed:
                continue
            listed = listed_on(smap, pg)
            note = f"on this page: {', '.join(listed)}" if listed else ("not on the Solutions: line" if smap else "no Solutions: line")
            if pg["hw"]:
                m = HW_RE.search(pg["file"])
                note += "; homework set" + (f" HW{int(m.group(1)):02d}" if m else "")
            unclaimed.append({"src": pg["src"], "file": pg["file"], "page": pg["page"], "note": note})
        P.layout(pack)["build"].mkdir(exist_ok=True)
        json.dump({"pcci": {"id": notes.pcci_id(), "images": []}, "posted": posted_for(n),
                   "problems": problems, "unclaimed": unclaimed},
                  open(P.layout(pack)["build"] / "crops.json", "w"), indent=1)
        wrote += 1
    print(f"wrote {wrote} crops.json; {cropped} solution crops; {statements} problem statements"
          + ("" if bands else "  (no taylor-bands yet)"))


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
