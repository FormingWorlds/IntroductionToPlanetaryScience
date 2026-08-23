"""Generate Fig. (`fig:coriolis`).

Single-panel schematic of the Coriolis deflection, viewed from above
the North Pole (centre = pole, rim = equator).

A projectile is launched from the pole, which has no rotational
velocity, toward a target on the equator. On a non-rotating Earth it
would travel straight to the target (dashed line). Because the Earth
turns eastward under the flight, its track over the ground curves to
the right in the Northern Hemisphere (red curve) and lands to the right
of the target. Launching from the pole keeps the geometry simple: the
straight path is radial and the deflection comes entirely from the
ground rotating beneath the flight.

Caption / figure id : `fig:coriolis`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/coriolis_effect.avif"

DISK = "#cfe5ff"
AIM = "0.40"
PATH = "#d62728"
DEFLECT_DEG = 25.0  # schematic deflection, exaggerated for clarity


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.4, 7.8))

    # Earth seen from above the North Pole: centre = pole, rim = equator.
    ax.add_patch(Circle((0, 0), 1.0, facecolor=DISK, edgecolor="black",
                        lw=1.2, zorder=0))
    # Faint meridians (offset off the axes so none overlaps the aim line or
    # the equator label) and one mid-latitude circle, as a light reference
    # that the disk is a rotating globe seen from above.
    for ang in range(22, 360, 45):
        a = np.radians(ang)
        ax.plot([0.12 * np.sin(a), np.sin(a)], [0.12 * np.cos(a), np.cos(a)],
                color="white", lw=0.7, alpha=0.35, zorder=1)
    ax.add_patch(Circle((0, 0), 0.5, facecolor="none", edgecolor="white",
                        lw=0.7, alpha=0.35, zorder=1))
    # Equator label sits just outside the rim, clear of the disk interior.
    ax.text(0.0, -1.10, "Equator (rim)", color="0.45", fontsize=9,
            ha="center", va="top", zorder=2)

    # Pole (launch point). Meridians start at r = 0.12, so the centre is clear.
    ax.plot(0, 0, "o", color="black", ms=8, zorder=6)
    ax.text(0.0, -0.10, "Launch\n(North Pole)", fontsize=10,
            ha="center", va="top", zorder=6)

    # Target on the equator (top of the rim).
    target = np.array([0.0, 1.0])
    ax.plot(*target, "*", color="black", ms=17, zorder=6)
    ax.text(target[0] - 0.05, target[1] + 0.04, "Target", fontsize=11,
            ha="right", va="bottom", zorder=6)

    # Intended path on a non-rotating Earth: straight pole -> target.
    ax.add_patch(FancyArrowPatch((0, 0), tuple(target * 0.99),
                                 arrowstyle="->", mutation_scale=14,
                                 color=AIM, lw=1.8,
                                 linestyle=(0, (6, 4)), zorder=4))
    # Label outside the disk on the left, with a leader to the aim line.
    ax.annotate("Aim: straight to target\n(non-rotating Earth)",
                xy=(0.0, 0.52), xytext=(-1.24, 0.55),
                color="0.35", fontsize=9.5, ha="center", va="center", zorder=5,
                arrowprops=dict(arrowstyle="-", color="0.6", lw=0.7))

    # Actual track over the rotating Earth: deflects to the right (NH).
    a = np.radians(DEFLECT_DEG)
    land = np.array([np.sin(a), np.cos(a)])  # on the rim, right of target
    t = np.linspace(0, 1, 200)
    x = land[0] * t ** 2   # start tangent purely +y, curvature toward +x
    y = land[1] * t
    ax.plot(x, y, color=PATH, lw=2.6, zorder=5)
    ax.add_patch(FancyArrowPatch((x[-3], y[-3]), (x[-1], y[-1]),
                                 arrowstyle="->", mutation_scale=18,
                                 color=PATH, lw=2.6, zorder=5))
    ax.plot(*land, "o", color=PATH, ms=9, zorder=6)
    # Both red labels sit outside the disk on the right, each with a leader.
    ax.annotate("Lands here\n(deflected right)",
                xy=(land[0] + 0.02, land[1]), xytext=(land[0] + 0.36, land[1] + 0.12),
                color=PATH, fontsize=10, ha="left", va="center", zorder=6,
                arrowprops=dict(arrowstyle="-", color=PATH, lw=0.8))
    ax.annotate("Actual track over\nthe rotating Earth",
                xy=(0.26, 0.72), xytext=(1.00, 0.48),
                color=PATH, fontsize=10, ha="left", va="center", zorder=5,
                arrowprops=dict(arrowstyle="-", color=PATH, lw=0.8))

    # Earth's rotation arrow: counterclockwise = eastward from above the pole.
    r_arc = 1.25
    ax.add_patch(Arc((0, 0), 2 * r_arc, 2 * r_arc, angle=0,
                    theta1=-70, theta2=-20, color="black", lw=1.2))
    a_tail, a_head = np.radians(-25), np.radians(-20)
    ax.add_patch(FancyArrowPatch(
        (r_arc * np.cos(a_tail), r_arc * np.sin(a_tail)),
        (r_arc * np.cos(a_head), r_arc * np.sin(a_head)),
        arrowstyle="->", mutation_scale=14, color="black", lw=1.2))
    ax.text(1.32, -1.00, "$\\Omega$: Earth spins\neastward",
            fontsize=11, ha="center", va="center")

    # One-line mechanism note, below the disk.
    ax.text(0, -1.38,
            "The Earth turns east under the flight, so the track bends to the "
            "right of\nthe direction of travel (Northern Hemisphere; it bends "
            "left in the Southern).",
            fontsize=10, ha="center", va="top")

    lim = 1.7
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Geometric origin of the Coriolis deflection\n"
                 "(view from above the North Pole)", fontsize=12)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
