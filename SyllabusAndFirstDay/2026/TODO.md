# PHY 317 Fall 2026: task list

Working list, same conventions as PHY 210's
(`../../../MathematicalPhysics/SyllabusAndFirstDay/2026/TODO.md`).
Plan-of-record: follow Will Raven's F2025 closely -- his pacing, topic
selection, and homework sets -- with Python in place of Mathematica
wherever feasible; Seth Hopper's archive is a quarry for examples and
ideas, not a second plan (reaffirmed by Michael 2026-09-02).

## Decided

- **Follow Will's calendar/pacing/topics** (2026-08-17, reaffirmed
  2026-09-02). Seth = examples and ideas only.
- **Python replaces Mathematica where possible** (2026-09-02).
  Students who know Mathematica may still use it (syllabus says so).
  Porting order of need: HW01's 1.50 [computational] (week 2); the Ch 2
  drag notebooks (week 2); HW13's DDP helper (the one place Mathematica
  is load-bearing; the five Ch 12 class notebooks are the same
  machinery). 21 of Will's 22 notebooks use Manipulate, so ports are
  Jupyter + ipywidgets or plain matplotlib parameter sweeps.
- **HW due Wednesdays 10:00 PM**, covering the previous Mon/Wed/Fri
  (2026-09-02). Our semester opens on a Wednesday, so Will's Friday
  deadlines would land ON each block's last teaching day. One-offs:
  HW06 Fri Oct 23 (Exam 1 Monday), HW11 Mon Nov 23 (Thanksgiving),
  HW12 Fri Dec 4 (before Exam 3), HW13 Wed Dec 16 (reading period).
  All encoded in the generator's `HWS`, with hard-fail guards.
- **Exam dates (revised 2026-09-04, Michael)**: Exam 1 Fri Oct 9
  (Will's exact slot), Exam 2 Wed Nov 11, Exam 3 Mon Dec 7. Rule: an
  exam comes after the last homework on its chapters is RETURNED, so
  HW04 is due Mon Oct 5 (back Wed Oct 7) and HW09 Fri Nov 6 (back Mon
  Nov 9, the review day). Ch 5 days shift one slot later (5.3-5.4 Wed
  Oct 14 ... 5.7-5.8 Mon Oct 19); changing orbits moves to Fri Nov 13,
  after Exam 2 (Ch 8 is not on it). Coverage audit still 0 violations.
  MOODLE IS ALREADY LIVE with the old dates/points: hand edits listed
  in item 16.
- **Grading: 1000 points** (revised 2026-09-04 by Michael, in the
  syllabus and the generator): participation/PCCIs 39 drop 4 @ 3.2 =
  112; HW 13 drop 1 @ 24 = 288; exams 3 @ 180 = 540; final 60. Every
  exam-type problem (3 per exam + the final's required one) is exactly
  60 points. Will's attendance grade caps are OUT for now (Michael has
  asked Will about them and will put them back if he advises it; the
  block is commented out in the syllabus, ready to uncomment). Seminar
  bonus dropped.
- **Late policy = Will's** (Michael's hand edit 2026-09-03): late
  homework at most half credit unless approved beforehand; more than a
  week late not accepted. The 210-style late passes are gone from this
  course. The drops (4 participation days, 1 HW) stay.
- **PCCIs** (2026-09-02): same machinery as 210, sourced from Will's
  "Look-At" problems (his pre-class problems, one per day, easiest star
  where he listed two) or a one-line reading prompt where he had none.
  Every class day except day 1 has one, in the generator.
- **HW graded on correctness with Will's +/check/-/X rubric and his
  reflection-resubmission option** (2026-09-02; in the syllabus). His
  "include an assessment" convention (limiting case / units / known
  result after every answer) is now stated explicitly in the syllabus
  -- his assignment PDFs assume students already know it.
- **HW turn-in = single PDF upload, no online text** (2026-09-02). The
  210 reflection-question machinery is for a 19-student good-faith
  course; here nine students' work is graded on correctness.
- **Add the jackknife problem** (2026-08-17): Michael's towed-trailer
  stability problem (`~/coding/jackknife/jackknife-physics.html`) as a
  custom problem on the Ch 7 constraints set -- HW08 (due Wed Nov 4)
  matches Will's own pattern of custom problems (HW06 RLC, HW07
  tautochrone). TODO: draft the problem-set version.
- **Moodle: build our own course** (2026-09-02; `MoodleBuildSpec.md`).
  No restore of Will's shell (Taylor scan + ISM excerpts + flat
  gradebook). Merge-only, same mechanics as 210.
- **Liouville aside in the chaos unit** (2026-08-24): Fri Dec 11 slot.
  Materials at `../../../FluctuationTheorems/01-classical-mechanics/`
  (unreviewed chat-session output; read before teaching). Budget 25-35
  min of that lecture + 3-4 problems on HW13.
- **Mid-semester anonymous Feedback activity** (2026-08-25, both
  courses): open at fall break; three questions (in the spec).
