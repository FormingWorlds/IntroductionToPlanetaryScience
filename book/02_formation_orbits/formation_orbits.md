(lecture02)=
# Planet Formation 101 & Orbital Dynamics

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the stages of planet formation from protoplanetary disks, apply Kepler's laws and the vis-viva equation, and explain the role of orbital resonances, tides, and migration in shaping planetary systems.
```

```{seealso}
**Slides:** [Download Lecture 2 (PDF)](../_static/slides/lecture02.pdf)
```

## Star formation and protoplanetary disks

Every planetary system begins with the collapse of a molecular cloud, a cold ($T \sim 10$–$20$ K), dense region of the interstellar medium composed primarily of molecular hydrogen ($\mathrm{H_2}$) and helium, with about 1% by mass of heavier elements in the form of microscopic dust grains. When a region of such a cloud becomes sufficiently massive and dense, its self-gravity overcomes thermal and magnetic pressure support, triggering gravitational collapse. The critical mass for collapse is the **Jeans mass**:

$$
M_J \sim \frac{c_s^3}{\sqrt{G^3 \rho}}
$$ (eq:jeans-mass)

where $c_s$ is the sound speed, $G$ is the gravitational constant, and $\rho$ is the gas density. For typical molecular cloud conditions ($T \approx 10$ K, $n_{\mathrm{H_2}} \approx 10^4$ cm$^{-3}$), this gives $M_J \sim 1$–$10$ $\Msun$, comparable to the masses of stars.

### From collapse to disk

As a cloud core collapses, conservation of angular momentum plays a decisive role. Even a small initial rotation (inevitable in a turbulent interstellar medium) is amplified enormously as the material contracts. A cloud core with radius $R_0 \sim 0.1$ pc collapsing to stellar scales ($\sim 1$ $\Rsun$) would need to spin up by a factor of $\sim 10^7$ if angular momentum were perfectly conserved. The material cannot all fall onto the central protostar; instead, it settles into a **protoplanetary disk** (also called a circumstellar disk) orbiting the young star.

The result is a flattened, rotating structure of gas and dust extending from a few stellar radii to hundreds of AU. The central protostar accretes material from the disk over timescales of $\sim 1$–$3$ Myr, while the disk itself becomes the raw material for planet formation. Such regions are visible today in nearby star-forming complexes ({numref}`fig:carina-cliffs`).

```{figure} figures/carina_cliffs_jwst.avif
:name: fig:carina-cliffs
:width: 600px
:align: center

The "Cosmic Cliffs" of the Carina Nebula imaged by JWST/NIRCam. Embedded protostars and outflows are visible at the edge of the molecular cloud where ultraviolet radiation from young massive stars sculpts the gas. Such regions are the present-day analogues of the environment in which the Solar System was born. Credit: NASA/ESA/CSA/STScI.
```





### Disk structure and properties

Protoplanetary disks are not uniform: they have well-defined radial and vertical structure governed by the balance of gravity, pressure, and rotation:

- **Temperature gradient:** The disk is heated by stellar irradiation and viscous dissipation. Temperatures range from $> 1500$ K in the innermost regions (where silicates are vaporised) to $< 30$ K in the outer disk. This temperature profile determines which materials can condense as solids at each distance.

- **Surface density:** The mass distribution follows roughly a power-law profile $\Sigma(r) \propto r^{-p}$ with $p \approx 0.5$–$1.5$, meaning most of the mass is concentrated in the inner disk. Typical total disk masses are $\sim 0.01$–$0.1$ $\Msun$, a few percent of the stellar mass {cite:p}`Miotello2023`.

- **Dust-to-gas ratio:** In the interstellar medium, dust makes up about 1% of the total mass. In disks, this ratio can be locally enhanced by dust settling to the midplane and radial drift, with important consequences for planet formation.

- **Vertical structure:** The disk is geometrically thin, with a scale height $H/r \sim 0.03$–$0.1$ that increases with distance (a "flared" disk). Dust settles toward the midplane due to the vertical component of the star's gravity, creating a denser dust layer within the gas disk. The flared geometry and central dark midplane are directly visible in edge-on systems such as HH 30 ({numref}`fig:hh30`); a schematic summary of the radial-vertical structure is given in {numref}`fig:disk-schematic`.

```{figure} figures/hh30_edge_on.avif
:name: fig:hh30
:width: 500px
:align: center

Edge-on view of the embedded protoplanetary disk around HH 30, imaged by HST. The dark dust lane at the midplane and the bright bipolar nebulae illuminated by light scattering off the upper and lower disk surfaces directly visualise the flared, vertically thin geometry of a young protoplanetary disk. Credit: NASA/ESA/STScI.
```

```{figure} figures/andrews2020_disk_schematic.avif
:name: fig:disk-schematic
:width: 600px
:align: center

Schematic vertical and radial structure of a protoplanetary disk. The dust temperature decreases with radius from $> 1500$ K at the silicate sublimation front to $< 30$ K beyond the CO snow line; the gas scale height $H/r$ increases with radius, producing a flared geometry. Adapted from {cite:t}`Andrews2020`; see also {cite:t}`WilliamsCieza2011` for an earlier review of disk structure.
```

### The snow line and volatile distribution

A critical feature of any protoplanetary disk is the **snow line** (or ice line): the distance from the star beyond which water can condense as ice. In the solar nebula, this was located at roughly 2.5–3.5 AU, between the orbits of Mars and Jupiter. The snow line matters because:

1. **Beyond the snow line**, solid material is much more abundant: adding water ice to the rocky/metallic inventory roughly triples the available solid mass.
2. **The CHNOPS elements** (carbon, hydrogen, nitrogen, oxygen, phosphorus, sulphur), essential for biology, are distributed between volatile and refractory phases depending on local disk temperature {cite:p}`Krijt2023`. The location where a planet forms relative to various ice lines determines its initial volatile budget.

Ice lines for other species ($\mathrm{CO_2}$, $\mathrm{CO}$, $\mathrm{N_2}$, $\mathrm{NH_3}$) exist at progressively larger distances, creating a compositional gradient across the disk ({numref}`fig:snowlines`).

```{figure} figures/oberg2011_snowlines.avif
:name: fig:snowlines
:width: 600px
:align: center

