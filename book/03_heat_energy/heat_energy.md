(lecture03)=
# Lecture 3: Planetary Heat & Energy Transport

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to identify the main energy sources driving planetary evolution, distinguish between heat transport mechanisms, and apply scaling laws for convection and thermal evolution.
```

## Energy sources

A planet's geological and geophysical evolution is fundamentally governed by its **thermal history** — how much heat it starts with, how it generates new heat, and how efficiently it can lose that heat to space. Without internal heat, there would be no volcanism, no magnetic field, no plate tectonics, and no atmospheric outgassing. Understanding where planetary heat comes from is therefore the starting point for understanding planetary evolution.

There are four principal sources of heat in planets:

### Accretional heating

During planet formation ({ref}`lecture02`), gravitational potential energy is converted into kinetic energy as material falls onto the growing body, and that kinetic energy is converted into heat upon impact. The total gravitational energy released in assembling a uniform sphere of mass $M$ and radius $R$ from dispersed material is:

$$
E_{\mathrm{acc}} \sim \frac{3}{5} \frac{G M^2}{R}
$$ (eq:accretional-energy)

For Earth ($M = 5.97 \times 10^{24}$ kg, $R = 6.37 \times 10^6$ m), this gives $E_{\mathrm{acc}} \approx 2.2 \times 10^{32}$ J. If all this energy were retained as heat and distributed uniformly, it would raise the temperature by:

$$
\Delta T = \frac{E_{\mathrm{acc}}}{M c_p} \approx \frac{2.2 \times 10^{32}}{5.97 \times 10^{24} \times 1200} \approx 30{,}000 \text{ K}
$$

where $c_p \approx 1200$ J kg$^{-1}$ K$^{-1}$ is a representative specific heat for silicate rock. This is enough to melt Earth many times over. In practice, not all energy is retained — some is radiated back to space during accretion, especially in the later stages when the surface is molten and radiates efficiently. Nevertheless, accretional heating is more than sufficient to produce a fully molten planet — a **magma ocean** — by the end of formation {cite}`Lichtenberg2023`.

### Gravitational differentiation

When a planet melts (from accretional heating and other sources), dense metallic iron sinks to the centre while lighter silicates rise to form the mantle. This **core formation** process releases additional gravitational potential energy as the denser material moves to a lower gravitational potential. For Earth, the energy released by core–mantle differentiation is estimated at:

$$
E_{\mathrm{diff}} \approx 2 \times 10^{31} \text{ J}
$$

This is about 10% of the accretional energy, but is released relatively quickly during the differentiation process — further heating the interior and helping to sustain the early magma ocean. Gravitational differentiation is a one-time energy source: once the core has formed, this energy has been spent.

### Radioactive decay

The decay of naturally occurring radioactive isotopes provides a sustained heat source that continues to power planetary interiors billions of years after formation. There are two categories:

**Long-lived isotopes** have half-lives comparable to or longer than the age of the solar system. The four most important for planetary heat production are:

| Isotope | Half-life (Gyr) | Heat production (W kg$^{-1}$ of isotope) | Concentration in bulk silicate Earth |
|---------|:-:|:-:|:-:|
| ${}^{238}\mathrm{U}$ | 4.47 | $9.5 \times 10^{-5}$ | 20 ppb |
| ${}^{235}\mathrm{U}$ | 0.704 | $5.7 \times 10^{-4}$ | 0.14 ppb |
| ${}^{232}\mathrm{Th}$ | 14.0 | $2.6 \times 10^{-5}$ | 80 ppb |
| ${}^{40}\mathrm{K}$ | 1.25 | $2.9 \times 10^{-5}$ | 240 ppb |

These isotopes are **lithophile** ("rock-loving") elements that concentrate in the silicate mantle and crust rather than the metallic core. Together, they produce Earth's present-day radiogenic heat of approximately 20 TW (terawatts) {cite}`Jaupart2015`. Because the shorter-lived isotopes (${}^{235}\mathrm{U}$, ${}^{40}\mathrm{K}$) were more abundant in the past, total radiogenic heat production was 3–4 times higher at the time of Earth's formation (4.5 Gyr ago) than it is today.

**Short-lived isotopes** had half-lives of only a few million years and are now extinct, but were present when the solar system formed. The most important is ${}^{26}\mathrm{Al}$ (half-life 0.72 Myr), which was produced by nearby stellar nucleosynthesis and incorporated into the solar nebula. In the first few million years, ${}^{26}\mathrm{Al}$ was an extraordinarily potent heat source — it could melt planetesimals as small as a few kilometres in radius, initiating core formation and volatile loss even before planet-sized bodies had assembled {cite}`Lichtenberg2023`. The short-lived isotope ${}^{60}\mathrm{Fe}$ (half-life 2.6 Myr) also contributed, though to a lesser extent.

```{figure} figures/radiogenic_heat_evolution.svg
:name: fig:radiogenic-heat
:width: 500px
:align: center

