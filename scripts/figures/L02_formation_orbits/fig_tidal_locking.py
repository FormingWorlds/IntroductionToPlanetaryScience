"""Generate Fig. (`fig:tidal-locking`).

Two-panel schematic contrasting free rotation with synchronous
rotation (tidal locking). A moon on a circular orbit is drawn at four
orbital phases; a black surface marker shows which hemisphere faces
the planet. In panel (a) the spin and orbital periods differ, so the
marker points in different directions relative to the planet at each
phase. In panel (b) the two periods are equal and the marker always
faces the planet.

Caption / figure id : `fig:tidal-locking`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : (none — course-original schematic)
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "tidal_locking_inputs.json"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/tidal_locking.avif"

ORBIT_R = 1.0     # orbit radius (arbitrary units)
MOON_R = 0.13     # moon radius
PLANET_R = 0.22   # planet radius


def write_metadata() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. fig:tidal-locking: schematic contrast of free vs synchronous rotation.",
        "construction": {
            "orbital_phases_deg": [0, 90, 180, 270],
            "panel_a": "spin faster than orbit: surface marker bearing = 2x orbital phase",
            "panel_b": "synchronous: surface marker always points at the planet",
        },
        "license_note": "Course-original schematic; no external data.",
    }, indent=2))


def draw_panel(ax, synchronous: bool) -> None:
    ax.set_aspect("equal")
    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(ORBIT_R * np.cos(theta), ORBIT_R * np.sin(theta),
            linestyle="--", color="#999999", lw=0.9, zorder=1)

    planet = mpatches.Circle((0, 0), PLANET_R, facecolor="#1f77b4",
                             edgecolor="black", lw=1.0, zorder=3)
    ax.add_patch(planet)
    ax.text(0, 0, "P", color="white", ha="center", va="center",
            fontsize=12, fontweight="bold", zorder=4)

    for phase_deg in (0, 90, 180, 270):
        phi = np.radians(phase_deg)
        cx, cy = ORBIT_R * np.cos(phi), ORBIT_R * np.sin(phi)
        moon = mpatches.Circle((cx, cy), MOON_R, facecolor="#d9d9d9",
                               edgecolor="black", lw=1.0, zorder=3)
        ax.add_patch(moon)
        # Surface marker: synchronous -> always faces the planet;
        # free rotation -> spin advances twice per orbit here.
        bearing = phi + np.pi if synchronous else 2.0 * phi + np.pi
        mx = cx + MOON_R * np.cos(bearing)
        my = cy + MOON_R * np.sin(bearing)
        ax.plot(mx, my, "o", color="black", markersize=5, zorder=5)
        # Body-fixed spin axis indicator (red arrow) on the free-rotation
        # panel only, where it visibly decouples from the orbit.
        if not synchronous:
            ax.annotate("", xy=(cx + 1.9 * MOON_R * np.cos(bearing),
                                cy + 1.9 * MOON_R * np.sin(bearing)),
                        xytext=(cx, cy),
                        arrowprops=dict(arrowstyle="->", color="#d62728",
                                        lw=1.2), zorder=4)

    ax.annotate("orbital\nmotion", xy=(0.32, ORBIT_R + 0.16),
                fontsize=9, color="#666666", ha="center")
    ax.annotate("", xy=(0.24, ORBIT_R + 0.04), xytext=(-0.06, ORBIT_R + 0.04),
                arrowprops=dict(arrowstyle="->", color="#666666", lw=1.2))

    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.5, 1.65)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    title = (r"(b) Synchronous rotation: $P_{\mathrm{spin}} = P_{\mathrm{orb}}$"
             if synchronous else
             r"(a) Free rotation: $P_{\mathrm{spin}} \neq P_{\mathrm{orb}}$")
    ax.set_title(title, fontsize=11)


def make_plot() -> Path:
    apply_style()
    write_metadata()

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(9.6, 5.2))
    draw_panel(ax_a, synchronous=False)
    draw_panel(ax_b, synchronous=True)
    fig.text(0.5, 0.015,
             "Red arrow: body-fixed axis of moon. Black dot: marker on the "
             "moon's surface. P: planet (blue).",
             ha="center", fontsize=9, color="#555555")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
