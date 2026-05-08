"""PREM (Dziewonski & Anderson 1981) tabulator.

Returns rho [g/cm^3], v_P [km/s], v_S [km/s] for any depth z [km]
between 0 and 6371 km, using the polynomial-in-x coefficients of
Table 1 of Dziewonski & Anderson 1981 (Phys. Earth Planet. Inter.
25, 297). x = r / 6371 is the dimensionless normalised radius.

This is the isotropic, transversely-averaged form. Anisotropy in the
upper 220 km is averaged over for plotting purposes.
"""
from __future__ import annotations

import numpy as np

R_EARTH = 6371.0  # km

# Each tuple: (r_min_km, r_max_km, [rho coeffs], [vP coeffs], [vS coeffs])
# Polynomial: f(x) = c0 + c1*x + c2*x^2 + c3*x^3, x = r / R_EARTH
LAYERS = [
    # Inner core
    (0.0, 1221.5,
     [13.0885,  0.0,    -8.8381,  0.0],
     [11.2622,  0.0,    -6.3640,  0.0],
     [ 3.6678,  0.0,    -4.4475,  0.0]),
    # Outer core
    (1221.5, 3480.0,
     [12.5815, -1.2638, -3.6426, -5.5281],
     [11.0487, -4.0362,  4.8023, -13.5732],
     [ 0.0,     0.0,     0.0,    0.0]),
    # Lower mantle: D" plus the rest of the lower mantle have the same density polynomial.
    # We use the unified lower-mantle density curve below; for v_P/v_S we treat 3480-3630
    # ('D"' layer) and 3630-5600 with their respective coefficients.
    (3480.0, 3630.0,
     [ 7.9565, -6.4761,  5.5283, -3.0807],
     [15.3891, -5.3181,  5.5242, -2.5514],
     [ 6.9254,  1.4672, -2.0834,  0.9783]),
    (3630.0, 5600.0,
     [ 7.9565, -6.4761,  5.5283, -3.0807],
     [24.9520, -40.4673, 51.4832, -26.6419],
     [11.1671, -13.7818, 17.4575, -9.2777]),
    (5600.0, 5701.0,
     [ 7.9565, -6.4761,  5.5283, -3.0807],
     [29.2766, -23.6027,  5.5242, -2.5514],
     [22.3459, -17.2473, -2.0834,  0.9783]),
    # Transition zone
    (5701.0, 5771.0,
     [ 5.3197, -1.4836,  0.0,     0.0],
     [19.0957, -9.8672,  0.0,     0.0],
     [ 9.9839, -4.9324,  0.0,     0.0]),
    (5771.0, 5971.0,
     [11.2494, -8.0298,  0.0,     0.0],
     [39.7027, -32.6166, 0.0,     0.0],
     [22.3512, -18.5856, 0.0,     0.0]),
    (5971.0, 6151.0,
     [ 7.1089, -3.8045,  0.0,     0.0],
     [20.3926, -12.2569, 0.0,     0.0],
     [ 8.9496, -4.4597,  0.0,     0.0]),
    # Upper mantle (LVZ + LID)
    (6151.0, 6291.0,
     [ 2.6910,  0.6924,  0.0,     0.0],
     [ 4.1875,  3.9382,  0.0,     0.0],
     [ 2.1519,  2.3481,  0.0,     0.0]),
    (6291.0, 6346.6,
     [ 2.6910,  0.6924,  0.0,     0.0],
     [ 4.1875,  3.9382,  0.0,     0.0],
     [ 2.1519,  2.3481,  0.0,     0.0]),
    # Crust
    (6346.6, 6356.0,
     [ 2.900,   0.0,     0.0,     0.0],
     [ 6.800,   0.0,     0.0,     0.0],
     [ 3.900,   0.0,     0.0,     0.0]),
    (6356.0, 6368.0,
     [ 2.600,   0.0,     0.0,     0.0],
     [ 5.800,   0.0,     0.0,     0.0],
     [ 3.200,   0.0,     0.0,     0.0]),
    # Ocean (we replace by upper crust for plotting purposes)
    (6368.0, 6371.0,
     [ 2.600,   0.0,     0.0,     0.0],
     [ 5.800,   0.0,     0.0,     0.0],
     [ 3.200,   0.0,     0.0,     0.0]),
]


def _poly(coeffs, x):
    return coeffs[0] + coeffs[1] * x + coeffs[2] * x * x + coeffs[3] * x ** 3


def prem(r_km: np.ndarray):
    """Return rho [g/cm^3], v_P [km/s], v_S [km/s] for radius r in km."""
    r = np.atleast_1d(np.asarray(r_km, dtype=float))
    rho = np.full_like(r, np.nan)
    vP = np.full_like(r, np.nan)
    vS = np.full_like(r, np.nan)
    x = r / R_EARTH
    for (r0, r1, c_rho, c_vP, c_vS) in LAYERS:
        in_layer = (r >= r0) & (r <= r1)
        if not np.any(in_layer):
            continue
        rho[in_layer] = _poly(c_rho, x[in_layer])
        vP[in_layer] = _poly(c_vP, x[in_layer])
        vS[in_layer] = _poly(c_vS, x[in_layer])
    return rho, vP, vS


def prem_at_depth(z_km: np.ndarray):
    """As prem() but takes depth (km below surface)."""
    return prem(R_EARTH - np.asarray(z_km))
