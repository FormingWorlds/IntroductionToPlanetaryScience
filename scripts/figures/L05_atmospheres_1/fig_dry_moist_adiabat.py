"""Generate Fig. (`fig:dry-moist-adiabat`).

Dry adiabatic lapse rate Gamma_d = g/c_p ~ 9.8 K/km, a representative
saturated moist adiabat (~5 K/km) and the deterministic US Standard
Atmosphere 1976 (USSA76) layer-defined profile, plotted as
temperature vs altitude up to 18 km.

Caption / figure id : `fig:dry-moist-adiabat`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md

The "observed" curve is the USSA76 piecewise-linear definition, not
measured data; layer breakpoints are tabulated in the standard.
The dry adiabat anchors at the surface (288.15 K, 0 km). The moist
adiabat is approximated as 5 K/km below the tropopause, then frozen
to the dry-adiabat-anchored isothermal value above 11 km.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/dry_moist_adiabat.avif"

# Surface anchor (USSA76)
T_SFC = 288.15  # K
GAMMA_DRY = 9.8  # K/km
GAMMA_MOIST = 5.0  # K/km (representative warm-troposphere value)

# USSA76 piecewise definition: (z_top_km, lapse_rate_K_per_km, T_top_K)
USSA76_LAYERS = [
    (0.0,  None,  288.15),
    (11.0, -6.5,  216.65),
    (20.0,  0.0,  216.65),
    (32.0,  1.0,  228.65),
    (47.0,  2.8,  270.65),
    (51.0,  0.0,  270.65),
    (71.0, -2.8,  214.65),
    (84.852, -2.0, 186.946),
]


def ussa76(z_km: np.ndarray) -> np.ndarray:
    """Return USSA76 temperature (K) for altitude z (km)."""
    z = np.atleast_1d(z_km)
    T = np.full_like(z, np.nan, dtype=float)
    for i in range(1, len(USSA76_LAYERS)):
        z0, _, T0 = USSA76_LAYERS[i - 1]
        z1, lapse, T1 = USSA76_LAYERS[i]
        in_layer = (z >= z0) & (z <= z1)
        if np.any(in_layer):
            T[in_layer] = T0 + lapse * (z[in_layer] - z0)
    return T


def make_plot() -> Path:
    apply_style()
    z = np.linspace(0, 18, 400)

    T_dry = T_SFC - GAMMA_DRY * z
    # Moist adiabat: shallow lapse below tropopause, isothermal above
    z_trop = 11.0
    T_moist = np.where(z <= z_trop, T_SFC - GAMMA_MOIST * z,
                       T_SFC - GAMMA_MOIST * z_trop)
    T_obs = ussa76(z)

    fig, ax = plt.subplots(figsize=(6.0, 6.5))
    ax.plot(T_dry, z, "k--", lw=1.6,
            label=r"Dry adiabat ($\Gamma_d = g/c_p \approx 9.8$ K km$^{-1}$)")
    ax.plot(T_moist, z, ":", lw=2.0, color="#1f77b4",
            label=r"Saturated moist adiabat ($\sim 5$ K km$^{-1}$)")
    ax.plot(T_obs, z, "-", lw=2.0, color="#1f77b4",
            label="Observed mean (US Standard 1976)")

    ax.axhline(z_trop, color="0.7", linestyle=":", lw=0.8)
    ax.text(298, z_trop + 0.2, "tropopause", color="0.5",
            fontsize=9, ha="right")

    ax.set_xlim(150, 305)
    ax.set_ylim(0, 18)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title("Dry vs moist adiabatic lapse rates (Earth)")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=False, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
