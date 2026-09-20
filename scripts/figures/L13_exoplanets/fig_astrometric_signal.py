"""Astrometric reflex amplitude against distance for planetary analogues.

Angular amplitude alpha = (m_p / M_star) * (a_p / d) yields arcseconds when
a_p is in AU and d in pc, scaled by 1e6 to microarcseconds. Gaia achieves a
final precision of about 10 microarcseconds for bright stars.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
# Output path: book/13_exoplanets/figures/astrometric_signal.avif
OUT_AVIF = REPO_ROOT / "book/13_exoplanets/figures/astrometric_signal.avif"

# Parameters
# Jupiter analogue: m_p / M_star = 1 / 1047, a_p = 5.2 AU
M_JUP_OVER_M_STAR = 1.0 / 1047.0
A_JUP_AU = 5.2

# Earth analogue: m_p / M_star = 1 / 333000, a_p = 1.0 AU
M_EARTH_OVER_M_STAR = 1.0 / 333000.0
A_EARTH_AU = 1.0

# Gaia final precision for bright stars: about 10 microarcseconds
GAIA_PRECISION_UAS = 10.0


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(5.76, 3.24))

    # Distance d from 1 to 100 pc on log-log axes
    d = np.logspace(0, 2, 300)

    # alpha in microarcseconds: (m_p / M_star) * a_p[AU] / d[pc] * 1e6
    alpha_jup = M_JUP_OVER_M_STAR * (A_JUP_AU / d) * 1e6
    alpha_earth = M_EARTH_OVER_M_STAR * (A_EARTH_AU / d) * 1e6

    ax.loglog(d, alpha_jup, color="#1f6db8", lw=2.2)
    ax.loglog(d, alpha_earth, color="#2ca25f", lw=2.2)

    # Gaia threshold: about 10 microarcseconds
    ax.axhline(
        GAIA_PRECISION_UAS,
        color="#c0392b",
        linestyle="--",
        lw=1.8,
    )

    # Anchor values at 10 pc
    # Jupiter analogue: about 500 uas (half a milliarcsecond)
    # Earth analogue: 0.3 uas
    d_anchor = 10.0
    alpha_jup_10 = M_JUP_OVER_M_STAR * (A_JUP_AU / d_anchor) * 1e6
    alpha_earth_10 = M_EARTH_OVER_M_STAR * (A_EARTH_AU / d_anchor) * 1e6

    ax.plot(d_anchor, alpha_jup_10, "o", color="#1f6db8", ms=6, zorder=5)
    ax.plot(d_anchor, alpha_earth_10, "o", color="#2ca25f", ms=6, zorder=5)

    ax.annotate(
        "10 pc: about 500 $\\mu$as\n(half a milliarcsecond)",
        xy=(d_anchor, alpha_jup_10),
        xytext=(2.0, 40.0),
        fontsize=10,
        color="#1f6db8",
        arrowprops=dict(arrowstyle="->", color="#1f6db8", lw=1.0),
    )

    ax.annotate(
        "10 pc: 0.3 $\\mu$as",
        xy=(d_anchor, alpha_earth_10),
        xytext=(3.0, 0.05),
        fontsize=10,
        color="#2ca25f",
        arrowprops=dict(arrowstyle="->", color="#2ca25f", lw=1.0),
    )

    ax.set_xlim(1.0, 100.0)
    ax.set_ylim(0.01, 10000.0)
    ax.set_xlabel("Distance (pc)")
    ax.set_ylabel(r"Angular reflex amplitude $\alpha$ ($\mu$as)")
    # Title
    ax.set_title("Astrometric reflex amplitude against distance", fontsize=11)
    # Line labels along each curve, with a white halo where the label sits on its line
    halo = dict(facecolor="white", edgecolor="none", pad=1.5)
    fig.canvas.draw()
    for label, y_of, colour in (
        ("Jupiter analogue (5.2 AU)", lambda x: M_JUP_OVER_M_STAR * (A_JUP_AU / x) * 1e6, "#1f6db8"),
        ("Earth analogue (1 AU)", lambda x: M_EARTH_OVER_M_STAR * (A_EARTH_AU / x) * 1e6, "#2ca25f"),
    ):
        x0, x1 = 30.0, 60.0
        (px0, py0), (px1, py1) = ax.transData.transform([(x0, y_of(x0)), (x1, y_of(x1))])
        angle = np.degrees(np.arctan2(py1 - py0, px1 - px0))
        ax.annotate(label, xy=(36.0, y_of(36.0)), xytext=(0, 5), textcoords="offset points",
                    rotation=angle, rotation_mode="anchor", ha="center", va="bottom",
                    fontsize=10, color=colour, bbox=halo)
    ax.text(95.0, 14.0, "Gaia, about 10 microarcseconds", ha="right", va="bottom", fontsize=10, color="#c0392b")

    fig.tight_layout()
    save_figure(fig, OUT_AVIF, dpi=280)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
