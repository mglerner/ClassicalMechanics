"""Generate the Fall 2026 PHY 317 (Classical Mechanics, Smith) course calendar.

Format follows the P125/PHY210 calendar style: a "Schedule" sheet with
Week | Class | Date | Topics | Reading Due | HW Due | Exams in two
side-by-side half-semester blocks, plus a "Grade Categories" sheet.
Content follows Will Raven's Fall 2025 PHY 317 sequence (Taylor,
Classical Mechanics) remapped onto the Smith Fall 2026 academic calendar;
his 39 teaching slots (including the Mountain Day holder and catch-up
days) map one-to-one onto Fall 2026's 39 MWF meetings.

Usage: python make_fall2026_calendar.py OUTPUT.xlsx
"""
import sys
from datetime import date, timedelta

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

# ---------------------------------------------------------------- semester
# Smith Fall 2026: classes Tue Sep 8 - Tue Dec 15.
# MWF meetings; skip Mon Oct 12 (autumn recess), Wed Nov 25 + Fri Nov 27
# (Thanksgiving). Cromwell Day (Tue Nov 10) doesn't hit MWF.
FIRST_DAY = date(2026, 9, 9)   # first MWF meeting (classes open Tue Sep 8)
LAST_DAY = date(2026, 12, 14)  # last MWF meeting
NO_CLASS = {
    date(2026, 10, 12): "Autumn recess",
    date(2026, 11, 25): "Thanksgiving",
    date(2026, 11, 27): "Thanksgiving",
}

def class_days():
    d = FIRST_DAY
    while d <= LAST_DAY:
        if d.weekday() in (0, 2, 4) and d not in NO_CLASS:  # M W F
            yield d
        d += timedelta(days=1)

