"""The three heat transport mechanisms in schematic form.

Conduction: heat passes through a solid down a temperature gradient
without bulk motion. Convection: hot fluid rises and cold fluid sinks.
Radiation: a hot surface emits photons. Schematic.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/heat_transport_modes.avif"

HOT = "#d7301f"
COLD = "#2b8cbe"


def make_plot() -> plt.Figure:
    """Build the three-panel icon figure, save it and return it."""
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.6))
    titles = ("(a) Conduction", "(b) Convection", "(c) Radiation")
    for ax, t in zip(axes, titles):
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 3.2)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(t, fontsize=11)
    ax = axes[0]
    grad = np.linspace(0, 1, 100).reshape(1, -1)
    ax.imshow(grad, extent=(0.5, 3.5, 0.9, 2.3), cmap="coolwarm_r", aspect="auto", zorder=1)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3.2)
    ax.add_patch(Rectangle((0.5, 0.9), 3.0, 1.4, facecolor="none", edgecolor="0.2", lw=1.2, zorder=2))
    ax.add_patch(FancyArrowPatch((1.0, 1.6), (3.0, 1.6), arrowstyle="-|>", mutation_scale=16, color="0.1", lw=2.0, zorder=3))
    ax.text(0.5, 2.5, "hot", ha="center", fontsize=10, color=HOT)
    ax.text(3.5, 2.5, "cold", ha="center", fontsize=10, color=COLD)
    ax.text(2.0, 0.4, r"$\vec{q} = -k\nabla T$: no bulk motion", ha="center", fontsize=10)
    ax = axes[1]
    ax.add_patch(Rectangle((0.5, 0.6), 3.0, 2.2, facecolor="#f4efe6", edgecolor="0.2", lw=1.2))
    ax.add_patch(Rectangle((0.5, 0.6), 3.0, 0.18, facecolor=HOT, edgecolor="none"))
    ax.add_patch(Rectangle((0.5, 2.62), 3.0, 0.18, facecolor=COLD, edgecolor="none"))
    ax.add_patch(FancyArrowPatch((2.0, 0.9), (2.0, 2.5), arrowstyle="-|>", mutation_scale=14, color=HOT, lw=2.0))
    ax.add_patch(FancyArrowPatch((1.0, 2.5), (1.0, 0.9), arrowstyle="-|>", mutation_scale=14, color=COLD, lw=2.0))
    ax.add_patch(FancyArrowPatch((3.0, 2.5), (3.0, 0.9), arrowstyle="-|>", mutation_scale=14, color=COLD, lw=2.0))
    ax.text(2.0, 0.25, "hot fluid rises, cold fluid sinks", ha="center", fontsize=10)
    ax = axes[2]
    ax.add_patch(Rectangle((0.5, 0.6), 3.0, 0.9, facecolor="#f0a070", edgecolor="0.2", lw=1.2))
    ax.text(2.0, 1.0, "hot surface at $T$", ha="center", va="center", fontsize=10)
    for x in (1.1, 2.0, 2.9):
        y = np.linspace(1.55, 2.75, 60)
        ax.plot(x + 0.08 * np.sin(12 * y), y, color="#e6550d", lw=1.6)
        ax.add_patch(FancyArrowPatch((x, 2.7), (x, 2.95), arrowstyle="-|>", mutation_scale=12, color="#e6550d", lw=1.6))
    ax.text(2.0, 0.25, r"$F = \epsilon \sigma T^4$: photons carry the energy", ha="center", fontsize=10)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.02, wspace=0.05)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
