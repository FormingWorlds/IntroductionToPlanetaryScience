"""Generate Fig. (`fig:stokes-settling`).

Stokes settling velocity of an iron droplet in a low-viscosity
silicate magma ocean as a function of droplet radius:

    v_Stokes = 2 * Delta_rho * g * r^2 / (9 * mu)

with the canonical magma-ocean parameters
Delta_rho = 4000 kg/m^3, g = 5 m/s^2, mu = 0.1 Pa s
(L04 caption text and Eq. eq:stokes-settling).

Caption / figure id : `fig:stokes-settling`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Rubie2015
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/stokes_settling.avif"

DELTA_RHO = 4000.0   # kg/m^3
G = 5.0              # m/s^2 (magma-ocean midpoint gravity)
MU = 0.1             # Pa s


def v_stokes(r_m: np.ndarray) -> np.ndarray:
    return 2.0 * DELTA_RHO * G * r_m ** 2 / (9.0 * MU)


def make_plot() -> Path:
    apply_style()
    r_cm = np.logspace(-2, 2, 400)
    r_m = r_cm * 1e-2
    v = v_stokes(r_m)

    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    ax.plot(r_cm, v, color="#d62728", lw=2.0)

    # Reference points
    refs = [
        (0.1, "1 mm droplet"),
        (1.0, "1 cm droplet"),
        (10.0, "10 cm blob"),
    ]
    for rc, label in refs:
        v_pt = v_stokes(rc * 1e-2)
        ax.plot(rc, v_pt, "o", color="black", ms=5, zorder=5)
        v_str = np.format_float_positional(float(f"{v_pt:.2g}"), trim="-")
        ax.annotate(f"{label}\n({v_str} m s$^{{-1}}$)",
                    xy=(rc, v_pt), xytext=(rc * 1.6, v_pt * 0.25),
                    fontsize=9, ha="left", va="top")

    # Equation in a box
    ax.text(0.95, 0.05,
            r"$v_{\mathrm{Stokes}} = \dfrac{2}{9}\,"
            r"\dfrac{\Delta\rho\, g\, r^2}{\mu}$",
            transform=ax.transAxes, fontsize=12,
            ha="right", va="bottom",
            bbox=dict(facecolor="white", edgecolor="0.6",
                      boxstyle="round,pad=0.4"))

    # Laminar limit: Re = rho_melt * v_stokes * 2r / mu = 1 (rho_melt = 3000 kg/m3)
    r_lam_m = (9.0 * MU**2 / (4.0 * 3000.0 * DELTA_RHO * G)) ** (1.0 / 3.0)
    r_lam_cm = r_lam_m * 1e2
    ax.axvline(r_lam_cm, color="0.4", ls="--", lw=1.2)
    ax.text(r_lam_cm * 0.82, 3e-3, r"laminar limit ($\mathrm{Re} \approx 1$)",
            rotation=90, fontsize=9, color="0.35", ha="right", va="bottom")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.01, 100)
    ax.set_ylim(1e-4, 1e3)
    ax.set_xlabel("Iron droplet radius (cm)")
    ax.set_ylabel(r"Settling velocity (m s$^{-1}$)")
    ax.set_title("Stokes settling of iron droplets in a silicate magma ocean")
    ax.grid(which="both", linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
