"""Generate Fig. (`fig:earth-tz-layers`).

Earth's vertical temperature profile from US Standard Atmosphere
1976 with the four named layers (troposphere, stratosphere,
mesosphere, thermosphere) shaded. Pause levels at tropopause
(11 km), stratopause (50 km), mesopause (85 km) marked.

Caption / figure id : `fig:earth-tz-layers`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : USStandardAtmosphere1976

USSA76 layer breakpoints (deterministic):
- Troposphere   0-11 km : -6.5 K/km, T(0)=288.15 K
- Tropopause   11-20 km : isothermal 216.65 K
- Stratosphere 20-32 km : +1.0 K/km
- Stratosphere 32-47 km : +2.8 K/km
- Stratopause  47-51 km : isothermal 270.65 K
- Mesosphere   51-71 km : -2.8 K/km
- Mesosphere   71-85 km : -2.0 K/km

Above 85 km (USSA76 limit) we use a Bates-Walker thermosphere
profile T(z) = T_inf - (T_inf - T_120) * exp(-sigma (z - z_120))
with T_inf = 1000 K, T_120 = 360 K, sigma = 0.025 km^-1, anchored
to USSA76 at the mesopause via a smoothing transition. This is a
representative quiet-sun profile.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/earth_tz_layers.avif"

# USSA76 piecewise definition
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

# Bates-Walker thermosphere parameters
T_INF = 1000.0
T_120 = 360.0
SIGMA = 0.025  # km^-1


def ussa76(z_km: np.ndarray) -> np.ndarray:
    z = np.atleast_1d(z_km)
    T = np.full_like(z, np.nan, dtype=float)
    for i in range(1, len(USSA76_LAYERS)):
        z0, _, T0 = USSA76_LAYERS[i - 1]
        z1, lapse, _ = USSA76_LAYERS[i]
        in_layer = (z >= z0) & (z <= z1)
        if np.any(in_layer):
            T[in_layer] = T0 + lapse * (z[in_layer] - z0)
    return T


def thermosphere(z_km: np.ndarray) -> np.ndarray:
    return T_INF - (T_INF - T_120) * np.exp(-SIGMA * (z_km - 120.0))


def make_plot() -> Path:
    apply_style()
    z_lower = np.linspace(0, 85, 200)
    z_thermo = np.linspace(85, 200, 200)

    T_lower = ussa76(z_lower)
    # Smoothly interpolate from USSA76 mesopause T (~187 K) to T_120 (360 K)
    # over the 85-120 km region; above 120 km use Bates-Walker.
    T_thermo = np.where(
        z_thermo < 120,
        # Linear interp from (85, 187) to (120, 360)
        187.0 + (360.0 - 187.0) * (z_thermo - 85.0) / (120.0 - 85.0),
        thermosphere(z_thermo))

    fig, ax = plt.subplots(figsize=(6.5, 8.5))

    # Layer shading
    ax.axhspan(0, 11, color="#fde0e0", alpha=0.4, zorder=0)
    ax.axhspan(11, 50, color="#dde7f8", alpha=0.4, zorder=0)
    ax.axhspan(50, 85, color="#e6f0d8", alpha=0.4, zorder=0)
    ax.axhspan(85, 200, color="#fde6c8", alpha=0.4, zorder=0)

    # Layer name labels
    ax.text(950, 5, "Troposphere", color="#666", fontsize=11, ha="right",
            style="italic")
    ax.text(950, 30, "Stratosphere", color="#666", fontsize=11, ha="right",
            style="italic")
    ax.text(950, 67, "Mesosphere", color="#666", fontsize=11, ha="right",
            style="italic")
    ax.text(950, 140, "Thermosphere", color="#666", fontsize=11, ha="right",
            style="italic")

    # Pause levels
    for z, label in [(11, "Tropopause"), (50, "Stratopause"), (85, "Mesopause")]:
        ax.axhline(z, color="0.5", linestyle="--", lw=0.6)
        ax.text(150, z + 1.5, label, color="0.4", fontsize=9)

    ax.plot(T_lower, z_lower, color="#1f77b4", lw=2.5)
    ax.plot(T_thermo, z_thermo, color="#1f77b4", lw=2.5)

    ax.set_xlim(150, 1000)
    ax.set_ylim(0, 200)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title("Earth T(z), US Standard Atmosphere 1976")
    ax.grid(linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