Sequential condensation of major volatile species across a protoplanetary disk and the resulting C/O ratio of grains (dashed) and gas (solid) as a function of disk radius. The H$_2$O ice line at $\sim 2$ AU lowers grain C/O and raises gas C/O; the CO$_2$ ice line at $\sim 10$ AU shifts gas C/O further upward; and beyond the CO ice line at $\sim 40$ AU the gas C/O reaches unity. The dotted line marks the solar reference. The radial sequencing of these ice lines controls the volatile composition that forming planets inherit from their formation zone. Reproduced from {cite:t}`Oberg2011`, Fig. 2.
```

### Observational evidence: ALMA

The Atacama Large Millimeter/submillimeter Array (ALMA) has revolutionised our understanding of protoplanetary disks. The landmark 2014 observation of HL Tauri ({numref}`fig:hl-tau`) revealed a young disk ($\sim 1$ Myr) with a stunning series of concentric bright rings and dark gaps at AU-scale resolution {cite:p}`ALMAPartnership2015`.

```{figure} figures/hl_tau.avif
:name: fig:hl-tau
:width: 500px
:align: center

ALMA image of the protoplanetary disk around HL Tauri, a young ($\sim 1$ Myr) star in the Taurus molecular cloud, at 1.3 mm wavelength {cite:p}`ALMAPartnership2015`. The concentric bright rings and dark gaps extend to $\sim 100$ AU. The gaps may be carved by forming planets, though other mechanisms (ice lines, magnetically driven structures) have also been proposed. Credit: ALMA (ESO/NAOJ/NRAO), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

The DSHARP survey (Disk Substructures at High Angular Resolution Project) extended this to 20 nearby disks ({numref}`fig:dsharp`), revealing that ring-and-gap substructure is ubiquitous: virtually every disk observed at high resolution shows some form of structure {cite:p}`Andrews2018`. This suggests that the conditions for planet formation are established very early in disk evolution.

```{figure} figures/dsharp_composite.avif
:name: fig:dsharp
:width: 700px
:align: center

Composite of protoplanetary disks observed at $\sim 5$ AU resolution by the ALMA DSHARP survey {cite:p}`Andrews2018`. Each panel shows a different young system at the same spatial scale; rings, gaps, spirals, and crescents are present in essentially every target, demonstrating that such substructure is the rule rather than the exception in young disks. Credit: ALMA (ESO/NAOJ/NRAO), S. Andrews et al. 2018, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

### Disk lifetimes

Infrared excess surveys of young stellar clusters at different ages show that the fraction of stars retaining optically thick inner disks declines from $\sim 80$% at 1 Myr to $< 10$% by $\sim 6$ Myr {cite:p}`Haisch2001`. The median disk lifetime is roughly **3–5 Myr**, with significant scatter. This sets a hard deadline for gas giant formation: if a planet's core does not grow large enough to capture a gaseous envelope before the disk disperses, it will remain a rocky or icy body.

Disk dispersal is driven by a combination of viscous accretion onto the star, photoevaporation by stellar ultraviolet and X-ray radiation, and possibly magnetohydrodynamic winds.


## Dust coagulation and planetesimal formation

The raw building material for planets consists of sub-micrometre dust grains (silicates, metal oxides, and, beyond the snow line, ices) embedded in the gas disk. Growing from micrometre-sized dust to thousand-kilometre planets is a factor of $\sim 10^{13}$ in size, and the physics changes dramatically at each scale.

### Grain growth: sticking and settling

In the dense midplane of the disk, dust grains collide due to Brownian motion, turbulence, and differential settling. At low velocities ($\lesssim 1$ m s$^{-1}$), grains stick together through van der Waals forces, forming **fractal aggregates**: fluffy, porous structures that grow progressively larger ({numref}`fig:blum-aggregates`) {cite:p}`Blum2008`. This process is efficient up to millimetre and centimetre sizes.

```{figure} figures/blum2008_aggregate_growth.avif
:name: fig:blum-aggregates
:width: 500px
:align: center

Microgravity laboratory experiments on the earliest stage of dust coagulation. Inset: image of fractal aggregates of $1.9$ µm SiO$_2$ monomers grown in space-shuttle experiments. Main panel: the mean aggregate mass (in units of monomer mass) grows as a power law in time under Brownian-motion-driven sticking, with fractal dimension $D \approx 1.4$. Adapted from {cite:t}`Blum2008`.
```

### Growth barriers

Beyond centimetre scales, several barriers impede further growth:

- **Bouncing barrier ($\sim$ mm):** At slightly higher collision velocities, compacted aggregates bounce off each other rather than sticking, stalling growth at millimetre sizes.

- **Fragmentation barrier ($\sim$ cm):** At collision velocities above $\sim 1$–$10$ m s$^{-1}$ (depending on material), aggregates shatter rather than merge. Silicate particles are particularly fragile; icy particles can survive higher-velocity impacts.

- **Radial drift barrier ($\sim$ metre):** Solid particles orbiting in a gas disk experience a headwind because the gas, partially supported by its own pressure gradient, orbits slightly slower than the Keplerian velocity. This headwind causes particles to lose angular momentum and spiral inward. The drift rate peaks for metre-sized boulders, which would fall into the star in $\sim 100$–$1000$ years, far faster than they can grow. This is the notorious **metre-size barrier** or **radial drift barrier**.

The combined effect of these barriers is summarised in {numref}`fig:growth-barriers`: incremental sticking alone cannot bridge the gap between dust grains and planetesimals, motivating collective mechanisms such as the streaming instability discussed below.

```{figure} figures/drazkowska2023_growth_barriers.avif
:name: fig:growth-barriers
:width: 600px
:align: center

