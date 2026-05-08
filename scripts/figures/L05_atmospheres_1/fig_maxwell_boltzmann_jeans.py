"""Generate Fig. (`fig:mb-jeans`).

Maxwell-Boltzmann speed distribution f(v) for atomic hydrogen at the
exobase temperatures of Earth (T_exo = 1000 K) and Mars
(T_exo = 270 K), with vertical dashed lines at the local escape
velocities (v_esc ~ 10.6 km/s for Earth, ~4.9 km/s for Mars at the
exobase ~500 km altitude). The high-speed tail above v_esc is the
Jeans escape population.

Caption / figure id : `fig:mb-jeans`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md

Earth: T_exo = 1000 K (Tian2009 / Catling-Kasting2017 quiet-sun
midpoint of 700-1500 K range).
Mars:  T_exo = 270 K (Tian2009 quiet-sun upper-thermosphere value;
matches the L05 caption).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/maxwell_boltzmann_jeans.avif"

# Constants
K_B = 1.380649e-23      # J/K
M_H = 1.6735575e-27     # kg, atomic hydrogen mass

# Per-body parameters (T_exo in K, v_esc at exobase in m/s)
BODIES = [
    ("Earth, $T_\\mathrm{exo} = 1000$ K", 1000.0, 10.6e3, "#1f77b4"),
    ("Mars, $T_\\mathrm{exo} = 270$ K",   270.0,   4.9e3, "#d62728"),
]


def maxwell_boltzmann(v: np.ndarray, T: float, m: float) -> np.ndarray:
    coef = 4.0 * np.pi * (m / (2 * np.pi * K_B * T)) ** 1.5
    return coef * v ** 2 * np.exp(-m * v ** 2 / (2 * K_B * T))


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(7.5, 5.0))

    v_kms = np.linspace(0.01, 25.0, 1200)
    v = v_kms * 1e3  # m/s

    for label, T, v_esc, color in BODIES:
        f = maxwell_boltzmann(v, T, M_H)  # SI units: per (m/s)
        # Display in units of 10^-3 / (m/s) to keep numbers O(0.1-0.4)
        f_disp = f * 1e3
        ax.plot(v_kms, f_disp, color=color, lw=2.0, label=label)
        # Shade the escape tail
        mask = v >= v_esc
        ax.fill_between(v_kms[mask], 0, f_disp[mask],
                        color=color, alpha=0.18)
        # Vertical line at v_esc; label placed near top of dashed line
        ax.axvline(v_esc / 1e3, color=color, linestyle="--", lw=1.0)
        # Stagger labels in y so the two don't collide on the same line
        y_label = 0.40 if T < 500 else 0.36
        ax.text(v_esc / 1e3 + 0.15, y_label,
                r"$v_{\mathrm{esc}}$", color=color, fontsize=11,
                va="top")

    # Annotation pointing to the high-speed tail
    ax.annotate("Jeans escape tail\n($v > v_{\\mathrm{esc}}$)",
                xy=(15.0, 0.005), xytext=(18.0, 0.06),
                fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", lw=0.8, color="0.4"))

    ax.set_xlim(0, 25)
    ax.set_ylim(0, 0.45)
    ax.set_xlabel(r"Speed (km s$^{-1}$)")
    ax.set_ylabel(r"Probability density $f(v)$  (10$^{-3}$ s m$^{-1}$)")
    ax.set_title("Maxwell-Boltzmann speed distribution: atomic H at the exobase")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=False, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
