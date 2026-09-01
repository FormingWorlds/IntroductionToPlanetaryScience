"""Verify every printed number in mock exam 3 against an independent recomputation.

Each check reproduces the arithmetic chain exactly as the solutions print it,
including the intermediate rounding to 4 significant figures that the solutions
hand forward between steps.

Run
---
python scripts/exams/check_mockexam03.py
"""

from __future__ import annotations

import math

from _checker_common import SIGMA, check, check_points, teq, verdict

# ── Constants and data printed on the exam ──────────────────
G = 6.674e-11  # m^3 kg^-1 s^-2
AU = 1.496e11  # m
YR = 3.156e7  # s
DAY = 86400.0  # s
KB = 1.381e-23  # J/K
MU_ATOMIC = 1.661e-27  # kg, atomic mass unit
S0 = 1361.0  # W/m^2

# Data table values used below
RSUN = 6.957e8  # m
RJUP = 6.9911e7  # m
A_CAL = 1.883e9  # m, Callisto orbit
P_CAL_D = 16.69  # d, Callisto period
G_EARTH = 9.81  # m/s^2
G_MOON = 1.62  # m/s^2
R_MERC = 2.440e6  # m
RHO_MERC = 5427.0  # kg/m^3

# ── Problem 1: Weighing the Sun and Jupiter ─────────────────
print("Problem 1  Weighing the Sun and Jupiter")
num_sun = 4 * math.pi**2 * AU**3
den_sun = G * YR**2
check("(a) 4 pi^2 a^3 [numerator]", num_sun, 1.3218e35)
check("(a) G P^2 [denominator]", den_sun, 6.6475e4)
msun = num_sun / den_sun
check("(a) M_sun [kg]", msun, 1.988e30)
p_cal = P_CAL_D * DAY
check("(b) P_Callisto [s]", p_cal, 1.442e6)
num_jup = 4 * math.pi**2 * A_CAL**3
den_jup = G * p_cal**2
check("(b) numerator", num_jup, 2.6358e29)
check("(b) denominator", den_jup, 1.3878e2)
mjup = 2.6358e29 / 1.3878e2
check("(b) M_Jup [kg]", mjup, 1.899e27)
rho_sun = 1.988e30 / (4 / 3 * math.pi * RSUN**3)
check("(c) mean density Sun [kg/m^3]", rho_sun, 1409.0)
rho_jup = 1.899e27 / (4 / 3 * math.pi * RJUP**3)
check("(c) mean density Jupiter [kg/m^3]", rho_jup, 1327.0)
check("(b) Jupiter/Sun mass ratio ~1e-3", mjup / msun, 1e-3, rtol=5e-2)

# ── Problem 2: Reading a cratered surface ───────────────────
print("Problem 2  Reading a cratered surface")
m_imp = 4 / 3 * math.pi * 600.0**3 * 3000.0
check("(a) impactor mass [kg]", m_imp, 2.714e12)
e_imp = 0.5 * 2.714e12 * (1.8e4) ** 2
check("(a) kinetic energy [J]", e_imp, 4.397e20)
e_h = 4.397e20  # checkpoint value handed forward
check("(a) ratio to largest nuclear test ~2000", e_h / (50 * 4.184e15), 2000.0, rtol=6e-2)
x_moon = e_h / (2500.0 * G_MOON)
check("(b) E/(rho_t g) Moon", x_moon, 1.0857e17)
d_moon = x_moon**0.25
check("(b) crater D Moon [m]", d_moon, 1.815e4)
check("(b) crater D Moon [km]", d_moon / 1e3, 18.15)
t_plain = 1.8e-3 / 8.38e-4
check("(c) surface age [Gyr]", t_plain, 2.148)

