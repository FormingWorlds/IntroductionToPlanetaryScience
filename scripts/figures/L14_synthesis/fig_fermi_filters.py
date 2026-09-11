"""Generate Fig. (`fig:fermi-filters`).

Two-panel schematic illustrating the Fermi paradox:
(a) Horizontal sequence diagram of the Drake-equation factors as a chain
of filters: stars (R_*), planets (f_p), habitable planets (n_e), life (f_l),
intelligence (f_i), technology (f_c), and civilisation lifetime (L),
with annotations placing three proposed resolutions on the chain: rare life
at f_l, rare intelligence at f_i, and the Great Filter at L.
(b) Timescale comparison showing the sub-relativistic galactic crossing time
(order 10^6 to 10^7 years) versus the age of the Milky Way galaxy (10^10 years)
as horizontal bars, stating the paradox that crossing time is far shorter than
galaxy age.

Citations and provenance:
- Markdown source: book/14_synthesis/synthesis.md:361-377
  Heading: 'The Fermi paradox'
- Fermi paradox statement: book/14_synthesis/synthesis.md:363-365
  'The Fermi paradox is the question of why we observe no evidence of
  spacefaring civilisations, summarised as "where is everybody?".
  Because the Milky Way is about 10^{10} years old, an early spacefaring
  civilisation could have crossed the galaxy at sub-relativistic speeds.
  Yet, we observe no evidence of any such civilisation.'
- Proposed resolutions: book/14_synthesis/synthesis.md:367-372
  'Rare-life hypothesis: f_l is very small because life is hard to start.'
  'Rare-intelligence hypothesis: f_i is the bottleneck because
  technological intelligence rarely follows from biology.'
  'Great filter: L is short because civilisations self-terminate
  before covering the galaxy.'
- Drake equation factors: book/14_synthesis/synthesis.md:348
  Factors R_*, f_p, n_e, f_l, f_i, f_c, L.
- Sketch specification: material_11.txt:21
  'A horizontal sequence diagram of the Drake-equation factors as a chain
  of filters: stars -> planets -> habitable planets -> life (f_l) ->
  intelligence (f_i) -> technology (f_c) -> lifetime (L), drawn as boxes
  with arrows, and three annotations placing the proposed resolutions
  on the chain: rare life at f_l, rare intelligence at f_i, Great Filter
  at L; a second row shows the galactic crossing time versus galaxy age
  as two bars (crossing time of order 1e6 to 1e7 years labelled as an
  order of magnitude versus 1e10 years galaxy age) to state the paradox;
  no invented numbers beyond these orders of magnitude.'

Caption / figure id : `fig:fermi-filters`
Markdown source     : book/14_synthesis/synthesis.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/14_synthesis/figures/fermi_filters.avif"


def panel_a(ax: plt.Axes) -> None:
    """Draw the Drake-equation filter chain and proposed resolutions.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axis for the horizontal sequence diagram.
    """
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.55, 1.95)
    ax.axis("off")
    ax.set_title(
        "(a) Drake-equation filter chain and proposed resolutions (schematic)",
        fontsize=11, fontweight="bold", loc="left",
    )

    # 7 Drake-equation filter boxes across the row
    boxes = [
        ("Stars\n($R_\\star$)", False),
        ("Planets\n($f_p$)", False),
        ("Habitable\nplanets ($n_e$)", False),
        ("Life\n($f_l$)", True),
        ("Intelligence\n($f_i$)", True),
        ("Technology\n($f_c$)", False),
        ("Lifetime\n($L$)", True),
    ]

    xs = np.linspace(0.72, 9.28, 7)
    y_box = 0.70
    box_w = 1.12
    box_h = 0.58

    for i, ((label, is_filter), x) in enumerate(zip(boxes, xs)):
        fc = "#fef0d9" if is_filter else "#eef4f8"
        ec = "#e6550d" if is_filter else "#4a6984"
        rect = FancyBboxPatch(
            (x - box_w / 2, y_box - box_h / 2), box_w, box_h,
            boxstyle="round,pad=0.03,rounding_size=0.08",
            facecolor=fc, edgecolor=ec, lw=1.1,
        )
        ax.add_patch(rect)
        ax.text(x, y_box, label, ha="center", va="center", fontsize=10)
        if i < 6:
            next_x = xs[i + 1]
            ax.annotate(
                "", xy=(next_x - box_w / 2 - 0.02, y_box),
                xytext=(x + box_w / 2 + 0.02, y_box),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="0.3"),
            )

    # Three annotations placing proposed resolutions on the filter chain
    # Resolution 1: Rare life at f_l (above box 3)
    ax.text(
        xs[3], 1.58, "Rare-life hypothesis\n($f_l$ is very small)",
        ha="center", va="center", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#fee8c8",
                  edgecolor="#e6550d", lw=0.9),
    )
    ax.annotate(
        "", xy=(xs[3], y_box + box_h / 2 + 0.03), xytext=(xs[3], 1.30),
        arrowprops=dict(arrowstyle="->", lw=1.1, color="#e6550d"),
    )

    # Resolution 2: Rare intelligence at f_i (below box 4)
    ax.text(
        xs[4], -0.22, "Rare-intelligence hypothesis\n($f_i$ bottleneck)",
        ha="center", va="center", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#fee8c8",
                  edgecolor="#e6550d", lw=0.9),
    )
    ax.annotate(
        "", xy=(xs[4], y_box - box_h / 2 - 0.03), xytext=(xs[4], 0.06),
        arrowprops=dict(arrowstyle="->", lw=1.1, color="#e6550d"),
    )

    # Resolution 3: Great Filter at L (above box 6)
    ax.text(
        xs[6], 1.58, "Great Filter\n(short lifetime $L$)",
        ha="center", va="center", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#fee8c8",
                  edgecolor="#e6550d", lw=0.9),
    )
    ax.annotate(
        "", xy=(xs[6], y_box + box_h / 2 + 0.03), xytext=(xs[6], 1.30),
        arrowprops=dict(arrowstyle="->", lw=1.1, color="#e6550d"),
    )


def _note(ax: plt.Axes) -> None:
    """Add the two resolutions that act on observational limits."""
    ax.text(0.18, -0.30, "Outside the chain, two resolutions act on\nobservational limits: detection threshold\n(signals below sensitivity) and zoo scenarios",
            ha="left", va="center", fontsize=10, color="0.35", style="italic")


def panel_b(ax: plt.Axes) -> None:
    """Draw the galactic crossing time versus galaxy age comparison bars.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axis for the horizontal timescale comparison bars.
    """
    ax.set_xscale("log")
    ax.set_xlim(1e6, 2e10)
    ax.set_ylim(-0.65, 1.55)
    ax.set_title(
        "(b) Galactic crossing time versus galaxy age (schematic)",
        fontsize=11, fontweight="bold", loc="left",
    )

    # Milky Way galaxy age bar: 10^10 yr duration
    ax.barh(0, 1e10 - 1e6, left=1e6, height=0.38,
            color="#bdd7e7", edgecolor="#2171b5", lw=1.0)
    ax.text(
        2e7, 0, r"Milky Way galaxy age: $\sim 10^{10}$ yr",
        va="center", ha="left", fontsize=10, fontweight="bold",
        color="#08519c",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor="none", alpha=0.9),
    )

    # Galactic crossing time bar: order 10^6 to 10^7 yr
    ax.barh(1, 1e7 - 1e6, left=1e6, height=0.38,
            color="#fcbba1", edgecolor="#cb181d", lw=1.0)
    ax.text(
        1.5e7, 1,
        r"Galactic crossing time at 0.01 to 0.1 $c$: $\sim 10^6$ to $10^7$ yr",
        va="center", ha="left", fontsize=10, fontweight="bold",
        color="#a50f15",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor="none", alpha=0.9),
    )

    # Statement of the paradox from subsection text
    ax.text(
        1.2e6, -0.48,
        r"Paradox: crossing time ($10^6$ to $10^7$ yr) $\ll$ galaxy age "
        r"($10^{10}$ yr): where is everybody?",
        fontsize=10, fontstyle="italic", color="0.25",
        bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                  edgecolor="none", alpha=0.9),
    )

    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Galaxy age", "Crossing time"], fontsize=10)
    ax.set_xlabel("Timescale (years, logarithmic scale)", fontsize=10)


def make_plot() -> Path:
    """Build the two-panel Fermi paradox figure and save to AVIF.

    Returns
    -------
    pathlib.Path
        Path to the saved AVIF image.
    """
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(
        2, 1, figsize=(9.0, 4.2),
        gridspec_kw={"height_ratios": [1.35, 1.0]},
    )
    panel_a(ax_a)
    _note(ax_a)
    panel_b(ax_b)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Execute figure generation and display output path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()