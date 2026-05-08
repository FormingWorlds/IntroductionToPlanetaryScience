"""Generate Fig. (`fig:q-vs-age`).

Surface heat flux q as a function of seafloor age, predicted by the
half-space cooling model:

    q(t) = k (T_m - T_s) / sqrt(pi * kappa * t)  ~  t^{-1/2}

Caption / figure id : `fig:q-vs-age`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : SteinStein1992 (plate-cooling asymptote ~48 mW/m^2)

Defaults: k = 3.3 W/m/K, T_m - T_s = 1327 K, kappa = 1e-6 m^2/s.
Stein & Stein 1992 plate-cooling asymptote: ~48 mW/m^2.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/q_vs_seafloor_age.avif"

K_TH = 3.3            # W/m/K
DELTA_T = 1327.0      # K (T_m - T_s)
KAPPA = 1.0e-6        # m^2/s
SEC_PER_YR = 365.25 * 24 * 3600
Q_PLATE_ASYMPTOTE = 48.0  # mW/m^2 (Stein & Stein 1992)


def make_plot() -> Path:
    apply_style()
    t_Myr = np.logspace(-1, 3, 400)
    t_s = t_Myr * 1e6 * SEC_PER_YR
    q_W = K_TH * DELTA_T / np.sqrt(np.pi * KAPPA * t_s)
    q_mW = q_W * 1000.0

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.plot(t_Myr, q_mW, color="#1f77b4", lw=2.0,
            label=r"Half-space: $q \propto t^{-1/2}$")
    ax.axhline(Q_PLATE_ASYMPTOTE, color="#d62728", lw=1.0, linestyle="--",
               label=f"Plate-cooling asymptote (~{Q_PLATE_ASYMPTOTE:.0f} mW m$^{{-2}}$)")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Seafloor age (Myr)")
    ax.set_ylabel(r"Surface heat flux $q$ (mW m$^{-2}$)")
    ax.set_xlim(0.5, 200)
    ax.set_ylim(20, 5000)
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=False, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
