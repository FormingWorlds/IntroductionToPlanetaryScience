"""A microlensing event with a planetary perturbation.

A foreground lens star briefly magnifies light from a background star.
A planetary companion introduces an additional spike lasting hours to days,
encoding the planet mass and projected separation in Einstein radii.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
# Output path: book/13_exoplanets/figures/microlensing_lightcurve.avif
OUT_AVIF = REPO_ROOT / "book/13_exoplanets/figures/microlensing_lightcurve.avif"

# Point-lens and planetary spike parameters
# u0 = 0.3, tE = 15 days, spike near t = 8 days with amplitude 0.6 and width 0.3 days
U0 = 0.3
T_E = 15.0  # days
T_SPIKE = 8.0  # days
SPIKE_AMP = 0.6
SPIKE_WIDTH = 0.3  # days


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.2, 4.4))

    # Time grid from -30 to 30 days
    t = np.linspace(-30.0, 30.0, 1000)

    # Point-lens magnification A(u) = (u^2 + 2)/(u sqrt(u^2 + 4)) with u(t) = sqrt(u0^2 + (t/tE)^2)
    u = np.sqrt(U0**2 + (t / T_E)**2)
    a_point = (u**2 + 2.0) / (u * np.sqrt(u**2 + 4.0))

    # Planetary perturbation: Gaussian bump of amplitude 0.6 and width 0.3 days
    spike = SPIKE_AMP * np.exp(-0.5 * ((t - T_SPIKE) / SPIKE_WIDTH)**2)
    a_total = a_point + spike

    # Unperturbed single-lens baseline underneath the spike and total light curve with planet
    ax.plot(t, a_point, color="0.55", ls="--", lw=1.2)
    ax.plot(t, a_total, color="#1f6db8", lw=2.2)

    # Inset text box: 'spike amplitude and timing give the planet mass and its projected separation in Einstein radii'
    patch = FancyBboxPatch(
        (6.0, 3.05),
        23.5,
        0.95,
        boxstyle="round,pad=0.1,rounding_size=0.3",
        facecolor="#e8f1fa",
        edgecolor="#1f6db8",
        lw=1.0,
    )
    ax.add_patch(patch)

    inset_text = (
        "spike amplitude and timing give\n"
        "the planet mass and its projected\n"
        "separation in Einstein radii"
    )
    ax.text(
        17.75,
        3.525,
        inset_text,
        fontsize=10,
        color="0.15",
        ha="center",
        va="center",
    )

    # Main peak annotation: 'lens star passes in front of the source'
    ax.add_patch(
        FancyArrowPatch(
            (0.0, 3.75),
            (0.0, 3.52),
            arrowstyle="-|>",
            mutation_scale=10,
            color="0.3",
            lw=1.2,
        )
    )
    ax.text(
        -1.5,
        3.82,
        "lens star passes in front of the source",
        ha="right",
        va="bottom",
        fontsize=10,
        color="0.2",
    )

    # Planetary spike annotation: 'planet: spike of hours to days'
    ax.add_patch(
        FancyArrowPatch(
            (12.0, 2.62),
            (8.4, 2.48),
            arrowstyle="-|>",
            mutation_scale=10,
            color="#c0392b",
            lw=1.2,
        )
    )
    ax.text(
        12.5,
        2.62,
        "planet: spike of hours to days",
        ha="left",
        va="center",
        fontsize=10,
        color="#c0392b",
    )

    ax.set_xlim(-30.0, 30.0)
    ax.set_ylim(0.8, 4.3)
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Magnification")
    # Title: 'A microlensing event with a planet'
    ax.set_title("A microlensing event with a planet", fontsize=11)

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
