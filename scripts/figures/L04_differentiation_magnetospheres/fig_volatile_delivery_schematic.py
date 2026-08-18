"""Generate Fig. (`fig:volatile-delivery`).

Two-panel schematic contrasting the classical and the revised picture
of volatile delivery to the terrestrial planets. Panel (a): a fixed
snow line separates a dry inner disk from an ice-rich outer disk, and
water arrives late from outside. Panel (b): the snow line sweeps
outward and then back inward, early inner-disk planetesimals carry
ice, and Jupiter's growth blocks the inward drift of icy pebbles,
splitting the disk into the NC and CC meteorite reservoirs.

Caption / figure id : `fig:volatile-delivery`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : Alexander2019a, Lichtenberg2021, Grewal2019, Grewal2024
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "volatile_delivery_schematic.avif")

DRY = "#e8b07a"
ICY = "#b8d4ea"
NC = "#dfa08f"
CC = "#8fb8dd"
SUN = "#f5c542"
ROCK = "#8a5a3c"
ICE_DOT = "#3f6fa8"
BLUE_TXT = "#2f5f8f"
RED_TXT = "#8f3f2f"


def band(ax, x0, x1, color):
    ax.add_patch(Rectangle((x0, 0), x1 - x0, 0.9, facecolor=color,
                           edgecolor="0.45", lw=0.8))


def sun(ax):
    ax.add_patch(Wedge((0.25, 0.45), 0.36, -90, 90,
                       facecolor=SUN, edgecolor="0.45", lw=0.8))


def panel_a(ax):
    ax.text(0.0, 2.0, "(a) classical view: dry inner solar system, water arrives late",
            fontsize=11, fontweight="bold", va="top")
    band(ax, 0.25, 4.0, DRY)
    band(ax, 4.0, 10.55, ICY)
    sun(ax)
    # Fixed snow line
    ax.plot([4.0, 4.0], [-0.12, 1.12], ls="--", lw=1.4, color="0.3")
    ax.text(4.12, 0.98, "snow line (fixed)", ha="left", va="bottom",
            fontsize=10, color="0.25")
    # Dry rocky planets inside, ice-rich bodies outside
    for x, r in [(1.2, 0.06), (1.9, 0.09), (2.6, 0.09), (3.4, 0.07)]:
        ax.add_patch(Circle((x, 0.45), r, facecolor=ROCK, edgecolor="none"))
    ax.text(2.3, -0.22, "dry rocky planets", ha="center", va="top",
            fontsize=10, color=RED_TXT)
    for x in (6.6, 7.4, 8.3, 9.2):
        ax.add_patch(Circle((x, 0.45), 0.06, facecolor=ICE_DOT,
                            edgecolor="none"))
    ax.text(7.9, -0.22, "ice-rich asteroids and comets", ha="center",
            va="top", fontsize=10, color=BLUE_TXT)
    # Late delivery arrow, arcing over the snow line
    ax.add_patch(FancyArrowPatch((7.4, 1.02), (2.3, 1.02),
                                 connectionstyle="arc3,rad=0.22",
                                 arrowstyle="-|>", mutation_scale=16,
                                 lw=1.6, color=BLUE_TXT))
    ax.text(4.85, 1.62, "water delivered late", ha="center", va="bottom",
            fontsize=10, color=BLUE_TXT)


def panel_b(ax):
    ax.text(0.0, 2.0, "(b) revised view: ice arrives early, Jupiter splits the disk",
            fontsize=11, fontweight="bold", va="top")
    band(ax, 0.25, 4.9, NC)
    band(ax, 5.55, 10.55, CC)
    sun(ax)
    # Jupiter in the gap between the two reservoirs
    ax.add_patch(Ellipse((5.22, 0.45), 0.66, 0.52, facecolor="#b5885a",
                         edgecolor="0.45", lw=0.8))
    ax.text(5.22, -0.22, "Jupiter", ha="center", va="top", fontsize=10,
            color="0.2")
    # Snow line sweeps outward early, then back inward as the disk cools
    ax.add_patch(FancyArrowPatch((1.3, 1.05), (4.2, 1.05),
                                 arrowstyle="<|-|>", mutation_scale=16,
                                 lw=1.4, ls="--", color="0.3"))
    ax.text(2.75, 1.20, "snow line sweeps outward, then back in",
            ha="center", va="bottom", fontsize=10, color="0.25")
    # Ice-bearing bodies inside the inner reservoir
    for x in (1.1, 1.9, 2.7, 3.5):
        ax.add_patch(Circle((x, 0.45), 0.06, facecolor=ICE_DOT,
                            edgecolor="none"))
    # Icy pebbles drift inward and pile up at Jupiter
    for x in (6.0, 6.3, 6.6):
        ax.add_patch(Circle((x, 0.45), 0.045, facecolor=ICE_DOT,
                            edgecolor="none"))
    ax.add_patch(FancyArrowPatch((8.4, 0.45), (6.85, 0.45),
                                 arrowstyle="-|>", mutation_scale=14,
                                 lw=1.4, color=BLUE_TXT))
    ax.text(8.05, 1.20, "icy pebbles drift inward,\nblocked by Jupiter",
            ha="center", va="bottom", fontsize=10, color=BLUE_TXT)
    # Reservoir labels
    ax.text(2.55, -0.22, "inner reservoir: forms early, with ice\n(NC meteorites)",
            ha="center", va="top", fontsize=10, color=RED_TXT)
    ax.text(8.05, -0.22, "outer reservoir: ice-rich\n(CC meteorites)",
            ha="center", va="top", fontsize=10, color=BLUE_TXT)
    ax.annotate(r"distance from the Sun $\rightarrow$", xy=(10.55, -0.82),
                ha="right", va="top", fontsize=10, color="0.35")


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(7.6, 5.6))
    for ax in (ax_a, ax_b):
        ax.set_xlim(0, 10.6)
        ax.set_ylim(-1.0, 2.1)
        ax.axis("off")
    panel_a(ax_a)
    panel_b(ax_b)
    fig.tight_layout(pad=0.3)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
