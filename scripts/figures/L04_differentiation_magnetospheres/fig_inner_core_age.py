"""The inner-core age debate on one timeline.

A geodynamo is recorded from at least 3.45 Ga (Tarduno 2010), and its
power source before the inner core existed is the new core paradox
(Olson 2013). Nucleation estimates run from 0.55 to 2 Ga: a high iron
conductivity gives an inner core younger than about 1 Gyr (Labrosse
2015, Ohta 2016), a low measured conductivity allows 2 Gyr or older
(Konopkova 2016), a paleointensity rise at 1.0 to 1.5 Ga (Biggin 2015)
and an ultralow field at 565 Ma followed by renewal (Bono 2019, Zhou
2022) are read as nucleation.
"""

from __future__ import annotations

from pathlib import Path

import textwrap

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/inner_core_age.avif"


def make_plot() -> plt.Figure:
    """Build the timeline, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(9.0, 4.6))
    red, blue, orange, grey = "#c0392b", "#1f6db8", "#a05a00", "0.35"
    # Geodynamo record and the paradox of its early power source.
    ax.add_patch(Rectangle((0.0, 3.6), 3.45, 0.45, facecolor="#7fb3d5", alpha=0.55, edgecolor="none"))
    ax.text(1.725, 3.82, "geodynamo recorded since at least 3.45 Ga,\n50 to 70% of today's strength (Tarduno 2010)", ha="center", va="center", fontsize=9.5)
    ax.text(3.45, 3.42, "power source before nucleation unclear:\nthe new core paradox (Olson 2013)", ha="left", va="top", fontsize=9.5, color=grey)
    # Nucleation estimates, oldest at the top.
    rows = [
        (2.55, 0.0, 2.0, grey, "low measured conductivity of 18 to 44 W m$^{-1}$ K$^{-1}$: inner core 2 Gyr old or older (Kon\u00f4pkov\u00e1 2016)"),
        (1.85, 1.0, 1.5, blue, "paleointensity rise at 1.0 to 1.5 Ga read as nucleation (Biggin 2015)"),
        (1.15, 0.0, 1.0, red, "high iron conductivity: inner core younger than about 1 Gyr (Labrosse 2015, Ohta 2016)"),
        (0.45, 0.53, 0.57, orange, "ultralow field at 565 Ma, five-fold renewal by 532 Ma: nucleation near 0.55 Ga (Bono 2019, Zhou 2022)"),
    ]
    for y, x0, x1, color, label in rows:
        ax.plot([x1, x0], [y, y], color=color, lw=6.0, solid_capstyle="butt")
        ax.text(x1 + 0.08, y, textwrap.fill(label, 58), ha="right", va="center", fontsize=9.5, color=color)
    ax.plot([4.54, 4.54], [3.3, 4.05], color="0.2", lw=1.0, ls="--")
    ax.text(4.52, 4.12, "Earth forms", ha="left", va="bottom", fontsize=9.5)
    ax.text(-0.02, 4.12, "today", ha="right", va="bottom", fontsize=9.5)
    ax.set_xlim(4.7, -0.05)
    ax.set_ylim(0.1, 4.5)
    ax.set_yticks([])
    ax.set_xlabel("Time before present (Ga)")
    ax.set_title("When did Earth's inner core nucleate? Estimates range from 0.55 to 2 Ga", fontsize=11)
    ax.grid(False)
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
