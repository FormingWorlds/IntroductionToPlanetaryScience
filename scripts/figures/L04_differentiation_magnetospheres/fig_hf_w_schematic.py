"""Generate Fig. (`fig:hf-w-schematic`).

Two-panel explanatory schematic of Hf-W chronometry:

(a) Why the system dates core formation: 182Hf is lithophile and stays
    in the mantle, W is siderophile and is extracted into the core, so
    core formation separates the parent from the daughter reservoir.
(b) Mantle 182W excess vs time for early, Earth-like, and late core
    formation. Curves follow the two-stage model of Eq. eq:hfw-age in
    the notes: eps(t) = A0 * exp(-lambda t_cf) * (1 - exp(-lambda (t -
    t_cf))) with A0 = Q * (f - 1) * (182Hf/180Hf)_0 = 1e4 * 17 *
    1.02e-4 = 17.3 for Earth's mantle Hf/W enrichment, so the 28-Myr
    case plateaus at the measured mantle value of +2 epsilon units,
    reproducing the worked example.

Caption / figure id : `fig:hf-w-schematic`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Kleine2009
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/hf_w_schematic.avif")

HALF_LIFE = 8.9                      # Myr
LAM = np.log(2.0) / HALF_LIFE
AMP0 = 1e4 * 17.0 * 1.02e-4          # Q * (f - 1) * (182Hf/180Hf)_0, Earth Hf/W
EPS_EARTH = 2.0                      # measured mantle excess, epsilon units
T_EARTH = 28.0                       # two-stage model age from Eq. eq:hfw-age

CASES = [
    (10.0, "#d62728", "early (10 Myr)"),
    (T_EARTH, "#1f77b4", "Earth-like (28 Myr)"),
    (100.0, "#2ca02c", "late (100 Myr)"),
]


def eps_curve(t: np.ndarray, t_cf: float) -> np.ndarray:
    """Mantle 182W excess vs time for core formation at t_cf."""
    amp = AMP0 * np.exp(-LAM * t_cf)
    out = np.where(t > t_cf, amp * (1.0 - np.exp(-LAM * (t - t_cf))), 0.0)
    return out


def draw_cartoon(ax: plt.Axes) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.add_patch(Circle((5, 5.4), 3.4, facecolor="#f5deb3",
                        edgecolor="0.4", lw=1.2, zorder=1))
    ax.add_patch(Circle((5, 5.4), 1.5, facecolor="0.55",
                        edgecolor="0.3", lw=1.2, zorder=2))

    # W droplets sinking from the mantle into the core
    rng_pts = [(3.4, 7.4), (6.7, 7.2), (2.9, 4.6), (7.2, 4.9)]
    for (x, y) in rng_pts:
        ax.plot(x, y, "o", color="0.25", ms=5, zorder=3)
        dx, dy = (5 - x) * 0.35, (5.4 - y) * 0.35
        ax.add_patch(FancyArrowPatch((x, y), (x + dx, y + dy),
                                     arrowstyle="-|>", mutation_scale=10,
                                     color="0.25", lw=1.0, zorder=3))
    ax.annotate("W (siderophile)\nsinks into the core", xy=(5, 0.6),
                fontsize=9.5, ha="center", color="0.2")

    ax.annotate("mantle: Hf (lithophile) stays", xy=(5, 9.5), fontsize=9.5,
                ha="center", color="#8a6d1a")
    ax.annotate("$^{182}\\mathrm{Hf} \\rightarrow\\, ^{182}\\mathrm{W}$\n"
                "$t_{1/2} = 8.9$ Myr", xy=(5, 7.6), fontsize=9.5,
                ha="center", color="#8a6d1a", zorder=4)
    ax.annotate("core", xy=(5, 5.3), fontsize=10, ha="center",
                color="white", zorder=4)
    ax.set_title("(a) parent and daughter separate", fontsize=11)


def draw_curves(ax: plt.Axes) -> None:
    t = np.linspace(0.0, 130.0, 600)
    for t_cf, color, label in CASES:
        ax.plot(t, eps_curve(t, t_cf), color=color, lw=2.2, label=label)
        ax.axvline(t_cf, color=color, lw=0.8, ls=":", alpha=0.6)

    ax.axhline(0.0, color="0.4", lw=1.0)
    ax.annotate("chondrites (never differentiated)", xy=(64, 0.12),
                fontsize=8.5, color="0.35")
    ax.axhline(EPS_EARTH, color="0.2", lw=1.0, ls="--")
    ax.annotate("Earth's mantle today ($+2\\,\\varepsilon$)",
                xy=(64, EPS_EARTH + 0.12), fontsize=8.5, color="0.2")

    ax.set_xlim(0, 130)
    ax.set_ylim(-0.4, 9)
    ax.set_xlabel("Time after CAI condensation (Myr)")
    ax.set_ylabel(r"mantle $\varepsilon^{182}\mathrm{W}$ (parts per $10^4$)")
    ax.legend(title="core formation", loc="center right", fontsize=9)
    ax.set_title("(b) earlier core formation, larger excess", fontsize=11)


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10.4, 4.6),
                                     gridspec_kw={"width_ratios": [1, 1.35]})
    draw_cartoon(ax_a)
    draw_curves(ax_b)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
