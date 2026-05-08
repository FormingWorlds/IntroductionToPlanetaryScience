"""Generate Fig. (`fig:planetary-dipole-moments`).

Horizontal log-bar chart of planetary magnetic dipole moments
relative to Earth's, ordered from largest to smallest. Bodies with
no global field today (Mars, Venus) are shown as upper limits in
grey.

Caption / figure id : `fig:planetary-dipole-moments`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Bagenal2013

Numerics live in `data/planetary_dipole_moments.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_FILE = Path(__file__).resolve().parent / "data/planetary_dipole_moments.json"
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/planetary_dipole_moments.avif"


def _fmt(v: float) -> str:
    if v >= 100:
        return f"{v:.0e}".replace("e+0", "e+").replace("e+", "e+")
    if v >= 1:
        return f"{v:.1f}"
    if v >= 1e-3:
        return f"{v:.0e}".replace("e-0", "e-")
    return f"{v:.0e}".replace("e-0", "e-")


def make_plot() -> Path:
    apply_style()
    data = json.loads(DATA_FILE.read_text())
    bodies = data["bodies"]

    # Order largest to smallest magnetic moment (top -> bottom)
    bodies = sorted(bodies, key=lambda b: b["M_over_Mearth"], reverse=True)
    labels = [b["body"] for b in bodies]
    values = np.array([b["M_over_Mearth"] for b in bodies])
    is_active = [b["active"] for b in bodies]

    fig, ax = plt.subplots(figsize=(9.0, 5.2))
    y = np.arange(len(bodies))[::-1]  # so first label appears at top
    colors = ["#1f77b4" if a else "#888888" for a in is_active]

    ax.barh(y, values, color=colors, edgecolor="black", lw=0.6)

    # Numeric labels to the right of each bar
    for yi, v in zip(y, values):
        if v >= 100:
            txt = f"{v:.0e}".replace("e+04", "e4").replace("e+02", "e2") \
                .replace("e+01", "e1")
        elif v >= 1:
            txt = f"{v:.1f}"
        else:
            txt = f"{v:.0e}".replace("e-03", "e-3").replace("e-04", "e-4") \
                .replace("e-05", "e-5")
        ax.text(v * 1.4, yi, txt, va="center", fontsize=10)

    ax.axvline(1.0, color="0.4", linestyle="--", lw=0.8)
    ax.set_xscale("log")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(1e-6, 1e5)
    ax.set_xlabel(r"Dipole moment relative to Earth ($\mathcal{M}/\mathcal{M}_\oplus$)")
    ax.set_title("Planetary magnetic dipole moments")
    ax.grid(axis="x", which="both", linestyle=":", alpha=0.3)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    legend_elements = [
        Patch(facecolor="#1f77b4", edgecolor="black", label="Active dynamo"),
        Patch(facecolor="#888888", edgecolor="black",
              label="No global field today (upper limit)"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", frameon=True)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  data : {DATA_FILE}")
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
