"""Generate Fig. (`fig:plume-vs-ridge`).

Schematic contrast of the two modes of mantle upwelling: passive
upwelling beneath a mid-ocean ridge, where diverging plates draw
ambient-temperature mantle upward, and active upwelling in a mantle
plume, a buoyant column of anomalously hot material rising from the
deep mantle beneath a moving plate.

Caption / figure id : `fig:plume-vs-ridge`
Markdown source     : book/03_heat_energy/heat_energy.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/plume_vs_ridge_upwelling.avif"

Y_SURF = 8.0

C_MANTLE = "#f7e2c0"
C_LITH = "#9db8cc"
C_MELT = "#e8735a"
C_PLUME = "#d62728"
C_AMBIENT = "#b08d57"
C_LINE = "#333333"


def _frame(ax, title):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title(title, fontsize=12)
    ax.add_patch(Rectangle((0, 0), 10, Y_SURF, fc=C_MANTLE, ec="none", zorder=0))
    ax.plot([0, 0], [0, Y_SURF], color=C_LINE, lw=1.0, zorder=3)
    ax.plot([10, 10], [0, Y_SURF], color=C_LINE, lw=1.0, zorder=3)
    ax.plot([0, 10], [0, 0], color=C_LINE, lw=1.5, zorder=3)


def _up_arrow(ax, x, y0, y1, color, width=8, alpha=1.0):
    ax.add_patch(FancyArrowPatch(
        (x, y0), (x, y1),
        arrowstyle=f"Simple,head_length={1.6 * width},"
                   f"head_width={1.9 * width},tail_width={width}",
        color=color, alpha=alpha, lw=0, zorder=2))


def make_plot() -> Path:
    apply_style()
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(9.2, 4.3))

    # Left: mid-ocean ridge, passive upwelling
    _frame(axl, "Mid-ocean ridge: passive upwelling")
    # lithosphere wedges thickening away from the ridge axis
    axl.add_patch(Polygon([[0, Y_SURF], [4.8, Y_SURF], [4.8, 7.85],
                           [3.2, 7.5], [0, 6.7]],
                          closed=True, fc=C_LITH, ec="none", zorder=2))
    axl.add_patch(Polygon([[10, Y_SURF], [5.2, Y_SURF], [5.2, 7.85],
                           [6.8, 7.5], [10, 6.7]],
                          closed=True, fc=C_LITH, ec="none", zorder=2))
    axl.plot([0, 10], [Y_SURF, Y_SURF], color=C_LINE, lw=2.0, zorder=4)
    axl.add_patch(Polygon([[4.6, Y_SURF], [5.4, Y_SURF], [5.0, 8.4]],
                          closed=True, fc="#5a7a94", ec="none", zorder=4))
    # diverging plate-motion arrows
    axl.annotate("", xy=(1.6, 8.65), xytext=(3.6, 8.65),
                 arrowprops=dict(arrowstyle="-|>", color=C_LINE, lw=1.8))
    axl.annotate("", xy=(8.4, 8.65), xytext=(6.4, 8.65),
                 arrowprops=dict(arrowstyle="-|>", color=C_LINE, lw=1.8))
    axl.text(5.0, 9.35, "plates pull apart", ha="center", va="bottom",
             fontsize=9.5, color=C_LINE)
    # broad passive upwelling of ambient-temperature mantle
    _up_arrow(axl, 5.0, 1.0, 6.2, C_AMBIENT, width=14, alpha=0.75)
    _up_arrow(axl, 3.4, 1.6, 5.0, C_AMBIENT, width=7, alpha=0.55)
    _up_arrow(axl, 6.6, 1.6, 5.0, C_AMBIENT, width=7, alpha=0.55)
    # decompression melting zone under the ridge axis
    axl.add_patch(Polygon([[4.2, 7.7], [5.8, 7.7], [5.0, 5.9]],
                          closed=True, fc=C_MELT, ec="none",
                          alpha=0.85, zorder=3))
    axl.text(6.05, 6.6, "decompression\nmelting", ha="left", va="center",
             fontsize=9, color="#b04a34")
    axl.text(5.0, 0.55, "broad, ambient mantle temperature",
             ha="center", va="bottom", fontsize=9, color="#7a6134",
             bbox=dict(fc="white", ec="none", alpha=0.6, pad=1.0))

    # Right: mantle plume, active upwelling
    _frame(axr, "Mantle plume: active upwelling")
    axr.add_patch(Rectangle((0, 7.1), 10, Y_SURF - 7.1,
                            fc=C_LITH, ec="none", zorder=2))
    axr.plot([0, 10], [Y_SURF, Y_SURF], color=C_LINE, lw=2.0, zorder=4)
    axr.annotate("", xy=(9.7, 9.0), xytext=(7.9, 9.0),
                 arrowprops=dict(arrowstyle="-|>", color=C_LINE, lw=1.8))
    axr.text(8.8, 9.35, "plate moves", ha="center", va="bottom",
             fontsize=9.5, color=C_LINE)
    # narrow hot conduit from the deep mantle with a bulbous head
    axr.plot([4.0, 4.0], [0.1, 6.5], color=C_PLUME, lw=4.5,
             solid_capstyle="round", zorder=3)
    axr.add_patch(Circle((4.0, 6.55), 0.75, fc=C_PLUME, ec="none", zorder=3))
    axr.plot([4.0, 4.0], [6.6, 8.5], color=C_PLUME, lw=2.2, zorder=3)
    _up_arrow(axr, 4.0, 2.2, 4.6, "#ffffff", width=3.5, alpha=0.85)
    # hotspot volcano above the head, older cone carried downstream
    axr.add_patch(Polygon([[3.4, Y_SURF], [4.6, Y_SURF], [4.0, 8.85]],
                          closed=True, fc="#7f4f24", ec="none", zorder=5))
    for dx in (-0.18, 0.0, 0.18):
        axr.plot([4.0, 4.0 + 2.2 * dx], [8.85, 9.35],
                 color=C_PLUME, lw=1.4, zorder=5)
    axr.add_patch(Polygon([[6.3, Y_SURF], [7.1, Y_SURF], [6.7, 8.5]],
                          closed=True, fc="#a08b76", ec="none", zorder=5))
    axr.text(6.7, 8.62, "extinct", ha="center", va="bottom",
             fontsize=8, color="#7a6a58")
    axr.text(4.45, 3.4, "narrow conduit,\n$\\Delta T \\approx$ 200 to 300 K",
             ha="left", va="center", fontsize=9, color=C_PLUME)
    axr.text(5.0, 0.55, "rooted in the deep mantle", ha="center", va="bottom",
             fontsize=9, color="#7a6134",
             bbox=dict(fc="white", ec="none", alpha=0.6, pad=1.0))

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
