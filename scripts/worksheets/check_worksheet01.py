"""Recompute every numerical answer printed in Worksheet 01 (Lectures 1-2).

Each value is recomputed from the rounded constants printed on the sheet,
following the same intermediate rounding the worked solutions hand forward, so
the script reproduces the digits a student obtains. A final section checks the
sheet's constants against IAU 2012 / JPL DE440 reference values, so the
rounding error a student inherits from the printed data stays explicit.

Run
---
python scripts/worksheets/check_worksheet01.py

Notes
-----
Reference values: astronomical unit and heliocentric gravitational constant
from JPL SSD astrodynamic constants (IAU 2012 Resolution B1); planetary
masses, radii and densities from JPL SSD planetary physical parameters.
Orbital periods of the Galilean moons are the sidereal periods quoted in the
Lecture 2 notes.
"""

from __future__ import annotations

import math

# ── Constants printed on the worksheet ──────────────────────
G = 6.674e-11  # m^3 kg^-1 s^-2
AU = 1.496e11  # m
YR = 3.156e7  # s
MSUN = 1.989e30  # kg
MEARTH = 5.972e24  # kg
REARTH = 6.371e6  # m
DAY = 86400.0  # s

# ── Reference values (IAU 2012 / JPL SSD) ───────────────────
AU_REF = 1.495978707e11  # m
GM_SUN_REF = 1.32712440041279419e20  # m^3 s^-2
YR_JULIAN = 365.25 * DAY  # s
MJUP_REF = 1.898125e27  # kg


def kepler_mass(a: float, period: float) -> float:
    """Central mass in kg from Newton's form of Kepler's third law.

    Parameters
    ----------
    a : float
        Semi-major axis in m.
    period : float
        Orbital period in s.

    Returns
    -------
    float
        Central mass in kg, valid for a negligible orbiter mass.
    """
    return 4.0 * math.pi**2 * a**3 / (G * period**2)


def vis_viva(r: float, a: float, gm: float) -> float:
    """Orbital speed in m/s at radius r on an orbit of semi-major axis a."""
    return math.sqrt(gm * (2.0 / r - 1.0 / a))


def roche_fluid(r_p: float, rho_p: float, rho_s: float) -> float:
    """Fluid Roche limit in the units of r_p."""
    return 2.46 * r_p * (rho_p / rho_s) ** (1.0 / 3.0)


def banner(text: str) -> None:
    print(f"\n{'=' * 72}\n{text}\n{'=' * 72}")


def rel(value: float, reference: float) -> str:
    """Signed relative difference of value and reference, in percent."""
    return f"{100.0 * (value / reference - 1.0):+.2f}%"


# ── Problem 1: weighing the Sun and Jupiter ─────────────────
banner("PROBLEM 1  Kepler's third law: the Sun and Jupiter")

r_jup, p_jup = 5.203 * AU, 11.86 * YR
msun_from_jup = kepler_mass(r_jup, p_jup)
print(f"(c) checkpoints: r = {r_jup:.4e} m, P = {p_jup:.4e} s")
print(f"    M_sun = {msun_from_jup:.4e} kg   ({rel(msun_from_jup, MSUN)} vs printed 1.989e30)")

# (b) judge: exact-form correction for a doubled Jupiter mass, from the table's 317.8 M_earth
mjup = 317.8 * MEARTH
dP_over_P = 0.5 * mjup / MSUN
print(f"(b) doubled Jupiter shortens P by ~{dP_over_P:.1e} (printed ~5e-4; claim 'noticeably longer' is false)")

# (c) coda: the computed mass is M_sun + M_Jup, and M_Jup/M_sun ~ 1e-3
ratio = mjup / MSUN
print(f"(c) M_Jup/M_sun = {ratio:.4e} (printed ~1e-3)")
print(f"    M_sun (1 + ratio) = {MSUN * (1 + ratio):.4e} kg vs computed {msun_from_jup:.4e}")

# ── Problem 2: vis-viva and the transfer to Mars ────────────
banner("PROBLEM 2  Vis-viva: minimum-energy transfer to Mars")

gm_sun = G * MSUN
r1, r2 = 1.000 * AU, 1.524 * AU
a_t = 0.5 * (r1 + r2)
print(f"(b) a_t = {a_t / AU:.4f} AU = {a_t:.5e} m ; GM = {gm_sun:.5e}")
p_t = 2.0 * math.pi * math.sqrt(a_t**3 / gm_sun)
print(f"    P_t = {p_t:.4e} s ; flight time = {0.5 * p_t:.4e} s = {0.5 * p_t / DAY:.1f} d")
print(f"    check via P[yr] = a[AU]^(3/2): {(a_t / AU) ** 1.5:.4f} yr, half = {(a_t / AU) ** 1.5 / 2:.4f} yr")