Grain size as a function of orbital distance, with the classical growth barriers indicated. The fragmentation barrier (red, shown for three fragmentation velocities) and drift barrier (blue) bound the achievable grain size; their location depends on disk radius and the local fragmentation velocity, so the canonical "mm bouncing, cm fragmentation, m drift" sequence is realised only at characteristic disk radii of a few AU. Together these barriers prevent classical incremental sticking from bridging the gap between dust grains and planetesimals, motivating collective mechanisms such as the streaming instability. Adapted from {cite:t}`Drazkowska2023` (see also {cite:t}`Birnstiel2016`).
```

### The streaming instability

The solution to the radial drift problem appears to be **collective effects**. When the local dust-to-gas mass ratio approaches or exceeds unity (which can happen through settling to the midplane and accumulation at pressure bumps), the drag interaction between dust and gas changes qualitatively. Instead of all particles drifting inward, they can spontaneously clump through a process called the **streaming instability** {cite:p}`Johansen2007`.

In the streaming instability, particles that happen to be concentrated accelerate the local gas toward the Keplerian velocity (reducing the headwind), which attracts more drifting particles from further out. This positive feedback loop creates dense filaments and clumps of pebbles ({numref}`fig:streaming`). When these clumps become sufficiently dense, they collapse under their own gravity to form **planetesimals**, solid bodies with radii of $\sim 50$–$500$ km, essentially bypassing the difficult metre-to-kilometre growth step that direct sticking cannot achieve.

```{figure} figures/simon2016_streaming.avif
:name: fig:streaming
:width: 500px
:align: center

Snapshot of a local shearing-box simulation showing the streaming instability concentrating pebbles into dense filaments that exceed the local Roche density and gravitationally collapse into planetesimals. Reproduced from {cite:t}`Simon2016`.
```

### Pebble accretion

Once planetesimals exist, those that are large enough can grow efficiently by sweeping up the abundant mm- to cm-sized "pebbles" that pervade the disk. This **pebble accretion** mechanism ({numref}`fig:pebble-accretion`) {cite:p}`Lambrechts2012` is far more efficient than the classical picture of accreting only planetesimals, because gas drag causes pebbles to be strongly deflected toward the growing body, dramatically increasing the effective cross-section. Pebble accretion enables planetary cores to grow to $\sim 10$ $\Mearth$ within the disk lifetime, fast enough to trigger gas accretion and form giant planets.

```{figure} figures/lambrechts2012_pebble_accretion.avif
:name: fig:pebble-accretion
:width: 500px
:align: center

Schematic of pebble accretion. Gas drag deflects mm- to cm-sized particles toward a growing planetary embryo, enlarging the effective accretion cross-section far beyond the geometric value. This mechanism allows cores to reach $\sim 10\,\Mearth$ within the disk lifetime, in contrast to the much slower classical planetesimal-only accretion. Adapted from {cite:t}`Lambrechts2012`.
```

### Preferential formation sites

Planet formation does not proceed uniformly throughout the disk. Planets preferentially form at locations where conditions favour dust concentration: pressure bumps (where the gas pressure has a local maximum, halting radial drift), ice lines (where sublimation and recondensation enhance local solid density), and the edges of dead zones (regions of low turbulence). The resulting non-uniform distribution of forming planets helps explain the diverse architectures observed in exoplanetary systems {cite:p}`Drazkowska2023`. {numref}`fig:solar-nebula` summarises the modern roadmap from sub-µm dust to fully assembled planets.

```{figure} figures/drazkowska2023_roadmap.avif
:name: fig:solar-nebula
:width: 600px
:align: center

Modern roadmap of the planet-formation sequence: sub-µm dust grains in the parent molecular cloud, settling and coagulation in the disk midplane, planetesimal formation via the streaming instability, growth to planetary cores via pebble accretion, and either gas envelope capture (giant planets) or terrestrial planet assembly via giant impacts after disk dispersal. Adapted from {cite:t}`Drazkowska2023`.
```


## Runaway and oligarchic growth

Once a population of planetesimals has formed, gravitational interactions take over as the dominant growth mechanism.

### Runaway growth

In a swarm of planetesimals, larger bodies have a decisive advantage: their stronger gravity allows them to focus incoming trajectories toward themselves, effectively increasing their collision cross-section far beyond their geometric size. The effective cross-section is enhanced by the **gravitational focusing factor**:

$$
\sigma_{\mathrm{eff}} = \pi R^2 \left(1 + \frac{v_{\mathrm{esc}}^2}{v_{\infty}^2}\right)
$$ (eq:grav-focusing)

where $R$ is the body's radius, $v_{\mathrm{esc}} = \sqrt{2GM/R}$ is the escape velocity, and $v_{\infty}$ is the relative velocity at infinity (approach velocity). When $v_{\mathrm{esc}} \gg v_{\infty}$ (which occurs when the random velocities of planetesimals are small), the focusing factor can be enormous. Because $v_{\mathrm{esc}}$ increases with mass, the largest body grows faster than its neighbours: this is **runaway growth**. A single body can rapidly outpace the rest of the swarm, reaching the mass of the Moon to Mars within $\sim 10^5$ years.

### Oligarchic growth

Runaway growth is self-limiting. As the largest bodies grow, they gravitationally stir up the surrounding planetesimals, increasing the random velocities $v_{\infty}$ and thereby reducing the gravitational focusing factor. Growth transitions to the **oligarchic regime** {cite:p}`Kokubo1998`, in which a few dozen roughly equal-mass "oligarchs" dominate their local feeding zones, each separated by $\sim 5$–$10$ mutual Hill radii. They continue to grow by accreting the remaining smaller planetesimals, but more slowly, until each reaches its **isolation mass**: the mass at which it has consumed all available material in its feeding zone. In the inner solar system, the isolation mass is $\sim 0.01$–$0.1$ $\Mearth$, insufficient to explain the terrestrial planets.

### Core accretion: building giant planets

The dominant model for giant planet formation is the **core accretion** model {cite:p}`Pollack1996`. In this scenario:

1. A solid core grows by accreting planetesimals and pebbles in the outer disk (beyond the snow line, where more solid material is available).
2. Once the core reaches a critical mass of $\sim 10$–$20$ $\Mearth$, its gravity becomes strong enough to bind a substantial gas envelope from the surrounding disk.
3. The envelope contracts and cools, allowing more gas to flow in, leading to a phase of rapid, runaway gas accretion. Within $\sim 10^5$ years, the planet can accumulate hundreds of Earth masses of hydrogen and helium.
4. Accretion ceases when the planet opens a gap in the disk or when the disk itself dissipates.

This model naturally explains why Jupiter and Saturn are massive (they formed in the solid-rich region beyond the snow line and reached critical core mass before disk dispersal) and why Uranus and Neptune are smaller (they likely reached critical mass too late, after most gas had been removed). The mass-vs-time evolution of the three core-accretion phases is shown in {numref}`fig:core-accretion`.

```{figure} figures/drazkowska2023_core_accretion.avif
:name: fig:core-accretion
:width: 600px
:align: center

