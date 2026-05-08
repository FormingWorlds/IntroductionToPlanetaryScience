"""Generate Fig. (`fig:hadley-observed`).

Idealised zonal-mean meridional streamfunction of Earth's
troposphere (latitude vs altitude). Three pairs of cells per
hemisphere: thermally-direct Hadley cells (equator to ~30 deg),
indirect Ferrel cells (~30-60 deg), weak polar cells (poleward
of ~60 deg). Solid blue = counter-clockwise (NH Hadley sense),
dashed red = clockwise.

Caption / figure id : `fig:hadley-observed`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
Citation key        : Held1980

Synthetic streamfunction following the structural shape of an
axisymmetric inviscid atmosphere; not a reproduction of any single
reanalysis dataset. Cell amplitudes are scaled to give realistic
visual contour spacings.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/hadley_observed.avif"


def streamfunction(phi_deg: np.ndarray, z_km: np.ndarray) -> np.ndarray:
    """Synthetic streamfunction with three latitudinal cell pairs.

    psi(phi, z) = A * sin(pi z / H) * (
        Hadley:  + sin(2 phi)            for |phi| < 30 deg
        Ferrel:  - 0.5 * sin(2 (phi - 30 deg))  for 30 <= |phi| < 60 deg, sign flipped
        Polar:   + 0.2 * sin(3 (phi - 60 deg))  for 60 <= |phi| <= 90 deg
    )

    Implemented as a sum of latitudinal lobes with appropriate signs
    so that NH Hadley is counter-clockwise (rising at equator,
    sinking at 30 deg N).
    """
    PHI, Z = np.meshgrid(phi_deg, z_km)
    # Vertical envelope (zero at surface and tropopause)
    H_TROP = 15.0  # km (tropopause)
    vertical = np.where(Z <= H_TROP, np.sin(np.pi * Z / H_TROP), 0.0)

    psi = np.zeros_like(PHI)

    # Hadley: peak at +/-15 deg, vanishing at 0 and +/-30
    hadley_mask = np.abs(PHI) <= 30.0
    psi += np.where(hadley_mask,
                    np.sin(np.pi * PHI / 30.0),
                    0.0) * 1.0

    # Ferrel: between 30-60, opposite sense
    ferrel_mask = (np.abs(PHI) > 30.0) & (np.abs(PHI) <= 60.0)
    psi += np.where(ferrel_mask,
                    -np.sign(PHI) * np.sin(np.pi * (np.abs(PHI) - 30.0) / 30.0),
                    0.0) * 0.45

    # Polar: between 60-90, same sense as Hadley
    polar_mask = np.abs(PHI) > 60.0
    psi += np.where(polar_mask,
                    np.sign(PHI) * np.sin(np.pi * (np.abs(PHI) - 60.0) / 30.0),
                    0.0) * 0.18

    return psi * vertical


def make_plot() -> Path:
    apply_style()
    phi = np.linspace(-90, 90, 400)
    z = np.linspace(0, 20, 200)
    psi = streamfunction(phi, z)

    fig, ax = plt.subplots(figsize=(9.5, 5.5))

    levels_pos = np.linspace(0.05, 1.0, 6)
    levels_neg = -levels_pos[::-1]

    cs_pos = ax.contour(phi, z, psi, levels=levels_pos,
                         colors="#1f4e79", linewidths=1.2)
    cs_neg = ax.contour(phi, z, psi, levels=levels_neg,
                         colors="#a83232", linewidths=1.2,
                         linestyles="--")

    # Tropopause
    ax.axhline(15, color="black", linestyle="--", lw=1.0)
    ax.text(85, 15.5, "Tropopause", color="0.3", fontsize=9, ha="right")

    # Cell labels
    cell_labels = [
        (-75, 5, "Polar"),
        (-45, 5, "Ferrel"),
        (-15, 5, "Hadley\n(SH)"),
        ( 15, 5, "Hadley\n(NH)"),
        ( 45, 5, "Ferrel"),
        ( 75, 5, "Polar"),
    ]
    for x, y, label in cell_labels:
        ax.text(x, y, label, fontsize=9, ha="center", va="center",
                bbox=dict(facecolor="white", edgecolor="none", pad=2))

    ax.set_xlim(-90, 90)
    ax.set_ylim(0, 18)
    ax.set_xlabel("Latitude (deg)")
    ax.set_ylabel("Altitude (km)")
    ax.set_xticks(np.arange(-90, 91, 30))
    ax.set_title("Earth zonal-mean meridional streamfunction (idealised)")
    ax.grid(linestyle=":", alpha=0.3)

    # Legend proxies
    from matplotlib.lines import Line2D
    handles = [
        Line2D([0], [0], color="#1f4e79", lw=1.5,
               label="Counter-clockwise (NH Hadley sense)"),
        Line2D([0], [0], color="#a83232", lw=1.5, linestyle="--",
               label="Clockwise"),
        Line2D([0], [0], color="black", lw=1.0, linestyle="--",
               label="Tropopause"),
    ]
    ax.legend(handles=handles, loc="upper right", frameon=True, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
