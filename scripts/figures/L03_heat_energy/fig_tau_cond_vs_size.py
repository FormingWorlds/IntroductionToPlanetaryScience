"""Generate Fig. (`fig:tau-cond-vs-size`).

Conductive cooling timescale tau_cond = L^2 / kappa as a function of
body lengthscale, with horizontal reference lines at the age of the
solar system and the age of the universe, plus markers for the Moon,
Mars, Earth, an asteroid, and a chondrule.

Caption / figure id : `fig:tau-cond-vs-size`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : (none — derived from physical constants)

Inputs (silicate rock):
  kappa = 1e-6 m^2/s   (canonical thermal diffusivity)
  L = body radius, m
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/tau_cond_vs_size.avif"

KAPPA = 1.0e-6  # m^2/s, silicate
SECONDS_PER_YR = 365.25 * 24 * 3600.0

# Reference bodies: name, radius (m)
BODIES = [
    ("Chondrule",  0.5e-3),
    ("Asteroid (1 km)", 1.0e3),
    ("Moon",       1737.4e3),
    ("Mars",       3389.5e3),
    ("Earth",      6371.0e3),
]


def make_plot() -> Path:
    apply_style()

    L = np.logspace(-4, 7.2, 400)  # 0.1 mm to ~16,000 km
    tau_yr = (L ** 2) / KAPPA / SECONDS_PER_YR

    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    ax.plot(L, tau_yr, color="#1f77b4", lw=2.0,
            label=r"$\tau_{\rm cond} = L^2/\kappa$  ($\kappa = 10^{-6}\ {\rm m}^2{\rm s}^{-1}$)")

    ax.axhline(4.567e9, color="#d62728", lw=1.0, linestyle="--",
               label="Age of the Solar System (4.57 Gyr)")
    ax.axhline(13.8e9, color="black", lw=1.0, linestyle=":",
               label="Age of the universe (13.8 Gyr)")

    offsets = {
        "Chondrule": (25, 5),          # a bit higher
        "Asteroid (1 km)": (25, -5),   # as well
        "Moon": (-45, 5),              # to the left
        "Mars": (15, -5),              # right bottom, but higher to clear lines
        "Earth": (10, 15),             # right top
    }

    for name, R in BODIES:
        y = (R ** 2) / KAPPA / SECONDS_PER_YR
        ax.plot(R, y, "o", color="#ff7f0e", markeredgecolor="black", markersize=8, zorder=5)
        
        ha = "left" if offsets[name][0] > 0 else "right"
        va = "bottom" if offsets[name][1] > 0 else "top"
        
        ax.annotate(
            name, (R, y),
            xytext=offsets[name], textcoords="offset points",
            fontsize=9, ha=ha, va=va,
            arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6, shrinkA=0, shrinkB=4)
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Body length scale $L$ (m)")
    ax.set_ylabel(r"Conductive cooling timescale $\tau_{\rm cond}$ (yr)")
    ax.set_xlim(1e-4, 1e8)
    ax.set_ylim(1e-9, 1e16)
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=False, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80, keep_png=True)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
