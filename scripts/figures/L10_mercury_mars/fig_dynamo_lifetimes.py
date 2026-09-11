"""Dynamo lifetimes and longevity across the four rocky planets.

Earth and Mercury maintain active dynamos driven by core convection,
whereas Mars sustained a dynamo only for its first 500 to 800 Myr,
ceasing between 4.1 and 3.7 Ga, and Venus lacks a detectable field.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/10_mercury_mars/figures/dynamo_lifetimes.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.2, 4.8))

    ax.set_xlim(4.6, -0.1)
    ax.set_ylim(-0.28, 5.5)

    y_earth = 4.8
    y_merc = 3.6
    y_mars = 2.2
    y_venus = 1.1
    h = 0.40

    # Earth: active dynamo sustained by compositional buoyancy
    ax.add_patch(Rectangle((4.0, y_earth - h / 2), 0.5, h, facecolor="#e8f1fa", edgecolor="#1f6db8", hatch="//", lw=1.2))
    ax.add_patch(Rectangle((0.0, y_earth - h / 2), 4.0, h, facecolor="#1f6db8", edgecolor="#1f6db8", lw=1.2))
    ax.text(2.0, y_earth, "active dynamo, compositional buoyancy", color="white", ha="center", va="center", fontsize=10, weight="bold")

    # Mercury: weak dynamo in a thin liquid shell
    ax.add_patch(Rectangle((4.0, y_merc - h / 2), 0.5, h, facecolor="#e8f1fa", edgecolor="#4a6984", hatch="//", lw=1.2))
    ax.add_patch(Rectangle((0.0, y_merc - h / 2), 4.0, h, facecolor="#4a6984", edgecolor="#4a6984", lw=1.2))
    ax.text(2.0, y_merc, "weak dynamo, thin liquid shell", color="white", ha="center", va="center", fontsize=10, weight="bold")

    # Mars: dynamo for first 500 to 800 Myr, ceased between 4.1 and 3.7 Ga
    ax.add_patch(Rectangle((4.1, y_mars - h / 2), 0.4, h, facecolor="#c0392b", edgecolor="#c0392b", lw=1.2))
    ax.add_patch(Rectangle((3.7, y_mars - h / 2), 0.4, h, facecolor="#fdebd0", edgecolor="#c0392b", lw=1.2))

    ax.add_patch(FancyArrowPatch((4.25, 2.72), (4.25, 2.45), arrowstyle="-|>", mutation_scale=10, color="#c0392b", lw=1.2))
    ax.text(4.35, 2.80, "dynamo (first 500 to 800 Myr)", ha="left", va="bottom", fontsize=10, color="#c0392b")

    ax.add_patch(FancyArrowPatch((3.40, y_mars), (3.68, y_mars), arrowstyle="-|>", mutation_scale=10, color="#c0392b", lw=1.2))
    ax.text(3.30, y_mars, "longer-lived or episodic (MAVEN crustal fields to 3.7 Ga)", ha="left", va="center", fontsize=10, color="#c0392b")

    # Venus: lacks detectable intrinsic field, history unknown
    ax.add_patch(Rectangle((0.0, y_venus - h / 2), 4.5, h, facecolor="#f8f9fa", edgecolor="0.5", linestyle=":", lw=1.2))
    ax.text(4.25, y_venus, "?", color="0.3", ha="center", va="center", fontsize=12, weight="bold")
    ax.text(2.0, y_venus, "no detectable field, history unknown", color="0.3", ha="center", va="center", fontsize=10)

    # Habitability summary: ion escape suppression and atmosphere loss timescale
    ax.text(
        2.25, 0.32,
        "a magnetic shield suppresses ion escape by up to an order of magnitude over Gyr;\n"
        "an unmagnetised Mars-sized planet still loses its atmosphere on 1e9-year timescales",
        ha="center", va="center", fontsize=10, color="0.2", linespacing=1.2,
    )

    # Y-axis configuration
    ax.set_yticks([y_venus, y_mars, y_merc, y_earth])
    ax.set_yticklabels(["Venus", "Mars", "Mercury", "Earth"], fontsize=10, fontweight="bold")
    ax.tick_params(left=False)

    # X-axis configuration
    ax.set_xticks([4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0])
    ax.set_xticklabels(["4.5", "4.0", "3.5", "3.0", "2.5", "2.0", "1.5", "1.0", "0.5", "0 (today)"])
    ax.set_xlabel("Time before present (Ga)")
    ax.set_title("Dynamo lifetimes of the rocky planets", fontsize=11)

    ax.grid(axis="x", alpha=0.3)
    ax.grid(axis="y", visible=False)

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
