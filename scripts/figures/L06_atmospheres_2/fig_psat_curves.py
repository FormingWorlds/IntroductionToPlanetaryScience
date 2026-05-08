"""Generate Fig. (`fig:psat-curves`).

Saturation vapour pressure P_sat(T) for the major planetary
condensables: H2O, H2SO4, NH3, CH4, and CO2 (sublimation curve),
from the integrated Clausius-Clapeyron equation

    P_sat(T) = P_ref * exp[ -L/R_s * (1/T - 1/T_ref) ]

where L is the latent heat of vaporisation (or sublimation, for CO2)
and R_s = R_universal / M is the specific gas constant of the
condensable.

Caption / figure id : `fig:psat-curves`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md

Reference values (literature):
- H2O: L_vap = 2.50e6 J/kg, T_ref = 373.15 K, P_ref = 101325 Pa
       (boiling point at 1 atm)
- H2SO4: L_vap = 7.2e5 J/kg, T_ref = 610 K, P_ref = 101325 Pa
       (boiling point at 1 atm; Pruppacher & Klett 1997)
- NH3: L_vap = 1.371e6 J/kg, T_ref = 239.7 K, P_ref = 101325 Pa
- CH4: L_vap = 5.10e5 J/kg, T_ref = 111.7 K, P_ref = 101325 Pa
- CO2: L_sub = 5.71e5 J/kg, T_ref = 194.7 K, P_ref = 101325 Pa
       (sublimation point at 1 atm)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/psat_curves.avif"

R_UNIV = 8.314  # J/mol/K

# (label, M [kg/mol], L [J/kg], T_ref [K], P_ref [Pa], color, condensation_T_band [K, K])
SPECIES = [
    (r"H$_2$O",   18.015e-3, 2.50e6, 373.15, 101325.0, "#1f77b4", (250, 320)),
    (r"H$_2$SO$_4$", 98.08e-3, 7.2e5, 610.0,  101325.0, "#d62728", (300, 420)),
    (r"NH$_3$",   17.031e-3, 1.371e6, 239.7,  101325.0, "#2ca02c", (130, 180)),
    (r"CH$_4$",   16.043e-3, 5.10e5, 111.7,  101325.0, "#ff7f0e", (90, 150)),
    (r"CO$_2$ (subl.)", 44.01e-3, 5.71e5, 194.7, 101325.0, "#9467bd", (110, 180)),
]


def psat(T: np.ndarray, M: float, L: float, T_ref: float, P_ref: float) -> np.ndarray:
    R_s = R_UNIV / M
    return P_ref * np.exp(-(L / R_s) * (1.0 / T - 1.0 / T_ref))


def make_plot() -> Path:
    apply_style()
    T = np.linspace(80, 600, 600)

    fig, ax = plt.subplots(figsize=(8.5, 5.6))
    for label, M, L, T_ref, P_ref, color, _ in SPECIES:
        ax.plot(T, psat(T, M, L, T_ref, P_ref),
                color=color, lw=1.8, label=label)

    # Ice line at 1 atm
    ax.axhline(101325.0, color="0.5", linestyle=":", lw=0.8)
    ax.text(580, 1.4e5, "1 atm", color="0.4", fontsize=9, ha="right")

    # Coloured bands at the bottom for typical condensation T ranges
    for label, M, L, T_ref, P_ref, color, band in SPECIES:
        ax.fill_betweenx([1e-5, 1e-4], band[0], band[1],
                         color=color, alpha=0.6)

    ax.set_yscale("log")
    ax.set_xlim(80, 600)
    ax.set_ylim(1e-5, 1e9)
    ax.set_xlabel(r"Temperature $T$ [K]")
    ax.set_ylabel(r"Saturation vapour pressure $P_{\mathrm{sat}}$ [Pa]")
    ax.set_title("Saturation vapour pressure curves (Clausius-Clapeyron)")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=False, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