- **Noether's theorem, simple version** (Michael asked 2026-09-02):
  Taylor 7.8 added to the Mon Nov 2 reading (translation invariance of
  L -> total momentum conserved, with the five-line proof; time
  independence of L -> the Hamiltonian conserved and = T + U for
  natural coordinates; Taylor names Noether explicitly). Taylor 7.46
  (rotational invariance -> L_z conserved) added to HW09. Will never
  assigned 7.8; his only Noether mention was one line of Ch 4 ink
  ("translation invariance -> from Noether's theorem, cons. of
  momentum", slide 24), which is now a forward pointer. Budget ~15 min
  of the Nov 2 class; the PCCI stays 7.17. Ties to the fluctuation
  theorem arc (Hamiltonian, phase space) later.
- Section-label check (2026-09-02): Will's calendar row "7.5, 7.9 --
  Lagrange multipliers" mislabels: in Taylor, multipliers are 7.10 and
  7.9 is magnetic forces (his HW08 has problem 7.10 and nothing from
  section 7.9). Our reading now says 7.5, 7.8, 7.10. CONFIRM when
  building that deck.

## Registrar facts (verified 2026-08-17)

- PHY 317 01: W/F 1:20-2:35 PM + Mon 1:40-2:55 PM, Sabin-Reed 308,
  4 cr, 9 enrolled (as of 8/17). Prereqs PHY 210 & 215. Same MWF days
  as 210, so the 39-meeting mapping holds; every slot is 75 min.

## Before the first class (Wed Sep 9)

1. Syllabus: the one red left is office hours, set after the week-1
   poll (the SAME When2Meet poll as 210's, decided 2026-09-02; Michael
   splits the responses by student name). No course tutors for 317 and
   no physics help room (Michael, 2026-09-02), so no tutor line.
   Syllabus restyled 2026-09-02 in Seth's layout, no prose preamble;
   Will's AI statement + prompts + example problem (now in Python)
   reused with credit. Post to Moodle as the GitHub raw link (master).
2. Moodle shell: settings, sections 0-2 and the exemplars DONE
   2026-09-03; the mbz is built (item 16). Still by hand after the
   restore: syllabus link; the schedule Sheet (convert the xlsx ONCE;
   embed range `A1:I16`, note column I); anonymous + mid-semester
   Feedback; office-hours poll; Will's "AI prompts for students" PDF;
   attach the 1.50 notebook to HW01.
3. Week-1 decks (classes 01, 02) from prep packs 01-02 once their
   `00-prep-notes.md` exist (deck reads in progress 2026-09-02).
4. Zoom recurring meeting for this section (MWF at 1:20/1:40 -- two
   different start times; the web portal handles it; see the 210 TODO
   item 24 for the rig).
5. posit.smith.edu: confirm the 317 students have access; post a
   starter notebook for 1.50 with HW01.

## Open decisions

6. Mountain Day holder is Mon Oct 5 (a guess); HW04 is due that day at
   10 PM regardless (Moodle deadline). If Mountain Day lands on a class
   day, that day's content shifts into the holder.
7. ASK WILL: his exams. NO exam content exists anywhere (not in the
   backup, not in Dropbox). We have the design (3 problems, one per
   chapter, ~25 min each; redemption final with 9 optional problems)
   and zero instruments. Seth's Test 1 (both variants + solutions +
   a commented-out bank of four more Ch 1-4 problems) is at
   `.../Seth/PHYS 425 - Classical mechanics/Tests - Main/Test 1/` --
   take-home 6-hour format, so problems need re-scoping for 75 min.
