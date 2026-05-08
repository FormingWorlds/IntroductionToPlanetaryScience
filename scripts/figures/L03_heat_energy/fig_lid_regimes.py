"""Generate Fig. (`fig:lid-regimes`).

End-member tectonic regimes for rocky planets: mobile lid (left,
plate tectonics on Earth) vs stagnant lid (right, Mars / Venus /
Mercury / Moon).

Caption / figure id : `fig:lid-regimes`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : (textbook schematic; cited as Stevenson2003 / textbook)

Pure schematic, no input data.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/lid_regimes.avif"

MANTLE = "#f5d3a0"   # warm sandy
LID = "#5b8caf"      # blue-grey
RED = "#d62728"
BLUE_DK = "#1f4e79"
GREY = "#444444"


def draw_panel(ax, mode: str) -> None:
    """Draw one panel; mode in {'mobile', 'stagnant'}."""
    # Panel frame: x in [0, 10], mantle 0-3, lid 3-3.7, surface above 3.7
    x0, x1 = 0.0, 10.0
    y_floor = 0.0
    y_lid_bottom = 3.0
    y_lid_top = 3.7
    y_top = 4.2

    # Mantle
    ax.add_patch(Rectangle((x0, y_floor), x1 - x0, y_lid_bottom - y_floor,
                           color=MANTLE, zorder=1))
    # Lid
    ax.add_patch(Rectangle((x0, y_lid_bottom), x1 - x0, y_lid_top - y_lid_bottom,
                           color=LID, alpha=0.85, zorder=1.5))

    # Outline
    ax.add_patch(Rectangle((x0, y_floor), x1 - x0, y_lid_top - y_floor,
                           fill=False, edgecolor="black", lw=1.4, zorder=3))

    ax.text((x0 + x1) / 2, 0.4, "core", color=GREY,
            fontsize=10, ha="center", va="center", zorder=4)

    if mode == "mobile":
        ax.set_title("Mobile lid: plate tectonics (Earth)", fontsize=12, pad=8)

        # Ridge in middle (small gap in lid)
        ridge_x = 3.0
        ax.add_patch(Rectangle((ridge_x - 0.07, y_lid_bottom),
                               0.14, y_lid_top - y_lid_bottom,
                               color="white", zorder=2))

        # Two diverging arrows above ridge
        ax.add_patch(FancyArrowPatch(
            (ridge_x, y_lid_top - 0.05), (ridge_x - 1.0, y_lid_top + 0.4),
            arrowstyle="->", mutation_scale=14, color=RED, lw=1.5, zorder=4))
        ax.add_patch(FancyArrowPatch(
            (ridge_x, y_lid_top - 0.05), (ridge_x + 1.0, y_lid_top + 0.4),
            arrowstyle="->", mutation_scale=14, color=RED, lw=1.5, zorder=4))
        ax.text(ridge_x - 1.2, y_top, "ridge", color=RED, fontsize=11, ha="left")

        # Subducting slab: curved line plus tail
        slab_t = np.linspace(0, 1, 50)
        slab_x = ridge_x + 0.3 + 1.5 * slab_t
        slab_y = y_lid_bottom - 1.6 * slab_t ** 1.6
        ax.plot(slab_x, slab_y, color=BLUE_DK, lw=3.5, zorder=4)
        # Arrow tip on slab
        ax.add_patch(FancyArrowPatch(
            (slab_x[-3], slab_y[-3]), (slab_x[-1], slab_y[-1]),
            arrowstyle="->", mutation_scale=18, color=BLUE_DK, lw=3.0, zorder=4))
        ax.text(slab_x[-1] - 0.1, slab_y[-1] - 0.3, "subducting\nslab",
                color=BLUE_DK, fontsize=10, ha="center", va="top")

        # Hotspot plume on right
        hs_x = 7.5
        ax.add_patch(FancyArrowPatch(
            (hs_x, 0.6), (hs_x, y_top),
            arrowstyle="->", mutation_scale=15, color=RED, lw=2.0, zorder=4))
        ax.text(hs_x, y_top + 0.1, "hotspot", color=RED, fontsize=11, ha="center")

    else:
        ax.set_title("Stagnant lid (Mars, Venus, Moon)", fontsize=12, pad=8)
        ax.text((x0 + x1) / 2, (y_lid_top + y_lid_bottom) / 2,
                "rigid stagnant lid", color=BLUE_DK, fontsize=12,
                ha="center", va="center", weight="bold", zorder=4)

        # Conductive heat-loss arrows across lid (small upward grey)
        for hx in [1.5, 4.5, 6.0, 8.5]:
            ax.add_patch(FancyArrowPatch(
                (hx, y_lid_top - 0.05), (hx, y_top),
                arrowstyle="->", mutation_scale=10, color=GREY, lw=1.0, zorder=4))
        ax.text(2.5, y_top + 0.05, "conductive heat loss",
                color=GREY, fontsize=11, ha="center")

        # Volcanism: thick red arrow puncturing the lid in middle
        vx = 5.0
        ax.add_patch(FancyArrowPatch(
            (vx, 1.0), (vx, y_top),
            arrowstyle="->", mutation_scale=18, color=RED, lw=2.6, zorder=5))
        ax.text(vx, y_top + 0.05, "volcanism",
                color=RED, fontsize=11, ha="center")

        # Sub-lid convection cells (two ellipses with circulating arrows)
        for cx in [2.5, 7.5]:
            ax.add_patch(Ellipse((cx, 1.6), 2.4, 1.0, fill=False,
                                 edgecolor=RED, lw=1.3, zorder=4))
            # small arrow on ellipse to indicate direction
            ax.add_patch(FancyArrowPatch(
                (cx + 0.05, 1.1), (cx + 0.55, 1.4),
                arrowstyle="->", mutation_scale=10, color=RED, lw=1.2, zorder=5))

    ax.set_xlim(x0 - 0.3, x1 + 0.3)
    ax.set_ylim(y_floor - 0.3, y_top + 0.6)
    ax.set_aspect("equal")
    ax.axis("off")


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 4.6))
    draw_panel(axes[0], "mobile")
    draw_panel(axes[1], "stagnant")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
