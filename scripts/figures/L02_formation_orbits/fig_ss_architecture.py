"""Generate Fig. (`fig:ss-architecture`).

Architecture of the Solar System on a logarithmic semi-major-axis
scale: the eight planets plus Pluto as filled circles whose area
scales with log(1 + R/R_earth), the asteroid main belt and the
classical Kuiper Belt as shaded radial spans, and the 2.5-3.5 AU range
of the solar nebula's water snow line as a labelled band.

Caption / figure id : `fig:ss-architecture`
Markdown source     : book/02_formation_orbits/formation_orbits.md
Citation key        : NSSDCPlanetaryFactSheet (semi-major axes, radii)
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "ss_architecture_inputs.json"
OUT_AVIF = REPO_ROOT / "book/02_formation_orbits/figures/solar_system_architecture.avif"

# Semi-major axis (AU) and mean radius (Earth radii).
# Source: NASA NSSDCA Planetary Fact Sheet (Williams).
BODIES = {
    "Mercury": {"a": 0.387, "R": 0.383, "color": "#9c9c9c"},
    "Venus":   {"a": 0.723, "R": 0.949, "color": "#d4a373"},
    "Earth":   {"a": 1.000, "R": 1.000, "color": "#2a6fdb"},
    "Mars":    {"a": 1.524, "R": 0.532, "color": "#c1440e"},
    "Jupiter": {"a": 5.204, "R": 10.97, "color": "#c8a165"},
    "Saturn":  {"a": 9.573, "R": 9.14,  "color": "#e0c98f"},
    "Uranus":  {"a": 19.165, "R": 3.98, "color": "#9fd6d2"},
    "Neptune": {"a": 30.178, "R": 3.87, "color": "#4062bb"},
    "Pluto":   {"a": 39.482, "R": 0.186, "color": "#b0a190"},
}

ASTEROID_BELT = (2.1, 3.3)   # AU
KUIPER_BELT = (30.0, 50.0)   # AU, classical belt
SNOW_LINE = (2.5, 3.5)       # AU, solar-nebula H2O snow line range


def write_metadata() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. fig:ss-architecture: solar-system architecture on log semi-major axis.",
        "bodies": {k: {kk: v[kk] for kk in ("a", "R")} for k, v in BODIES.items()},
        "asteroid_belt_AU": ASTEROID_BELT,
        "kuiper_belt_AU": KUIPER_BELT,
        "snow_line_AU": SNOW_LINE,
        "symbol_scaling": "marker area proportional to log10(1 + R/R_earth)",
        "source": "NASA NSSDCA Planetary Fact Sheet (semi-major axes, mean radii)",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    write_metadata()

    fig, ax = plt.subplots(figsize=(9.5, 3.4))

    # Belts as shaded spans.
    ax.axvspan(*ASTEROID_BELT, color="#b5b5b5", alpha=0.35, zorder=1)
    ax.text(np.sqrt(ASTEROID_BELT[0] * ASTEROID_BELT[1]), 0.72,
            "asteroid\nbelt", ha="center", fontsize=9, color="#555555")
    ax.axvspan(*KUIPER_BELT, color="#b5c8d8", alpha=0.35, zorder=1)
    ax.text(np.sqrt(KUIPER_BELT[0] * KUIPER_BELT[1]), 0.72,
            "Kuiper Belt", ha="center", fontsize=9, color="#446")

    # Water snow line range of the solar nebula.
    ax.axvspan(*SNOW_LINE, color="#7ec8e3", alpha=0.30, zorder=2)
    ax.annotate(r"H$_2$O snow line" "\n" r"($\sim$2.5$-$3.5 AU)",
                xy=(np.sqrt(SNOW_LINE[0] * SNOW_LINE[1]), -0.62),
                ha="center", fontsize=9, color="#20708f")

    # Planets on the midline, size by log(1 + R/R_earth).
    for i, (name, b) in enumerate(BODIES.items()):
        size = 900.0 * np.log10(1.0 + b["R"])
        ax.scatter(b["a"], 0.0, s=max(size, 12), color=b["color"],
                   edgecolor="black", linewidth=0.6, zorder=5)
        dy = 0.34 if i % 2 == 0 else -0.34
        va = "bottom" if dy > 0 else "top"
        ax.text(b["a"], dy, name, ha="center", va=va, fontsize=9, zorder=6)

    ax.set_xscale("log")
    ax.set_xlim(0.3, 60)
    ax.set_ylim(-1.0, 1.0)
    ax.set_yticks([])
    ax.set_xlabel("Semi-major axis (AU)")
    ax.grid(axis="x", which="both", linestyle=":", alpha=0.3)
    ax.grid(axis="y", visible=False)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.set_xticks([0.3, 1, 3, 10, 30], labels=["0.3", "1", "3", "10", "30"])

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
