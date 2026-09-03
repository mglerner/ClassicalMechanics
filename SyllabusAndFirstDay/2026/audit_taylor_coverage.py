"""Coverage audit: is every assigned Taylor problem taught before it is due?

The Taylor PDF we have (Will's scan) has no text layer, so the problem-set
pages were OCR'd once (private/TaylorOCR/ocr.sh: pdftoppm + tesseract,
PDF page = book page + 15). This script reads those page texts, recovers
Taylor's "SECTION n.m" headers inside each chapter's problem set, maps
every problem number to its section, maps every section to the first
class day whose reading covers it (from make_fall2026_calendar.CONTENT),
and checks each homework problem against its due date.

Usage: python audit_taylor_coverage.py          (prints a table; exit 1 on
       any problem taught on/after its due date or not taught at all)
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_fall2026_calendar as CAL  # noqa: E402

OCR = Path.home() / "coding/courses/ClassicalMechanics/private/TaylorOCR"
PAGES = range(16, 536)

# ------------------------------------------------------------ OCR -> sections
def load_problem_sections():
    """Return {(ch, n): section 'ch.m'} for every problem line found in the
    problem-set pages, plus the list of (ch, m, first_problem) headers."""
    prob_section = {}
    headers = []
    chapter = None
    section = None
    for pg in PAGES:
        f = OCR / f"p{pg}.txt"
        if not f.exists():
            continue
        text = f.read_text(errors="replace")
        # running header on problem pages: "Problems for Chapter 7   285"
        m = re.search(r"Problems for Chapter\s*(\d+)", text)
        if m:
            chapter = int(m.group(1))
            if section is None or int(section.split(".")[0]) != chapter:
                section = None
        elif chapter is not None and re.search(r"CHAPTER\s*\d+", text):
            # a new chapter's opening page ends the previous problem set
            chapter = None
            section = None
        if chapter is None:
            continue
        for line in text.splitlines():
            s = re.match(r"\s*SECTION\s*(\d+)\s*[.,]\s*(\d+)", line, re.I)
            if s and int(s.group(1)) == chapter:
                section = f"{chapter}.{int(s.group(2))}"
                headers.append((chapter, int(s.group(2)), None))
                continue
            p = re.match(r"\s*(\d+)\s*[.,]\s*(\d+)\s*(?:\*|★|x|\W)", line)
            if p and int(p.group(1)) == chapter:
                n = int(p.group(2))
                if 1 <= n <= 80 and (chapter, n) not in prob_section:
                    prob_section[(chapter, n)] = section or f"{chapter}.1"
                    if headers and headers[-1][2] is None and headers[-1][0] == chapter:
                        headers[-1] = (chapter, headers[-1][1], n)
    return prob_section, headers

# ------------------------------------------------------ readings -> dates
def sections_in(reading):
    """'2.1-2.2' -> {'2.1','2.2'}; '7.5, 7.8, 7.10' -> {...}; 'Ch. 1' -> ('chapter', 1)."""
    out = set()
    chapters = set()
    for tok in re.split(r"[;,]", reading):
        tok = tok.strip()
        m = re.match(r"Ch\.?\s*(\d+)", tok)
        if m:
            chapters.add(int(m.group(1))); continue
        m = re.match(r"(\d+)\.(\d+)\s*-\s*(\d+)\.(\d+)", tok)
        if m:
            c, a, c2, b = map(int, m.groups())
            assert c == c2, tok
            out |= {f"{c}.{k}" for k in range(a, b + 1)}; continue
        m = re.match(r"(\d+)\.(\d+)$", tok)
        if m:
            out.add(f"{int(m.group(1))}.{int(m.group(2))}")
    return out, chapters

def first_teach_dates():
    days = list(CAL.class_days())
    exam_slots = set(CAL.EXAMS)
    content = iter(CAL.CONTENT)
    first = {}
    whole_chapter = {}
    for i, d in enumerate(days):
        if i in exam_slots:
            continue
        topic, reading, prereq = next(content)
        secs, chapters = sections_in(reading)
        for s in secs:
            first.setdefault(s, d)
        for c in chapters:
            whole_chapter.setdefault(c, d)
    return first, whole_chapter

# ---------------------------------------------------------------- the audit
def assigned_problems(problems):
    """Problem numbers in an HWS 'problems' string, ignoring bracketed hints
    (which cite in-class problems), expanding 'a.b-a.c' ranges."""
    s = re.sub(r"\[.*?\]", "", problems)
    out = []
    for m in re.finditer(r"(\d+)\.(\d+)(?:\s*-\s*(\d+)\.(\d+))?", s):
        c, a = int(m.group(1)), int(m.group(2))
        if m.group(3):
            for n in range(a, int(m.group(4)) + 1):
                out.append((c, n))
        else:
            out.append((c, a))
    return out

def main():
    prob_section, headers = load_problem_sections()
    first, whole_chapter = first_teach_dates()
    # sanity anchors read by eye from the book (2026-09-03)
    anchors = {(7, 46): "7.8", (7, 48): "7.9", (7, 50): "7.10", (7, 17): "7.5",
               (7, 27): "7.5", (7, 45): "7.8"}
    for k, v in anchors.items():
        got = prob_section.get(k)
        print(f"anchor {k[0]}.{k[1]}: OCR says {got}, book says {v}"
              + ("" if got == v else "   <-- MISMATCH"))
    print(f"problems mapped: {len(prob_section)}; section headers seen: {len(headers)}")

    bad = 0
    print(f"\n{'HW':5} {'due':11} {'problem':8} {'section':8} {'taught':11} status")
    for hw, due, through, chapters, covers, problems in CAL.HWS:
        for (c, n) in assigned_problems(problems):
            sec = prob_section.get((c, n))
            if sec is None:
                status, taught = "UNMAPPED (OCR miss)", None
            else:
                taught = first.get(sec) or whole_chapter.get(int(sec.split(".")[0]))
                if taught is None:
                    status = "SECTION NEVER TAUGHT"
                elif taught >= due:
                    status = "TAUGHT ON/AFTER DUE"
                elif taught == through and (due - through).days < 2:
                    status = "ok (tight)"
                else:
                    status = "ok"
            if not status.startswith("ok"):
                bad += 1
            print(f"HW{hw:02d}  {due.strftime('%a %b %-d'):11} {c}.{n:<6} {sec or '?':8} "
                  f"{taught.strftime('%a %b %-d') if taught else '-':11} {status}")
    print(f"\n{bad} problems flagged")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