Evolution of Earth's radiogenic heat production over time. The total heat production (black curve) is the sum of contributions from four long-lived isotopes: ${}^{238}\mathrm{U}$ (red), ${}^{235}\mathrm{U}$ (green), ${}^{232}\mathrm{Th}$ (grey), and ${}^{40}\mathrm{K}$ (blue). At the time of Earth's formation (4.5 Gyr ago), total radiogenic heat production was about 3–4 times higher than today, primarily due to the larger contributions of ${}^{40}\mathrm{K}$ and ${}^{235}\mathrm{U}$. Credit: Wikimedia Commons, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

### Tidal heating

When a body on a non-circular orbit is tidally deformed by a nearby massive companion, the periodic flexing of its interior dissipates energy as heat. This is a significant heat source for certain moons in the outer solar system, particularly Io and Enceladus. We will discuss tidal heating in detail in [section 7](tidal-dissipation) of this lecture.

### Earth's heat budget

The total heat flowing out of Earth's interior is approximately **47 TW** {cite}`DaviesDavies2010`. The approximate breakdown is:

| Source | Contribution |
|--------|:-:|
| Radiogenic heating (mantle + crust) | ~20 TW |
| Primordial (secular cooling) | ~15 TW |
| Core cooling and solidification | ~10 TW |
| Tidal dissipation (from the Moon) | ~0.1 TW |
| **Total** | **~47 TW** |

Roughly 40% of Earth's current heat loss is powered by ongoing radioactive decay, with the rest being the slow release of primordial heat stored since formation. This means Earth is still cooling — its interior temperature is gradually decreasing over geological time. The relative importance of these sources varies strongly across the solar system: small bodies like the Moon have lost most of their primordial heat long ago, while a tidally heated moon like Io has a heat budget dominated by tidal dissipation rather than radiogenic or primordial heat.


## Heat transport mechanisms

Heat moves through planetary interiors and escapes to space via three fundamental mechanisms: conduction, convection, and radiation. The dominance of each depends on the material properties and physical conditions at each depth.

### Conduction

In **conduction**, heat is transferred through a material by direct molecular or atomic collisions, without bulk motion of the material itself. In solids (such as rock or ice), thermal energy propagates as lattice vibrations (phonons); in metals, free electrons also carry heat. The rate of heat flow by conduction is described by **Fourier's law**:

$$
\vec{q} = -k \nabla T
$$ (eq:fourier-law)

where $\vec{q}$ is the heat flux (W m$^{-2}$), $k$ is the thermal conductivity (W m$^{-1}$ K$^{-1}$), and $\nabla T$ is the temperature gradient. The negative sign indicates that heat flows from hot to cold regions.

A closely related quantity is the **thermal diffusivity**, which controls how fast temperature disturbances propagate through a material:

$$
\kappa = \frac{k}{\rho c_p}
$$ (eq:thermal-diffusivity)

where $\rho$ is the density and $c_p$ is the specific heat capacity. Typical values for silicate rock are $k \approx 3$–$4$ W m$^{-1}$ K$^{-1}$ and $\kappa \approx 10^{-6}$ m$^2$ s$^{-1}$.

Conduction is inherently a **diffusive** process — slow and inefficient over large distances. As we will show in the blackboard derivation, the time for heat to conduct through a distance $L$ scales as $L^2/\kappa$, which becomes enormous for planet-sized bodies.

### Convection

In **convection**, heat is transported by the bulk motion of fluid. When a fluid layer is heated from below, hot material near the base becomes less dense (due to thermal expansion) and rises, while cool, denser material near the top sinks. This overturning circulation — **thermal convection** — is far more efficient at transporting heat than conduction.

