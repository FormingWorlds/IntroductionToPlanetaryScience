"""Generate Fig. (`fig:venus-activity-evidence`).

Timeline from 1975 to 2025 illustrating three lines of evidence for
present-day volcanic activity on Venus (book/09_earth_venus/:
(1) Upper-atmosphere SO2 variations over a 40-year baseline with mission
    coverage bars for Pioneer Venus (1978 to 1992), Magellan (1990 to 1994),
    and Venus Express (2006 to 2014) showing factor-of-several swings
"factor-of-several variations in upper-atmosphere
    SO2 concentrations over the 40-year baseline").
(2) Near-IR thermal emission anomalies over Idunn Mons detected by
    Venus Express, marked at 2010"Venus Express detected
    near-IR thermal emission anomalies over Idunn Mons consistent with cooling
    from recent lava flows").
(3) Magellan radar morphological changes at Maat Mons volcanic vent between
    1990 and 1992 observation cycles, providing the first direct evidence of
    active eruption"HerrickHensley2023 reanalysed Magellan
    radar data from 1990 to 1992 and identified morphological changes in a
    volcanic vent on the flank of Maat Mons").

Caption / figure id : `fig:venus-activity-evidence`
Markdown source     : book/09_earth_venus/(lines 661-671)
Specification       :line 20
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/09_earth_venus/figures/venus_activity_evidence.avif"

# Distinct palette for atmospheric, thermal, and radar evidence
C_ATM = "#1f6db8"
C_THERM = "#b22222"
C_RADAR = "#2ca02c"


def make_plot() -> Path:
    """Generate the schematic timeline of Venus volcanic activity evidence.

    Returns
    -------
    pathlib.Path
        Path to the saved AVIF image.
    """
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 4.5))

    # Timeline bounds from specification: 1975 to 2025
    ax.set_xlim(1975, 2025)
    ax.set_ylim(-0.1, 3.55)

    # Shaded row backgrounds and divider lines separating the three rows
    ax.add_patch(Rectangle((1975, 2.05), 50, 1.50, facecolor="#f4f7fa", edgecolor="none", zorder=0))
    ax.add_patch(Rectangle((1975, 1.05), 50, 1.00, facecolor="#ffffff", edgecolor="none", zorder=0))
    ax.add_patch(Rectangle((1975, 0.00), 50, 1.05, facecolor="#fbfbfc", edgecolor="none", zorder=0))
    ax.axhline(1.05, color="0.8", lw=0.8, ls=":")
    ax.axhline(2.05, color="0.8", lw=0.8, ls=":")

    # Three labelled rows of evidence on the y-axis
    ax.set_yticks([0.52, 1.55, 2.75])
    ax.set_yticklabels([
        "Row 3: Surface\nradar morphology",
        "Row 2: Near-IR\nthermal emission",
        "Row 1: Cloud-top\nSO$_2$ variation",
    ], fontsize=10, weight="bold")

    # --- ROW 1: Cloud-top SO2 variation and mission coverage bars ---
    # Mission bars: Pioneer Venus (1978-1992), Magellan (1990-1994), Venus Express (2006-2014)
    bars = [
        ("Pioneer Venus (1978-1992)", 1978, 1992, 2.98, "#2a6f97"),
        ("Magellan (1990-1994)", 1990, 1994, 3.26, "#c05621"),
        ("Venus Express (2006-2014)", 2006, 2014, 2.98, "#2a6f97"),
    ]
    for label, x0, x1, y, col in bars:
        ax.plot([x0, x1], [y, y], color=col, lw=3.2, solid_capstyle="round", zorder=3)
        ax.text(0.5 * (x0 + x1), y + 0.05, label, ha="center", va="bottom",
                fontsize=10, color=col, weight="bold")

    # Qualitative SO2 curve over the 40-year baseline
    t1 = np.linspace(1978, 1992, 100)
    so2_1 = 2.18 + 0.60 * np.exp(-(t1 - 1978) / 4.2)
    t_mid = np.linspace(1992, 2006, 80)
    so2_mid = np.full_like(t_mid, 2.18 + 0.60 * np.exp(-(1992 - 1978) / 4.2))
    t2 = np.linspace(2006, 2014, 80)
    so2_2 = 2.20 + 0.40 * np.exp(-((t2 - 2008) / 2.2)**2)

    t_all = np.concatenate([t1, t_mid, t2])
    so2_all = np.concatenate([so2_1, so2_mid, so2_2])

    for t_seg, s_seg in ((t1, so2_1), (t2, so2_2)):
        ax.plot(t_seg, s_seg, color=C_ATM, lw=2.2, zorder=4)
        ax.fill_between(t_seg, 2.12, s_seg, color=C_ATM, alpha=0.12, zorder=1)

    # Qualitative annotation without numerical SO2 values
    ax.text(1998.0, 2.50, "factor-of-several swings\n(episodic volcanic outgassing)",
            fontsize=10, ha="center", va="center", color=C_ATM, style="italic")

    # --- ROW 2: Venus Express near-IR thermal emission anomalies at Idunn Mons ---
    # Marked at 2010
    ax.plot(2010, 1.55, marker="D", color=C_THERM, ms=8, zorder=5)
    ax.axvline(2010, ymin=0.42, ymax=0.58, color=C_THERM, lw=0.9, ls="--", alpha=0.6)
    ax.annotate(
        "2010: near-IR thermal emission anomalies\nover Idunn Mons (Venus Express), consistent\nwith cooling of recent lava flows",
        xy=(2010, 1.55), xytext=(2008.0, 1.55),
        ha="right", va="center", fontsize=10, color=C_THERM,
        arrowprops=dict(arrowstyle="->", color=C_THERM, lw=1.0),
    )

    # --- ROW 3: Magellan radar vent changes and first direct evidence ---
    # Cycle changes between 1990 and 1992
    ax.plot([1990, 1992], [0.65, 0.65], color=C_RADAR, lw=4.5, solid_capstyle="round", zorder=4)
    ax.plot(1990, 0.65, marker="o", color=C_RADAR, ms=6, zorder=5)
    ax.plot(1992, 0.65, marker="o", color=C_RADAR, ms=6, zorder=5)
    ax.text(1991, 0.75, "Maat Mons vent, 1990 to 1992 cycles:\nenlarged, with a fresh lava flow",
            ha="center", va="bottom", fontsize=10, color=C_RADAR)

    # 2023 discovery: first direct evidence, Herrick and Hensley 2023
    ax.plot(2023, 0.35, marker="*", color="#b22222", ms=12, zorder=5)
    ax.add_patch(FancyArrowPatch(
        (1992.5, 0.60), (2022.0, 0.38),
        connectionstyle="arc3,rad=-0.15",
        arrowstyle="->", mutation_scale=10,
        color="0.5", lw=1.0, ls="--",
    ))
    ax.annotate(
        "first direct evidence, Herrick and Hensley 2023\n"
        "(2023 reanalysis of 1990-1992 Magellan radar data)",
        xy=(2023, 0.35), xytext=(2020.5, 0.35),
        ha="right", va="center", fontsize=10, color="#b22222", weight="bold",
        arrowprops=dict(arrowstyle="->", color="#b22222", lw=1.0),
    )

    ax.set_xlabel("Year", fontsize=11)
    ax.set_xticks([1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025])
    ax.set_title("Evidence for present-day volcanic activity on Venus (schematic timeline)",
                 fontsize=11.5, weight="bold", pad=10)

    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    """Execute figure generation and display the saved image path."""
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()