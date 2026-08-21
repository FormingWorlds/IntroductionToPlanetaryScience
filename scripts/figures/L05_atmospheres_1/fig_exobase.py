"""Generate Fig. (`fig:exobase`).

The exobase as the altitude where the mean free path l = 1 / (sigma n)
equals the pressure scale height H = k_B T / (m g) in Earth's upper
atmosphere. Below the crossing the atmosphere is collisional
(thermosphere); above it the atmosphere is effectively collisionless
(exosphere) and ballistic trajectories carry molecules to escape.

Crossing altitude is approximately 450-500 km for present-day Earth.

Caption / figure id : `fig:exobase`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md

Number-density profile combines the USSA76 model below 86 km (which
extrapolates to ~10^19 m^-3 at 86 km) with an isothermal-thermosphere
n(z) = n_86 * exp(-(z - 86) / H_avg) above. We use an effective
sigma = 1e-18 m^2 (per the caption). H is computed for atomic O
(m = 16 amu) at T_thermo = 1000 K.

Note: this is an analytic representation, not a direct re-tabulation
of MSIS-86. The crossing altitude (z_exo ~ 450 km) and the
qualitative shape are robust to MSIS / USSA differences for the
educational point.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/exobase_definition.avif"

K_B = 1.380649e-23     # J/K
AMU = 1.66054e-27      # kg
G_SURF = 9.81          # m/s^2 (lower atmosphere)
R_EARTH = 6371e3       # m
SIGMA = 1.0e-18        # m^2 (caption value)

# Lower atmosphere (USSA76-like) anchor: at z = 86 km, n ~ 8e18 m^-3
N_86 = 8.0e18
T_LOWER = 220.0     # K (mesopause T)
T_THERMO = 1000.0   # K (quiet-sun thermosphere)


def gravity(z_km: float) -> float:
    r = R_EARTH + z_km * 1e3
    return G_SURF * (R_EARTH / r) ** 2


# NRLMSIS/MSIS-86-style reference number-density anchors (m^-3) for
# quiet-Sun mid-latitude conditions. Interpolated log-linearly between
# anchors to mimic the profile that the lecture caption assumes.
N_ANCHORS_KM = np.array([
      0,   10,   20,   50,   86,  100,  150,  200,  300,
    400,  500,  600,  700,  800])
N_ANCHORS_DEN = np.array([
    2.55e25, 8.6e24, 1.8e24, 2.1e22, 8.0e18, 1.2e18, 5.0e16, 8.0e15, 4.0e14,
    5.0e13, 1.0e13, 3.0e12, 1.2e12, 5.0e11])


def number_density(z_km: np.ndarray) -> np.ndarray:
    """Log-linear interpolation through MSIS-86 reference anchors."""
    log_n = np.interp(z_km, N_ANCHORS_KM, np.log(N_ANCHORS_DEN))
    return np.exp(log_n)


def scale_height(z_km: np.ndarray) -> np.ndarray:
    """H(z) in km. Lower-atmosphere ~ 7-8 km, thermosphere computed from
    Bates-Walker T(z) with mean mass varying from N2 at 86 km to O at
    400+ km."""
    H = np.zeros_like(z_km, dtype=float)
    lower = z_km <= 86
    H[lower] = 7.0
    above = z_km > 86
    if np.any(above):
        z_t = z_km[above]
        T_z = T_THERMO - (T_THERMO - T_LOWER) * np.exp(-0.025 * (z_t - 86))
        m_z = 28.0 * AMU * np.exp(-(z_t - 86) / 250) + \
              16.0 * AMU * (1 - np.exp(-(z_t - 86) / 250))
        g = np.array([gravity(zi) for zi in z_t])
        H[above] = K_B * T_z / (m_z * g) * 1e-3
    return H


def make_plot() -> Path:
    apply_style()
    z = np.linspace(100, 800, 500)
    n = number_density(z)
    ell_km = 1.0 / (SIGMA * n) * 1e-3  # mean free path in km
    H_km = scale_height(z)

    fig, ax = plt.subplots(figsize=(8.5, 7.0))

    # Find crossing: ell = H
    ratio = ell_km / H_km
    idx_cross = np.argmin(np.abs(np.log(ratio)))
    z_exo = z[idx_cross]
    H_exo = H_km[idx_cross]

    # Shading
    ax.axhspan(z[0], z_exo, color="#dbe5f3", alpha=0.4, zorder=0)
    ax.axhspan(z_exo, z[-1], color="#fde6c8", alpha=0.4, zorder=0)
    ax.text(1e-3, (z[0] + z_exo) / 2, "Thermosphere\n(collisional)",
            color="#3a4f6f", fontsize=11, style="italic", va="center")
    # Left of the mean-free-path curve, below the legend
    ax.text(1e-3, (z_exo + z[-1]) / 2,
            "Exosphere\n(collisionless,\nballistic trajectories)",
            color="#a14a25", fontsize=11, style="italic", va="center",
            ha="left")

    ax.plot(ell_km, z, color="#1f77b4", lw=2.5, label=r"Mean free path $\ell$")
    ax.plot(H_km, z, color="#d62728", lw=2.0, linestyle="--",
            label=r"Scale height $H$")

    # Crossing marker
    ax.plot(H_exo, z_exo, "o", color="black", ms=8, zorder=5)
    ax.annotate(f"Exobase\n$z_{{\\rm exo}} \\approx {z_exo:.0f}$ km",
                xy=(H_exo, z_exo), xytext=(H_exo * 4, z_exo - 60),
                fontsize=11,
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8))

    ax.set_xscale("log")
    ax.set_xlim(1e-4, 1e5)
    ax.set_ylim(100, 800)
    ax.set_xlabel("Length scale (km)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title(r"Exobase definition: $\ell = H$ in Earth's upper atmosphere")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    # Upper left: the mean-free-path curve occupies the upper right and
    # both profiles stay clear of this corner.
    ax.legend(loc="upper left", frameon=True, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
