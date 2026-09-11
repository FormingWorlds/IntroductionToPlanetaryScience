"""Gravitational differentiation as a before-and-after cross-section.

Left: a homogeneous mixture of rock and metal. Right: the differentiated
body with a metal core and a silicate mantle. The sinking of the dense
metal lowers the gravitational potential energy and releases about
2e31 J for Earth, the value the notes give. Schematic, not to scale.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/differentiation_energy.avif"

ROCK = "#c9b69a"
METAL = "#6d6a68"


def make_plot() -> plt.Figure:
    """Build the schematic, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 4.0))
    for ax, title in ((ax1, "(a) Homogeneous body after accretion"), (ax2, "(b) After core formation")):
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.45, 1.45)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=11)
    ax1.add_patch(Circle((0, 0), 1.0, facecolor=ROCK, edgecolor="0.2", lw=1.2))
    rng = np.random.default_rng(3)
    for _ in range(140):
        rr, th = np.sqrt(rng.random()) * 0.95, rng.random() * 2 * np.pi
        ax1.add_patch(Circle((rr * np.cos(th), rr * np.sin(th)), 0.045, facecolor=METAL, edgecolor="none"))
    ax1.text(0, -1.25, "metal droplets dispersed in silicate rock", ha="center", fontsize=10)
    ax2.add_patch(Circle((0, 0), 1.0, facecolor=ROCK, edgecolor="0.2", lw=1.2))
    ax2.add_patch(Circle((0, 0), 0.55, facecolor=METAL, edgecolor="0.2", lw=1.0))
    ax2.text(0, 0, "metal\ncore", ha="center", va="center", fontsize=10, color="white")
    ax2.text(0, 0.78, "silicate mantle", ha="center", va="center", fontsize=10)
    for ang in (35, 145, 215, 325):
        a = np.radians(ang)
        ax2.add_patch(FancyArrowPatch((0.92 * np.cos(a), 0.92 * np.sin(a)), (0.62 * np.cos(a), 0.62 * np.sin(a)),
                                      arrowstyle="-|>", mutation_scale=12, color="#c0392b", lw=1.6))
    ax2.text(0, -1.25, r"dense metal sinks: $E_{\mathrm{diff}} \approx 2 \times 10^{31}$ J for Earth", ha="center", fontsize=10)
    fig.text(0.5, 0.93, "Gravitational differentiation (schematic)", ha="center", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.85, bottom=0.02, wspace=0.05)
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
