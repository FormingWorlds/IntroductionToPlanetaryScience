"""The Rossiter-McLaughlin effect for three spin-orbit angles.

A rotating star has an approaching (blueshifted) and a receding (redshifted)
half. A transiting planet hides part of one half and then part of the other,
so the flux-weighted mean velocity of the remaining starlight changes during
the transit. The anomaly is computed on a pixel grid of a limb-darkened disk
in the first-moment approximation,

    dv = - sum(I v)_hidden / (sum(I)_star - sum(I)_hidden),

for the same planet and impact parameter on three orbits: aligned (lambda = 0),
misaligned (lambda = 60 deg) and retrograde (lambda = 180 deg). lambda is the
sky-projected angle between the stellar spin axis and the orbit normal.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, FancyArrowPatch

from scripts.figures._shared.style import apply_style, save_figure

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_AVIF = REPO_ROOT / "book/13_exoplanets/figures/rossiter_mclaughlin_obliquity.avif"

# Hot Jupiter around a Sun-like star: Rp/R* = 0.1, v sin i* = 5 km/s, P = 3 d.
K_RADIUS = 0.10
VSINI = 5000.0  # m/s
U_LIMB = 0.6  # linear limb-darkening coefficient
IMPACT = 0.35  # impact parameter in stellar radii
CROSS_SPEED = 2.0 / 2.6  # stellar radii per hour: a central transit lasts about 2.6 h
CASES = [
    {"lam": 0.0, "title": r"(a) Aligned, $\lambda = 0^\circ$"},
    {"lam": 60.0, "title": r"(b) Misaligned, $\lambda = 60^\circ$"},
    {"lam": 180.0, "title": r"(c) Retrograde, $\lambda = 180^\circ$"},
]
DOPPLER_CMAP = LinearSegmentedColormap.from_list("doppler", ["#1f6db8", "#f4f4f4", "#c0392b"])


def _star_grid(n: int = 801) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return the sky coordinates, the intensity and the line-of-sight velocity of the disk.

    The projected spin axis points up (+y); the left half (x < 0) approaches.
    """
    x = np.linspace(-1, 1, n)
    xx, yy = np.meshgrid(x, x)
    r2 = xx**2 + yy**2
    on_disk = r2 <= 1.0
    mu = np.sqrt(np.clip(1.0 - r2, 0.0, None))
    intensity = np.where(on_disk, 1.0 - U_LIMB * (1.0 - mu), 0.0)
    velocity = VSINI * xx
    return xx, yy, intensity, velocity


