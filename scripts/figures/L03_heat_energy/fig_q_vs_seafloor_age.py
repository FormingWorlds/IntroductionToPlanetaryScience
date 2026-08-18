"""Generate Fig. (`fig:q-vs-age`).

Surface heat flux q as a function of seafloor age. The half-space cooling
model predicts

    q(t) = k (T_m - T_s) / sqrt(pi * kappa * t)  ~  t^{-1/2}

and is compared against the corrected, hydrothermally filtered global
compilation of oceanic heat-flow measurements binned in 2.5 Myr age
windows by Richards et al. (2018), data/richards2018_heatflow_binned_global.csv.

Caption / figure id : `fig:q-vs-age`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation keys       : SteinStein1992 (plate-cooling asymptote ~48 mW/m^2),
                      Richards2018 (binned heat-flow data)

Defaults: k = 3.3 W/m/K, T_m - T_s = 1327 K, kappa = 1e-6 m^2/s.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/q_vs_seafloor_age.avif"
DATA_CSV = Path(__file__).resolve().parent / "data/richards2018_heatflow_binned_global.csv"

K_TH = 3.3            # W/m/K
DELTA_T = 1327.0      # K (T_m - T_s)
KAPPA = 1.0e-6        # m^2/s
SEC_PER_YR = 365.25 * 24 * 3600
Q_PLATE_ASYMPTOTE = 48.0  # mW/m^2 (Stein & Stein 1992)


def load_data() -> np.ndarray:
    """Load the binned heat-flow compilation (age_myr, n, mean, median, lq, uq)."""
    return np.genfromtxt(DATA_CSV, delimiter=",", names=True, skip_header=4)


def make_plot() -> Path:
    apply_style()
    t_Myr = np.logspace(-0.31, np.log10(200), 400)
    t_s = t_Myr * 1e6 * SEC_PER_YR
    q_W = K_TH * DELTA_T / np.sqrt(np.pi * KAPPA * t_s)
    q_mW = q_W * 1000.0

    data = load_data()
    in_range = data["age_myr"] <= 200.0
    multi = data[in_range & (data["n_points"] > 1)]
    single = data[in_range & (data["n_points"] == 1)]

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.plot(t_Myr, q_mW, color="#1f77b4", lw=2.0, zorder=3,
            label=r"Half-space: $q \propto t^{-1/2}$")
    ax.axhline(Q_PLATE_ASYMPTOTE, color="#d62728", lw=1.0, linestyle="--",
               label=f"Plate-cooling asymptote (~{Q_PLATE_ASYMPTOTE:.0f} mW m$^{{-2}}$)")

    yerr = np.vstack([multi["q_median_mw_m2"] - multi["q_lq_mw_m2"],
                      multi["q_uq_mw_m2"] - multi["q_median_mw_m2"]])
    ax.errorbar(multi["age_myr"], multi["q_median_mw_m2"], yerr=yerr,
                fmt="o", ms=4, color="#555555", ecolor="#aaaaaa",
                elinewidth=1.0, capsize=0, zorder=2,
                label="Measured, 2.5 Myr bins (median, interquartile range)")
    ax.plot(single["age_myr"], single["q_median_mw_m2"], "o", ms=5,
            mfc="none", mec="#555555", mew=1.2, zorder=2,
            label="Bins with a single measurement")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Seafloor age (Myr)")
    ax.set_ylabel(r"Surface heat flux $q$ (mW m$^{-2}$)")
    ax.set_xlim(0.5, 200)
    ax.set_ylim(20, 1000)
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=False, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
