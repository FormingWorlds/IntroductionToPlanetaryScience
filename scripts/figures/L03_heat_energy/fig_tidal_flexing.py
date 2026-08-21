"""Generate Fig. (`fig:tidal-flexing`).

Schematic of tidal heating from orbital eccentricity. Two panels show
a moon (Io) at periapsis (close to planet, large tidal bulge) and at
apoapsis (far from planet, small bulge); the cyclic flexing
dissipates orbital energy as heat at a rate proportional to e^2 / Q.

Caption / figure id : `fig:tidal-flexing`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : (textbook schematic; cited as Peale1979 in body)

Geometry deliberately exaggerated for clarity. Pure schematic.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/tidal_flexing.avif"

JUPITER = "#e6a64a"
MOON = "#9aa0c7"
DASH = "#9b9b9b"


def draw_orbit(ax, a: float, e: float, flip: bool = False, center=(0.0, 0.0)) -> None:
    """Draw a dashed ellipse representing the orbit. The planet is
    placed at the origin (one focus); for the schematic we draw the
    ellipse centred such that periapsis distance = a(1-e) and apoapsis
    distance = a(1+e) along the x-axis."""
    theta = np.linspace(0, 2 * np.pi, 200)
    # Conic with focus at origin: r = a(1-e^2) / (1 + e cos theta)
    r = a * (1 - e ** 2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    if flip:
        x = -x
    x = x + center[0]
    y = r * np.sin(theta) + center[1]
    ax.plot(x, y, ls="--", color=DASH, lw=1.0, zorder=1)


def draw_panel(ax, mode: str) -> None:
    """mode in {'peri', 'apo'}."""
    a = 4.0
    e = 0.4  # exaggerated for visibility
    R_jup = 0.6
    R_moon = 0.32

    # Orbit (focus at origin = Jupiter centre)
    draw_orbit(ax, a, e, flip=(mode == "apo"))

    # Jupiter at origin
    ax.add_patch(Circle((0, 0), R_jup, color=JUPITER, ec="black", lw=0.6, zorder=3))
    ax.text(0, -R_jup - 0.25, "Jupiter", fontsize=11, ha="center",
            va="top", weight="bold")

    if mode == "peri":
        ax.set_title("Periapsis: large tidal bulge", fontsize=12)
        r_peri = a * (1 - e)
        # Moon at periapsis on +x axis
        # Bulge (large): elongate along Jupiter-moon axis
        ax.add_patch(Ellipse((r_peri, 0), 2 * R_moon * 1.55, 2 * R_moon * 0.95,
                             color=MOON, ec="black", lw=0.6, zorder=3))
        # Label right of the moon: outside the orbit, clear of the
        # dashed ellipse that passes vertically through periapsis
        ax.text(r_peri + R_moon * 1.55 + 0.12, 0, "Io", fontsize=11,
                ha="left", va="center", weight="bold")
        # Distance arrow
        ax.add_patch(FancyArrowPatch((R_jup + 0.05, -R_jup - 1.0),
                                     (r_peri - R_moon * 1.55, -R_jup - 1.0),
                                     arrowstyle="<->", mutation_scale=12,
                                     color="black", lw=1.0))
        # Left-aligned past x = 1.95: the orbit's lower branch crosses
        # this depth band at x < 1.85
        ax.text(1.95, -R_jup - 1.35,
                r"$r=a(1-e)$", fontsize=11, ha="left", va="top")

    else:
        ax.set_title("Apoapsis: small tidal bulge", fontsize=12)
        r_apo = a * (1 + e)
        # Moon at apoapsis (smaller bulge)
        ax.add_patch(Ellipse((r_apo, 0), 2 * R_moon * 1.10, 2 * R_moon * 0.92,
                             color=MOON, ec="black", lw=0.6, zorder=3))
        # Label left of the moon, inside the orbit: the dashed ellipse
        # passes vertically through apoapsis and clears |y| < 1.8 here
        ax.text(r_apo - R_moon * 1.10 - 0.12, 0, "Io", fontsize=11,
                ha="right", va="center", weight="bold")
        ax.add_patch(FancyArrowPatch((R_jup + 0.05, -R_jup - 1.0),
                                     (r_apo - R_moon * 1.10, -R_jup - 1.0),
                                     arrowstyle="<->", mutation_scale=12,
                                     color="black", lw=1.0))
        ax.text((R_jup + r_apo) / 2, -R_jup - 1.35,
                r"$r=a(1+e)$", fontsize=11, ha="center", va="top")

    ax.set_xlim(-a * (1 + e) - 0.5, a * (1 + e) + 0.8)
    ax.set_ylim(-a - 0.6, a + 0.4)
    ax.set_aspect("equal")
    ax.axis("off")


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.0))
    draw_panel(axes[0], "peri")
    draw_panel(axes[1], "apo")
    fig.suptitle(
        r"Cyclic flexing dissipates orbital energy as heat: "
        r"$\dot E_\mathrm{tidal} \propto e^2/Q$",
        y=0.97, fontsize=12, color="#d62728")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