def _planet_path(lam_deg: float, t_hours: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Sky position of the planet centre at times t (hours from mid-transit).

    For lambda = 0 the planet moves left to right, below the stellar centre by
    the impact parameter; a rotation by lambda tilts the path on the sky.
    """
    s = CROSS_SPEED * t_hours
    lam = np.radians(lam_deg)
    x_orb, y_orb = s, -IMPACT * np.ones_like(s)
    x = x_orb * np.cos(lam) - y_orb * np.sin(lam)
    y = x_orb * np.sin(lam) + y_orb * np.cos(lam)
    return x, y


def rm_anomaly(lam_deg: float, t_hours: np.ndarray) -> np.ndarray:
    """Radial velocity anomaly (m/s) of the star during the transit."""
    xx, yy, intensity, velocity = _star_grid()
    total = intensity.sum()
    xp, yp = _planet_path(lam_deg, t_hours)
    dv = np.zeros_like(t_hours)
    for k, (xc, yc) in enumerate(zip(xp, yp)):
        hidden = (xx - xc) ** 2 + (yy - yc) ** 2 <= K_RADIUS**2
        f_hidden = intensity[hidden].sum()
        dv[k] = -(intensity[hidden] * velocity[hidden]).sum() / (total - f_hidden)
    return dv


def _disk_panel(ax: plt.Axes, lam_deg: float, title: str) -> None:
    """Draw the Doppler map of the star, the spin axis and the transit chord."""
    xx, yy, intensity, velocity = _star_grid(401)
    img = np.where(intensity > 0, velocity / VSINI, np.nan)
    ax.imshow(img, extent=(-1, 1, -1, 1), origin="lower", cmap=DOPPLER_CMAP, vmin=-1, vmax=1)
    ax.add_patch(Circle((0, 0), 1.0, fill=False, color="0.3", lw=0.8))
    ax.plot([0, 0], [-1.25, 1.3], color="black", lw=1.2)
    ax.add_patch(FancyArrowPatch((-0.22, 1.2), (0.22, 1.2), connectionstyle="arc3,rad=0.4", arrowstyle="-|>",
                                 mutation_scale=9, color="black", lw=1.0))
    ax.text(-0.95, 1.08, "approaching", fontsize=8.5, color="#1f6db8", ha="left")
    ax.text(0.95, 1.08, "receding", fontsize=8.5, color="#c0392b", ha="right")
    t = np.linspace(-1.75, 1.75, 50)
    xp, yp = _planet_path(lam_deg, t)
    ax.plot(xp, yp, color="black", ls="--", lw=1.0)
    # Direction of motion: an arrow head on the chord just inside the limb
    xa, ya = _planet_path(lam_deg, np.array([0.55, 0.8]) / CROSS_SPEED)
    ax.add_patch(FancyArrowPatch((xa[0], ya[0]), (xa[1], ya[1]), arrowstyle="-|>", mutation_scale=14,
                                 color="black", lw=1.4, zorder=5))
    x0, y0 = _planet_path(lam_deg, np.array([0.0]))
    ax.add_patch(Circle((x0[0], y0[0]), K_RADIUS, color="black", zorder=4))
    if 0.0 < lam_deg < 180.0:
        # lambda between the stellar equator direction and the planet's path
        ax.plot([x0[0], x0[0] + 0.55], [y0[0], y0[0]], color="black", ls=":", lw=1.0)
        arc = np.radians(np.linspace(0.0, lam_deg, 40))
        ax.plot(x0[0] + 0.38 * np.cos(arc), y0[0] + 0.38 * np.sin(arc), color="black", lw=1.0)
        mid = np.radians(lam_deg / 2)
        ax.text(x0[0] + 0.5 * np.cos(mid), y0[0] + 0.5 * np.sin(mid), r"$\lambda$", fontsize=11, ha="center",
                va="center")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=10)


def make_plot() -> plt.Figure:
    """Build the figure, save it and return it."""
    apply_style()
    fig, axes = plt.subplots(2, 3, figsize=(8.6, 5.2), gridspec_kw={"height_ratios": [1.15, 1.0]})
    t = np.linspace(-2.0, 2.0, 321)
    curves = [rm_anomaly(c["lam"], t) for c in CASES]
    vmax = 1.15 * max(np.abs(c).max() for c in curves)
    for col, (case, dv) in enumerate(zip(CASES, curves)):
        _disk_panel(axes[0, col], case["lam"], case["title"])
        ax = axes[1, col]
        ax.plot(t, dv, color="black", lw=1.6)
        ax.axhline(0, color="0.6", ls=":", lw=0.9)
        ax.set_xlim(t[0], t[-1])
        ax.set_ylim(-vmax, vmax)
        ax.set_xlabel("Time from mid-transit (h)", fontsize=9)
        if col == 0:
            ax.set_ylabel("RV anomaly (m/s)", fontsize=10)
        else:
            ax.set_yticklabels([])
    fig.tight_layout()
    save_figure(fig, OUT_AVIF, dpi=280)
    return fig


def main() -> None:
    """Generate the figure and report its path and peak anomalies."""
    fig = make_plot()
    t = np.linspace(-2.0, 2.0, 321)
    for case in CASES:
        dv = rm_anomaly(case["lam"], t)
        print(f"  lambda = {case['lam']:5.1f} deg: max {dv.max():6.1f} m/s, min {dv.min():6.1f} m/s")
    print(f"  plot : {OUT_AVIF}")
    plt.close(fig)


if __name__ == "__main__":
    main()
