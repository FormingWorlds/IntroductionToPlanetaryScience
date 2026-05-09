"""Generate Fig. (`fig:earth-heat-budget`).

Pie chart of Earth's surface heat-flux budget, ~47 TW total,
decomposed into radiogenic, primordial / secular cooling, core
cooling and solidification, and lunar tidal dissipation.

Caption / figure id : `fig:earth-heat-budget`
Markdown source     : book/03_heat_energy/heat_energy.md
Citation key        : DaviesDavies2010

Component values are static numerics from the Davies & Davies 2010
review and are tabulated in `data/earth_heat_budget.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
META = DATA_DIR / "earth_heat_budget.json"
OUT_AVIF = REPO_ROOT / "book/03_heat_energy/figures/earth_heat_budget.avif"

COMPONENTS = [
    ("Radiogenic\n(mantle + crust)", 22.0, "#d62728"),
    ("Primordial\n(secular cooling)", 15.0, "#ff7f0e"),
    ("Core cooling\nand solidification", 10.0, "#1f77b4"),
    ("Tidal (lunar)", 0.1, "#2ca02c"),
]


def write_metadata() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    META.write_text(json.dumps({
        "purpose": "Fig. fig:earth-heat-budget: Earth surface heat budget pie",
        "total_TW": 47.0,
        "components": [{"label": l, "TW": v} for l, v, _ in COMPONENTS],
        "source": "Davies, J. H. & Davies, D. R. (2010), Solid Earth 1, 5-24",
        "doi": "10.5194/se-1-5-2010",
        "citation_key": "DaviesDavies2010",
        "license_note": "Component figures are conventional review values.",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    write_metadata()
    labels, sizes, colors = zip(*[(l, v, c) for l, v, c in COMPONENTS])

    fig, ax = plt.subplots(figsize=(7, 5.5))
    wedges, texts = ax.pie(
        sizes, colors=colors,
        labels=[f"{l}\n~{v:.1f} TW" for l, v in zip(labels, sizes)],
        startangle=90, counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5},
        textprops={"fontsize": 10},
        labeldistance=1.1,
    )

    # Inside-wedge values for the larger components
    for w, val in zip(wedges, sizes):
        if val >= 5:
            ang = (w.theta1 + w.theta2) / 2
            import numpy as np
            x = 0.6 * np.cos(np.radians(ang))
            y = 0.6 * np.sin(np.radians(ang))
            ax.text(x, y, f"{val:.0f} TW", ha="center", va="center",
                    fontsize=11, color="white", fontweight="bold")

    ax.set_title("Earth's surface heat-flux budget (~47 TW)", fontsize=12, pad=18)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  meta : {META}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
