"""Atmospheric flow regimes sorted by the Rossby number Ro = U / (f L).

For mid-latitude Earth (f = 1e-4 s^-1), flows with Ro << 1 are dominated
by rotation (large-scale circulation), whereas flows with Ro >> 1 are
governed by pressure gradients and friction (tornadoes and dust devils).
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/06_atmospheres_2/figures/rossby_regimes.avif"

# Mid-latitude Earth Coriolis parameter
F_CORIOLIS = 1.0e-4  # s^-1

# Large-scale atmospheric flow example
L_LARGE = 1.0e6  # m (1000 km)
U_LARGE = 10.0  # m/s
RO_LARGE = U_LARGE / (F_CORIOLIS * L_LARGE)  # 0.1

# Small-scale order-of-magnitude examples
L_DUST = 10.0  # m (about 10 m)
U_DUST = 10.0  # m/s (about 10 m/s)
RO_DUST = U_DUST / (F_CORIOLIS * L_DUST)  # 10000

L_TORNADO = 100.0  # m (about 100 m)
U_TORNADO = 50.0  # m/s (about 50 m/s)
RO_TORNADO = U_TORNADO / (F_CORIOLIS * L_TORNADO)  # 5000


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, ax = plt.subplots(figsize=(8.5, 4.8))

    # Log-log coordinates: L from 1 m to 10 000 km (1e7 m), U from 0.1 to 100 m/s
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1.0, 1.0e7)
    ax.set_ylim(0.1, 100.0)

    # Shading: Ro < 1 light blue (#e8f1fa), Ro > 1 light orange (#fdebd0)
    l_grid = np.logspace(0, 7, 500)
    u_ro1 = F_CORIOLIS * l_grid
    u_ro1_clamped = np.clip(u_ro1, 0.1, 100.0)
    ax.fill_between(l_grid, u_ro1_clamped, 100.0, color="#fdebd0", alpha=0.55, zorder=0)
    ax.fill_between(l_grid, 0.1, u_ro1_clamped, color="#e8f1fa", alpha=0.55, zorder=0)

    # Lines of constant Rossby number Ro = U / (f L) for Ro = 0.01, 0.1, 1, 10, 100
    ros = [0.01, 0.1, 1.0, 10.0, 100.0]
    for ro in ros:
        l_min = max(1.0, 0.1 / (ro * F_CORIOLIS))
        l_max = min(1.0e7, 100.0 / (ro * F_CORIOLIS))
        ax.plot(
            [l_min, l_max],
            [ro * F_CORIOLIS * l_min, ro * F_CORIOLIS * l_max],
            color="#4a6984" if ro == 1.0 else "0.45",
            lw=2.0 if ro == 1.0 else 1.2,
            ls="-" if ro == 1.0 else "--",
            zorder=2,
        )

    fig.tight_layout()
    fig.canvas.draw()
    p1 = ax.transData.transform((1.0e3, 0.1))
    p2 = ax.transData.transform((1.0e6, 100.0))
    angle = np.degrees(np.arctan2(p2[1] - p1[1], p2[0] - p1[0]))

    # Line labels parallel to each constant-Ro line
    for ro in ros:
        l_pt = 0.35 / (ro * F_CORIOLIS)
        ax.text(
            l_pt * 0.68,
            0.52,
            rf"$\mathrm{{Ro}} = {ro:g}$",
            rotation=angle,
            fontsize=10,
            ha="center",
            va="bottom",
            color="#4a6984" if ro == 1.0 else "0.35",
            weight="bold" if ro == 1.0 else "normal",
            zorder=3,
        )

    # Data points: large-scale flow, dust devil, tornado
    ax.plot(L_LARGE, U_LARGE, "o", color="#1f6db8", ms=7, zorder=5)
    ax.annotate(
        "Large-scale atmospheric flow\n" + r"($L = 1000$ km, $U = 10$ m/s, $\mathrm{Ro} = 0.1$)",
        xy=(L_LARGE, U_LARGE),
        xytext=(1.4e6, 4.2),
        fontsize=10,
        color="0.2",
        bbox=dict(facecolor="#e8f1fa", edgecolor="none", pad=1.5),
        arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9),
        zorder=6,
    )

    ax.plot(L_DUST, U_DUST, "o", color="#c46b1a", ms=7, zorder=5)
    ax.annotate(
        "Dust devil\n(about 10 m, about 10 m/s)",
        xy=(L_DUST, U_DUST),
        xytext=(1.4, 4.0),
        fontsize=10,
        color="0.2",
        bbox=dict(facecolor="#fdebd0", edgecolor="none", pad=1.5),
        arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9),
        zorder=6,
    )

    ax.plot(L_TORNADO, U_TORNADO, "o", color="#c46b1a", ms=7, zorder=5)
    ax.annotate(
        "Tornado\n(about 100 m, about 50 m/s)",
        xy=(L_TORNADO, U_TORNADO),
        xytext=(15, 60),
        fontsize=10,
        color="0.2",
        bbox=dict(facecolor="#fdebd0", edgecolor="none", pad=1.5),
        arrowprops=dict(arrowstyle="->", color="0.3", lw=0.9),
        zorder=6,
    )

    # Regime labels for Ro < 1 and Ro > 1
    ax.text(
        3.0e5,
        0.16,
        "rotation dominates (Ro << 1):\nlarge-scale circulation",
        fontsize=10,
        color="#1f6db8",
        weight="bold",
        ha="left",
        va="bottom",
        bbox=dict(facecolor="#e8f1fa", edgecolor="none", pad=1.5),
        zorder=4,
    )

    ax.text(
        2.0,
        30.0,
        "rotation unimportant (Ro >> 1):\npressure gradients and friction",
        fontsize=10,
        color="#c46b1a",
        weight="bold",
        ha="left",
        va="center",
        bbox=dict(facecolor="#fdebd0", edgecolor="none", pad=1.5),
        zorder=4,
    )

    ax.set_xlabel("Horizontal length scale $L$ (m)", fontsize=10)
    ax.set_ylabel(r"Wind speed $U$ (m s$^{-1}$)", fontsize=10)
    ax.set_title("The Rossby number sorts flows by the role of rotation", fontsize=11, pad=24)
    ax.text(
        0.5,
        1.02,
        r"mid-latitude Earth ($f = 10^{-4}$ s$^{-1}$)",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=10,
        color="0.3",
    )

    save_figure(fig, OUT_AVIF)
    return fig


def main() -> None:
    """Generate the figure and report its path."""
    fig = make_plot()
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
