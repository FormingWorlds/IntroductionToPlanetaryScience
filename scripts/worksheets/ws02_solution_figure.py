"""Generate the thermal-evolution figure for Worksheet 2, Problem 3.

Integrates the worksheet's thermal-evolution model and saves the two-panel
temperature and power history to
``worksheets/worksheet02/figures/thermal_evolution_solution.pdf``. The problem
statement embeds the figure, so it appears on both the problem sheet and the
solutions sheet; students read the peak, the endpoint, and the Urey ratio off
its curves.

Run from the repository root:  python3 scripts/worksheets/ws02_solution_figure.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "worksheets/worksheet02/figures/thermal_evolution_solution.pdf"

C = 5.0e27        # J/K   : heat capacity of the silicate shell (M_BSE * c_p)
Q_0 = 47e12       # W     : convective heat loss at the reference temperature
T_0 = 2500.0      # K     : reference mantle temperature contrast (today)
H_F = 94e12       # W     : radiogenic heating at t = 0 (formation)
TAU_R = 2.91      # Gyr   : effective decay time of the summed long-lived isotopes
T_INIT = 3000.0   # K
T_END = 4.5       # Gyr
SEC_PER_GYR = 3.156e16


def main() -> None:
    dt = 1e-4
    n = int(T_END / dt)
    t_arr = np.zeros(n)
    T_arr = np.zeros(n)
    H_arr = np.zeros(n)
    Q_arr = np.zeros(n)
    T, t = T_INIT, 0.0
    for i in range(n):
        H = H_F * np.exp(-t / TAU_R)
        Q = Q_0 * (T / T_0) ** (4.0 / 3.0)
        t_arr[i], T_arr[i], H_arr[i], Q_arr[i] = t, T, H, Q
        T += (H - Q) / C * SEC_PER_GYR * dt
        t += dt

    i_max = int(np.argmax(T_arr))
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6.0), sharex=True)
    ax1.plot(t_arr, T_arr, color="#1f77b4", lw=2.0)
    ax1.set_ylabel("Mantle temperature contrast $T$ (K)")
    ax2.plot(t_arr, H_arr / 1e12, color="#d62728", lw=1.8, label="$H(t)$ heating")
    ax2.plot(t_arr, Q_arr / 1e12, color="#2ca02c", lw=1.8, label="$Q(T)$ heat loss")
    ax2.set_xlabel("Time after formation (Gyr)")
    ax2.set_ylabel("Power (TW)")
    ax2.legend()
    for ax in (ax1, ax2):
        ax.grid(linestyle=":", alpha=0.4)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT)
    print(f"  peak {T_arr[i_max]:.0f} K at {t_arr[i_max]:.2f} Gyr; "
          f"final {T_arr[-1]:.0f} K; Urey {H_arr[-1] / Q_arr[-1]:.3f}")
    print(f"  plot : {OUT}")


if __name__ == "__main__":
    main()
