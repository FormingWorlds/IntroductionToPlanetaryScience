"""Generate Fig. (`fig:heat-pipe`).

Schematic of the heat-pipe mode of planetary heat transport: melt from
a partially molten interior ascends through narrow volcanic conduits,
erupts, and buries older flows, so the thick cold lithosphere advects
downward between the pipes. Io is the type example.

Caption / figure id : `fig:heat-pipe`
Markdown source     : book/03_heat_energy/heat_energy.md
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/heat_pipe.avif"

Y_SURF = 7.2
Y_MELT = 2.2

C_LITH = "#cfd8de"
C_MELT = "#e8735a"
C_MAGMA = "#d62728"
C_LINE = "#333333"
C_DOWN = "#1f77b4"


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # cold lithosphere above a partially molten interior
    ax.add_patch(Rectangle((0, Y_MELT), 10, Y_SURF - Y_MELT,
                           fc=C_LITH, ec="none", zorder=0))
    ax.add_patch(Rectangle((0, 0), 10, Y_MELT, fc=C_MELT, ec="none", zorder=0))
    ax.plot([0, 10], [Y_SURF, Y_SURF], color=C_LINE, lw=2.0, zorder=4)
    ax.plot([0, 10], [Y_MELT, Y_MELT], color="#b04a34", lw=1.2,
            linestyle=(0, (4, 3)), zorder=3)
    ax.plot([0, 0], [0, Y_SURF], color=C_LINE, lw=1.0, zorder=4)
    ax.plot([10, 10], [0, Y_SURF], color=C_LINE, lw=1.0, zorder=4)
    ax.plot([0, 10], [0, 0], color=C_LINE, lw=1.5, zorder=4)

    # buried older flows: stratified layers that sag under new deposits
    for y0 in np.linspace(2.9, 6.7, 6):
        x = np.linspace(0.15, 9.85, 200)
        sag = 0.22 * np.exp(-((x - 5.0) ** 2) / 4.5)
        ax.plot(x, y0 - sag * (Y_SURF - y0), color="#8fa1ad", lw=0.8, zorder=1)

    # two volcanic conduits feeding surface eruptions
    for xc in (3.0, 7.0):
        ax.plot([xc, xc], [Y_MELT - 0.3, Y_SURF + 0.55],
                color=C_MAGMA, lw=4.0, solid_capstyle="round", zorder=3)
        ax.add_patch(Polygon([[xc - 0.55, Y_SURF], [xc + 0.55, Y_SURF],
                              [xc, Y_SURF + 0.75]],
                             closed=True, fc="#7f4f24", ec="none", zorder=5))
        for dx in (-0.3, 0.0, 0.3):
            ax.plot([xc, xc + dx], [Y_SURF + 0.75, Y_SURF + 1.3],
                    color=C_MAGMA, lw=1.3, zorder=5)
        ax.add_patch(FancyArrowPatch(
            (xc, 2.8), (xc, 4.6),
            arrowstyle="Simple,head_length=7,head_width=8,tail_width=2.5",
            color="#ffffff", alpha=0.9, lw=0, zorder=4))
    # a sill: melt intruded sideways from a conduit
    ax.plot([3.0, 4.4], [4.4, 4.55], color=C_MAGMA, lw=2.6,
            solid_capstyle="round", zorder=3)

    # fresh deposits on the surface
    for x0 in np.linspace(0.4, 9.2, 12):
        ax.plot([x0, x0 + 0.45], [Y_SURF + 0.1, Y_SURF + 0.1],
                color=C_MAGMA, lw=2.0, zorder=4)

    # downward advection of the buried lithosphere between the pipes
    for xd in (1.3, 5.0, 8.7):
        ax.add_patch(FancyArrowPatch(
            (xd, 6.4), (xd, 4.4),
            arrowstyle="Simple,head_length=8,head_width=9,tail_width=3",
            color=C_DOWN, alpha=0.85, lw=0, zorder=2))

    # labels
    ax.text(5.0, 9.5, "eruptions resurface the planet; old flows are buried",
            ha="center", va="bottom", fontsize=10, color=C_LINE)
    ax.text(1.3, 7.75, "new deposits\nload the surface", ha="center",
            va="bottom", fontsize=8.5, color=C_LINE, zorder=5)
    ax.text(5.0, 3.75, "cold lithosphere\nadvects downward", ha="center",
            va="top", fontsize=9, color=C_DOWN, zorder=5,
            bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.0))
    ax.text(3.55, 5.05, "melt ascends\nin narrow pipes", ha="left",
            va="bottom", fontsize=9, color=C_MAGMA, zorder=5,
            bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.0))
    ax.text(4.5, 4.9, "sill", ha="center", va="top", fontsize=8.5,
            color=C_MAGMA, zorder=5)
    ax.text(9.75, 1.1, "partially molten interior", ha="right", va="center",
            fontsize=9.5, color="#8c2f1b", zorder=5)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