Mass evolution of a forming giant planet in the canonical core-accretion picture {cite:p}`Pollack1996`. Phase 1: rapid solid-core growth by planetesimal and pebble accretion. Phase 2: slow envelope contraction at near-constant total mass. Phase 3: runaway gas accretion once the gas envelope mass equals the core mass ($\sim 10$–$20\,\Mearth$ for the nominal Jupiter case), leading to a Jupiter-mass object on a $\sim 10^5$ yr timescale. Adapted from {cite:t}`Drazkowska2023`.
```

### Gravitational instability: an alternative pathway

An alternative scenario for gas giant formation is **direct gravitational instability** of the gas disk {cite:p}`Boss1997`. If a massive disk cools sufficiently rapidly, it can fragment into self-gravitating clumps that contract directly into giant planets, bypassing the slow step of building a solid core. This mechanism can form giant planets very quickly ($\sim 10^3$ years), but requires disk conditions (high mass, efficient cooling) that may only be realised at large orbital distances ($\gtrsim 30$–$50$ AU) or in unusually massive disks. It remains debated whether the giant planets of the solar system formed this way.

### The giant impact phase

In the inner solar system, after the disk has dispersed and gas drag is no longer available to circularise orbits, the protoplanetary embryos (oligarchs) undergo a final phase of chaotic **giant impacts** lasting $\sim 10$–$100$ Myr. Their orbits become increasingly eccentric and crossing, leading to collisions that assemble the final terrestrial planets from a smaller number of embryos. The Moon-forming impact (a collision between the proto-Earth and a Mars-sized body, Theia) is the most dramatic example from our solar system.

### Geophysical evolution during formation

Planet formation is not merely an assembly process: it drives profound geophysical changes. The energy delivered by accretion and giant impacts melts the growing planet, producing a global **magma ocean**. In this molten state, dense metallic iron sinks to form a core, while lighter silicates float to form the mantle, a process called **core-mantle differentiation**. Early radioactive heating from short-lived isotopes (particularly ${}^{26}\mathrm{Al}$, with a half-life of 0.7 Myr) can melt even small planetesimals, initiating differentiation before the planet has finished assembling {cite:p}`Lichtenberg2023`. The thermal and chemical state inherited from this formation epoch profoundly shapes a planet's subsequent evolution: its magnetic field, volcanic activity, atmospheric outgassing, and ultimately its habitability ({ref}`Lecture 3 <lecture03>`, {ref}`Lecture 4 <lecture04>`).


## Kepler's laws and orbital elements

Having discussed how planets form, we now turn to how they move. Planetary orbits are the most precisely measured quantities in all of planetary science, and they are governed by some of the simplest equations in physics.

### Kepler's three laws

In the early 17th century, Johannes Kepler distilled decades of precise observations by Tycho Brahe into three empirical laws:

1. **The law of ellipses:** Each planet moves in an **elliptical orbit** with the Sun at one focus.

2. **The law of equal areas:** A line connecting the planet to the Sun sweeps out **equal areas in equal times**. This means the planet moves fastest at perihelion (closest approach) and slowest at aphelion (farthest distance).

3. **The harmonic law:** The square of the orbital period is proportional to the cube of the semi-major axis:

$$
P^2 = \frac{4\pi^2}{G(M_1 + M_2)}\, a^3
$$ (eq:kepler-third-law)

As we saw in {ref}`Lecture 1 <lecture01>`, Newton showed that all three laws follow from his universal law of gravitation. Kepler's third law, in its Newtonian form (Eq. {eq}`eq:kepler-third-law`), is one of the most useful equations in astronomy: it connects an easily measured quantity (the orbital period) to the total mass of the system. The geometry of the three laws is summarised in {numref}`fig:kepler-laws`, and the resulting solar-system architecture, with all eight planets plus the asteroid belt and Kuiper belt on a logarithmic semi-major-axis axis, is shown in {numref}`fig:ss-architecture`.

```{figure} figures/kepler_laws.svg
:name: fig:kepler-laws
:width: 500px
:align: center

Illustration of Kepler's three laws of planetary motion. (1) Orbits are ellipses with the Sun at one focus; (2) the radius vector sweeps out equal areas in equal times (shaded regions have equal area); (3) the period-squared is proportional to the semi-major axis cubed. Credit: Hankwang, [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/).
```

```{figure} figures/solar_system_architecture.avif
:name: fig:ss-architecture
:width: 750px
:align: center

