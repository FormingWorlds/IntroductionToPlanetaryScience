"""Timeline and thermal history of CAIs and chondrules.

CAIs condensed above about 1400 K at 4567.30 Myr, defining time zero.
Chondrules formed 2 to 4 Myr later, crystallising from droplets heated
to 1500 to 1900 K and cooling at hundreds to thousands of K per hour.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/12_small_bodies/figures/chondrule_cai_timeline.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.2))

    # --- Panel (a): Timeline of the oldest solids ---
    # Time axis in Myr after CAI formation from 0 to 5
    # Zero point defined by CAI condensation
    ax1.set_xlim(-0.5, 5.5)
    ax1.set_ylim(0.0, 3.2)
    ax1.set_xticks([0, 1, 2, 3, 4, 5])
    ax1.set_yticks([])
    ax1.spines["left"].set_visible(False)
    ax1.set_xlabel("Time after CAI formation (Myr)")
    ax1.set_title("(a) The oldest solids", fontsize=11)

    # CAIs at 0: "yield the same CAI age of 4567.30 Myr to within +-0.16 Myr"
    # Three independent Pb chronometers agree
    ax1.plot([0, 0], [0.2, 2.8], color="#c0392b", lw=2.5, zorder=3)
    ax1.plot(0, 2.1, "o", color="#c0392b", ms=7, zorder=4)
    ax1.text(
        0.18,
        2.1,
        "CAIs (time zero)\n4567.30 Myr, plus or minus 0.16 Myr;\nthree Pb chronometers agree",
        fontsize=10,
        ha="left",
        va="center",
        color="#c0392b",
    )

    # Chondrules: "systematically younger than CAIs by about 2 to 4 Myr"
    # Shaded band from 2 to 4 Myr
    ax1.axvspan(2, 4, facecolor="#e8f1fa", edgecolor="none")
    ax1.text(
        3.0,
        1.0,
        "chondrules form,\n2 to 4 Myr after CAIs",
        fontsize=10,
        ha="center",
        va="center",
        color="#1f6db8",
    )

    # --- Panel (b): Chondrule heating and cooling schematic ---
    # Temperature against time for one chondrule over 0 to 10 hours
    ax2.set_xlim(0, 10)
    ax2.set_ylim(200, 2050)
    ax2.set_xlabel("Time (hours)")
    ax2.set_ylabel("Temperature (K)")
    ax2.set_title("(b) A chondrule's heating event", fontsize=11)

    # Peak temperatures: "peak temperatures of ~ 1500-1900 K"
    ax2.axhspan(1500, 1900, facecolor="#fdebd0", edgecolor="none")
    ax2.text(
        6.0,
        1750,
        "peak temperatures: 1500 to 1900 K",
        fontsize=10,
        ha="center",
        va="center",
        color="#c46b1a",
    )

    # CAI condensation temperature: "condensed from hot gas above ~ 1400 K"
    ax2.axhline(1400, color="#c0392b", linestyle="--", lw=1.5)
    ax2.text(
        9.8,
        1460,
        "CAI condensation above about 1400 K",
        fontsize=10,
        ha="right",
        va="bottom",
        color="#c0392b",
    )

    # Cooling curves from 1700 K peak: "cooling rates from hundreds to thousands of K per hour"
    # Linear cooling over 0 to 10 hours clipped at 300 K
    t = np.linspace(0, 10, 200)
    t_slow = np.maximum(300.0, 1700.0 - 100.0 * t)
    t_fast = np.maximum(300.0, 1700.0 - 1000.0 * t)
    ax2.plot(t, t_slow, color="#1f6db8", lw=2.0)
    ax2.plot(t, t_fast, color="#4a6984", lw=2.0)

    # Curve labels
    ax2.text(
        5.5,
        750,
        "cooling at 100 K per hour",
        fontsize=10,
        ha="center",
        va="center",
        color="#1f6db8",
    )
    ax2.text(
        2.0,
        420,
        "cooling at 1000 K per hour",
        fontsize=10,
        ha="left",
        va="bottom",
        color="#4a6984",
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
