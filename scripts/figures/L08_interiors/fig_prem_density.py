"""Generate Fig. (`fig:prem-density`).

PREM density as a function of radius, drawn straight from the
polynomial coefficients of Dziewonski & Anderson (1981) rather than
traced off a published plot.

Each PREM branch is sampled on its own interval and the pieces are
concatenated, so every density discontinuity (the inner-core boundary,
the core-mantle boundary, the 410 and 660 km transitions, the Moho)
appears as a vertical riser instead of a smoothed ramp.

Caption / figure id : `fig:prem-density`
Markdown source     : book/08_interiors/interiors.md
Data                : PREM polynomial coefficients, Table 1 of
                      Dziewonski & Anderson (1981), via `_prem.py`
Citation key        : Dziewonski1981
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

from ._prem import LAYERS, R_EARTH, _poly

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/prem_density.avif"

R_ICB = 1221.5
R_CMB = 3480.0
R_660 = 5701.0
R_410 = 5971.0

MANTLE_FILL = "#efe9e2"
OUTER_CORE_FILL = "#f4c76a"
INNER_CORE_FILL = "#e08a3c"
CURVE = "#1f5fa8"

Y_TOP = 14200.0


def density_profile(n_per_branch: int = 400) -> tuple[np.ndarray, np.ndarray]:
    """Return radius [km] and density [kg m^-3] as one piecewise polyline.

    Returns
    -------
    r : ndarray
        Radius in km, ascending, with each branch boundary repeated so
        the polyline carries a vertical riser across a discontinuity.
    rho : ndarray
        Density in kg m^-3 at those radii.
    """
    r_parts, rho_parts = [], []
    for (r0, r1, c_rho, _, _) in LAYERS:
        r = np.linspace(r0, r1, n_per_branch)
        r_parts.append(r)
        rho_parts.append(_poly(c_rho, r / R_EARTH) * 1.0e3)
    return np.concatenate(r_parts), np.concatenate(rho_parts)


def draw_layers(ax: plt.Axes) -> None:
    """Shade the three major layers and mark their bounding radii."""
    ax.axvspan(0.0, R_ICB, color=INNER_CORE_FILL, alpha=0.55, lw=0)
    ax.axvspan(R_ICB, R_CMB, color=OUTER_CORE_FILL, alpha=0.55, lw=0)
    ax.axvspan(R_CMB, R_EARTH, color=MANTLE_FILL, alpha=0.9, lw=0)
    # Stop the lines short of the bottom so the radius labels below them
    # sit on clean fill.
    for r_b in (R_ICB, R_CMB):
        ax.vlines(r_b, 2700.0, Y_TOP, color="0.35", ls="--", lw=0.9)


def label_layers(ax: plt.Axes) -> None:
    """Name the layers and the two bounding radii, clear of the curve."""
    ax.text(0.5 * R_ICB, 6800.0, "Inner\ncore", ha="center", va="center",
            fontsize=9, color="black")
    ax.text(0.5 * (R_ICB + R_CMB), 6800.0, "Outer core", ha="center",
            va="center", fontsize=9, color="black")
    ax.text(0.5 * (R_CMB + R_EARTH), 6800.0, "Mantle", ha="center",
            va="center", fontsize=9, color="black")
    ax.text(R_ICB, 1500.0, "ICB\n1221 km", ha="center", va="center",
            fontsize=8, color="black")
    ax.text(R_CMB, 1500.0, "CMB\n3480 km", ha="center", va="center",
            fontsize=8, color="black")


def annotate_transitions(ax: plt.Axes) -> None:
    """Point at the 410 and 660 km phase-transition steps."""
    ax.annotate("410 and 660 km\ndiscontinuities",
                xy=(0.5 * (R_660 + R_410), 4050.0),
                xytext=(4550.0, 2100.0),
                ha="center", va="center", fontsize=8, color="black",
                arrowprops=dict(arrowstyle="-", color="0.35", lw=0.8,
                                shrinkA=4, shrinkB=4))


def make_plot() -> Path:
    """Render the figure and write it to `OUT_AVIF`."""
    apply_style()
    fig, ax = plt.subplots(figsize=(5.4, 4.4))

    r, rho = density_profile()
    draw_layers(ax)
    ax.plot(r, rho, color=CURVE, lw=2.0)
    label_layers(ax)
    annotate_transitions(ax)

    ax.set_xlim(0.0, R_EARTH)
    ax.set_ylim(0.0, Y_TOP)
    ax.set_xlabel("Radius (km)")
    ax.set_ylabel(r"Density (kg m$^{-3}$)")
    ax.set_xticks(np.arange(0, 6001, 1000))
    ax.set_yticks(np.arange(0, 14001, 2000))
    ax.grid(False)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80, dpi=300)


def main() -> None:
    r, rho = density_profile()
    for label, r_q in (("centre", 0.0), ("ICB, inner side", R_ICB - 1.0),
                       ("ICB, outer side", R_ICB + 1.0),
                       ("CMB, core side", R_CMB - 1.0),
                       ("CMB, mantle side", R_CMB + 1.0),
                       ("upper mantle", 6200.0)):
        print(f"  rho at {label:17s}: {np.interp(r_q, r, rho):8.0f} kg m^-3")
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
