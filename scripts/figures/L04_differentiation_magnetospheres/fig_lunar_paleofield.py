"""The lunar dynamo paradox: paleofield strength against age.

The Apollo samples record a high-field epoch with a mean of about 77
microtesla between 3.85 and 3.56 Ga and fields below 7 microtesla by
3.3 Ga (Weiss 2014), from a body with a liquid core of only about
400 km radius.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/lunar_paleofield.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    box_color, mean_color, limit_color = "#f4a261", "#c0392b", "#1f6db8"
    # High-field epoch: tens of microtesla between 3.85 and 3.56 Ga.
    ax.add_patch(Rectangle((3.56, 40), 0.29, 70, facecolor=box_color, alpha=0.45, edgecolor="none"))
    ax.text(3.705, 113, "high-field epoch, 3.85 to 3.56 Ga", ha="center", va="bottom", fontsize=10, color="#a05a00")
    ax.text(3.705, 50, "tens of $\\mu$T", ha="center", va="center", fontsize=10, color="#a05a00")
    ax.plot([3.85, 3.56], [77, 77], color=mean_color, lw=3.0)
    ax.text(3.54, 77, "mean about 77 $\\mu$T", ha="left", va="center", fontsize=10, color=mean_color)
    # Decline between the two constraints, with a timing that the samples do not resolve.
    ax.plot([3.56, 3.36], [77, 9], color="0.5", lw=1.5, ls="--")
    ax.text(3.40, 44, "decline, timing\nnot resolved", ha="left", va="center", fontsize=9, color="0.4")
    # Upper limit at 3.3 Ga, drawn as a capped downward arrow.
    ax.plot([3.34, 3.26], [7, 7], color=limit_color, lw=2.5)
    ax.add_patch(FancyArrowPatch((3.3, 7), (3.3, 0.5), arrowstyle="-|>", mutation_scale=14, color=limit_color, lw=2.0))
    ax.text(3.25, 10, "below 7 $\\mu$T by 3.3 Ga", ha="left", va="bottom", fontsize=10, color=limit_color)
    ax.text(3.54, 100, "Liquid core radius only about 400 km:\nthermal convection alone cannot\nsustain a field of tens of $\\mu$T.", ha="left", va="top", fontsize=9.5, color="0.3")
    ax.set_xlim(4.0, 3.0)
    ax.set_ylim(0, 125)
    ax.set_xlabel("Age (Ga)")
    ax.set_ylabel("Surface paleofield strength ($\\mu$T)")
    ax.set_title("The lunar dynamo paradox: Apollo 15, 16 and 17 paleointensities", fontsize=11)
    ax.grid(alpha=0.3)
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
