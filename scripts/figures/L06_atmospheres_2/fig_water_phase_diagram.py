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

# Ice Ih / ice III / liquid triple point: the high-pressure end of the ice Ih
# field, where the melting curve turns and higher-pressure ice phases begin.
T_IH_END = 251.165  # K
P_IH_END = 208.566e6  # Pa


def cc_curve(T: np.ndarray, T_anchor: float, P_anchor: float, L: float) -> np.ndarray:
    return P_anchor * np.exp(-(L / R_V) * (1.0 / T - 1.0 / T_anchor))


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 6.0))

    # Liquid-vapour (vaporisation): triple point to critical point.
    T_lv = np.linspace(T_TP, T_CRIT, 400)
    P_lv = cc_curve(T_lv, T_TP, P_TP, L_VAP)
    ax.plot(T_lv, P_lv, color="#1f77b4", lw=2.0,
            label="Vaporisation (liquid-vapour)")

    # Solid-vapour (sublimation): low temperature up to the triple point.
    T_sv = np.linspace(180.0, T_TP, 400)
    P_sv = cc_curve(T_sv, T_TP, P_TP, L_SUB)
    ax.plot(T_sv, P_sv, color="#2bbcd6", lw=2.0,
            label="Sublimation (solid-vapour)")

    # Solid-liquid (melting): Clapeyron slope dP/dT = L_fus / (T DV).
    # Invert to T(P) = T_TP exp((P - P_TP) DV / L_fus) and sample in
    # pressure, so the near-vertical curve is anchored exactly at the
    # triple point and stays well resolved along its steep length.
    # DV_FUSION is the ice Ih value, so the curve stops where that field
    # ends; past it the slope reverses and the curve would be wrong.
    P_sl = np.logspace(np.log10(P_TP), np.log10(P_IH_END), 400)
    T_sl = T_TP * np.exp((P_sl - P_TP) * DV_FUSION / L_FUS)
    ax.plot(T_sl, P_sl, color="black", lw=2.0,
            label="Melting (solid-liquid, ice Ih)")
    ax.plot(T_sl[-1], P_sl[-1], "o", color="black", ms=6, mfc="white",
            mew=1.2, zorder=5)
    ax.annotate("Ice Ih field ends near 0.2 GPa;\nhigh-pressure ice phases\nnot shown",
                xy=(T_sl[-1], P_sl[-1]), xytext=(283, 7.5e8),
                fontsize=8.5, color="0.35", ha="left", va="top",
                arrowprops=dict(arrowstyle="-", color="0.5", lw=0.6))

    # Triple point
    ax.plot(T_TP, P_TP, "o", color="black", ms=8, zorder=5)
    ax.annotate(f"Triple point\n({T_TP:.2f} K, {P_TP:.1f} Pa)",
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
