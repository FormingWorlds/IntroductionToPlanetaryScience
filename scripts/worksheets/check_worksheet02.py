"""Recompute every printed number in Worksheet 2 and its solutions.

Follows the printed-chain policy: each derived value is computed from the
values as PRINTED in the sheet (at their displayed precision), not from
higher-precision internal values, so a student who follows the printed
checkpoints reproduces every digit.

Run: python3 scripts/worksheets/check_worksheet02.py
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
    print(f"{'OK  ' if ok else 'FAIL'} {name:42s} got {got:.6g}  printed {printed:.6g}")
    if not ok:
        FAIL.append(name)


# ── Problem 1: the radiogenic clock ─────────────────────────────────────
M_E = 5.972e24
chk("P1a M_BSE", (1 - 0.32) * M_E, 4.0610e24)
c238, c235, c232, c40 = 20e-9, 0.14e-9, 80e-9, 28e-9
h238, h235, h232, h40 = 9.5e-5, 5.7e-4, 2.6e-5, 2.9e-5
r238, r235, r232, r40 = c238 * h238, c235 * h235, c232 * h232, c40 * h40
chk("P1a 238U rate", r238, 1.9000e-12)
chk("P1a 235U rate", r235, 7.9800e-14)
chk("P1a 232Th rate", r232, 2.0800e-12)
chk("P1a 40K rate", r40, 8.1200e-13)
h_today = 1.9000e-12 + 0.0798e-12 + 2.0800e-12 + 0.8120e-12
chk("P1a sum (checkpoint)", h_today, 4.8718e-12)
chk("P1a power (TW)", 4.872e-12 * 4.0e24 / 1e12, 19.488, 1e-3)

f238, f235, f232, f40 = 2 ** (4.5 / 4.47), 2 ** (4.5 / 0.704), 2 ** (4.5 / 14.0), 2 ** (4.5 / 1.25)
chk("P1b factor 238U", f238, 2.0093)
chk("P1b factor 235U", f235, 83.98, 1e-3)
chk("P1b factor 232Th", f232, 1.2497)
chk("P1b factor 40K", f40, 12.126)
s238 = 1.9000 * 2.0093
s235 = 0.0798 * 83.98
s232 = 2.0800 * 1.2497
s40 = 0.8120 * 12.126
chk("P1b scaled 238U", s238, 3.8177)
chk("P1b scaled 235U", s235, 6.7016)
chk("P1b scaled 232Th", s232, 2.5994)
chk("P1b scaled 40K", s40, 9.8463)
h_form = (3.8177 + 6.7016 + 2.5994 + 9.8463) * 1e-12
chk("P1b sum (checkpoint)", h_form, 2.2965e-11)
chk("P1b power (TW)", 2.297e-11 * 4.0e24 / 1e12, 91.88, 1e-3)
chk("P1b ratio", 2.297e-11 / 4.872e-12, 4.7147, 1e-3)

chk("P1c half-lives", 10 / 0.72, 13.9, 2e-3)
chk("P1c decay factor", 2 ** 13.9, 1.53e4, 5e-3)

# ── Problem 2: conduction vs convection ─────────────────────────────────
L2 = (1.737e6) ** 2
chk("P2a L^2", L2, 3.0172e12)
tau_s = 3.0172e12 / 1e-6
chk("P2a tau (s)", tau_s, 3.0172e18)
chk("P2a tau (yr, checkpoint)", 3.0172e18 / 3.156e7, 9.5602e10)
chk("P2a tau / age", 9.56e10 / 4.57e9, 20.9, 2e-3)
t_age = 4.57e9 * 3.156e7
chk("P2a age (s)", t_age, 1.4423e17)
chk("P2a L (m)", math.sqrt(1e-6 * 1.4423e17), 3.798e5)

num1 = 4000 * 10 * 2e-5 * 2500
chk("P2b alpha rho g dT", num1, 2000)
chk("P2b d^3", (3e6) ** 3, 2.7e19)
chk("P2b Ra (checkpoint)", 2000 * 2.7e19 / 1e15, 5.4e7)
chk("P2b Ra/Ra_c", 5.4e7 / 1708, 3.162e4)
chk("P2c Nu", (3.162e4) ** (1 / 3), 31.62)

# P2d sketch: TikZ mapping x = T/700 (per cm), y = -depth/578; anchors from the notes
chk("P2d sketch x(300 K)", 300 / 700, 0.43, 5e-3)
chk("P2d sketch x(2500 K)", 2500 / 700, 3.57, 2e-3)
chk("P2d sketch x(4000 K)", 4000 / 700, 5.71, 2e-3)
chk("P2d sketch y(100 km)", 100 / 578, 0.17, 2e-2)
chk("P2d sketch y(2690 km)", 2690 / 578, 4.65, 2e-3)
chk("P2d sketch y(2890 km)", 2890 / 578, 5.0, 1e-3)
# drawn adiabat slope between the lithosphere base and the top of D-double-prime
slope = (3.57 - 1.86) * 700 / ((4.65 - 0.17) * 578)
chk("P2d sketch adiabat slope (K/km)", slope, 0.5, 0.1)
chk("P2e 2^(4/3)", 2 ** (4 / 3), 2.52, 1e-3)

# ── Problem 3: thermal evolution model ──────────────────────────────────
chk("P3b dT/dt (K/s)", (20e12 - 47e12) / 5.0e27, -5.400e-15)
chk("P3b dT/dt (K/Gyr)", -5.400e-15 * 3.156e16, -170.4)

C, Q0, T0, HF, TAU = 5.0e27, 47e12, 2500.0, 94e12, 2.91
T, t, dt = 3000.0, 0.0, 1e-4
Tmax, tmax = T, 0.0
n = int(4.5 / dt)
for _ in range(n):
    H = HF * math.exp(-t / TAU)
    Q = Q0 * (T / T0) ** (4 / 3)
    T += (H - Q) / C * 3.156e16 * dt
    t += dt
    if T > Tmax:
        Tmax, tmax = T, t
chk("P3c peak T", Tmax, 3110, 3e-3)
chk("P3c peak t (Gyr)", tmax, 1.2, 3e-2)
chk("P3c final T", T, 2670, 2e-3)
H_end = HF * math.exp(-4.5 / TAU)
Q_end = Q0 * (T / T0) ** (4 / 3)
chk("P3c final H (TW)", H_end / 1e12, 20.0, 3e-3)
chk("P3c final Q (TW)", Q_end / 1e12, 51.4, 3e-3)
chk("P3c Urey ratio", H_end / Q_end, 0.39, 3e-3)

# ── Problem 4: core formation and Hf-W ──────────────────────────────────
v = (2 / 9) * 4000 * 5 * (5e-3) ** 2 / 0.1
chk("P4a v (checkpoint)", v, 1.1111)
chk("P4a crossing (s)", 1.5e6 / 1.111, 1.3501e6)
chk("P4a crossing (d)", 1.3501e6 / 86400, 15.6, 2e-3)

chk("P4b x(D-1)", 0.32 * 9999, 3200, 2e-4)
chk("P4b fraction (checkpoint)", 1 / 3201, 3.124e-4)
chk("P4c excess ratio", 1e-3 / 3.124e-4, 3.20, 2e-3)

denom = 1e4 * 25 * 1.02e-4
chk("P4d denominator", denom, 25.5)
chk("P4d e^-lt (checkpoint)", 20 / 25.5, 0.784, 1e-3)
chk("P4d t_c (Myr)", -math.log(0.784) / 7.79e-2, 3.1238)
chk("P4e Hf-W window (Myr)", 5 * 8.9, 44.5)

# ── Problem 5: dynamos and shields ──────────────────────────────────────
chk("P5a 10^(1/6)", 10 ** (1 / 6), 1.4678)
chk("P5a compressed r_mp", 10 / 1.4678, 6.813)
chk("P5b Rm (checkpoint)", 5e-4 * 3.0e5 / 1, 150)
chk("P5c tau_ohm (s)", (3.0e5) ** 2 / 1, 9.0e10)
chk("P5c tau_ohm (yr)", 9.0e10 / 3.156e7, 2852, 1e-3)

print()
if FAIL:
    print(f"{len(FAIL)} FAILURES: {FAIL}")
    raise SystemExit(1)
print(f"ALL OK ({N_CHECKS} checks)")
