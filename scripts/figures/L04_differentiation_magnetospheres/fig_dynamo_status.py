"""Dynamo status of the terrestrial bodies and Ganymede.

One row per body with the state of its dynamo and the surface field,
as the lecture notes describe them. Schematic table figure.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/dynamo_status.avif"

ROWS = [
    ("Mercury", "active", "weak, about 1% of Earth's; dipole offset northward; thin liquid shell", "#2ca25f"),
    ("Venus", "none detected", "no inner core to drive compositional convection; stagnant lid slows core cooling", "#c0392b"),
    ("Earth", "active", "reference case; inner-core nucleation within the past 1 Gyr", "#2ca25f"),
    ("Moon", "extinct", "paleofields of tens of microtesla from 3.85 to 3.56 Ga, below 7 microtesla by 3.3 Ga", "#e6a817"),
    ("Mars", "extinct", "remnant crustal magnetism in the southern highlands; global field lost about 4 Gyr ago", "#e6a817"),
    ("Ganymede", "active", "the only moon with an active dynamo; surface field about 0.7 microtesla, above Mercury's 0.3 microtesla", "#2ca25f"),
]


def make_plot() -> plt.Figure:
    """Build the table figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.2)
    ax.axis("off")
    ax.text(0.9, 6.75, "Body", fontsize=11, weight="bold")
    ax.text(2.9, 6.75, "Dynamo today", fontsize=11, weight="bold")
    ax.text(4.5, 6.75, "What the field tells us", fontsize=11, weight="bold")
    for i, (body, status, note, col) in enumerate(ROWS):
        y = 6.0 - i * 1.05
        ax.add_patch(FancyBboxPatch((0.3, y - 0.42), 9.5, 0.86, boxstyle="round,pad=0.02,rounding_size=0.1", facecolor="#f7f7f7" if i % 2 else "white", edgecolor="0.8", lw=0.8))
        ax.text(0.9, y, body, fontsize=11, weight="bold", va="center")
        ax.add_patch(Circle((2.7, y), 0.16, facecolor=col, edgecolor="none"))
        ax.text(2.95, y, status, fontsize=10, va="center", color=col)
        ax.text(4.5, y, note, fontsize=10, va="center")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
