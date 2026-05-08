"""Generate Fig. (`fig:venus-zonal-winds`).

Schematic of the zonal wind speed |u| on Venus as a function of
altitude, after the Venus Express VIRTIS cloud-tracking measurements
of Sanchez-Lavega 2008.

- Surface: |u| ~ 1.8 m/s (co-rotating with the solid body)
- Cloud-top peak (~70 km): |u| ~ 100 m/s (super-rotation)
- Mesospheric decline above the cloud tops

Caption / figure id : `fig:venus-zonal-winds`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md
Citation key        : SanchezLavega2008
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/venus_zonal_winds.avif"

# Reference points (z_km, u_m_s) compiled from Sanchez-Lavega 2008
# and earlier VIRA/VeGa lower-atmosphere descents.
PROFILE = [
    ( 0,    1.8),
    (10,    8.0),
    (20,   25.0),
    (30,   45.0),
    (40,   65.0),
    (50,   80.0),
    (60,   95.0),
    (70,  100.0),   # cloud-top peak
    (80,   85.0),
    (90,   60.0),
    (100,  40.0),
    (110,  30.0),
    (120,  20.0),
]


def make_plot() -> Path:
    apply_style()
    z = np.array([p[0] for p in PROFILE])
    u = np.array([p[1] for p in PROFILE])

    fig, ax = plt.subplots(figsize=(6.5, 7.5))
    ax.plot(u, z, color="#9b3c3c", lw=2.0)
    ax.fill_betweenx(z, 0, u, color="#9b3c3c", alpha=0.15)

    # Cloud deck shading
    ax.axhspan(48, 70, color="#f0e3a8", alpha=0.5, zorder=0,
               label="H$_2$SO$_4$ cloud deck (48-70 km)")

    # Surface co-rotation marker (vertical reference)
    ax.axvline(1.8, color="0.5", linestyle=":", lw=0.8)
    ax.text(2.5, 5, "Solid-body rotation\n(~1.8 m s$^{-1}$ surface)",
            fontsize=9, color="0.4")

    # Cloud-top peak annotation
    ax.annotate("Cloud-top super-rotation\n~100 m s$^{-1}$ at 70 km",
                xy=(100, 70), xytext=(60, 95),
                fontsize=10, color="#9b3c3c",
                arrowprops=dict(arrowstyle="->", color="#9b3c3c", lw=0.8))

    ax.set_xlim(0, 120)
    ax.set_ylim(0, 120)
    ax.set_xlabel(r"Zonal wind speed $|u|$ (m s$^{-1}$)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title("Venus zonal wind profile (after Sanchez-Lavega 2008)")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=True, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
