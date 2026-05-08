"""Generate Fig. (`fig:visviva`).

Orbital speed v(r) from the vis-viva equation, plotted for Earth and
Halley's comet to contrast a near-circular and a highly eccentric
orbit.

  v(r) = sqrt( G M_sun (2/r - 1/a) )

Caption / figure id : `fig:visviva`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : (none — derived from physical constants)

Orbital parameters are static and tabulated in
`data/visviva_orbits.json` next to this script.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "visviva_orbits.json"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/visviva_earth_halley.avif"

# Physical constants (SI units)
G = 6.67430e-11
M_SUN = 1.98892e30
AU = 1.495978707e11

# Orbits to plot. Source values as recorded in the JSON sidecar:
#   Earth          a = 1 AU,        e = 0.01671 (NASA Fact Sheet, Williams 2024)
#   Halley's comet a = 17.834 AU,   e = 0.9671  (JPL Small-Body Database, 2024)
ORBITS = {
    "Earth":          {"a_AU": 1.0,    "e": 0.01671, "color": "#1f77b4"},
    "Halley's comet": {"a_AU": 17.834, "e": 0.9671,  "color": "#d62728"},
}


def write_metadata() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. fig:visviva: orbital speed from vis-viva for Earth and Halley's comet.",
        "constants_SI": {
            "G": 6.67430e-11,
            "M_sun_kg": 1.98892e30,
            "AU_m": 1.495978707e11,
        },
        "orbits": {
            "Earth":          {"a_AU": 1.0,    "e": 0.01671,
                               "source": "NASA Planetary Fact Sheet (Williams 2024)"},
            "Halley's comet": {"a_AU": 17.834, "e": 0.9671,
                               "source": "JPL Small-Body Database, accessed 2026"},
        },
        "license_note": "Derived from public physical constants and orbital parameters.",
    }, indent=2))


def vis_viva(r_au: np.ndarray, a_au: float) -> np.ndarray:
    """Return v(r) in km/s given r and a in AU."""
    r = r_au * AU
    a = a_au * AU
    v_m_s = np.sqrt(G * M_SUN * (2.0 / r - 1.0 / a))
    return v_m_s / 1000.0


def make_plot() -> Path:
    apply_style()
    write_metadata()

    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    for name, p in ORBITS.items():
        a, e = p["a_AU"], p["e"]
        r_peri = a * (1 - e)
        r_apo = a * (1 + e)
        r = np.linspace(r_peri, r_apo, 400)
        v = vis_viva(r, a)
        ax.plot(r, v, color=p["color"], lw=2.0, label=f"{name} ($e={e:.3f}$)")
        # peri/apo markers
        ax.plot([r_peri, r_apo], [vis_viva(np.array([r_peri, r_apo]), a)[0],
                                   vis_viva(np.array([r_peri, r_apo]), a)[1]],
                "o", color=p["color"], markeredgecolor="black",
                markersize=8, zorder=5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"Heliocentric distance $r$ (AU)")
    ax.set_ylabel(r"Orbital speed $v$ (km s$^{-1}$)")
    ax.set_xlim(0.01, 50)
    ax.set_ylim(0.5, 200)
    ax.grid(which="both", linestyle=":", alpha=0.3)
    ax.legend(loc="upper right", frameon=False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
