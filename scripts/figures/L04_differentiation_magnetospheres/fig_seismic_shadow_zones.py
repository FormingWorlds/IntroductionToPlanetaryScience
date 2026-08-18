"""Generate Fig. (`fig:seismic-shadow-zones`).

Two-panel schematic of how P- and S-wave shadow zones constrain the
structure of Earth's core:

(a) S waves: transverse waves are absorbed at the core-mantle boundary
    because the liquid outer core cannot support shear, so no direct S
    wave arrives beyond an epicentral distance of ~103 degrees. The
    absence of S waves over the whole far hemisphere reveals that the
    outer core is liquid.
(b) P waves: compressional waves are transmitted, but the drop in
    P-wave velocity across the core-mantle boundary (~13.7 to ~8 km/s)
    refracts core-transiting rays steeply downward, so no direct P wave
    arrives between ~103 and ~143 degrees (the P-wave shadow zone) and
    the refracted PKP rays emerge beyond ~143 degrees. Waves refracted
    a second time through the solid inner core (PKIKP) arrive inside
    the shadow zone, which is how the inner core was found.

Geometry: radii to scale (R = 6371 km, CMB at r = 3480 km, ICB at
r = 1220 km). Mantle ray paths are schematic circular-arc-like curves
r(s) = R - d_max sin(pi s) whose bottoming depth d_max grows with
epicentral distance and reaches the CMB at 103 degrees; core-transiting
rays are drawn as straight chords with refraction kinks at each
boundary crossing. Ray paths are illustrative, not traced through a
velocity model.

Caption / figure id : `fig:seismic-shadow-zones`
Markdown source     : book/04_differentiation_magnetospheres/differentiation_magnetospheres.md
Citation key        : Oldham1906
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

from scripts.figures._shared.style import apply_style, save_figure


REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = (REPO_ROOT /
            "book/04_differentiation_magnetospheres/figures/seismic_shadow_zones.avif")

R_SURF = 1.0
R_CMB = 3480.0 / 6371.0          # 0.546
R_ICB = 1220.0 / 6371.0          # 0.192
DELTA_GRAZE = 103.0              # deg, last direct mantle ray grazes the CMB
DELTA_PKP = 143.0                # deg, first PKP arrival

C_P = "#1f77b4"                  # P rays, matches V_p in the PREM figure
C_S = "#d62728"                  # S rays, matches V_s in the PREM figure
C_MANTLE = "#f5deb3"
C_OUTER = "#cfe3f2"
C_INNER = "0.62"


def _xy(r: np.ndarray, ang_deg: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    a = np.deg2rad(ang_deg)
    return r * np.cos(a), r * np.sin(a)


def mantle_ray(delta: float, side: int, n: int = 200):
    """Direct mantle ray from the source (top) to epicentral distance delta."""
    s = np.linspace(0.0, 1.0, n)
    d_max = (R_SURF - R_CMB) * (delta / DELTA_GRAZE) ** 1.5
    r = R_SURF - d_max * np.sin(np.pi * s)
    ang = 90.0 - side * delta * s
    return _xy(r, ang)


def absorbed_s_ray(delta: float, side: int, n: int = 200):
    """Mantle-ray path truncated where it first reaches the CMB."""
    d_max = (R_SURF - R_CMB) * (delta / DELTA_GRAZE) ** 1.5
    s_hit = np.arcsin((R_SURF - R_CMB) / d_max) / np.pi
    s = np.linspace(0.0, s_hit, n)
    r = R_SURF - d_max * np.sin(np.pi * s)
    ang = 90.0 - side * delta * s
    return _xy(r, ang)


def leg(phi0: float, phi1: float, r0: float, r1: float, n: int = 60):
    """Straight-in-(r, angle) segment between two boundary points."""
    s = np.linspace(0.0, 1.0, n)
    return _xy(r0 + (r1 - r0) * s, phi0 + (phi1 - phi0) * s)


def draw_earth(ax: plt.Axes, label_layers: bool) -> None:
    ax.add_patch(Circle((0, 0), R_SURF, facecolor=C_MANTLE,
                        edgecolor="0.3", lw=1.2, zorder=1))
    ax.add_patch(Circle((0, 0), R_CMB, facecolor=C_OUTER,
                        edgecolor="0.35", lw=1.0, zorder=2))
    ax.add_patch(Circle((0, 0), R_ICB, facecolor=C_INNER,
                        edgecolor="0.3", lw=1.0, zorder=3))
    ax.plot(0, R_SURF, marker=(5, 1, 0), ms=17, color="#e6b800",
            mec="0.2", mew=0.8, zorder=6, clip_on=False)
    ax.annotate("earthquake", xy=(0, R_SURF + 0.16), fontsize=9.5,
                ha="center", color="0.15", zorder=6)
    if label_layers:
        ax.annotate("mantle", xy=(0.0, -0.76), fontsize=9, ha="center",
                    color="#7a5c1e", zorder=6)
        ax.annotate("outer core\n(liquid)", xy=(0.0, 0.31), fontsize=9,
                    ha="center", color="#1a4a6e", zorder=6)
        ax.annotate("inner core\n(solid)", xy=(0.0, 0.0), fontsize=7,
                    ha="center", va="center", color="white", zorder=6)


def shadow_wedge(ax: plt.Axes, th1: float, th2: float, color: str) -> None:
    ax.add_patch(Wedge((0, 0), R_SURF + 0.085, th1, th2, width=0.085,
                       facecolor=color, alpha=0.45, edgecolor="none",
                       zorder=0))


def arrival_arrow(ax, x, y, color, ls="-"):
    """Short outward arrowhead where a ray reaches the surface."""
    r = np.hypot(x[-1], y[-1])
    ux, uy = x[-1] / r, y[-1] / r
    ax.annotate("", xy=(x[-1] + 0.045 * ux, y[-1] + 0.045 * uy),
                xytext=(x[-1] - 0.001 * ux, y[-1] - 0.001 * uy),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4,
                                ls=ls), zorder=5)


def draw_s_panel(ax: plt.Axes) -> None:
    draw_earth(ax, label_layers=True)
    shadow_wedge(ax, 90.0 + DELTA_GRAZE, 90.0 - DELTA_GRAZE + 360.0, C_S)

    for side in (+1, -1):
        for delta in (30, 60, 90, DELTA_GRAZE):
            x, y = mantle_ray(delta, side)
            ax.plot(x, y, color=C_S, lw=1.5, zorder=4)
            arrival_arrow(ax, x, y, C_S)
        x, y = absorbed_s_ray(135, side)
        ax.plot(x, y, color=C_S, lw=1.5, zorder=4)
        ax.plot(x[-1], y[-1], "x", color=C_S, ms=9, mew=2.2, zorder=5)

    end_x, end_y = absorbed_s_ray(135, +1)
    ax.annotate("absorbed: the liquid\ncarries no shear waves",
                xy=(end_x[-1] + 0.02, end_y[-1] + 0.02),
                xytext=(1.30, 0.90), fontsize=8.5, ha="center",
                color=C_S, zorder=6,
                arrowprops=dict(arrowstyle="->", color=C_S, lw=1.0,
                                shrinkB=6))
    ax.annotate("103°", xy=(1.24, -0.22), fontsize=9, ha="center",
                color="0.15")
    ax.annotate("103°", xy=(-1.24, -0.22), fontsize=9, ha="center",
                color="0.15")
    ax.annotate("no direct S waves beyond 103°", xy=(0, -1.22),
                fontsize=9.5, ha="center", color=C_S)
    ax.set_title("(a) S waves: stopped by the liquid outer core",
                 fontsize=11)


def draw_p_panel(ax: plt.Axes) -> None:
    draw_earth(ax, label_layers=False)
    shadow_wedge(ax, 90.0 + DELTA_GRAZE, 90.0 + DELTA_PKP, C_P)
    shadow_wedge(ax, 90.0 - DELTA_PKP, 90.0 - DELTA_GRAZE, C_P)

    for side in (+1, -1):
        for delta in (30, 60, 90, DELTA_GRAZE):
            x, y = mantle_ray(delta, side)
            ax.plot(x, y, color=C_P, lw=1.5, zorder=4)
            arrival_arrow(ax, x, y, C_P)

    # PKP rays: mantle leg (30 deg), refracted chord across the outer
    # core, symmetric exit leg; arrivals at 150 and 180 degrees.
    for side, delta in ((+1, 150.0), (-1, 150.0), (+1, 180.0)):
        phi_leg = 30.0
        phi_core = delta - 2.0 * phi_leg
        a_e1 = 90.0 - side * phi_leg
        a_e2 = a_e1 - side * phi_core
        a_arr = 90.0 - side * delta
        segs = [leg(90.0, a_e1, R_SURF, R_CMB),
                leg(a_e1, a_e2, R_CMB, R_CMB, n=120),
                leg(a_e2, a_arr, R_CMB, R_SURF)]
        # bow the outer-core chord into a true straight line
        a = np.deg2rad(np.linspace(a_e1, a_e2, 120))
        p1 = np.array([R_CMB * np.cos(np.deg2rad(a_e1)),
                       R_CMB * np.sin(np.deg2rad(a_e1))])
        p2 = np.array([R_CMB * np.cos(np.deg2rad(a_e2)),
                       R_CMB * np.sin(np.deg2rad(a_e2))])
        chord = np.outer(np.linspace(0, 1, 120), p2 - p1) + p1
        segs[1] = (chord[:, 0], chord[:, 1])
        for i, (x, y) in enumerate(segs):
            ax.plot(x, y, color=C_P, lw=1.5, zorder=4)
        arrival_arrow(ax, segs[-1][0], segs[-1][1], C_P)

    # PKIKP: refracted again at the inner-core boundary, crosses the
    # solid inner core, arrives inside the shadow zone at 125 degrees.
    delta, phi_leg, phi_ic = 125.0, 20.0, 45.0
    a_e1 = 90.0 - phi_leg
    a_arr = 90.0 - delta
    a_e2 = a_arr + phi_leg
    a_mid = 0.5 * (a_e1 + a_e2)
    a_i1, a_i2 = a_mid + phi_ic, a_mid - phi_ic
    pts = [(R_SURF, 90.0), (R_CMB, a_e1), (R_ICB, a_i1),
           (R_ICB, a_i2), (R_CMB, a_e2), (R_SURF, a_arr)]
    xs, ys = [], []
    for (r1, f1), (r2, f2) in zip(pts[:-1], pts[1:]):
        q1 = np.array(_xy(np.array([r1]), np.array([f1]))).ravel()
        q2 = np.array(_xy(np.array([r2]), np.array([f2]))).ravel()
        t = np.linspace(0, 1, 60)
        xs.append(q1[0] + (q2[0] - q1[0]) * t)
        ys.append(q1[1] + (q2[1] - q1[1]) * t)
    x = np.concatenate(xs)
    y = np.concatenate(ys)
    ax.plot(x, y, color=C_P, lw=1.5, ls="--", zorder=4)
    arrival_arrow(ax, x, y, C_P, ls="--")

    ax.annotate("PKIKP: through the\nsolid inner core,\narrives in the shadow",
                xy=(1.02, -0.80), fontsize=8.5, ha="left", color=C_P,
                zorder=6)
    ax.annotate("PKP", xy=(0.0, -1.16), fontsize=9.5, ha="center",
                color=C_P)
    ax.annotate("shadow zone\n103° to 143°", xy=(-1.30, -0.62),
                fontsize=9, ha="center", color="#14507a")
    kx, ky = _xy(np.array([R_CMB]), np.array([120.0]))
    ax.annotate("refracted at the\ncore-mantle boundary",
                xy=(float(kx[0]), float(ky[0])),
                xytext=(-1.30, 0.95), fontsize=8.5, ha="center",
                color="#14507a", zorder=6,
                arrowprops=dict(arrowstyle="->", color="#14507a",
                                lw=1.0, shrinkB=2))
    ax.set_title("(b) P waves: refracted by the core", fontsize=11)


def make_plot() -> Path:
    apply_style()
    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.2, 5.9))
    for ax in (ax_a, ax_b):
        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-1.45, 1.30)
        ax.set_aspect("equal")
        ax.axis("off")
    draw_s_panel(ax_a)
    draw_p_panel(ax_b)
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80)


if __name__ == "__main__":
    out = make_plot()
    print(out)
