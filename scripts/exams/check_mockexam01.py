"""Recompute every numerical value printed in Mock exam 1.

Each value is recomputed from the constants printed in the exam's data box,
following the same intermediate rounding the worked solutions hand forward,
and compared against the digits printed on the sheet. The script fails loudly
on any mismatch and prints ``ALL OK (N checks)`` when every printed number
reproduces.

Run
---
python scripts/exams/check_mockexam01.py
"""

from __future__ import annotations

import math

from _checker_common import SIGMA, check, check_points, teq, verdict

# ── Constants and data printed on the exam ──────────────────
# SIGMA (Stefan-Boltzmann) is imported above with the shared helpers.
G = 6.674e-11  # m^3 kg^-1 s^-2
AU = 1.496e11  # m
YR_D = 365.25  # d
DAY = 86400.0  # s
MSUN = 1.989e30  # kg
RSUN = 6.957e8  # m
RJUP_KM = 71492.0  # km
KB = 1.381e-23  # J K^-1
MU_ATOMIC = 1.661e-27  # kg
S0 = 1361.0  # W m^-2 at 1 AU

A_VENUS, ALB_VENUS = 0.723, 0.77
T_VENUS, P_VENUS_BAR = 737.0, 92.0
G_VENUS, MU_VENUS, CP_VENUS = 8.87, 43.4, 1130.0
A_MARS, ALB_MARS, T_MARS = 1.524, 0.25, 215.0
ALB_EARTH, Q_EARTH = 0.30, 0.092
M_IO, R_IO, L_IO = 8.93e22, 1.821e6, 1e14
M_EARTH = 5.972e24  # kg
H_RADIOGENIC = 5e-12  # W kg^-1
THALF_K40 = 1.25  # Gyr
AGE_SS = 4.567  # Gyr

gm_sun = G * MSUN

# ── Problem 1: Route to Venus ───────────────────────────────
print("Problem 1  Route to Venus")
p_venus_yr = A_VENUS**1.5
check("(a) P_Venus [yr]", p_venus_yr, 0.6148)
check("(a) P_Venus [d]", p_venus_yr * YR_D, 224.5)

a_t = 0.5 * (1.000 + A_VENUS)
check("(b) a_t [AU]", a_t, 0.8615)
t_flight_yr = 0.5 * a_t**1.5
check("(b) flight [yr]", t_flight_yr, 0.39981)
check("(b) flight [d] checkpoint", t_flight_yr * YR_D, 146.0)

r_aph = 1.000 * AU
v_aph = math.sqrt(gm_sun * (2.0 / r_aph - 1.0 / (a_t * AU)))
v_earth = math.sqrt(gm_sun / r_aph)
check("(c) GM_sun", gm_sun, 1.3275e20)
check("(c) v_aphelion [km/s]", v_aph / 1e3, 27.29)
check("(c) v_circ Earth [km/s]", v_earth / 1e3, 29.79)
check("(c) dv retrograde [km/s]", (v_earth - v_aph) / 1e3, 2.50, rtol=2e-3)

s_syn_yr = 1.0 / (1.0 / p_venus_yr - 1.0)
check("(d) 1/P_V [1/yr]", 1.0 / p_venus_yr, 1.6266)
check("(d) 1/S [1/yr]", 1.0 / p_venus_yr - 1.0, 0.6266)
check("(d) S [yr]", s_syn_yr, 1.5958)
check("(d) S [d]", s_syn_yr * YR_D, 582.9)

phase_venus = 360.0 * t_flight_yr / p_venus_yr
check("(e) Venus arc [deg]", phase_venus, 234.1)
check("(e) trail angle [deg]", phase_venus - 180.0, 54.1, rtol=1e-3)

# ── Problem 2: Beneath the clouds of Venus ──────────────────
print("Problem 2  Beneath the clouds of Venus")
h_venus = KB * T_VENUS / (MU_VENUS * MU_ATOMIC * G_VENUS)
check("(a) H [km] checkpoint", h_venus / 1e3, 15.92, rtol=1e-3)
check("(a) numerator", KB * T_VENUS, 1.0178e-20)
check("(a) denominator", MU_VENUS * MU_ATOMIC * G_VENUS, 6.3942e-25)

z_1bar = h_venus * math.log(P_VENUS_BAR)
check("(b) ln 92", math.log(P_VENUS_BAR), 4.5218)
check("(b) z(1 bar) [km]", z_1bar / 1e3, 71.98, rtol=1e-3)

lapse = G_VENUS / CP_VENUS
check("(c) Gamma [K/km]", lapse * 1e3, 7.85, rtol=1e-3)
check("(c) T(50 km) [K]", T_VENUS - lapse * 50e3, 344.5)

