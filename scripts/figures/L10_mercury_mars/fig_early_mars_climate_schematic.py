"""Generate Fig. (`fig:early-mars-climate-schematic`).

Two-panel schematic of the "cold baseline with transient warm excursions"
picture of the early Mars climate. Both panels are an idealised
cross-section from the northern lowlands (left) to the southern highlands
(right). Panel (a): the cold baseline, in which water vapour condenses as
snow on the high, cold southern terrain (the icy-highlands hypothesis) and
the lowland basins stay frozen. Panel (b): a transient warm excursion, in
which H2 from volcanism, serpentinisation or a large impact strengthens
the greenhouse effect through H2-CO2 collision-induced absorption, snow
melts and runs downhill, and the excursion ends when H2 escapes to space.
Carbonate formation in wet ground is the long-term CO2 sink that acts over
many excursions.

The script writes the book AVIF and copies it to the lecture-10 deck.

Caption / figure id : `fig:early-mars-climate-schematic`
Markdown source     : book/10_mercury_mars/mercury_mars.md
Citation keys       : Wordsworth2016, Wordsworth2017, Wordsworth2021,
                      Kite2019, KiteEpisodic2021, KiteConway2024, Kite2025
"""

from __future__ import annotations

import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/10_mercury_mars/figures/early_mars_climate_schematic.avif"
DECK_AVIF = REPO_ROOT / "slides/lecture10/figures/early_mars_climate_schematic.avif"

ROCK = "#b98a62"
ROCK_DARK = "#8a6142"
CRYO = "#c7d3dd"
WATER = "#4a86c5"
ICE = "#d9e6f0"
ICE_EDGE = "#9dbad6"
CLOUD = "#dfe8f0"
SUN = "#f2d27a"
LAVA = "#c8553d"
DELTA = "#d9b98a"
CARBONATE = "#fbf3df"
BLUE_TXT = "#2f5f8f"
RED_TXT = "#8f3f2f"
GREY_TXT = "0.3"

# Surface profile: lowland plain with a basin, slope, highland plateau
PROFILE = np.array(
    [
        (0.0, 0.5),
        (1.0, 0.5),
        (1.3, 0.2),
        (2.9, 0.2),
        (3.2, 0.5),
        (3.6, 0.55),
        (5.4, 1.45),
        (5.7, 1.5),
        (10.0, 1.5),
    ]
)
LAKE_LEVEL = 0.46
# Basin walls cross the lake level at these x positions
LAKE_X0 = 1.0 + 0.3 * (0.5 - LAKE_LEVEL) / 0.3
LAKE_X1 = 2.9 + 0.3 * (LAKE_LEVEL - 0.2) / 0.3


def surface_y(x):
    """Return the surface elevation of the idealised profile at ``x``.

    Parameters
    ----------
    x : float or array_like
        Horizontal position in axis units (0 = north, 10 = south).

    Returns
    -------
    float or ndarray
        Surface elevation interpolated linearly along ``PROFILE``.
    """
    return np.interp(x, PROFILE[:, 0], PROFILE[:, 1])


def ground(ax):
    """Draw the rock, the cryosphere band and the surface line.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes in the panel coordinate system.
    """
    xs = PROFILE[:, 0]
    ys = PROFILE[:, 1]
    rock = np.vstack([np.column_stack([xs, ys]), [(10.0, -1.0), (0.0, -1.0)]])
    ax.add_patch(Polygon(rock, closed=True, facecolor=ROCK, edgecolor="none"))
    # Cryosphere: a frozen band directly under the surface
    cryo = np.vstack(
        [np.column_stack([xs, ys - 0.04]), np.column_stack([xs[::-1], ys[::-1] - 0.42])]
    )
    ax.add_patch(
        Polygon(cryo, closed=True, facecolor=CRYO, edgecolor="none", alpha=0.85)
    )
    ax.plot(xs, ys, color="0.35", lw=1.2)
    ax.text(
        0.25,
        -0.8,
        "northern lowlands",
        ha="left",
        va="center",
        fontsize=9,
        color="white",
    )
    ax.text(
        9.75,
        -0.8,
        "southern highlands",
        ha="right",
        va="center",
        fontsize=9,
        color="white",
    )


