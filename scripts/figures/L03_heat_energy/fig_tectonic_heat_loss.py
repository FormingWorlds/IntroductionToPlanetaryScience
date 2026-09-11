"""Heat loss under three tectonic regimes as cross-section icons.

Mobile lid: subduction and seafloor spreading carry heat out; stagnant
lid: conduction through a thick lid plus episodic volcanism; heat pipe:
erupted magma cools at the surface and is buried by later flows.
Schematic, not to scale.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/tectonic_heat_loss.avif"

MANTLE = "#e8a87c"
LID = "#9c8b7a"
MAGMA = "#d7301f"


def _base(ax: plt.Axes, title: str, lid: float) -> None:
    """Draw the mantle box and a lid of the given thickness."""
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=11)
    ax.add_patch(Rectangle((0.3, 0.3), 5.4, 3.0, facecolor=MANTLE, edgecolor="0.2", lw=1.2))
    ax.add_patch(Rectangle((0.3, 3.3 - lid), 5.4, lid, facecolor=LID, edgecolor="0.2", lw=1.2))


def make_plot() -> plt.Figure:
    """Build the three-panel figure, save it and return it."""
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.8))
    ax = axes[0]
    _base(ax, "(a) Mobile lid (plate tectonics)", 0.35)
    ax.add_patch(Polygon([[4.2, 3.3], [4.65, 3.3], [5.55, 0.3], [5.1, 0.3]], facecolor=LID, edgecolor="0.2", lw=1.0))
    ax.add_patch(FancyArrowPatch((1.6, 0.6), (1.6, 2.7), arrowstyle="-|>", mutation_scale=12, color=MAGMA, lw=2.0))
    ax.add_patch(FancyArrowPatch((1.9, 3.15), (3.9, 3.15), arrowstyle="-|>", mutation_scale=10, color="0.1", lw=1.4))
    ax.add_patch(FancyArrowPatch((4.6, 2.9), (5.3, 0.7), arrowstyle="-|>", mutation_scale=12, color="#2b8cbe", lw=2.0))
    ax.text(1.6, 3.55, "ridge", ha="center", fontsize=10)
    ax.text(5.0, 3.55, "subduction", ha="center", fontsize=10)
    ax.text(3.0, 4.05, "high heat flux", ha="center", fontsize=10, weight="bold")
    ax = axes[1]
    _base(ax, "(b) Stagnant lid", 1.1)
    for x in (1.5, 3.0, 4.5):
        ax.add_patch(FancyArrowPatch((x, 2.3), (x, 2.58), arrowstyle="-|>", mutation_scale=9, color="0.1", lw=1.0, ls="--"))
    ax.add_patch(FancyArrowPatch((5.0, 0.8), (5.0, 3.25), arrowstyle="-|>", mutation_scale=12, color=MAGMA, lw=2.0))
    ax.text(3.0, 1.2, "convecting interior", ha="center", fontsize=10)
    ax.text(2.6, 2.95, "conduction through\na thick lid", ha="center", va="center", fontsize=10, color="white")
    ax.text(5.0, 3.55, "episodic\nvolcanism", ha="center", fontsize=10)
    ax.text(3.0, 4.05, "lower heat flux", ha="center", fontsize=10, weight="bold")
    ax = axes[2]
    _base(ax, "(c) Heat pipe (Io, early Earth)", 0.9)
    for x in (1.5, 3.0, 4.5):
        ax.add_patch(FancyArrowPatch((x, 0.6), (x, 3.5), arrowstyle="-|>", mutation_scale=12, color=MAGMA, lw=2.0))
    for yy in np.linspace(2.45, 3.25, 5):
        ax.plot([0.35, 5.65], [yy, yy], color="0.3", lw=0.6)
    ax.add_patch(FancyArrowPatch((5.4, 3.35), (5.4, 2.55), arrowstyle="-|>", mutation_scale=10, color="0.1", lw=1.2))
    ax.text(3.0, 3.55, "magma erupts, cools, is buried by later flows", ha="center", fontsize=10)
    ax.text(3.0, 4.05, "high heat flux without plates", ha="center", fontsize=10, weight="bold")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02, wspace=0.05)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
