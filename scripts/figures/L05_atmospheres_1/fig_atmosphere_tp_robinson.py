"""Generate Fig. (`fig:tp-profiles`).

Measured vertical temperature-pressure profiles of seven solar-system
atmospheres (Venus, Earth, Titan, Jupiter, Saturn, Uranus, Neptune),
digitized from the vector curves of Robinson & Catling (2014), their
Fig. 1, and replotted in the course style. The common feature is the
tropopause temperature minimum near 0.1 bar in Earth, Titan, and the
four giant planets; Venus shows only a weak global-mean minimum there
(it lacks a strong stratospheric inversion, per the source paper).
The digitized data live in `data/rc2014_fig1_tp_profiles.csv` with the
calibration provenance in its header; recovered anchor points agree
with in-situ measurements (Jupiter 165 K at 1 bar, Seiff et al. 1998;
Titan 94 K at 1.5 bar, Fulchignoni et al. 2005).

Caption / figure id : `fig:tp-profiles`
Markdown source     : book/05_atmospheres_1/atmospheres_1.md
Citation key        : Robinson2014
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_CSV = Path(__file__).resolve().parent / "data/rc2014_fig1_tp_profiles.csv"
OUT_AVIF = REPO_ROOT / "book/05_atmospheres_1/figures/atmosphere_tp_robinson.avif"

P_TROP = 0.1  # bar, the common tropopause pressure

COLORS = {
    "Venus":   "#8c8c1a",
    "Earth":   "#1f77b4",
    "Titan":   "#ff7f0e",
    "Jupiter": "#d62728",
    "Saturn":  "#9467bd",
    "Uranus":  "#2ca02c",
    "Neptune": "#17becf",
}


def load_profiles() -> dict[str, np.ndarray]:
    """Read the digitized profiles as {body: array of (T [K], P [bar])}."""
    profiles: dict[str, list[list[float]]] = {}
    with open(DATA_CSV) as f:
        rows = (r for r in f if not r.startswith("#"))
        for rec in csv.DictReader(rows):
            profiles.setdefault(rec["body"], []).append(
                [float(rec["T_K"]), float(rec["P_bar"])])
    if set(profiles) != set(COLORS):
        raise ValueError(
            f"CSV bodies {sorted(profiles)} do not match "
            f"COLORS keys {sorted(COLORS)}")
    return {k: np.array(v) for k, v in profiles.items()}


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(8.0, 7.6))

    profiles = load_profiles()
    for name, color in COLORS.items():
        arr = profiles[name]
        ax.plot(arr[:, 0], arr[:, 1], color=color, lw=2.2, label=name)

    ax.axhline(P_TROP, color="0.4", linestyle="--", lw=1.2, alpha=0.7)
    ax.text(357, 0.085, "0.1 bar tropopause", color="0.4", fontsize=11,
            ha="right", va="bottom")

    ax.set_yscale("log")
    ax.invert_yaxis()
    ax.set_xlim(38, 360)
    ax.set_ylim(6, 1e-3)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Pressure (bar)")
    ax.set_title("Measured T(p) profiles of seven solar-system atmospheres")
    ax.grid(which="both", linestyle=":", alpha=0.3)
    # Upper right: above 0.01 bar no profile exceeds about 285 K, so the
    # corner right of 290 K stays clear of all curves.
    ax.legend(loc="upper right", frameon=True, fontsize=11)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
