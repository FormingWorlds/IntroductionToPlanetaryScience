"""Generate Fig. (`fig:mantle-adiabat`).

Schematic temperature profile of Earth's mantle showing the
cold TBL (lithosphere), the adiabatic convecting mantle, and the
hot TBL (D'' layer).

Caption / figure id : `fig:mantle-adiabat`
Markdown source     : book/03_heat_energy/heat_energy.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/mantle_adiabat_tbl.avif"

def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7, 7.5))

    # Depth and Temperature points
    # Surface -> Base of Lithosphere -> Top of D'' -> Core-Mantle Boundary
    depths = np.array([0, 100, 2700, 2900])
    temps = np.array([300, 1600, 2900, 4000])

    # Plot the main temperature profile line
    ax.plot(temps, depths, color="#1f77b4", lw=3.0)

    # Shaded region for Cold TBL (lithosphere)
    ax.axhspan(0, 100, color="#1f77b4", alpha=0.15)
    ax.text(1900, 50, "Cold TBL\n(lithosphere, ~100 km)", color="#1f77b4",
            ha="center", va="center", fontsize=11)

    # Shaded region for Hot TBL (D'')
    ax.axhspan(2700, 2900, color="#d62728", alpha=0.12)
    ax.text(1500, 2800, "Hot TBL (D'', ~200 km)", color="#d62728",
            ha="center", va="center", fontsize=11)

    # Convecting mantle label
    ax.text(3500, 1400, "Convecting mantle\n(near-adiabatic)", color="0.2",
            ha="center", va="center", fontsize=11)

    # Core-mantle boundary line
    ax.axhline(2900, color="0.3", linestyle="--", lw=1.2)
    ax.text(2250, 2970, "Core-mantle boundary", color="0.3",
            ha="center", va="center", fontsize=11)

    ax.set_ylim(3050, -100)
    ax.set_xlim(0, 4500)
    ax.set_xlabel("Temperature $T$ (K)")
    ax.set_ylabel("Depth (km)")
    ax.set_title("Schematic temperature profile through Earth's mantle")
    
    ax.grid(linestyle="-", alpha=0.2)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=75)

def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")

if __name__ == "__main__":
    main()
