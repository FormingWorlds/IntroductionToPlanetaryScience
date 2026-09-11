"""Stellar radial velocity signals and spectroscopic detection limits.

Planetary reflex motion induces a Doppler semi-amplitude K in the host star,
reaching 12.5 m/s for a Jupiter analogue, 2.7 m/s for Saturn, and 0.09 m/s
for Earth, compared to instrumental precisions from 10 m/s down to 0.1 m/s.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/13_exoplanets/figures/radial_velocity_signal.avif"


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.4))

    # --- Panel (a): Reflex motion of a Sun with a Jupiter analogue ---
    # Stellar reflex velocity curve v_r(t) = K sin(2 pi t / P) over two periods
    t = np.linspace(0, 2, 500)
    # Jupiter analogue around Sun produces K = 12.5 m/s
    v = 12.5 * np.sin(2 * np.pi * t)
    ax1.plot(t, v, color="#1f6db8", lw=2.0)
    ax1.axhline(0, color="0.7", linestyle=":", lw=0.8)
    ax1.set_xlim(0, 2.0)
    ax1.set_ylim(-15, 18)
    ax1.set_xlabel("Time (orbital periods, $t/P$)")
    ax1.set_ylabel("Stellar radial velocity (m/s)")
    ax1.set_title("(a) Reflex motion of a Sun with a Jupiter analogue", fontsize=11)

    # Mark semi-amplitude K with double-headed arrow from 0 to peak
    ax1.add_patch(
        FancyArrowPatch((0.25, 0.3), (0.25, 12.2), arrowstyle="<|-|>", mutation_scale=10, color="#c0392b", lw=1.5)
    )
    ax1.text(0.27, 13.2, "$K = 12.5$ m/s", ha="left", va="bottom", fontsize=10, color="#c0392b")

    # Horizontal precision lines: ELODIE 10 m/s, HARPS 1 m/s, ESPRESSO 10 cm/s = 0.1 m/s
    ax1.axhline(10, color="#c0392b", linestyle="--", lw=1.2)
    ax1.axhline(1, color="#c46b1a", linestyle="--", lw=1.2)
    ax1.axhline(0.1, color="#2ca25f", linestyle="--", lw=1.2)

    bbox_white = dict(facecolor="white", edgecolor="none", pad=1.5)
    ax1.text(1.95, 10.0, "ELODIE\n(10 m/s)", ha="right", va="center", fontsize=10, color="#c0392b", bbox=bbox_white)
    ax1.text(1.95, 2.3, "HARPS\n(1 m/s)", ha="right", va="center", fontsize=10, color="#c46b1a", bbox=bbox_white)
    ax1.text(1.95, -1.3, "ESPRESSO\n(0.1 m/s)", ha="right", va="center", fontsize=10, color="#2ca25f", bbox=bbox_white)

    # --- Panel (b): Bar chart of semi-amplitudes against instrument precision ---
    # Three analogues: Jupiter 12.5 m/s, Saturn at 9.5 AU 2.7 m/s, Earth at 1 AU 0.09 m/s
    planets = ["Jupiter\n(12.5 m/s)", "Saturn, 9.5 AU\n(2.7 m/s)", "Earth, 1 AU\n(0.09 m/s)"]
    k_vals = [12.5, 2.7, 0.09]
    x = np.arange(len(planets))
    ax2.bar(x, k_vals, width=0.5, color="#1f6db8", alpha=0.85, edgecolor="black", lw=0.8)
    ax2.set_yscale("log")
    ax2.set_ylim(0.03, 35)
    ax2.set_xlim(-0.5, 2.9)
    ax2.set_xticks(x)
    ax2.set_xticklabels(planets)
    ax2.set_ylabel(r"Semi-amplitude $K_\star$ (m/s)")
    ax2.set_title("(b) Semi-amplitudes against instrument precision", fontsize=11)

    # Instrument precision lines repeated on log scale
    ax2.axhline(10, color="#c0392b", linestyle="--", lw=1.2)
    ax2.axhline(1, color="#c46b1a", linestyle="--", lw=1.2)
    ax2.axhline(0.1, color="#2ca25f", linestyle="--", lw=1.2)

    ax2.text(2.85, 11.5, "10 m/s (ELODIE)", ha="right", va="bottom", fontsize=10, color="#c0392b")
    ax2.text(2.85, 1.15, "1 m/s (HARPS)", ha="right", va="bottom", fontsize=10, color="#c46b1a")
    ax2.text(2.85, 0.115, "0.1 m/s (ESPRESSO)", ha="right", va="bottom", fontsize=10, color="#2ca25f")

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
