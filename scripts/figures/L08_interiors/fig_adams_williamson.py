"""Generate Fig. (`fig:adams-williamson`).

Two-panel test of the Adams-Williamson relation against PREM.

(a) Lower mantle (771-2741 km depth), where composition is
approximately uniform: integrating

    d ln rho / dr = -g / phi,   phi = K_S / rho = v_P^2 - (4/3) v_S^2

reproduces PREM well; the density rise is dominated by self-
compression.

(b) Across the core-mantle boundary at 2891 km depth: PREM jumps
from ~5570 to ~9900 kg/m^3, while a no-composition-change
Adams-Williamson extrapolation predicts a smooth, much smaller
increase. The deviation directly exposes the silicate -> Fe-alloy
compositional change.

Caption / figure id : `fig:adams-williamson`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Dziewonski1981

PREM tabulator in `_prem.py`. We integrate dlnrho/dr along the
PREM-defined seismic parameter phi, using PREM density at the start
of the integration as the boundary condition.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure
from scripts.figures.L08_interiors._prem import prem_at_depth, R_EARTH


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/adams_williamson.avif"

G_NEWTON = 6.6743e-11      # m^3 / kg / s^2
M_EARTH = 5.972e24         # kg


def gravity_at_depth(z_km: np.ndarray) -> np.ndarray:
    """Return g(r) [m/s^2]. Use simple m(r) approximation by
    integrating PREM density (in SI) inward from the surface."""
    z_grid = np.linspace(0, 6371, 6372)  # 1 km resolution
    rho_g_per_cm3, _, _ = prem_at_depth(z_grid)
    rho_si = rho_g_per_cm3 * 1000.0  # kg/m^3
    r_grid = (R_EARTH - z_grid) * 1000.0  # m
    # Integrate mass(r) from centre outward
    # m(r) = sum 4 pi r^2 rho dr  (use trapezoidal in r, ascending)
    r_asc = r_grid[::-1]
    rho_asc = rho_si[::-1]
    dr = np.diff(r_asc)
    shell_mass = 4 * np.pi * (0.5 * (r_asc[:-1] + r_asc[1:])) ** 2 \
                 * 0.5 * (rho_asc[:-1] + rho_asc[1:]) * dr
    m_asc = np.concatenate([[0.0], np.cumsum(shell_mass)])
    # g(0) is set to zero explicitly; dividing there would be 0/0.
    g_asc = np.zeros_like(r_asc)
    np.divide(G_NEWTON * m_asc, r_asc ** 2, out=g_asc, where=r_asc > 0)
    g_at_depth_grid = g_asc[::-1]  # back to descending depth
    # Interpolate to caller's depth
    return np.interp(z_km, z_grid, g_at_depth_grid)


def aw_integrate(z_km, rho_start, debug_label=""):
    """Integrate dlnrho/dz = +g / phi along z from shallow to deep.
    (note +g because dz = -dr; phi already in (km/s)^2 = (1000 m/s)^2.)"""
    rho_g, vP, vS = prem_at_depth(z_km)
    # phi in m^2/s^2 (vP, vS are km/s; multiply by 1e3)
    phi = (vP * 1e3) ** 2 - (4.0 / 3.0) * (vS * 1e3) ** 2
    g = gravity_at_depth(z_km)
    # integrate dlnrho/dz_m = g / phi (rising rho with depth)
    z_m = z_km * 1000.0
    dlnrho_dz = g / phi
    lnrho = np.zeros_like(z_km, dtype=float)
    lnrho[0] = np.log(rho_start)
    for i in range(1, len(z_km)):
        lnrho[i] = lnrho[i - 1] + 0.5 * (dlnrho_dz[i - 1] + dlnrho_dz[i]) \
                                     * (z_m[i] - z_m[i - 1])
    return np.exp(lnrho)


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.5, 5.5))

    # Panel (a): lower mantle 771 - 2741 km
    z_a = np.linspace(771, 2741, 240)
    rho_a_prem_g, _, _ = prem_at_depth(z_a)
    rho_a_prem = rho_a_prem_g * 1000.0  # kg/m^3
    rho_a_aw = aw_integrate(z_a, rho_start=rho_a_prem[0])
    ax_a.plot(rho_a_prem, z_a, color="#1f77b4", lw=2.0,
              label="PREM (observed)")
    ax_a.plot(rho_a_aw, z_a, color="#d62728", lw=1.8, linestyle="--",
              label="Adams-Williamson prediction")
    ax_a.invert_yaxis()
    ax_a.set_xlabel(r"Density $\rho$ (kg m$^{-3}$)")
    ax_a.set_ylabel("Depth (km)")
    ax_a.set_title("(a) Lower mantle: approximately uniform composition")
    # Lower left: density increases with depth, so the deep low-density
    # corner holds no curve and no text box.
    ax_a.legend(loc="lower left", frameon=True, fontsize=10)
    ax_a.grid(linestyle=":", alpha=0.3)
    # Below-left of the curve: density rises with depth, so this
    # triangle holds no curve, and the box clears the axis tick labels.
    ax_a.text(4550, 2150, "AW reproduces PREM well\n"
              "(compositional gradient small)",
              fontsize=9, color="0.3",
              bbox=dict(facecolor="#f6f4e6", edgecolor="0.7", pad=4))

    # Panel (b): across the CMB
    # Build PREM curve from 2200 to 4000 km (spans CMB at 2891 km)
    z_b_above = np.linspace(2200, 2890.0, 80)
    z_b_below = np.linspace(2891.5, 4000, 120)
    rho_b_above_g, _, _ = prem_at_depth(z_b_above)
    rho_b_below_g, _, _ = prem_at_depth(z_b_below)
    rho_b_above = rho_b_above_g * 1000.0
    rho_b_below = rho_b_below_g * 1000.0

    ax_b.plot(rho_b_above, z_b_above, color="#1f77b4", lw=2.0,
              label="PREM (observed)")
    ax_b.plot(rho_b_below, z_b_below, color="#1f77b4", lw=2.0)

    # AW extrapolation continued straight through CMB (no compositional change)
    # Start at PREM density just above CMB and integrate through to 4000 km.
    z_b_aw = np.linspace(2200, 4000, 360)
    # Use PREM seismic parameter from the mantle side throughout (no jump),
    # since AW assumes uniform composition. To do this we evaluate PREM seismic
    # parameter at z<CMB and extrapolate it linearly into z>CMB.
    z_above_only = np.linspace(2200, 2890, 200)
    _, vP_a, vS_a = prem_at_depth(z_above_only)
    phi_above = (vP_a * 1e3) ** 2 - (4.0 / 3.0) * (vS_a * 1e3) ** 2
    # Linear extrapolation of phi vs depth into the core region
    coef = np.polyfit(z_above_only, phi_above, 1)

    def phi_aw(z):
        return np.polyval(coef, z)

    g = gravity_at_depth(z_b_aw)
    z_m = z_b_aw * 1000.0
    rho_aw_b = np.zeros_like(z_b_aw)
    rho_aw_b[0] = rho_b_above[0]
    for i in range(1, len(z_b_aw)):
        dlnrho_dz = 0.5 * (g[i - 1] / phi_aw(z_b_aw[i - 1])
                           + g[i] / phi_aw(z_b_aw[i]))
        rho_aw_b[i] = rho_aw_b[i - 1] * np.exp(
            dlnrho_dz * (z_m[i] - z_m[i - 1]))

    ax_b.plot(rho_aw_b, z_b_aw, color="#d62728", lw=1.8, linestyle="--",
              label="AW (no composition change)")
    ax_b.axhline(2891, color="0.5", linestyle=":", lw=1.0)
    ax_b.text(7000, 2870, "CMB (2891 km)", color="0.4", fontsize=9,
              ha="center", va="bottom")

    ax_b.invert_yaxis()
    ax_b.set_xlabel(r"Density $\rho$ (kg m$^{-3}$)")
    ax_b.set_title("(b) Across the core-mantle boundary")
    # Upper right: the mantle-side curves sit at low density and the
    # core-side curves below the CMB line, so the shallow high-density
    # corner stays clear.
    ax_b.legend(loc="upper right", frameon=True, fontsize=10)
    ax_b.grid(linestyle=":", alpha=0.3)
    ax_b.set_xlim(4500, 12500)
    ax_b.annotate("Compositional jump\n(silicate -> Fe-alloy)",
                  xy=(8500, 2891), xytext=(8500, 3500),
                  fontsize=9, color="#a83232", ha="left",
                  arrowprops=dict(arrowstyle="->", color="#a83232", lw=1.0),
                  bbox=dict(facecolor="#fdf0f0", edgecolor="0.7", pad=4))

    fig.suptitle("Adams-Williamson relation: PREM density vs prediction "
                 r"$d\ln\rho/dr = -g/\phi$",
                 fontsize=12, y=1.02)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
