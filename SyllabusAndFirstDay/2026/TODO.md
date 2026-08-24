# PHY 317 Fall 2026: task list

Working list, same conventions as PHY 210's
(`../../../MathematicalPhysics/SyllabusAndFirstDay/2026/TODO.md`).
Plan-of-record: follow Will Raven's F2025 closely (calendar generator
here already mirrors his 39-slot sequence, Monday exams, redemption
final, 1000-point conversion).

## Decided

- **Follow Will's syllabus consistently** (2026-08-17, reaffirmed).
- **Add the jackknife problem** (2026-08-17): the towed-trailer
  kinematics/stability problem from Michael's own project
  (`~/coding/jackknife/jackknife-physics.html` -- nonholonomic rolling
  constraints, kinematic bicycle model, the articulation ODE
  gamma-dot = -(v/D) sin(gamma) - (v/W)(1 + (L/D)cos(gamma)) tan(delta),
  straight-line reversing as a saddle, geometric critical jackknife
  angle). Natural home: a homework problem (possibly multi-part or
  Depth-style) during the Lagrangian/constraints stretch (Taylor
  Ch 7, late Oct), where nonholonomic constraints get their one
  spotlight; the interactive sim is the payoff demo. TODO: draft the
  problem set version + decide HW number once the HW skeleton exists.

## Registrar facts (verified 2026-08-17)

- PHY 317 01: W/F 1:20-2:35 PM + Mon 1:40-2:55 PM, Sabin-Reed 308,
  4 cr, 9 enrolled (as of 8/17). Prereqs PHY 210 & 215. NOTE the
  Monday block is a shifted time (1:40-2:55) -- same days (MWF), so
  the 39-meeting calendar holds; exams stay on Mondays, 75 min.

## To explore / mine (Seth Hopper's Earlham PHYS 425 archive)

At `~/Dropbox/__Smith/Classes/317-Classical/Seth/PHYS 425 - Classical
mechanics/` (F2017/F2021/F2023 instances). First-look highlights,
worth a proper inventory pass before building HW:

