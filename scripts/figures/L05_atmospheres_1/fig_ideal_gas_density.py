"""Generate Fig. (`fig:ideal-gas-density`).

Log-log plot of atmospheric gas mass density rho = P mu m_u / (kB T)
versus pressure P from 1e-3 to 1e2 bar for compositions with mu = 2.2
(H2/He, Jupiter), 28.97 (Earth air), and 43.4 (CO2, Venus) at T = 288 K
and T = 737 K. Marked points highlight surface conditions on Earth and
Venus and the 1-bar level on Jupiter.

Caption / figure id : `fig:ideal-gas-density`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md (lines 133-141)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/ideal_gas_density.avif"

# Constants from subsection text (book/05_atmospheres_1/atmospheres_1.md)
KB = 1.381e-23  # Boltzmann constant [J K^-1]
M_U = 1.661e-27  # atomic mass unit [kg]
BAR_TO_PA = 1e5  # 1 bar = 10^5 Pa

# Compositions: (mu, label, color)
COMPOSITIONS = [
    (43.4, r"Venus $\mathrm{CO_2}$ ($\mu = 43.4$)", "#d62728"),
    (28.97, r"Earth air ($\mu = 28.97$)", "#1f77b4"),
    (2.2, r"Jupiter $\mathrm{H_2/He}$ ($\mu = 2.2$)", "#2ca02c"),
]


def density(p_bar: np.ndarray | float, mu: float, temp_k: float) -> np.ndarray | float:
    """Compute gas mass density from the ideal gas law in atmospheric form.

    Uses rho = P * mu * m_u / (kB * T) as given in Eq. (eq:ideal-gas-atm).

    Parameters
    ----------
    p_bar : numpy.ndarray or float
        Atmospheric pressure in bar.
    mu : float
        Mean molecular weight in atomic mass units.
    temp_k : float
        Atmospheric temperature in Kelvin.

    Returns
    -------
    numpy.ndarray or float
        Gas mass density in kg m^-3.
    """
    p_pa = p_bar * BAR_TO_PA
    return (p_pa * mu * M_U) / (KB * temp_k)


def make_plot() -> Path:
    """Generate the ideal gas density figure and save to AVIF.

    Returns
    -------
    pathlib.Path
        Path to the saved figure file.
    """
    apply_style()
    fig, ax = plt.subplots(figsize=(7, 4.2))

    # Pressure range from 1e-3 to 1e2 bar specified in sketch spec
    p_grid = np.logspace(-3, 2, 300)

    # Three lines at T = 288 K (solid)
    for mu, label, color in COMPOSITIONS:
        ax.loglog(p_grid, density(p_grid, mu, 288.0), color=color, lw=1.8,
                  label=label)

    # Dashed set of the same three at T = 737 K to show temperature dependence
    for mu, _, color in COMPOSITIONS:
        ax.loglog(p_grid, density(p_grid, mu, 737.0), color=color, lw=1.8,
                  ls="--")

    # Style indicators for temperature in legend
    ax.plot([], [], color="0.3", lw=1.5, ls="-", label=r"$T = 288\ \mathrm{K}$")
    ax.plot([], [], color="0.3", lw=1.5, ls="--", label=r"$T = 737\ \mathrm{K}$")

    # Earth surface marker: 1 bar, 288 K, mu = 28.97
    rho_earth = density(1.0, 28.97, 288.0)
    ax.plot(1.0, rho_earth, "o", color="#1f77b4", ms=7, zorder=5)
    ax.annotate(
        "Earth surface\n(1 bar, 288 K)",
        xy=(1.0, rho_earth),
        xytext=(0.25, 80.0),
        textcoords="data",
        ha="center",
        va="center",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="0.3", lw=0.8),
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor="none", alpha=0.85),
    )

    # Venus surface marker: 92 bar, 737 K, mu = 43.4
    rho_venus = density(92.0, 43.4, 737.0)
    ax.plot(92.0, rho_venus, "s", color="#d62728", ms=7, zorder=5)
    ax.annotate(
        "Venus surface\n(92 bar, 737 K)",
        xy=(92.0, rho_venus),
        xytext=(-15, 12),
        textcoords="offset points",
        ha="right",
        va="bottom",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="0.3", lw=0.8),
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor="none", alpha=0.85),
    )

    # Jupiter 1-bar level marker: 1 bar, 165 K, mu = 2.2
    rho_jup = density(1.0, 2.2, 165.0)
    ax.plot(1.0, rho_jup, "^", color="#2ca02c", ms=7, zorder=5)
    ax.annotate(
        "Jupiter 1-bar level\n(1 bar, 165 K)",
        xy=(1.0, rho_jup),
        xytext=(30, -35),
        textcoords="offset points",
        ha="left",
        va="top",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="0.3", lw=0.8),
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                  edgecolor="none", alpha=0.85),
    )

    ax.set_xlim(1e-3, 1e2)
    ax.set_ylim(1e-5, 8e2)
    ax.set_xlabel("Pressure $P$ (bar)", fontsize=11)
    ax.set_ylabel(r"Gas mass density $\rho$ (kg m$^{-3}$)", fontsize=11)
    ax.legend(loc="upper left", framealpha=0.9, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Build the figure and display the output path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()