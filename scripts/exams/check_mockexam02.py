"""Recompute every numerical value printed in Mock exam 2.

Each value is recomputed from the constants printed in the exam's data box,
following the same intermediate rounding the worked solutions hand forward,
and compared against the digits printed on the sheet. The script fails loudly
on any mismatch and prints ``ALL OK (N checks)`` when every printed number
reproduces.

Run
---
python scripts/exams/check_mockexam02.py
"""

from __future__ import annotations

import math

from _checker_common import SIGMA, check, check_points, teq, verdict

# ── Constants and data printed on the exam ──────────────────
# SIGMA (Stefan-Boltzmann) is imported above with the shared helpers.
G = 6.674e-11  # m^3 kg^-1 s^-2
AU = 1.496e11  # m
YR_D = 365.25  # d
MSUN = 1.989e30  # kg
KB = 1.381e-23  # J K^-1
MU_ATOMIC = 1.661e-27  # kg
S0 = 1361.0  # W m^-2 at 1 AU

R_EARTH = 6.371e6  # m
RHO_EARTH = 5514.0  # kg m^-3
A_VENUS = 0.723  # AU
A_MARS = 1.524  # AU
M_MARS, R_MARS = 6.417e23, 3.390e6
A_SAT, ALB_SAT = 9.58, 0.34
M_SAT, R_SAT = 5.683e26, 5.8232e7
TEFF_SAT = 95.0  # K
M_TITAN, R_TITAN, T_TITAN = 1.345e23, 2.575e6, 160.0
M_MOON, R_MOON, T_MOON = 7.342e22, 1.737e6, 390.0
Q_PERI, Q_APH = 0.59, 35.1

# Values printed in the problem statements
CP_ROCK = 1000.0  # J kg^-1 K^-1
RHO_CORE, RHO_MANTLE = 11000.0, 4500.0  # kg m^-3, two-layer Earth model
RHO_ICE = 900.0  # kg m^-3, ring material
MU_N2, MU_H2 = 28.0, 2.0
HZ_SIN, HZ_SOUT = 1.05, 0.35  # inner/outer edge flux in units of S0
L_DWARF, M_DWARF = 0.02, 0.30  # red dwarf, solar units

gm_sun = G * MSUN

# ── Problem 1: The orbit of a comet ─────────────────────────
print("Problem 1  The orbit of a comet")
a_comet = 0.5 * (Q_PERI + Q_APH)
check("(a) a [AU]", a_comet, 17.845)
check("(a) e numerator", Q_APH - Q_PERI, 34.51)
check("(a) e denominator", Q_APH + Q_PERI, 35.69)
check("(a) e", (Q_APH - Q_PERI) / (Q_APH + Q_PERI), 0.9669)
check("(a) P [yr]", a_comet**1.5, 75.38)
check("(a) P answer [yr]", a_comet**1.5, 75.4, rtol=5e-3)

check("(b) GM_sun", gm_sun, 1.3275e20)
q_m = Q_PERI * AU
a_m = a_comet * AU
check("(b) q [m]", q_m, 8.8264e10)
check("(b) a [m]", a_m, 2.6696e12)
bracket = 2.0 / q_m - 1.0 / a_m
check("(b) 2/q - 1/a", bracket, 2.2285e-11)
v_peri_sq = gm_sun * bracket
check("(b) v_p^2", v_peri_sq, 2.9583e9)
v_peri = math.sqrt(v_peri_sq)
check("(b) v_p checkpoint [km/s]", v_peri / 1e3, 54.39)
v_aph = 54.39 * Q_PERI / Q_APH  # hands forward the printed 54.39
check("(b) v_a [km/s]", v_aph, 0.914)
check("(b) speed ratio ~60", v_peri / 1e3 / v_aph, 60.0, rtol=1e-2)

