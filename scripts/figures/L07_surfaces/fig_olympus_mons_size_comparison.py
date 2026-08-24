"""Generate Fig. (`fig:olympus-comparison`).

Height comparison between Olympus Mons and the two tallest mountains on
Earth, drawn on one linear elevation axis so the three edifices can be
read against each other directly.

Each silhouette rises from its own base, which is the reference the
quoted height belongs to:

    Olympus Mons   21.2 km above the Mars datum
    Mauna Kea      10.2 km above the ocean floor it stands on
    Mount Everest   8.848 km above sea level

Only the vertical axis carries a scale. The horizontal axis is unlabelled
because the three footprints are too unequal to share one scale: Olympus
Mons is about 600 km across at its base, many times the width of either
terrestrial mountain, so a true horizontal scale would reduce Everest to a
line. The drawn widths are compressed. The compression keeps the order of
the real footprints, and it keeps Olympus Mons the flattest of the three
profiles, so the shield stays broad and gently sloping rather than steep.

Caption / figure id : `fig:olympus-comparison`
Markdown source     : book/07_surfaces/surfaces.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/07_surfaces/figures/olympus_mons_size_comparison.avif"

# Summit height above the base each quoted value is referred to, in km.
OLYMPUS_H = 21.2      # above the Mars datum
MAUNA_KEA_H = 10.2    # above the ocean floor
EVEREST_H = 8.848     # above sea level

# Colours: Martian rust, Hawaiian basalt green, Himalayan rock grey.
OLYMPUS_FILL = "#c07a4e"
MAUNA_KEA_FILL = "#4f7d4a"
EVEREST_FILL = "#8d8f96"

# Drawn half-widths and centres, in schematic x units. Real width-to-height
# is about 28 for Olympus Mons and several times less for the two terrestrial
# mountains. The drawn values compress that range hard but keep its order, so
# Olympus Mons stays the flattest silhouette of the three.
LAYOUT = {"olympus": (3.05, 3.35), "mauna_kea": (0.85, 8.20), "everest": (0.55, 10.60)}


def shield_profile(half_width: float, height: float, exponent: float) -> tuple[np.ndarray, np.ndarray]:
    """Silhouette of one edifice as a smooth peak of the given height.

    Parameters
    ----------
    half_width
        Half the drawn footprint, in the figure's schematic x units.
    height
        Summit height above the base, in km.
    exponent
        Flank shape. Values above 1 give the convex, broad-shouldered
        profile of a shield volcano; values below 1 give the concave
        flanks of a steep peak.

    Returns
    -------
    x, y
        Offsets from the edifice centre and elevations above its base.
    """
    # Odd sample count, so x = 0 is on the grid and the summit reaches its
    # full height. With an even count a sharp peak falls short of it.
    x = np.linspace(-half_width, half_width, 401)
    y = height * (1.0 - np.abs(x / half_width) ** exponent)
    return x, y


def make_plot() -> Path:
    """Draw the comparison and write the AVIF."""
    apply_style()
    fig, ax = plt.subplots(figsize=(10.0, 5.625))

    edifices = [
        ("olympus", "Olympus Mons\n(Mars)", OLYMPUS_H, OLYMPUS_FILL, 2.6),
        ("mauna_kea", "Mauna Kea\n(Hawaii)", MAUNA_KEA_H, MAUNA_KEA_FILL, 2.0),
        ("everest", "Mount Everest\n(Himalaya)", EVEREST_H, EVEREST_FILL, 0.75),
    ]

    for key, label, height, fill, exponent in edifices:
        half_width, centre = LAYOUT[key]
        x, y = shield_profile(half_width, height, exponent)
        ax.fill_between(centre + x, 0.0, y, color=fill, linewidth=0.8,
                        edgecolor="#3a3a3a", zorder=3)
        ax.annotate(f"{height:.1f} km", xy=(centre, height),
                    xytext=(0, 6), textcoords="offset points",
                    ha="center", va="bottom", fontsize=11, fontweight="bold",
                    zorder=4)
        ax.text(centre, -1.4, label, ha="center", va="top", fontsize=10)

    # Guides at the two terrestrial summits, so the comparison is readable
    # off the Olympus Mons silhouette without going back to the axis.
    for height, colour in ((MAUNA_KEA_H, MAUNA_KEA_FILL), (EVEREST_H, EVEREST_FILL)):
        ax.axhline(height, color=colour, linestyle="--", linewidth=1.0,
                   alpha=0.85, zorder=1)

    ax.set_xlim(-0.5, 12.4)
    ax.set_ylim(-3.4, 23.6)
    ax.set_yticks(np.arange(0, 25, 5))
    ax.set_ylabel("Height above base (km)")
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.grid(axis="y", linestyle=":", alpha=0.35)
    ax.grid(axis="x", visible=False)
    ax.axhline(0.0, color="#3a3a3a", linewidth=1.0, zorder=2)

    ax.text(12.2, 22.6,
            "Olympus Mons is 2.4 times the height\n"
            "of Everest and 2.1 times the height\n"
            "of Mauna Kea. Heights share one scale;\n"
            "widths are schematic.",
            ha="right", va="top", fontsize=10.5, style="italic")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    print(make_plot())


if __name__ == "__main__":
    main()
