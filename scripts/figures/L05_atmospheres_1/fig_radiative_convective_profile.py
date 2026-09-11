"""Generate Fig. (`fig:radiative-convective`).

Schematic temperature-altitude diagram showing radiative-convective
equilibrium in an atmosphere (book/05_atmospheres_1/atmospheres_1.md).
Compares the unstable pure radiative equilibrium profile with the
convectively adjusted profile following the dry adiabatic lapse rate
(about 9.8 K/km, book/05_atmospheres_1/atmospheres_1.md, Eq. eq:dry-adiabat)
up to the tropopause near 12 km (book/05_atmospheres_1/atmospheres_1.md).

Caption / figure id : `fig:radiative-convective`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/radiative_convective_profile.avif"

# Characteristic numbers from subsection text and sketch specification
Z_TROPOPAUSE = 12.0  # km, tropopause level where gradients cross
GAMMA_DRY = 9.8  # K/km, dry adiabatic lapse rate (eq:dry-adiabat)

# Schematic temperature scaling constants (arbitrary reference units)
T_TROPOPAUSE = 200.0
CURVATURE_B = 1.3


def make_plot() -> Path:
    """Build the radiative-convective equilibrium schematic figure.

    Returns
    -------
    Path
        Path to the saved AVIF figure file.
    """
    apply_style()
    fig, ax = plt.subplots(figsize=(7.0, 4.0))

    # Altitude coordinate from 0 to 20 km as specified
    z = np.linspace(0.0, 20.0, 400)

    # Pure radiative profile: superadiabatic near surface, crosses adiabat at 12 km
    u = z - Z_TROPOPAUSE
    t_rad = T_TROPOPAUSE - GAMMA_DRY * u + 0.5 * CURVATURE_B * (u ** 2)

    # Convectively adjusted profile: dry adiabat below 12 km, radiative above
    t_conv = np.where(z <= Z_TROPOPAUSE,
                      T_TROPOPAUSE + GAMMA_DRY * (Z_TROPOPAUSE - z),
                      t_rad)

    # Shade the convective layer (0 to 12 km)
    ax.axhspan(0.0, Z_TROPOPAUSE, color="#eaf2fb", alpha=0.5, zorder=0)

    # Shade convective adjustment region between unstable radiative and dry adiabat
    ax.fill_betweenx(z[z <= Z_TROPOPAUSE], t_conv[z <= Z_TROPOPAUSE],
                     t_rad[z <= Z_TROPOPAUSE], color="#fde0e0", alpha=0.5,
                     zorder=1)

    # Pure radiative equilibrium curve (superadiabatic and unstable near surface)
    ax.plot(t_rad[z <= Z_TROPOPAUSE], z[z <= Z_TROPOPAUSE], linestyle="--",
            color="0.5", lw=2.0, label="radiative equilibrium (unstable)")

    # Convectively adjusted profile along dry adiabat and into stratosphere
    ax.plot(t_conv, z, linestyle="-", color="#1f77b4", lw=2.2,
            label="radiative-convective profile (dry adiabat)")

    # Tropopause level line and label
    ax.axhline(Z_TROPOPAUSE, color="0.55", linestyle=":", lw=1.0)
    ax.text(145.0, Z_TROPOPAUSE + 0.3, "tropopause", fontsize=10,
            color="0.35", va="bottom")

    # Stratosphere label in stable radiative region aloft
    ax.text(330.0, 13.8, "stratosphere (radiative)", fontsize=10,
            color="0.25", ha="center", va="center", style="italic")

    # Convective adjustment annotation with arrow into the adjusted region
    ax.text(145.0, 3.8, "convective adjustment", fontsize=10,
            color="#b22222", va="center")
    ax.add_patch(FancyArrowPatch((245.0, 3.8), (288.0, 3.8), arrowstyle="->",
                                 mutation_scale=10, color="#b22222", lw=1.2))

    ax.set_xlim(130.0, 430.0)
    ax.set_ylim(0.0, 20.0)
    ax.set_yticks([0, 4, 8, 12, 16, 20])
    ax.set_xticks([])
    ax.set_ylabel("Altitude (km)", fontsize=11)
    ax.set_xlabel("Temperature", fontsize=11)
    ax.set_title("Radiative-convective equilibrium (schematic)", fontsize=12)

    # Legend in the clear upper-right region, right of the stratospheric curve
    ax.legend(loc="upper right", frameon=True, facecolor="white",
              edgecolor="none", fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Generate and save figure."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()