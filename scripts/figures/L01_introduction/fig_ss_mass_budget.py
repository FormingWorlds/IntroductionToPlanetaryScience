"""Generate Fig. 1.18 (`fig:ss-mass-budget`).

Mass budget of the solar system: a two-panel pie chart.
- Left panel: Sun vs total planetary mass.
- Right panel: planet masses, with the four terrestrial planets
  (Mercury, Venus, Earth, Mars) grouped into a single wedge so that
  the labels do not collide. Individual terrestrial contributions
  to total planetary mass are below 0.25% each.

Data are static (JPL Solar System Dynamics) and stored
verbatim in `data/solar_system_masses.csv` next to this script.
Update the CSV (and bump its sidecar JSON) only when planetary mass
values are formally revised.

Caption / figure id : Fig. 1.18 / `fig:ss-mass-budget`
Markdown source     : book/01_introduction/introduction.md
Citation key        : NASAFactSheet
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from scripts.figures._shared.style import (apply_style, save_figure,
                                           text_color_on)


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
CSV = DATA_DIR / "solar_system_masses.csv"
META = DATA_DIR / "solar_system_masses.json"
OUT_AVIF = REPO_ROOT / "book/01_introduction/figures/ss_mass_budget.avif"

# Solar mass: 1.98892e30 kg (CODATA 2018)
M_SUN_KG = 1.98892e30


def write_data() -> None:
    """Static data block. Written once; do not regenerate from secondary sources."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    rows = [
        # name, mass [Earth masses], notes
        ("Mercury",  0.0553,  ""),
        ("Venus",    0.815,   ""),
        ("Earth",    1.0,     "M_Earth = 5.9722e24 kg"),
        ("Mars",     0.107,   ""),
        ("Jupiter",  317.83,  ""),
        ("Saturn",    95.16,  ""),
        ("Uranus",    14.54,  ""),
        ("Neptune",   17.15,  ""),
    ]
    df = pd.DataFrame(rows, columns=["body", "mass_earth_units", "notes"])
    df.to_csv(CSV, index=False)
    META.write_text(json.dumps({
        "purpose": "Fig. 2.18 (fig:ss-mass-budget): solar system mass budget pie",
        "source": "JPL Solar System Dynamics",
        "source_url": "https://ssd.jpl.nasa.gov/planets/phys_par.html",
        "retrieved_date": "2026-04-23",
        "citation_key": "NASAFactSheet",
        "columns": {
            "body":              "Planet name (string).",
            "mass_earth_units":  "Planet mass in Earth masses (M_Earth = 5.9722e24 kg).",
            "notes":              "Free-form notes.",
        },
        "constants": {
            "M_sun_kg": M_SUN_KG,
            "M_earth_kg": 5.9722e24,
        },
        "license_note": "JPL Solar System Dynamics content is in the public domain (NASA).",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    if not CSV.exists():
        write_data()
    df = pd.read_csv(CSV)

    M_earth_kg = 5.9722e24
    df["mass_kg"] = df["mass_earth_units"] * M_earth_kg
    total_planet_kg = df["mass_kg"].sum()

    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))

    # Left: Sun vs all planets
    sun_pct = M_SUN_KG / (M_SUN_KG + total_planet_kg) * 100.0
    plt_pct = 100.0 - sun_pct
    axes[0].pie(
        [sun_pct, plt_pct],
        labels=[f"Sun\n{sun_pct:.2f}%", f"Planets\n{plt_pct:.2f}%"],
        colors=["#f4c542", "#5b8def"],
        startangle=90, counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.0},
        textprops={"fontsize": 11},
    )
    axes[0].set_title("Sun vs planets")

    # Right: among the planets. Terrestrials are grouped into a single
    # wedge because their individual contributions (Mercury 0.01%,
    # Venus 0.18%, Earth 0.22%, Mars 0.02%) are too small for separate
    # labels to remain legible at this scale. Wedge order is chosen so
    # that the four small wedges (Saturn, Neptune, Uranus, Terrestrials)
    # all sit on the right side of the pie and Jupiter occupies the
    # entire left half; this gives each small wedge enough angular
    # separation from its neighbours to carry a colour-coded label just
    # outside the wedge without any leader lines.
    import numpy as np
    terrestrials = {"Mercury", "Venus", "Earth", "Mars"}
    is_terrestrial = df["body"].isin(terrestrials)
    terr_pct = (df.loc[is_terrestrial, "mass_kg"].sum()
                / total_planet_kg * 100.0)
    giants = df[~is_terrestrial].copy()
    giants["pct"] = giants["mass_kg"] / total_planet_kg * 100.0
    pct_by = {row["body"]: row["pct"] for _, row in giants.iterrows()}

    # Explicit order around the pie: starting at 12 o'clock and going
    # clockwise, the small wedges come first (Saturn down to Terrestrials
    # on the right side), then Jupiter sweeps the whole bottom-left.
    order = ["Saturn", "Neptune", "Uranus", "Terrestrials", "Jupiter"]
    pct_by["Terrestrials"] = terr_pct
    right_sizes = [pct_by[n] for n in order]
    right_names = order
    # Colours match the wedge order above (Saturn, Neptune, Uranus,
    # Terrestrials, Jupiter).
    right_colors = ["#e09e58", "#3a87bd", "#76d6e2", "#d62728", "#bb6c44"]
    wedges, _ = axes[1].pie(
        right_sizes,
        labels=None,
        colors=right_colors,
        startangle=90, counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.0},
    )
    # Place labels: large wedges (>=10%) get the label inside the wedge,
    # black or white by contrast. Small wedges get a colour-coded label
    # just outside their own wedge, on the right side of the pie. No
    # leader lines.
    LARGE_PCT_INSIDE = 10.0
    for wedge, name, pct, colour in zip(wedges, right_names, right_sizes,
                                        right_colors):
        theta = np.deg2rad(0.5 * (wedge.theta1 + wedge.theta2))
        x_pie, y_pie = np.cos(theta), np.sin(theta)
        if pct >= LARGE_PCT_INSIDE:
            axes[1].text(0.62 * x_pie, 0.62 * y_pie,
                         f"{name}\n{pct:.1f}%",
                         ha="center", va="center", fontsize=11,
                         color=text_color_on(colour), weight="bold")
        else:
            label = (f"{name}  {pct:.2f}%" if name == "Terrestrials"
                     else f"{name}  {pct:.1f}%")
            axes[1].text(1.07 * x_pie, 1.07 * y_pie, label,
                         ha="left", va="center", fontsize=10,
                         color=colour, weight="bold")
    # Widen the right axes so the offset small-wedge labels stay visible.
    axes[1].set_xlim(-1.25, 1.65)
    axes[1].set_title("Among the planets")

    fig.suptitle("Mass budget of the solar system", fontsize=12, y=0.98)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    write_data()  # idempotent; refreshes sidecar metadata
    out = make_plot()
    print(f"  data : {CSV}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
