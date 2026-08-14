"""Generate Fig. (`fig:water-phase-diagram`).

Phase diagram of water in P-T space:
- liquid-vapour coexistence: integrated Clausius-Clapeyron with
  L_vap = 2.289e6 J/kg (effective constant value: the integrated
  curve then passes through both the triple point and the critical
  point; the true L falls from 2.50e6 at 273 K to 0 at T_crit)
- solid-vapour (sublimation): integrated Clausius-Clapeyron with
  L_sub = 2.83e6 J/kg
- solid-liquid: anomalously negative slope, dP/dT = L_fus / (T DV)
  with L_fus = 3.34e5 J/kg, DV = -9e-5 m^3/kg (ice less dense than
  liquid)
The triple point at (273.16 K, 611 Pa) is anchor for all three.

Caption / figure id : `fig:water-phase-diagram`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/water_phase_diagram.avif"

R_V = 461.5      # J/kg/K specific gas constant of water vapour
L_VAP = 2.289e6  # J/kg, effective: pins the constant-L curve to both anchors
L_SUB = 2.83e6   # J/kg
L_FUS = 3.34e5   # J/kg
DV_FUSION = -9.05e-5  # m^3/kg (V_liquid - V_solid; negative because ice less dense)

T_TP = 273.16    # K
P_TP = 611.657   # Pa
T_CRIT = 647.0   # K
P_CRIT = 22.064e6  # Pa


def cc_curve(T: np.ndarray, T_anchor: float, P_anchor: float, L: float) -> np.ndarray:
    return P_anchor * np.exp(-(L / R_V) * (1.0 / T - 1.0 / T_anchor))


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 6.0))

    # Liquid-vapour: T from triple point to critical
    T_lv = np.linspace(T_TP, T_CRIT, 400)
    P_lv = cc_curve(T_lv, T_TP, P_TP, L_VAP)
    ax.plot(T_lv, P_lv, color="#1f77b4", lw=2.0,
            label="Liquid-vapour")

    # Solid-vapour (sublimation): T from low to triple point
    T_sv = np.linspace(180.0, T_TP, 400)
    P_sv = cc_curve(T_sv, T_TP, P_TP, L_SUB)
    ax.plot(T_sv, P_sv, color="#2bbcd6", lw=2.0,
            label="Solid-vapour (sublimation)")

    # Solid-liquid: dP/dT = L_fus / (T * DV); integrate from triple point
    # P_sl(T) = P_TP + (L_fus / DV) * ln(T / T_TP)
    T_sl = np.linspace(T_TP - 30, T_TP + 1, 400)
    P_sl = P_TP + (L_FUS / DV_FUSION) * np.log(T_sl / T_TP)
    ok = P_sl > 1e-2
    ax.plot(T_sl[ok], P_sl[ok], color="black", lw=2.0,
            label="Solid-liquid")

    # Triple point
    ax.plot(T_TP, P_TP, "o", color="black", ms=8, zorder=5)
    ax.annotate(f"Triple point\n({T_TP:.2f} K, {P_TP:.0f} Pa)",
                xy=(T_TP, P_TP), xytext=(T_TP + 20, P_TP * 0.06),
                fontsize=10, ha="left",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    # Critical point
    ax.plot(T_CRIT, P_CRIT, "o", color="#d62728", ms=8, zorder=5)
    ax.annotate(f"Critical point\n({T_CRIT:.0f} K, {P_CRIT/1e6:.1f} MPa)",
                xy=(T_CRIT, P_CRIT), xytext=(T_CRIT - 200, P_CRIT * 1.5),
                fontsize=10, color="#d62728", ha="right",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    # Earth surface
    ax.plot(288.0, 1.013e5, "*", color="#2ca02c", ms=14,
            mec="black", mew=0.5, zorder=5,
            label="Earth surface (288 K, 1 bar)")

    # Region labels
    ax.text(220, 1e4, "ICE", color="0.5", fontsize=14, weight="bold",
            ha="center", va="center")
    ax.text(310, 1e6, "LIQUID", color="#1f4e79", fontsize=14, weight="bold",
            ha="center", va="center")
    ax.text(450, 1e3, "VAPOUR", color="#1f6b3b", fontsize=14, weight="bold",
            ha="center", va="center")

    ax.set_yscale("log")
    ax.set_xlim(170, 700)
    ax.set_ylim(1e-2, 1e9)
    ax.set_xlabel("Temperature [K]")
    ax.set_ylabel("Pressure [Pa]")
    ax.set_title("Phase diagram of water")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="lower right", frameon=True, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
