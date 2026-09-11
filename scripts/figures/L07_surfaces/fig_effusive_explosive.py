"""Generate Fig. (`fig:effusive-explosive`).

Two-panel cross-section schematic contrasting volcanic eruption styles:
(a) Effusive volcanism from low-viscosity basaltic magma (~50% SiO2),
forming a broad shield volcano, summit vent with quietly escaping gas,
and fissure-fed thin lava sheets (flood basalts); dominant on the Moon,
Mars, and Io.
(b) Explosive volcanism from high-viscosity silicic magma (>65% SiO2),
forming a steep stratovolcano of alternating lava and ash layers,
with a viscous plug trapping volatiles, violent explosive column,
and widespread ash fall; dominant on Earth.

Caption / figure id : `fig:effusive-explosive`
Markdown source     : book/07_surfaces/
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/07_surfaces/figures/effusive_explosive.avif"


def draw_shield_volcano(ax: plt.Axes) -> None:
    """Draw cross-section of a broad shield volcano and flood basalt plain.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes on which to draw the schematic.
    """
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-1.5, 6.0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")
    ax.set_title("(a) Effusive volcanism (schematic)",
                 fontsize=11, fontweight="bold")

    # Bedrock crust below the surface
    ax.add_patch(Rectangle((-5.0, -1.3), 10.0, 1.3, facecolor="#eae5dc",
                           edgecolor="#706a60", lw=1.0))

    # Conduit and feeder dyke for the fissure
    ax.add_patch(Rectangle((-1.35, -1.3), 0.3, 2.6, facecolor="#d94318",
                           edgecolor="#992606", lw=0.8, zorder=2))
    feeder = np.array([[-1.2, -0.4], [1.8, 0.0], [2.0, 0.0], [-1.05, -0.4]])
    ax.add_patch(Polygon(feeder, facecolor="#d94318", edgecolor="#992606",
                         lw=0.8, zorder=2))

    # Broad, low shield volcano edifice with gentle flanks
    xs = np.linspace(-4.5, 1.4, 150)
    x_summit = -1.2
    h_summit = 1.3
    ys = np.zeros_like(xs)
    left = xs <= x_summit
    right = xs > x_summit
    ys[left] = h_summit * (1.0 - ((xs[left] - x_summit) / (-4.5 - x_summit))**2)
    ys[right] = h_summit * (1.0 - ((xs[right] - x_summit) / (1.4 - x_summit))**2)

    shield_pts = list(zip(xs, ys)) + [[1.4, 0.0], [-4.5, 0.0]]
    ax.add_patch(Polygon(shield_pts, facecolor="#998f85",
                         edgecolor="#44403c", lw=1.2, zorder=3))
    ax.add_patch(Rectangle((-1.32, 0.0), 0.24, 1.3, facecolor="#d94318",
                           edgecolor="none", zorder=4))

    # Active thin lava flow on the left shield flank
    fx = np.linspace(-4.2, -1.3, 40)
    fy = h_summit * (1.0 - ((fx - x_summit) / (-4.5 - x_summit))**2)
    flow_poly_pts = (list(zip(fx, fy + 0.06))
                     + list(zip(fx[::-1], fy[::-1] + 0.01)))
    ax.add_patch(Polygon(flow_poly_pts, facecolor="#e65100",
                         edgecolor="none", zorder=4))

    # Flood basalt plain fed by the fissure
    ax.add_patch(Rectangle((1.8, 0.0), 3.1, 0.22, facecolor="#5c5650",
                           edgecolor="#44403c", lw=0.8, zorder=3))
    ax.add_patch(Rectangle((1.8, 0.16), 3.1, 0.06, facecolor="#d94318",
                           edgecolor="none", zorder=4))

    # Volatile bubbles quietly rising and escaping from the summit vent
    for by in [0.4, 0.8, 1.1, 1.45, 1.75, 2.1, 2.5]:
        bx = -1.2 + np.sin(by * 5) * 0.06
        ax.add_patch(Circle((bx, by), 0.06, facecolor="white",
                            edgecolor="#333333", lw=0.7, zorder=5))

    # Text annotations and labels
    ax.text(-3.2, 4.6,
            "Low-viscosity magma\n"
            + r"($\sim$50% $\mathrm{SiO_2}$, basaltic)" + "\n"
            "Flows easily (effusive)",
            fontsize=10, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="#cccccc", alpha=0.9))

    ax.annotate("Gas escapes quietly\n"
                + r"($\mathrm{H_2O}$, $\mathrm{CO_2}$ bubbles)",
                xy=(-1.1, 2.0), xytext=(2.0, 3.0),
                fontsize=10, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.annotate("Gentle slope\n(broad, flat edifice)",
                xy=(-2.8, 0.7), xytext=(-3.6, 2.0),
                fontsize=10, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.annotate("Fissure\neruption",
                xy=(1.8, 0.25), xytext=(1.0, 1.2),
                fontsize=10, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.annotate("Thin lava sheets\n(flood basalts)",
                xy=(3.8, 0.25), xytext=(3.8, 0.9),
                fontsize=10, ha="center", va="bottom",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.text(2.6, -0.95, "Dominant on:\nMoon, Mars, Io",
            fontsize=10, ha="center", va="center", fontweight="bold", zorder=9,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#f0ede6",
                      edgecolor="#8c827a"))


def draw_stratovolcano(ax: plt.Axes) -> None:
    """Draw cross-section of a steep stratovolcano and explosive column.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes on which to draw the schematic.
    """
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-1.5, 6.0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")
    ax.set_title("(b) Explosive volcanism (schematic)",
                 fontsize=11, fontweight="bold")

    # Bedrock crust below the surface
    ax.add_patch(Rectangle((-5.0, -1.3), 10.0, 1.3, facecolor="#eae5dc",
                           edgecolor="#706a60", lw=1.0))

    # Stratovolcano edifice built from alternating layers of lava and ash
    scales = [1.0, 0.85, 0.70, 0.55, 0.40, 0.25]
    layer_colors = ["#d4cdc3", "#9e6b55", "#d4cdc3", "#9e6b55",
                    "#d4cdc3", "#9e6b55"]
    for s, c in zip(scales, layer_colors):
        w = 2.6 * s
        h = 2.7 * s
        xs = np.linspace(-w, w, 100)
        ys = h * (1.0 - (np.abs(xs) / w)**0.8)
        pts = list(zip(xs, ys)) + [[w, 0.0], [-w, 0.0]]
        ax.add_patch(Polygon(pts, facecolor=c, edgecolor="#5c5650",
                             lw=0.6, zorder=3))

    # Central conduit with viscous silicic magma
    ax.add_patch(Rectangle((-0.2, -1.3), 0.4, 3.6, facecolor="#c25953",
                           edgecolor="#7d2e27", lw=0.8, zorder=4))

    # Viscous plug blocking the summit vent
    plug_pts = [[-0.35, 2.3], [0.35, 2.3], [0.3, 2.75], [-0.3, 2.75]]
    ax.add_patch(Polygon(plug_pts, facecolor="#3a3836",
                         edgecolor="black", lw=1.0, zorder=5))

    # Trapped gas bubbles accumulating under the viscous plug
    rng = np.random.default_rng(42)
    for by in np.linspace(1.1, 2.2, 14):
        bx = (rng.random() - 0.5) * 0.24
        r = 0.04 + rng.random() * 0.03
        ax.add_patch(Circle((bx, by), r, facecolor="white",
                            edgecolor="#333333", lw=0.7, zorder=6))

    # Explosive Plinian eruption column and umbrella cloud
    ax.add_patch(Polygon([[-0.25, 2.75], [0.25, 2.75], [0.5, 4.2], [-0.5, 4.2]],
                         facecolor="#55524f", edgecolor="none", zorder=7))
    puffs = [
        (0.0, 4.6, 0.8, "#55524f"),
        (-0.9, 4.5, 0.75, "#6e6a66"),
        (0.9, 4.5, 0.75, "#6e6a66"),
        (-1.8, 4.4, 0.7, "#88837e"),
        (1.8, 4.4, 0.7, "#88837e"),
        (-2.4, 4.3, 0.6, "#a8a39d"),
        (2.4, 4.3, 0.6, "#a8a39d"),
        (-0.5, 4.9, 0.65, "#88837e"),
        (0.5, 4.9, 0.65, "#88837e"),
    ]
    for px, py, pr, pc in puffs:
        ax.add_patch(Circle((px, py), pr, facecolor=pc, edgecolor="#44403c",
                            lw=0.5, alpha=0.9, zorder=7))

    # Text annotations and labels
    ax.text(0.0, 5.95, "Explosive eruption column (ash and gas plume)",
            fontsize=10, ha="center", va="top", fontweight="bold")

    ax.text(-3.4, 3.05,
            "High-viscosity magma\n"
            + r"($>65$% $\mathrm{SiO_2}$, silicic)" + "\n"
            "Traps volatiles (explosive)",
            fontsize=10, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="#cccccc", alpha=0.9))

    ax.annotate("Viscous plug\n(solidified dome)",
                xy=(0.3, 2.55), xytext=(1.8, 2.9),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.annotate("Trapped gas bubbles\n(pressure builds)",
                xy=(-0.15, 1.8), xytext=(-1.6, 2.0),
                fontsize=10, ha="right", va="center",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.annotate("Steep slope\n(cone-shaped)",
                xy=(-1.6, 1.0), xytext=(-3.6, 1.0),
                fontsize=10, ha="center", va="center",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.annotate("Alternating layers of\nlava and ash",
                xy=(1.1, 0.9), xytext=(2.0, 1.3),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8))

    ax.text(0.0, -0.95,
            "Earth: Mount St. Helens, Krakatoa\n"
            "(requires high silica + volatiles)",
            fontsize=10, ha="center", va="center", fontweight="bold", zorder=9,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#f0ede6",
                      edgecolor="#8c827a"))


def make_plot() -> plt.Figure:
    """Build the two-panel comparison figure.

    Returns
    -------
    matplotlib.figure.Figure
        The constructed matplotlib figure.
    """
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    draw_shield_volcano(axes[0])
    draw_stratovolcano(axes[1])
    fig.tight_layout()
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate and save the effusive vs. explosive volcanism figure."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()