v_peri = vis_viva(r1, a_t, gm_sun)
v_apo = vis_viva(r2, a_t, gm_sun)
v_earth = math.sqrt(gm_sun / r1)
v_mars = math.sqrt(gm_sun / r2)
print(f"(c) v_p = {v_peri / 1e3:.2f} km/s, v_a = {v_apo / 1e3:.2f} km/s")
print(f"    given circular speeds: v_Earth = {v_earth / 1e3:.2f} km/s (printed 29.79), v_Mars = {v_mars / 1e3:.2f} km/s (printed 24.13)")
dv1, dv2 = round((v_peri - 29.79e3) / 1e3, 2), round((24.13e3 - v_apo) / 1e3, 2)
print(f"    dv1 = {dv1:.2f}, dv2 = {dv2:.2f}, total = {dv1 + dv2:.2f} km/s (printed 2.94 + 2.65 = 5.59)")

# ── Problem 3: the Laplace resonance ────────────────────────
banner("PROBLEM 3  The Laplace resonance of the Galilean moons")

p_io, p_eur, p_gan_d = 1.769, 3.551, 7.155
print(f"(a) P_Eur/P_Io = {p_eur / p_io:.5f}  ({100 * (p_eur / p_io / 2 - 1):+.2f}% from 2)")
print(f"    P_Gan/P_Eur = {p_gan_d / p_eur:.5f}  ({100 * (p_gan_d / p_eur / 2 - 1):+.2f}% from 2)")
print(f"    P_Gan/P_Io  = {p_gan_d / p_io:.5f}  ({100 * (p_gan_d / p_io / 4 - 1):+.2f}% from 4)")

n_io, n_eur, n_gan = 1.0 / p_io, 1.0 / p_eur, 1.0 / p_gan_d
lap = n_io - 3.0 * n_eur + 2.0 * n_gan
print(f"(a) coda: Laplace relation = {lap:+.7f} /d ; relative {lap / n_io:+.2e} (printed: three parts in 1e5)")

# (b) azimuths for the idealized 1:2:4 sketch (start: Io 180, Eur 0, Gan 0)
print("(b) azimuths (deg) at t Io-periods [Io, Eur, Gan]:")
for t in (0, 1, 2, 4):
    print(f"    t={t}: [{(180 + 360 * t) % 360:3d}, {(180 * t) % 360:3d}, {(90 * t) % 360:3d}]")

# ── Problem 4: tides and the Roche limit ────────────────────
banner("PROBLEM 4  Tides and the Roche limit")

r_sat, rho_sat = 5.8232e7, 687.0
d_solid = roche_fluid(r_sat, rho_sat, 1000.0)
print(f"(c) checkpoint (687/1000)^(1/3) = {(687 / 1000) ** (1 / 3):.4f}")
print(f"    d_R(solid ice) = {d_solid / 1e3:.0f} km = {d_solid / r_sat:.2f} R_Sat")
factor = 2.0 ** (1.0 / 3.0)
print(f"    porous factor 2^(1/3) = {factor:.2f} -> {factor * d_solid / 1e3:.0f} km = {factor * d_solid / r_sat:.2f} R_Sat")
print("    rings 67 000-137 000 km, F ring ~140 000 km")

# ── Problem 5: gravitational focusing ───────────────────────
banner("PROBLEM 5  Gravitational focusing and the growth regimes")

RHO_BODY = 3000.0


def escape_speed(radius: float) -> float:
    """Escape speed in m/s from a sphere of radius `radius` at RHO_BODY."""
    mass = 4.0 / 3.0 * math.pi * radius**3 * RHO_BODY
    return math.sqrt(2.0 * G * mass / radius)


v_small, v_big = escape_speed(5.0e4), escape_speed(5.0e5)
print(f"(a) v_esc: {v_small:.1f} m/s (50 km), {v_big:.1f} m/s (500 km); ratio {v_big / v_small:.2f}")
f_s, f_b = 1 + (v_small / 10) ** 2, 1 + (v_big / 10) ** 2
print(f"    focusing at 10 m/s: {f_s:.1f} and {f_b:.0f}")
print(f"    sigma ratio from printed factors = 100 x {4195 / 42.9:.1f} = {100 * 4195 / 42.9:.3g} (geometric: 100)")

g_s, g_b = 1 + (v_small / 500) ** 2, 1 + (v_big / 500) ** 2
print(f"(b) focusing at 500 m/s: {g_s:.2f} and {g_b:.2f}; advantage over R^2 = {g_b / g_s:.1f}")

# ── Reference cross-check ───────────────────────────────────
banner("CROSS-CHECK of the printed constants against IAU 2012 / JPL DE440")

print(f"AU printed / AU exact: {rel(AU, AU_REF)}")
print(f"yr printed / Julian yr: {rel(YR, YR_JULIAN)}")
print(f"G printed / CODATA: {rel(G, 6.67430e-11)}")
print(f"G*M_sun printed / GM_sun exact: {rel(G * MSUN, GM_SUN_REF)}")
print(f"M_Jup from table (317.8 M_earth) / JPL: {rel(mjup, MJUP_REF)}")
