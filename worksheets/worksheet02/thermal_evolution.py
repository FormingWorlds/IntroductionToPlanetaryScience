"""Minimal thermal evolution model for Worksheet 2, Problem 3(c).

Integrates C dT/dt = H(t) - Q(T) for Earth's silicate shell:

    H(t) = H_F * np.exp(-t / TAU_R)         (radiogenic heating, single-exponential)
    Q(T) = Q_0 * (T / T_0) ** (4.0 / 3.0)   (parametrised convective heat loss)

Complete the two marked lines, then run:  python3 thermal_evolution.py
The script prints the peak temperature, the final temperature, and the final
Urey ratio H/Q, and saves the temperature history to thermal_evolution.pdf.
"""

import numpy as np
import matplotlib.pyplot as plt

C = 5.0e27        # J/K   : heat capacity of the silicate shell (M_BSE * c_p)
Q_0 = 47e12       # W     : convective heat loss at the reference temperature
T_0 = 2500.0      # K     : reference mantle temperature contrast (today)
H_F = 94e12       # W     : radiogenic heating at t = 0 (formation)
TAU_R = 2.91      # Gyr   : effective decay time of the summed long-lived isotopes
T_INIT = 3000.0   # K     : initial temperature contrast
T_END = 4.5       # Gyr   : integration time
SEC_PER_GYR = 3.156e16

dt = 1e-4  # Gyr
n = int(T_END / dt)
t_arr = np.zeros(n)
T_arr = np.zeros(n)
H_arr = np.zeros(n)
Q_arr = np.zeros(n)

T = T_INIT
t = 0.0
for i in range(n):
    # ---- complete the next two lines -------------------------------------
    H = ...   # radiogenic heating at time t  [W]
    Q = ...   # convective heat loss at temperature T  [W]
    # ----------------------------------------------------------------------
    t_arr[i], T_arr[i], H_arr[i], Q_arr[i] = t, T, H, Q
    T += (H - Q) / C * SEC_PER_GYR * dt
    t += dt

i_max = int(np.argmax(T_arr))
print(f"Peak temperature : {T_arr[i_max]:.0f} K at t = {t_arr[i_max]:.2f} Gyr")
print(f"Final temperature: {T_arr[-1]:.0f} K at t = {t_arr[-1]:.1f} Gyr")
print(f"Final Urey ratio : H/Q = {H_arr[-1] / Q_arr[-1]:.2f}")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6.4), sharex=True)
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
fig.savefig("thermal_evolution.pdf")
print("Wrote thermal_evolution.pdf")
