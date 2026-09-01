(mock_exams)=
# Mock exams

Three mock exams and their full solutions are collected on this page as the course runs.
They have the same shape and level as the final written exam and are the best gauge of what to expect.
The first two are available below; the third will appear here as the course runs.

| # | Exam | Solutions |
|---|---|---|
| 1 | [Mock exam 1 (PDF)](_static/exams/mockexam01.pdf) | [Solutions (PDF)](_static/exams/mockexam01_solutions.pdf) |
| 2 | [Mock exam 2 (PDF)](_static/exams/mockexam02.pdf) | [Solutions (PDF)](_static/exams/mockexam02_solutions.pdf) |
| 3 | Coming soon | Coming soon |

(must_know_list)=
## What you must know by heart

The final exam is closed book: a calculator and a pen are all that is allowed.
The twelve relations below are the ones you are expected to know from memory and apply without prompting.
Every other formula a question needs, for example the vis-viva equation, the Roche limit, or the Jeans escape flux, is printed in the question itself.

The same list is available as a PDF in the course style: [Download the formula list (PDF)](_static/exams/formulalist.pdf).

**1. Newton's law of gravitation**

$$
F = \frac{G M m}{r^2}, \qquad U = -\frac{G M m}{r}
$$

The attractive force between masses $M$ and $m$ at separation $r$, and the corresponding gravitational potential energy.
This pair underlies all orbital dynamics and the energy release of accretion and differentiation.
The force law drives the orbit derivations of {ref}`Lecture 1 <lecture01>`; the energy form is introduced in {ref}`Lecture 2 <lecture02>` and drives the heating budgets of {ref}`Lecture 4 <lecture04>`.

**2. Circular orbit speed**

$$
v_{\mathrm{c}} = \sqrt{\frac{G M}{r}}
$$

The speed of a body on a circular orbit of radius $r$ around a central mass $M$, from the balance of gravitational and centripetal acceleration.
Derived in {ref}`Lecture 1 <lecture01>`; generalised by the vis-viva equation of {ref}`Lecture 2 <lecture02>`.

**3. Escape velocity**

$$
v_{\mathrm{esc}} = \sqrt{\frac{2 G M}{r}}
$$

The minimum speed needed to escape to infinity from distance $r$, from setting kinetic plus potential energy to zero.
It controls impact energetics and which gases a planet can retain.
Introduced in {ref}`Lecture 2 <lecture02>`; central to atmospheric escape in {ref}`Lecture 5 <lecture05>`.

**4. Kepler's third law**

$$
P^2 = \frac{4 \pi^2 a^3}{G M}
$$

The orbital period $P$ of an orbit with semi-major axis $a$ around a central mass $M$.
It is the primary tool for weighing central bodies and for converting exoplanet periods into orbital distances.
Derived in Newtonian form in {ref}`Lecture 1 <lecture01>`; restated in {ref}`Lecture 2 <lecture02>` and applied to exoplanets in {ref}`Lecture 13 <lecture13>`.

**5. Mean density**

$$
M = \frac{4}{3} \pi R^3 \bar{\rho}
$$

The relation between mass, radius, and bulk density $\bar{\rho}$.
Bulk density is the first-order constraint on whether a body is made of rock, ice, or gas.
Used throughout {ref}`Lecture 8 <lecture08>` and {ref}`Lecture 13 <lecture13>`.

**6. Hydrostatic equilibrium**

$$
\dv{P}{r} = -\rho g
$$

The pressure gradient that balances gravity in any static fluid layer.
It structures both atmospheres and interiors and is the starting point of the scale-height and central-pressure estimates.
Introduced in {ref}`Lecture 5 <lecture05>` and {ref}`Lecture 8 <lecture08>`.

**7. Ideal gas law**

$$
P = n \kB T = \frac{\rho \kB T}{\mu\, m_u}
$$

The equation of state of a dilute gas, with number density $n$, mean molecular weight $\mu$, and atomic mass unit $m_u$.
It closes the hydrostatic equation for atmospheres.
Introduced in {ref}`Lecture 5 <lecture05>`.

**8. Isothermal scale height**

$$
H = \frac{\kB T}{\mu\, m_u\, g}
$$

The e-folding height of pressure in an isothermal atmosphere, from hydrostatic equilibrium plus the ideal gas law.
Hotter or lighter atmospheres are more extended; stronger gravity compresses them.
Derived in {ref}`Lecture 5 <lecture05>`.

**9. Stefan-Boltzmann law**

$$
F = \sigma T^4
$$

The radiative flux from an ideal (blackbody) surface at temperature $T$, with $\sigma$ the Stefan-Boltzmann constant.
{ref}`Lecture 3 <lecture03>` states the general form $F = \epsilon \sigma T^4$, with emissivity $\epsilon \leq 1$ close to 1 for most planetary surfaces.
It governs how planets shed heat to space.

**10. Equilibrium temperature (energy balance)**

$$
\frac{S}{4} (1 - A) = \sigma T_{\mathrm{eq}}^4
\qquad \Longrightarrow \qquad
T_{\mathrm{eq}} = \left[ \frac{S (1 - A)}{4 \sigma} \right]^{1/4}
$$

Absorbed stellar flux (stellar constant $S$, Bond albedo $A$, the factor 4 from the ratio of a sphere's surface to its cross-section) equals emitted thermal flux.
This balance sets the baseline temperature of every planet before greenhouse warming.
Derived in {ref}`Lecture 5 <lecture05>`; extended to the greenhouse model in {ref}`Lecture 9 <lecture09>` and applied to exoplanets in {ref}`Lecture 13 <lecture13>`.

**11. Thermal energy per particle**

$$
E_{\mathrm{th}} = \frac{3}{2} \kB T
$$

The mean kinetic energy of a gas particle at temperature $T$.
Comparing thermal and gravitational energy per molecule decides between retention and escape of an atmosphere.
The escape physics of {ref}`Lecture 5 <lecture05>` and {ref}`Lecture 10 <lecture10>` builds on this comparison; the Jeans parameter there uses $\kB T$ as the thermal scale.

**12. Radioactive decay**

$$
N(t) = N_0\, e^{-\lambda t}, \qquad t_{1/2} = \frac{\ln 2}{\lambda}
$$

The exponential decay of a parent isotope with decay constant $\lambda$ and half-life $t_{1/2}$.
It powers radiogenic heating of interiors and underlies all radiometric dating.
The half-lives behind radiogenic heating appear in {ref}`Lecture 3 <lecture03>`; the decay law itself is introduced with radiometric dating in {ref}`Lecture 12 <lecture12>`.
