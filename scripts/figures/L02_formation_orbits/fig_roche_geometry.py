"""Generate Fig. (`fig:roche-geometry`).

Two-panel Roche-limit figure:
(a) Cartoon of a fluid satellite at a safe orbital distance (rounded)
    versus at the Roche limit (stretched along the planet-satellite
    line). Annotates the fluid Roche-limit formula.
(b) Tidal acceleration across a 200 km icy body and the body's
    surface self-gravity, plotted against orbital distance from
    Saturn (in units of R_p). The curve crossing defines the
    *rigid* Roche limit at d_R ≈ 1.11 R_p for ρ_s = 1000 kg/m^3
    (i.e. d = R_p (2 ρ_p / ρ_s)^(1/3)). The *fluid* Roche limit at
    d_R ≈ 2.17 R_p (using the 2.46 prefactor) is drawn as a
    separate dotted vertical line; tidal stretching of a fluid body
    becomes catastrophic well before the rigid-body crossover.

Saturn primary used as a concrete example so the figure is consistent
with the body text. All values derived from public physical
constants and the Saturn Fact Sheet.

Caption / figure id : `fig:roche-geometry`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : NASAFactSheet
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "roche_geometry_inputs.json"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/roche_geometry.avif"

# Physical constants (SI)
G = 6.67430e-11

# Saturn primary (JPL Solar System Dynamics)
M_SATURN = 5.6834e26   # kg
R_SATURN = 58_232.0e3  # m, volumetric mean radius
RHO_SATURN = 687.0     # kg/m^3 (mean)

# Test satellite: 200 km icy body, density 1000 kg/m^3
R_SAT = 200.0e3
RHO_SAT = 1000.0


def write_metadata() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. fig:roche-geometry: tidal acceleration vs self-gravity for an icy body around Saturn",
        "primary": {
            "body": "Saturn",
            "M_kg": M_SATURN,
            "R_m": R_SATURN,
            "mean_density_kg_m3": RHO_SATURN,
            "source": "JPL Solar System Dynamics",
        },
        "satellite": {
            "kind": "Icy body",
            "R_m": R_SAT,
            "density_kg_m3": RHO_SAT,
            "note": "Representative ice density used in body text.",
        },
        "constants_SI": {"G": G},
        "expected_fluid_Roche_R_p": 2.46 * (RHO_SATURN / RHO_SAT) ** (1.0 / 3.0),
        "license_note": "Derived from public physical constants and Saturn Fact Sheet.",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    write_metadata()

    fig, (ax_geom, ax_acc) = plt.subplots(1, 2, figsize=(11, 4.5))

    # ------- Panel (a): cartoon -------
    ax_geom.set_aspect("equal")

    # Primary
    primary = mpatches.Circle((0, 0), 0.55, color="#f4c542",
                              ec="#a87f1d", lw=1.2)
    ax_geom.add_patch(primary)
    ax_geom.text(0, 0, "Primary", ha="center", va="center", fontsize=10)

    # Roche-limit dashed circle
    d_R = 2.46  # in units of R_p (visual; the (rho_p/rho_s)^1/3 factor for
                # this cartoon's chosen densities is exactly 1 by design)
    theta = np.linspace(0, 2 * np.pi, 200)
    ax_geom.plot(d_R * np.cos(theta), d_R * np.sin(theta),
                 color="#d62728", lw=1.0, linestyle="--")

    # Safe satellite (rounded), placed OUTSIDE the Roche circle
    safe = mpatches.Circle((2.35, 2.0), 0.25, color="#a8c8ff",
                           ec="#1f4f99", lw=1.0)
    ax_geom.add_patch(safe)
    ax_geom.annotate("Safe distance\n(spherical)", xy=(2.35, 2.0),
                     xytext=(2.9, 1.35), fontsize=9, ha="center",
                     bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))

    # Stretched satellite at Roche limit
    stretched = mpatches.Ellipse((d_R, -0.05), 0.6, 0.22,
                                 color="#a8c8ff", ec="#1f4f99", lw=1.0)
    ax_geom.add_patch(stretched)
    # Tidal-stretching arrows
    ax_geom.annotate("", xy=(d_R + 0.45, -0.05), xytext=(d_R + 0.05, -0.05),
                     arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.5))
    ax_geom.annotate("", xy=(d_R - 0.45, -0.05), xytext=(d_R - 0.05, -0.05),
                     arrowprops=dict(arrowstyle="->", color="#d62728", lw=1.5))

    ax_geom.text(d_R, -0.55, "At Roche limit $d_R$\n(stretched, breaks up)",
                 ha="center", fontsize=9,
                 bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    ax_geom.text(-2.6, 2.45, r"$d_R \approx 2.46\,R_p\,(\rho_p/\rho_s)^{1/3}$",
                 fontsize=10, color="#a83232",
                 bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))
    ax_geom.text(-2.6, 2.08,
                 r"(dashed circle: equal-density case $\rho_p = \rho_s$)",
                 fontsize=8, color="#a83232", style="italic",
                 bbox=dict(facecolor="white", edgecolor="none", alpha=0.9))

    ax_geom.set_xlim(-3.0, 3.5)
    ax_geom.set_ylim(-2.0, 2.7)
    ax_geom.set_xticks([])
    ax_geom.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax_geom.spines[s].set_visible(False)
    ax_geom.set_title("(a) Tidal geometry near the Roche limit")

    # ------- Panel (b): tidal acceleration vs self-gravity -------
    d_over_R = np.linspace(1.0, 30.0, 600)
    d_m = d_over_R * R_SATURN
    tidal_accel = 2.0 * G * M_SATURN * R_SAT / d_m ** 3
    g_self = G * (4.0 / 3.0) * np.pi * RHO_SAT * R_SAT  # surface self-gravity

    ax_acc.plot(d_over_R, tidal_accel, color="#1f77b4", lw=2.0,
                label=r"Tidal $\Delta a$ across satellite")
    ax_acc.axhline(g_self, color="black", lw=1.0, linestyle="--",
                   label=r"Satellite self-gravity $g_\text{self}$")

    # The crossing of tidal_accel and g_self defines the **rigid** Roche
    # limit at d_R^rigid = R_p (2 rho_p/rho_s)^{1/3} ~ 1.11 R_p for these
    # densities. The textbook **fluid** Roche limit uses a 2.46 prefactor
    # in place of 2^{1/3}, and is the value cited in the body text.
    d_R_fluid = 2.46 * (RHO_SATURN / RHO_SAT) ** (1.0 / 3.0)
    ax_acc.axvline(d_R_fluid, color="#d62728", lw=1.0, linestyle=":",
                   label=fr"Fluid Roche limit ($d_R = {d_R_fluid:.2f}\,R_p$)")

    ax_acc.set_yscale("log")
    ax_acc.set_xscale("log")
    ax_acc.set_xlabel(r"Orbital distance $d / R_p$")
    ax_acc.set_ylabel(r"Acceleration (m s$^{-2}$)")
    ax_acc.set_xlim(1.0, 30.0)
    ax_acc.set_ylim(1e-5, 1e-1)
    ax_acc.set_title(r"(b) Tidal vs self-gravity, $R_s = 200$ km icy body, Saturn primary")
    ax_acc.grid(which="both", linestyle=":", alpha=0.3)
    ax_acc.legend(loc="lower left", frameon=False, fontsize=9)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
