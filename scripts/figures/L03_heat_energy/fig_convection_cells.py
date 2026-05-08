"""Generate Fig. (`fig:convection-cells`).

Schematic of Rayleigh-Bénard convection: a fluid layer of depth `d`
heated from below at `T_h` and cooled from above at `T_c`, with thin
hot and cold thermal boundary layers (TBLs) and alternating
hot-rising / cold-sinking plumes that close the circulation.

Caption / figure id : `fig:convection-cells`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : (textbook schematic)

Pure schematic, no input data.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/rayleigh_benard_schematic.avif"

COLD = "#1f77b4"
HOT = "#d62728"


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(10, 5))

    # Domain: x in [0, 10], y in [0, 5]; box from (0.5, 0.5) to (9.5, 4.5)
    x0, x1 = 0.5, 9.5
    y0, y1 = 0.5, 4.5
    tbl_h = 0.4

    # Outer hot/cold plates
    ax.add_patch(Rectangle((x0, y1), x1 - x0, 0.25, color=COLD, alpha=0.85, zorder=1))
    ax.add_patch(Rectangle((x0, y0 - 0.25), x1 - x0, 0.25, color=HOT, alpha=0.85, zorder=1))

    # Convection cell box
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0,
                           fill=False, edgecolor="black", lw=1.4, zorder=2))

    # Cold and hot TBLs (shaded inside box, top and bottom)
    ax.add_patch(Rectangle((x0, y1 - tbl_h), x1 - x0, tbl_h,
                           color=COLD, alpha=0.18, zorder=1.5))
    ax.add_patch(Rectangle((x0, y0), x1 - x0, tbl_h,
                           color=HOT, alpha=0.18, zorder=1.5))

    # TBL labels
    ax.text(x0 + 0.25, y1 - tbl_h / 2, "Cold TBL", color=COLD,
            fontsize=10, va="center", ha="left")
    ax.text(x0 + 0.25, y0 + tbl_h / 2, "Hot TBL", color=HOT,
            fontsize=10, va="center", ha="left")

    # Plate labels
    ax.text((x0 + x1) / 2, y1 + 0.45, r"$T_c$ (cold)", color=COLD,
            fontsize=13, ha="center", va="bottom")
    ax.text((x0 + x1) / 2, y0 - 0.45, r"$T_h$ (hot)", color=HOT,
            fontsize=13, ha="center", va="top")

    # Plumes: alternating hot-rising / cold-sinking
    plume_x = [2.0, 3.7, 5.5, 7.3, 9.0]
    plume_kind = ["down", "up", "down", "up", "down"]
    for px, kind in zip(plume_x, plume_kind):
        if kind == "up":
            ax.add_patch(FancyArrowPatch(
                (px, y0 + tbl_h), (px, y1 - tbl_h),
                arrowstyle="->", mutation_scale=18, color=HOT, lw=2.0))
        else:
            ax.add_patch(FancyArrowPatch(
                (px, y1 - tbl_h), (px, y0 + tbl_h),
                arrowstyle="->", mutation_scale=18, color=COLD, lw=2.0))

    # Plume labels
    ax.text(3.7, (y0 + y1) / 2, "Hot rising", color=HOT,
            fontsize=11, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=2))
    ax.text(5.5, (y0 + y1) / 2, "Cold sinking", color=COLD,
            fontsize=11, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=2))
    ax.text(7.3, (y0 + y1) / 2, "Hot rising", color=HOT,
            fontsize=11, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=2))

    # Lateral boundary-layer flow arrows (start past the TBL labels)
    ax.add_patch(FancyArrowPatch(
        (x0 + 1.7, y1 - tbl_h / 2), (x0 + 3.2, y1 - tbl_h / 2),
        arrowstyle="->", mutation_scale=12, color=COLD, lw=1.2))
    ax.add_patch(FancyArrowPatch(
        (x1 - 3.2, y1 - tbl_h / 2), (x1 - 0.7, y1 - tbl_h / 2),
        arrowstyle="->", mutation_scale=12, color=COLD, lw=1.2))
    ax.add_patch(FancyArrowPatch(
        (x0 + 1.7, y0 + tbl_h / 2), (x0 + 3.2, y0 + tbl_h / 2),
        arrowstyle="->", mutation_scale=12, color=HOT, lw=1.2))
    ax.add_patch(FancyArrowPatch(
        (x1 - 3.2, y0 + tbl_h / 2), (x1 - 0.7, y0 + tbl_h / 2),
        arrowstyle="->", mutation_scale=12, color=HOT, lw=1.2))

    # Heat in / heat out arrows outside box
    ax.add_patch(FancyArrowPatch(
        (x1 + 0.4, y1 + 0.1), (x1 + 0.4, y1 + 0.8),
        arrowstyle="->", mutation_scale=15, color=COLD, lw=1.5))
    ax.text(x1 + 0.6, y1 + 0.55, r"heat out $q$",
            color=COLD, fontsize=10, va="center")
    ax.add_patch(FancyArrowPatch(
        (x0 + 0.6, y0 - 0.7), (x0 + 0.6, y0 - 0.1),
        arrowstyle="->", mutation_scale=15, color=HOT, lw=1.5))
    ax.text(x0 + 0.85, y0 - 0.45, r"heat in $q$",
            color=HOT, fontsize=10, va="center")

    # Depth indicator d on the right
    ax.annotate("", xy=(x1 + 0.05, y0), xytext=(x1 + 0.05, y1),
                arrowprops=dict(arrowstyle="<->", lw=1.0, color="black"))
    ax.text(x1 + 0.15, (y0 + y1) / 2, r"$d$", fontsize=14, va="center")

    ax.set_xlim(-0.2, 10.5)
    ax.set_ylim(-0.6, 5.4)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
