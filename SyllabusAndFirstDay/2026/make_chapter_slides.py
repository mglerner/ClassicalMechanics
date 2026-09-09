"""Chapter-opening problem slides (PHY 317 F2026), one HTML page per chapter.

Will Raven opened each chapter with a three-column slide: Look at /
In class / Homework. Ours are generated from the calendar generator so
the day labels are OUR dates and the lists are OUR lists: screenshot the
page and paste it into the chapter's GoodNotes deck. Rerun after any
change to CHAPTER_PROBLEMS, HWS, PCCI, or the calendar:

    python make_chapter_slides.py

Writes private/Decks/ChapterSlides/ChNN.html (and index.html). Generated; do not edit.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import make_fall2026_calendar as CAL          # noqa: E402
import make_review_checklists as CHK          # noqa: E402

# Prep material, not course-facing: lives with the decks in private/ (Dropbox).
OUT = Path.home() / "coding/courses/ClassicalMechanics/private/Decks/ChapterSlides"
TITLES = {
    1: "Newton's Laws of Motion", 2: "Projectiles and Charged Particles",
    3: "Momentum and Angular Momentum", 4: "Energy", 5: "Oscillations",
    6: "Calculus of Variations", 7: "Lagrange's Equations",
    8: "Two-Body Central-Force Problems", 9: "Mechanics in Noninertial Frames",
    11: "Coupled Oscillators and Normal Modes", 12: "Nonlinear Mechanics and Chaos",
}
CSS = """
body { background: #fffff8; margin: 0; padding: 28px; color: #111;
       font-family: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
       font-variant-numeric: tabular-nums oldstyle-nums; }
.slide { width: 1040px; padding: 30px 40px 26px 40px; box-sizing: border-box; background: #fffff8; }
header { display: flex; align-items: baseline; justify-content: space-between;
         border-bottom: 1px solid #999; padding-bottom: 10px; margin-bottom: 20px; }
header .num { font-size: 40px; font-weight: normal; margin: 0; letter-spacing: .01em; }
header .name { font-size: 22px; font-style: italic; color: #444; margin-left: 14px; }
header .when { font-size: 17px; color: #6b6b6b; font-style: italic; }
.cols { display: grid; grid-template-columns: 1fr 1fr 1.15fr; column-gap: 44px; }
h2 { font-size: 15px; font-weight: normal; letter-spacing: .12em; text-transform: uppercase;
     color: #6b6b6b; margin: 0 0 10px 0; }
.day, .grp { font-size: 16px; font-style: italic; color: #6b6b6b; margin: 10px 0 2px 0; }
.day:first-of-type, .grp:first-of-type { margin-top: 0; }
ul { list-style: none; margin: 0; padding: 0; }
li { font-size: 21px; line-height: 1.35; padding-left: 1.1em; text-indent: -1.1em; }
li.note { font-size: 17px; color: #444; font-style: italic; }
b.pcci { font-weight: normal; border-bottom: 2px solid #b33; padding-bottom: 1px; }
.hwhead { font-size: 21px; margin: 12px 0 2px 0; }
.hwhead:first-of-type { margin-top: 0; }
.hwhead .due { font-size: 16px; font-style: italic; color: #6b6b6b; margin-left: 6px; }
footer { margin-top: 22px; font-size: 16px; color: #6b6b6b; font-style: italic; }
footer .key { border-bottom: 2px solid #b33; color: #111; font-style: normal; }
"""


def fmt(d):
    return d.strftime("%a %b %-d")


def chapter_days():
    days = defaultdict(list)
    for _n, d, _t, _r, ch, _cd in CHK.class_rows():
        if ch:
            days[ch].append(d)
    return days


def pcci_on(d):
    return CAL.PCCI.get(d, "")


def items(problems, d=None):
    """One <li> per problem; bold the one that is that day's PCCI."""
    out = []
    for p in problems:
        is_pcci = d is not None and re.search(r"(^|[^\d.])" + re.escape(p) + r"($|[^\d])", pcci_on(d))
        out.append(f"<li>{'<b class=pcci>' + p + '</b>' if is_pcci else p}</li>")
    return "<ul>" + "".join(out) + "</ul>"


def day_lists(lists, days):
    """[(label, problems)] with a date label when the lists line up with the days."""
    if len(lists) == len(days):
        return [(fmt(d), lst, d) for d, lst in zip(days, lists)]
    if len(lists) == 1:
        label = "both days" if len(days) == 2 else "all days"
        return [(label, lists[0], None)]
    return [(f"Day {i}", lst, None) for i, lst in enumerate(lists, 1)]


def slide(ch, days):
    cp = CAL.CHAPTER_PROBLEMS[ch]
    due = {hw: d for hw, d, *_ in CAL.HWS}
    span = f"{fmt(days[0])} to {fmt(days[-1])}" if len(days) > 1 else fmt(days[0])
    h = [f"<!doctype html><meta charset=utf-8><title>Ch {ch} problems</title><style>{CSS}</style>",
         "<div class=slide>",
         f"<header><div><span class=num>Chapter {ch}</span><span class=name>{TITLES[ch]}</span></div>"
         f"<div class=when>{span}</div></header>",
         "<div class=cols>"]
    h.append("<div><h2>Look at</h2>")
    for label, lst, d in day_lists(cp["lookat"], days):
        h.append(f"<div class=day>{label}</div>{items(lst, d)}")
    h.append("</div>")
    h.append("<div><h2>In class</h2>")
    for label, lst, d in day_lists(cp["inclass"], days):
        h.append(f"<div class=day>{label}</div>{items(lst)}")
    h.append("</div>")
    h.append("<div><h2>Homework</h2>")
    for name, probs in cp["hw"]:
        n = int(name[2:])
        h.append(f"<div class=hwhead>{name}<span class=due>due {fmt(due[n])}</span></div><ul>")
        h.extend(f"<li>{p}</li>" for p in probs)
        h.append("</ul>")
    h.append("</div></div>")
    h.append("<footer>Solutions to the look-at and in-class problems are on Moodle. "
             "<span class=key>Underlined</span> = that day's PCCI, on paper at the start of class.</footer>")
    h.append("</div>")
    return "\n".join(h) + "\n"


def main():
    OUT.mkdir(exist_ok=True)
    days = chapter_days()
    links = []
    for ch in sorted(CAL.CHAPTER_PROBLEMS):
        (OUT / f"Ch{ch:02d}.html").write_text(slide(ch, days[ch]))
        links.append(f"<li><a href=Ch{ch:02d}.html>Chapter {ch}: {TITLES[ch]}</a> ({fmt(days[ch][0])})</li>")
    (OUT / "index.html").write_text(
        "<!doctype html><meta charset=utf-8><title>PHY 317 chapter slides</title>"
        "<body style='font-family:Helvetica,Arial,sans-serif;padding:24px'>"
        "<h1>PHY 317 F2026 chapter-opening problem slides</h1>"
        "<p>Generated by make_chapter_slides.py from the calendar generator. Open one, screenshot the card, paste into the deck.</p>"
        "<ul>" + "\n".join(links) + "</ul></body>\n")
    print(f"wrote {len(links)} chapter slides to {OUT}")


if __name__ == "__main__":
    main()
