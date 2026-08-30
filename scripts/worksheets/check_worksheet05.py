"""Recompute every printed number in Worksheet 5 and its solutions.

Follows the printed-chain policy: each derived value is computed from the
values as PRINTED in the sheet (at their displayed precision), not from
higher-precision internal values, so a student who follows the printed
checkpoints reproduces every digit.

Every quantity in this worksheet is analytical, so this checker depends only
on the standard library; no figure script is imported.

Run: python3 scripts/worksheets/check_worksheet05.py
Exit 0 and a final ``ALL OK`` line mean every check passed.
"""

import math
import sys

FAIL = []
N_CHECKS = 0


def chk(name, got, printed, rel=5e-4):
    """Compare a recomputed value against the printed value."""
    global N_CHECKS
    N_CHECKS += 1
    ok = abs(got - printed) <= abs(printed) * rel
    print(f"{'OK  ' if ok else 'FAIL'} {name:46s} got {got:.6g}  printed {printed:.6g}")
    if not ok:
        FAIL.append(name)


G = 6.674e-11
SIGMA = 5.670e-8
KB = 1.381e-23
U = 1.661e-27
S0 = 1361.0

# ── Problem 1: equilibrium temperature and greenhouse ────────────────────
chk("P1a S(1-A) Earth (W m^-2)", S0 * 0.70, 952.70)
chk("P1a 4 sigma", 4 * SIGMA, 2.2680e-7, 1e-4)
chk("P1a S(1-A)/4sigma Earth", 952.70 / 2.2680e-7, 4.2006e9, 1e-4)
Teq_E = (4.2006e9) ** 0.25  # printed-chain
chk("P1a Teq Earth (K)", Teq_E, 254.58, 1e-4)

chk("P1b 2^(1/4)", 2 ** 0.25, 1.18921, 1e-4)
Ts_E = 1.18921 * 254.58  # printed-chain
chk("P1b one-layer surface T (K)", Ts_E, 302.75, 1e-4)
chk("P1b greenhouse excess (~15 K)", 302.75 - 288, 15, 2e-2)

chk("P1c S Venus (1.91 S0)", 1.91 * S0, 2599.5, 1e-4)
chk("P1c S(1-A)/4sigma Venus", 2599.5 * 0.23 / 2.2680e-7, 2.6362e9, 2e-4)
Teq_V = (2.6362e9) ** 0.25  # printed-chain
chk("P1c Teq Venus (K)", Teq_V, 226.59, 1e-4)
chk("P1c warming Earth (K)", 288 - 254.58, 33.42, 1e-3)
chk("P1c warming Venus (K)", 737 - 226.59, 510.41, 1e-3)
chk("P1c warming ratio (~15)", 510.41 / 33.42, 15, 3e-2)

# ── Problem 2: runaway greenhouse / Simpson-Nakajima ─────────────────────
chk("P2a F_abs Earth (W m^-2)", S0 * 0.70 / 4, 238.18, 1e-4)
chk("P2a F_abs Venus (W m^-2)", 1.91 * S0 * 0.70 / 4, 454.91, 1e-4)

chk("P2b photosphere pressure (Pa)", 10.0 / 5e-2, 200.0)
chk("P2b L/Rv (K)", 2.5e6 / 461.0, 5423.0, 1e-4)
chk("P2b 1/T_ref (K^-1)", 1 / 273.0, 3.6630e-3, 1e-4)
cc_term = -math.log(200.0 / 611.0) / 5423.0  # printed-chain
chk("P2b Clausius-Clapeyron term (K^-1)", cc_term, 2.0593e-4, 1e-3)
inv_Tphot = 3.6630e-3 + 2.0593e-4  # printed-chain
chk("P2b 1/T_phot (K^-1)", inv_Tphot, 3.8689e-3, 1e-4)
chk("P2b T_phot (K)", 1 / 3.8689e-3, 258.47, 1e-4)

chk("P2c T_phot^4 (K^4)", 258.47 ** 4, 4.4631e9, 1e-4)
chk("P2c F_OLR max (W m^-2)", 5.670e-8 * 4.4631e9, 253.06, 1e-4)
chk("P2c Earth safe (238 < 253)", float(238.18 < 253.06), 1.0, 0)
chk("P2c Venus runaway (455 > 253)", float(454.91 > 253.06), 1.0, 0)

