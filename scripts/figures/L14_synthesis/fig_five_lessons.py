"""Generate Fig. (`fig:five-lessons`).

Five-panel infographic schematic illustrating the five key synthesis lessons
from the course wrap-up (book/14_synthesis/synthesis.md:662-668):
(a) Planet formation: physical process governed by accretion, gravity, and
    disk dynamics (synthesis.md:664).
(b) Planetary interiors: heat engines driving dynamos, outgassing, and
    tectonics (synthesis.md:665).
(c) Atmospheres: dynamic evolving systems with outgassing and escape,
    showing no default atmosphere exists (synthesis.md:666).
(d) Habitability: coupled systems property linking star, atmosphere,
    surface, and interior (synthesis.md:667).
(e) The solar system: detailed reference case compared to statistical
    context from exoplanet populations (synthesis.md:668).

Caption / figure id : `fig:five-lessons`
Markdown source     : book/14_synthesis/synthesis.md (lines 662-668)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/14_synthesis/figures/five_lessons.avif"


def panel_a(ax: plt.Axes) -> None:
    """Draw schematic of planet formation in a circumstellar disk.

    Illustrates accretion and gravity in a protoplanetary disk as described
    in synthesis.md:664.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axes on which to draw the schematic.

    Returns
    -------
    None
    """
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(a) Planet formation", fontsize=11, fontweight="bold", pad=8)

    # Protoplanetary disk outer, gap, and inner regions
    ax.add_patch(Ellipse((0, 0), 2.0, 0.75, facecolor="#f3e9db",
                         edgecolor="#c49c6d", lw=1.2, alpha=0.5, zorder=1))
    ax.add_patch(Ellipse((0, 0), 1.4, 0.52, facecolor="white",
                         edgecolor="#d9c2a7", linestyle="--", lw=1.2, zorder=2))
    ax.add_patch(Ellipse((0, 0), 0.8, 0.30, facecolor="#e8d5b7",
                         edgecolor="#c49c6d", lw=1.2, alpha=0.7, zorder=3))

    # Central protostar
    ax.add_patch(Circle((0, 0), 0.16, facecolor="#fdb813",
                        edgecolor="#e68a00", lw=1.5, zorder=4))
    ax.text(0, 0, "Star", fontsize=10, ha="center", va="center",
            weight="bold", color="#734100", zorder=5,
            bbox=dict(facecolor="#fdb813", edgecolor="none", pad=1, alpha=0.9))

    # Growing protoplanet with accretion arrows
    ax.add_patch(Circle((0.55, 0.12), 0.065, facecolor="#1f77b4",
                        edgecolor="#0b4572", lw=1.2, zorder=5))
    ax.add_patch(FancyArrowPatch((0.40, 0.28), (0.50, 0.17),
                                 arrowstyle="->", mutation_scale=10,
                                 color="#d95f02", lw=1.4, zorder=6))
    ax.add_patch(FancyArrowPatch((0.68, -0.02), (0.59, 0.08),
                                 arrowstyle="->", mutation_scale=10,
                                 color="#d95f02", lw=1.4, zorder=6))

    # Feature annotations
    ax.text(0.55, 0.46, "Growing\nprotoplanet", fontsize=10,
            ha="center", va="bottom", weight="bold", color="#0b4572", zorder=6,
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=0.9))
    ax.text(0.26, 0.30, "Accretion", fontsize=10, ha="right", va="center",
            color="#d95f02", weight="bold",
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=0.9))
    ax.text(0.0, -0.55, "Protoplanetary disk", fontsize=10, ha="center",
            va="top", color="#5c4a32",
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=0.9))
    ax.text(0.0, -0.90, "Accretion and disk\n(schematic)", fontsize=10,
            ha="center", va="center", color="0.3", style="italic")


def panel_b(ax: plt.Axes) -> None:
    """Draw schematic of layered planetary interior as a heat engine.

    Illustrates core dynamo and convective heat flux as described
    in synthesis.md:665.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axes on which to draw the schematic.

    Returns
    -------
    None
    """
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(b) Planetary interiors", fontsize=11, fontweight="bold", pad=8)

    # Concentric interior layers: mantle, outer core, inner core
    ax.add_patch(Circle((0, 0), 0.72, facecolor="#dfc27d",
                        edgecolor="#333333", lw=1.5, zorder=1))
    ax.add_patch(Circle((0, 0), 0.38, facecolor="#d73027",
                        edgecolor="#7f0000", lw=1.2, zorder=2))
    ax.add_patch(Circle((0, 0), 0.18, facecolor="#fee08b",
                        edgecolor="#d73027", lw=1.0, zorder=3))

    # Heat flux arrows radiating upward through mantle to surface
    ax.add_patch(FancyArrowPatch((-0.25, 0.25), (-0.46, 0.46),
                                 arrowstyle="->", mutation_scale=11,
                                 color="#b22222", lw=1.8, zorder=4))
    ax.add_patch(FancyArrowPatch((0.0, 0.38), (0.0, 0.64),
                                 arrowstyle="->", mutation_scale=11,
                                 color="#b22222", lw=1.8, zorder=4))
    ax.add_patch(FancyArrowPatch((0.25, 0.25), (0.46, 0.46),
                                 arrowstyle="->", mutation_scale=11,
                                 color="#b22222", lw=1.8, zorder=4))

    # Layer and heat engine labels
    ax.text(0.0, -0.16, "Core\n(dynamo)", fontsize=10, ha="center",
            va="center", color="#7f0000", weight="bold", zorder=5,
            bbox=dict(facecolor="#fee08b", edgecolor="none", pad=1, alpha=1.0))
    ax.text(0.0, -0.52, "Mantle", fontsize=10, ha="center", va="center",
            color="#5c4a32", weight="bold", zorder=5,
            bbox=dict(facecolor="#dfc27d", edgecolor="none", pad=1, alpha=0.9))
    ax.text(0.0, 0.82, "Heat flux", fontsize=10, ha="center", va="bottom",
            color="#b22222", weight="bold", zorder=5)
    ax.text(0.0, -0.90, "Internal heat engine\n(schematic)", fontsize=10,
            ha="center", va="center", color="0.3", style="italic")


def panel_c(ax: plt.Axes) -> None:
    """Draw schematic of dynamic atmosphere with outgassing and escape.

    Illustrates atmospheric interactions with surface, interior, and space
    as described in synthesis.md:666.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axes on which to draw the schematic.

    Returns
    -------
    None
    """
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(c) Atmospheres", fontsize=11, fontweight="bold", pad=8)

    # Vertical layers: surface/interior, atmosphere, space
    ax.add_patch(Rectangle((-0.90, -0.65), 1.80, 0.30, facecolor="#a67c52",
                           edgecolor="#5c4a32", lw=1.2, zorder=1))
    ax.text(0.0, -0.50, "Interior / Surface", fontsize=10, ha="center",
            va="center", color="white", weight="bold", zorder=3,
            bbox=dict(facecolor="#a67c52", edgecolor="none", pad=1, alpha=0.9))

    ax.add_patch(Rectangle((-0.90, -0.35), 1.80, 0.70, facecolor="#cfe5ff",
                           edgecolor="#5b9bd5", lw=1.2, alpha=0.8, zorder=1))
    ax.text(0.12, 0.0, "Atmosphere", fontsize=10, ha="center",
            va="center", color="#1c4e80", weight="bold", zorder=3,
            bbox=dict(facecolor="#cfe5ff", edgecolor="none", pad=1, alpha=0.9))

    ax.add_patch(Rectangle((-0.90, 0.35), 1.80, 0.35, facecolor="#2b2b2b",
                           edgecolor="#2b2b2b", lw=1.2, zorder=1))
    ax.text(0.0, 0.52, "Space", fontsize=10, ha="center", va="center",
            color="white", weight="bold", zorder=3,
            bbox=dict(facecolor="#2b2b2b", edgecolor="none", pad=1, alpha=0.9))

    # Outgassing and escape arrows
    ax.add_patch(FancyArrowPatch((-0.62, -0.35), (-0.62, 0.10),
                                 arrowstyle="->", mutation_scale=12,
                                 color="#d95f02", lw=2.0, zorder=4))
    ax.text(-0.62, -0.15, "Outgassing", fontsize=10, ha="center",
            va="center", color="#d95f02", weight="bold", zorder=5,
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=1.0))

    ax.add_patch(FancyArrowPatch((0.62, 0.15), (0.62, 0.55),
                                 arrowstyle="->", mutation_scale=12,
                                 color="#b22222", lw=2.0, zorder=4))
    ax.text(0.62, 0.35, "Escape", fontsize=10, ha="center", va="center",
            color="#b22222", weight="bold", zorder=5,
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=1.0))

    ax.text(0.0, -0.90, "Evolution and escape\n(schematic)", fontsize=10,
            ha="center", va="center", color="0.3", style="italic")


def panel_d(ax: plt.Axes) -> None:
    """Draw schematic loop of coupled habitability components.

    Illustrates coupling among star, atmosphere, surface, and interior
    as described in synthesis.md:667.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axes on which to draw the schematic.

    Returns
    -------
    None
    """
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(d) Habitability", fontsize=11, fontweight="bold", pad=8)

    # Curved coupling arrows connecting adjacent components in a closed loop
    ax.add_patch(FancyArrowPatch((0.22, 0.46), (0.50, 0.18),
                                 arrowstyle="<->", connectionstyle="arc3,rad=0.2",
                                 mutation_scale=10, color="#1f6db8", lw=1.5, zorder=2))
    ax.add_patch(FancyArrowPatch((0.50, -0.18), (0.22, -0.46),
                                 arrowstyle="<->", connectionstyle="arc3,rad=0.2",
                                 mutation_scale=10, color="#1f6db8", lw=1.5, zorder=2))
    ax.add_patch(FancyArrowPatch((-0.22, -0.46), (-0.50, -0.18),
                                 arrowstyle="<->", connectionstyle="arc3,rad=0.2",
                                 mutation_scale=10, color="#1f6db8", lw=1.5, zorder=2))
    ax.add_patch(FancyArrowPatch((-0.50, 0.18), (-0.22, 0.46),
                                 arrowstyle="<->", connectionstyle="arc3,rad=0.2",
                                 mutation_scale=10, color="#1f6db8", lw=1.5, zorder=2))

    # Center label and component nodes
    ax.text(0.0, 0.54, "Star", fontsize=10, ha="center", va="center",
            weight="bold", color="#734100",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff3cd",
                      edgecolor="#fdb813", lw=1.2, alpha=0.9), zorder=4)
    ax.text(0.62, 0.0, "Atmosphere", fontsize=10, ha="center", va="center",
            weight="bold", color="#0c5460",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#d1ecf1",
                      edgecolor="#17a2b8", lw=1.2, alpha=0.9), zorder=4)
    ax.text(0.0, -0.54, "Surface", fontsize=10, ha="center", va="center",
            weight="bold", color="#155724",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#d4edda",
                      edgecolor="#28a745", lw=1.2, alpha=0.9), zorder=4)
    ax.text(-0.62, 0.0, "Interior", fontsize=10, ha="center", va="center",
            weight="bold", color="#721c24",
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#f8d7da",
                      edgecolor="#dc3545", lw=1.2, alpha=0.9), zorder=4)

    ax.text(0.0, -0.90, "Coupled habitability\n(schematic)", fontsize=10,
            ha="center", va="center", color="0.3", style="italic")


def panel_e(ax: plt.Axes) -> None:
    """Draw schematic comparing solar system reference to exoplanet context.

    Illustrates solar system detail next to statistical population scatter
    as described in synthesis.md:668.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Subplot axes on which to draw the schematic.

    Returns
    -------
    None
    """
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("(e) The solar system", fontsize=11, fontweight="bold", pad=8)

    # Dividing separator between reference case and population scatter
    ax.plot([0.0, 0.0], [-0.75, 0.75], color="0.7", linestyle=":", lw=1.0)

    # Left side: Solar system reference case
    ax.text(-0.55, 0.65, "Solar system", fontsize=10, ha="center",
            va="center", weight="bold", color="#1c4e80")
    ax.text(-0.55, 0.45, "Reference case", fontsize=10, ha="center",
            va="center", color="0.4")

    ax.add_patch(Circle((-0.95, -0.05), 0.10, facecolor="#fdb813",
                        edgecolor="#e68a00", lw=1.2, zorder=2))
    for r in (0.25, 0.45, 0.70):
        arc = Arc((-0.95, -0.05), 2 * r, 2 * r, angle=0,
                  theta1=-45, theta2=45, color="0.6", linestyle="--", lw=0.9)
        ax.add_patch(arc)

    ax.add_patch(Circle((-0.50, -0.05), 0.035, facecolor="#1f77b4",
                        edgecolor="#0b4572", lw=1.0, zorder=3))
    ax.add_patch(Circle((-0.25, -0.05), 0.055, facecolor="#d95f02",
                        edgecolor="#7f2704", lw=1.0, zorder=3))

    ax.text(-0.55, -0.55, "Detailed\nin situ", fontsize=10, ha="center",
            va="center", color="#1c4e80",
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=0.9))

    # Right side: Exoplanet statistical population
    ax.text(0.55, 0.65, "Exoplanets", fontsize=10, ha="center",
            va="center", weight="bold", color="#7f2704")
    ax.text(0.55, 0.45, "Statistical context", fontsize=10, ha="center",
            va="center", color="0.4")

    rng = np.random.default_rng(42)
    x_sc = rng.uniform(0.18, 0.92, 28)
    y_sc = rng.uniform(-0.35, 0.25, 28)
    ax.scatter(x_sc, y_sc, s=18, color="#8c564b", alpha=0.6, zorder=2)

    ax.text(0.55, -0.55, "Population\nstatistics", fontsize=10, ha="center",
            va="center", color="#7f2704",
            bbox=dict(facecolor="white", edgecolor="none", pad=1, alpha=0.9))

    ax.text(0.0, -0.90, "Reference vs typical\n(schematic)", fontsize=10,
            ha="center", va="center", color="0.3", style="italic")


def make_plot() -> Path:
    """Generate the five-panel synthesis infographic and save to AVIF.

    Returns
    -------
    pathlib.Path
        Path to the generated AVIF image file.
    """
    apply_style()
    fig, axes = plt.subplots(1, 5, figsize=(14.0, 3.8))
    panel_a(axes[0])
    panel_b(axes[1])
    panel_c(axes[2])
    panel_d(axes[3])
    panel_e(axes[4])
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Build the figure and print the output file path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()