Convection is the dominant heat transport mechanism in:
- Earth's **mantle** (solid-state convection of slowly creeping rock, with velocities of ~cm/year)
- Earth's **outer core** (liquid metal convection, driving the geodynamo)
- **Giant planet interiors** (convecting metallic hydrogen and other fluids)
- Planetary **atmospheres** (rising thermals, Hadley cells)

The efficiency of convection compared to conduction is quantified by the **Nusselt number** (discussed in [section 4](rayleigh-nusselt)).

### Radiation

Heat can also be transported by electromagnetic radiation. The radiative heat flux from a surface at temperature $T$ is given by the Stefan–Boltzmann law:

$$
F = \epsilon \sigma T^4
$$ (eq:stefan-boltzmann)

where $\sigma = 5.67 \times 10^{-8}$ W m$^{-2}$ K$^{-4}$ is the Stefan–Boltzmann constant and $\epsilon$ is the emissivity (close to 1 for most planetary surfaces). Radiation is the dominant mechanism for:
- Heat loss from planetary **surfaces** to space
- Energy transport through optically thin **atmospheres**
- Cooling of magma ocean surfaces in the early stages of planetary evolution

Inside solid planetary interiors, radiation is generally less important than conduction and convection because rocks are opaque at infrared wavelengths. However, at very high temperatures ($\gtrsim 2000$ K), radiative heat transfer through partially transparent silicates can become significant.

```{figure} figures/convection_cells.svg
:name: fig:convection-cells
:width: 400px
:align: center

Schematic of convection cells in a fluid heated from below. Hot material rises at the centre, spreads laterally along the top, cools, and sinks at the edges — completing a circulation loop. This is the fundamental mechanism by which planetary mantles, outer cores, and atmospheres transport heat. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

### Comparison

The key distinction is one of **timescale**. Conduction is a diffusive process that becomes prohibitively slow for large bodies. Convection is an advective process that can transport heat over large distances much more rapidly. This difference explains why small bodies (asteroids, small moons) cool primarily by conduction, while larger bodies (terrestrial planets, giant planets) must convect to lose their internal heat.


## Blackboard derivation: The conductive cooling timescale

```{admonition} Blackboard derivation (~10 min)
:class: tip