# ── Problem 2: The energy of building Mars ──────────────────
print("Problem 2  The energy of building Mars")
e_num = 3.0 * G * M_MARS**2
check("(a) 3 G M^2", e_num, 8.2446e37)
check("(a) 5 R", 5.0 * R_MARS, 1.695e7)
e_bind = e_num / (5.0 * R_MARS)
check("(a) E checkpoint [J]", e_bind, 4.864e30)

dt_mars = 4.864e30 / (M_MARS * CP_ROCK)  # hands forward 4.864e30
check("(b) Delta T [K]", dt_mars, 7580.0)
check("(b) Delta T answer [K]", dt_mars, 7600.0, rtol=5e-3)

# ── Problem 3: Inside the Earth ─────────────────────────────
print("Problem 3  Inside the Earth")
x3 = (RHO_EARTH - RHO_MANTLE) / (RHO_CORE - RHO_MANTLE)
check("(a) x^3 numerator", RHO_EARTH - RHO_MANTLE, 1014.0)
check("(a) x^3 denominator", RHO_CORE - RHO_MANTLE, 6500.0)
check("(a) x^3", x3, 0.1560)
x = x3 ** (1.0 / 3.0)
check("(a) x", x, 0.5383)
check("(a) R_core checkpoint [km]", 0.5383 * 6371.0, 3430.0)
check("(a) core mass fraction", RHO_CORE * 0.1560 / RHO_EARTH, 0.311, rtol=1e-3)

p_c = (2.0 / 3.0) * math.pi * G * RHO_EARTH**2 * R_EARTH**2
check("(b) P_c [Pa]", p_c, 1.725e11)
check("(b) P_c [GPa]", p_c / 1e9, 172.5)

# ── Problem 4: The rings and glow of Saturn ─────────────────
print("Problem 4  The rings and glow of Saturn")
v_sat = (4.0 / 3.0) * math.pi * R_SAT**3
check("(a) volume [m^3]", v_sat, 8.2712e23)
rho_sat = M_SAT / v_sat
check("(a) mean density", rho_sat, 687.1)

cube = (687.1 / RHO_ICE) ** (1.0 / 3.0)  # hands forward 687.1
check("(b) (rho_p/rho_m)^(1/3)", cube, 0.9140)
d_roche = 2.44 * R_SAT * 0.9140
check("(b) Roche limit [m]", d_roche, 1.299e8, rtol=1e-3)
check("(b) Roche limit checkpoint [km]", d_roche / 1e3, 129900.0, rtol=1e-3)
check("(b) d in Saturn radii", d_roche / R_SAT, 2.2, rtol=2e-2)
# Full-precision cross-check: the limit depends on the planet only through
# its mass, d = 2.44 (M / (4/3 pi rho_m))^(1/3), so radius rounding cancels.
d_mass_form = 2.44 * (M_SAT / ((4.0 / 3.0) * math.pi * RHO_ICE)) ** (1.0 / 3.0)
check("(b) Roche limit, mass form [m]", d_mass_form, 1.299e8, rtol=1e-3)

s_sat = S0 / A_SAT**2
check("(c) S at Saturn", s_sat, 14.83)
absorbed = (14.83 / 4.0) * (1.0 - ALB_SAT)  # hands forward 14.83
check("(c) absorbed flux", absorbed, 2.447)
emitted = SIGMA * TEFF_SAT**4
check("(c) emitted flux", emitted, 4.618)
check("(c) emitted/absorbed", 4.618 / 2.447, 1.89, rtol=2e-3)
check("(c) internal excess", 4.618 - 2.447, 2.2, rtol=2e-2)

# ── Problem 5: Keeping an atmosphere ────────────────────────
print("Problem 5  Keeping an atmosphere")
vesc_titan_sq = 2.0 * G * M_TITAN / R_TITAN
check("(a) v_esc^2 Titan", vesc_titan_sq, 6.9721e6)
vesc_titan = math.sqrt(vesc_titan_sq)
check("(a) v_esc Titan [m/s]", vesc_titan, 2640.0)

