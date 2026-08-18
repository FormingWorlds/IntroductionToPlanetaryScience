"""Generate Fig. (`fig:magnetopause-balance`).

Schematic of pressure balance at the dayside magnetopause: solar
wind (left) is decelerated at the bow shock and deflected around the
magnetopause, which compresses Earth's dipolar field on the dayside
and stretches it into a long magnetotail. The standoff distance for
Earth under typical conditions is r_mp ~ 10 R_E.

Caption / figure id : `fig:magnetopause-balance`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Kivelson1995

Pure schematic; geometry is illustrative.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/04_differentiation_magnetospheres/figures/magnetopause_pressure_balance.avif"

GREEN = "#2ca02c"
RED = "#d62728"
ORANGE = "#ff7f0e"


def make_plot() -> Path:
    apply_style()
    fig, ax = plt.subplots(figsize=(10, 6.5))

    # Earth at origin (small blue circle)
    R_E = 0.6
    ax.add_patch(Circle((0, 0), R_E, color="#2b6cb0",
                        ec="black", lw=0.6, zorder=5))
    # Label sits clear of the field-line loops, tied back by a leader
    ax.annotate("Earth", xy=(-0.45, -0.45), xytext=(-3.4, -4.9),
                fontsize=10, color="black", ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color="0.5", lw=0.7,
                                shrinkA=6, shrinkB=2))

    # Magnetic dipole field lines: dayside is -x (sunward), tail is +x.
    # Compress -x side and stretch +x side.
    for L in (1.5, 2.4, 3.4, 4.6, 6.0, 8.0):
        theta = np.linspace(-0.92 * np.pi, 0.92 * np.pi, 400)
        r = L * np.cos(theta) ** 2
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        # Compress dayside (x < 0)
        x_compress = np.where(x < 0, x * (0.55 / (0.55 + 0.05 * L)), x)
        # Stretch tail (x > 0)
        stretch = 1.0 + 0.65 * L
        x_stretch = np.where(x_compress > 0, x_compress * stretch, x_compress)
        y_stretch = np.where(x_stretch > 0,
                             y * (1.0 / (1.0 + 0.05 * L)),
                             y)
        ax.plot(x_stretch, y_stretch, color="#444", lw=0.8, alpha=0.85,
                zorder=2)

    # Magnetopause: solid red, opening to LEFT (sunward, -x)
    # Use Shue-style r(theta) = r0 * (2/(1+cos(theta)))^a where theta=0 is
    # the standoff direction. Place standoff along -x by mapping theta->pi-theta.
    th = np.linspace(-np.pi * 0.78, np.pi * 0.78, 300)
    a = 0.6
    rho = (10.0 * R_E) * (2.0 / (1.0 + np.cos(th))) ** a
    x_mp = -rho * np.cos(th)   # mirror: standoff at x = -10 R_E
    y_mp = rho * np.sin(th)
    mask = (x_mp < 14.0)
    ax.plot(x_mp[mask], y_mp[mask], color=RED, lw=2.0, label="Magnetopause",
            zorder=4)

    # Bow shock: orange dashed, sunward of magnetopause
    rho_bs = (13.0 * R_E) * (2.0 / (1.0 + np.cos(th))) ** a
    x_bs = -rho_bs * np.cos(th)
    y_bs = rho_bs * np.sin(th)
    mask_bs = (x_bs < 16.0)
    ax.plot(x_bs[mask_bs], y_bs[mask_bs], color=ORANGE, lw=1.6,
            linestyle="--", label="Bow shock", zorder=4)

    # Solar wind arrows from far left, flowing rightward toward Earth
    sw_x = np.array([-15.5, -15.5, -15.5, -15.5, -15.5])
    sw_y = np.array([-4.0, -2.0, 0.0, 2.0, 4.0])
    for x_, y_ in zip(sw_x, sw_y):
        ax.add_patch(FancyArrowPatch(
            (x_, y_), (x_ + 1.6, y_),
            arrowstyle="->", mutation_scale=14, color=GREEN, lw=1.5))
    ax.text(-15.5, 5.6, r"Solar wind" + "\n" + r"$\rho_{sw}\, V_{sw}^2$",
            color=GREEN, fontsize=11, ha="left")
    ax.text(-15.5, -5.5, "To Sun", color="0.4", fontsize=9, ha="left")

    # Pressure-balance equation
    ax.text(0.0, 6.5,
            r"$\dfrac{1}{2}\rho_{sw} V_{sw}^2 = \dfrac{B_{\rm mp}^2}{2\mu_0}$",
            fontsize=13, ha="center",
            bbox=dict(facecolor="white", edgecolor="0.6", boxstyle="round,pad=0.3"))

    # Standoff arrow on -x side
    ax.add_patch(FancyArrowPatch(
        (0.0, -7.8), (-10.0 * R_E, -7.8),
        arrowstyle="<->", mutation_scale=14, color="black", lw=1.0))
    ax.text(-6.1, -8.25,
            r"$r_{\mathrm{mp}} \approx 10\,R_\oplus$",
            ha="center", va="top", fontsize=11)

    ax.set_xlim(-17, 14)
    ax.set_ylim(-9, 8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Pressure balance at the dayside magnetopause", fontsize=12)
    ax.legend(loc="lower right", frameon=True, fontsize=10)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


def main() -> None:
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
