"""Generate Fig. (`fig:prem-shadow-zones`).

Two-panel ray diagram of the seismic shadow zones, traced through the
PREM velocity model rather than sketched:

(a) P waves. Rays that bottom in the mantle emerge no further than
    98 deg from the source. Rays that reach the core-mantle boundary
    refract downward into the slower outer core and re-emerge only
    beyond the PKP caustic at 145 deg.
(b) S waves. Shear waves do not propagate through the liquid outer
    core, so every S ray bottoms in the mantle and none arrives
    beyond 103 deg.

Each ray is integrated from the conserved ray parameter
p = r sin(i) / v, which is constant along a ray in a spherically
symmetric body. A ray turns where r / v(r) = p, and its angular
distance follows from dtheta/dr = p / (r sqrt((r/v)^2 - p^2)).

Caption / figure id : `fig:prem-shadow-zones`
Markdown source     : book/08_interiors/interiors.md
Data                : PREM polynomial coefficients, Table 1 of
                      Dziewonski & Anderson (1981), via `_prem.py`
Citation key        : Dziewonski1981
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

from scripts.figures._shared.style import apply_style, save_figure

from ._prem import prem

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/08_interiors/figures/prem_shadow_zones.avif"

R_EARTH = 6371.0
R_CMB = 3480.0
R_ICB = 1221.5
# Radii at which PREM's velocity polynomials change branch. A ray is
# integrated one branch at a time so a discontinuity is never crossed
# inside a quadrature interval.
BRANCHES = [R_EARTH, 5701.0, R_CMB, R_ICB, 0.0]

MANTLE_FILL = "#efe9e2"
OUTER_CORE_FILL = "#f4c76a"
INNER_CORE_FILL = "#e08a3c"
P_RAY = "#1f5fa8"
CORE_RAY = "#7b3fa0"
S_RAY = "#b03a2e"
SHADOW_FILL = "#3d3d3d"


def slowness(r_km: np.ndarray, wave: str) -> np.ndarray:
    """Return r / v(r) in s/rad, infinite where the wave cannot travel."""
    _, v_p, v_s = prem(np.atleast_1d(r_km))
    v = v_p if wave == "P" else v_s
    return np.where(v > 0.0, r_km / np.where(v > 0.0, v, 1.0), np.inf)


def turning_point(p: float, wave: str) -> tuple[float | None, int | None]:
    """Deepest radius a ray of parameter `p` reaches, and its branch index."""
    for i in range(len(BRANCHES) - 1):
        top, bottom = BRANCHES[i], max(BRANCHES[i + 1], 1e-3)
        if slowness(np.array([bottom]), wave)[0] >= p:
            continue  # the ray passes straight through this branch
        lo, hi = bottom, top
        for _ in range(90):
            mid = 0.5 * (lo + hi)
            if slowness(np.array([mid]), wave)[0] < p:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi), i
    return None, None


def upgoing_leg(p: float, wave: str, n: int = 2000):
    """Radii and angular distances from the turning point to the surface."""
    r_turn, branch = turning_point(p, wave)
    if r_turn is None:
        return None, None
    radii, angles, theta = [], [], 0.0
    for i in range(branch, -1, -1):
        top = BRANCHES[i]
        bottom = r_turn if i == branch else BRANCHES[i + 1]
        if i == branch:
            # r = bottom + L s^2 clusters samples on the inverse-square-root
            # singularity at the turning point, and the substitution's own
            # Jacobian cancels it.
            s = np.linspace(0.0, 1.0, n)
            length = top - bottom
            r = bottom + length * s**2
            disc = np.maximum(slowness(r, wave) ** 2 - p * p, 0.0)
            with np.errstate(divide="ignore", invalid="ignore"):
                integrand = p / (r * np.sqrt(disc)) * 2.0 * length * s
            integrand[0] = integrand[1]
            step = np.diff(s)
        else:
            r = np.linspace(bottom, top, n)
            disc = np.maximum(slowness(r, wave) ** 2 - p * p, 0.0)
            with np.errstate(divide="ignore", invalid="ignore"):
                integrand = p / (r * np.sqrt(disc))
            integrand = np.where(np.isfinite(integrand), integrand, 0.0)
            step = np.diff(r)
        d_theta = np.concatenate(
            [[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * step)]
        )
        radii.append(r)
        angles.append(theta + d_theta)
        theta += d_theta[-1]
    return np.concatenate(radii), np.concatenate(angles)


def ray_path(p: float, wave: str):
    """Full source-to-receiver path as (x, y) with the source at the top."""
    r, theta = upgoing_leg(p, wave)
    if r is None:
        return None, None, None
    half = theta[-1]
    r_full = np.concatenate([r[::-1], r[1:]])
    th_full = np.concatenate([half - theta[::-1], half + theta[1:]])
    return r_full * np.sin(th_full), r_full * np.cos(th_full), np.degrees(2 * half)


def epicentral_distance(p: float, wave: str) -> float:
    """Angular distance in degrees between source and receiver."""
    _, theta = upgoing_leg(p, wave)
    return float(np.degrees(2 * theta[-1]))


def grazing_parameter(wave: str) -> float:
    """Ray parameter of the ray that just grazes the core-mantle boundary."""
    return float(slowness(np.array([R_CMB + 0.1]), wave)[0])


def pkp_caustic() -> tuple[float, float]:
    """Ray parameter and angular distance of the first PKP arrival."""
    grid = np.linspace(130.0, grazing_parameter("P") - 0.5, 400)
    distances = np.array([epicentral_distance(p, "P") for p in grid])
    i = int(np.argmin(distances))
    return float(grid[i]), float(distances[i])


def draw_earth(ax) -> None:
    """Layer discs, boundary rings, and the layer labels on the left half."""
    ax.add_patch(Circle((0, 0), R_EARTH, facecolor=MANTLE_FILL,
                        edgecolor="black", lw=1.2, zorder=0))
    ax.add_patch(Circle((0, 0), R_CMB, facecolor=OUTER_CORE_FILL,
                        edgecolor="black", lw=1.0, zorder=1))
    ax.add_patch(Circle((0, 0), R_ICB, facecolor=INNER_CORE_FILL,
                        edgecolor="black", lw=0.8, zorder=2))

    # Layer names sit on the ray-free left half, level with each layer.
    # The outer core is a 2260 km annulus, so its label is stacked to
    # keep the whole box inside the fill.
    for x_km, name in [
        (-0.5 * (R_CMB + R_EARTH), "Mantle"),
        (-0.55 * (R_ICB + R_CMB), "Outer\ncore"),
        (0.0, "Inner\ncore"),
    ]:
        ax.text(x_km, 0.0, name, ha="center", va="center", fontsize=9,
                color="black", zorder=6)


def draw_rim_scale(ax) -> None:
    """Angular distance ticks around the right half of the surface."""
    # 0 deg is left to the source marker, whose label occupies that spot.
    for degrees in range(30, 181, 30):
        angle = np.radians(degrees)
        x, y = np.sin(angle), np.cos(angle)
        ax.plot([R_EARTH * x, 1.045 * R_EARTH * x],
                [R_EARTH * y, 1.045 * R_EARTH * y],
                color="0.35", lw=0.8, zorder=5)
        label_r = 1.20 * R_EARTH
        ax.text(label_r * x, label_r * y, f"{degrees}°",
                ha="center", va="center", fontsize=8.5, color="0.3", zorder=5)


def draw_shadow(ax, start_deg: float, end_deg: float) -> None:
    """Shade the surface arc that receives no direct arrival."""
    ax.add_patch(Wedge((0, 0), 1.075 * R_EARTH, 90.0 - end_deg, 90.0 - start_deg,
                       width=0.075 * R_EARTH, facecolor=SHADOW_FILL,
                       edgecolor="none", alpha=0.75, zorder=4))


def draw_source(ax) -> None:
    ax.plot([0], [R_EARTH], marker="*", markersize=15, color="black",
            zorder=7, clip_on=False)
    ax.text(0, 1.19 * R_EARTH, "Earthquake", ha="center", va="center",
            fontsize=9.5, zorder=7)


def draw_ray_key(ax, entries) -> None:
    """Colour key for the ray families, in the free space above the rim."""
    for i, (colour, label) in enumerate(entries):
        ax.text(-1.33 * R_EARTH, (1.17 - 0.11 * i) * R_EARTH, label,
                color=colour, ha="left", va="center", fontsize=9.5, zorder=6)


def panel_p(ax) -> tuple[float, float]:
    graze = grazing_parameter("P")
    p_caustic, d_caustic = pkp_caustic()
    d_direct = epicentral_distance(graze + 0.05, "P")

    draw_earth(ax)
    for p in np.linspace(graze + 0.05, 900.0, 13):
        x, y, _ = ray_path(float(p), "P")
        ax.plot(x, y, color=P_RAY, lw=0.9, zorder=3)
    for p in np.linspace(p_caustic, 250.0, 5):
        x, y, _ = ray_path(float(p), "P")
        ax.plot(x, y, color=CORE_RAY, lw=0.9, zorder=3)

    draw_shadow(ax, d_direct, d_caustic)
    draw_rim_scale(ax)
    draw_source(ax)
    draw_ray_key(ax, [(P_RAY, "P through the mantle"),
                      (CORE_RAY, "PKP through the core")])
    ax.set_title("(a) P waves: refracted into the core", fontsize=11)
    return d_direct, d_caustic


def panel_s(ax) -> float:
    graze = grazing_parameter("S")
    d_direct = epicentral_distance(graze + 0.05, "S")

    draw_earth(ax)
    for p in np.linspace(graze + 0.05, 1600.0, 13):
        x, y, _ = ray_path(float(p), "S")
        ax.plot(x, y, color=S_RAY, lw=0.9, zorder=3)

    draw_shadow(ax, d_direct, 180.0)
    draw_rim_scale(ax)
    draw_source(ax)
    draw_ray_key(ax, [(S_RAY, "S through the mantle")])
    ax.set_title("(b) S waves: stopped at the liquid core", fontsize=11)
    return d_direct


def annotate_shadow(ax, text: str, degrees: float) -> None:
    """Label a shaded arc from outside the rim, on a leader line.

    The angle is chosen midway between two rim ticks so the leader line
    never crosses a distance label.
    """
    angle = np.radians(degrees)
    tip = 1.10 * R_EARTH
    tail = 1.42 * R_EARTH
    ax.annotate(
        text,
        xy=(tip * np.sin(angle), tip * np.cos(angle)),
        xytext=(tail * np.sin(angle), tail * np.cos(angle)),
        ha="left", va="center", fontsize=9.5, color="0.15", zorder=8,
        arrowprops=dict(arrowstyle="-", color="0.45", lw=0.8),
    )


def make_plot() -> Path:
    apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.8))
    d_direct_p, d_caustic = panel_p(axes[0])
    d_direct_s = panel_s(axes[1])

    annotate_shadow(axes[0],
                    f"P shadow zone\n{d_direct_p:.0f}° to {d_caustic:.0f}°",
                    111.0)
    annotate_shadow(axes[1],
                    f"S shadow zone\nbeyond {d_direct_s:.0f}°",
                    135.0)

    for ax in axes:
        ax.set_xlim(-1.35 * R_EARTH, 1.90 * R_EARTH)
        ax.set_ylim(-1.32 * R_EARTH, 1.32 * R_EARTH)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout()
    return save_figure(fig, OUT_AVIF, avif_quality=80, dpi=300)


def main() -> None:
    print(f"  P grazing the CMB reaches   : {epicentral_distance(grazing_parameter('P') + 0.05, 'P'):.1f} deg")
    print(f"  first PKP arrival (caustic) : {pkp_caustic()[1]:.1f} deg")
    print(f"  S grazing the CMB reaches   : {epicentral_distance(grazing_parameter('S') + 0.05, 'S'):.1f} deg")
    out = make_plot()
    print(f"  plot : {out}")


if __name__ == "__main__":
    main()