# ------------------------------------------------------------------ content
# (topic, reading, prerequisites) per teaching slot, in Will Raven's F2025
# order. Readings are Taylor chapter/sections, read before class.
# Prerequisites are Will's just-in-time review pointers: Knight = intro
# physics (PHY 117/118), Math Methods = Felder & Felder (PHY 210).
# Exams are pinned to Monday slot indices (Will gave Monday exams; pinning
# also keeps them off Fridays so no HW due-date is displaced).
EXAMS = {
    16: "EXAM 1 (Ch 2-4)",       # Mon Oct 19
    25: "EXAM 2 (Ch 5-7)",       # Mon Nov 9
    35: "EXAM 3 (Ch 8, 9, 11)",  # Mon Dec 7
}
CONTENT = [
    ("Notation; Newton's laws; polar coordinates", "Ch. 1",
     "Knight: Ch. 3 (Vectors), Ch. 4-6 (Forces)"),
    ("Newton's laws", "Ch. 1",
     "Knight: Ch. 3 (Vectors), Ch. 4-6 (Forces)\n"
     "Math Methods: Ch. 5 (Cylindrical and Spherical Coordinates)\n"
     "Other: Algebra"),
    ("Linear drag force; terminal velocity", "2.1-2.2",
     "Knight: Ch. 5 (Drag)\nMath Methods: Ch. 1 (Intro to ODEs)\n"
     "Other: Algebra, graphs, integrals, derivatives"),
    ("Trajectories and range; quadratic air drag", "2.3-2.4",
     "Knight: Ch. 4 (Kinematics in 2D)\nMath Methods: Ch. 1 (Intro to ODEs)\n"
     "Other: Algebra, graphs, integrals, derivatives"),
    ("Lorentz force law; cyclotron motion", "2.5",
     "Knight: Ch. 3 (Vectors), Ch. 22-23 (Electromagnetism Review)\n"
     "Math Methods: Ch. 3 (Complex numbers, Euler's equation), "
     "Ch. 8 (Vector Calculus)\nOther: Cross products"),
    ("Conservation of momentum; rocket motion", "3.1-3.2",
     "Knight: Ch. 11 (Impulse and Momentum)\n"
     "Other: Integrals, vector components"),
    ("Center of mass; angular momentum", "3.3-3.4",
     "Knight: Ch. 11 (Momentum), Ch. 12 (Rotation)\n"
     "Other: Integrals, vector components, cross products"),
    ("Moment of inertia; conservation of angular momentum", "3.5",
     "Knight: Ch. 12 (Rotation of Rigid Body)\n"
     "Other: Integrals, vector components"),
    ("Work-KE theorem; conservative forces", "4.1-4.3",
     "Knight: Ch. 9-10 (Work and Kinetic Energy)\n"
     "Math Methods: Ch. 8 (Line integrals, curls)"),
    ("Potential energy; graphs of PE functions", "4.4-4.7",
     "Knight: Ch. 9-10 (Potential Energy)\n"
     "Other: Full derivatives and chain rule"),
    ("Central forces; multiparticle systems", "4.8-4.10",
     "Knight: Ch. 12 (Gravity)\nMath Methods: Ch. 5 (Spherical "
     "Coordinates), Ch. 8 (Gradients in spherical)"),
    ("Mountain Day holder", "", ""),
    ("Spring forces; simple harmonic oscillator", "5.1-5.2",
     "Knight: Ch. 15 (Oscillations)\nMath Methods: Ch. 6 (Oscillations)"),
    ("2D oscillators; damped SHO", "5.3-5.4",
     "Math Methods: Ch. 1 (ODEs)"),
    ("Forced damped SHO; resonance", "5.5-5.6",
     "Math Methods: Ch. 3 (Complex Numbers), Ch. 1 (ODEs)"),
    ("Fourier series analysis of driven SHO", "5.7-5.8",
     "Math Methods: Ch. 9 (Fourier Series and Transforms)"),
    ("Calculus of variations; Fermat's principle; Euler-Lagrange", "6.1-6.2",
     "Math Methods: Ch. 4 (Partial Derivatives), Ch. 5 (Integration)"),
    ("Euler-Lagrange equation; brachistochrone problem", "6.3",
     "Math Methods: Ch. 4 (Partial Derivatives)"),
    ("Multiple variables; generalized coordinates", "6.4", ""),
    ("Lagrange's equations; Hamilton's principle", "7.1", ""),
    ("Constrained systems; generalized coordinates", "7.2-7.3", ""),
    ("Examples of Lagrange's equations; Lagrange multipliers", "7.5, 7.9",
     ""),
    ("Central forces; reduced mass; equations of motion", "8.1-8.4",
     "Knight: Ch. 12 (Gravity)"),
    ("Orbits", "8.5-8.6",
     "Math Methods: Ch. 1 (ODEs)\nCalculus I & II"),
    ("Changing orbits", "8.7-8.8", "Calculus I & II"),
    ("Catch-up day", "", ""),
    ("Accelerating frames; tides", "9.1-9.2",
     "Math Methods: Ch. 8 (Vector Calculus)"),
    ("Angular velocity; rotating frames", "9.3-9.5",
     "Math Methods: Ch. 8 (Vectors in Curvilinear Coordinates)"),
    ("Centrifugal force; Coriolis force", "9.6-9.7", ""),
    ("Coupled oscillators; two masses and three springs", "11.1-11.2",
     "Knight: Ch. 15 (Oscillations)\nMath Methods: Ch. 6 "
     "(Eigenvectors/Eigenvalues)\nReview the ideas behind basis vectors"),
    ("Normal coordinates; weakly coupled oscillators", "11.2-11.4",
     "Math Methods: Ch. 6 (Eigenvectors/Eigenvalues)"),
    ("Catch-up day", "", ""),
    ("Double pendulum", "11.4", ""),
    ("Chaos", "12.1-12.3", ""),
    ("Chaos", "12.1-12.3", ""),
    ("Last day: review and wrap-up", "", ""),
]