m_n2 = MU_N2 * MU_ATOMIC
check("(b) m_N2 [kg]", m_n2, 4.6508e-26)
two_kt_160 = 2.0 * KB * T_TITAN
check("(b) 2 kB T at 160 K", two_kt_160, 4.4192e-21)
vth_n2_sq = two_kt_160 / m_n2
check("(b) v_th^2 N2", vth_n2_sq, 9.5020e4)
vth_n2 = math.sqrt(vth_n2_sq)
check("(b) v_th N2 [m/s]", vth_n2, 308.0, rtol=1e-3)
check("(b) ratio N2", 2640.0 / 308.3, 8.6, rtol=5e-3)
m_h2 = MU_H2 * MU_ATOMIC
check("(b) m_H2 [kg]", m_h2, 3.322e-27)
vth_h2_sq = two_kt_160 / m_h2
check("(b) v_th^2 H2", vth_h2_sq, 1.3303e6)
vth_h2 = math.sqrt(vth_h2_sq)
check("(b) v_th H2 [m/s]", vth_h2, 1153.0)
check("(b) ratio H2", 2640.0 / 1153.0, 2.3, rtol=5e-3)

vesc_moon_sq = 2.0 * G * M_MOON / R_MOON
check("(c) v_esc^2 Moon", vesc_moon_sq, 5.6420e6)
vesc_moon = math.sqrt(vesc_moon_sq)
check("(c) v_esc Moon [m/s]", vesc_moon, 2375.0)
vth_moon_sq = 2.0 * KB * T_MOON / m_n2
check("(c) v_th^2 N2 at 390 K", vth_moon_sq, 2.3161e5)
vth_moon = math.sqrt(vth_moon_sq)
check("(c) v_th N2 at 390 K [m/s]", vth_moon, 481.0, rtol=1e-3)
check("(c) ratio Moon", 2375.0 / 481.3, 4.9, rtol=1e-2)

# ── Problem 6: The habitable zone ───────────────────────────
print("Problem 6  The habitable zone")
check("(a) inner edge [AU]", math.sqrt(1.0 / HZ_SIN), 0.976)
check("(a) outer edge [AU]", math.sqrt(1.0 / HZ_SOUT), 1.690)
check("(a) Mars inside zone", float(A_MARS < math.sqrt(1.0 / HZ_SOUT)), 1.0)
check("(a) Earth inside zone", float(math.sqrt(1.0 / HZ_SIN) < 1.000 < math.sqrt(1.0 / HZ_SOUT)), 1.0)
check("(a) Venus inside inner edge", float(A_VENUS < math.sqrt(1.0 / HZ_SIN)), 1.0)
check("(c) Mars flux [S0] > outer limit", float(1.0 / A_MARS**2 > HZ_SOUT), 1.0)

check("(b) dwarf inner edge [AU]", math.sqrt(L_DWARF / HZ_SIN), 0.138)
check("(b) dwarf outer edge [AU]", math.sqrt(L_DWARF / HZ_SOUT), 0.239)
p_sq = 0.138**3 / M_DWARF  # hands forward 0.138
check("(b) P^2 [yr^2]", p_sq, 8.7602e-3)
p_yr = math.sqrt(p_sq)
check("(b) P [yr]", p_yr, 0.09360)
check("(b) P [d]", p_yr * YR_D, 34.2, rtol=1e-3)
# Full-precision cross-check in SI units.
a_in_m = math.sqrt(L_DWARF / HZ_SIN) * AU
p_si = 2.0 * math.pi * math.sqrt(a_in_m**3 / (gm_sun * M_DWARF))
check("(b) P [d], SI cross-check", p_si / 86400.0, 34.2, rtol=2e-3)

# ── Marks bookkeeping and verdict ───────────────────────────
print("Marks")
check_points("mockexam02/mockexam02_content.tex", expected=60.0, each=10.0)

verdict()
