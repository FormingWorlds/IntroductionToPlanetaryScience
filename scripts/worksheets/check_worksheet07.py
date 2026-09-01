"""Recompute every printed number in Worksheet 7 and its solutions.

Follows the printed-chain policy: each derived value is computed from the
values as PRINTED in the sheet (at their displayed precision), not from
higher-precision internal values, so a student who follows the printed
checkpoints reproduces every digit.

Every quantity in this worksheet is analytical, so this checker depends only
on the standard library; no figure script is imported.

Run: python3 scripts/worksheets/check_worksheet07.py
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
MSUN = 1.989e30
LSUN = 3.828e26
RSUN = 6.957e8
MJ = 1.898e27
ME = 5.972e24
RE = 6.371e6
AU = 1.496e11
PC = 3.086e16
YR = 3.156e7
DAY = 86400.0
RAD_ARCSEC = 206265.0

# ── Problem 1: transit depths and geometric probability ──────────────────
# (a) hot-Jupiter transit depth
chk("P1a R_p/R_star", 8.6e7 / RSUN, 0.12362, 1e-4)
chk("P1a delta hot Jupiter", 0.12362**2, 1.5281e-2, 1e-4)

# (b) Earth-analogue transit depth
chk("P1b R_E/R_sun", RE / RSUN, 9.1577e-3, 1e-4)
chk("P1b delta Earth", (9.1577e-3) ** 2, 8.3863e-5, 1e-4)
chk("P1b delta Earth (ppm ~84)", 8.3863e-5 * 1e6, 84.0, 5e-3)

# (c) geometric transit probabilities
chk("P1c p_Earth", RSUN / AU, 4.6504e-3, 1e-4)
chk("P1c 1/p_Earth (~215)", 1 / 4.6504e-3, 215.0, 5e-3)
chk("P1c p_HJ", RSUN / (0.05 * AU), 9.3008e-2, 1e-4)
chk("P1c ratio p_HJ/p_Earth", 9.3008e-2 / 4.6504e-3, 20.0, 1e-4)

# ── Problem 2: radial-velocity masses and K2-18 b density ────────────────
# (a) 51 Peg b analogue semi-amplitude
chk("P2a 2 pi G", 2 * math.pi * G, 4.1934e-10, 1e-4)
chk("P2a P (s)", 4.23 * DAY, 3.6547e5, 1e-4)
chk("P2a 2piG/P", 4.1934e-10 / 3.6547e5, 1.1474e-15, 1e-4)
chk("P2a (2piG/P)^(1/3)", (1.1474e-15) ** (1 / 3), 1.0469e-5, 1e-4)
chk("P2a M_sun^(2/3)", MSUN ** (2 / 3), 1.5816e20, 1e-4)
chk("P2a m_p sin i (kg)", 0.5 * MJ, 9.490e26, 1e-4)
chk("P2a K 51 Peg b (m/s)", 1.0469e-5 * 9.490e26 / 1.5816e20, 62.82, 5e-4)

# (b) Earth-analogue semi-amplitude
chk("P2b 2piG/P (1 yr)", 4.1934e-10 / YR, 1.3287e-17, 1e-4)
chk("P2b (2piG/P)^(1/3)", (1.3287e-17) ** (1 / 3), 2.3685e-6, 1e-4)
chk("P2b K Earth (m/s)", 2.3685e-6 * ME / 1.5816e20, 8.943e-2, 5e-4)

# (c) K2-18 b bulk density
chk("P2c m_p (kg)", 8.6 * ME, 5.1359e25, 1e-4)
chk("P2c R_p (m)", 2.6 * RE, 1.6565e7, 1e-4)
chk("P2c (4/3)pi R^3 (m^3)", 4 / 3 * math.pi * (1.6565e7) ** 3, 1.9038e22, 1e-4)
chk("P2c rho K2-18 b (kg m^-3)", 5.1359e25 / 1.9038e22, 2697.7, 5e-4)

# ── Problem 3: scale heights and transmission spectroscopy ───────────────
# (a) hot-Jupiter terminator scale height
chk("given g vs GM/R^2", G * 0.5 * MJ / (8.6e7) ** 2, 8.6, 5e-3)
chk("P3a k_B T (J)", KB * 1500.0, 2.0715e-20, 1e-4)
chk("P3a mu u g (kg m s^-2)", 2.3 * U * 8.6, 3.2855e-26, 1e-4)
chk("P3a H hot Jupiter (m)", 2.0715e-20 / 3.2855e-26, 6.3050e5, 1e-4)

# (b) rocky CO2 scale height and ratio
chk("P3b k_B T (J)", KB * 300.0, 4.1430e-21, 1e-4)
chk("P3b mu u g (kg m s^-2)", 44.0 * U * 9.81, 7.1695e-25, 1e-4)
chk("P3b H rocky (m)", 4.1430e-21 / 7.1695e-25, 5778.6, 1e-4)
chk("P3b H ratio (~109)", 6.3050e5 / 5778.6, 109.1, 5e-4)

# (c) transmission modulation of the hot Jupiter
chk("P3c ddelta/delta", 2 * 5 * 6.3050e5 / 8.6e7, 7.3314e-2, 1e-4)
chk("P3c ddelta (abs)", 7.3314e-2 * 1.5281e-2, 1.1203e-3, 1e-4)
chk("P3c ddelta (ppm ~1120)", 1.1203e-3 * 1e6, 1120.0, 5e-3)

# ── Problem 4: equilibrium temperature and the habitable zone ────────────
# (a) Earth equilibrium temperature
chk("P4a L (1-A) (W)", LSUN * 0.7, 2.6796e26, 1e-4)
chk("P4a 16 pi sigma d^2", 16 * math.pi * SIGMA * AU**2, 6.3785e16, 1e-4)
chk("P4a T^4 (K^4)", 2.6796e26 / 6.3785e16, 4.2010e9, 1e-4)
chk("P4a T_eq Earth (K)", (4.2010e9) ** 0.25, 254.6, 5e-4)

# (b) solar habitable zone, Venus and Mars fluxes
chk("P4b d_in Sun (AU)", 1 / math.sqrt(1.06), 0.9713, 1e-4)
chk("P4b d_out Sun (AU)", 1 / math.sqrt(0.35), 1.6903, 1e-4)
chk("P4b S_eff Venus", 1 / 0.72**2, 1.929, 5e-4)
chk("P4b S_eff Mars", 1 / 1.52**2, 0.4328, 5e-4)

# (c) K- and M-dwarf habitable zones, K-dwarf lifetime
chk("P4c K dwarf d_in (AU)", math.sqrt(0.3 / 1.06), 0.5320, 1e-4)
chk("P4c K dwarf d_out (AU)", math.sqrt(0.3 / 0.35), 0.9258, 1e-4)
chk("P4c M dwarf d_in (AU)", math.sqrt(5e-4 / 1.06), 0.02172, 1e-4)
chk("P4c M dwarf d_out (AU)", math.sqrt(5e-4 / 0.35), 0.03780, 1e-4)
chk("P4c 0.7^-2.5", 0.7 ** (-2.5), 2.4392, 1e-4)
chk("P4c t_MS K dwarf (Gyr)", 10 * 2.4392, 24.39, 5e-4)

# ── Problem 5: direct imaging and the Drake equation ─────────────────────
# (a) angular separations at 10 pc
chk("P5a theta_Earth (rad)", AU / (10 * PC), 4.8477e-7, 1e-4)
chk("P5a theta_Earth (arcsec)", 4.8477e-7 * RAD_ARCSEC, 0.09999, 1e-4)
chk("P5a theta_Jupiter (arcsec)", 5 * 0.09999, 0.5000, 5e-4)

# (b) habitable-zone angular extents at 10 pc
chk("P5b Sun HZ inner (arcsec)", 0.9713 / 10, 0.09713, 1e-4)
chk("P5b Sun HZ outer (arcsec)", 1.6903 / 10, 0.16903, 1e-4)
chk("P5b M dwarf inner (arcsec)", 0.02172 / 10, 2.172e-3, 1e-4)
chk("P5b M dwarf outer (arcsec)", 0.03780 / 10, 3.780e-3, 1e-4)

# (c) log-uniform Drake toy model
chk("P5c mean log10 N", 4 * (-5.0), -20.0, 1e-6)
chk("P5c var one factor", 10**2 / 12, 8.3333, 1e-4)
chk("P5c sigma log10 N", math.sqrt(4 * 8.3333), 5.7735, 1e-4)
chk("P5c z-score of N=1", (0 - (-20.0)) / 5.7735, 3.464, 5e-4)

print()
print(f"{N_CHECKS} checks, {len(FAIL)} failures")
if FAIL:
    for name in FAIL:
        print(f"  FAIL: {name}")
    sys.exit(1)
print("ALL OK")
