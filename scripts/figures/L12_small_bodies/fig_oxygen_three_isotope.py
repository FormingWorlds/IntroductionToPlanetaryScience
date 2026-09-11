"""Oxygen three-isotope diagram as a parent-body fingerprint.

Mass-dependent fractionation yields a slope-1/2 line; CAIs define a slope-1 line.
Cluster positions are schematic; only slopes and ordering come from the text.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/12_small_bodies/figures/oxygen_three_isotope.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.8, 4.8))

    ax.set_xlim(-10, 10)
    ax.set_ylim(-8, 6)
    ax.set_xlabel(r"$\delta^{18}\mathrm{O}$ (‰)")
    ax.set_ylabel(r"$\delta^{17}\mathrm{O}$ (‰)")
    ax.set_title("Oxygen isotopes fingerprint the parent body", fontsize=11)

    p1 = ax.transData.transform((0, 0))
    p2 = ax.transData.transform((2, 1))
    disp_slope_half = float(np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0])))

    q1 = ax.transData.transform((0, 0))
    q2 = ax.transData.transform((1, 1))
    disp_slope_one = float(np.degrees(np.arctan2(q2[1] - q1[1], q2[0] - q1[0])))

    # Terrestrial fractionation line: slope 1/2 through origin (0, 0)
    x_tfl = np.array([-10.0, 10.0])
    ax.plot(x_tfl, 0.5 * x_tfl, color="#1f6db8", lw=2.0, zorder=2)
    ax.text(
        -9.3,
        1.8,
        "terrestrial fractionation line, slope 1/2:\nEarth, Moon, enstatite chondrites",
        fontsize=10,
        color="#1f6db8",
        ha="left",
        va="bottom",
    )
    ax.annotate(
        "",
        xy=(-3.5, -1.75),
        xytext=(-5.5, 1.6),
        arrowprops=dict(arrowstyle="->", color="#1f6db8", lw=1.2),
    )

    # CAI line: slope 1 passing through origin region, extending to negative values
    x_cai = np.array([-7.5, 0.8])
    y_cai = 1.0 * x_cai - 0.5
    ax.plot(x_cai, y_cai, color="#c0392b", lw=2.0, ls="--", zorder=2)
    ax.text(
        -3.0,
        -7.2,
        "CAI line, slope 1:\nmixing with a $^{16}$O-rich reservoir",
        fontsize=10,
        color="#c0392b",
        ha="left",
        va="bottom",
    )
    ax.annotate(
        "",
        xy=(-5.5, -6.0),
        xytext=(-3.2, -6.6),
        arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.2),
    )

    # Carbonaceous chondrites: cluster below terrestrial line
    e_cc = Ellipse(
        (-1.5, -3.5),
        width=4.0,
        height=2.0,
        angle=disp_slope_one,
        facecolor="#fdebd0",
        edgecolor="#c46b1a",
        lw=1.2,
        zorder=3,
    )
    ax.add_patch(e_cc)
    ax.text(
        1.2,
        -3.5,
        "Carbonaceous\nchondrites",
        fontsize=10,
        color="#c46b1a",
        ha="left",
        va="center",
        zorder=4,
    )
    ax.annotate(
        "",
        xy=(0.3, -3.5),
        xytext=(1.0, -3.5),
        arrowprops=dict(arrowstyle="->", color="#c46b1a", lw=1.0),
    )

    # Ordinary chondrites: cluster above terrestrial line
    e_oc = Ellipse(
        (1.8, 4.0),
        width=3.6,
        height=1.4,
        angle=disp_slope_half,
        facecolor="#e8f1fa",
        edgecolor="#1f6db8",
        lw=1.2,
        zorder=3,
    )
    ax.add_patch(e_oc)
    ax.text(
        1.8,
        5.0,
        "Ordinary chondrites",
        fontsize=10,
        color="#1f6db8",
        ha="center",
        va="bottom",
        zorder=4,
    )

    # SNC (Mars): short parallel line of slope 1/2 offset above terrestrial line
    x_snc = np.array([4.2, 5.8])
    y_snc = 0.5 * x_snc + 0.9
    ax.plot(x_snc, y_snc, color="#4a6984", lw=1.2, ls=":", zorder=2)
    e_snc = Ellipse(
        (5.0, 0.5 * 5.0 + 0.9),
        width=1.3,
        height=0.55,
        angle=disp_slope_half,
        facecolor="#fadbd8",
        edgecolor="#c0392b",
        lw=1.2,
        zorder=3,
    )
    ax.add_patch(e_snc)
    ax.text(
        5.0,
        4.1,
        "SNC: Mars",
        fontsize=10,
        color="#c0392b",
        ha="center",
        va="bottom",
        zorder=4,
    )

    # HED (Vesta): short parallel line of slope 1/2 offset below terrestrial line
    x_hed = np.array([1.8, 3.6])
    y_hed = 0.5 * x_hed - 0.9
    ax.plot(x_hed, y_hed, color="#4a6984", lw=1.2, ls=":", zorder=2)
    e_hed = Ellipse(
        (2.7, 0.5 * 2.7 - 0.9),
        width=1.3,
        height=0.55,
        angle=disp_slope_half,
        facecolor="#e8f5e9",
        edgecolor="#2ca25f",
        lw=1.2,
        zorder=3,
    )
    ax.add_patch(e_hed)
    ax.text(
        2.7,
        -0.9,
        "HED: Vesta",
        fontsize=10,
        color="#2ca25f",
        ha="center",
        va="top",
        zorder=4,
    )

    # CI chondrites with Ryugu: cluster below line near positive end
    e_ci = Ellipse(
        (8.0, 2.2),
        width=2.4,
        height=1.4,
        angle=disp_slope_half,
        facecolor="#fdebd0",
        edgecolor="#c46b1a",
        lw=1.2,
        zorder=3,
    )
    ax.add_patch(e_ci)
    ax.text(
        8.0,
        1.0,
        "CI chondrites\nwith Ryugu",
        fontsize=10,
        color="#c46b1a",
        ha="center",
        va="top",
        zorder=4,
    )

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
