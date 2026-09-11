"""Five open questions of the course and what will decide each of them.

Each row pairs one open question with the test or facility that the
synthesis chapter names for it.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/14_synthesis/figures/five_questions.avif"

ROWS = [
    ("Is the origin of life a rare accident\nor a generic chemical inevitability?",
     "The largest uncertainty in quantitative\nhabitability estimates"),
    ("What carves the radius valley between\nsuper-Earths and sub-Neptunes?",
     "Photoevaporation, core-powered mass loss,\nor distinct formation channels"),
    ("When did Jupiter form?",
     "Architect of the inner solar system:\nthe NC-CC dichotomy and Earth-like system rarity"),
    ("Was Mars ever inhabited?",
     "Mars Sample Return, the most direct test;\nit recalibrates the prior on $f_l$"),
    ("Is the solar system rare or typical?",
     "PLATO, Gaia DR4/DR5 and long-baseline RV\ngive a probabilistic answer"),
]
Q_FC, Q_EC = "#eef4f8", "#4a6984"
A_FC, A_EC = "#fef3e2", "#c46b1a"


def make_plot() -> plt.Figure:
    """Build the five-row question figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(0.0, 6.0)
    ax.axis("off")
    ax.text(2.55, 5.72, "Open question", ha="center", va="center", fontsize=11, weight="bold", color=Q_EC)
    ax.text(7.35, 5.72, "What is at stake, and what will decide it", ha="center", va="center", fontsize=11, weight="bold", color=A_EC)
    for i, (question, answer) in enumerate(ROWS):
        yc = 4.95 - 1.08 * i
        ax.add_patch(Circle((0.45, yc), 0.28, facecolor=Q_EC, edgecolor="none", zorder=3))
        ax.text(0.45, yc, str(i + 1), ha="center", va="center", fontsize=11, weight="bold", color="white", zorder=4)
        ax.add_patch(FancyBboxPatch((0.95, yc - 0.42), 3.9, 0.84, boxstyle="round,pad=0.02,rounding_size=0.12",
                                    facecolor=Q_FC, edgecolor=Q_EC, lw=1.0, zorder=2))
        ax.text(2.9, yc, question, ha="center", va="center", fontsize=10, zorder=4)
        ax.add_patch(FancyBboxPatch((5.05, yc - 0.42), 4.85, 0.84, boxstyle="round,pad=0.02,rounding_size=0.12",
                                    facecolor=A_FC, edgecolor=A_EC, lw=1.0, zorder=2))
        ax.text(7.475, yc, answer, ha="center", va="center", fontsize=10, zorder=4)
        ax.annotate("", xy=(5.03, yc), xytext=(4.87, yc), arrowprops=dict(arrowstyle="-|>", color="0.4", lw=1.2))
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
