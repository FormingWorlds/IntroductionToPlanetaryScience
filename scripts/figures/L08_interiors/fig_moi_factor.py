"""Generate Fig. (`fig:moi-factor`).

Bar chart of measured moment-of-inertia factors C/MR^2 for nine
solar-system bodies, ordered from least-differentiated (highest
C/MR^2) to most-differentiated (lowest). The dashed red line marks
the uniform-density-sphere value 2/5 = 0.4.

Caption / figure id : `fig:moi-factor`
Markdown source     : book/08_interiors/interiors.md

Numerics + per-body provenance live in `data/moi_factors.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_FILE = Path(__file__).resolve().parent / "data/moi_factors.json"
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/moi_factor.avif"

UNIFORM_VALUE = 0.4


def make_plot() -> Path:
    apply_style()
    data = json.loads(DATA_FILE.read_text())
    bodies = sorted(data["bodies"], key=lambda b: -b["C_over_MR2"])

    labels = [b["body"] for b in bodies]
    vals = np.array([b["C_over_MR2"] for b in bodies])
    errs = np.array([b["uncertainty"] for b in bodies])

    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(bodies))
    colors = cm.viridis(np.linspace(0.85, 0.20, len(bodies)))

    ax.bar(x, vals, yerr=errs, capsize=4,
           color=colors, edgecolor="black", lw=0.5,
           ecolor="black", error_kw=dict(lw=1.0))

    # Numerical value labels inside or above each bar
    for xi, v, err in zip(x, vals, errs):
        ax.text(xi, v - 0.012, f"{v:.3f}", ha="center", va="top",
                color="white", fontsize=10, weight="bold")

    ax.axhline(UNIFORM_VALUE, color="#d62728", linestyle="--", lw=1.6)
    ax.text(len(bodies) - 0.5, UNIFORM_VALUE + 0.003,
            r"Uniform-density sphere: $C/MR^2 = 2/5 = 0.4$",
            color="#d62728", fontsize=11, ha="right", va="bottom")

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(r"Moment of inertia factor $C/MR^2$")
    ax.set_ylim(0.28, 0.42)
    ax.set_title(r"Measured $C/MR^2$ for solar-system bodies "
                 r"(lower $\Rightarrow$ stronger central concentration of mass)",
                 fontsize=12)
    ax.grid(axis="y", linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_FILE}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