8. Exam note sheet: one handwritten 8.5x11 both sides (mirrors 210;
   Will's syllabus was silent). Confirm.
9. HW09 keeps Will's 8.2 even though 8.1-8.2 is taught Wed Nov 4 and
   the set is now due FRIDAY Nov 6 (two days; it is the one easy
   problem on the set). Will flagged HW09 as "an intensive homework
   set"; with the Friday due date it also has five days, not seven.
10. Copyright before posting anything of Will's: the 808-page Taylor
    scan and the 22 Look-At/In-Class PDFs (ISM image excerpts) do NOT
    get re-posted. Post our own worked solutions in our own hand.
11. Will's Ch 9 deck taught the Coriolis unit with LATITUDE where Taylor
    uses CO-LATITUDE; caught by a student on 12/07, after the unit. The
    backup deck is the corrected revision, but re-derive from Taylor
    p. 353 (PDF p. 368) before building the Ch 9 decks. HW11's 9.15
    note ("Northampton: latitude 42, colatitude 48") is where to make
    it stick.
12. Seminar bonus (+0.5 final-grade points per physics seminar, max 4)
    has no home in a points scheme. Ask the department whether seminar
    attendance is an expectation for majors in 317; if so, fold it into
    participation somehow.

## Build tasks

13. Prep packs 01-11 (weeks 1-4, through Fri Oct 2) DONE (01-05 on
    2026-09-02, 06-11 on 2026-09-03): `00-prep-notes.md` per day +
    Will/Seth sources + the raw deck extractions at
    `private/F2026PrepPacks/`. Next to build: 12 (Mon Oct 5 holder) and
    the Ch 5 packs 13-16, which need a Ch 5 deck read first (Will's
    Ch 5 deck is 4 days / ~30 slides). Headline errata for Ch 3-4: Will's Ch 3 deck has NO
    Monday ink (exported before the moment-of-inertia class); Ch 4
    slides 14-15 have (1/2) m xdot^2 = U - E (should be E - U); HW03's
    3.36 solution uses I = 2mb (should be 2mb^2); HW04's solutions are
    numbered off by one against the assignment; in-class 4.26 has no
    posted solution anywhere.
14. DONE 2026-09-02: PCCIs for every class day are in the generator
    (Will's Look-At problems, one per day; reading prompts where he had
    none). Only day 1 has none, by design.
15. DONE 2026-09-03: HW coverage audit, Taylor edition.
    `audit_taylor_coverage.py` maps every assigned problem to its Taylor
    section (section headers OCR'd from the scanned PDF: tesseract over
    all 808 pages, text in `private/TaylorOCR/`, PDF page = book page +
    15) and that section to the first class day whose reading covers it.
    Result: 71 problems, 0 taught on or after their due date. The 8
    initial flags were reading LABELS narrower than what Will taught, now
    widened in the generator: Ch 2 day 3 = 2.5-2.7 (2.53 is 2.7), Ch 9
    day 3 = 9.6-9.8 (9.28/9.29), chaos days = 12.1-12.4 and 12.4-12.5
    (12.7-12.13). Rerun the audit after any HWS or CONTENT edit.
16. RESTORED 2026-09-03 (Michael: "went well"). `private/MoodleBuild/build_317.py` ->
    `PHY317-F2026-course.mbz` (11 chapter sections, 4 grade categories +
    2 participation items, 17 assignments; validated: gradebook 1000,
    ustar + index + declarations). The course is live: sections 0-13,
    gradebook 1000, 17 assignments. ANY further Moodle change is either
    by hand in Moodle or a NEW merge-only mbz containing ONLY new
    material -- never re-restore this file. Remaining by hand: section 0
    (item 2).
    MOODLE HAND EDITS NEEDED (2026-09-04 changes; the mbz is spent, so
    these are by hand; unknown whether Michael has done any):
    - Exam 1: due Fri Oct 9 13:20 (was Mon Oct 19 13:40); max grade 180.
    - Exam 2: due Wed Nov 11 13:20 (was Fri Nov 13); max grade 180.
    - Exam 3: max grade 180 (date unchanged).
    - HW04: due Mon Oct 5 22:00 (was Wed Oct 7); Restrict access date
      Thu Sep 24 (was Sep 27); description = regenerated HW04 block in
      hw-descriptions.html (it now says "due Monday").
    - HW09: due Fri Nov 6 22:00 (was Wed Nov 11); Restrict access date
      Tue Oct 27 (was Nov 1); description = regenerated HW09 block.
    - HW01-HW13: max grade 24 (was 25) -- Gradebook setup, 13 edits.
    - Participation manual items: 40 (through fall break) + 72 (after)
      = 112 (were 25 + 45 = 70).
    Gate after: course total reads 1000 again.
17. Python ports, in order of need: 1.50 starter notebook DONE
    2026-09-02 (`NewtonsLaws/skateboard_1_50.ipynb`); Linear Drag and
    Linear Drag Range DONE 2026-09-03 (`Drag/linear_drag.ipynb`,
    `Drag/linear_drag_range.ipynb`); Rockets DONE 2026-09-03
    (`Momentum/rockets.ipynb`). All four are INTERACTIVE via ipywidgets
    `interact` (decided 2026-09-03: match Will's Manipulate; 21 of his 22
    notebooks had sliders), written for JupyterLab on posit.smith.edu, no
    fallback -- if posit stays broken, Michael will ask for Colab
    versions. ipywidgets + numpy/scipy/sympy/matplotlib must be in
    /opt/python/3.12.3 there (in the ITS ticket). Next: Ch 5 (2DHM,
    DampedOscillations, FourierSeriesOfSquareWave). HW13 helper by late
    November.
18. Seth's order-of-magnitude assignment (12 hand-computed solar-system
    questions ending with the falling Moon predicting g; full solutions
    at `private/F2026PrepPacks/_shared/Seth order-of-magnitude
    assignment/`). Cool-stuff candidate: an early optional/bonus set, or
    the Mountain Day holder day's activity if Mountain Day has already
    passed. Decide by week 3.
19. Seth's Ch 4 "cube rocking on a cylinder" stability example and his
    "energy is harder than momentum" Ch 4 opener; his Ch 3 Kepler-II
    from centrality alone; his Ch 1 "counter-example" (two charges at
    right angles, momentum in the fields). Candidate steals for the Ch
    3-4 decks (weeks 3-4).
20. AT FALL BREAK (Tue Oct 13): switch the Moodle schedule embed to
    chunk 2 (`A17:I46`); open the mid-semester feedback. Carry into
    the class-15 (Wed Oct 14) prep pack when built.
21. Per-problem exam score records from Exam 1 on (three per exam), in a
    private spreadsheet -- the redemption final cannot be scored
    without them.
22. Week 1-2 AI-norms class discussion (15-min chunk; same as 210's
    decision); post the agreed norms next to the syllabus policy.
