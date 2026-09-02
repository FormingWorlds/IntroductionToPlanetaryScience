"""Recompute every printed number in Worksheet 6 and its solutions.

Follows the printed-chain policy: each derived value is computed from the
values as PRINTED in the sheet (at their displayed precision), not from
higher-precision internal values, so a student who follows the printed
checkpoints reproduces every digit.

Every quantity in this worksheet is analytical, so this checker depends only
on the standard library; no figure script is imported.

Run: python3 scripts/worksheets/check_worksheet06.py
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
U = 1.661e-27
S0 = 1361.0
LN2 = 0.6931

# ── Problem 1: giant-planet interiors, metallic hydrogen ─────────────────
# (a) Jupiter bulk density
chk("P1a R_J^3 (m^3)", (6.991e7) ** 3, 3.4168e23, 1e-4)
chk("P1a (4/3)pi R^3 (m^3)", 4 / 3 * math.pi * 3.4168e23, 1.4312e24, 1e-4)
chk("P1a rho Jupiter (kg m^-3)", 1.898e27 / 1.4312e24, 1326.0, 1e-3)

# (b) Jupiter central pressure P_c = 3 G M^2 / (8 pi R^4)
chk("P1b M_J^2 (kg^2)", (1.898e27) ** 2, 3.6024e54, 1e-4)
chk("P1b 3 G M^2 (numerator)", 3 * G * 3.6024e54, 7.2121e44, 1e-4)
chk("P1b R_J^4 (m^4)", (6.991e7) ** 4, 2.3887e31, 1e-4)
chk("P1b 8 pi R^4 (denominator)", 8 * math.pi * 2.3887e31, 6.0034e32, 1e-4)
chk("P1b P_c Jupiter (Pa)", 7.2121e44 / 6.0034e32, 1.201e12, 1e-3)
chk("P1b P_c / 100 GPa (~12)", 1201.0 / 100.0, 12.0, 1e-2)

# (c) Saturn central pressure (R_p = 5.8232e7 m volumetric mean)
chk("P1c M_Sat^2 (kg^2)", (5.683e26) ** 2, 3.2296e53, 1e-4)
chk("P1c 3 G M^2 (numerator)", 3 * G * 3.2296e53, 6.4669e43, 1e-4)
chk("P1c R_Sat^4 (m^4)", (5.8232e7) ** 4, 1.1499e31, 1e-4)
chk("P1c 8 pi R^4 (denominator)", 8 * math.pi * 1.1499e31, 2.8900e32, 1e-4)
chk("P1c P_c Saturn (Pa)", 6.4669e43 / 2.8900e32, 2.238e11, 1e-3)
chk("P1c P_c Saturn (GPa) ~224", 2.238e11 / 1e9, 224.0, 5e-3)
chk("P1c P_c / 100 GPa (~2.24)", 223.8 / 100.0, 2.24, 1e-2)

# ── Problem 2: Roche limit and Saturn's rings ────────────────────────────
# Saturn volumetric mean radius in km; densities from the given block
RP = 58232.0
chk("P2a (rho_p/rho_s)^(1/3) ice", (687.0 / 1000.0) ** (1 / 3), 0.882, 5e-4)
chk("P2a rigid Roche (km)", 1.26 * RP * 0.882, 64710.0, 1e-3)
chk("P2a rigid Roche (R_p)", 64710.0 / RP, 1.111, 1e-3)

chk("P2b fluid Roche (km)", 2.46 * RP * 0.882, 126350.0, 1e-3)
chk("P2b fluid Roche (R_p)", 126350.0 / RP, 2.170, 1e-3)
chk("P2b A-ring mismatch (frac)", (137000.0 - 126350.0) / 137000.0, 0.078, 5e-3)

chk("P2c (rho_p/rho_s)^(1/3) rock", (687.0 / 3000.0) ** (1 / 3), 0.612, 1e-3)
chk("P2c rocky fluid Roche (km)", 2.46 * RP * 0.612, 87670.0, 1e-3)

# ── Problem 3: radioactive dating ────────────────────────────────────────
# (a) Al-26 decay constant and survival after 2 Myr
chk("P3a lambda_Al26 (Myr^-1)", LN2 / 0.717, 0.9667, 1e-3)
chk("P3a N/N0 at 2 Myr", math.exp(-0.9667 * 2), 0.1447, 1e-3)

# (b) live Al-26/Al-27 at 2 Myr, heating factor
chk("P3b (Al26/Al27) at 2 Myr", 5.2e-5 * 0.1447, 7.52e-6, 1e-3)
chk("P3b heating factor (~6.9)", 1 / 0.1447, 6.9, 1e-2)

# (c) Pb-Pb isochron slope at CAI age
chk("P3c lambda_235 (Gyr^-1)", LN2 / 0.7038, 0.9848, 1e-3)
chk("P3c lambda_238 (Gyr^-1)", LN2 / 4.4683, 0.1551, 1e-3)
chk("P3c lambda_235 t", 0.9848 * 4.5673, 4.498, 1e-3)
chk("P3c lambda_238 t", 0.1551 * 4.5673, 0.7084, 1e-3)
chk("P3c exp(l235 t) - 1", math.exp(4.498) - 1, 88.84, 1e-3)
chk("P3c exp(l238 t) - 1", math.exp(0.7084) - 1, 1.031, 1e-3)
chk("P3c 235U/238U", 1 / 137.82, 7.256e-3, 1e-3)
chk("P3c ratio (e235-1)/(e238-1)", 88.84 / 1.031, 86.17, 1e-3)
chk("P3c Pb-Pb slope", 7.256e-3 * 86.17, 0.6252, 1e-3)

# ── Problem 4: Kirkwood gaps ─────────────────────────────────────────────
AJ = 5.203
chk("P4a (1/3)^(2/3)", (1 / 3) ** (2 / 3), 0.4807, 1e-3)
chk("P4a a_3:1 (AU)", AJ * 0.4807, 2.501, 1e-3)

chk("P4b (2/5)^(2/3)", (2 / 5) ** (2 / 3), 0.5429, 1e-3)
chk("P4b a_5:2 (AU)", AJ * 0.5429, 2.825, 1e-3)
chk("P4b (1/2)^(2/3)", (1 / 2) ** (2 / 3), 0.6300, 1e-3)
chk("P4b a_2:1 (AU)", AJ * 0.6300, 3.278, 1e-3)

chk("P4c sqrt(2.501)", math.sqrt(2.501), 1.5814, 1e-3)
chk("P4c T at 3:1 (yr)", 2.501 * 1.5814, 3.955, 1e-3)
chk("P4c T_J / 3 (yr)", 11.86 / 3, 3.953, 1e-3)

# ── Problem 5: cometary activity ─────────────────────────────────────────
# (a) grey nucleus temperature, fast rotator
chk("P5a S0/(4 sigma) (K^4)", S0 / (4 * SIGMA), 6.0009e9, 1e-4)
chk("P5a T at 1 AU (K)", (6.0009e9) ** 0.25, 278.3, 1e-3)
chk("P5a T at 3 AU (K)", 278.3 / math.sqrt(3), 160.7, 1e-3)

# (b) onset distance for T = 150 K
chk("P5b onset distance (AU)", (278.3 / 150.0) ** 2, 3.442, 1e-3)

# (c) sublimation rate at 1 AU
chk("P5c water molecular mass (kg)", 18 * U, 2.990e-26, 1e-3)
chk("P5c 4 L m (denominator)", 4 * 2.83e6 * 2.990e-26, 3.385e-19, 1e-3)
chk("P5c Z at 1 AU (m^-2 s^-1)", 1361.0 / 3.385e-19, 4.021e21, 1e-3)

print()
print(f"{N_CHECKS} checks, {len(FAIL)} failures")
if FAIL:
    for name in FAIL:
        print(f"  FAIL: {name}")
    sys.exit(1)
print("ALL OK")
