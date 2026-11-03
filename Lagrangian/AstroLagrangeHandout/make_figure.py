#!/usr/bin/env python3
"""Draw ueff_contours.pdf for AstroLagrange.tex: contours of the effective potential of the
restricted three-body problem in the rotating frame (units R = 1, G(M1+M2) = 1, Omega = 1),
with the two primaries and the five Lagrange points. mu = 0.1 so the five points separate on
the page. Run from this folder: ../../../.venv/bin/python make_figure.py"""
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def collinear_points(mu):
    """x of L1, L2, L3 on the axis (M1 = 1-mu at x = -mu, M2 = mu at x = 1-mu)."""
    f = lambda x: x - (1 - mu) * (x + mu) / abs(x + mu) ** 3 - mu * (x - 1 + mu) / abs(x - 1 + mu) ** 3
    L3 = brentq(f, -2.0, -mu - 1e-9)
    L1 = brentq(f, -mu + 1e-9, 1 - mu - 1e-9)
    L2 = brentq(f, 1 - mu + 1e-9, 2.5)
    return L1, L2, L3


mu = 0.1
L1, L2, L3 = collinear_points(mu)
x = np.linspace(-1.6, 1.6, 801)
X, Y = np.meshgrid(x, x)
r1 = np.hypot(X + mu, Y)
r2 = np.hypot(X - 1 + mu, Y)
U = -(1 - mu) / r1 - mu / r2 - 0.5 * (X ** 2 + Y ** 2)   # U_eff per unit mass

fig, ax = plt.subplots(figsize=(5.2, 5.2))
ax.contour(X, Y, np.clip(U, -3, 0), levels=np.linspace(-2.2, -1.45, 16), colors="0.55", linewidths=0.8)
ax.plot([-mu, 1 - mu], [0, 0], "o", color="black", ms=9)
ax.text(-mu, -0.12, "$M_1$", ha="center", va="top")
ax.text(1 - mu, -0.12, "$M_2$", ha="center", va="top")
points = {"1": (L1, 0), "2": (L2, 0), "3": (L3, 0),
          "4": (0.5 - mu, np.sqrt(3) / 2), "5": (0.5 - mu, -np.sqrt(3) / 2)}
for k, (px, py) in points.items():
    ax.plot(px, py, "o", ms=6, mfc="white", mec="black", mew=1.4)
    below = k == "5"
    ax.text(px, py + (-0.1 if below else 0.1), f"$L_{k}$", ha="center", va="top" if below else "bottom")
ax.plot(0, 0, "+", color="black", ms=8)
ax.text(0.05, 0.06, "CM", fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_xlabel("$x/R$ (rotating frame)")
ax.set_ylabel("$y/R$")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color("0.6")
ax.tick_params(colors="0.3")
fig.tight_layout()
fig.savefig("ueff_contours.pdf")
print("ueff_contours.pdf; L1, L2, L3 =", round(L1, 4), round(L2, 4), round(L3, 4))