**Goal:** Derive the characteristic timescale for heat to conduct through a body of size $L$, and show that conduction alone cannot cool planet-sized bodies — motivating the need for convection.
```

### Setup

The starting point is the **heat diffusion equation** (also called the heat equation), which describes how temperature evolves in a conducting medium:

$$
\pdv{T}{t} = \kappa \nabla^2 T
$$ (eq:heat-equation)

where $T$ is temperature, $t$ is time, $\kappa$ is the thermal diffusivity (Eq. {eq}`eq:thermal-diffusivity`), and $\nabla^2 T$ is the Laplacian of the temperature field. In one dimension:

$$
\pdv{T}{t} = \kappa \pdv{^2 T}{x^2}
$$

This equation says that the rate of temperature change at any point is proportional to the curvature of the temperature profile — regions where the temperature profile is concave up ($\pdv{^2 T}{x^2} > 0$) heat up, and regions where it is concave down cool down.

### Derivation

We use **dimensional analysis** to extract the characteristic timescale. The heat equation relates:
- A time derivative: $\pdv{T}{t} \sim T/\tau$ (where $\tau$ is the timescale we seek)
- A spatial derivative: $\pdv{^2 T}{x^2} \sim T/L^2$ (where $L$ is the lengthscale)

Substituting into the heat equation:

$$
\frac{T}{\tau} \sim \kappa \frac{T}{L^2}
$$

The temperature $T$ cancels, giving:

$$
\boxed{\tau_{\mathrm{cond}} \sim \frac{L^2}{\kappa}}
$$ (eq:cooling-timescale)

This is the **conductive cooling timescale**. It tells us how long it takes for a thermal disturbance to propagate a distance $L$ by conduction alone. The key feature is the **$L^2$ dependence**: doubling the size of a body increases its conductive cooling time by a factor of four.

### Application

Using $\kappa \approx 10^{-6}$ m$^2$ s$^{-1}$ (typical for silicate rock), we can estimate the conductive cooling timescale for bodies of different sizes:

| Body | Length $L$ | $\tau_{\mathrm{cond}} = L^2/\kappa$ | In familiar units |
|------|:-:|:-:|:-:|
| 1 m boulder | 1 m | $10^6$ s | ~12 days |
| 100 km asteroid | $10^5$ m | $10^{16}$ s | ~300 Myr |
| Moon ($R = 1740$ km) | $1.7 \times 10^6$ m | $3 \times 10^{18}$ s | ~100 Gyr |
| Earth ($R = 6370$ km) | $6.4 \times 10^6$ m | $4 \times 10^{19}$ s | ~1300 Gyr |

A small boulder cools in days — consistent with everyday experience. A 100 km asteroid cools in hundreds of millions of years, which is long but shorter than the age of the solar system — so small asteroids should have cooled and solidified, consistent with the meteorite record. But for the Moon and Earth, the conductive cooling time far exceeds the age of the universe ($\sim 14$ Gyr). **Earth cannot cool by conduction alone.**

```{note}
This result tells us something profound: since Earth *is* losing heat at a rate of ~47 TW ({cite}`DaviesDavies2010`), there must be a more efficient transport mechanism operating in its interior. That mechanism is **convection**. The question of *when* convection occurs — and how vigorous it is — leads directly to the Rayleigh number.
```

(rayleigh-nusselt)=
## Rayleigh number and convective vigour

Whether a fluid layer convects or conducts depends on the competition between two forces: **buoyancy** (which drives convection) and **viscous resistance** (which opposes it). The balance between these forces is captured by a single dimensionless number.

### Onset of convection

Consider a horizontal fluid layer of depth $d$, heated from below with a temperature difference $\Delta T$ between the bottom and top boundaries. The hot fluid at the base is less dense than the cool fluid at the top — an inherently unstable configuration. But viscosity and thermal diffusion resist the onset of overturning. Convection begins only when the destabilising buoyancy force exceeds the stabilising effects of viscosity and thermal diffusion.

### The Rayleigh number

The **Rayleigh number** Ra quantifies this balance:

$$
\mathrm{Ra} = \frac{\alpha \rho g \Delta T \, d^3}{\kappa \eta}
$$ (eq:rayleigh-number)

where:
- $\alpha$ is the thermal expansion coefficient (K$^{-1}$) — how much the fluid expands when heated
- $\rho$ is the density (kg m$^{-3}$)
- $g$ is gravitational acceleration (m s$^{-2}$)
- $\Delta T$ is the temperature difference across the layer (K)
- $d$ is the layer depth (m)
- $\kappa$ is the thermal diffusivity (m$^2$ s$^{-1}$)
- $\eta$ is the dynamic viscosity (Pa s)

The numerator ($\alpha \rho g \Delta T \, d^3$) represents the **buoyancy force** driving convection. The denominator ($\kappa \eta$) represents the combined **dissipative forces** resisting it.

### Critical Rayleigh number

Convection occurs when Ra exceeds a critical value:

$$
\mathrm{Ra}_c \approx 1000
$$

(the exact value depends on the boundary conditions; $\mathrm{Ra}_c = 657.5$ for free-slip boundaries and $\mathrm{Ra}_c = 1707.8$ for rigid boundaries {cite}`Turcotte2002`). When $\mathrm{Ra} < \mathrm{Ra}_c$, heat is transported by conduction alone. When $\mathrm{Ra} \gg \mathrm{Ra}_c$, vigorous convection dominates.

For Earth's mantle, typical parameters are $\alpha \sim 2 \times 10^{-5}$ K$^{-1}$, $\rho \sim 4000$ kg m$^{-3}$, $g \sim 10$ m s$^{-2}$, $\Delta T \sim 2500$ K, $d \sim 3 \times 10^6$ m, $\kappa \sim 10^{-6}$ m$^2$ s$^{-1}$, and $\eta \sim 10^{21}$ Pa s. This gives:

$$
\mathrm{Ra}_{\oplus} \sim \frac{2 \times 10^{-5} \times 4000 \times 10 \times 2500 \times (3 \times 10^6)^3}{10^{-6} \times 10^{21}} \sim 10^7 \text{–} 10^8
$$

This is many orders of magnitude above $\mathrm{Ra}_c$ — confirming that Earth's mantle convects vigorously {cite}`Schubert2001`.

### The Nusselt number

The **Nusselt number** Nu measures how much more efficiently convection transports heat compared to conduction alone:

$$
\mathrm{Nu} = \frac{q_{\mathrm{total}}}{q_{\mathrm{cond}}}
$$ (eq:nusselt-number)

where $q_{\mathrm{total}}$ is the actual heat flux and $q_{\mathrm{cond}} = k \Delta T / d$ is the heat flux that would occur by conduction alone across the same temperature difference. When $\mathrm{Nu} = 1$, all heat is transported by conduction. When $\mathrm{Nu} \gg 1$, convection dominates.

A classic result from convection theory relates the Nusselt number to the Rayleigh number through a power law:

$$
\mathrm{Nu} \propto \mathrm{Ra}^\beta
$$ (eq:nu-ra-scaling)

where $\beta \approx 1/3$ for simple convection in a layer heated from below {cite}`Turcotte2002`. For Earth's mantle with $\mathrm{Ra} \sim 10^7$:

$$
\mathrm{Nu} \sim (10^7)^{1/3} \sim 200
$$

This means convection transports heat roughly 200 times more efficiently than conduction would across the same temperature drop — confirming the essential role of convection in planetary thermal evolution.


## Thermal boundary layers and mantle convection

### The boundary layer structure

A convecting planetary interior does not have a uniform temperature gradient. Instead, it develops a characteristic three-layer structure {cite}`Schubert2001`:

1. **Cold thermal boundary layer (TBL) at the top** — a thin conductive layer where temperature drops steeply from the hot interior to the cold surface. In Earth, this is the **lithosphere** — the rigid outer shell of the planet, approximately 100 km thick beneath oceans and up to 200 km beneath continents.

2. **Well-mixed convecting interior** — the bulk of the mantle, where temperatures vary only slowly with depth (following an **adiabatic gradient**). Vigorous convective stirring keeps this region nearly isothermal on large scales.

3. **Hot thermal boundary layer at the base** — a thin layer above the core–mantle boundary where temperature rises steeply into the hot core. In Earth, this corresponds to the **D'' layer** (the lowermost ~200 km of the mantle), where the temperature increases from the mantle adiabat (~2500 K) to the core–mantle boundary temperature (~4000 K).

The temperature drop across the whole mantle is accommodated almost entirely in these two thin boundary layers, while the interior between them is nearly isothermal.

### Plate tectonics: the mobile lid regime

The cold thermal boundary layer at Earth's surface behaves in a remarkable way: rather than remaining as a stagnant conductive lid, it **breaks into rigid plates** that move laterally, subduct back into the mantle at convergent boundaries, and are recycled. This is **plate tectonics** — the surface expression of mantle convection in a **mobile lid regime**.

Plate tectonics is the most efficient way for a rocky planet to lose heat, because subducting plates carry cold surface material deep into the mantle, while hot material rises at mid-ocean ridges and volcanic hotspots. This vigorous recycling is why Earth's surface heat flow is as high as it is.

### The stagnant lid regime

Most other rocky bodies in the solar system — including Venus, Mars, Mercury, and the Moon — appear to operate in a **stagnant lid regime**, where the cold thermal boundary layer forms a single, thick, immobile shell. Without plate tectonics, heat can only escape through the lid by conduction (and volcanism, where magma punches through the lid). This is less efficient than plate tectonics, so stagnant lid planets cool more slowly and may retain more internal heat.

Why Earth has plate tectonics while other rocky planets do not is one of the major unsolved problems in geophysics. Factors likely include:
- The presence of **water** in the mantle, which weakens rocks and enables the formation of narrow shear zones (plate boundaries)
- The **size** of the planet — a larger planet has more vigorous convection and higher stresses in the lithosphere
- The **thermal history** — the balance between internal heating and surface cooling

### Mantle plumes

In addition to the broad convective circulation, hot upwellings can develop from the hot thermal boundary layer at the base of the mantle. These **mantle plumes** are narrow columns of anomalously hot material that rise through the mantle and produce localised volcanism at the surface — so-called **hotspots** (e.g., Hawaii, Iceland, Yellowstone). Plumes are a direct consequence of the thermal boundary layer structure: just as the cold TBL can become gravitationally unstable and sink (subduction), the hot TBL can become unstable and rise.

```{figure} figures/earth_interior_cutaway.svg
:name: fig:earth-interior
:width: 500px
:align: center

