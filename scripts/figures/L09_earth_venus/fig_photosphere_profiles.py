"""Generate Fig. (`fig:photosphere-profiles`): the infrared photosphere of a
saturated steam atmosphere for four surface temperatures.

Left panel: temperature against altitude. A saturated pure-steam column in
hydrostatic balance follows z(T) = (L/g) ln(T_s/T), so the column of a warmer
surface reaches higher, and the photosphere (the level where p = g/kappa)
climbs with T_s while its temperature stays at T_phot. The inset shows the
consequence: the emitted flux sigma T_phot^4 is the same for every surface
temperature, which is the Simpson-Nakajima limit of the grey model.

Right panel: pressure against temperature. Every column lies on the same
Clausius-Clapeyron saturation curve; the photosphere pressure g/kappa is a
horizontal line, and the two cross at one point, so T_phot does not depend on
the surface temperature.

Constants follow the Lecture 9 board derivation and Worksheet 5: L = 2.5e6
J/kg, R_v = 461 J/(kg K), (p_ref, T_ref) = (611 Pa, 273 K), kappa = 0.05
m^2/kg, g = 10 m/s^2. The constant-L saturation curve overestimates p_sat by
about 23 percent at the normal boiling point and by more above it, so the
surface pressures on the right panel are model values, not steam-table values.

Caption / figure id : `fig:photosphere-profiles`
Markdown source     : book/09_earth_venus/earth_venus.md
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/09_earth_venus/figures/photosphere_profiles.avif"

L_VAP = 2.5e6      # J/kg, latent heat of vaporisation
R_V = 461.0        # J/(kg K), gas constant of water vapour
P_REF = 611.0      # Pa, reference pressure of the saturation curve
T_REF = 273.0      # K, reference temperature, rounded as in the notes and Worksheet 5
KAPPA = 5e-2       # m^2/kg, grey infrared opacity of water vapour
G_SURF = 10.0      # m/s^2
SIGMA_SB = 5.670e-8  # W/(m^2 K^4)

T_SURFACES = [290.0, 320.0, 350.0, 400.0]  # K
COLORS = ["#4c72b0", "#55a868", "#dd8452", "#c44e52"]
T_TOP = 220.0      # K, where the plotted columns stop


def p_sat(T):
    """Saturation vapour pressure from the integrated Clausius-Clapeyron relation.

    Parameters
    ----------
    T : float or numpy.ndarray
        Temperature in K.

    Returns
    -------
    float or numpy.ndarray
        Saturation vapour pressure in Pa.
    """
    return P_REF * np.exp(-(L_VAP / R_V) * (1.0 / np.asarray(T, dtype=float) - 1.0 / T_REF))


def t_sat(p):
    """Temperature at which saturated water vapour has pressure p.

    Parameters
    ----------
    p : float or numpy.ndarray
        Pressure in Pa.

    Returns
    -------
    float or numpy.ndarray
        Saturation temperature in K, the inverse of `p_sat`.
    """
    return 1.0 / (1.0 / T_REF - (R_V / L_VAP) * np.log(np.asarray(p, dtype=float) / P_REF))


def altitude_km(T, T_s):
    """Altitude of temperature T in a saturated steam column over a surface at T_s.

    Hydrostatic balance with p = p_sat(T) at every level gives
    z = (L/g) ln(T_s/T), valid for T <= T_s.

    Parameters
    ----------
    T : float or numpy.ndarray
        Temperature in K.
    T_s : float
        Surface temperature in K.

    Returns
    -------
    float or numpy.ndarray
        Altitude in km.
    """
    return (L_VAP / G_SURF) * np.log(T_s / np.asarray(T, dtype=float)) / 1e3


# Derived photosphere quantities, exposed for checks and for the caption
P_PHOT = G_SURF / KAPPA            # Pa
T_PHOT = float(t_sat(P_PHOT))      # K
F_OLR = SIGMA_SB * T_PHOT**4       # W/m^2

assert abs(p_sat(T_PHOT) - P_PHOT) < 1e-6 * P_PHOT
assert all(T_s > T_PHOT for T_s in T_SURFACES), "every column must reach above the photosphere"


def make_plot() -> Path:
    apply_style()
    n_col = len(T_SURFACES)
    widths = np.linspace(1.4, 6.0, n_col)  # thin for the coolest, thick for the warmest surface

    fig, (ax_z, ax_p) = plt.subplots(1, 2, figsize=(7.22, 3.7))

    # ── Left: temperature against altitude ─────────────────────────────
    for T_s, col in zip(T_SURFACES, COLORS):
        T = np.linspace(T_s, T_TOP, 300)
        ax_z.plot(T, altitude_km(T, T_s), color=col, lw=1.8)
        ax_z.plot(T_s, 0.0, "s", color=col, ms=5, zorder=4, clip_on=False)
        z_phot = float(altitude_km(T_PHOT, T_s))
        ax_z.plot(T_PHOT, z_phot, "o", color=col, ms=6, zorder=4)
        ax_z.annotate("", xy=(T_PHOT, z_phot + 14), xytext=(T_PHOT, z_phot + 2),
                      arrowprops=dict(arrowstyle="->", color=col, lw=1.2))

    ax_z.axvline(T_PHOT, color="0.45", ls="--", lw=0.9, zorder=1)
    # In the band above every column, between the dashed line and the legend
    ax_z.text(T_PHOT + 7, 168, rf"$T_\mathrm{{phot}} = {T_PHOT:.0f}$ K",
              ha="left", va="center", fontsize=8, color="0.3")
    ax_z.set_xlim(215, 410)
    ax_z.set_ylim(0, 178)
    ax_z.set_xlabel("Temperature (K)")
    ax_z.set_ylabel("Altitude (km)")
    ax_z.set_title("The photosphere climbs with $T_s$", fontsize=11)
    handles = [Line2D([], [], color=c, lw=1.8, label=rf"$T_s$ = {T:.0f} K")
               for T, c in zip(T_SURFACES, COLORS)]
    handles += [Line2D([], [], ls="", marker="s", color="0.4", ms=5, label="surface"),
                Line2D([], [], ls="", marker="o", color="0.4", ms=6, label="photosphere")]
    ax_z.legend(handles=handles, loc="upper right", frameon=False, fontsize=8,
                handlelength=1.3, handletextpad=0.5, labelspacing=0.35, borderaxespad=0.2)

    # Inset: the emitted flux against surface temperature is flat
    ax_in = ax_z.inset_axes([0.63, 0.29, 0.35, 0.20])
    ax_in.axhline(F_OLR, color="0.45", lw=1.2)
    for T_s, col in zip(T_SURFACES, COLORS):
        ax_in.plot(T_s, F_OLR, "o", color=col, ms=5, zorder=3)
    ax_in.set_xlim(280, 410)
    ax_in.set_ylim(F_OLR - 60, F_OLR + 60)
    ax_in.set_xticks([300, 350, 400])
    ax_in.set_yticks([F_OLR])
    ax_in.set_yticklabels([f"{F_OLR:.0f}"])
    ax_in.tick_params(labelsize=7.5, length=2, pad=1.5)
    ax_in.set_xlabel("$T_s$ (K)", fontsize=7.5, labelpad=1)
    ax_in.set_title(r"emitted flux $\sigma T_\mathrm{phot}^4$ (W m$^{-2}$)", fontsize=7.5, pad=2)
    ax_in.grid(False)

    # ── Right: pressure against temperature ────────────────────────────
    # Every column is a segment of the one saturation curve, from its surface
    # to the top; nested widths keep all four visible where they overlap
    for T_s, col, lw in zip(T_SURFACES[::-1], COLORS[::-1], widths[::-1]):
        T = np.linspace(T_TOP, T_s, 300)
        ax_p.plot(T, p_sat(T), color=col, lw=lw, solid_capstyle="butt", zorder=2)
        ax_p.plot(T_s, p_sat(T_s), "s", color=col, ms=5, zorder=4)
        ax_p.text(T_s + 13, p_sat(T_s) * 0.8, rf"$T_s = {T_s:.0f}$ K", ha="left",
                  va="center", fontsize=9, color=col)

    ax_p.axhline(P_PHOT, color="0.45", ls="--", lw=0.9, zorder=1)
    ax_p.text(436, P_PHOT * 1.7, rf"$\tau = 1$: $p = g/\kappa = {P_PHOT:.0f}$ Pa",
              ha="right", va="center", fontsize=9, color="0.3")
    ax_p.plot(T_PHOT, P_PHOT, "o", color="black", ms=7, zorder=5)
    ax_p.annotate(
        "photosphere, the same\npoint for every column",
        xy=(T_PHOT + 4, P_PHOT * 0.9), xytext=(300, 45),
        ha="left", va="center", fontsize=9, color="0.3",
        arrowprops=dict(arrowstyle="-", color="0.6", lw=0.6),
    )
    T_lab = 232.0
    ax_p.annotate(
        "saturation curve:\nevery column lies on it",
        xy=(T_lab, p_sat(T_lab)), xytext=(262, 7),
        ha="left", va="center", fontsize=9, color="0.3",
        arrowprops=dict(arrowstyle="-", color="0.6", lw=0.6),
    )
    ax_p.set_yscale("log")
    ax_p.set_ylim(1.2e6, 3)
    ax_p.set_xlim(215, 440)
    ax_p.set_xlabel("Temperature (K)")
    ax_p.set_ylabel("Pressure (Pa)")
    ax_p.set_title("Its temperature is pinned", fontsize=11)

    fig.tight_layout(w_pad=2.0)
    return save_figure(fig, OUT_AVIF, avif_quality=80, dpi=280)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")
    print(f"  photosphere: p = {P_PHOT:.0f} Pa, T = {T_PHOT:.2f} K, flux = {F_OLR:.1f} W/m^2")


if __name__ == "__main__":
    main()