1. **Order of magnitude/** -- a distinctive standalone assignment
   (OrderOfMag.tex + solutions + a moon-gravity scaling Mathematica
   notebook). Cool-stuff candidate #1: could become an early HW or
   recurring thread.
2. **Lecture notes - Main/** -- per-chapter Mathematica notebooks +
   PDFs (Ch 1-9, 13, 14; Taylor numbering to confirm) -- reference
   while hand-building class materials.
3. **Solutions - Main/** -- HW 1-11 in LaTeX + Mathematica with
   figures; a full problem-set skeleton to compare against Will's.
4. **Tests - Main/** -- Tests 1-4 + TestQuestions.nb question bank.
5. **ProjectIdeas.txt** -- demo/experiment ideas: drag with
   water-wheel rotation, photogates, "bendable track to race balls --
   derive cycloid to show it's the fastest" (brachistochrone demo!),
   rockets.
6. **Howell CM Notes/** and **Papers/**, **Texts/** -- unexamined.

## Open decisions

7. Mathematica -> Python: the backup makes the cost concrete. 21 of
   Will's 22 notebooks are built on Manipulate (interactive sliders;
   2masses_3springs.nb has 20 of them), so a Python port means
   Jupyter + ipywidgets, not plain matplotlib. Mathematica is
   load-bearing in exactly one place (HW13 chaos, with a dedicated
   Helper.nb) and decorative-but-pervasive elsewhere. Options: port
   (real work), keep Mathematica for 317 only, or hybrid (port HW13's
   helper, drop the rest to optional demos).
8. Attendance + seminars: Will used grade caps (4 misses -> max B),
   not points, AND +0.5 final-grade points per physics seminar
   attended (4 max) -- neither is in the 1000-point conversion.
   Decide: PCCIs/participation points like 210, Will's caps +
   seminar bonus, or neither (9 students).
9. Syllabus rewrite (tufte-handout like PHY 210's? shared AI policy
   with 210 -- start from Will's F2025 statement, which is already the
   newer text).
10. RESOLVED 2026-08-17: Will's full Moodle backup extracted to
    `private/WillF2025/MoodleCourse/extracted/` (structure.txt = the
    course map + appendices). Recovered: all 13 HW sets + solutions,
    11 skeleton-slide chapter decks (typed slides completed with live
    tablet ink -- a format worth copying), per-chapter day-by-day
    in-class problem records, the delivered schedule with the full
    Prerequisites column, 22 Mathematica notebooks, the 7-deck linear
    algebra review (keyed to Felder Ch 6), Norsen's
    generalized-coordinates guest deck, and the department "AI prompts
    for students" doc. The 39-slot mapping is CONFIRMED against his
    delivered pace, and Exam 3 = Ch 8, 9, 11 is CONFIRMED (the
    calendar rows' "Ch 9-11" is Will's typo; the syllabus's 3x3
    redemption-problem arithmetic proves it).
11. Mountain Day holder is Mon Oct 5 (a guess); same caveat as 210.

## New items from the Moodle backup (2026-08-17)

12. HW due-date fixes in the generator (Will's practice vs our
    mechanical Fridays): (a) shift HW11 from Fri Nov 20 to Mon Nov 23
    to avoid a 14-day HW11->HW12 gap over Thanksgiving (Will did the
    same shift); (b) HW13 currently lands Fri Dec 11 = the second
    chaos lecture -- move to Mon Dec 14 or into reading period (Will
    gave 6 days); (c) note HW01 is due after only two meetings
    (content checks out -- Will's HW01 is pure Ch 1 -- but it's a
    fast first week). Also: Will's stated "Fridays at 10pm" drifted
    in practice; pick one time and keep it.
13. Exam 1 trade-off (aware, accepted for now): our placement gives
    an unbroken Ch 5 block but a 17-day Ch 4 -> Exam 1 gap (Will's
    was 7). The Prerequisites column + a review PCCI can bridge it.
14. ASK WILL: his exams. NO exam content exists anywhere -- not in
    the backup (never posted to Moodle), not in his empty Dropbox
    folder. We have the exam design (3 problems, one per chapter;
    redemption final with 9 optional problems) but zero instruments.
15. HW grading rubric: Will's syllabus has a +/check/-/X rubric WITH
    a reflection-resubmission policy the calendar never mentioned --
    read it before writing our HW policy (syllabus PDF sec., in
    extracted/01_Course_Information/).
16. Moodle build for 317: restore the .mbz (clean no-users export,
    needs mod_subsection >= 4.5 -- Smith is on 5.0.9); replace Will's
    personal Google booking link; verify the Library Research Guide
    LTI resolves; the gradebook is net-new work (his was a flat
    1300-pt HW sum; exams/final never in Moodle; add our 1000-pt
    categories + droplow=1).
17. COPYRIGHT cautions before reusing Will's Moodle shell: the full
    808-page scanned Taylor textbook is posted in Course Information,
    and the 22 Look-At/In-Class PDFs are Taylor Instructor Solutions
    Manual image excerpts. Decide what to keep/replace; don't blindly
    re-post.
18. Syllabus rewrite inputs: the department "AI prompts for students"
    doc (extracted/01_Course_Information/) alongside Will's AI
    statement; the just-in-time/just-after-time Prerequisites framing
    (02_Schedule/_section_summary.txt) is worth quoting.
19. Jackknife problem placement, refined: Will's HW07 already
    contains his own custom brachistochrone-as-tautochrone problem,
    and HW06 has an RLC-SHO analogy -- his sets DO carry custom
    problems, so adding jackknife as a custom problem on the Ch 7
    (Lagrangian/constraints) set matches his pattern exactly.

20. Liouville aside in the chaos unit (added 2026-08-24): neither Will
    nor Seth ever taught Liouville (Taylor 13.7; Will's course never
    reaches Ch 13, and Seth's Ch 13 notes stop short of it). Plan: a
    ~15-min aside during the Ch 12 chaos days -- Hamiltonian flows
    conserve phase-space volume, so ATTRACTORS REQUIRE DISSIPATION
    (why the damped driven pendulum can have one and the ideal
    pendulum can't). Frame the volume conservation as zero divergence
    of the phase-space flow: a direct callback to the Feynman
    divergence unit these students just had in PHY 210. Context: this
    is the first step in Michael's long-term arc toward teaching the
    fluctuation theorems at an undergraduate level (Green-Kubo /
    fluctuation-theorem material already appears in his Earlham 360
    project-ideas list); Liouville -> phase-space measure -> entropy
    production is the spine of that arc.
