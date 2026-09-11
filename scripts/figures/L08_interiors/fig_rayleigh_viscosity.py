"""The Rayleigh number governing mantle convection against dynamic viscosity.

Course Earth mantle values: alpha = 2e-5 per K, rho = 4000 kg/m^3, g = 10 m/s^2,
Delta T = 2500 K, d = 3e6 m, kappa = 1e-6 m^2/s, with eta from 1e18 to 1e25 Pa s.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/rayleigh_viscosity.avif"

# Earth mantle parameters, "Ra = alpha rho g Delta T d^3 / (kappa eta)")
ALPHA = 2e-5        # Thermal expansivity [K^-1]
RHO = 4000.0        # Mantle density [kg m^-3]
G = 10.0            # Gravitational acceleration [m s^-2]
DELTA_T = 2500.0    # Temperature difference [K]
D = 3e6             # Mantle layer thickness [m]
KAPPA = 1e-6        # Thermal diffusivity [m^2 s^-1]
RA_C = 1e3          # Critical Rayleigh number, Ra_c about 1e3


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.2, 4.6))

    # Viscosity range: 1e18 to 1e25 Pa s
    eta = np.logspace(18, 25, 300)
    # Ra = alpha rho g Delta T d^3 / (kappa eta)
    ra = (ALPHA * RHO * G * DELTA_T * D**3) / (KAPPA * eta)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e18, 1e25)
    ax.set_ylim(1e2, 1e12)

    # Shaded convective regime Ra >= Ra_c
    ax.axhspan(RA_C, 1e12, facecolor="#e8f1fa", edgecolor="none", zorder=0)

    # Earth mantle band eta = 1e21 to 1e22 Pa s,268,)
    ax.axvspan(1e21, 1e22, facecolor="#fdebd0", edgecolor="none", alpha=0.7, zorder=1)

    # Critical Rayleigh number onset line,)
    ax.axhline(RA_C, color="#c0392b", linestyle="--", lw=1.5, zorder=2)

    # Rayleigh number curve,)
    ax.plot(eta, ra, color="#1f6db8", lw=2.5, zorder=3)

    # Labels placed in empty space
    ax.text(
        1.5e18, 1.8e3,
        "onset of convection, Ra_c about 1e3",
        color="#c0392b", fontsize=10, ha="left", va="bottom", zorder=4,
    )
    ax.text(
        2e23, 2e10,
        "convects",
        color="#1f6db8", fontsize=10, ha="center", va="center", weight="bold", zorder=4,
    )
    ax.text(
        3.16e21, 2e11,
        "Earth: Ra about 1e7 to 1e8",
        color="#c46b1a", fontsize=10, ha="center", va="center", weight="bold", zorder=4,
    )

    ax.set_xlabel(r"Mantle dynamic viscosity $\eta$ (Pa s)")
    ax.set_ylabel(r"Rayleigh number $\mathrm{Ra}$")
    ax.set_title("Convection is decided by the Rayleigh number", fontsize=11)

    fig.tight_layout()
    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
