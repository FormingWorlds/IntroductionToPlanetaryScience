"""Generate Fig. (`fig:half-space-cooling`).

Half-space cooling solution for the temperature profile beneath
oceanic lithosphere:

    T(z, t) = T_s + (T_m - T_s) * erf( z / (2 sqrt(kappa t)) )

Plotted for ages 1, 10, 50, 100, 200 Myr.

Caption / figure id : `fig:half-space-cooling`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : (none — physical solution)

Defaults: T_s = 273 K, T_m = 1600 K, kappa = 1e-6 m^2/s.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/half_space_cooling.avif"

T_S = 273.0
T_M = 1600.0
KAPPA = 1.0e-6
SEC_PER_YR = 365.25 * 24 * 3600


def make_plot() -> Path:
    apply_style()
    z_km = np.linspace(0, 150, 400)
    z = z_km * 1000.0

    fig, ax = plt.subplots(figsize=(6.5, 6.0))
    ages_Myr = [1, 10, 50, 100, 200]
    cmap = plt.cm.viridis(np.linspace(0.15, 0.9, len(ages_Myr)))

    for age, color in zip(ages_Myr, cmap):
        t_s = age * 1e6 * SEC_PER_YR
        T = T_S + (T_M - T_S) * erf(z / (2.0 * np.sqrt(KAPPA * t_s)))
        ax.plot(T, z_km, color=color, lw=2.0, label=f"{age} Myr")

    ax.axvline(T_M, color="#a83232", lw=1.0, linestyle=":",
               label=fr"$T_m = {T_M:.0f}$ K (mantle)")
    ax.axvline(T_S, color="#1f77b4", lw=1.0, linestyle=":",
               label=fr"$T_s = {T_S:.0f}$ K (seafloor)")

    ax.invert_yaxis()
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Depth (km)")
    ax.set_xlim(200, 1700)
    ax.set_ylim(150, 0)
    ax.set_title("Half-space cooling temperature profile")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="lower left", frameon=False, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