# ── Problem 3: deuterium and Venus's lost water ──────────────────────────
chk("P3a fraction remaining f", 150.0 ** -2, 4.4444e-5, 1e-4)
chk("P3b initial water (m GEL)", 0.02 / 4.4444e-5, 450.00, 1e-4)
chk("P3b Earth-ocean fraction (~0.17)", 450.0 / 2700.0, 0.17, 3e-2)
f_071 = 150.0 ** (1 / (0.71 - 1))  # printed-chain, bare-Jeans alpha
chk("P3d f for alpha=0.71 (~3e-8)", f_071, 3e-8, 5e-2)
chk("P3d implied oceans in the hundreds (>200)", float((0.02 / f_071) / 2700.0 > 200), 1.0, 0)

# ── Problem 4: Jeans escape from Mars ────────────────────────────────────
chk("P4a 2GM (m^3 s^-2)", 2 * 6.674e-11 * 6.4e23, 8.5427e13, 1e-4)
chk("P4a 2GM/r (m^2 s^-2)", 8.5427e13 / 3.6e6, 2.3730e7, 1e-4)
chk("P4a escape speed (m s^-1)", math.sqrt(2.3730e7), 4871.3, 1e-4)
chk("P4a escape speed (~4.9 km s^-1)", 4871.3 / 1000.0, 4.9, 1e-2)

chk("P4b GM (m^3 s^-2)", 6.674e-11 * 6.4e23, 4.2714e13, 1e-4)
chk("P4b kB T r (J m)", 1.381e-23 * 270.0 * 3.6e6, 1.3423e-14, 1e-4)
chk("P4b GM/(kB T r) (kg^-1)", 4.2714e13 / 1.3423e-14, 3.1820e27, 1e-4)
chk("P4b lambda_H", 3.1820e27 * 1.661e-27, 5.2854, 1e-4)
chk("P4b lambda_H2", 2 * 5.2854, 10.571, 1e-4)
chk("P4b lambda_CO2", 44 * 5.2854, 232.56, 1e-4)

chk("P4c exp(-lambda_H)", math.exp(-5.2854), 5.0651e-3, 1e-3)
chk("P4c exp(-lambda_H2)", math.exp(-10.571), 2.5656e-5, 1e-3)
ratio = math.sqrt(2.0) * (1 + 5.2854) * 5.0651e-3 / ((1 + 10.571) * 2.5656e-5)
chk("P4c flux ratio H/H2", ratio, 151.67, 1e-3)  # printed-chain from printed exps
chk("P4c log10 exp(-lambda_CO2) (~-101)", -232.56 / math.log(10), -101, 5e-3)

# ── Problem 5: Mercury and Mars, two ways to end ─────────────────────────
chk("P5a 1/P_rot (d^-1)", 1 / 58.65, 1.70503e-2, 1e-4)
chk("P5a 1/P_orb (d^-1)", 1 / 87.97, 1.13675e-2, 1e-4)
chk("P5a solar-day rate (d^-1)", 1.70503e-2 - 1.13675e-2, 5.6828e-3, 1e-4)
chk("P5a solar day (d)", 1 / 5.6828e-3, 175.97, 1e-4)
chk("P5a two orbits (d)", 2 * 87.97, 175.94)
chk("P5a solar day ~ two Mercury years", float(abs(175.97 - 175.94) < 0.05), 1.0, 0)

chk("P5b delta A / A", 2 * 7.0 / 2440.0, 5.7377e-3, 1e-4)
chk("P5b area change (~0.57%)", 2 * 7.0 / 2440.0 * 100, 0.57, 1e-2)

chk("P5c a^3 (m^3)", (9.376e6) ** 3, 8.2424e20, 1e-4)
chk("P5c GM Mars (m^3 s^-2)", 6.674e-11 * 6.4e23, 4.2714e13, 1e-4)
chk("P5c a^3/GM (s^2)", 8.2424e20 / 4.2714e13, 1.9297e7, 1e-4)
T_ph = 2 * math.pi * math.sqrt(1.9297e7)  # printed-chain
chk("P5c Phobos period (s)", T_ph, 2.7601e4, 1e-4)
chk("P5c Phobos period (h)", 2.7601e4 / 3600, 7.667, 1e-3)
chk("P5c Phobos below synchronous", float(7.667 < 24.62), 1.0, 0)

print()
print(f"{N_CHECKS} checks, {len(FAIL)} failures")
if FAIL:
    for name in FAIL:
        print(f"  FAIL: {name}")
    sys.exit(1)
print("ALL OK")