def snow(ax, x0, thickness):
    """Draw a snowpack that tapers in from ``x0`` and covers the terrain south of it.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    x0 : float
        Northern edge of the snowpack in axis units.
    thickness : float
        Full snow thickness in axis units, reached 0.8 units south of ``x0``.
    """
    xs = np.linspace(x0, 10.0, 40)
    ys = surface_y(xs)
    taper = np.clip((xs - x0) / 0.8, 0, 1)
    top = ys + thickness * taper
    poly = np.vstack(
        [np.column_stack([xs, top]), np.column_stack([xs[::-1], ys[::-1]])]
    )
    ax.add_patch(
        Polygon(poly, closed=True, facecolor="white", edgecolor=ICE_EDGE, lw=0.8)
    )


def clouds(ax, centres, y, color=CLOUD):
    """Draw a row of elliptical cloud symbols.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    centres : iterable of float
        Horizontal centres of the cloud ellipses.
    y : float
        Common vertical centre of the row.
    color : str, optional
        Fill colour of the ellipses.
    """
    for x in centres:
        ax.add_patch(
            Ellipse((x, y), 0.75, 0.28, facecolor=color, edgecolor="0.6", lw=0.6)
        )


def basin(ax, wet):
    """Fill the lowland basin, either with ground ice or with a lake and delta.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    wet : bool
        If True, draw open water, a delta at the southern shore and a
        carbonate-bearing sediment layer on the lake floor; otherwise fill
        the basin with ground ice.
    """
    fill = [(LAKE_X0, LAKE_LEVEL), (1.3, 0.2), (2.9, 0.2), (LAKE_X1, LAKE_LEVEL)]
    if not wet:
        ax.add_patch(
            Polygon(fill, closed=True, facecolor=ICE, edgecolor=ICE_EDGE, lw=0.7)
        )
        return
    ax.add_patch(Polygon(fill, closed=True, facecolor=WATER, edgecolor="none"))
    # Lake-floor sediment with carbonate nodules
    ax.add_patch(
        Polygon(
            [(1.3, 0.2), (2.75, 0.2), (2.6, 0.28), (1.4, 0.28)],
            closed=True,
            facecolor=DELTA,
            edgecolor="none",
        )
    )
    for x in (1.55, 1.8, 2.05, 2.3):
        ax.add_patch(
            Circle((x, 0.24), 0.035, facecolor=CARBONATE, edgecolor="0.45", lw=0.5)
        )
    # Delta: a sediment wedge from the southern shore onto the lake floor
    ax.add_patch(
        Polygon(
            [(LAKE_X1, LAKE_LEVEL), (2.55, LAKE_LEVEL), (2.75, 0.2), (2.9, 0.2)],
            closed=True,
            facecolor=DELTA,
            edgecolor="none",
        )
    )


