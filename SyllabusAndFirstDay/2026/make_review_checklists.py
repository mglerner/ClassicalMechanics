"""Per-class-day review checklists for the prep packs (PHY 317).

Michael's standing rule (2026-09-07): every PCCI and every in-class
problem must be reviewed BEFORE the class it appears in, and every
homework SOLUTIONS must be finalized and hand-reviewed by Michael before
the set goes live (ideal) and no later than the first class after it
goes live (mandatory: students may ask about it in that class)
(assigned = the day the Moodle assignment becomes visible, 10.5 days
before it is due). This script enumerates those problems per day from
the calendar generator -- PCCI, CHAPTER_PROBLEMS, HWS -- so the lists
stay correct when the assignments change. The in-class problems come
from the pack's own plan (the `## In-class problems` section of its
notes; packnotes.Notes) when it has one, else from Will's
CHAPTER_PROBLEMS menu. Rerun after any generator edit or pack-notes
edit:

    python make_review_checklists.py

Writes `review-checklist.md` into every existing prep-pack folder's build
directory (packnotes.layout()["build"]: `.build/`, or `_gen/` in old-layout
packs; matched by the NN- class-number prefix, checked against the date)
and the whole-semester `REVIEW-SCHEDULE.md` at the prep-pack root. Both
are generated files; do not edit them by hand.
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_fall2026_calendar as CAL  # noqa: E402
sys.path.insert(0, str(Path.home() / "coding/courses/shared"))
import coverage_gate as GATE              # noqa: E402
import packnotes as PN                    # noqa: E402

# Coverage gate (2026-10-01): a week before each set goes live, the checklist asks for
# /coverage-check; at go-live it prints the mechanical gate (verdict on file, links exist,
# notebook linked when the set needs a computer). See shared/coverage_gate.py.
DESCRIPTIONS = GATE.description_blocks(Path.home() / "coding/courses/ClassicalMechanics/private/MoodleBuild/hw-descriptions.html")
SOLUTIONS = Path.home() / "coding/courses/ClassicalMechanics/private/Solutions"

PACKS = Path.home() / "coding/courses/ClassicalMechanics/private/F2026PrepPacks"
AVAILABLE_DAYS_BEFORE = 10.5          # build_317.py
FIRST_CLASS = date(2026, 9, 9)

# ------------------------------------------------------------ logistics
# The bring / set-up list is checklist material (a checkbox, not prose),
# so it lives here as data rather than in the hand-written prep notes.
EVERY_DAY = [
    "iPad",
    "Voting cards",
]
# date -> items specific to that day
DAY_LOGISTICS = {
    date(2026, 9, 9): ["Printed photo roster (private/Roster/PHY317-F2026-roster.pdf)",
                       "Printed syllabus, one per student (9) + a spare",
                       "PRINT the voting cards, one set per student (shared/VotingCardLandscape.pdf)"],
    date(2026, 9, 11): ["Chalk and whiteboard markers (board work: 1.43, the skateboard)",
                        "Students' LAPTOPS (announced Wednesday) for the ten-minute jupyterhub walkthrough",
                        "Your own laptop logged into jupyterhub.smith.edu with the HW01 notebook already uploaded",
                        "Check HW01 is visible on Moodle and its notebook link (GitHub) opens"],
    date(2026, 10, 16): ["Exam 1: printed copies + a spare; per-problem score sheet ready"],   # exam moved to Oct 16 on 2026-09-24
    # Exam hand-backs (Michael 2026-10-04): the redo is one PDF on Moodle, due at the start of class one
    # week after the hand-back rounded to the next class day; the 'Exam N redo' item comes from
    # build_add_317.py examN-redo (a restore-only merge). Edit its dates if the hand-back moves.
    date(2026, 10, 19): ["Hand back the graded Exam 1 papers; redos go on Moodle as one PDF, due Mon Oct 26 at the "
                         "start of class. The 'Exam 1 redo' Moodle item must already exist (build_add_317.py exam1-redo)."],
    date(2026, 11, 16): ["Exam 2: printed copies + a spare; per-problem score sheet ready"],   # exam is Mon Nov 16
    date(2026, 11, 18): ["Hand back the graded Exam 2 papers; redos go on Moodle as one PDF, due Mon Nov 30 at the "
                         "start of class (no class Nov 25/27). The 'Exam 2 redo' Moodle item must already exist "
                         "(build_add_317.py exam2-redo)."],
    date(2026, 12, 7): ["Exam 3: printed copies + a spare; per-problem score sheet ready"],
    date(2026, 12, 9): ["Hand back the graded Exam 3 papers; redos go on Moodle as one PDF, due Wed Dec 16 at 13:20 "
                        "(one week; after the last class, Mon Dec 14 -- Michael to confirm). The 'Exam 3 redo' Moodle item "
                        "must already exist (build_add_317.py exam3-redo)."],
    date(2026, 12, 11): ["iPad with the folio keyboard (AirPlay as usual) for the driven-pendulum notebook; students bring laptops"],
}


def fmt(d):
    return d.strftime("%a %b %-d")


def chapter_of(reading):
    m = re.match(r"(?:Ch\.?\s*)?(\d+)", reading.strip())
    return int(m.group(1)) if m else None


def class_rows():
    """[(class_no, date, topic, reading, chapter, chapter_day)] for content
    days; exam days carry chapter None."""
    days = list(CAL.class_days())
    # The calendar build()'s guards, repeated here because the consumers of class_rows() never run
    # build(): an extra CONTENT row would silently drop off the end, a misdated exam would be
    # treated as content (too FEW rows is loud: next() raises StopIteration).
    assert len(CAL.CONTENT) + len(CAL.EXAMS) == len(days), (
        f"{len(CAL.CONTENT)} content + {len(CAL.EXAMS)} exams for {len(days)} class meetings")
    assert all(d in days for d in CAL.EXAMS), "exam not on a class day"
    assert all(d in days for d in CAL.LAPTOP_DAYS), "LAPTOP_DAYS names a non-class day"
    content = iter(CAL.CONTENT)
    seen = {}
    rows = []
    for i, d in enumerate(days):
        if d in CAL.EXAMS:            # EXAMS keyed by date since 2026-09-24
            rows.append((i + 1, d, CAL.EXAMS[d][0], "", None, None))
            continue
        topic, reading, _ = next(content)
        ch = chapter_of(reading) if reading else None
        if ch is not None:
            seen[ch] = seen.get(ch, 0) + 1
        rows.append((i + 1, d, topic, reading, ch, seen.get(ch) if ch else None))
    return rows


def hw_events():
    """[(hw, visible_date, due, covers, problems)]"""
    out = []
    for hw, due, through, chapters, covers, problems in CAL.HWS:
        vis = max(due - timedelta(days=AVAILABLE_DAYS_BEFORE), FIRST_CLASS)
        out.append((hw, vis, due, covers, problems))
    return out


def pack_plan(pack):
    """(problems, notes path relative to the pack) from the pack's `## In-class problems` section;
    ([], None) when there is no pack, no notes, or old-format (timed-plan) notes."""
    if pack is None:
        return [], None
    notes = PN.layout(pack)["notes"]
    if not notes.exists():
        return [], None
    N = PN.Notes(notes)
    if N.old_format:
        return [], None
    return N.inclass_problems(), notes.relative_to(pack)


def checklist(row, all_rows, hws, pack=None):
    n, d, topic, reading, ch, chday = row
    lines = [f"# Review checklist -- class {n:02d}, {fmt(d)} -- {topic}", "",
             "GENERATED by SyllabusAndFirstDay/2026/make_review_checklists.py from",
             "the calendar generator; rerun it after any change to PCCIs, in-class",
             "lists, homework, or the logistics table. Do not edit by hand.",
             "CHECKLIST = everything that is a checkbox (review items, deadlines,",
             "bring/set-up). PREP NOTES = the judgment (sources, errata, pacing).", ""]
    # ---- before class
    lines += ["## Before class (review these yourself first)", ""]
    pcci = CAL.PCCI.get(d)
    lines.append(f"- [ ] PCCI due today: **{pcci}**" if pcci else "- [ ] PCCI due today: none")
    plan, rel = pack_plan(pack)
    # The pack's plan is what gets worked (prep process 2026-10-03); Will's list is a menu, used
    # only when the pack has no plan to read (no pack, old-format notes, or no problem numbers).
    plan_line = (f"- [ ] In-class problems today (the `## In-class problems` section of `{rel}`): "
                 + ", ".join(f"**{p}**" for p in plan)) if plan else None
    if d in CAL.EXAMS:
        lines.append("- [ ] EXAM DAY: the exam worked through end to end, every version you are printing")
    elif ch is not None and ch in CAL.CHAPTER_PROBLEMS:
        cp = CAL.CHAPTER_PROBLEMS[ch]
        # Ch 1's lists are not split by day in Will's PDFs (one list for
        # both days); a single-list chapter shows the whole list every day.
        def day_list(key):
            lst = cp[key]
            if len(lst) == 1:
                return lst[0], " (whole-chapter list; not split by day)"
            return (lst[chday - 1] if chday - 1 < len(lst) else []), ""
        ic, note = day_list("inclass")
        la, _ = day_list("lookat")
        lines.append(plan_line or "- [ ] In-class problems today: "
                     + (", ".join(f"**{p}**" for p in ic) + note if ic else "none listed"))
        others = [p for p in la if not pcci or p not in pcci]
        if others:
            lines.append("- [ ] Other look-at problems for today (solutions to post): " + ", ".join(others))
    elif plan_line:
        lines.append(plan_line)
    else:
        lines.append("- [ ] In-class problems today: none (not a content day)")
    # next PCCI, announced today
    later = [r for r in all_rows if r[1] > d and CAL.PCCI.get(r[1])]
    if later:
        nd = later[0][1]
        lines.append(f"- [ ] Next PCCI (on the Moodle schedule, due {fmt(nd)}; review it now): {CAL.PCCI[nd]}")
    # ---- homework
    lines += ["", "## Homework (solutions finalized + hand-reviewed: ideally before go-live, MANDATORY by the first class after)", ""]
    next_class = min([r[1] for r in all_rows if r[1] > d], default=None)
    prev_class = max([r[1] for r in all_rows if r[1] < d], default=None)
    any_hw = False
    class_dates = [r[1] for r in all_rows]
    for hw, vis, due, *_ in hws:
        if vis >= GATE.GATE_START and GATE.coverage_day(vis, class_dates) == d and vis > d:
            any_hw = True
            lines += GATE.checklist_lines(f"HW{hw:02d}", vis, due, d, DESCRIPTIONS.get(hw, ""),
                                          SOLUTIONS / f"HW{hw:02d}", None, fmt)
    for hw, vis, due, covers, problems in hws:
        goes_live_now = (prev_class is None and vis <= d) or (prev_class is not None and prev_class < vis <= d)
        if goes_live_now:
            any_hw = True
            lines += [f"- [ ] **HW{hw:02d} goes live {fmt(vis)}: solutions FINALIZED and hand-reviewed, "
                      f"MANDATORY by class today** (due {fmt(due)}). Covers {covers}.",
                      f"      Problems: {problems}"]
            if vis >= GATE.GATE_START:
                lines += GATE.golive_lines(f"HW{hw:02d}", DESCRIPTIONS.get(hw, ""), SOLUTIONS / f"HW{hw:02d}", None)
        if next_class is not None and d < vis <= next_class:
            any_hw = True
            lines += [f"- [ ] HW{hw:02d} goes live {fmt(vis)}, before the next class: finalize and "
                      f"hand-review its solutions NOW (the ideal deadline). Covers {covers}.",
                      f"      Problems: {problems}"]
        if due == d:
            any_hw = True
            lines.append(f"- HW{hw:02d} is DUE today 10:00 PM.")
        if CAL.HW_GRACE.get(hw) == d:          # Moodle Cut-off; the solutions open then (moodle_audit)
            any_hw = True
            lines.append(f"- HW{hw:02d} grace cut-off today 10:00 PM (solutions open then).")
    for ed, label in CAL.EXTRA_DUE.items():
        if ed == d:
            any_hw = True
            lines.append(f"- {label} today.")
    if not any_hw:
        lines.append("- nothing new goes live or comes due today")
    # ---- bring / set up
    lines += ["", "## Bring / set up", ""]
    if d in CAL.LAPTOP_DAYS:
        lines.append("- [ ] **Students bring LAPTOPS today (tagged on the Moodle schedule)**")
    for item in DAY_LOGISTICS.get(d, []):
        lines.append(f"- [ ] **{item}**")
    for item in EVERY_DAY:
        if any(item.lower() in x.lower() for x in DAY_LOGISTICS.get(d, [])):
            continue          # a bold day-specific line already covers it
        lines.append(f"- [ ] {item}")
    return "\n".join(lines) + "\n"


def main():
    rows = class_rows()
    hws = hw_events()
    packs = {int(p.name[:2]): p for p in PACKS.iterdir()
             if p.is_dir() and re.match(r"\d\d-", p.name)}
    # Guard (2026-10-04): a pack's number must be the calendar's number for its date. Otherwise a
    # lost meeting (Mountain Day) sends class N's checklist into another day's folder.
    by_date = {r[1].isoformat(): r[0] for r in rows}
    for n, p in sorted(packs.items()):
        assert by_date.get(p.name[3:13]) == n, (
            f"pack {p.name}: the calendar numbers {p.name[3:13]} as class {by_date.get(p.name[3:13])}, the folder says {n}")
    written = 0
    sched = ["# Review schedule, whole semester (PHY 317 F2026)", "",
             "GENERATED by make_review_checklists.py; rerun after any generator edit.",
             "Rule: PCCIs and in-class problems reviewed BEFORE the class; HW solutions",
             "finalized and hand-reviewed before the set goes live (ideal), MANDATORY by",
             "the first class after it goes live.", ""]
    for row in rows:
        n = row[0]
        text = checklist(row, rows, hws, packs.get(n))
        if n in packs:
            build = PN.layout(packs[n])["build"]
            build.mkdir(exist_ok=True)
            (build / "review-checklist.md").write_text(text)
            written += 1
        body = text[text.index("## Before class"):]          # drop the title + header note
        sched += [f"## Class {n:02d} -- {fmt(row[1])} -- {row[2]}", "", body.strip(), ""]
    (PACKS / "REVIEW-SCHEDULE.md").write_text("\n".join(sched))
    print(f"wrote REVIEW-SCHEDULE.md ({len(rows)} days) and {written} pack checklists")


if __name__ == "__main__":
    main()
