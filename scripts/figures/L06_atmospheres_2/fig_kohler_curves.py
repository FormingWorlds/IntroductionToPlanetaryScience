"""Generate Fig. (`fig:kohler-curves`).

Köhler curves: equilibrium saturation S(r) - 1 vs droplet radius r
for a pure water droplet (Kelvin term only) and three solution
droplets condensed on dry NaCl CCN of three different solute masses.

    S - 1 ~ A/r - B/r^3
    A = 2 sigma_w / (rho_w R_v T)        (Kelvin / curvature)
    B = 3 i M_w m_s / (4 pi rho_w M_s)   (Raoult / solute)

Caption / figure id : `fig:kohler-curves`
Markdown source     : book/06_atmospheres_2/atmospheres_2.md

NOTE on solute masses:
The L06 caption text quotes "m_s = 10^-19 to 10^-17 g". That range
gives unrealistic activation supersaturations of 1-13 percent. The
canonical textbook range for atmospheric CCN (Wallace & Hobbs 2nd
ed., Pruppacher & Klett 1997, Rogers & Yau) is m_s = 10^-16 to
10^-14 g ("large" to "giant" CCN), which gives realistic activation
peaks at S - 1 ~ 0.04 to 0.4 percent. This script uses the
canonical literature range; the caption mass range should be
corrected to match.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/kohler_curves.avif"

# Constants
SIGMA_W = 0.0728       # N/m surface tension of water at 273 K
RHO_W = 1000.0         # kg/m^3
R_V = 461.5            # J/kg/K specific gas constant of water vapour
T = 273.0              # K
M_W = 18.015e-3        # kg/mol
M_NACL = 58.44e-3      # kg/mol
I_VH = 2.0             # van't Hoff factor for NaCl (full dissociation)


def kelvin_A(T: float) -> float:
    return 2.0 * SIGMA_W / (RHO_W * R_V * T)


def raoult_B(m_s_kg: float) -> float:
    """B for solute mass m_s (kg) as solute particle dissolved in droplet."""
    return 3.0 * I_VH * M_W * m_s_kg / (4.0 * np.pi * RHO_W * M_NACL)


def make_plot() -> Path:
    apply_style()
    A = kelvin_A(T)
    r_um = np.logspace(-2, 1, 600)
    r = r_um * 1e-6  # m

    fig, ax = plt.subplots(figsize=(8.5, 5.6))

    # Pure-water Kelvin curve
    S_kelvin = 1.0 + A / r
    ax.plot(r_um, (S_kelvin - 1.0) * 100, "k--", lw=1.8,
            label="Pure water (Kelvin / homogeneous)")

    # Three CCN masses (literature canonical range, in grams)
    masses_g = [
        (1e-16, "Small CCN ($m_s = 10^{-16}$ g)", "#9467bd"),
        (1e-15, "Medium CCN ($m_s = 10^{-15}$ g)", "#1f77b4"),
        (1e-14, "Large CCN ($m_s = 10^{-14}$ g)", "#2ca02c"),
    ]
    for m_g, label, color in masses_g:
        m_kg = m_g * 1e-3
        B = raoult_B(m_kg)
        S = 1.0 + A / r - B / r ** 3
        # Plot only positive supersaturation region for clarity
        ax.plot(r_um, (S - 1.0) * 100, color=color, lw=2.0, label=label)
        # Activation peak (max of S-1)
        idx = np.argmax(S - 1.0)
        ax.plot(r_um[idx], (S[idx] - 1.0) * 100, "o", color=color, ms=8,
                mec="black", mew=0.5, zorder=5)

    # Annotation for activation peak
    ax.annotate(r"Activation peaks  $(r_*, S^*)$",
                xy=(0.6, 0.13), xytext=(2.2, 0.6),
                fontsize=10, ha="left",
                arrowprops=dict(arrowstyle="-", color="0.4", lw=0.6))

    ax.text(0.012, 1.3, "Kelvin curve\nrises off-frame", color="0.3",
            fontsize=9)

    ax.axhline(0, color="0.6", lw=0.5)
    ax.set_xscale("log")
    ax.set_xlim(1e-2, 1e1)
    ax.set_ylim(-0.3, 1.6)
    ax.set_xlabel(r"Droplet radius $r$  [$\mu$m]")
    ax.set_ylabel(r"Supersaturation  $S - 1$  [%]")
    ax.set_title("Köhler curves: equilibrium supersaturation of solution droplets")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=True, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