Cutaway view of Earth's interior, showing the layered structure from crust to inner core. The mantle convects in broad circulation patterns; the cold surface boundary layer (lithosphere) breaks into tectonic plates, while the hot boundary layer at the core–mantle boundary spawns mantle plumes. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```


## Surface heat flow

The heat flowing out of a planet's surface is one of the most directly measurable quantities in planetary geophysics, and it provides a fundamental constraint on the thermal state of the interior.

### Earth's surface heat flow

Earth's average surface heat flux is approximately $90$ mW m$^{-2}$, totalling about **47 TW** when integrated over the entire surface area {cite}`DaviesDavies2010`. This heat flow is not uniform:

- **Oceanic regions** account for about 70% of the total heat loss, despite covering about 60% of the surface. The high oceanic heat flow reflects the thinness of oceanic lithosphere and the creation of new, hot crust at mid-ocean ridges.
- **Continental regions** account for about 30% of the total heat loss. Continental heat flow is lower on average because the thick continental lithosphere is an effective insulator, and because continents preferentially accumulate heat-producing elements (U, Th, K) in the crust.

The spatial pattern of heat flow — highest at mid-ocean ridges, decreasing with the age of the ocean floor, lowest in old continental shields — is a direct expression of plate tectonics and confirms that convection controls Earth's heat loss.

