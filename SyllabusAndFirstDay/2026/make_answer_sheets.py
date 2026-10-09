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
import sys
from pathlib import Path

# Imported here, not per function: without Pillow the crops used to come back empty and every
# crops.json was overwritten with no crops, silently (2026-10-05).
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
import answer_sheets as AS  # noqa: E402  (trim_margins, band files, page cache, render, crop)
import courses as C  # noqa: E402
import packnotes as P  # noqa: E402
import make_review_checklists as CHK
import make_fall2026_calendar as CAL

SOL_GLOB = "*olution*.pdf"
HW_RE = re.compile(r"\bHW\s*0*(\d+)", re.I)
PAD = AS.PAD             # page-height fraction added above and below a crop

# Taylor's own problem statements. One shared scan for the whole course, so
# the band map is shared too rather than copied into 27 packs. Lines look
# like `3.10 = 115@.700-.756` -- PDF page (book page +15, except Ch 12: +17 from book p460;
# see audit_taylor_coverage.py), then the band.
TEXTBOOK = (C.private("317") / "WillF2025"
            / "MoodleCourse/extracted/01_Course_Information/Classical_Taylor.pdf")
PROBLEM_BANDS = C.packs("317") / "_shared"   # taylor-bands-ch*.txt, one per chapter
# Raw page renders of the textbook scan, kept across runs (only the render is cached).
PAGE_CACHE = AS.page_cache("taylor-pages")


def problem_bands():
    """-> {problem: [(pdf_page, top, bottom), ...]}; a statement may span pages."""
    return AS.read_bands(sorted(PROBLEM_BANDS.glob("taylor-bands-ch*.txt")))


def crop_statements(pack_dir, wanted, bands):
    """Cut each wanted problem's statement out of the textbook. -> {prob: [src]}."""
    todo = {q: bands[q] for q in wanted if q in bands}
    if not todo or not TEXTBOOK.exists() or not shutil.which("pdftoppm"):
        return {}
    out_dir = P.layout(pack_dir)["build"] / "answer-images"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = {}
    for prob, spans in sorted(todo.items()):
      for i, (page, top, bot) in enumerate(spans):
        im = Image.open(AS.raw_page(TEXTBOOK, page, PAGE_CACHE))
        w, h = im.size
        y0, y1 = max(0, int((top - PAD) * h)), min(h, int((bot + PAD) * h))
        if y1 <= y0:
            continue
        name = f"taylor-{prob.replace('.', '_')}-{i + 1}.png"
        AS.trim_margins(im.crop((0, y0, w, y1))).save(out_dir / name)
        out.setdefault(prob, []).append(f"answer-images/{name}")
    return out


def is_blank(png):
    """True for an all-but-empty scan page (Ch7's in-class p4)."""
    im = Image.open(png).convert("L")
    lo, hi = im.getextrema()
    return lo > 235          # nothing darker than near-white anywhere


def render_pages(pack_dir):
    """Rasterise every solution PDF page once, blank scan pages left out. -> [{path, src, file,
    stem, page, hw}]."""
    if not shutil.which("pdftoppm"):
        return []
    pages = AS.render_pages(pack_dir, P.pdfs(pack_dir, SOL_GLOB), skip=is_blank)
    for pg in pages:
        pg["hw"] = bool(HW_RE.search(pg["file"]))
    return pages


def listed_on(smap, pg):
    items = AS.listed_on(smap, pg)
    return None if items is None else [p for p, _ in items]


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
        smap = notes.solutions_map()
        pages = render_pages(pack)
        crops, claimed = AS.crop_problems(pages, smap)
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
