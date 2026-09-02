"""Recompute every printed number in Worksheet 3 and its solutions.

Follows the printed-chain policy: each derived value is computed from the
values as PRINTED in the sheet (at their displayed precision), not from
higher-precision internal values, so a student who follows the printed
checkpoints reproduces every digit.

Run: python3 scripts/worksheets/check_worksheet03.py
Exit 0 and a final ``ALL OK`` line mean every check passed.
"""

import math

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


kB = 1.381e-23
m_u = 1.661e-27
sigma = 5.670e-8
S0 = 1361.0

# ── Problem 1: how thick is an atmosphere? ──────────────────────────────
H_E = kB * 288 / (28.97 * m_u * 9.81)
chk("P1a H_Earth (km)", H_E / 1e3, 8.426, 1e-3)
chk("P1a H_Earth numerator", kB * 288, 3.9773e-21)
chk("P1a H_Earth denominator", 28.97 * m_u * 9.81, 4.7205e-25)
H_T = kB * 94 / (28.6 * m_u * 1.35)
chk("P1a H_Titan (km)", H_T / 1e3, 20.24, 1e-3)
chk("P1a H_Titan numerator", kB * 94, 1.2981e-21)
chk("P1a H_Titan denominator", 28.6 * m_u * 1.35, 6.4131e-26)
# printed-chain: the division of the two PRINTED 5-sf values
chk("P1a H_Titan printed-chain (m)", 1.2981e-21 / 6.4131e-26, 20241, 5e-5)
chk("P1a H_Earth printed-chain (m)", 3.9773e-21 / 4.7205e-25, 8425.6, 5e-5)
# P1b ratio quoted qualitatively: (288/94) ~ 3.1 vs (9.81/1.35) ~ 7.3 -> ~2.4
chk("P1b T ratio", 288 / 94, 3.1, 2e-2)
chk("P1b g ratio", 9.81 / 1.35, 7.3, 1e-2)
chk("P1b H ratio", 7.3 / 3.1, 2.4, 2e-2)
# P1c column mass and atmosphere mass (chain: printed 1.0326e4)
m_col = 1.013e5 / 9.81
chk("P1c column mass (kg m^-2)", m_col, 1.0326e4, 1e-3)
M_atm = 4 * math.pi * (6.371e6) ** 2 * 1.0326e4
chk("P1c atmosphere mass (kg)", M_atm, 5.267e18, 1e-3)

# ── Problem 2: sunlight in, infrared out ────────────────────────────────
S_V = S0 / 0.72 ** 2
chk("P2a S_Venus (checkpoint)", S_V, 2625.4, 2e-4)
T_eq = ((1 - 0.77) * 2625.4 / (4 * sigma)) ** 0.25
# printed-chain: the bracket from the PRINTED S_Venus checkpoint
chk("P2a inner bracket (K^4)", (1 - 0.77) * 2625.4 / (4 * sigma), 2.6624e9, 5e-5)
chk("P2a T_eq Venus (K)", T_eq, 227.2, 5e-4)

# ── Problem 3: from vapour to cloud base ────────────────────────────────
P293 = 611 * math.exp(-5400 * (1 / 293 - 1 / 273))
chk("P3a exponent", -5400 * (1 / 293 - 1 / 273), 1.3502, 2e-4)
chk("P3a P_sat(293) (Pa)", P293, 2357, 1e-3)
chk("P3a P_vap (Pa)", 0.5 * 2357, 1179, 1e-3)
inv_Td = 1 / 273 - math.log(1179 / 611) / 5400
chk("P3a ln ratio", math.log(1179 / 611), math.log(1.9296), 2e-4)
chk("P3a 1/T_d (K^-1)", inv_Td, 3.5413e-3, 2e-4)
chk("P3a T_d (K)", 1 / inv_Td, 282.4, 5e-4)
chk("P3a z_LCL (km)", (293 - 282.4) / 9.8, 1.082, 1e-3)
# P3b figure read: CH4 at 90 K vs 1e4 Pa, from the psat script constants
R_UNIV = 8.314
L_ch4, M_ch4, Tref_ch4 = 5.10e5, 16.043e-3, 111.7
psat_ch4_90 = 101325 * math.exp(-(L_ch4 / (R_UNIV / M_ch4)) * (1 / 90 - 1 / Tref_ch4))
chk("P3b CH4 psat at 90 K (Pa, order 1e4)", psat_ch4_90, 1.2e4, 0.05)

# ── Problem 4: winds on a rotating planet ───────────────────────────────
f = 2 * 7.29e-5 * math.sin(math.radians(53))
chk("P4a sin 53 deg", math.sin(math.radians(53)), 0.79864, 1e-4)
chk("P4a f (s^-1)", f, 1.164e-4, 5e-4)
chk("P4a 1/f (hours)", 1 / 1.164e-4 / 3600, 2.4, 1e-2)
chk("P4b Rossby number", 15 / (1.164e-4 * 2.0e6), 0.064, 1e-2)

# ── Problem 5: climate on the edge ──────────────────────────────────────
chk("P5a 0.71^(1/4)", 0.71 ** 0.25, 0.91794, 1e-4)
chk("P5a T_eq young Sun (K)", 255 * 0.91794, 234.1, 5e-4)
chk("P5a implied surface (K)", 234.1 + 33, 267.1, 1e-3)
# P5b figure read: the three equilibria as asserted by the figure checker
import importlib.util as _ilu
import pathlib as _pl
import sys as _sys

_root = _pl.Path(__file__).resolve().parents[2]
_sys.path.insert(0, str(_root))
_spec = _ilu.spec_from_file_location(
    "fig_snowball", _root / "scripts/figures/L06_atmospheres_2/fig_snowball_bistability.py")
_m = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_m)
import numpy as _np

_T = _np.linspace(220, 320, 200000)
_roots = _T[_np.where(_np.diff(_np.sign(_m.absorbed(_T) - _m.OLR(_T))))[0]]
chk("P5b cold equilibrium (K)", float(_roots[0]), 250, 1.5e-2)
chk("P5b unstable threshold (K)", float(_roots[1]), 267, 1e-2)
chk("P5b warm equilibrium (K)", float(_roots[2]), 287, 1e-2)

print()
if FAIL:
    print(f"{len(FAIL)} FAILURES: {FAIL}")
    raise SystemExit(1)
print(f"ALL OK ({N_CHECKS} checks)")
