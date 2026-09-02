"""Margin figures for the PHY 317 F2026 syllabus (tufte-handout).

Writes brachistochrone.pdf and chaos_pendulum.pdf next to this script.
Run in the courses/ uv venv:  python make_syllabus_figures.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).parent
plt.rcParams.update({"font.size": 8, "font.family": "serif"})
W = 2.2  # tufte margin width in inches


def brachistochrone():
    """Cycloid vs straight line vs circular arc between the same two points."""
    g = 9.8
    # Cycloid from (0,0) down to (x1, -y1): pick the cycloid parameter so
    # it lands on the target point.
    x1, y1 = 2.0, 1.0
    from scipy.optimize import brentq
    f = lambda th: (th - np.sin(th)) / (1 - np.cos(th)) - x1 / y1
    th1 = brentq(f, 0.1, 2 * np.pi - 0.1)
    a = y1 / (1 - np.cos(th1))
    th = np.linspace(0, th1, 300)
    xc, yc = a * (th - np.sin(th)), -a * (1 - np.cos(th))
    # travel times by numerical quadrature of ds / sqrt(2 g |y|)
    def travel_time(x, y):
        ds = np.hypot(np.diff(x), np.diff(y))
        ymid = -(y[1:] + y[:-1]) / 2
        return np.sum(ds / np.sqrt(2 * g * np.maximum(ymid, 1e-9)))
    xl = np.linspace(0, x1, 300)
    yl = -y1 * xl / x1
    # circular arc through the endpoints, bulging below the chord: the
    # center sits ABOVE the chord and we draw the minor arc.
    r = 1.25
    mx, my = x1 / 2, -y1 / 2
    d = np.hypot(x1, y1)
    h = np.sqrt(r**2 - (d / 2)**2)
    cx, cy = mx + h * (y1 / d), my + h * (x1 / d)  # center on the high side
    a0, a1 = np.arctan2(0 - cy, 0 - cx), np.arctan2(-y1 - cy, x1 - cx)
    while a1 - a0 > np.pi:
        a1 -= 2 * np.pi
    while a0 - a1 > np.pi:
        a1 += 2 * np.pi
    ang = np.linspace(a0, a1, 300)
    xa, ya = cx + r * np.cos(ang), cy + r * np.sin(ang)
    fig, ax = plt.subplots(figsize=(W, 1.5))
    for x, y, lab, ls in [(xl, yl, "straight", ":"), (xa, ya, "arc", "--"),
                          (xc, yc, "cycloid", "-")]:
        ax.plot(x, y, ls, color="k", lw=1.2,
                label=f"{lab}: {travel_time(x, y):.3f} s")
    ax.plot([0, x1], [0, -y1], "o", color="k", ms=3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.legend(loc="upper right", frameon=False, fontsize=6.5,
              handlelength=1.6)
    fig.tight_layout(pad=0.1)
    fig.savefig(HERE / "brachistochrone.pdf")


def chaos_pendulum():
    """Driven damped pendulum: two nearby starts diverge (Taylor 12.1-12.3)."""
    # Taylor's parameters: omega0 = 1.5 omega, beta = omega0/4, omega = 2 pi.
    w, w0 = 2 * np.pi, 1.5 * 2 * np.pi
    beta = w0 / 4
    gamma = 1.105  # in Taylor's chaotic range

    def rhs(t, s):
        phi, om = s
        return [om, -2 * beta * om - w0**2 * np.sin(phi)
                + gamma * w0**2 * np.cos(w * t)]
    t = np.linspace(0, 12, 3000)
    fig, ax = plt.subplots(figsize=(W, 1.3))
    for phi0, ls in [(0.0, "-"), (0.001, "--")]:
        sol = solve_ivp(rhs, (0, 12), [phi0, 0.0], t_eval=t, rtol=1e-9,
                        atol=1e-11)
        ax.plot(t, sol.y[0] / np.pi, ls, color="k", lw=0.9)
    ax.set_xlabel("t (drive periods)", labelpad=1)
    ax.set_ylabel(r"$\phi/\pi$", labelpad=1)
    ax.set_xlim(0, 12)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout(pad=0.1)
    fig.savefig(HERE / "chaos_pendulum.pdf")


if __name__ == "__main__":
    brachistochrone()
    chaos_pendulum()
    print("wrote brachistochrone.pdf, chaos_pendulum.pdf")
