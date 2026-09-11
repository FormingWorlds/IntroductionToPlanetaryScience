"""A global magnetic field as a shield for the atmosphere.

Left: a magnetised planet deflects the solar wind around its
magnetosphere. Right: an unmagnetised planet loses atmosphere by
sputtering and ion pickup. Schematic, not to scale.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/magnetic_shielding.avif"

WIND = "#e6550d"
FIELD = "#1f6db8"
ATM = "#a6cee3"


def _planet(ax: plt.Axes, atm: float) -> None:
    ax.add_patch(Circle((0, 0), atm, facecolor=ATM, edgecolor="none", alpha=0.7))
    ax.add_patch(Circle((0, 0), 1.0, facecolor="#8c7b6b", edgecolor="0.2", lw=1.2))


def make_plot() -> plt.Figure:
    """Build the two-panel schematic, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2))
    for ax in (ax1, ax2):
        ax.set_xlim(-5.2, 3.4)
        ax.set_ylim(-3.2, 3.4)
        ax.set_aspect("equal")
        ax.axis("off")
    ax1.set_title("(a) Global field: solar wind deflected", fontsize=11)
    ax2.set_title("(b) No global field: atmosphere eroded", fontsize=11)
    _planet(ax1, 1.35)
    # dipole field lines
    for r0 in (1.6, 2.2, 2.9):
        th = np.linspace(0.12, np.pi - 0.12, 120)
        r = r0 * np.sin(th) ** 2
        for sgn in (1, -1):
            ax1.plot(sgn * r * np.sin(th), r * np.cos(th), color=FIELD, lw=1.2)
    # magnetopause and deflected wind
    th = np.linspace(-1.35, 1.35, 100)
    ax1.plot(-3.2 * np.cos(th) ** 0.5, 3.4 * np.sin(th), color=FIELD, lw=1.6, ls="--")
    for y in (2.6, 1.3, 0.0, -1.3, -2.6):
        end = (-3.35, y) if abs(y) > 2 else (-3.55 + 0.25 * abs(y) / 1.3, y)
        ax1.add_patch(FancyArrowPatch((-5.0, y), end, arrowstyle="-|>", mutation_scale=10, color=WIND, lw=1.5))
    ax1.text(-4.9, 3.15, "solar wind", fontsize=10, color=WIND)
    ax1.text(-2.4, -2.25, "magnetopause", fontsize=10, color=FIELD)
    ax1.text(2.0, 2.6, "field lines", fontsize=10, color=FIELD)
    _planet(ax2, 1.35)
    for y in (2.6, 1.3, 0.0, -1.3, -2.6):
        ax2.add_patch(FancyArrowPatch((-5.0, y), (-1.4 if abs(y) < 1.3 else -1.0, y), arrowstyle="-|>", mutation_scale=10, color=WIND, lw=1.5))
    for ang, lab in ((60, "sputtered atoms"), (-55, "picked-up ions")):
        a = np.radians(ang)
        ax2.add_patch(FancyArrowPatch((1.3 * np.cos(a), 1.3 * np.sin(a)), (2.9 * np.cos(a), 2.9 * np.sin(a)), arrowstyle="-|>", mutation_scale=10, color="0.25", lw=1.4, ls=":"))
    ax2.text(1.3, 3.0, "sputtering", fontsize=10, color="0.25")
    ax2.text(1.3, -2.95, "ion pickup", fontsize=10, color="0.25")
    ax2.text(-4.9, 3.15, "solar wind", fontsize=10, color=WIND)
    ax2.text(-4.9, -3.05, "Mars after its dynamo died, about 4 Gyr ago", fontsize=10, color="0.3")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02, wspace=0.04)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
