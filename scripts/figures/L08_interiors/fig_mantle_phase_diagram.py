"""Generate Fig. (`fig:mantle-phase-diagram`).

Schematic pressure-temperature phase diagram of the Earth's mantle
in the olivine-bearing system. Major boundaries:

- olivine (alpha-Mg2SiO4) -> wadsleyite (beta) at ~14 GPa (410 km)
- wadsleyite -> ringwoodite (gamma) at ~18 GPa (520 km)
- ringwoodite -> bridgmanite + ferropericlase at ~24 GPa (660 km),
  with NEGATIVE Clapeyron slope
- bridgmanite -> post-perovskite at ~125 GPa (D" layer, ~2700 km),
  with POSITIVE Clapeyron slope

Caption / figure id : `fig:mantle-phase-diagram`
Markdown source     : book/08_interiors/interiors.md
Citation keys       : Turcotte2002, Murakami2004
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/mantle_phase_diagram.avif"

# Phase boundary anchor points (T_K, P_GPa) and Clapeyron slopes (MPa/K)
BOUNDARIES = [
    {"name": "Olivine -> Wadsleyite",
     "T0": 1750.0, "P0": 14.0, "slope_MPa_K": +2.5,
     "depth_label": "410 km"},
    {"name": "Wadsleyite -> Ringwoodite",
     "T0": 1900.0, "P0": 18.0, "slope_MPa_K": +4.0,
     "depth_label": "520 km"},
    {"name": "Ringwoodite -> Bridgmanite + Ferropericlase",
     "T0": 1900.0, "P0": 24.0, "slope_MPa_K": -2.5,
     "depth_label": "660 km"},
    {"name": "Bridgmanite -> Post-perovskite",
     "T0": 2500.0, "P0": 125.0, "slope_MPa_K": +8.0,
     "depth_label": "D\" ($\\sim$2700 km)"},
]

# Approximate adiabatic geotherm anchor points (T_K, P_GPa)
GEOTHERM_T = np.array([1500, 1700, 1900, 2400, 2800, 3500, 4000])
GEOTHERM_P = np.array([0,    14,   24,   60,   100,  130,  135])


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 7.0))

    T = np.linspace(1000, 4500, 400)
    for b in BOUNDARIES:
        # Clapeyron line: P(T) = P0 + (slope / 1000) * (T - T0); slope MPa/K -> GPa/K
        P_line = b["P0"] + (b["slope_MPa_K"] / 1000.0) * (T - b["T0"])
        ax.plot(T, P_line, color="black", lw=1.4)
        # Right-side depth label
        ax.text(T[-1] + 30, P_line[-1], b["depth_label"], color="0.4",
                fontsize=9, va="center")

    # Geotherm
    ax.plot(GEOTHERM_T, GEOTHERM_P, color="#d62728", lw=2.0, linestyle="--",
            label="Earth mantle geotherm")

    # Phase region labels
    ax.text(1100, 4, r"Olivine ($\alpha$-Mg$_2$SiO$_4$)", fontsize=10)
    ax.text(1100, 16, r"Wadsleyite ($\beta$)", fontsize=10)
    ax.text(1100, 21, r"Ringwoodite ($\gamma$)", fontsize=10)
    ax.text(1500, 60, "Bridgmanite + Ferropericlase\n(perovskite-structured)",
            fontsize=10, ha="left")
    ax.text(3500, 138, "Post-perovskite (PPv)", fontsize=10, ha="center")

    ax.invert_yaxis()
    ax.set_xlim(1000, 4500)
    ax.set_ylim(160, 0)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Pressure (GPa)")
    ax.set_title("Mantle phase diagram: olivine system at planetary pressures")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="lower left", frameon=False, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
