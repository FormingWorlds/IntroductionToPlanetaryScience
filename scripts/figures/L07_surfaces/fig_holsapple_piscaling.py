"""Generate Fig. (`fig:holsapple-piscaling`).

Schematic of crater pi-scaling after Holsapple (1993). The
cratering efficiency

    pi_D = D (rho / m)^{1/3}

is plotted against the gravity-scaled impactor size

    pi_2 = g a / v^2.

At small pi_2 (laboratory craters), the target's tensile strength
dominates and pi_D is independent of pi_2 (strength regime). At
large pi_2 (planetary craters), gravity confines the ejecta and
pi_D ~ pi_2^(-mu/(2+mu)) (gravity regime).

Caption / figure id : `fig:holsapple-piscaling`
Markdown source     : book/07_surfaces/surfaces.md
Citation key        : Holsapple1993

Reference values follow the competent-rocky-target case
(mu = 0.55, applicable to soft and hard rock); strength-regime
plateau height is illustrative.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/07_surfaces/figures/holsapple_piscaling.avif"

MU = 0.55         # rocky target (Holsapple 1993, Table 1)
PI_D_STRENGTH = 30.0  # plateau height in strength regime (illustrative)
PI_2_TRANSITION = 1e-7  # rough transition pi_2 between strength and gravity


def make_plot() -> Path:
    apply_style()
    pi_2 = np.logspace(-9, -1, 600)

    # Strength-only branch (constant)
    pi_D_strength = np.full_like(pi_2, PI_D_STRENGTH)

    # Gravity-only branch: choose K so it crosses the strength plateau at
    # the transition pi_2 (so the two curves meet smoothly there).
    exponent = -MU / (2.0 + MU)
    K_grav = PI_D_STRENGTH / (PI_2_TRANSITION ** exponent)
    pi_D_gravity = K_grav * pi_2 ** exponent

    # Combined envelope: the smaller of the two on each branch
    pi_D_combined = np.minimum(pi_D_strength, pi_D_gravity)

    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    ax.plot(pi_2, pi_D_strength, color="#d62728", lw=1.4, linestyle="--",
            label="Strength-only (constant)")
    ax.plot(pi_2, pi_D_gravity, color="#1f77b4", lw=1.4, linestyle="--",
            label=fr"Gravity-only (slope $-\mu/(2+\mu)$)")
    ax.plot(pi_2, pi_D_combined, color="black", lw=2.0,
            label="Combined gravity + strength")

    # Annotate regimes
    ax.text(1e-9, 38, "Strength regime\n(small craters,\nlab impacts)",
            color="#a14a25", fontsize=9, ha="left")
    ax.text(2e-2, 1.8, "Gravity regime\n(planetary craters)",
            color="#1f4e79", fontsize=9, ha="right")

    # Transition pointer
    ax.annotate("Strength-gravity\ntransition",
                xy=(PI_2_TRANSITION, PI_D_STRENGTH),
                xytext=(3e-6, 8.0),
                fontsize=9, color="0.3", ha="center",
                arrowprops=dict(arrowstyle="->", color="0.3", lw=0.6))

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-9, 1e-1)
    ax.set_ylim(0.5, 100)
    ax.set_xlabel(r"$\pi_2 = g\,a / v^2$  (gravity-scaled impactor radius)")
    ax.set_ylabel(r"$\pi_D = D\,(\rho/m)^{1/3}$  (scaled crater diameter)")
    ax.set_title("Crater pi-scaling: gravity vs strength regime "
                 "(after Holsapple 1993)")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="lower left", frameon=False, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
