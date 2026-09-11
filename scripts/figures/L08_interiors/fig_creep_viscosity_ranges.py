"""Mantle viscosity ranges by solid-state creep mechanism.

Silicate rock flows by solid-state creep when temperature exceeds about
0.5 T_melt via dislocation creep in the upper mantle and diffusion creep
in the lower mantle.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/creep_viscosity_ranges.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.8, 4.4))

    # Note text above the two rows
    ax.text(
        10**21.5,
        3.45,
        "solid rock flows by solid-state creep when T exceeds about 0.5 T_melt",
        ha="center",
        va="center",
        fontsize=10,
        fontstyle="italic",
        color="0.25",
    )

    # Upper mantle: dislocation creep (defect glide) from 1e20 to 1e21 Pa s
    y_up = 2.05
    h = 0.28
    r_up = Rectangle(
        (1e20, y_up - h / 2),
        1e21 - 1e20,
        h,
        facecolor="#e8f1fa",
        edgecolor="#1f6db8",
        lw=1.5,
        zorder=2,
    )
    ax.add_patch(r_up)
    ax.text(
        10**20.5,
        y_up + h / 2 + 0.35,
        "dislocation creep, upper mantle: 1e20 to 1e21 Pa s\n(defect glide)",
        ha="center",
        va="bottom",
        fontsize=10,
        color="#1f6db8",
        linespacing=1.3,
    )

    # Lower mantle: diffusion creep (vacancy migration) from 1e22 to 1e23 Pa s
    y_lo = 0.65
    r_lo = Rectangle(
        (1e22, y_lo - h / 2),
        1e23 - 1e22,
        h,
        facecolor="#fdebd0",
        edgecolor="#c46b1a",
        lw=1.5,
        zorder=2,
    )
    ax.add_patch(r_lo)
    ax.text(
        10**22.5,
        y_lo + h / 2 + 0.35,
        "diffusion creep, lower mantle: 1e22 to 1e23 Pa s\n(vacancy migration)",
        ha="center",
        va="bottom",
        fontsize=10,
        color="#c46b1a",
        linespacing=1.3,
    )

    # Viscosity log axis from 1e19 to 1e24 Pa s
    ax.set_xscale("log")
    ax.set_xlim(1e19, 1e24)
    ax.set_xticks([1e19, 1e20, 1e21, 1e22, 1e23, 1e24])
    ax.set_xlabel(r"Dynamic viscosity $\eta$ (Pa s)", fontsize=10)

    # Vertical limits and aesthetics
    ax.set_ylim(0.0, 3.8)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", alpha=0.3, linestyle=":")

    # Title
    ax.set_title("Mantle viscosity by creep mechanism", fontsize=11)

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
