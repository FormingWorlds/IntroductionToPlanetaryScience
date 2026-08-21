"""Generate Fig. (`fig:birchs-law`).

Birch's law plot: compressional-wave velocity v_P vs density rho
for common mantle-forming minerals at ambient conditions. The
approximately linear trend holds at fixed mean atomic mass; outliers
such as Fe-rich fayalite sit below the trend due to higher mean
atomic mass.

Caption / figure id : `fig:birchs-law`
Markdown source     : book/08_interiors/interiors.md
Citation key        : Birch1952

Trend: v_P [km/s] = 3.28 * rho [g/cm^3] - 2.53 (Birch 1952 / Anderson
"Theory of the Earth"; representative for mean atomic mass ~20).

Mineral values + provenance live in `data/birch_minerals.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_FILE = Path(__file__).resolve().parent / "data/birch_minerals.json"
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/birchs_law.avif"

# Birch trend coefficients
TREND_A = -2.53   # intercept (km/s)
TREND_B =  3.28   # slope (km/s per g/cm^3)


def make_plot() -> Path:
    apply_style()
    data = json.loads(DATA_FILE.read_text())

    fig, ax = plt.subplots(figsize=(8.5, 6.0))

    # Trend line
    rho = np.linspace(2.4, 4.6, 100)
    v_P_trend = TREND_A + TREND_B * rho
    ax.plot(rho, v_P_trend, color="#d62728", lw=1.6, linestyle="--",
            label=(r"Birch trend (mean atomic mass $\bar M \sim 20$):" "\n"
                   fr"  $v_P = {TREND_B:.2f}\,\rho - {-TREND_A:.2f}$ km s$^{{-1}}$"))

    # Mineral points (split into trend members and outliers)
    main_x, main_y, main_n = [], [], []
    out_x, out_y, out_n = [], [], []
    for m in data["minerals"]:
        if m["outlier"]:
            out_x.append(m["density"])
            out_y.append(m["v_P"])
            out_n.append(m["name"])
        else:
            main_x.append(m["density"])
            main_y.append(m["v_P"])
            main_n.append(m["name"])

    ax.plot(main_x, main_y, "o", color="#1f3a5f", ms=11,
            mec="black", mew=0.4, zorder=5)

    # Points sitting close to the trend line need their label pushed off
    # the line rather than the default sideways offset; (dx, dy, ha, va).
    LABEL_OVERRIDE = {
        "Forsterite":  (0, 10, "center", "bottom"),
        "Periclase":   (-9, 0, "right", "center"),
        "Ringwoodite": (-8, 14, "center", "bottom"),
        "Corundum":    (0, 10, "center", "bottom"),
    }
    for x, y, n in zip(main_x, main_y, main_n):
        dx, dy, ha, va = LABEL_OVERRIDE.get(n, (8, 0, "left", "center"))
        ax.annotate(n, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=9, ha=ha, va=va)

    # Fayalite outlier in different colour, with annotation
    if out_x:
        ax.plot(out_x, out_y, "o", color="#d68a32", ms=11,
                mec="black", mew=0.4, zorder=5)
        for x, y, n in zip(out_x, out_y, out_n):
            ax.annotate(n, xy=(x, y), xytext=(8, 0), textcoords="offset points",
                        fontsize=9, va="center")
        # Annotation arrow showing the offset
        ax.annotate("Higher mean atomic\nmass (Fe-rich)\noffsets the trend",
                    xy=(out_x[0] - 0.05, out_y[0] + 0.2),
                    xytext=(3.3, 6.35),
                    fontsize=9, color="#7a2a2a", ha="left", va="center",
                    arrowprops=dict(arrowstyle="->", color="#7a2a2a", lw=0.7,
                                    shrinkA=4))

    ax.set_xlim(2.3, 4.6)
    ax.set_ylim(5, 11.5)
    ax.set_xlabel(r"Density $\rho$ (g cm$^{-3}$)")
    ax.set_ylabel(r"Compressional velocity $v_P$ (km s$^{-1}$)")
    ax.set_title(r"Birch's law: $v_P \approx a + b\,\rho$ "
                 "for silicates and oxides")
    ax.grid(linestyle=":", alpha=0.3)
    ax.legend(loc="upper left", frameon=True, fontsize=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_FILE}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
