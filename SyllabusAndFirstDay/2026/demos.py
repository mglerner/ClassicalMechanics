"""PHY 317 lecture demos, Fall 2026: the data behind the demo map (shared/demo_map.py).

days() adapts the calendar generator; DEMOS is the curated list (research 2026-10-06, the
lab-manager meeting). Keys are documented in shared/demo_map.py.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_fall2026_calendar as CAL      # noqa: E402
import make_review_checklists as K        # noqa: E402

TITLE = "PHY 317 demo map (Fall 2026)"
SUBTITLE = ("Classical Mechanics (Taylor). One demo per week is the aspiration; nothing is on this map just "
            "to fill a week. Candidates are decided with the lab manager.")
CH_COLORS = {1: "#2563eb", 2: "#0d9488", 3: "#7c3aed", 4: "#c2410c", 5: "#be185d",
             6: "#15803d", 7: "#0369a1", 8: "#a16207", 9: "#4338ca", 11: "#b91c1c", 12: "#475569"}
NOTES = {9: "Observation day (done)."}


def days():
    out = [dict(date=d, kind="off", topic=why) for d, why in CAL.NO_CLASS.items()]
    for n, d, topic, reading, ch, _chday in K.class_rows():
        day = dict(date=d, n=n, topic=topic, reading=f"Taylor {reading}" if reading else "", note=NOTES.get(n))
        if ch is None and reading == "" and d in CAL.EXAMS:
            day.update(kind="exam")
        else:
            day.update(kind="class", color=CH_COLORS.get(ch, "#94a3b8"), group=f"Ch {ch}" if ch else None)
        out.append(day)
    return out


# The curated list (research files in demo-research/; curated 2026-10-06).
DEMOS = json.loads((HERE / "demos.json").read_text())

SKIPS_HTML = """
<h2>Looked at and left out</h2>
<p>Topics where the research found nothing worth the minutes, so the week stays demo-free on purpose.</p>
<ul>
<li><b>SHO (class 12):</b> vertical-vs-horizontal spring period and amplitude independence; a strong upper-division class predicts both, so no vote splits. Borrow 210's turntable for a one-minute look at 5.2's complex exponential if it is built.</li>
<li><b>Light damping shifts the period (class 13):</b> too small to see; in water the added-mass shift swamps it and the demo would show the wrong cause.</li>
<li><b>Hamilton's principle (class 20):</b> no physical demo of "the action is stationary"; a notebook of trial paths with action values does it better.</li>
<li><b>Atwood machine via Lagrange (class 21):</b> everyone predicts it; nothing to vote on. (The swinging Atwood machine is a chaos demo and belongs to Ch 12.)</li>
<li><b>Noether's theorem (class 22):</b> conservation demos re-show conservation, not the symmetry link; the driven phi in the rotating hoop (p_phi NOT conserved) makes the point better on the board.</li>
<li><b>Lagrange multipliers (class 22):</b> no demo makes the constraint force the observable.</li>
<li><b>Rocket (class 06), central forces and multiparticle systems (class 11):</b> intro-level demos with no upper-division prediction worth the minutes.</li>
<li><b>Kepler orbits with real apparatus, reduced mass (classes 23-24):</b> nothing gives a true 1/r^2 orbit; the spandex sheet survives only as the "orbits that do NOT close" counterexample, with its known critiques in the entry.</li>
<li><b>Hohmann transfers (class 25):</b> no tabletop demo; the catch-up-by-slowing-down simulation is the vote.</li>
<li><b>Tides (class 26):</b> no physical demo shows the far-side bulge for the right reason; water-tray models get it from the centrifugal hand-waving Taylor 9.2 replaces. The helium balloon sets up "-mA everywhere" and the tidal field is drawn.</li>
<li><b>Shive wave machine (Ch 11):</b> a waves-course demo; Taylor stops at three coupled pendula.</li>
<li><b>Physical driven damped pendulum (class 36):</b> the PASCO chaos accessory is not Taylor's equation and period doubling is unreliable live; the simulation entry carries the vote.</li>
<li><b>Liouville (class 37):</b> no direct physical demonstration; the Couette "unmixing" cell is an honest analog for area preservation only, and only if one already exists. The reversibility it shows is a different fact.</li>
</ul>
"""
