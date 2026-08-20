"""Recompute every printed number in Worksheet 4 and its solutions.

Follows the printed-chain policy: each derived value is computed from the
values as PRINTED in the sheet (at their displayed precision), not from
higher-precision internal values, so a student who follows the printed
checkpoints reproduces every digit.

The chronology checks import the Lecture 7 figure script, so the sheet is
compared against the exact coefficients the figure is drawn from.

Run: python3 scripts/worksheets/check_worksheet04.py
Exit 0 and a final ``ALL OK`` line mean every check passed.
"""

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.figures.L07_surfaces.fig_neukum_chronology import (  # noqa: E402
    A_EXP,
    B_LIN,
    LAMBDA,
    age_from_density,
)

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

# ── Given block: coefficients on the figure match the sheet's usage ──────
chk("given a (km^-2)", A_EXP, 5.44e-14, 1e-9)
chk("given lambda (Gyr^-1)", LAMBDA, 6.93, 1e-9)
chk("given b (km^-2 Gyr^-1)", B_LIN, 8.38e-4, 1e-9)

# ── Problem 1: impact energetics on Mars ─────────────────────────────────
m = 4 / 3 * math.pi * 200**3 * 3000
chk("P1a impactor mass (kg)", m, 1.0053e11, 1e-4)
E = 0.5 * 1.0053e11 * (1.2e4) ** 2  # printed-chain from m
chk("P1a kinetic energy (J)", E, 7.2382e18, 1e-4)
scale = 7.2382e18 / (3000 * 3.71)  # printed-chain from E
chk("P1a E/(rho g) (m^4)", scale, 6.5033e14, 1e-4)
D = 6.5033e14**0.25  # printed-chain
chk("P1a crater diameter (m)", D, 5049.9, 1e-4)
chk("P1a crater/impactor ratio > 12", 5049.9 / 400, 12.6, 5e-3)

L2 = 400 * (50 / 5.05) ** (4 / 3)  # printed-chain from D = 5.05 km
chk("P1b impactor for 50 km crater (m)", L2, 8504, 2e-4)
chk("P1b size ratio", (50 / 5.05) ** (4 / 3), 21.260, 1e-4)

Dt = 15 * 1.62 / 3.71
chk("P1c transition diameter Mars (km)", Dt, 6.5499, 1e-4)

# ── Problem 2: reading ages from craters ─────────────────────────────────
T_lin = 2.5e-3 / B_LIN
chk("P2a linear age (Gyr)", T_lin, 2.9833, 1e-4)
exp_term = A_EXP * (math.exp(LAMBDA * 2.9833) - 1)  # printed-chain from T
chk("P2a exponential factor", math.exp(LAMBDA * 2.9833) - 1, 9.5218e8, 1e-4)
chk("P2a exponential term (km^-2)", exp_term, 5.1799e-5, 1e-4)
chk("P2a term fraction (~2.1%)", 5.1799e-5 / 2.5e-3, 0.021, 2e-2)

N_b = 3e-2
T0 = math.log(1 + N_b / A_EXP) / LAMBDA
chk("P2b N/a", N_b / A_EXP, 5.5147e11, 1e-4)
chk("P2b log argument", math.log(5.5147e11), 27.036, 1e-4)
chk("P2b first estimate T0 (Gyr)", T0, 3.9013, 1e-4)
bT0 = B_LIN * 3.9013  # printed-chain from T0
chk("P2b linear contribution (km^-2)", bT0, 3.2693e-3, 1e-4)
chk("P2b linear fraction (~11%)", 3.2693e-3 / N_b, 0.109, 2e-2)
T1 = math.log(1 + 2.6731e-2 / A_EXP) / LAMBDA  # printed-chain from N - bT0
chk("P2b corrected N (km^-2)", N_b - 3.2693e-3, 2.6731e-2, 1e-4)
chk("P2b corrected age T1 (Gyr)", T1, 3.8846, 1e-4)
chk("P2b exact inversion agrees", age_from_density(N_b), 3.885, 2e-4)
next_move = abs(math.log(1 + (N_b - B_LIN * 3.8846) / A_EXP) / LAMBDA - 3.8846)
chk("P2b next iterate moves < 0.001 Gyr", float(next_move < 1e-3), 1.0, 0)
chk("P2b figure read-off (~3.9 Gyr)", age_from_density(N_b), 3.9, 5e-3)
chk("P2b age for N/2 (Gyr)", age_from_density(N_b / 2), 3.77, 2e-3)
chk("P2b age for 2N (Gyr)", age_from_density(N_b * 2), 3.99, 2e-3)
chk("P2b ln2/lambda shift (Gyr)", math.log(2) / LAMBDA, 0.1, 2e-3)

