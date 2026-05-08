"""Generate Fig. (`fig:tidal-resonance`).

Two-panel schematic of the Io-Europa-Ganymede Laplace resonance.

(a) Schematic view of the three Galilean moons orbiting Jupiter
    (not to scale); mean-motion frequencies stand in 4:2:1 ratio.
(b) Bar chart of the corresponding orbital periods (1.77, 3.55,
    7.15 Earth days) showing the 1:2:4 commensurability.

Caption / figure id : `fig:tidal-resonance`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Hussmann2006

Orbital periods from NASA/JPL Solar System Dynamics.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/tidal_resonance.avif"

# Orbital periods (Earth days) from NASA/JPL
MOON_PERIODS = [
    ("Io",       1.77, "#e6a64a"),
    ("Europa",   3.55, "#5b6daa"),
    ("Ganymede", 7.15, "#5b3a8c"),
]
# Schematic semi-major-axis spacing for panel (a)
ORBIT_RADII = [0.5, 0.95, 1.5]


def panel_a(ax) -> None:
    # Jupiter at origin
    ax.add_patch(Circle((0, 0), 0.18, color="#c08555",
                        ec="black", lw=0.6, zorder=5))
    ax.text(0, 0, "J", color="white", fontsize=14, weight="bold",
            ha="center", va="center", zorder=6)

    # Orbits and moons (placed at conjunction at t=0 for illustration: Io
    # at +x, Europa at +y direction from periapsis line, Ganymede at -y)
    moon_angles_deg = [0, -10, 80]  # arbitrary positions for visual
    for (name, _, color), R, theta in zip(MOON_PERIODS, ORBIT_RADII,
                                            moon_angles_deg):
        # Orbit circle
        ax.add_patch(Circle((0, 0), R, fill=False, edgecolor=color,
                            lw=1.0, alpha=0.5))
        # Moon
        x = R * np.cos(np.radians(theta))
        y = R * np.sin(np.radians(theta))
        ax.add_patch(Circle((x, y), 0.07, color=color, ec="black",
                            lw=0.6, zorder=5))
        ax.text(x + 0.1, y + 0.05, name, fontsize=11, va="center")

    ax.set_xlim(-1.7, 1.9)
    ax.set_ylim(-1.7, 1.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Laplace resonance (Io-Europa-Ganymede)", fontsize=11,
                 weight="bold", loc="left")
    ax.text(0.0, 1.7, "(a) Orbital configuration (not to scale)",
            ha="center", fontsize=10, color="0.4")
    ax.text(0.0, -1.6,
            r"Mean-motion commensurability:  $n_{\rm Io} : n_{\rm Eur} : n_{\rm Gan} = 4 : 2 : 1$",
            ha="center", fontsize=10, color="0.2")


def panel_b(ax) -> None:
    names = [m[0] for m in MOON_PERIODS]
    periods = [m[1] for m in MOON_PERIODS]
    colors = [m[2] for m in MOON_PERIODS]

    y = np.arange(len(MOON_PERIODS))
    ax.barh(y, periods, color=colors, edgecolor="black", lw=0.5)
    for yi, p in zip(y, periods):
        ax.text(p + 0.15, yi, f"{p:.2f} d", va="center", fontsize=11)

    ax.set_yticks(y)
    ax.set_yticklabels(names)
    ax.set_xlabel("Orbital period (Earth days)")
    ax.set_xlim(0, 9)
    ax.set_title("(b) Orbital periods: 1:2:4 commensurability", fontsize=11)
    ax.grid(axis="x", linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5),
                              gridspec_kw={"width_ratios": [1.0, 1.4]})
    panel_a(axes[0])
    panel_b(axes[1])
    fig.suptitle("Tidal resonance geometry sustaining icy-moon oceans",
                 fontsize=12, y=1.0)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