# ── Problem 3: The birth of a core and a dynamo ─────────────
print("Problem 3  The birth of a core and a dynamo")
lam = 0.6931 / 8.9
check("(a) lambda [1/Myr]", lam, 7.788e-2)
lam_h = 7.788e-2
check("(a) exponent at 30 Myr", lam_h * 30, 2.3364)
frac30 = math.exp(-2.3364)
check("(a) fraction left at 30 Myr", frac30, 9.668e-2)
frac45 = math.exp(-lam_h * 45)
check("(a) fraction left at 45 Myr ~3%", frac45, 0.03, rtol=5e-3)
rm = 5e-4 * 1.8e6 / 1.0
check("(b) magnetic Reynolds number", rm, 900.0)

# ── Problem 4: Cloud bases on Earth and Titan ───────────────
print("Problem 4  Cloud bases on Earth and Titan")
h_earth = KB * 288.0 / (28.97 * MU_ATOMIC * G_EARTH)
check("(a) scale height Earth [m]", h_earth, 8426.0)
check("(b) 1/273 [1/K]", 1 / 273, 3.6630e-3)
lnratio = math.log(1700.0 / 611.0)
check("(b) ln(1700/611)", lnratio, 1.0233)
inv_td = 3.6630e-3 - 1.0233 / 5400.0
check("(b) 1/T_d [1/K]", inv_td, 3.4735e-3)
td = 1 / 3.4735e-3
check("(b) dew point [K]", td, 287.9)
z_cb = (303.0 - 287.9) / 9.8
check("(b) cloud base [km]", z_cb, 1.541)
expo_m = -980.0 * (1 / 94 - 1 / 90.7)
check("(c) exponent", expo_m, 0.3793)
psat94 = 1.17e4 * math.exp(0.3793)
check("(c) P_sat CH4(94 K) [Pa]", psat94, 1.710e4)
p_ch4 = 0.05 * 1.5e5
check("(c) CH4 partial pressure [Pa]", p_ch4, 7.5e3)
check("(c) relative humidity", p_ch4 / 1.710e4, 0.44, rtol=5e-3)

# ── Problem 5: Mercury, the shrinking planet ────────────────
print("Problem 5  Mercury, the shrinking planet")
m_merc = 4 / 3 * math.pi * R_MERC**3 * RHO_MERC
check("(a) Mercury mass [kg]", m_merc, 3.302e23)
e_cool = 3.302e23 * 800.0 * 200.0
check("(a) cooling energy [J]", e_cool, 5.283e28)
t_45 = 4.5e9 * YR
check("(b) 4.5 Gyr [s]", t_45, 1.4202e17)
p_avg = 5.283e28 / 1.4202e17
check("(b) mean power [W]", p_avg, 3.720e11)
area = 4 * math.pi * R_MERC**2
check("(b) surface area [m^2]", area, 7.4815e13)
q_flux = 3.720e11 / 7.4815e13
check("(b) heat flux [W/m^2]", q_flux, 4.972e-3)
check("(b) Earth/Mercury flux ratio ~17", 87.0 / (q_flux * 1e3), 17.0, rtol=3e-2)
dr = 3e-5 / 3 * R_MERC * 200.0
check("(c) radius contraction [m]", dr, 4880.0)

# ── Problem 6: A planet around a K dwarf ────────────────────
print("Problem 6  A planet around a K dwarf")
lum = 0.7**3.5
check("(a) L/Lsun", lum, 0.2870)
check("(a) luminosity drop factor ~3.5", 1 / lum, 3.5, rtol=5e-3)
d_hz = math.sqrt(0.2870)
check("(b) equal-flux distance [AU]", d_hz, 0.5357)
arg_hz = S0 * 0.70 / (4 * SIGMA)
check("(b) T_eq^4 argument", arg_hz, 4.2006e9)
check("(b) T_eq [K]", teq(S0, 0.30), 254.6)
check("(c) d^3", 0.5357**3, 0.1537)
check("(c) d^3 / (M/Msun)", 0.1537 / 0.7, 0.2196)
p_orb = math.sqrt(0.2196)
check("(c) orbital period [yr]", p_orb, 0.4686)
check("(c) orbital period [d]", 0.4686 * 365.25, 171.0, rtol=2e-3)

# ── Marks bookkeeping and verdict ───────────────────────────
check_points("mockexam03/mockexam03_content.tex", expected=60.0, each=10.0)
verdict()