Architecture of the Solar System on a logarithmic semi-major axis scale. The eight planets, Pluto, the asteroid main belt, and the Kuiper belt are shown to scale in distance; symbol size is scaled by $\log(1 + R/R_\oplus)$ so that all bodies remain visible. The asteroid main belt sits between Mars and Jupiter, near the present-day H$_2$O snow line at $\sim 3$ AU separating the rocky inner planets from the gas and ice giants. Planetary semi-major axes from the NASA Planetary Fact Sheet.
```

### Orbital elements

The orbit of a body in a gravitational field is fully described by **six orbital elements**:

| Element | Symbol | Description |
|---------|--------|-------------|
| Semi-major axis | $a$ | Size of the orbit (half the long axis of the ellipse) |
| Eccentricity | $e$ | Shape of the orbit ($e = 0$ is circular, $0 < e < 1$ is elliptical) |
| Inclination | $i$ | Tilt of the orbital plane relative to a reference plane |
| Longitude of ascending node | $\Omega$ | Orientation of the line where the orbital plane crosses the reference plane |
| Argument of perihelion | $\omega$ | Orientation of the ellipse within the orbital plane |
| True anomaly | $\nu$ | Position of the body along the orbit at a given time |

The first five elements define the size, shape, and orientation of the orbit; the sixth specifies where the body is at any moment. The geometric meaning of each element is illustrated in {numref}`fig:orbital-elements`.

```{figure} figures/orbital_elements.svg
:name: fig:orbital-elements
:width: 400px
:align: center

The six classical orbital elements. The reference plane is shown in grey; the orbital plane is tilted by the inclination $i$. The ascending node ($\Omega$) and argument of perihelion ($\omega$) orient the orbit in space. Credit: Lasunncty, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

In the solar system, most planets have nearly circular orbits ($e < 0.1$) and low inclinations ($i < 3°$), reflecting the disk-like origin of the system. Exceptions include Mercury ($e = 0.206$) and, among dwarf planets, Pluto ($e = 0.25$, $i = 17°$), hinting at a more complex dynamical history.


## Two-body problem and the vis-viva equation

### The two-body problem

Consider two bodies of masses $m_1$ and $m_2$ interacting through gravity alone. In the centre-of-mass frame, the problem reduces to a single body of **reduced mass**

$$
\mu = \frac{m_1 m_2}{m_1 + m_2}
$$

moving in the gravitational field of a fixed central mass $M = m_1 + m_2$.

The total orbital energy is the sum of kinetic and gravitational potential energy:

$$
E = \frac{1}{2}\mu v^2 - \frac{G m_1 m_2}{r}
$$

A fundamental result of orbital mechanics is that **the total energy depends only on the semi-major axis**:

$$
E = -\frac{G m_1 m_2}{2a}
$$ (eq:orbital-energy)

This means that two orbits with the same semi-major axis have the same total energy, regardless of their eccentricity. A circular orbit and a highly eccentric orbit with the same $a$ are energetically equivalent: they simply distribute kinetic and potential energy differently along the orbit.

### The vis-viva equation

Combining the total energy expression (Eq. {eq}`eq:orbital-energy`) with the instantaneous kinetic and potential energy, we obtain the **vis-viva equation** (Latin for "living force"):

$$
\boxed{v^2 = G(m_1 + m_2)\left(\frac{2}{r} - \frac{1}{a}\right)}
$$ (eq:vis-viva)

For the common case where $m_2 \ll m_1$ (e.g., a planet orbiting a star), this simplifies to:

$$
v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)
$$

The vis-viva equation tells us the speed $v$ of an orbiting body at any distance $r$ from the central mass, given the semi-major axis $a$. It has important special cases:

- **Circular orbit** ($r = a$): $v_{\mathrm{circ}} = \sqrt{GM/a}$
- **Escape velocity** ($a \to \infty$, $E = 0$): $v_{\mathrm{esc}} = \sqrt{2GM/r}$

The escape velocity is exactly $\sqrt{2}$ times the circular orbital velocity at the same distance, a factor worth remembering.


## Blackboard derivation: The vis-viva equation

```{admonition} Blackboard derivation: The vis-viva equation
:class: tip

**Goal:** Derive the vis-viva equation from energy conservation in a Keplerian orbit, then apply it to calculate orbital velocities for Earth and Halley's comet.

**Setup.**

Consider a planet of mass $m$ in an elliptical orbit around a star of mass $M$ (with $m \ll M$). The orbit has semi-major axis $a$ and eccentricity $e$. At any point, the planet is at distance $r$ from the star and moves with speed $v$.

The total mechanical energy is conserved:

$$
E = \frac{1}{2}mv^2 - \frac{GMm}{r} = \mathrm{constant}
$$

We want to express $E$ in terms of $a$ alone, then derive a formula for $v(r)$.

**Derivation.**

**Step 1: Evaluate energy at perihelion and aphelion.**

At **perihelion** (closest approach), $r_p = a(1 - e)$, and at **aphelion** (farthest distance), $r_a = a(1 + e)$. Writing energy conservation at these two points:

$$
\frac{1}{2}mv_p^2 - \frac{GMm}{a(1-e)} = \frac{1}{2}mv_a^2 - \frac{GMm}{a(1+e)}
$$

**Step 2: Use angular momentum conservation.**

At perihelion and aphelion, the velocity is purely tangential (perpendicular to the radius vector), so angular momentum conservation gives:

$$
L = m\, v_p\, r_p = m\, v_a\, r_a \quad \Rightarrow \quad v_p\, a(1-e) = v_a\, a(1+e)
$$

Therefore $v_p / v_a = (1+e)/(1-e)$.

**Step 3: Solve for the total energy.**

Substituting back and solving (the algebra is left as an exercise; try it!), we find:

$$
E = -\frac{GMm}{2a}
$$

This is a remarkable result: the total energy depends *only* on the semi-major axis, not on the eccentricity.

**Step 4: Write the vis-viva equation.**

Setting the total energy equal to the instantaneous kinetic + potential energy:

$$
\frac{1}{2}mv^2 - \frac{GMm}{r} = -\frac{GMm}{2a}
$$

Dividing through by $m/2$ and rearranging:

$$
\boxed{v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)}
$$

**Application: Earth's orbital velocity.**

For Earth ($a = 1$ AU $= 1.496 \times 10^{11}$ m, $e = 0.017$):

| Point | Distance $r$ | Velocity |
|-------|-------------|----------|
| Perihelion | $a(1-e) = 1.471 \times 10^{11}$ m | $v_p = 30.29$ km s$^{-1}$ |
| Aphelion | $a(1+e) = 1.521 \times 10^{11}$ m | $v_a = 29.29$ km s$^{-1}$ |

The variation is only about $\pm 0.5$ km s$^{-1}$ around the mean, because Earth's orbit is nearly circular. The mean orbital velocity is approximately $v \approx 2\pi a / P \approx 29.8$ km s$^{-1}$.

**Application: Halley's comet.**

For a dramatic contrast, consider Halley's comet ($a = 17.83$ AU, $e = 0.967$):

| Point | Distance $r$ | Velocity |
|-------|-------------|----------|
| Perihelion | $a(1-e) = 0.586$ AU | $v_p = 54.6$ km s$^{-1}$ |
| Aphelion | $a(1+e) = 35.1$ AU | $v_a = 0.91$ km s$^{-1}$ |

Halley's comet hurtles through the inner solar system at nearly twice Earth's speed, yet crawls beyond Neptune's orbit at less than 1 km s$^{-1}$. This enormous range is a direct consequence of the vis-viva equation applied to a highly eccentric orbit; both speed profiles are plotted in {numref}`fig:visviva`.

**Note:** The vis-viva equation is the generalisation of the Kepler mass formula derived in {ref}`Lecture 1 <lecture01>`. There, we used a circular orbit ($r = a$) to get $v^2 = GM/a$, which is just the vis-viva equation with $r = a$.
```

