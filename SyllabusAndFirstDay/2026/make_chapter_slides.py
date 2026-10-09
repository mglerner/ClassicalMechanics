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
import make_review_checklists as CHK          # noqa: E402  (puts shared/ on sys.path)
import chapter_slides as CS                   # noqa: E402  (CSS, fmt, write_index)
import courses as C                           # noqa: E402

# Prep material, not course-facing: lives with the decks in private/ (Dropbox).
OUT = C.private("317") / "Decks/ChapterSlides"
TITLES = {
    1: "Newton's Laws of Motion", 2: "Projectiles and Charged Particles",
    3: "Momentum and Angular Momentum", 4: "Energy", 5: "Oscillations",
    6: "Calculus of Variations", 7: "Lagrange's Equations",
    8: "Two-Body Central-Force Problems", 9: "Mechanics in Noninertial Frames",
    11: "Coupled Oscillators and Normal Modes", 12: "Nonlinear Mechanics and Chaos",
}
CSS = CS.CSS


fmt = CS.fmt


def chapter_days():
    days = defaultdict(list)
    for _n, d, _t, _r, ch, _cd in CHK.class_rows():
        if ch:
            days[ch].append(d)
    return days


def pcci_on(d):
    return CAL.PCCI.get(d, "")


def items(problems, when=None):
    """One <li> per problem; mark the one that is a PCCI. `when` is the day
    the list belongs to, or the list of days when one list covers them all."""
    dates = [] if when is None else (when if isinstance(when, list) else [when])
    out = []
    for p in problems:
        is_pcci = any(re.search(r"(^|[^\d.])" + re.escape(p) + r"($|[^\d])", pcci_on(d)) for d in dates)
        out.append(f"<li>{'<b class=pcci>' + p + '</b>' if is_pcci else p}</li>")
    return "<ul>" + "".join(out) + "</ul>"


def day_lists(lists, days):
    """[(label, problems)] with a date label when the lists line up with the days."""
    if len(lists) == len(days):
        return [(fmt(d), lst, d) for d, lst in zip(days, lists)]
    if len(lists) == 1:
        label = "both days" if len(days) == 2 else "all days"
        return [(label, lists[0], list(days))]
    return [(f"Day {i}", lst, None) for i, lst in enumerate(lists, 1)]


def slide(ch, days):
    cp = CAL.CHAPTER_PROBLEMS[ch]
    due = {hw: d for hw, d, *_ in CAL.HWS}
    span = (f"{fmt(days[0])} to {fmt(days[-1])}" if len(days) > 1
            else fmt(days[0]) if days else "")          # no class day: chapter cut (as 210)
    h = [f"<!doctype html><meta charset=utf-8><title>Ch {ch} problems</title><style>{CSS}</style>",
         "<div class=slide>",
         f"<header><div><span class=num>Chapter {ch}</span><span class=name>{TITLES[ch]}</span></div>"
         f"<div class=when>{span}</div></header>",
         "<div class=cols>"]
    h.append("<div><h2>Look at</h2>")
    for label, lst, d in day_lists(cp["lookat"], days):
        h.append(f"<div class=day>{label}</div>{items(lst, d)}")
    h.append("</div>")
    h.append("<div><h2>In-class options</h2>")
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
    chapters = []
    for ch in sorted(CAL.CHAPTER_PROBLEMS):
        (OUT / f"Ch{ch:02d}.html").write_text(slide(ch, days[ch]))
        chapters.append((ch, TITLES[ch], fmt(days[ch][0]) if days[ch] else "no class day"))
    links = CS.write_index(OUT, C.COURSE["317"]["name"], chapters, "slides", "problem slides")
    print(f"wrote {len(links)} chapter slides to {OUT}")


if __name__ == "__main__":
    main()
