"""Generate Fig. (`fig:hf-w-chronometry`).

Two-panel chronology of accretion and core formation focused on
planetary cores and the ages of bodies, in particular the Earth.

(a) The first 5 Myr after CAI condensation, linear axis: CAI
    formation, chondrule formation, NC and CC planetesimal accretion,
    half of Mars's mass, and gas-disk dissipation. Bar spans are
    schematic, redrawn after Fig. 4 of Lichtenberg et al. (2023,
    Protostars and Planets VII) and the references therein.
(b) Core formation on a logarithmic axis to 300 Myr: planetesimal
    cores at ~1-3 Myr (Kleine & Walker 2017), Mars complete within
    ~10 Myr (Kleine & Walker 2017; Kruijer et al. 2017), Earth with
    the two-stage age of ~30 Myr as a lower limit and completion
    probably within ~100 Myr (Nimmo & Kleine 2015; Kleine & Walker
    2017), and the Moon-forming impact later than ~50 Myr (Nimmo &
    Kleine 2015).

Caption / figure id : `fig:hf-w-chronometry`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : Lichtenberg2023, KleineWalker2017, NimmoKleine2015, Kruijer2017Mars
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "accretion_core_formation_timeline.avif")

C_CAI = "#17becf"
C_CHON = "#7f7f7f"
C_NC = "#d62728"
C_CC = "#1f77b4"
C_MARS = "#e07b39"
C_DISK = "#9467bd"
C_EARTH = "#1f77b4"
C_MOON = "#555555"


def grad_bar(ax, x0, x1, y, color, h=0.52, fade_left=None, fade_right=None,
             alpha=0.85, n=60):
    """Horizontal bar from x0 to x1 with optional linear alpha fade-out
    before x0+fade_left and after x1-fade_right (data units)."""
    xs = np.linspace(x0, x1, n + 1)
    for xa, xb in zip(xs[:-1], xs[1:]):
        xm = 0.5 * (xa + xb)
        a = alpha
        if fade_left is not None and xm < x0 + fade_left:
            a = alpha * (xm - x0) / fade_left
        if fade_right is not None and xm > x1 - fade_right:
            a = alpha * (x1 - xm) / fade_right
        ax.add_patch(Rectangle((xa, y - h / 2), xb - xa, h,
                               facecolor=color, edgecolor="none",
                               alpha=max(a, 0.0)))


def panel_a(ax):
    rows = [
        ("CAI formation", 0.0, 0.2, C_CAI, None, None),
        ("chondrule formation", 0.0, 3.6, C_CHON, None, 1.2),
        ("NC planetesimals accrete", 0.1, 1.9, C_NC, None, 0.7),
        ("CC planetesimals accrete", 0.75, 3.6, C_CC, None, 1.0),
        ("half of Mars's mass", 0.8, 2.7, C_MARS, None, None),
        ("gas disk dissipates", 1.2, 4.7, C_DISK, 0.8, 1.0),
    ]
    for i, (label, x0, x1, color, fl, fr) in enumerate(rows):
        y = len(rows) - i
        grad_bar(ax, x0, x1, y, color, fade_left=fl, fade_right=fr)
        ax.annotate(label, xy=(x1 + 0.07 if x1 < 3.4 else x0 - 0.07, y),
                    ha="left" if x1 < 3.4 else "right", va="center",
                    fontsize=9.5, color=color)
    # Mars half-mass best estimate
    ax.plot(1.8, 2, marker="v", color=C_MARS, ms=7, zorder=5)
    ax.annotate("~1.8 Myr", xy=(1.8, 2.42), ha="center", fontsize=8,
                color=C_MARS)

    ax.set_xlim(-0.1, 5.0)
    ax.set_ylim(0.35, 6.85)
    ax.set_yticks([])
    ax.set_xlabel("Time after CAI condensation (Myr)")
    ax.set_title("(a) the planetesimal era: the first 5 Myr", fontsize=11,
                 loc="left")
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)


def panel_b(ax):
    ax.set_xscale("log")

    # zoom marker for panel (a)
    ax.axvspan(0.6, 5.0, color="0.55", alpha=0.10, zorder=0)
    ax.annotate("panel (a)", xy=(1.7, 4.62), ha="center", fontsize=8,
                color="0.35")

    # planetesimal cores
    y = 4
    grad_bar(ax, 1.0, 3.0, y, C_NC)
    ax.plot(3.0, y, marker="s", color=C_NC, ms=7, zorder=5)
    ax.annotate("planetesimal cores complete by ~1-3 Myr\n"
                "(iron-meteorite parent bodies)", xy=(3.6, y), va="center",
                fontsize=9.5, color=C_NC)

    # Mars
    y = 3
    grad_bar(ax, 0.8, 10.0, y, C_MARS, fade_left=1.0)
    ax.plot(10.0, y, marker="s", color=C_MARS, ms=7, zorder=5)
    ax.annotate("Mars: accretion and core complete within ~10 Myr",
                xy=(12, y), va="center", fontsize=9.5, color=C_MARS)

    # Earth
    y = 2
    grad_bar(ax, 1.0, 100.0, y, C_EARTH, fade_left=2.0, fade_right=55.0)
    ax.plot(30.0, y, marker="D", color=C_EARTH, ms=8, zorder=5)
    ax.annotate("Earth: two-stage age ~30 Myr = lower limit;\n"
                "core formation ends within ~100 Myr", xy=(1.05, 1.35),
                va="center", fontsize=9.5, color=C_EARTH)

    # Moon-forming impact
    y = 0.72
    grad_bar(ax, 50.0, 150.0, y, C_MOON, fade_right=60.0)
    ax.annotate("Moon-forming giant impact: later than ~50 Myr",
                xy=(45, y), ha="right", va="center", fontsize=9.5,
                color=C_MOON)

    ax.set_xlim(0.6, 300)
    ax.set_ylim(0.15, 4.85)
    ax.set_yticks([])
    ax.set_xlabel("Time after CAI condensation (Myr, log scale)")
    ax.set_title("(b) core formation: small bodies finish early, Earth finishes late",
                 fontsize=11, loc="left")
    for s in ("left", "right", "top"):
        ax.spines[s].set_visible(False)


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(9.6, 7.0),
                                     gridspec_kw={"height_ratios": [1.15, 1]})
    panel_a(ax_a)
    panel_b(ax_b)
    fig.tight_layout(h_pad=2.2)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
