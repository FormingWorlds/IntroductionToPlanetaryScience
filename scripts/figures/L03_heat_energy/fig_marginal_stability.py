"""Generate Fig. (`fig:marginal-stability`).

Schematic Rayleigh-Bénard marginal-stability curve normalised to the
canonical critical values: Ra_c ≈ 1708 at non-dimensional wavenumber
k_c ≈ 3.117 between rigid horizontal boundaries.

Caption / figure id : `fig:marginal-stability`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : Chandrasekhar1961

The exact stability curve solves a transcendental boundary-value
problem; here we plot the standard analytic approximation:

    Ra(k) = (k^2 + pi^2)^3 / k^2

This is the *free-slip* (stress-free) result with Ra_c = 657.5 at
k_c = pi/sqrt(2) ≈ 2.221. The classical *rigid-rigid* boundary case
(Ra_c = 1707.762, k_c = 3.117) does not have a closed-form curve
but is well approximated for visualisation by scaling the free-slip
curve so its minimum sits at the rigid values, which is what we do.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/marginal_stability.avif"

# Rigid-rigid critical values (Chandrasekhar 1961, Table II)
RA_C = 1707.762
K_C = 3.117


def make_plot() -> Path:
    apply_style()

    # Free-slip stability curve (analytic) shifted to land on the
    # rigid-rigid critical values for visualisation.
    k = np.linspace(0.4, 8.0, 400)
    pi = np.pi
    free_slip = (k ** 2 + pi ** 2) ** 3 / k ** 2
    free_slip_min = 27.0 * pi ** 4 / 4.0  # value at k = pi/sqrt(2): 657.51
    # Scale and shift in k so the minimum hits (K_C, RA_C)
    scale_k = K_C / (pi / np.sqrt(2))
    k_shifted = k * scale_k
    Ra_shifted = free_slip * (RA_C / free_slip_min)

    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    ax.plot(k_shifted, Ra_shifted, color="#1f77b4", lw=2.0)

    # Fill convection-on region
    ax.fill_between(k_shifted, Ra_shifted, 1e6, color="#ff7f0e", alpha=0.13,
                    label="Convection")
    ax.fill_between(k_shifted, 0, Ra_shifted, color="#1f77b4", alpha=0.10,
                    label="Conduction only")

    # Mark critical point
    ax.plot(K_C, RA_C, "o", color="#d62728", markeredgecolor="black",
            markersize=8, zorder=5)
    ax.annotate(f"$\\mathrm{{Ra}}_c \\approx {RA_C:.0f}$,\n"
                f"$k_c \\approx {K_C:.2f}$",
                xy=(K_C, RA_C), xytext=(K_C + 0.5, RA_C * 0.45),
                fontsize=10,
                arrowprops=dict(arrowstyle="->", lw=0.8, color="dimgray"))

    ax.set_yscale("log")
    ax.set_xlabel(r"Non-dimensional horizontal wavenumber $k$")
    ax.set_ylabel(r"Rayleigh number $\mathrm{Ra}$")
    ax.set_xlim(0, 8)
    ax.set_ylim(5e2, 5e5)
    ax.set_title("Marginal stability curve (rigid horizontal boundaries)")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
