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
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.add_patch(Rectangle((3.56, 40), 0.29, 70, facecolor="#f4a261", alpha=0.5, edgecolor="none"))
    ax.plot([3.85, 3.56], [77, 77], color="#c0392b", lw=3.0)
    ax.text(3.705, 82, "high-field epoch: mean about 77 $\\mu$T", ha="center", va="bottom", fontsize=10, color="#c0392b")
    ax.text(3.705, 45, "tens of $\\mu$T", ha="center", va="bottom", fontsize=10, color="#a05a00")
    ax.add_patch(FancyArrowPatch((3.3, 7), (3.3, 1.5), arrowstyle="-|>", mutation_scale=12, color="#1f6db8", lw=2.0))
    ax.plot([3.34, 3.26], [7, 7], color="#1f6db8", lw=2.5)
    ax.text(3.27, 9, "below 7 $\\mu$T by 3.3 Ga", ha="left", va="bottom", fontsize=10, color="#1f6db8")
    ax.text(3.98, 110, "Apollo 15, 16 and 17 samples; liquid core radius only about 400 km", fontsize=10, color="0.3")
    ax.set_xlim(4.0, 3.1)
    ax.set_ylim(0, 120)
    ax.set_xlabel("Age (Ga)")
    ax.set_ylabel("Surface paleofield strength ($\\mu$T)")
    ax.set_title("The lunar dynamo paradox", fontsize=11)
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
