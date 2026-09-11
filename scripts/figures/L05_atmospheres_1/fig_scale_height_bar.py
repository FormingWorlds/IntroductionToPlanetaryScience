"""Generate Fig. (`fig:scale-height-bar`).

Horizontal bar chart of atmospheric scale heights H = kB*T / (mu*m_u*g)
for Venus, Earth, Mars, Jupiter, and Titan, computed from characteristic
temperatures, mean molecular weights, and surface gravities.

Caption / figure id : `fig:scale-height-bar`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md (lines 215-232)
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/scale_height_bar.avif"

# Physical constants from subsection text (worked example, line 226):
# kB in J K^-1 and m_u in kg.
KB = 1.381e-23
MU_U = 1.661e-27

# Atmospheric data from table in book/05_atmospheres_1/atmospheres_1.md:
# body, T [K], mu, g [m s^-2], H_table [km].
BODIES_DATA = [
    {"name": "Venus", "T": 737.0, "mu": 43.4, "g": 8.87, "H_table": 15.9, "color": "#c29b38"},
    {"name": "Earth", "T": 288.0, "mu": 28.97, "g": 9.81, "H_table": 8.4, "color": "#2a6fdb"},
    {"name": "Mars", "T": 215.0, "mu": 43.3, "g": 3.72, "H_table": 11.1, "color": "#c1440e"},
    {"name": "Jupiter", "T": 165.0, "mu": 2.2, "g": 24.8, "H_table": 25.0, "color": "#c8a165"},
    {"name": "Titan", "T": 94.0, "mu": 27.4, "g": 1.35, "H_table": 21.0, "color": "#e89242"},
]


def compute_scale_height(temperature: float, mu: float, gravity: float) -> float:
    """Compute atmospheric scale height in kilometres.

    Parameters
    ----------
    temperature : float
        Characteristic atmospheric temperature in kelvins.
    mu : float
        Mean molecular weight in atomic mass units.
    gravity : float
        Surface gravity in m s^-2.

    Returns
    -------
    float
        Atmospheric scale height H = kB * T / (mu * m_u * g) in km.
    """
    return (KB * temperature) / (mu * MU_U * gravity) / 1000.0


def make_plot() -> Path:
    """Generate the scale height horizontal bar chart.

    Returns
    -------
    Path
        Path to the saved AVIF figure.
    """
    apply_style()

    # Recompute scale heights and verify against table values.
    records = []
    for entry in BODIES_DATA:
        h_calc = compute_scale_height(entry["T"], entry["mu"], entry["g"])
        records.append({**entry, "H_calc": h_calc})

    # Sort bodies by computed scale height in ascending order.
    records.sort(key=lambda item: item["H_calc"])

    fig, ax = plt.subplots(figsize=(7.5, 4.0))

    y_pos = np.arange(len(records))
    h_values = [r["H_calc"] for r in records]
    colors = [r["color"] for r in records]
    labels = [r["name"] for r in records]

    ax.barh(y_pos, h_values, height=0.55, color=colors, edgecolor="black", linewidth=0.6)

    # Label each bar with H in km and annotate T, mu, g used.
    for y_idx, rec in zip(y_pos, records):
        h = rec["H_calc"]
        temp = int(rec["T"]) if rec["T"].is_integer() else rec["T"]
        mu = rec["mu"]
        g = rec["g"]
        ax.text(h + 0.5, y_idx - 0.12, f"{h:.1f} km", va="center", ha="left", fontsize=10.5, weight="bold")
        param_str = rf"($T = {temp}\ \mathrm{{K}},\ \mu = {mu},\ g = {g}\ \mathrm{{m\,s^{{-2}}}}$)"
        ax.text(h + 0.5, y_idx + 0.15, param_str, va="center", ha="left", fontsize=10, color="#333333")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel(r"Atmospheric scale height $H$ (km)", fontsize=11)
    ax.set_xlim(0, 44)
    ax.set_ylim(len(records) - 0.4, -0.6)
    ax.set_title(r"Atmospheric scale heights: $H = k_\mathrm{B} T / (\mu \, m_u \, g)$", fontsize=12, pad=10)
    ax.grid(axis="x", linestyle=":", alpha=0.3)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Recompute scale heights, report comparison, and generate plot."""
    print("Scale height comparison (computed vs table):")
    for entry in BODIES_DATA:
        h_calc = compute_scale_height(entry["T"], entry["mu"], entry["g"])
        diff = h_calc - entry["H_table"]
        name = entry["name"]
        ht = entry["H_table"]
        print(f"  {name:8s}: computed={h_calc:5.2f} km, table={ht:4.1f} km, diff={diff:+5.2f} km")

    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()