### Comparison across the solar system

| Body | Surface heat flux (mW m$^{-2}$) | Total heat loss (TW) | Dominant source |
|------|:-:|:-:|------|
| Earth | ~90 | ~47 | Radiogenic + primordial |
| Moon | ~10–15 | ~0.3 | Primordial (largely cooled) |
| Mars | ~15–25 (estimated) | ~3–5 | Radiogenic + primordial |
| Io | ~2000–3000 | ~$10^{14}$ W | Tidal dissipation |

The Moon and Mars have much lower surface heat flow than Earth, reflecting their smaller sizes (faster cooling through their conductive cooling timescale), the absence of plate tectonics (stagnant lid), and their smaller inventories of heat-producing elements. Io stands out dramatically — its surface heat flux is 20–30 times higher than Earth's, entirely driven by tidal heating.

### Connection to tectonic regime

A planet's surface heat flow is intimately linked to its tectonic regime:
- **Mobile lid (plate tectonics):** Efficient heat loss through subduction and seafloor spreading → high surface heat flux
- **Stagnant lid:** Heat loss limited to conduction through a thick lid plus episodic volcanism → lower surface heat flux
- **Heat-pipe volcanism:** On bodies like early Earth or Io, vigorous volcanism can transport heat by erupting hot magma at the surface, which then cools and is buried by subsequent flows — an alternative to plate tectonics for efficient heat loss {cite}`Turcotte2002`

(tidal-dissipation)=
## Tidal dissipation

We introduced tidal forces in {ref}`lecture02` as a consequence of the gradient in gravitational acceleration across an extended body. Here we explore the consequences: when tidal forces are combined with **orbital eccentricity**, they become a sustained source of internal heating that drives some of the most spectacular geological activity in the solar system.

### How tidal heating works

On a circular orbit, a tidally locked moon maintains a constant distance from its planet, and the tidal bulge points steadily toward the planet — there is no flexing and no heat generation. But if the orbit has even a small **eccentricity**, the distance varies periodically: at periapsis the tidal force is stronger (and the moon moves faster than it rotates), and at apoapsis it is weaker (and the moon rotates faster than it orbits). The result is a continually varying tidal deformation — the body is rhythmically squeezed and stretched every orbit. The energy dissipated in this cyclic deformation is converted to heat.

The tidal heating rate depends on:
- **Orbital eccentricity** $e$ — zero eccentricity means zero tidal heating
- **Orbital distance** $a$ — tidal forces fall off steeply with distance (heating $\propto a^{-6}$ for a given eccentricity)
- **Internal dissipation** — parameterised by the tidal quality factor $Q$ (lower $Q$ means more dissipation per deformation cycle)
- **Body rigidity** — a stiffer body deforms less per cycle but may dissipate more depending on rheology

### Io: the most volcanically active body in the solar system

Jupiter's innermost Galilean moon **Io** (radius 1821 km, similar in size to our Moon) is the most extreme example of tidal heating in the solar system. Despite having no significant radiogenic heat sources at present, Io produces a staggering ~$10^{14}$ W of tidal heat {cite}`Spencer2000` — roughly twice Earth's total heat output, from a body with only 1.2% of Earth's mass.

