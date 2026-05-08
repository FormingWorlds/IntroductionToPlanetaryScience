"""Generate Fig. (`fig:prem-profile`).

PREM (Dziewonski & Anderson 1981) radial profiles of compressional
(v_P), shear (v_S) wave speeds and density (rho) plotted against
depth, with the major boundaries marked: the Mohorovicic disc.
(Moho, ~24 km), the upper-mantle phase transitions at 410 and 660
km, the core-mantle boundary (CMB, 2891 km) where v_S drops to zero
in the liquid outer core, and the inner-core boundary (ICB, 5150 km).

Caption / figure id : `fig:prem-profile`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Dziewonski1981

PREM polynomial coefficients are encoded in `_prem.py` (this dir).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure
from scripts.figures.L08_interiors._prem import prem_at_depth


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/prem_profile.avif"

# Major depth boundaries (km)
BOUNDARIES = {
    "Moho ($\\sim$24 km)": 24.0,
    "410 km": 410.0,
    "660 km": 660.0,
    "CMB (2891 km)": 2891.0,
    "ICB (5150 km)": 5150.0,
}


def make_plot() -> Path:
    apply_style()

    # Sample finely around discontinuities to capture the jumps
    z_dense = np.concatenate([
        np.linspace(0, 50, 50),
        np.linspace(50, 700, 200),
        np.linspace(700, 2890, 220),
        np.linspace(2890.001, 5149.999, 230),
        np.linspace(5150.001, 6371, 100),
    ])
    rho, vP, vS = prem_at_depth(z_dense)

    fig, ax = plt.subplots(figsize=(7.5, 8.5))
    ax.plot(vP, z_dense, color="#1f77b4", lw=2.0, label=r"$v_P$ (km s$^{-1}$)")
    ax.plot(vS, z_dense, color="#d62728", lw=2.0, label=r"$v_S$ (km s$^{-1}$)")
    ax.plot(rho, z_dense, color="#2ca02c", lw=2.0, label=r"$\rho$ (g cm$^{-3}$)")

    ax.invert_yaxis()
    ax.set_xlim(0, 15)
    ax.set_ylim(6371, 0)
    ax.set_xlabel(r"$v_P$, $v_S$ (km s$^{-1}$);  $\rho$ (g cm$^{-3}$)")
    ax.set_ylabel("Depth (km)")
    ax.set_title("PREM: Earth's radial structure (Dziewonski & Anderson 1981)")
    ax.grid(linestyle=":", alpha=0.3)

    # Boundary annotations
    for label, depth in BOUNDARIES.items():
        ax.axhline(depth, color="0.5", linestyle=":", lw=0.8)
        ax.text(14.5, depth, label, color="0.4", fontsize=9,
                ha="right", va="bottom")

    # Explicit v_S = 0 callout at the CMB (key seismology result -
    # liquid outer core has zero shear strength)
    ax.annotate(r"$v_S = 0$" + "\n(liquid outer core)",
                xy=(0.05, 2891), xytext=(2.3, 3500),
                fontsize=10, color="#a83232",
                arrowprops=dict(arrowstyle="->", color="#a83232", lw=1.0))

    # Region labels
    ax.text(0.5, 250, "Upper mantle", color="0.4", fontsize=10,
            ha="left", va="center")
    ax.text(0.5, 1700, "Lower mantle", color="0.4", fontsize=10,
            ha="left", va="center")
    ax.text(0.5, 4000, "Outer core (liquid)", color="0.4", fontsize=10,
            ha="left", va="center")
    ax.text(0.5, 6000, "Inner core (solid)", color="0.4", fontsize=10,
            ha="left", va="center")

    ax.legend(loc="lower right", frameon=True, fontsize=10)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