def panel_a(ax):
    """Draw panel (a): the cold baseline of the icy-highlands hypothesis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    """
    ax.text(
        0.0,
        4.13,
        "(a) cold baseline (icy highlands): snow collects on the southern highlands",
        fontsize=10.5,
        fontweight="bold",
        va="top",
    )
    ground(ax)
    snow(ax, 5.0, 0.25)
    basin(ax, wet=False)
    # Faint young Sun
    ax.add_patch(Circle((0.55, 2.75), 0.28, facecolor=SUN, edgecolor="0.5", lw=0.7))
    ax.text(
        1.0,
        2.75,
        "faint young Sun:\n~75% of today's flux",
        ha="left",
        va="center",
        fontsize=9,
        color=GREY_TXT,
    )
    ax.text(
        1.0,
        2.05,
        "mean surface temperature $\\leq$ 225 K:\nprecipitation falls only as snow",
        ha="left",
        va="center",
        fontsize=9,
        color=BLUE_TXT,
    )
    ax.text(
        2.1,
        0.92,
        "frozen lowland basin",
        ha="center",
        va="bottom",
        fontsize=9,
        color=BLUE_TXT,
    )
    # Vapour transport uphill, deposited as snow on the cold highlands
    ax.add_patch(
        FancyArrowPatch(
            (3.9, 1.1),
            (6.3, 1.9),
            connectionstyle="arc3,rad=-0.25",
            arrowstyle="-|>",
            mutation_scale=16,
            lw=1.6,
            color=BLUE_TXT,
        )
    )
    ax.text(
        4.3,
        2.35,
        "water vapour moves uphill,\ncondenses as snow",
        ha="center",
        va="bottom",
        fontsize=9,
        color=BLUE_TXT,
    )
    ax.text(
        7.9,
        1.95,
        "snow and ice accumulate\non the cold highlands",
        ha="center",
        va="bottom",
        fontsize=9,
        color=BLUE_TXT,
    )
    # CO2 ice clouds aloft
    clouds(ax, (5.3, 6.05, 6.8), 3.05)
    ax.text(
        7.35,
        3.05,
        "CO$_2$ ice clouds:\nsmall net effect",
        ha="left",
        va="center",
        fontsize=9,
        color=GREY_TXT,
    )
    ax.text(
        8.3, 1.26, "cryosphere", ha="center", va="center", fontsize=9, color=GREY_TXT
    )