```{figure} figures/visviva_earth_halley.avif
:name: fig:visviva
:width: 600px
:align: center

Orbital speed $v(r)$ from the vis-viva equation for Earth ($a = 1$ AU, $e = 0.0167$) and Halley's comet ($a = 17.83$ AU, $e = 0.967$). Filled circles mark perihelion and aphelion of each orbit. Earth's nearly circular orbit gives $v \approx 30$ km s$^{-1}$ throughout, whereas Halley's high eccentricity produces a $\sim 60\times$ swing in speed between perihelion ($54.6$ km s$^{-1}$) and aphelion ($0.91$ km s$^{-1}$).
```


## Orbital resonances

When two orbiting bodies have orbital periods in a ratio of small integers, they are in a **mean-motion resonance** (MMR). At each conjunction (closest approach), the bodies are at the same relative positions, and their mutual gravitational perturbations add up coherently over many orbits, rather than averaging to zero.

### Mean-motion resonances

A $p$:$q$ mean-motion resonance (with $p > q$) means that the inner body completes $p$ orbits in the same time the outer body completes $q$ orbits. The gravitational kicks at each conjunction always occur at the same orbital phases, which can either stabilise or destabilise the configuration depending on the geometry {cite:p}`MurrayDermott1999`.

Resonances are widespread in the solar system:

| Resonance | Bodies | Period ratio |
|-----------|--------|-------------|
| 3:2 | Pluto-Neptune | Pluto completes 2 orbits per 3 of Neptune |
| Near 5:2 | Jupiter-Saturn | "Great inequality": near-resonance drives long-period perturbations |
| 3:1, 5:2, 7:3, 2:1 | Several asteroid gaps | Kirkwood gaps in the asteroid belt ({ref}`Lecture 12 <lecture12>`) |
| 1:1 | Jupiter Trojans | Co-orbital asteroids at L4 and L5 Lagrange points |

### The Laplace resonance

The most famous resonance in the solar system is the **Laplace resonance** of Jupiter's three inner Galilean moons: Io, Europa, and Ganymede. Their orbital periods are in a 1:2:4 ratio {cite:p}`Peale1979`:

| Moon | Period (days) | Ratio to Io |
|------|:---:|:---:|
| Io | 1.769 | 1 |
| Europa | 3.551 | $\approx$ 2 |
| Ganymede | 7.155 | $\approx$ 4 |

This three-body resonance is maintained by tidal interactions with Jupiter. The key consequence is that it **forces non-zero orbital eccentricities**: Io's eccentricity is maintained at $e \approx 0.004$ (small, but crucial). This continual eccentricity forcing drives tidal flexing inside Io, generating enough heat to make it the most volcanically active body in the solar system ({numref}`fig:laplace-resonance`, {numref}`fig:io-volcanism`), a connection we will explore in {ref}`Lecture 3 <lecture03>`.

```{figure} figures/laplace_resonance.avif
:name: fig:laplace-resonance
:width: 500px
:align: center

The Laplace resonance of the Galilean moons. Io, Europa, and Ganymede have orbital periods in the ratio 1 : 2 : 4, so the same conjunction geometry repeats every Io period. The resulting periodic gravitational kicks force a non-zero eccentricity on Io ($e \approx 0.004$), driving the tidal heating that powers its volcanism {cite:p}`Peale1979`.
```

```{figure} figures/io_volcanism.avif
:name: fig:io-volcanism
:width: 500px
:align: center

Half-disk view of Jupiter's moon Io imaged by the Galileo spacecraft, showing an active volcanic plume rising in profile against the dark sky at the limb. The mottled, sulphur-rich surface is reshaped on geological timescales by the underlying volcanism. Resonance-forced eccentricity from the Laplace resonance feeds tidal dissipation that makes Io the most volcanically active body in the Solar System. Credit: NASA/JPL/University of Arizona.
```


## Tidal forces and tidal locking

### The tidal force

A tidal force arises whenever a gravitational field varies across the finite extent of an extended body. Consider a moon of radius $R_s$ at distance $d$ from a planet of mass $M_p$. The near side of the moon experiences a stronger gravitational pull than the far side, creating a differential force that tends to elongate the moon along the line connecting it to the planet. The tidal acceleration across the moon is approximately:

$$
\Delta a_{\mathrm{tidal}} \approx \frac{2 G M_p R_s}{d^3}
$$

This $1/d^3$ dependence (compared to the $1/d^2$ dependence of gravity itself) means that tidal forces are strongly distance-dependent.

### Tidal bulges and energy dissipation

