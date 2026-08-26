"""Generate Fig. (`fig:central-pressure`).

Central pressure from interior models against the uniform-density
estimate P_c = 3GM^2/(8 pi R^4) for six solar-system bodies, on
log-log axes with the 1:1 line for reference. The uniform-density
values are computed here from each body's mass and radius; the
model values come from the seismology, geodesy, and gravity
constrained interior models cited per body below.

Caption / figure id : `fig:central-pressure`
Markdown source     : book/08_interiors/interiors.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/central_pressure.avif"

G = 6.674e-11   # m^3 kg^-1 s^-2

# name: (mass [kg], mean radius [m], model central pressure [GPa], source)
BODIES = {
    "Moon": (7.346e22, 1.7374e6, 5.0, "Weber et al. (2011)"),
    "Mercury": (3.301e23, 2.4397e6, 36.0, "Hauck models, Margot et al. (2018)"),
    "Mars": (6.417e23, 3.3895e6, 40.0, "InSight models, Stähler et al. (2021)"),
    "Venus": (4.867e24, 6.0518e6, 275.0, "Aitta (2012)"),
    "Earth": (5.972e24, 6.371e6, 364.0, "PREM, Dziewonski & Anderson (1981)"),
    "Jupiter": (1.898e27, 6.9911e7, 4000.0, "Juno models, Wahl et al. (2017)"),
}

# Label offsets in points, keeping the near-coincident Mercury/Mars and
# Venus/Earth pairs and the 1:1 line clear of every label
LABEL_OFFSETS = {
    "Moon": (14, -5, "left"),
    "Mercury": (16, -9, "left"),
    "Mars": (-16, 6, "right"),
    "Venus": (-16, -9, "right"),
    "Earth": (-16, 6, "right"),
    "Jupiter": (-16, 6, "right"),
}

POINT_COLOR = "#1f77b4"
LINE_COLOR = "#888888"


def uniform_central_pressure(mass: float, radius: float) -> float:
    """Return the uniform-density central pressure in GPa.

    Parameters
    ----------
    mass : float
        Body mass in kg.
    radius : float
        Body mean radius in m.

    Returns
    -------
    float
        Central pressure 3GM^2/(8 pi R^4) in GPa.
    """
    return 3.0 * G * mass**2 / (8.0 * np.pi * radius**4) / 1e9


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(5.8, 5.2))

    lo, hi = 2.0, 9000.0
    ax.plot([lo, hi], [lo, hi], "--", color=LINE_COLOR, lw=1.2, zorder=1)
    # 1:1 label in the clear region below the line, rotated to match its
    # 45-degree display slope (the axes are square in decades)
    ax.text(600, 320, "1:1", rotation=45, fontsize=10, color=LINE_COLOR,
            ha="center", va="center")

    for name, (mass, radius, p_model, _src) in BODIES.items():
        p_uni = uniform_central_pressure(mass, radius)
        # White edge keeps the near-coincident Mercury and Mars markers
        # readable as two points
        ax.plot(p_uni, p_model, "o", color=POINT_COLOR, ms=7,
                mec="white", mew=0.9, zorder=3)
        dx, dy, ha = LABEL_OFFSETS[name]
        ax.annotate(name, (p_uni, p_model), textcoords="offset points",
                    xytext=(dx, dy), fontsize=10, ha=ha, va="center",
                    zorder=4)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.set_xlabel(r"Uniform-density estimate $3GM^2/(8\pi R^4)$ [GPa]")
    ax.set_ylabel("Central pressure from interior models [GPa]")

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
