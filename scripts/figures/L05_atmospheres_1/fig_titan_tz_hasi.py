"""Generate Fig. (`fig:titan-tz-hasi`).

Titan's vertical temperature profile from the Huygens HASI descent
on 14 January 2005, as published by Fulchignoni et al. 2005.
Pedagogical fit to the published HASI profile, not a direct
reproduction.

Caption / figure id : `fig:titan-tz-hasi`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : Fulchignoni2005

Reference points from Fulchignoni 2005 Fig. 2:
- Surface: 94 K, 1.5 bar
- Tropopause: ~44 km, 70 K
- Stratospheric peak (haze heating): ~200 km, ~175 K
- Mesospheric minimum: ~600 km, ~140 K
- Thermosphere: rising back to ~200 K at 1400 km
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/titan_tz_hasi.avif"

# (altitude_km, temperature_K) from Fulchignoni 2005 Fig. 2 reference points
PROFILE = [
    (   0,  94.0),
    (  10,  84.0),
    (  20,  76.0),
    (  44,  70.0),    # tropopause
    (  60,  82.0),
    (  80,  98.0),
    ( 100, 130.0),
    ( 150, 165.0),
    ( 200, 175.0),    # stratospheric peak
    ( 300, 165.0),
    ( 400, 150.0),
    ( 500, 142.0),
    ( 600, 140.0),    # mesospheric min
    ( 800, 152.0),
    (1000, 168.0),
    (1200, 188.0),
    (1400, 205.0),
]


def make_plot() -> Path:
    apply_style()
    z = np.array([p[0] for p in PROFILE])
    T = np.array([p[1] for p in PROFILE])

    fig, ax = plt.subplots(figsize=(7.0, 8.0))

    # Stratospheric haze layer shading (qualitative)
    ax.axhspan(50, 300, color="#fce6c4", alpha=0.45, zorder=0)
    ax.text(220, 250, "Stratospheric\ninversion\n(haze heating)",
            color="#9b6818", fontsize=10, style="italic", ha="center")

    ax.plot(T, z, color="#a04018", lw=2.5)

    # Surface anchor
    ax.plot(94, 0, "o", color="#a04018", ms=8, zorder=5)
    ax.annotate("Surface\n94 K, 1.5 bar",
                xy=(94, 0), xytext=(120, 150),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.5))

    # Tropopause
    ax.plot(70, 44, "o", color="#a04018", ms=7, zorder=5)
    ax.annotate("Tropopause\n~44 km, 70 K",
                xy=(70, 44), xytext=(80, 350),
                fontsize=10,
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.5))

    ax.set_xlim(60, 220)
    ax.set_ylim(0, 1400)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title("Titan T(z) from Huygens HASI descent")
    ax.grid(linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
