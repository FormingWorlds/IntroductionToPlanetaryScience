"""Transit timing variations and exoplanet timing detection methods.

Gravitational interactions between planets perturb transit timings periodically,
yielding dynamical mass measurements without radial velocity follow-up.
Other timing methods include pulsar timing and eclipse timing in binaries.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
# Output path: book/13_exoplanets/figures/transit_timing_variations.avif
OUT_AVIF = REPO_ROOT / "book/13_exoplanets/figures/transit_timing_variations.avif"

# Sinusoidal TTV signal parameters
# Amplitude 5 minutes, period 12 transits, transit number 0 to 40
AMPLITUDE_MIN = 5.0  # minutes
PERIOD_TRANSITS = 12.0  # transits
N_MAX = 40  # transits


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(9.0, 4.2), gridspec_kw={"width_ratios": [1.12, 1.0]}
    )

    # --- Panel (a): Observed-minus-calculated (O-C) transit timing diagram ---
    # Transit number 0 to 40 on x, O-C in minutes on y
    transits = np.arange(0, N_MAX + 1)
    # Sinusoidal variation: amplitude 5 min, period 12 transits
    oc_points = AMPLITUDE_MIN * np.sin(2.0 * np.pi * transits / PERIOD_TRANSITS)

    transit_curve = np.linspace(0, N_MAX, 300)
    oc_curve = AMPLITUDE_MIN * np.sin(2.0 * np.pi * transit_curve / PERIOD_TRANSITS)

    # Flat dashed zero line: 'unperturbed, constant period'
    ax1.axhline(
        0,
        color="0.4",
        linestyle="--",
        linewidth=1.0,
        label="unperturbed, constant period",
    )

    # Perturbed transit signal with points and a thin line
    # "gravitational interactions periodically perturb its transit times, producing transit timing variations"
    ax1.plot(
        transit_curve,
        oc_curve,
        color="#1f6db8",
        linewidth=1.2,
        label="perturbation by a companion planet",
    )
    ax1.plot(transits, oc_points, "o", color="#1f6db8", markersize=3.5)

    ax1.set_xlim(-1, 41)
    ax1.set_ylim(-9.0, 9.0)
    ax1.set_xlabel("Transit number", fontsize=10)
    ax1.set_ylabel("O - C (minutes)", fontsize=10)
    # Title (a) 'Transit timing variations'
    ax1.set_title("(a) Transit timing variations", fontsize=11)
    ax1.legend(loc="upper right", fontsize=9, framealpha=0.95)

    # --- Panel (b): Schematic of the three timing methods ---
    # Three labelled boxes for the timing methods
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")
    # Title (b) 'Timing methods'
    ax2.set_title("(b) Timing methods", fontsize=11)

    # Box contents and citations:
    # 1. 'transit timing variations: dynamical masses (TRAPPIST-1)'
    # 2. 'pulsar timing: the first exoplanets (1992)'
    # 3. 'eclipse timing in binaries: circumbinary planets (Kepler-16 b, 2011)'
    boxes = [
        (
            0.5,
            6.8,
            9.0,
            2.6,
            "#e8f1fa",
            "#1f6db8",
            "transit timing variations:",
            "dynamical masses (TRAPPIST-1)",
        ),
        (
            0.5,
            3.7,
            9.0,
            2.6,
            "#fdebd0",
            "#c46b1a",
            "pulsar timing:",
            "the first exoplanets (1992)",
        ),
        (
            0.5,
            0.6,
            9.0,
            2.6,
            "#e8f5e9",
            "#2ca25f",
            "eclipse timing in binaries:",
            "circumbinary planets (Kepler-16 b, 2011)",
        ),
    ]

    for x, y, w, h, fc, ec, header, desc in boxes:
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.0,rounding_size=0.3",
            facecolor=fc,
            edgecolor=ec,
            lw=1.2,
        )
        ax2.add_patch(patch)
        ax2.text(
            x + w / 2,
            y + h * 0.68,
            header,
            ha="center",
            va="center",
            fontsize=10,
            weight="bold",
            color=ec,
        )
        ax2.text(
            x + w / 2,
            y + h * 0.32,
            desc,
            ha="center",
            va="center",
            fontsize=10,
            color="0.2",
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
