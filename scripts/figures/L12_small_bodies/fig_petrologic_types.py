"""Petrographic types and shock stages in chondritic meteorites.

Type 3 chondrites are the least altered, with types 2 to 1 recording
aqueous alteration and types 4 to 7 recording thermal metamorphism.
Shock stages S1 to S6 record impact pressures up to tens of GPa.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/12_small_bodies/figures/petrologic_types.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(0.0, 10.0)
    ax.axis("off")
    ax.set_title("Two scales that record what happened on the parent body", fontsize=11, pad=12)

    # Top scale: Petrographic type scale 1 to 7
    # "The petrographic type of a chondrite, on a scale from 1 to 7, records how much its parent body altered it after accretion."
    ax.text(5.0, 9.4, "Petrographic type (scale 1 to 7)", ha="center", va="center", fontsize=10, weight="bold", color="0.2")

    # 7 boxes for types 1 to 7
    w_box = 1.05
    h_box = 0.85
    gap = 0.22
    total_w = 7 * w_box + 6 * gap
    x_start = (10.0 - total_w) / 2
    y_box_top = 6.2

    box_centers = []
    for i in range(7):
        x_b = x_start + i * (w_box + gap)
        xc = x_b + w_box / 2
        box_centers.append(xc)
        ptype = i + 1
        if ptype == 3:
            # Box 3 least altered
            # "By convention, type 3 is the least altered."
            fc, ec, lw = "#e8f5e9", "#2ca25f", 1.8
            tc = "#2ca25f"
        elif ptype < 3:
            # Types 2 and 1 aqueous alteration
            # "Types 2 and 1 record progressively heavier aqueous alteration"
            fc, ec, lw = "#e8f1fa", "#1f6db8", 1.2
            tc = "#1f6db8"
        else:
            # Types 4 through 7 thermal metamorphism
            # "Types 4 through 7 record increasing thermal metamorphism"
            fc, ec, lw = "#fdebd0", "#c46b1a", 1.2
            tc = "#c46b1a"
        patch = FancyBboxPatch(
            (x_b, y_box_top), w_box, h_box,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=fc, edgecolor=ec, lw=lw,
        )
        ax.add_patch(patch)
        ax.text(xc, y_box_top + h_box / 2, f"Type {ptype}", ha="center", va="center", fontsize=10, weight="bold", color=tc)

    # Box 3 highlight label
    ax.text(box_centers[2], y_box_top - 0.22, "least altered", ha="center", va="top", fontsize=10, weight="bold", color="#2ca25f")

    # Arrow left from 3 over 2 and 1
    # "aqueous alteration, where low-temperature reactions with water form clays and erase original chondrules"
    y_arr_top = 7.7
    ax.add_patch(FancyArrowPatch(
        (box_centers[2] - 0.4, y_arr_top), (box_centers[0] - 0.4, y_arr_top),
        arrowstyle="-|>", mutation_scale=12, color="#1f6db8", lw=1.6,
    ))
    ax.text(
        (box_centers[2] + box_centers[0]) / 2 - 0.4, y_arr_top + 0.55,
        "aqueous alteration:\nwater forms clays, erases chondrules",
        ha="center", va="center", fontsize=10, color="#1f6db8",
    )

    # Arrow right from 3 over 4 to 7
    # "thermal metamorphism, where higher temperatures coarsen mineral grains, equilibrate compositions, and destroy chondrule outlines"
    ax.add_patch(FancyArrowPatch(
        (box_centers[2] + 0.4, y_arr_top), (box_centers[6] + 0.4, y_arr_top),
        arrowstyle="-|>", mutation_scale=12, color="#c46b1a", lw=1.6,
    ))
    ax.text(
        (box_centers[2] + box_centers[6]) / 2 + 0.4, y_arr_top + 0.55,
        "thermal metamorphism: grains coarsen,\ncompositions equilibrate, chondrule outlines vanish",
        ha="center", va="center", fontsize=10, color="#c46b1a",
    )

    # Bottom scale: Shock stage S1 to S6
    # "The shock stage, denoted S1 (unshocked) through S6 (heavily shocked, partially melted), records impact history"
    ax.text(5.0, 4.6, "Shock stage (scale S1 to S6)", ha="center", va="center", fontsize=10, weight="bold", color="0.2")

    w_sbox = 1.15
    h_sbox = 0.85
    gap_s = 0.28
    total_sw = 6 * w_sbox + 5 * gap_s
    x_start_s = (10.0 - total_sw) / 2
    y_box_bot = 2.0

    sbox_centers = []
    for i in range(6):
        x_b = x_start_s + i * (w_sbox + gap_s)
        xc = x_b + w_sbox / 2
        sbox_centers.append(xc)
        stage = f"S{i+1}"
        if i == 0:
            fc, ec, lw = "#e8f1fa", "#4a6984", 1.2
            tc = "0.2"
        elif i == 5:
            fc, ec, lw = "#fdebd0", "#c0392b", 1.8
            tc = "#c0392b"
        else:
            fc, ec, lw = "#f5f5f5", "#4a6984", 1.0
            tc = "0.3"
        patch = FancyBboxPatch(
            (x_b, y_box_bot), w_sbox, h_sbox,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=fc, edgecolor=ec, lw=lw,
        )
        ax.add_patch(patch)
        ax.text(xc, y_box_bot + h_sbox / 2, stage, ha="center", va="center", fontsize=10, weight="bold", color=tc)

    # S1 and S6 annotations
    ax.text(sbox_centers[0], y_box_bot - 0.22, "unshocked", ha="center", va="top", fontsize=10, color="0.2")
    ax.text(sbox_centers[5], y_box_bot - 0.22, "heavily shocked,\npartially melted", ha="center", va="top", fontsize=10, color="#c0392b")

    # Bottom arrow: rightward over S1 to S6
    # "Shock features include planar fractures in olivine and pyroxene crystals, dark melt veins, and high-pressure minerals such as ringwoodite and majorite that form at pressures of tens of GPa."
    y_arr_bot = 3.4
    ax.add_patch(FancyArrowPatch(
        (sbox_centers[0] - 0.4, y_arr_bot), (sbox_centers[5] + 0.4, y_arr_bot),
        arrowstyle="-|>", mutation_scale=12, color="#4a6984", lw=1.6,
    ))
    ax.text(
        5.0, y_arr_bot + 0.55,
        "planar fractures, melt veins, high-pressure minerals\n(ringwoodite, majorite) at tens of GPa",
        ha="center", va="center", fontsize=10, color="#4a6984",
    )

    fig.tight_layout()
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