The tidal force raises **tidal bulges** on both sides of the body: one facing the perturber and one on the opposite side. If the body rotates at a different rate than it orbits (which is initially the case for most moons and planets), the bulges are carried away from the line connecting the two bodies. This misalignment creates a torque that transfers angular momentum between the body's spin and its orbit, gradually changing both. The energy dissipated in continually deforming the body is converted to heat: this is **tidal heating**, which powers Io's volcanism and may maintain subsurface oceans on Europa and Enceladus ({ref}`Lecture 3 <lecture03>`).

### Tidal locking (synchronous rotation)

Over time, the tidal torque slows the faster-spinning body until its rotation period equals its orbital period, a state called **synchronous rotation** or **tidal locking** ({numref}`fig:tidal-locking`). In this configuration, the same face always points toward the perturber, and the tidal bulge is aligned with the connecting line, so no further torque acts.

```{figure} figures/tidal_locking.avif
:name: fig:tidal-locking
:width: 500px
:align: center

Tidal locking of the Moon with the Earth. The Moon's rotation period equals its orbital period, so the same hemisphere always faces Earth and the tidal bulge raised by Earth stays aligned with the Earth-Moon line. This synchronous state was reached through billions of years of tidal dissipation {cite:p}`MurrayDermott1999`. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

The Moon is tidally locked to Earth; this is why we always see the same face. All four Galilean moons are tidally locked to Jupiter. Most large moons in the solar system are synchronous rotators. The timescale for tidal locking scales as $\propto d^6 / (M_p^2 R_s^3)$, which is why more distant moons and smaller bodies take longer to lock {cite:p}`MurrayDermott1999`.

### The Roche limit

There is a minimum distance at which a self-gravitating body can survive the tidal force of a larger body. Inside this distance, the **Roche limit** ({numref}`fig:roche-geometry`), tidal forces exceed the satellite's self-gravity, and the body is torn apart. For a fluid satellite of density $\rho_s$ orbiting a planet of radius $R_p$ and density $\rho_p$:

$$
d_R \approx 2.46\, R_p \left(\frac{\rho_p}{\rho_s}\right)^{1/3}
$$ (eq:roche-limit)

```{figure} figures/roche_geometry.avif
:name: fig:roche-geometry
:width: 750px
:align: center

Roche limit geometry. (a) A self-gravitating fluid satellite (blue) is rounded at safe orbital distance, but at the Roche limit $d_R$ the differential tidal acceleration across its diameter exceeds its self-gravity and it is stretched and torn apart along the line to the primary. (b) Tidal acceleration across a $200$ km icy body and the body's surface self-gravity, plotted against orbital distance from Saturn (in units of $R_p$). The simple crossing of the two curves defines the *rigid* Roche limit at $d_R^{\rm rigid} \approx 1.11\,R_p$ for $\rho_s = 1000$ kg m$^{-3}$; the textbook *fluid* Roche limit $d_R \approx 2.17\,R_p$ (red dotted line) carries an additional factor that accounts for tidal deformation of the satellite.
```

For Saturn ($R_p = 58{,}232$ km, $\rho_p = 687$ kg m$^{-3}$) and an icy satellite ($\rho_s \approx 1000$ kg m$^{-3}$):

$$
d_R \approx 2.46 \times 58{,}232 \times \left(\frac{687}{1000}\right)^{1/3} \approx 126{,}500 \text{ km} \approx 2.17\, R_p
$$

Saturn's main ring system ({numref}`fig:saturn-rings`) extends from about 67,000 km to 137,000 km from Saturn's centre, mostly within the Roche limit (the fluid approximation gives $d_R \approx 126{,}000$ km, but the exact boundary depends on the rigidity and composition of the orbiting material; the outer A ring extends slightly beyond the fluid Roche limit but remains within the rigid-body limit). The rings consist of countless small particles that cannot coalesce into a moon because tidal forces prevent their gravitational aggregation. We will derive the Roche limit in full in {ref}`Lecture 11 <lecture11>`.

```{figure} figures/saturn_rings.avif
:name: fig:saturn-rings
:width: 700px
:align: center

Saturn and its rings imaged by the Cassini wide-angle camera in April 2016. The main ring system spans roughly $67{,}000$ km to $137{,}000$ km from Saturn's centre and lies almost entirely within the fluid Roche limit at $\sim 126{,}000$ km. The countless cm- to m-sized icy particles that make up the rings cannot coalesce into a moon because Saturn's tides exceed their mutual self-gravity. Credit: NASA/JPL-Caltech/Space Science Institute (PIA21046).
```


## Planetary migration

The orbits of planets are not fixed after formation. Interactions between planets and the disk (and later, between planets themselves) can cause substantial **orbital migration**, moving planets from their birth locations to very different orbits {cite:p}`Paardekooper2023`.

### Planet-disk interactions

A planet embedded in a gaseous disk excites spiral density waves at **Lindblad resonances** (where the disk material orbits at frequencies commensurate with the planet's orbital frequency plus/minus its epicyclic frequency). These waves carry angular momentum away from the planet. Additionally, material co-orbiting with the planet (at the **corotation resonances**) exchanges angular momentum through horseshoe-shaped streamlines. The net torque on the planet determines whether it migrates inward or outward.

### Types of migration

- **Type I migration:** A low-mass planet (up to a few Earth masses) remains fully embedded in the disk and migrates due to the imbalance between inner and outer Lindblad torques. In a simple disk model, the outer torque slightly dominates, driving inward migration on timescales of $\sim 10^5$ years, potentially too fast, suggesting that additional physics (thermal effects, magnetic fields, disk structure) must slow or reverse migration in many cases.

- **Type II migration:** A massive planet (roughly Jupiter-mass and above) opens a **gap** in the disk, an annular region cleared of gas by the planet's gravity. The planet then migrates on the slower viscous timescale of the disk ($\sim 10^5$–$10^6$ years) as the disk accretes onto the star.

- **Type III migration:** In massive disks with a sharp density gradient near the planet, a rapid, runaway migration can occur when the co-orbital mass deficit (the difference between the disk mass that would fill the horseshoe region and the actual mass there) becomes comparable to the planet's mass. This can cause very fast inward or outward migration.

The disk-flow patterns that drive these torques, including the spiral wakes at Lindblad resonances and the horseshoe streamlines at corotation, are shown in {numref}`fig:migration`.

```{figure} figures/paardekooper2023_disk_flow.avif
:name: fig:migration
:width: 600px
:align: center

