"""Generate Fig. (`fig:escape-regime`).

Schematic regime diagram for atmospheric escape in the
(lambda_J, F_EUV / F_EUV_today) plane: hydrodynamic outflow at low
Jeans parameter or high EUV; Jeans (thermal) escape at moderate
lambda_J, present-day EUV; full retention at large lambda_J.

Caption / figure id : `fig:escape-regime`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation keys       : Hunten1987, Tian2009

Marker positions are illustrative and follow the caption text:
- atomic H on Earth and Mars  -> Jeans regime
- N2 on Titan, CO2 on Mars     -> retained
- H2 on early sub-Neptune      -> hydrodynamic
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/escape_regime_diagram.avif"

# Regime boundaries (illustrative)
LAM_HYDRO = 3.0       # below this lambda_J, always hydrodynamic
LAM_RETAIN = 30.0     # above this, retained
EUV_HYDRO = 30.0      # above this multiple of present Earth, hydrodynamic at any lambda


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 6.5))

    lam_min, lam_max = 0.3, 500
    f_min, f_max = 0.4, 300

    # Shaded regions
    # Hydrodynamic: lambda < LAM_HYDRO  OR  EUV > EUV_HYDRO
    # We draw two rectangles:
    ax.add_patch(Rectangle((lam_min, f_min), LAM_HYDRO - lam_min,
                           f_max - f_min, color="#e07a4a", alpha=0.18, zorder=0))
    ax.add_patch(Rectangle((LAM_HYDRO, EUV_HYDRO),
                           lam_max - LAM_HYDRO, f_max - EUV_HYDRO,
                           color="#e07a4a", alpha=0.18, zorder=0))
    # Jeans: middle band
    ax.add_patch(Rectangle((LAM_HYDRO, f_min),
                           LAM_RETAIN - LAM_HYDRO, EUV_HYDRO - f_min,
                           color="#e6c852", alpha=0.20, zorder=0))
    # Retained
    ax.add_patch(Rectangle((LAM_RETAIN, f_min),
                           lam_max - LAM_RETAIN, EUV_HYDRO - f_min,
                           color="#3aab66", alpha=0.18, zorder=0))

    # Region labels
    ax.text(0.7, 4.0, "Hydrodynamic\noutflow",
            fontsize=11, color="#a14a25", weight="bold", ha="left")
    ax.text(8.0, 80, "EUV-driven hydrodynamic\n(young-star regime)",
            fontsize=11, color="#a14a25", weight="bold", ha="center")
    ax.text(9.0, 8.0, "Jeans\n(thermal)",
            fontsize=11, color="#9b7b18", weight="bold", ha="center")
    ax.text(80, 8.0, "Retained",
            fontsize=11, color="#1f6b3b", weight="bold", ha="center")

    # Markers (place labels ABOVE markers to keep them inside the plot)
    markers = [
        ("H on Earth today", 8.0, 1.0, "#1f77b4"),
        ("H on Mars today", 5.5, 1.5, "#d62728"),
        ("N$_2$ on Titan today", 70.0, 0.6, "#b8860b"),
        ("CO$_2$ on Mars today", 250.0, 1.5, "#2ca02c"),
        (r"H$_2$ on early sub-Neptune", 2.0, 50.0, "#6a3d9a"),
    ]
    for label, lam, fxuv, color in markers:
        ax.plot(lam, fxuv, "o", color=color, ms=9, mec="black", mew=0.5,
                zorder=5)
        if "Titan" in label:
            xytext = (lam * 1.5, fxuv * 1.7)
            ha = "left"
        elif "CO" in label:
            xytext = (lam * 0.4, fxuv * 1.6)
            ha = "right"
        elif "sub-Neptune" in label:
            xytext = (lam * 1.6, fxuv * 0.45)
            ha = "left"
        elif "Mars today" in label:
            xytext = (lam * 0.45, fxuv * 1.6)
            ha = "right"
        else:  # Earth
            xytext = (lam * 1.4, fxuv * 1.7)
            ha = "left"
        ax.annotate(label, xy=(lam, fxuv), xytext=xytext, ha=ha,
                    fontsize=9, color=color,
                    arrowprops=dict(arrowstyle="-", color=color,
                                    lw=0.6))

    # Boundary lines
    ax.axvline(LAM_HYDRO, color="0.35", linestyle="--", lw=0.8, zorder=1)
    ax.axvline(LAM_RETAIN, color="0.35", linestyle="--", lw=0.8, zorder=1)
    ax.axhline(EUV_HYDRO, color="0.35", linestyle="--", lw=0.8, zorder=1)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(lam_min, lam_max)
    ax.set_ylim(f_min, f_max)
    ax.set_xlabel(r"Jeans escape parameter $\lambda_J = v_{\mathrm{esc}}^2 / v_{\mathrm{th}}^2$")
    ax.set_ylabel(r"EUV flux (present-day Earth units)")
    ax.set_title("Atmospheric escape regime diagram")
    ax.grid(which="both", linestyle=":", alpha=0.25, zorder=1)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
