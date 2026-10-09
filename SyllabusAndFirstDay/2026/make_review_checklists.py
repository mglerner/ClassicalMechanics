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
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "shared"))
import courses as C                       # noqa: E402
import coverage_gate as GATE              # noqa: E402
import fall2026_calendar as TERM          # noqa: E402
import packnotes as PN                    # noqa: E402
import review_checklists as RC            # noqa: E402

# Coverage gate (2026-10-01): a week before each set goes live, the checklist asks for
# /coverage-check; at go-live it prints the mechanical gate (verdict on file, links exist,
# notebook linked when the set needs a computer). See shared/coverage_gate.py.
DESCRIPTIONS = GATE.description_blocks(C.moodlebuild("317") / "hw-descriptions.html")
SOLUTIONS = C.private("317") / "Solutions"


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


fmt = RC.fmt


def chapter_of(reading):
    m = re.match(r"(?:Ch\.?\s*)?(\d+)", reading.strip())
    return int(m.group(1)) if m else None


def class_rows():
    """[(class_no, date, topic, reading, chapter, chapter_day)] from the calendar's rows() (flex days and
    slips applied); exam days and flex days carry chapter None."""
    seen, out = {}, []
    for r in CAL.rows():
        if r["kind"] == "assessment":
            out.append((r["n"], r["date"], r["topic"], "", None, None))
            continue
        ch = chapter_of(r["reading"]) if r["reading"] else None
        if ch is not None:
            seen[ch] = seen.get(ch, 0) + 1
        out.append((r["n"], r["date"], r["topic"], r["reading"], ch, seen.get(ch) if ch else None))
    return out


def hw_events():
    """[(hw, visible_date, due, covers, problems)]"""
    out = []
    for hw, due, through, chapters, covers, problems in CAL.HWS:
        vis = max(due - timedelta(days=TERM.AVAILABLE_DAYS_BEFORE), TERM.FIRST_DAY)
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
    lines = RC.header(n, d, topic, ["the calendar generator; rerun it after any change to PCCIs, in-class",
                                    "lists, homework, or the logistics table. Do not edit by hand."])
    # ---- before class
    lines += RC.before_class(d, CAL.PCCI)
    pcci = CAL.PCCI.get(d)
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
    lines += RC.next_pcci(d, all_rows, CAL.PCCI)          # next PCCI, announced today
    lines += RC.homework(d, all_rows, hws, "HW", lambda hw, covers, problems: (covers, [f"      Problems: {problems}"]),
                         DESCRIPTIONS, SOLUTIONS, CAL.EXTRA_DUE, grace=CAL.HW_GRACE)
    lines += RC.bring(d, CAL.LAPTOP_DAYS, DAY_LOGISTICS, EVERY_DAY)
    return "\n".join(lines) + "\n"


def main():
    RC.write_all("317", class_rows(), hw_events(), checklist, "HW")


if __name__ == "__main__":
    main()
