"""Mantle reservoirs left by magma ocean crystallisation.

A box diagram of the depleted MORB mantle, the enriched reservoirs
sampled by plumes, and the crust that extracted the incompatible
elements. Schematic.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/mantle_reservoirs.avif"


def box(ax, x, y, w, h, fc, ec, title, body):
    """Draw one labelled reservoir box."""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.2", facecolor=fc, edgecolor=ec, lw=1.3))
    ax.text(x + w / 2, y + h - 0.45, title, ha="center", va="center", fontsize=11, weight="bold", color=ec)
    ax.text(x + w / 2, y + h / 2 - 0.3, body, ha="center", va="center", fontsize=10)


def make_plot() -> plt.Figure:
    """Build the box diagram, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(7.65, 3.74))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    box(ax, 0.4, 4.3, 11.2, 1.7, "#e8e2d4", "#6b5e4a", "Crust",
        "continental crust: enriched in incompatible elements (U, Th, K)\nby partial melting and crustal extraction;\noceanic crust: basalt returned to the mantle by subduction")
    box(ax, 0.4, 0.4, 5.4, 3.2, "#e8f1fa", "#1f6db8", "Depleted MORB mantle (DMM)",
        "source of mid-ocean ridge basalts;\ndepleted in incompatible\nelements over Gyr")
    box(ax, 6.2, 0.4, 5.4, 3.2, "#fdebd0", "#c46b1a", "Enriched mantle",
        "deep reservoirs sampled by plumes\n(ocean island basalts: Hawaii, Iceland);\nless-processed primordial material\nor recycled oceanic crust")
    ax.add_patch(FancyArrowPatch((3.1, 3.65), (3.1, 4.25), arrowstyle="-|>", mutation_scale=14, color="#1f6db8", lw=2.0))
    ax.text(3.35, 3.95, "melt extraction", ha="left", va="center", fontsize=10, color="#1f6db8")
    ax.add_patch(FancyArrowPatch((8.9, 4.25), (8.9, 3.65), arrowstyle="-|>", mutation_scale=14, color="#c46b1a", lw=2.0))
    ax.text(9.15, 3.95, "recycled oceanic crust", ha="left", va="center", fontsize=10, color="#c46b1a")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    save_figure(fig, OUT_AVIF, dpi=280)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
