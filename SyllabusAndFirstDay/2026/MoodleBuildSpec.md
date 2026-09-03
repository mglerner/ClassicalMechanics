# PHY 317 F2026 Moodle build spec

Companion to PHY 210's `MathematicalPhysics/SyllabusAndFirstDay/2026/
MoodleBuildSpec.md`; same decisions wherever the courses overlap, so the
two Moodle pages read as one instructor's. Decisions encoded 2026-09-02.

Build our OWN course in the F2026 shell. Do NOT restore Will Raven's
F2025 backup (`private/WillF2025/MoodleCourse/`): it stays a reference
archive. Two reasons beyond the PHY 210 precedent: (1) his shell posts
the full 808-page Taylor scan and 22 Instructor-Solutions-Manual excerpt
PDFs, none of which we can carry forward (copyright); (2) his gradebook
was a flat 1300-point HW sum with exams kept on paper, and ours is the
1000-point scheme with categories. Organize by CHAPTER (Will did; topic
sections age better than week sections when the schedule slips), and
make every deadline a native Moodle assignment so it lands on the
students' Moodle calendar.

## Course settings

- Format: **Collapsed Topics** (what Smith has; no format_tiles).
- `showactivitydates`: YES. Completion tracking ON, manual completion
  boxes on assignments. Hidden sections completely invisible.
- Blocks: Announcements forum (default), Calendar, Timeline. No other
  forums.

## Sections (Collapsed Topics)

As built 2026-09-03 (Michael made 0-2 by hand; the mbz creates 3-13):

0. **General** -- syllabus (the GitHub raw link to `PHY317Syllabus.pdf` on
   main, so commits update it live); the Course Calendar Page (schedule
   embed, below); posit.smith.edu pointer; office-hours info; Will's "AI
   prompts for students" PDF (a department document); anonymous feedback
   via a Moodle Feedback activity (anonymous, multiple submissions, one
   open textarea); the week-1 office-hours scheduling poll (temporary);
   and the SECOND Feedback activity, **mid-semester feedback** (decided
   2026-08-25, both courses), hidden until fall break, at least these
   three textarea questions:
   1. What's working well?
   2. What's not working well, and how can the instructor make things
      better?
   3. What can you, as the student, do to make the class better?
1. **Homework** -- the 13 HW assignments. Section name carries NO dates
   (Michael, 2026-09-03: the assignments already carry them). NO section
   summary anywhere (merge restores reinstate stale summaries).
2. **Exams** -- the three exam assignments + the final; practice
   problems / solutions as each exam approaches.
3. **Ch 1: Newton's laws**
4. **Ch 2: Projectiles and charged particles**
5. **Ch 3: Momentum and angular momentum**
6. **Ch 4: Energy**
7. **Ch 5: Oscillations**
8. **Ch 6: Calculus of variations**
9. **Ch 7: Lagrange's equations**
10. **Ch 8: Two-body central-force problems**
11. **Ch 9: Mechanics in non-inertial frames**
12. **Ch 11: Coupled oscillators and normal modes** (+ a pointer to
    Felder Ch 6 / the PHY 210 page for the eigenvector prerequisite; Will
    embedded his own PHY 210 decks here)
13. **Ch 12: Nonlinear mechanics and chaos**

Per-chapter sections hold: the posted class-notes PDFs (GoodNotes
exports after each class, Will's "updated with class markings"
practice), the Python notebooks (ported from Will's Mathematica
notebooks where they are worth porting; Will's .nb files posted as
optional extras for students who have Mathematica), and the PCCI
statement for each day if it is not simply a Taylor problem number.

What is deliberately NOT posted, from Will's shell: the Taylor scan;
the Look-At / In-Class "solutions" PDFs (ISM excerpts -- use them to
PREPARE, post our own worked solutions in our own hand instead); his
personal Google appointment-booking link.

## Schedule embed (same design as PHY 210)

The generator writes the "Schedule" tab as TWO CHUNKS split at fall
break and prints the ranges on every run; current build:
chunk 1 = `A1:I16` (Sep 9 - Oct 12), chunk 2 = `A17:I46` (Oct 14 on).
Note the extra Prerequisites column: ranges run to column **I**, not H.

- Convert the xlsx to a Google Sheet ONCE; afterwards update ONLY via
  File -> Import -> Upload -> "Replace spreadsheet" (a fresh convert
  mints a new document id and orphans the published URL).
- Publish to web -> Embed -> Schedule tab; auto-republish ON; access
  restriction OFF.
- Course Calendar Page = iframe of the published URL + `&range=A1:I16`,
  width 100%, height ~800, plus a plain link to the unranged URL
  labeled "full-semester calendar".
- AT FALL BREAK (Tue Oct 13): change the range parameter to `A17:I46`
  and open the mid-semester feedback activity. Reminder lives in
  TODO.md and the class-15 prep pack when built; NOT a Moodle calendar
  event (student-visible).

## Assignments (all native Moodle; this IS the calendar)

Common settings: **file submission, max 1 file, `.pdf` only**; online
text OFF (the PHY 210 reflection-question machinery is for a 19-student
good-faith-graded course; here nine students' homework is graded on
correctness and the reflections are Will's resubmission reflections,
which arrive on paper with the next set). Feedback = comments +
annotate PDF; no cutoff date; `submissiondrafts=0`; grade category per
below. Same visibility rule as PHY 210: each assignment is hidden by a
Restrict-access DATE condition until 1.5 weeks before it is due, so a
pacing change never leaves a stale problem list on display.

| Assignment | Due               | Pts | Notes                                                                               |
| ---------- | ----------------- | --- | ----------------------------------------------------------------------------------- |
| HW01..HW13 | see generator     | 25  | Wednesdays 22:00; HW06 Fri Oct 23, HW11 Mon Nov 23, HW12 Fri Dec 4, HW13 Wed Dec 16 |
| Exam 1     | Mon Oct 19, 13:40 | 190 | no submission; Ch 2-4                                                               |
| Exam 2     | Fri Nov 13, 13:20 | 190 | no submission; Ch 5-7                                                               |
| Exam 3     | Mon Dec 7, 13:40  | 190 | no submission; Ch 8, 9, 11                                                          |
| Final exam | Tue Dec 22, 15:00 | 60  | no submission; required Ch 12 problem; timestamp = end of the self-scheduled window |

One due TIME everywhere: 22:00 (Will's drifted between 18:00, 22:00
and 23:59 within one semester; pick one, keep it).

HW description template (per week): one standing preamble (problems
from Taylor 2005; work together, write it up yourself; one PDF; the
rubric in one line with a link to the syllabus) + the week's problem
list with Will's hints + any custom problem in full + the computational
problem's Python note (starter notebook link) + the turn-in line.
Paste-ready HTML for all 13 lives in `private/MoodleBuild/
hw-descriptions.html` once written (build task).

## Gradebook (mirrors the 1000-point scheme, natively)

Categories (aggregation Natural):
- Participation & PCCIs -- 70 pts; graded on paper; two manual items
  ("Participation through fall break" /25, "Participation after fall
  break" /45 -- the 70 split in proportion to 14 and 25 class days; the
  four drops are handled on the paper tally, as in PHY 210).
- Weekly homework -- 13 x 25, **droplow = 1** on the category.
- Exams -- 3 assignments @ 190.
- Final exam -- 1 assignment @ 60.
Total 1000; verify against the generator's Grade Categories sheet.

Redemption bookkeeping: keep PER-PROBLEM exam scores in a private
spreadsheet (three per exam, ~63 pts each); the Moodle exam item holds
the sum. After the final, edit the Moodle exam items upward where a
redemption problem beat the original. The same lesson as PHY 210:
per-problem records from day one, or the redemption final cannot be
scored.

## Build mechanics (read PHY 210's private/MoodleBuild/README.md first)

Everything hard-won there applies verbatim: MERGE-ONLY restores (delete
mode destroyed the teacher role assignment and Smith's backups can
never put one back); mbz built with Python `tarfile` in ustar format
with a regenerated `.ARCHIVE_INDEX` first and the double-quoted XML
declaration; never rehearse in a sandbox course; restore exactly once;
the mbz must carry no section summaries.

DONE 2026-09-03: Michael built sections 0-2 and the two exemplar
assignments in the shell (course 57083) and dropped the -nu backup in
`private/MoodleBuild/`; `build_317.py` produced
`PHY317-F2026-course.mbz`, one merge-only file with the 11 chapter
sections, the 4 grade categories + 2 participation items, and all 17
assignments. Two things differ from the 210 build and make this a single
file: the shell has one grade category, so Moodle's gradebook restore
step runs on merge and creates ours; and a merge restore creates section
numbers that do not exist in the target. The restore protocol and the
two-number gate (0 before, 1000 after) are in that directory's README.

## Deliberately NOT doing

- No restore of Will's .mbz; no Taylor scan; no ISM excerpts; no
  Google Forms; no extension-request form (late passes by email); no
  seminar-attendance bonus (Will's +0.5 per seminar has no home in a
  points scheme -- revisit if the department expects it); no Library
  Research Guide LTI unless it resolves on its own.
