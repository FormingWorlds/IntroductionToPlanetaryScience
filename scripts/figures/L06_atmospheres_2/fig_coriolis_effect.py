"""Generate Fig. (`fig:coriolis`).

Two-panel schematic of the Coriolis effect viewed from above the
North Pole.

Left panel (inertial frame): a parcel launched poleward from a low
latitude moves in a straight line; the surface beneath rotates east
with angular velocity Omega.

Right panel (rotating frame of the planet): the same parcel appears
to curve to the right of its motion in the Northern Hemisphere.

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


def draw_disk(ax) -> None:
    ax.add_patch(Circle((0, 0), 1.0, facecolor=DISK, edgecolor="black", lw=1.0))
    ax.plot(0, 0, "+", color="black", ms=12)
    ax.text(0.05, 0.05, "N pole", fontsize=9, ha="left", va="bottom")


def panel_left(ax) -> None:
    draw_disk(ax)
    # Arrow indicating Omega rotation (counterclockwise viewed from N)
    arc = Arc((0, 0), 2.4, 2.4, angle=0, theta1=10, theta2=80,
              color="black", lw=1.0)
    ax.add_patch(arc)
    ax.add_patch(FancyArrowPatch(
        (np.cos(np.radians(80)) * 1.2, np.sin(np.radians(80)) * 1.2),
        (np.cos(np.radians(85)) * 1.2, np.sin(np.radians(85)) * 1.2),
        arrowstyle="->", mutation_scale=12, color="black", lw=1.0))
    ax.text(0.95, 1.3, r"$\Omega$", fontsize=14, ha="left", va="bottom")

    # Launch point near south, parcel goes straight north
    launch = (0.0, -0.85)
    end = (0.0, 0.7)
    ax.plot(*launch, "o", color="#1f77b4", ms=10, zorder=5)
    ax.add_patch(FancyArrowPatch(launch, end,
                                 arrowstyle="->", mutation_scale=14,
                                 color="#1f77b4", lw=2.0))
    ax.text(launch[0] + 0.05, launch[1] - 0.03, "Launch\n(low latitude)",
            color="#1f77b4", fontsize=9, va="top")

    # Surface point that rotates east during flight: indicate launch point and
    # show the same patch of ground at the end of flight rotated by ~25 deg.
    rot_angle = np.radians(25.0)
    surf_x = launch[0] * np.cos(rot_angle) - launch[1] * np.sin(rot_angle)
    surf_y = launch[0] * np.sin(rot_angle) + launch[1] * np.cos(rot_angle)
    ax.plot(surf_x, surf_y, "s", color="#888", ms=10, zorder=4)
    ax.text(surf_x + 0.06, surf_y, "Surface point\n(rotated east)",
            color="#555", fontsize=9, va="center")

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Inertial (non-rotating) frame:\n"
                 "parcel travels in a straight line", fontsize=11)


def panel_right(ax) -> None:
    draw_disk(ax)
    # In the rotating frame, the parcel curves to the right (east in NH).
    # Parametric path: start at launch heading north (+y), bend eastward (+x).
    launch = (0.0, -0.85)
    ax.plot(*launch, "o", color="#d62728", ms=10, zorder=5)

    # Quadratic-in-t east drift, linear-in-t north drift. Initial tangent
    # (dx/dt, dy/dt) at t=0 is (0, b), purely northward (correct boundary
    # condition); curvature is to the east (parcel deflects right in NH).
    t = np.linspace(0, 1, 200)
    a = 0.85   # eastward drift coefficient (sets endpoint x)
    b = 1.55   # northward drift coefficient (sets endpoint y above origin)
    x = launch[0] + a * t ** 2
    y = launch[1] + b * t
    ax.plot(x, y, color="#d62728", lw=2.0)
    ax.add_patch(FancyArrowPatch(
        (x[-3], y[-3]), (x[-1], y[-1]),
        arrowstyle="->", mutation_scale=16, color="#d62728", lw=2.0))

    ax.text(launch[0] + 0.05, launch[1] - 0.05, "Launch\n(low latitude)",
            color="#d62728", fontsize=9, va="top")
    # Place "Deflection to the right" label near the actual end of the curve
    ax.text(x[-1] + 0.05, y[-1] + 0.05, "Deflection\nto the right",
            color="#d62728", fontsize=10, ha="left", va="bottom")

    # Reference straight line (greyed out)
    ax.plot([0, 0], [-0.85, 0.7], color="0.6", linestyle="--", lw=1.0)
    ax.text(0.05, 0.0, "Expected\n(no deflection)", color="0.5", fontsize=9,
            va="center", ha="left")

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Rotating (planet) frame:\n"
                 "parcel appears deflected to the right (NH)", fontsize=11)


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5))
    panel_left(axes[0])
    panel_right(axes[1])
    fig.suptitle(
        "Geometric origin of the Coriolis effect (view from above the North Pole)",
        fontsize=12, y=1.02)

    # Build a manual legend at the bottom
    handles = [
        plt.Line2D([0], [0], color="#1f77b4", lw=2, label="Parcel path (inertial frame)"),
        plt.Line2D([0], [0], color="#d62728", lw=2, label="Apparent path (rotating frame)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2,
               frameon=False, fontsize=10, bbox_to_anchor=(0.5, -0.02))

    fig.tight_layout(rect=(0, 0.04, 1, 1.0))
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