Disk surface-density response to an embedded planet, showing the outer-Lindblad spiral wake and the partial gap carved by the planet's gravity. The inset zoom shows the horseshoe streamlines and density-wave structure in the co-orbital region that exchange angular momentum with the planet. The torque imbalance between these structures sets whether the planet migrates inward or outward and underlies both Type I and Type II migration. Adapted from {cite:t}`Paardekooper2023`.
```

### The Nice model

After the gas disk has dispersed, the giant planets can still undergo migration through interactions with a remnant disk of planetesimals. The **Nice model** {cite:p}`Tsiganis2005` proposes that the giant planets formed in a more compact configuration than today (all within $\sim 20$ AU) and subsequently underwent a dynamical instability, likely triggered when Jupiter and Saturn crossed their mutual 2:1 mean-motion resonance ({numref}`fig:nice-model`). This instability scattered Uranus and Neptune outward to their current orbits, disrupted the primordial Kuiper Belt, and may have triggered a spike of impacts throughout the inner solar system (the "Late Heavy Bombardment," although its timing and intensity remain debated).

```{figure} figures/nesvorny2018_nice.avif
:name: fig:nice-model
:width: 600px
:align: center

Evolution of the giant planets through the Nice-model instability. Left panel: semi-major axes vs time, beginning compact (Jupiter at $\sim 5.4$ AU, Saturn at $\sim 8.7$ AU, Uranus at $\sim 15$ AU, Neptune at $\sim 20$ AU). Right panel: the Saturn / Jupiter period ratio, showing the rapid 2:1 mean-motion resonance crossing that triggers the instability. The crossing scatters Uranus and Neptune outward to their present orbits and disrupts the primordial trans-Neptunian planetesimal disk {cite:p}`Nesvorny2018`. Note that the original Tsiganis et al. 2005 simulation used a slightly more compact configuration (Neptune at $\sim 13.5$–$17$ AU); the figure shown is from {cite:t}`Nesvorny2018`.
```

### The Grand Tack

The **Grand Tack hypothesis** {cite:p}`Walsh2011` proposes that Jupiter first migrated inward to $\sim 1.5$ AU via Type II migration, then reversed course when Saturn caught up and became trapped in the **3:2 mean-motion resonance** with Jupiter: the combined torques from their mutual interaction with the disk drove both planets outward ("tacking," as in sailing). This inward-then-outward migration ({numref}`fig:grand-tack`) would have scattered and depleted material in the inner solar system, potentially explaining the small mass of Mars and the compositional structure of the asteroid belt.

```{figure} figures/walsh2011_grand_tack.avif
:name: fig:grand-tack
:width: 600px
:align: center

The Grand Tack scenario from a Walsh et al. (2011) simulation. Top panel: mass evolution of the four giant planets during the disk phase. Bottom panel: semi-major axis evolution; each curve is labelled with the planet's name on the track. Jupiter migrates inward to $\sim 1.5$ AU via Type II migration; once Saturn catches up and the two planets become trapped in their mutual 3:2 mean-motion resonance, the combined torques reverse the migration and both planets move outward. The episode depletes solid material in the inner disk, with consequences for Mars's small mass and the asteroid belt's compositional structure. Reproduced from {cite:t}`Walsh2011`.
```

### Observational evidence for migration

The strongest evidence that migration is real comes from **hot Jupiters**: gas giant exoplanets orbiting their host stars with periods of just a few days ($a \lesssim 0.1$ AU). These planets cannot have formed in situ (there is not enough material, and temperatures are too high for solids to exist), so they must have formed further out and migrated inward ({numref}`fig:hot-jupiters`). Additionally, ALMA observations of gaps in protoplanetary disks (such as those in HL Tau) may represent the signatures of embedded planets undergoing migration. We will revisit exoplanet demographics and the evidence for migration in {ref}`Lecture 13 <lecture13>`.

```{figure} figures/hot_jupiter_mass_period.avif
:name: fig:hot-jupiters
:width: 600px
:align: center

Confirmed exoplanets in mass-period space, generated from the NASA Exoplanet Archive (accessed 2026-04). Detection methods are colour-coded; Solar System planets are overplotted as black stars for reference. The cluster of giant planets ($M \gtrsim 0.1\,M_J$) at orbital periods of a few days, the "hot Jupiters", cannot have formed in situ at such close-in orbital distances and is widely interpreted as evidence for large-scale orbital migration; see {cite:t}`DawsonJohnson2018` for a review of the proposed formation pathways.
```


## Recent advances

The study of planet formation has been transformed by high-resolution imaging of protoplanetary disks. The ALMA DSHARP survey {cite:p}`Andrews2018` revealed that ring-and-gap substructure is ubiquitous in protoplanetary disks, even around young ($\lesssim 1$ Myr) stars. These structures are widely interpreted as signatures of embedded planets clearing gaps in the disk, implying that planet formation begins earlier and proceeds faster than previously thought, consistent with the pebble accretion paradigm {cite:p}`Lambrechts2012`.

Theoretical advances have been consolidated in the *Protostars and Planets VII* review volume {cite:p}`Drazkowska2023`, which presents an updated synthesis of planet formation theory incorporating ALMA constraints. Key developments include refined models of the streaming instability that forms planetesimals, improved treatments of pebble accretion in evolving disks, and new constraints on giant planet formation timescales from isotopic analyses of meteorites and Juno gravity measurements {cite:p}`Wahl2017`. The emerging picture is that giant planet cores must form within the first 1–3 Myr of disk evolution (before the gas disperses), placing tight constraints on the growth mechanisms ({ref}`Lecture 8 <lecture08>`).


## References

```{bibliography}
:filter: docname in docnames
```
