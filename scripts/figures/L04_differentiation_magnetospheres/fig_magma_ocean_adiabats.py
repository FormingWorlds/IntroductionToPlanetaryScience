"""Generate Fig. (`fig:magma-ocean-crystallisation`).

Schematic temperature-pressure diagram of magma-ocean solidification:
the peridotite solidus and liquidus against a sequence of magma-ocean
adiabats at successive times as the planet cools. Both melting curves
rise more steeply with pressure than the adiabats, so a cooling
adiabat first drops below the liquidus, and then the solidus, at the
base of the mantle: crystallisation proceeds from the bottom up, and
the crystallisation front (adiabat-solidus intersection) migrates
upward with time. Each adiabat is drawn only above its solidus
crossing; below the front the mantle is solid. Curve shapes are
schematic, chosen to reproduce the behaviour established for
peridotite melting and magma-ocean adiabats (Elkins-Tanton 2012,
Annu. Rev. Earth Planet. Sci. 40, 113).

Caption / figure id : `fig:magma-ocean-crystallisation`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation keys       : ElkinsTanton2012, Labrosse2007, Samuel2023
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/"
            "magma_ocean_adiabats.avif")

P_CMB = 135.0  # GPa, base of Earth's mantle

# Schematic melting curves for peridotite (steep in T-P).
def t_solidus(p):
    return 1410.0 + 90.0 * np.asarray(p) ** 0.70


def t_liquidus(p):
    return 1980.0 + 95.0 * np.asarray(p) ** 0.72


# Schematic magma-ocean adiabats (shallower in T-P than the melting
# curves), anchored at the surface potential temperature T0.
def t_adiabat(p, t0):
    return t0 * (1.0 + 0.02 * np.asarray(p)) ** 0.37


ADIABATS = [
    (3300.0, "#d62728", "$t_1$"),
    (3100.0, "#e07b39", "$t_2$"),
    (2300.0, "#1f77b4", "$t_3$"),
    (1700.0, "#31446b", "$t_4$"),
]


def crossing(t0, t_melt):
    """Pressure where the adiabat crosses a melting curve, or None."""
    p = np.linspace(0.0, P_CMB, 4000)
    d = t_adiabat(p, t0) - t_melt(p)
    idx = np.where(np.diff(np.sign(d)) != 0)[0]
    if len(idx) == 0:
        return None
    i = idx[-1]
    return float(np.interp(0.0, [d[i + 1], d[i]], [p[i + 1], p[i]]))


def make_plot() -> Path:
    apply_style()
    p = np.linspace(0.0, P_CMB, 400)
    sol, liq = t_solidus(p), t_liquidus(p)

    fig, ax = plt.subplots(figsize=(8.0, 6.0))

    # Phase regions
    ax.fill_betweenx(p, 1200.0, sol, color="0.82", alpha=0.55, zorder=0)
    ax.fill_betweenx(p, sol, liq, color="#e8c88a", alpha=0.45, zorder=0)
    ax.fill_betweenx(p, liq, 5800.0, color="#f4b8b0", alpha=0.40, zorder=0)
    ax.annotate("solid", xy=(1750, 108), fontsize=10.5, color="0.30",
                ha="center")
    ax.annotate("mush", xy=(3900, 88), fontsize=10.5,
                color="#8a6d1a", ha="center", va="center")
    ax.annotate("fully molten", xy=(5030, 55), fontsize=10.5,
                color="#b0413e", ha="center")

    # Melting curves
    ax.plot(sol, p, color="0.25", lw=2.2, zorder=3)
    ax.plot(liq, p, color="0.25", lw=2.2, ls="--", zorder=3)
    ax.annotate("solidus", xy=(t_solidus(60) - 80, 60), fontsize=10,
                color="0.15", ha="right", va="center")
    ax.annotate("liquidus", xy=(t_liquidus(24) + 120, 24), fontsize=10,
                color="0.15", ha="left", va="center")

    # Adiabats at successive times, hot to cold, each truncated at its
    # solidus crossing (below the front the mantle is solid).
    for t0, color, label in ADIABATS:
        p_sol = crossing(t0, t_solidus)
        p_end = P_CMB if p_sol is None else p_sol
        pp = np.linspace(0.0, p_end, 300)
        ax.plot(t_adiabat(pp, t0), pp, color=color, lw=2.4, zorder=4)
        ax.annotate(label, xy=(t0, -3), ha="center", va="bottom",
                    fontsize=10, color=color)
        if p_sol is not None:
            ax.plot(t_adiabat(p_sol, t0), p_sol, marker="o", color=color,
                    ms=7, zorder=5)

    # Cooling sequence, hot t1 to cold t4
    ax.annotate("", xy=(1850, -9.5), xytext=(3150, -9.5),
                arrowprops=dict(arrowstyle="-|>", color="0.35", lw=1.4))
    ax.annotate("cooling", xy=(2500, -11.5), ha="center", va="bottom",
                fontsize=9, color="0.35")

    # First crystals: t2 adiabat meets the liquidus near the base
    t0_2, c_2 = ADIABATS[1][0], ADIABATS[1][1]
    p_liq2 = crossing(t0_2, t_liquidus)
    ax.plot(t_adiabat(p_liq2, t0_2), p_liq2, marker="o", mfc="white",
            mec=c_2, mew=1.8, ms=8, zorder=5)
    ax.annotate("first crystals\nat the base", xy=(5100, 76), ha="center",
                va="center", fontsize=9.5, color=c_2)
    ax.annotate("", xy=(t_adiabat(p_liq2, t0_2) + 60, p_liq2 + 1),
                xytext=(5060, 82),
                arrowprops=dict(arrowstyle="-|>", color=c_2, lw=1.2))

    # Front migration: dots on the solidus move to shallower depth
    ax.annotate("", xy=(1560, 14), xytext=(1560, 102),
                arrowprops=dict(arrowstyle="-|>", color="0.35", lw=1.6))
    ax.annotate("crystallisation front\nmoves upward", xy=(1340, 58),
                ha="center", va="center", fontsize=9.5, color="0.30",
                rotation=90)

    ax.axhline(P_CMB, color="0.4", lw=1.0)
    ax.annotate("core-mantle boundary", xy=(2600, P_CMB - 2.5),
                fontsize=9, color="0.35", va="bottom", ha="center")

    ax.set_xlim(1200, 5800)
    ax.set_ylim(140, -16)
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Pressure (GPa), depth increases downward")
    ax.grid(False)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