def build(outpath):
    days = list(class_days())
    n = len(days)
    assert len(CONTENT) + len(EXAMS) == n, (
        f"{len(CONTENT)} content + {len(EXAMS)} exams for {n} class meetings")
    assert all(days[i].weekday() == 0 for i in EXAMS), "exam not on a Monday"

    rows = []  # (week, class_no, date, topic, reading, prereq, hw, exam)
    week_no = 0
    last_week = None
    class_no = 0
    hw_no = 0
    content_i = 0
    breaks_seen = set()
    for slot_i, d in enumerate(days):
        iso_week = d.isocalendar()[1]
        if iso_week != last_week:
            week_no += 1
            last_week = iso_week
        for bd, why in NO_CLASS.items():
            if bd not in breaks_seen and bd < d:
                breaks_seen.add(bd)
                rows.append(
                    (None, None, bd, f"No class - {why}", "", "", "", ""))
        if slot_i in EXAMS:
            topic, reading, prereq, exam = EXAMS[slot_i], "", "", EXAMS[slot_i]
        else:
            (topic, reading, prereq), exam = CONTENT[content_i], ""
            content_i += 1
        hw = ""
        if d.weekday() == 4 and slot_i > 0:  # Fridays
            hw_no += 1
            hw = f"HW{hw_no:02d}"
        class_no += 1
        rows.append((week_no, class_no, d, topic, reading, prereq, hw, exam))
    for bd, why in NO_CLASS.items():
        if bd not in breaks_seen:
            rows.append((None, None, bd, f"No class - {why}", "", "", ""))
    rows.sort(key=lambda r: r[2])
    rows.append((None, None, date(2026, 12, 19),
                 "Final exam period Dec 19-22 (registrar schedules)",
                 "", "", "",
                 "Final (Ch 12 required + optional grade-replacement)"))

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Schedule"

    header_font = Font(bold=True)
    header_fill = PatternFill("solid", fgColor="D9E1F2")
    break_fill = PatternFill("solid", fgColor="FCE4D6")
    exam_fill = PatternFill("solid", fgColor="FFF2CC")
    thin = Side(style="thin", color="BBBBBB")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    wrap = Alignment(wrap_text=True, vertical="top")

    headers = ["Week", "Class", "Date", "Topics", "Reading Due",
               "Prerequisites", "HW Due", "Exams"]
    ncols = len(headers) + 1  # +1 spacer between the two blocks
    half = (len(rows) + 1) // 2
    blocks = [rows[:half], rows[half:]]
    for b, block in enumerate(blocks):
        c0 = 1 + b * ncols  # A=1, J=10
        for j, h in enumerate(headers):
            cell = ws.cell(row=1, column=c0 + j, value=h)
            cell.font = header_font
            cell.fill = header_fill
            cell.border = border
        for i, (wk, cn, d, topic, reading, prereq, hw, exam) in enumerate(
                block, start=2):
            vals = [wk, cn, d.strftime("%a %b %-d"), topic, reading,
                    prereq, hw, exam]
            for j, v in enumerate(vals):
                cell = ws.cell(row=i, column=c0 + j, value=v)
                cell.border = border
                cell.alignment = wrap
                if cn is None:
                    cell.fill = break_fill
                elif exam:
                    cell.fill = exam_fill

    widths = [6, 6, 11, 38, 12, 44, 9, 22]
    for b in range(2):
        for j, w in enumerate(widths):
            col = openpyxl.utils.get_column_letter(1 + b * ncols + j)
            ws.column_dimensions[col].width = w

    gc = wb.create_sheet("Grade Categories")
    gc.append(["Category", "Number", "Drop", "Points Each", "Total Points"])
    for cell in gc[1]:
        cell.font = header_font
        cell.fill = header_fill
    # Will Raven's weights (HW 30%, exams 21% x 3, final 7%) converted to
    # points. Course total must be exactly 1000 points.
    cats = [
        ("Weekly Homework", 13, 1, 25),
        ("Exams", 3, 0, 210),
        ("Final exam (Ch 12 problem)", 1, 0, 70),
    ]
    total = sum((num - drop) * pts for _, num, drop, pts in cats)
    assert total == 1000, f"grade categories sum to {total}, not 1000"
    for i, (name, num, drop, pts) in enumerate(cats, start=2):
        gc.append([name, num, drop, pts, f"=(B{i}-C{i})*D{i}"])
    gc.append(["Total", None, None, None, f"=SUM(E2:E{1 + len(cats)})"])
    for j, w in enumerate([28, 9, 7, 12, 13]):
        gc.column_dimensions[openpyxl.utils.get_column_letter(j + 1)].width = w

    wb.save(outpath)
    print(f"wrote {outpath}: {len(rows)} schedule rows, {n} class meetings, "
          f"{hw_no} HWs, grade total {total}")

if __name__ == "__main__":
    build(sys.argv[1])