This was predicted before it was observed. In a landmark 1979 paper, Peale, Cassen, and Reynolds calculated that tidal dissipation in Io, maintained by the **Laplace resonance** with Europa and Ganymede ({ref}`lecture02`), should be sufficient to melt Io's interior {cite}`Peale1979`. Just days after the paper was published, the Voyager 1 spacecraft flew past Io and discovered active volcanic eruptions — a stunning confirmation of theory.

The Laplace resonance is essential: it forces Io's orbital eccentricity to remain at $e \approx 0.004$. Without the resonance, tidal forces would circularise Io's orbit in a few tens of millions of years, and tidal heating would cease. The resonance continuously pumps the eccentricity, maintaining a steady heat source.

The consequences for Io are dramatic:
- Surface heat flux of ~2–3 W m$^{-2}$ — about **30 times** higher than Earth's
- Over 400 active volcanic centres identified
- The entire surface is resurfaced by lava flows on a ~Myr timescale — there are essentially no impact craters
- Internal structure consistent with a partially molten mantle (asthenosphere) {cite}`Keane2023`

```{figure} figures/io_tvashtar_plume.jpg
:name: fig:io-tvashtar
:width: 400px
:align: center

The Tvashtar volcanic plume on Io, captured by the New Horizons spacecraft during its Jupiter flyby in February 2007. The plume rises ~300 km above Io's surface, driven by the eruption of silicate magma heated by tidal dissipation. Io's extreme volcanism is powered entirely by tidal heating from the Laplace resonance with Europa and Ganymede. Credit: NASA/Johns Hopkins University Applied Physics Laboratory/Southwest Research Institute, public domain.
```

### Enceladus: a tiny moon with a big secret

Saturn's small moon **Enceladus** (radius 252 km) provides another dramatic example of tidal heating. In 2005, the Cassini spacecraft discovered jets of water ice and vapour erupting from four parallel fractures — dubbed "tiger stripes" — near the south pole {cite}`Porco2006`. Subsequent measurements showed that these jets carry ~5–15 GW of thermal power {cite}`Howett2011` — far more than can be explained by radioactive decay alone for such a small body.

The heat source is tidal dissipation, driven by Enceladus's 2:1 orbital resonance with the larger moon Dione. The heating is sufficient to maintain a **global subsurface ocean** of liquid water beneath an ice shell ~20–30 km thick. The erupted material from the tiger stripes feeds Saturn's E ring and provides direct samples of the subsurface ocean — analysis by Cassini's instruments revealed the presence of salts, silica nanoparticles (indicating hydrothermal activity on the ocean floor), and even complex organic molecules.

```{figure} figures/enceladus_plumes.jpg
:name: fig:enceladus-plumes
:width: 500px
:align: center

Geysers of water ice erupt from the "tiger stripe" fractures near the south pole of Enceladus, imaged by the Cassini spacecraft. The jets are driven by tidal heating that maintains a subsurface liquid water ocean. The erupted material feeds Saturn's E ring and provides evidence for hydrothermal activity on the ocean floor. Credit: NASA/JPL/Space Science Institute, public domain.
```

### Europa and Titan: subsurface oceans

Tidal heating is also implicated in maintaining subsurface oceans on other outer solar system moons {cite}`NimmoPappalardo2016`:

- **Europa** (Jupiter): The Laplace resonance forces Europa's eccentricity, generating tidal heat (though less than Io's, because Europa is further from Jupiter). Magnetic field measurements by the Galileo spacecraft, combined with gravity data, strongly suggest a global liquid water ocean ~100 km deep beneath an ice shell of ~10–30 km.

- **Titan** (Saturn): Saturn's largest moon shows evidence for a subsurface water ocean from measurements of its rotational state and tidal response by Cassini. Titan's ocean may be maintained by a combination of tidal heating and radiogenic heat in its rocky core.

These "ocean worlds" are among the most promising targets in the search for extraterrestrial life, because they possess liquid water, chemical energy sources (from rock–water interactions at the ocean floor), and the organic building blocks needed for biology. We will return to this topic in {ref}`lecture14`.


## References

```{bibliography}
:filter: docname in docnames
```
