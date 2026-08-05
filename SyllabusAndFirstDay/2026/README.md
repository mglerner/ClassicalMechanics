# PHY 317 — Fall 2026 (Smith College)

My first time teaching Classical Mechanics. Plan follows Will Raven's
Fall 2025 PHY 317 closely (Taylor, _Classical Mechanics_). Sources in
`../../../SmithPreMichaelArtifacts/`: `PHY317 F2025 Syllabus.pdf` and
`WillClassicalCalendar.docx`.

## Files here

- `PHY317 F2026 Calendar.xlsx` — draft course calendar (same format as my
  other course calendars). Import into Google Sheets (File > Import >
  Upload) and embed in Moodle.
- `make_fall2026_calendar.py` — regenerates the xlsx; edit `CONTENT` /
  `EXAMS` and rerun. Preflight checks hard-fail if slots don't match the
  39 class meetings, if an exam drifts off a Monday, or if grade
  categories don't total exactly 1000 points.

## Schedule notes

- Will's F2025 calendar had exactly 39 teaching slots; Fall 2026 has
  exactly 39 MWF meetings (Wed Sep 9 - Mon Dec 14), so his sequence maps
  one-to-one. His "Mountain Day holder" trick is kept (Mon Oct 5).
- Exams pinned to Mondays like his: Oct 19 (Ch 2-4), Nov 9 (Ch 5-7),
  Dec 7 (Ch 8, 9, 11). Note his syllabus says Exam 3 covers Ch 8, 9, 11
  but his calendar row said "Ch 9-11" (Ch 10 was never taught); I used
  the syllabus version.
- Final: required Ch 12 problem + optional grade-replacement problems
  (one per exam chapter, replace-if-higher), per Will's design.
- Will's "Prerequisites" column (just-in-time review pointers keyed to
  Knight and to Felder & Felder "Math Methods" chapters) is included in
  the Schedule sheet. His syllabus framing: use it for proactive review
  before class, or "just-after-time" review when a topic is rough.

## Grading (1000 points total)

Will's weights (HW 30%, exams 21% x 3, final 7%) converted to points in
the "Grade Categories" sheet: 13 HW drop 1 @ 25 = 300; 3 exams @ 210 =
630; final 70. Total 1000 (enforced by the generator). Will handled
attendance as grade caps (4 misses -> max B, etc.), not points; decide
whether to keep that or fold attendance into the point total.

## Assumptions to verify

- MWF meeting pattern (same caveat as PHY 210).
- Will used **Mathematica**; I lean Python. Decide before adapting his
  materials (his archive: `~/Dropbox/__Smith/Classes/317-Classical/`,
  including Seth Hopper's older course — exploring that is deferred).
- Mountain Day is TBA; the Mon Oct 5 holder is a guess at where it lands.

## Course machinery

- LMS: Moodle. Private materials go in `../../private/` ->
  `~/Dropbox/__Smith/Classes/317-Classical/private/` (gitignored symlink).