# ── Problem 3: moment of inertia and the inside of Mercury ───────────────
x = 0.83
chk("P3a x^3", x**3, 0.57179, 1e-4)
rho_c = 0.74 * 5427 / 0.57179  # printed-chain from x^3
chk("P3a core mass x mean density", 0.74 * 5427, 4016.0, 1e-4)
chk("P3a core density (kg m^-3)", rho_c, 7023.6, 1e-4)
chk("P3a mantle volume fraction", 1 - 0.57179, 0.42821, 1e-4)
rho_m = 0.26 * 5427 / 0.42821  # printed-chain
chk("P3a mantle mass x mean density", 0.26 * 5427, 1411.0, 1e-4)
chk("P3a mantle density (kg m^-3)", rho_m, 3295.1, 1e-4)

f = 7023.6 / 3295.1  # printed-chain
chk("P3b density contrast f", f, 2.1315, 1e-4)
chk("P3b x^5", x**5, 0.39390, 1e-4)
num = 1.1315 * 0.39390 + 1  # printed-chain
den = 1.1315 * 0.57179 + 1
chk("P3b numerator", num, 1.4457, 1e-4)
chk("P3b denominator", den, 1.6470, 1e-4)
chk("P3b MoI factor", 0.4 * 1.4457 / 1.6470, 0.35111, 1e-4)
chk("P3b deviation from measured (~1.5%)", 0.3511 / 0.346 - 1, 0.015, 5e-2)

xm = 380 / 1737
chk("P3c lunar x", xm, 0.219, 2e-3)
chk("P3c lunar x^3 (~1% volume)", 0.219**3, 0.0105, 2e-2)
moi_moon = 0.4 * (1 + 0.219**5) / (1 + 0.219**3)  # printed-chain, f = 2
chk("P3c lunar two-layer MoI", moi_moon, 0.396, 1e-3)

# ── Problem 4: central pressure ──────────────────────────────────────────
M_mars = 6.417e23
R_mars = 3.3895e6
V = 4 / 3 * math.pi * R_mars**3
chk("P4b volume denominator (m^3)", V, 1.63116e20, 1e-4)
rho_bar = M_mars / 1.63116e20  # printed-chain
chk("P4b mean density (kg m^-3)", rho_bar, 3934.0, 1e-4)
chk("P4b M^2 (kg^2)", M_mars**2, 4.1178e47, 1e-4)
chk("P4b R^4 (m^4)", R_mars**4, 1.3199e26, 1e-4)
chk("P4b 3G", 3 * G, 2.0022e-10, 1e-4)
chk("P4b 8 pi", 8 * math.pi, 25.133, 1e-4)
Pc = 2.0022e-10 * 4.1178e47 / (25.133 * 1.3199e26)  # printed-chain
chk("P4b central pressure (Pa)", Pc, 2.4853e10, 1e-4)
Pc_alt = 2 * math.pi / 3 * G * 3934.0**2 * R_mars**2
chk("P4b cross-check via density form (Pa)", Pc_alt, 2.4853e10, 2e-4)
chk("P4c Earth ratio (~7x Mars)", 170 / 24.9, 6.8, 5e-2)
chk("P4c Earth actual/uniform (~2x)", 360 / 170, 2.1, 3e-2)

print()
print(f"{N_CHECKS} checks, {len(FAIL)} failures")
if FAIL:
    for name in FAIL:
        print(f"  FAIL: {name}")
    sys.exit(1)
print("ALL OK")
