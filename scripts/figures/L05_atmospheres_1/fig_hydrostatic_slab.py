"""Generate Fig. (`fig:hydrostatic-slab`).

Schematic of the force balance on a thin horizontal slab of atmosphere:
pressure P(z) A pushing up on the lower face, pressure P(z + dz) A
pushing down on the upper face, and the slab weight rho(z) g A dz.
Setting the net force to zero and taking dz -> 0 gives the equation
of hydrostatic equilibrium, dP/dz = -rho g.

Caption / figure id : `fig:hydrostatic-slab`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/hydrostatic_slab.avif"

BLUE = "#1f77b4"
RED = "#c93434"
GROUND = "#8b6648"
SKY = "#cfe5ff"
SLAB = "#9ec3e0"

COL_X0, COL_X1 = 0.35, 0.65
SLAB_Y0, SLAB_Y1 = 0.52, 0.62
AXIS_X = 0.14


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(6.5, 6.5))

    # Ground band and atmosphere column
    ax.add_patch(Rectangle((0, 0.0), 1, 0.10, color=GROUND, alpha=0.85))
    ax.text(0.5, 0.05, "Surface", ha="center", va="center",
            fontsize=11, weight="bold", color="white")
    ax.add_patch(Rectangle((COL_X0, 0.10), COL_X1 - COL_X0, 0.85,
                           facecolor=SKY, edgecolor="none", alpha=0.45))
    for x in (COL_X0, COL_X1):
        ax.plot([x, x], [0.10, 0.95], color="0.45", lw=1.0, ls="--")
    ax.text(0.5, 0.925, "Atmosphere\ncolumn", ha="center", va="center",
            fontsize=10, color="0.35")

    # Slab at height z with thickness dz
    ax.add_patch(Rectangle((COL_X0, SLAB_Y0), COL_X1 - COL_X0,
                           SLAB_Y1 - SLAB_Y0,
                           facecolor=SLAB, edgecolor="black", lw=1.2))
    ax.text(0.435, 0.57, r"$\rho(z)$", ha="center", va="center",
            fontsize=11)

    # Height axis with the slab faces marked at z and z + dz
    ax.add_patch(FancyArrowPatch((AXIS_X, 0.10), (AXIS_X, 0.92),
                                 arrowstyle="->", mutation_scale=14,
                                 color="black", lw=1.2))
    ax.text(AXIS_X, 0.945, r"$z$", ha="center", va="center", fontsize=12)
    for y, lab in ((SLAB_Y0, r"$z$"), (SLAB_Y1, r"$z + \mathrm{d}z$")):
        ax.plot([AXIS_X, COL_X0], [y, y], color="0.45", lw=0.8, ls=":")
        ax.text(AXIS_X - 0.015, y, lab, ha="right", va="center",
                fontsize=11)

    # Slab thickness marker on the right of the column
    ax.add_patch(FancyArrowPatch((0.68, SLAB_Y0), (0.68, SLAB_Y1),
                                 arrowstyle="<->", mutation_scale=10,
                                 color="black", lw=1.0))
    ax.text(0.70, 0.57, r"$\mathrm{d}z$", ha="left", va="center",
            fontsize=11)
    # Cross-sectional area labels the upper face directly
    ax.annotate(r"cross-section $A$", xy=(0.60, SLAB_Y1),
                xytext=(0.72, 0.70), fontsize=10,
                ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color="0.35", lw=0.8))

    # Pressure on the lower face pushes up
    ax.add_patch(FancyArrowPatch((0.46, 0.36), (0.46, SLAB_Y0 - 0.005),
                                 arrowstyle="->", mutation_scale=18,
                                 color=BLUE, lw=2.2))
    ax.text(0.485, 0.42, r"$P(z)\,A$", ha="left", va="center",
            fontsize=12, color=BLUE)

    # Pressure on the upper face pushes down
    ax.add_patch(FancyArrowPatch((0.46, 0.78), (0.46, SLAB_Y1 + 0.005),
                                 arrowstyle="->", mutation_scale=18,
                                 color=BLUE, lw=2.2))
    ax.text(0.485, 0.72, r"$P(z + \mathrm{d}z)\,A$", ha="left",
            va="center", fontsize=12, color=BLUE)

    # Weight of the slab acts down from its centre
    ax.add_patch(FancyArrowPatch((0.58, 0.565), (0.58, 0.40),
                                 arrowstyle="->", mutation_scale=18,
                                 color=RED, lw=2.2))
    ax.text(0.565, 0.355, r"$\rho(z)\,g\,A\,\mathrm{d}z$", ha="center",
            va="center", fontsize=12, color=RED)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
