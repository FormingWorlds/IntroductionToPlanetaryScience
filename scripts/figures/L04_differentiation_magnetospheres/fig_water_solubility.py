"""Generate Fig. (`fig:water-solubility`).

Solubility of H2O in basaltic silicate melt as a function of the H2O
partial pressure above the melt, following the Henrian square-root
law for OH-speciated dissolved water:

    X_H2O [wt%] = K * sqrt(p_H2O [MPa])

with K ~ 0.42 wt% MPa^{-1/2} representative of basalt at 1573 K
(Hirschmann 2012).

Caption / figure id : `fig:water-solubility`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Hirschmann2012
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/water_solubility.avif"

K = 0.42  # wt% MPa^{-1/2}


def x_h2o(p_MPa: np.ndarray) -> np.ndarray:
    return K * np.sqrt(p_MPa)


def make_plot() -> Path:
    apply_style()
    p_MPa = np.logspace(-1, 3, 400)
    x = x_h2o(p_MPa)

    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    ax.plot(p_MPa, x, color="#1f77b4", lw=2.0,
            label=r"$X_{\mathrm{H_2O}} = K\, p_{\mathrm{H_2O}}^{1/2}$")

    # Reference markers chosen to anchor the caption text:
    # 1 bar ~ 0.1 MPa; 1 kbar = 100 MPa; 5 kbar = 500 MPa.
    refs = [
        (0.1, "1 bar"),
        (100.0, "1 kbar (~ 4 wt%)"),
        (500.0, "5 kbar (~ 9 wt%)"),
    ]
    for p_ref, label in refs:
        x_ref = x_h2o(p_ref)
        ax.plot(p_ref, x_ref, "o", color="black", ms=5, zorder=5)
        if p_ref < 1:
            ax.annotate(label, xy=(p_ref, x_ref),
                        xytext=(p_ref * 1.5, x_ref * 0.4),
                        fontsize=10, ha="left")
        else:
            ax.annotate(label, xy=(p_ref, x_ref),
                        xytext=(p_ref * 1.4, x_ref * 0.55),
                        fontsize=10, ha="left")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.1, 1000)
    ax.set_ylim(0.05, 30)
    ax.set_xlabel(r"$p_{\mathrm{H_2O}}$ (MPa)")
    ax.set_ylabel(r"Dissolved H$_2$O in basalt (wt%)")
    ax.set_title("Solubility of H$_2$O in basaltic melt at 1573 K")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
