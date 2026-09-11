"""Generate Fig. (`fig:size-distance-regimes`).

Conceptual regime diagram illustrating how planet size (radius in Earth radii)
and heliocentric distance (in AU) govern rocky planet evolution
(book/10_mercury_mars/. Plots Mercury, Venus, Earth,
Mars, and the Moon at their actual radii and orbital distances
(solar_system_planets.csv:2-5; worksheets/worksheet04_content.tex:22), with
qualitative shaded regimes for retained versus lost atmospheres separated by a
schematic boundary, and an annotation arrow showing that dynamo lifetime grows
with planet size.

Caption / figure id : `fig:size-distance-regimes`
Markdown source     : book/10_mercury_mars/(lines 761-767)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.patches import FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/10_mercury_mars/figures/size_distance_regimes.avif"

# Distance in AU and radius in R_earth for rocky bodies from course data
# (solar_system_planets.csv:2-5 and worksheets/worksheet04_content.tex:22).
PLANETS: dict[str, tuple[float, float, tuple[int, int], str]] = {
    "Mercury": (0.387, 0.383, (10, 5), "left"),
    "Venus": (0.723, 0.950, (-10, 8), "right"),
    "Earth": (1.000, 1.000, (10, -5), "left"),
    "Mars": (1.524, 0.532, (-10, 6), "right"),
    "Moon": (1.000, 0.273, (10, 0), "left"),
}


def boundary_radius(distance_au: np.ndarray | float) -> np.ndarray | float:
    """Compute schematic atmospheric retention boundary radius.

    Uses a Jeans escape scaling where critical radius scales with distance
    as d^(-1/4) (book/10_mercury_mars/.

    Parameters
    ----------
    distance_au : numpy.ndarray or float
        Heliocentric distance in AU.

    Returns
    -------
    numpy.ndarray or float
        Critical planet radius in Earth radii separating retention regimes.
    """
    return 0.72 * (distance_au ** -0.25)


def make_plot() -> Path:
    """Build the size-distance regime diagram and save to AVIF.

    Returns
    -------
    pathlib.Path
        Path to the saved AVIF figure file.
    """
    apply_style()
    fig, ax = plt.subplots(figsize=(7.0, 4.3))

    # Heliocentric distance grid from 0.3 to 1.7 AU
    d_grid = np.linspace(0.3, 1.7, 300)
    r_boundary = boundary_radius(d_grid)

    # Shaded qualitative regimes
    ax.fill_between(d_grid, r_boundary, 1.20, color="#d9edf7", alpha=0.55,
                    zorder=0)
    ax.fill_between(d_grid, 0.22, r_boundary, color="#fdf0e6", alpha=0.55,
                    zorder=0)

    # Schematic retention boundary curve
    ax.plot(d_grid, r_boundary, color="#2b5c8f", ls="--", lw=1.8, zorder=1)

    # Qualitative regime labels
    ax.text(0.42, 1.10, "Atmosphere retained", fontsize=11, fontweight="bold",
            color="#1a5276", ha="center", va="center", zorder=2)
    ax.text(0.55, 0.28, "Atmosphere lost", fontsize=11, fontweight="bold",
            color="#a04000", ha="center", va="center", zorder=2)

    # Regime boundary labeled as schematic
    ax.text(0.50, 0.78, "Regime boundary (schematic)", fontsize=10,
            color="#2b5c8f", ha="center", va="center", zorder=2,
            bbox=dict(boxstyle="square,pad=0.2", facecolor="white",
                      edgecolor="none", alpha=0.85))

    # Annotation arrow: dynamo lifetime grows with size
    arrow = FancyArrowPatch((1.38, 0.70), (1.38, 1.02),
                            arrowstyle="-|>", mutation_scale=14,
                            color="#2c3e50", lw=1.5, zorder=2)
    ax.add_patch(arrow)
    ax.text(1.38, 1.06, "Dynamo lifetime\ngrows with size", fontsize=10,
            ha="center", va="bottom", color="#2c3e50", zorder=2)

    # Plot planets and Moon at actual radii and distances
    for name, (dist, rad, offset, ha) in PLANETS.items():
        ax.plot(dist, rad, "o", color="#222222", ms=7, zorder=5)
        ax.annotate(name, xy=(dist, rad), xytext=offset,
                    textcoords="offset points", fontsize=10.5,
                    fontweight="bold", ha=ha, va="center", zorder=5)

    # Axes configuration with named parameters (book/10
    ax.set_xscale("log")
    ax.set_xlim(0.3, 1.7)
    ax.set_ylim(0.22, 1.20)
    ax.set_yticks([0.4, 0.6, 0.8, 1.0, 1.2])
    ax.set_xticks([0.3, 0.5, 0.7, 1.0, 1.5])
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_formatter(ticker.NullFormatter())

    ax.set_xlabel("Distance from the Sun (AU)", fontsize=11)
    ax.set_ylabel(r"Planet size: radius ($R_\oplus$)", fontsize=11)
    ax.set_title("Rocky planet evolution regimes (schematic)", fontsize=12)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Build the figure and display the output path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()