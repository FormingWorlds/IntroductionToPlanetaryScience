"""Generate Fig. (`fig:whole-vs-layered`).

Schematic contrast of the two candidate styles of mantle convection:
layered convection, with separate circulation systems above and below
the 660 km discontinuity, and whole-mantle convection, with slabs
sinking through 660 km and plumes rising from the core-mantle boundary.

Caption / figure id : `fig:whole-vs-layered`
Markdown source     : book/03_heat_energy/heat_energy.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/whole_vs_layered_convection.avif"

# Panel geometry (arbitrary units): x in [0, 10], depth axis y in [0, 10]
# with the surface at y = 10 and the core-mantle boundary at y = 0.
Y_SURF = 10.0
Y_660 = 7.7    # 660 km of 2890 km total depth, to scale
Y_CMB = 0.0

C_MANTLE_UP = "#fdf0dc"   # upper mantle fill
C_MANTLE_LO = "#f7e2c0"   # lower mantle fill
C_CORE = "#d9d9d9"
C_CELL = "#8c6d46"        # circulation arrows
C_SLAB = "#1f77b4"
C_PLUME = "#d62728"
C_LINE = "#333333"


def _cell(ax, cx, cy, rx, ry, sense=1, color=C_CELL, lw=1.6):
    """Draw one convection cell as two arc arrows closing a loop.

    sense=+1 draws a clockwise cell, sense=-1 counter-clockwise.
    """
    style = "Simple,head_length=5,head_width=4,tail_width=1.2"
    top = FancyArrowPatch(
        (cx - sense * rx, cy), (cx + sense * rx, cy),
        connectionstyle=f"arc3,rad={-0.9 * ry / rx:.3f}",
        arrowstyle=style, color=color, lw=0, zorder=4)
    bot = FancyArrowPatch(
        (cx + sense * rx, cy), (cx - sense * rx, cy),
        connectionstyle=f"arc3,rad={-0.9 * ry / rx:.3f}",
        arrowstyle=style, color=color, lw=0, zorder=4)
    ax.add_patch(top)
    ax.add_patch(bot)


def _frame(ax, title):
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.1, Y_SURF + 0.4)
    ax.axis("off")
    ax.set_title(title, fontsize=12)
    # mantle fills and core
    ax.add_patch(Rectangle((0, Y_660), 10, Y_SURF - Y_660,
                           fc=C_MANTLE_UP, ec="none", zorder=0))
    ax.add_patch(Rectangle((0, Y_CMB), 10, Y_660,
                           fc=C_MANTLE_LO, ec="none", zorder=0))
    ax.add_patch(Rectangle((0, -1.1), 10, 1.1, fc=C_CORE, ec="none", zorder=0))
    ax.plot([0, 10], [Y_SURF, Y_SURF], color=C_LINE, lw=2.0, zorder=3)
    ax.plot([0, 10], [Y_CMB, Y_CMB], color=C_LINE, lw=2.0, zorder=3)
    ax.plot([0, 0], [-1.1, Y_SURF], color=C_LINE, lw=1.0, zorder=3)
    ax.plot([10, 10], [-1.1, Y_SURF], color=C_LINE, lw=1.0, zorder=3)
    ax.text(-0.25, Y_SURF, "0 km", ha="right", va="center", fontsize=9)
    ax.text(-0.25, Y_660, "660 km", ha="right", va="center", fontsize=9)
    ax.text(-0.25, Y_CMB, "2890 km", ha="right", va="center", fontsize=9)
    ax.text(9.75, -0.55, "core", ha="right", va="center",
            fontsize=9, style="italic", color="#555555")


def make_plot() -> Path:
    apply_style()
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(9.2, 4.4))

    # Left: layered convection
    _frame(axl, "Layered convection")
    axl.plot([0, 10], [Y_660, Y_660], color=C_LINE, lw=2.2,
             linestyle=(0, (5, 3)), zorder=3)
    for cx, sense in [(2.0, 1), (5.0, -1), (8.0, 1)]:
        _cell(axl, cx, (Y_SURF + Y_660) / 2, 1.25, 0.85, sense=sense)
    for cx, sense in [(2.7, -1), (7.3, 1)]:
        _cell(axl, cx, Y_660 / 2, 2.0, 3.0, sense=sense)
    axl.text(5.0, Y_660 - 0.35, "impermeable boundary: no mass exchange",
             ha="center", va="top", fontsize=9, color=C_LINE, zorder=5,
             bbox=dict(fc="white", ec="none", alpha=0.75, pad=1.5))
    axl.text(5.0, 0.65, "separate lower-mantle cells", ha="center",
             va="center", fontsize=9, color="#6b4f2a", zorder=5,
             bbox=dict(fc="white", ec="none", alpha=0.6, pad=1.0))

    # Right: whole-mantle convection
    _frame(axr, "Whole-mantle convection")
    axr.plot([0, 10], [Y_660, Y_660], color=C_LINE, lw=1.0,
             linestyle=(0, (2, 4)), zorder=3)
    axr.text(0.25, Y_660 + 0.25, "partial barrier only", ha="left",
             va="bottom", fontsize=8.5, color="#555555", zorder=5)
    # one mantle-depth circulation between the slab and the plume
    _cell(axr, 5.9, 5.0, 1.4, 3.9, sense=1)
    # subducting slab: from the surface through 660 km to the deep mantle
    slab_x = [1.4, 2.3, 3.0, 3.5, 3.8]
    slab_y = [Y_SURF, 7.6, 5.2, 2.8, 1.0]
    axr.plot(slab_x, slab_y, color=C_SLAB, lw=5.0,
             solid_capstyle="round", zorder=4)
    axr.annotate("", xy=(4.0, 0.55), xytext=(3.65, 1.55),
                 arrowprops=dict(arrowstyle="-|>", color=C_SLAB, lw=2.0))
    axr.text(0.35, 3.6, "slab sinks\nthrough\n660 km", ha="left", va="center",
             fontsize=9, color=C_SLAB)
    # plume: conduit from the CMB with a bulbous head below the surface
    axr.plot([8.6, 8.6], [0.1, 9.95], color=C_PLUME, lw=3.5,
             solid_capstyle="round", zorder=4)
    axr.add_patch(Circle((8.6, 8.8), 0.55, fc=C_PLUME, ec="none", zorder=4))
    axr.add_patch(Polygon([[8.2, Y_SURF], [9.0, Y_SURF], [8.6, 10.35]],
                          closed=True, fc="#7f4f24", ec="none", zorder=5))
    axr.text(9.75, 4.4, "plume rises\nfrom the CMB", ha="right", va="center",
             fontsize=9, color=C_PLUME, zorder=5,
             bbox=dict(fc=C_MANTLE_LO, ec="none", alpha=0.8, pad=1.0))

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
