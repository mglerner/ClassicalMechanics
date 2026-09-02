# PHY 317 -- Fall 2026 (Smith College)

My first time teaching Classical Mechanics. Plan-of-record: follow Will
Raven's Fall 2025 PHY 317 closely (Taylor, _Classical Mechanics_, 2005)
-- his pacing, topic selection, and homework sets -- with Python in
place of his Mathematica wherever feasible. Seth Hopper's Earlham
PHYS 425 archive is an idea-and-example quarry, not a second plan.

Sources: `../../../SmithPreMichaelArtifacts/` (`PHY317 F2025 Syllabus.pdf`,
`WillClassicalCalendar.docx`) and, richer, Will's full Moodle backup
extracted at `../../private/WillF2025/MoodleCourse/extracted/`
(`structure.txt` is the course map; 13 HW sets + solutions, 11 skeleton
slide decks with class ink, per-day in-class problem records, 22
Mathematica notebooks).

## Files here

- `make_fall2026_calendar.py` -- **the source of truth** for every date.
  Regenerates the xlsx; edit `CONTENT` / `EXAMS` / `HWS` / `PCCI` /
  `cats` and rerun:
  `python make_fall2026_calendar.py "PHY317 F2026 Calendar.xlsx"`
  (the `courses/` uv venv; direnv activates it). Preflight guards
  hard-fail if slots don't match the 39 meetings, if an exam lands off
  Mon/Fri, if any HW is due on or before the class it draws on, on a
  no-class or exam day, or after the exam that covers its chapters, or
  if grade categories don't total exactly 1000.
- `PHY317 F2026 Calendar.xlsx` -- the generated calendar: "Schedule"
  (two chunks split at fall break, for the Moodle embed; the script
  prints the ranges), "HW Problem Lists", "Grade Categories".
- `PHY317Syllabus.tex` / `.pdf` -- the syllabus, in Seth Hopper's
  PHYS 425 layout (margin section titles; `seth-preamble.tex` is his
  preamble, itself the public "Simple LaTeX CV Template") rather than
  PHY 210's tufte-handout, for some style diversity. No prose preamble
  (decided 2026-09-02). Will Raven's AI statement, prompts, and example
  homework problem are reused with credit; the example is redone in
  Python (SymPy). Build: `pdflatex` twice (delete stale `.aux` if
  switching from the old tufte build).
- `make_syllabus_figures.py` (`brachistochrone.pdf`, `chaos_pendulum.pdf`)
  -- margin figures from the earlier tufte version; no longer in the
  syllabus, kept as slide assets.
- `MoodleBuildSpec.md` -- the Moodle course design (sections, assignments,
  gradebook, schedule embed, build protocol). Companion to PHY 210's.
- `TODO.md` -- the living task list; decisions and open items live THERE.

## Schedule (decided 2026-09-02)

- Will's 39 F2025 slots map one-to-one onto Fall 2026's 39 MWF meetings
  (Wed Sep 9 - Mon Dec 14). His Mountain Day holder is kept (Mon Oct 5).
- Exams: **Mon Oct 19** (Ch 2-4), **Fri Nov 13** (Ch 5-7), **Mon Dec 7**
  (Ch 8, 9, 11). Exam 2 moved off Will's Monday to the Friday so the
  Ch 7 homework can precede it without two sets landing two days apart,
  and so a review day sits right before it (as one already does before
  Exam 3). Final = required Ch 12 problem + nine optional redemption
  problems, per Will's design.
- Homework: Will's 13 sets kept intact; **due Wednesdays 10:00 PM**,
  covering the previous Mon/Wed/Fri. Our semester opens on a Wednesday,
  so Will's Friday deadlines would have landed on the last teaching day
  of each block. One-offs: HW06 Fri Oct 23, HW11 Mon Nov 23, HW12 Fri
  Dec 4, HW13 Wed Dec 16 (reading period).
- The double-pendulum day and the pre-Exam-3 catch-up day are swapped
  relative to Will's order (review day right before the exam).

## Grading (1000 points total, enforced by the generator)

Participation/PCCIs 39 drop 4 @ 2 = 70; HW 13 drop 1 @ 25 = 300; exams
3 @ 190 = 570; final (required Ch 12 problem) 60. Will's proportions
(HW 30%, exams 63%, final 7%) with PHY 210's participation machinery
added on top; each exam problem and the final's problem are worth about
the same (~63 vs 60). Will's attendance grade caps and seminar bonus are
dropped in favor of points.

## Registrar facts (verified 2026-08-17)

PHY 317 01: W/F 1:20-2:35 PM + Mon 1:40-2:55 PM, Sabin-Reed 308, 4 cr,
9 enrolled as of 8/17. Prereqs PHY 210 & 215.

## Course machinery

- LMS: Moodle (design in `MoodleBuildSpec.md`). Programming: Python
  (Jupyter on posit.smith.edu), Mathematica permitted for students who
  prefer it.
- Private materials (solutions, exams, grades, other professors' files)
  go in `../../private/` -> `~/Dropbox/__Smith/Classes/317-Classical/private/`
  (gitignored symlink). Per-day prep packs: `../../private/F2026PrepPacks/`
  (see its README).