def panel_b(ax):
    """Draw panel (b): a transient warm excursion with snowmelt and rivers.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Target axes.
    """
    ax.text(
        0.0,
        4.13,
        "(b) transient warm excursion, repeated: snow melts, runoff cuts valleys",
        fontsize=10.5,
        fontweight="bold",
        va="top",
    )
    ground(ax)
    snow(ax, 6.0, 0.22)
    basin(ax, wet=True)
    # Warm H2-CO2 atmosphere
    ax.text(
        0.3,
        2.55,
        "H$_2$-CO$_2$ collision-induced absorption:\n"
        "warm enough for melt and rivers, at least seasonally",
        ha="left",
        va="center",
        fontsize=9,
        color=RED_TXT,
    )
    # H2 escape ends the excursion
    ax.add_patch(
        FancyArrowPatch(
            (0.9, 3.3),
            (0.9, 3.8),
            arrowstyle="-|>",
            mutation_scale=14,
            lw=1.4,
            color=GREY_TXT,
        )
    )
    ax.text(
        1.2,
        3.55,
        "H$_2$ escapes to space: excursion ends\n"
        "($10^5$ to $10^6$ yr in outgassing models)",
        ha="left",
        va="center",
        fontsize=9,
        color=GREY_TXT,
    )
    # Carbonate formation: the long-term CO2 sink, marked on the lake floor
    ax.text(
        0.3,
        1.6,
        "carbonate forms in wet ground:\nlong-term CO$_2$ sink",
        ha="left",
        va="center",
        fontsize=9,
        color=GREY_TXT,
    )
    ax.plot([1.15, 1.6], [1.44, 0.3], lw=0.7, color=GREY_TXT)
    # High-altitude water-ice clouds
    clouds(ax, (3.9, 4.65, 5.4), 3.1, color="white")
    ax.text(
        5.8,
        3.1,
        "H$_2$O ice clouds aloft:\nextra warming in\nsome models",
        ha="left",
        va="center",
        fontsize=9,
        color=RED_TXT,
    )
    # Large impact: a crater cut through the snow and the ground
    ax.plot([7.55, 7.08], [2.7, 1.78], ls="--", lw=1.2, color=RED_TXT)
    ax.add_patch(Circle((7.55, 2.7), 0.09, facecolor=RED_TXT, edgecolor="none"))
    ax.add_patch(
        Wedge(
            (7.0, 1.72), 0.34, 180, 360, facecolor=ROCK_DARK, edgecolor="0.35", lw=0.8
        )
    )
    for sign in (-1, 1):
        rim = [
            (7.0 + sign * 0.34, 1.72),
            (7.0 + sign * 0.46, 1.72),
            (7.0 + sign * 0.37, 1.84),
        ]
        ax.add_patch(
            Polygon(rim, closed=True, facecolor=ROCK_DARK, edgecolor="0.35", lw=0.6)
        )
    ax.text(
        6.85,
        2.3,
        "large impact:\nH$_2$ release",
        ha="right",
        va="center",
        fontsize=9,
        color=RED_TXT,
    )
    # Volcano on the plateau
    ax.add_patch(
        Polygon(
            [(8.75, 1.5), (9.45, 1.5), (9.1, 2.05)],
            closed=True,
            facecolor=LAVA,
            edgecolor="none",
        )
    )
    ax.add_patch(
        FancyArrowPatch(
            (9.1, 2.12),
            (9.1, 2.85),
            arrowstyle="-|>",
            mutation_scale=14,
            lw=1.4,
            color=GREY_TXT,
        )
    )
    ax.text(
        9.1,
        2.95,
        "volcanic H$_2$\n(rate uncertain)",
        ha="center",
        va="bottom",
        fontsize=9,
        color=GREY_TXT,
    )
    # Serpentinisation in the crust releases H2 through the surface
    ax.add_patch(
        FancyArrowPatch(
            (4.0, -0.3),
            (4.0, 0.7),
            arrowstyle="-|>",
            mutation_scale=14,
            lw=1.4,
            color="white",
        )
    )
    ax.text(
        4.0,
        -0.62,
        "serpentinisation\nreleases H$_2$",
        ha="center",
        va="center",
        fontsize=9,
        color="white",
    )
    # Snowmelt follows the slope down to the lake, fed by tributaries
    xs = np.linspace(6.25, 3.45, 30)
    ax.plot(xs, surface_y(xs) + 0.09, lw=1.8, color=WATER, solid_capstyle="round")
    for x in (5.6, 4.9):
        ax.plot(
            [x, x - 0.4],
            [surface_y(x) + 0.36, surface_y(x - 0.4) + 0.09],
            lw=1.0,
            color=WATER,
        )
    ax.annotate(
        "",
        xy=(3.15, 0.5),
        xytext=(3.45, surface_y(3.45) + 0.09),
        arrowprops=dict(arrowstyle="-|>", color=WATER, lw=1.8, mutation_scale=16),
    )
    ax.text(
        4.6,
        1.78,
        "snowmelt runs downhill,\ncuts valley networks",
        ha="center",
        va="bottom",
        fontsize=9,
        color=BLUE_TXT,
    )
    ax.text(
        2.1,
        0.92,
        "lake with delta",
        ha="center",
        va="bottom",
        fontsize=9,
        color=BLUE_TXT,
    )


def make_plot() -> Path:
    """Render both panels and write the book AVIF.

    Returns
    -------
    pathlib.Path
        Path of the written book AVIF file.
    """
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(7.6, 8.0))
    for ax in (ax_a, ax_b):
        ax.set_xlim(0, 10.0)
        ax.set_ylim(-1.0, 4.2)
        ax.set_aspect("equal")
        ax.axis("off")
    panel_a(ax_a)
    panel_b(ax_b)
    fig.tight_layout(pad=0.3)
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Write the book AVIF and copy it to the lecture-10 deck."""
    out = make_plot()
    DECK_AVIF.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(out, DECK_AVIF)
    print(f"  plot : {out}")
    print(f"  deck : {DECK_AVIF}")


if __name__ == "__main__":
    main()
