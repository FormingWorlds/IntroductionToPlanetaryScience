"""Generate Fig. 6.2 (`fig:composition-bar`).

Stacked bar chart of atmospheric volume mixing ratios for five
representative solar-system bodies.

The data are static (NASA Planetary Fact Sheet, Williams 2024) and are
captured verbatim in `data/atmospheric_compositions.csv` next to this
script. Update the CSV (and bump its sidecar JSON) only when the Fact
Sheet revises its values.

Caption / figure id : Fig. 6.2 / `fig:composition-bar`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md (around line 61)
Citation key        : NASAFactSheet
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(__file__).resolve().parent / "data"
CSV = DATA_DIR / "atmospheric_compositions.csv"
META = DATA_DIR / "atmospheric_compositions.json"
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/composition_bar.avif"

SPECIES = ["CO2", "N2", "O2", "H2", "He", "CH4", "Ar", "Other"]
LABELS = ["CO$_2$", "N$_2$", "O$_2$", "H$_2$", "He", "CH$_4$", "Ar", "Other"]
COLORS = ["#222222", "#1f77b4", "#2ca02c", "#9467bd",
          "#bbbbbb", "#ff7f0e", "#8c564b", "#dddddd"]
LABEL_VALUE_THRESHOLD = 4.0  # percent


def write_data() -> None:
    """Static data block written to CSV+JSON. Edit values only by updating
    this function and rerunning the script."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    rows = [
        # body,    CO2,  N2,    O2,    H2,    He,    CH4,   Ar,    Other
        ("Venus",  96.5,  3.5,  0.0,   0.0,   0.0,   0.0,   0.0,   0.0  ),
        ("Earth",  0.04, 78.1, 20.9,   0.0,   0.0,   0.0,   0.93,  0.07 ),
        ("Mars",   95.1,  2.59, 0.16,  0.0,   0.0,   0.0,   1.94,  0.21 ),
        ("Jupiter", 0.0,  0.0,  0.0,   86.0, 13.6,   0.21,  0.0,   0.19 ),
        ("Titan",   0.0, 94.2,  0.0,   0.10,  0.0,   5.65,  0.05,  0.0  ),
    ]
    df = pd.DataFrame(rows, columns=["body", *SPECIES])
    df.to_csv(CSV, index=False)
    META.write_text(json.dumps({
        "purpose": "Fig. 6.2 (fig:composition-bar): atmospheric VMR by body",
        "source": "NASA Planetary Fact Sheet (Williams 2024)",
        "source_url": "https://nssdc.gsfc.nasa.gov/planetary/factsheet/",
        "retrieved_date": "2026-04-23",
        "citation_key": "NASAFactSheet",
        "units": "Volume mixing ratio in percent.",
        "columns": {sp: f"{sp} volume mixing ratio (%)" for sp in SPECIES},
        "license_note": "NASA Planetary Fact Sheet content is public domain.",
    }, indent=2))


def make_plot() -> Path:
    apply_style()
    if not CSV.exists():
        write_data()
    df = pd.read_csv(CSV)

    bodies = df["body"].tolist()
    fig, ax = plt.subplots(figsize=(8, 4.2))

    x = np.arange(len(bodies))
    width = 0.65
    bottoms = np.zeros(len(bodies))
    for i, sp in enumerate(SPECIES):
        vals = df[sp].to_numpy()
        ax.bar(x, vals, width, bottom=bottoms, color=COLORS[i],
               label=LABELS[i], edgecolor="white", linewidth=0.4)
        for j, v in enumerate(vals):
            if v >= LABEL_VALUE_THRESHOLD:
                txt_color = "white" if i in (0, 1, 3, 4) else "black"
                ax.text(x[j], bottoms[j] + v / 2.0, f"{v:.1f}%",
                        ha="center", va="center", color=txt_color, fontsize=9)
        bottoms += vals

    ax.set_xticks(x)
    ax.set_xticklabels(bodies, fontsize=11)
    ax.set_ylabel("Volume mixing ratio (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Atmospheric composition of five solar-system bodies",
                 fontsize=12, pad=10)
    ax.legend(bbox_to_anchor=(1.02, 1.0), loc="upper left", fontsize=10,
              frameon=False)
    ax.grid(axis="y", linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    write_data()
    out = make_plot()
    print(f"  data : {CSV}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
