"""The moment of inertia factor measures central mass concentration.

A uniform sphere has C/MR^2 = 0.400, while differentiated bodies have lower
values down to 0.331 for Earth (de Pater and Lissauer 2010).
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure, text_color_on

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/moment_of_inertia_factors.avif"

# Data
# "Uniform sphere 0.400 homogeneous; Moon 0.393 small core; Mars 0.364 moderate core;
#  Mercury 0.346 large core; Earth 0.331 iron core (de Pater and Lissauer 2010)."
BODIES = ["Uniform sphere", "Moon", "Mars", "Mercury", "Earth"]
FACTORS = [0.400, 0.393, 0.364, 0.346, 0.331]
STATES = ["homogeneous", "small core", "moderate core", "large core", "iron core"]

# Colours from approved palette (Rule 4): grey-blue, blue, orange, green, red
COLORS = ["#4a6984", "#1f6db8", "#c46b1a", "#2ca25f", "#c0392b"]


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 4.2))

    # Bars sorted from 0.400 down: Uniform sphere at top, Earth at bottom
    y_pos = np.arange(len(BODIES))[::-1]
    ax.barh(y_pos, FACTORS, height=0.50, color=COLORS, edgecolor="none")

    # Inscribed numerical values inside bars with contrast-checked text color
    for yi, val, c in zip(y_pos, FACTORS, COLORS):
        ax.text(val - 0.015, yi, f"{val:.3f}", ha="right", va="center",
                color=text_color_on(c), fontsize=10, weight="bold")

    # Dashed vertical line at 0.400 labelled 'uniform sphere'
    ax.axvline(0.400, color="0.4", linestyle="--", lw=1.2)
    ax.text(0.400, 4.6, "uniform sphere", ha="center", va="center",
            fontsize=10, color="0.3", bbox=dict(facecolor="white", edgecolor="none", pad=1.5))

    # Right-hand annotation column for physical state
    for yi, st in zip(y_pos, STATES):
        ax.text(0.415, yi, st, ha="left", va="center", fontsize=10, color="0.2")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(BODIES, fontsize=10)
    ax.set_xticks([0.0, 0.1, 0.2, 0.3, 0.4])
    ax.set_xlabel(r"Moment of inertia factor $C/MR^2$", fontsize=10)
    ax.set_xlim(0.0, 0.52)
    ax.set_ylim(-0.6, 5.0)

    # Title
    ax.set_title("The moment of inertia factor sorts bodies by central concentration", fontsize=11)
    ax.grid(axis="x", linestyle=":", alpha=0.3)
    ax.grid(axis="y", visible=False)

    # Note below the axis
    fig.text(0.5, 0.02, r"lower $C/MR^2$ means more mass concentrated toward the centre",
             ha="center", va="bottom", fontsize=10, color="0.3")

    fig.tight_layout(rect=[0, 0.06, 1, 1])
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