s_venus = S0 / A_VENUS**2
check("(d) S_Venus", s_venus, 2603.6)
abs_venus = s_venus / 4.0 * (1.0 - ALB_VENUS)
abs_earth = S0 / 4.0 * (1.0 - ALB_EARTH)
check("(d) absorbed Venus", abs_venus, 149.7)
check("(d) absorbed Earth", abs_earth, 238.2)
check("(d) Teq Venus", teq(s_venus, ALB_VENUS), 227.0, rtol=2e-3)
check("(d) Teq Earth", teq(S0, ALB_EARTH), 255.0, rtol=2e-3)

# ── Problem 3: Io's heat engine ─────────────────────────────
print("Problem 3  Io's heat engine")
vol_io = 4.0 / 3.0 * math.pi * R_IO**3
check("(a) volume", vol_io, 2.5294e19)
check("(a) density", M_IO / vol_io, 3530.0)

area_io = 4.0 * math.pi * R_IO**2
check("(b) area", area_io, 4.1672e13)
q_io = L_IO / area_io
check("(b) flux", q_io, 2.400, rtol=1e-3)
check("(b) ratio to Earth", q_io / Q_EARTH, 26.0, rtol=5e-3)
check("(b) Io/Earth mass [%]", M_IO / M_EARTH * 100.0, 1.5, rtol=1e-2)

l_rad = H_RADIOGENIC * M_IO
check("(d) radiogenic power", l_rad, 4.465e11)
check("(d) shortfall factor", L_IO / l_rad, 220.0, rtol=2e-2)

# ── Problem 4: Reading time from rock ───────────────────────
print("Problem 4  Reading time from rock")
frac = 1.0 / (1.0 + 7.0)
check("(b) K remaining checkpoint", frac, 0.125)
check("(b) age [Gyr]", THALF_K40 * math.log(8.0) / math.log(2.0), 3.75)

check("(c) K40 factor", 2.0 ** (AGE_SS / THALF_K40), 12.6, rtol=2e-3)

# ── Problem 5: The climate history of Mars ──────────────────
print("Problem 5  The climate history of Mars")
s_mars = S0 / A_MARS**2
check("(a) a^2", A_MARS**2, 2.3226)
check("(a) S_Mars checkpoint", s_mars, 586.0)
t_eq_mars = teq(s_mars, ALB_MARS)
check("(a) argument", s_mars * (1.0 - ALB_MARS) / (4.0 * SIGMA), 1.9378e9)
check("(a) Teq Mars", t_eq_mars, 209.8)
check("(a) greenhouse [K]", T_MARS - t_eq_mars, 5.0, rtol=5e-2)
check("(a) Earth/Mars greenhouse", 33.0 / (T_MARS - t_eq_mars), 6.0, rtol=1e-1)

check("(b) early water [m GEL]", 6.0 * 25.0, 150.0)

abs_mars_at_venus = S0 / A_VENUS**2 / 4.0 * (1.0 - ALB_MARS)
check("(d) absorbed flux", abs_mars_at_venus, 488.2)

# ── Problem 6: A planet from a light curve ──────────────────
print("Problem 6  A planet from a light curve")
r_p = math.sqrt(0.0100) * RSUN
check("(a) R_p [m]", r_p, 6.957e7)
check("(a) R_p [km]", r_p / 1e3, 69570.0)
check("(a) R_p [R_Jup]", r_p / 1e3 / RJUP_KM, 0.973, rtol=1e-3)

p_orb = 3.50 * DAY
check("(b) P [s]", p_orb, 3.024e5)
a3 = gm_sun * p_orb**2 / (4.0 * math.pi**2)
check("(b) numerator", gm_sun * p_orb**2, 1.2139e31)
check("(b) a^3", a3, 3.0749e29)
a_m = a3 ** (1.0 / 3.0)
check("(b) a [m]", a_m, 6.750e9)
check("(b) a [AU] checkpoint", a_m / AU, 0.04512, rtol=1e-3)
check("(b) AU-yr route [AU]", (3.50 / YR_D) ** (2.0 / 3.0), 0.0451, rtol=2e-3)
check("(b) a in stellar radii", a_m / RSUN, 9.7, rtol=2e-2)
check("(b) Earth/planet a ratio", AU / a_m, 22.0, rtol=1e-2)

a_au = a_m / AU
s_planet = S0 / a_au**2
check("(c) a^2 [AU^2]", a_au**2, 2.0358e-3)
check("(c) S at planet", s_planet, 6.685e5, rtol=1e-3)
check("(c) flux ratio to Earth", s_planet / S0, 490.0, rtol=5e-3)
check("(c) argument", s_planet * 0.90 / (4.0 * SIGMA), 2.6529e12, rtol=1e-3)
check("(c) Teq [K]", teq(s_planet, 0.10), 1276.0, rtol=1e-3)

# ── Marks bookkeeping and verdict ───────────────────────────
print("Marks")
check_points("mockexam01/mockexam01_content.tex")

verdict()
