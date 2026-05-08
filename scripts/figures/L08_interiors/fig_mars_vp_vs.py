"""Generate Fig. (`fig:mars-vp-vs`).

Schematic radial profiles of Mars compressional (v_P) and shear
(v_S) wave speeds adopted from InSight seismic analyses
(Stahler 2021, Khan 2021).

- Crust thins to mantle below ~50 km
- Mantle: v_P ~ 7.7-9.0 km/s, v_S ~ 4.4-5.1 km/s
- Mid-mantle transition around ~1100 km depth (small kink)
- CMB at ~1559 km depth (-> R_core = 1830 km, R_Mars = 3389.5)
- Liquid core: v_S = 0; v_P drops at the boundary

Caption / figure id : `fig:mars-vp-vs`
Markdown source     : book/08_interiors/interiors.md
Citation keys       : Stahler2021, Khan2021
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/mars_vp_vs.avif"

R_MARS = 3389.5
R_CORE = 1830.0
DEPTH_CMB = R_MARS - R_CORE   # km from surface = 1559.5

# Anchor points for piecewise-linear-with-kinks profile
# (depth_km, v_P_km_s, v_S_km_s)
ANCHORS = [
    (0,    3.0, 1.7),
    (40,   3.5, 2.0),
    (50,   7.8, 4.4),    # Moho-like discontinuity
    (300,  7.9, 4.5),
    (1000, 8.4, 4.7),
    (1100, 9.0, 4.9),    # mid-mantle transition kink
    (1200, 8.9, 4.8),
    (1559, 9.6, 5.1),    # base of mantle
    # CMB jump (handled by separate plot below)
    (1559.001, 5.2, 0.0),  # outer core top: v_P drops, v_S = 0
    (3389,  6.0, 0.0),     # near centre
]


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 7.0))

    # Split the data at the CMB so v_P/v_S have separate segments
    z_mantle = np.array([a[0] for a in ANCHORS if a[0] < DEPTH_CMB])
    vP_mantle = np.array([a[1] for a in ANCHORS if a[0] < DEPTH_CMB])
    vS_mantle = np.array([a[2] for a in ANCHORS if a[0] < DEPTH_CMB])
    z_core = np.array([a[0] for a in ANCHORS if a[0] >= DEPTH_CMB])
    vP_core = np.array([a[1] for a in ANCHORS if a[0] >= DEPTH_CMB])
    vS_core = np.array([a[2] for a in ANCHORS if a[0] >= DEPTH_CMB])

    ax.plot(vP_mantle, z_mantle, color="#1f77b4", lw=2.0,
            label=r"$v_P$ (P-wave)")
    ax.plot(vS_mantle, z_mantle, color="#d62728", lw=2.0,
            label=r"$v_S$ (S-wave)")
    ax.plot(vP_core, z_core, color="#1f77b4", lw=2.0)
    ax.plot(vS_core, z_core, color="#d62728", lw=2.0)

    # CMB line
    ax.axhline(DEPTH_CMB, color="black", linestyle="--", lw=1.0)
    ax.text(11.5, DEPTH_CMB - 30, f"CMB (depth = {DEPTH_CMB:.0f} km)",
            color="black", fontsize=10, ha="right", va="bottom")

    # Region shading
    ax.axhspan(DEPTH_CMB, R_MARS, color="#fdebcb", alpha=0.45, zorder=0)
    ax.text(8.0, 2400, "Liquid Fe-S core\n(no S-wave)", color="#a87f1d",
            fontsize=11, ha="center", va="center")
    ax.text(8.0, 250, "Mantle", color="#666", fontsize=11, ha="center")

    # Crust kink reference
    ax.axhline(50, color="0.6", linestyle=":", lw=0.7)
    ax.text(11.5, 50, "Moho", color="0.4", fontsize=9, ha="right", va="bottom")

    # Mantle transition reference
    ax.axhline(1100, color="0.6", linestyle=":", lw=0.7)
    ax.text(11.5, 1100, "Mantle transition", color="0.4", fontsize=9,
            ha="right", va="bottom")

    ax.invert_yaxis()
    ax.set_xlim(0, 12.5)
    ax.set_ylim(R_MARS, 0)
    ax.set_xlabel(r"Seismic velocity (km s$^{-1}$)")
    ax.set_ylabel("Depth from surface (km)")
    ax.set_title("Mars radial seismic-velocity profile (InSight constraints)")
    ax.legend(loc="lower left", frameon=True, fontsize=10)
    ax.grid(linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
