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

7. Mathematica -> Python: Will AND Seth both used Mathematica; Michael
   leans Python (same call as PHY 210, where Python won). Decide
   before adapting either's computational materials.
8. Attendance: Will used grade caps (4 misses -> max B), not points;
   the 1000-point conversion currently has no attendance category.
   PHY 210 uses PCCI-turn-in-as-participation -- decide whether 317
   gets PCCIs/participation points too, or keeps Will's caps, or
   neither (9 students; attendance may take care of itself).
9. Syllabus rewrite (tufte-handout like PHY 210's? shared AI policy
   with 210 -- start from Will's F2025 statement, which is already the
   newer text).
10. Verify Will's calendar mapping against his actual F2025 delivered
    pace if artifacts exist (his Dropbox folder
    `317-Classical/Will/` is EMPTY -- sources are only
    SmithPreMichaelArtifacts/PHY317 F2025 Syllabus.pdf +
    WillClassicalCalendar.docx; ask Will if more exists).
11. Mountain Day holder is Mon Oct 5 (a guess); same caveat as 210.
