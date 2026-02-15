(lecture07)=
# Lecture 7: Planetary Surfaces — Geology, Geomorphology, & Geophysics

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the major surface processes shaping planetary bodies, derive the crater scaling law from dimensional analysis and apply it to estimate crater sizes, use crater counting to constrain surface ages, and compare tectonic, volcanic, and erosional styles across the solar system.
```

## Surface processes

A planet's surface is its geological record — the integrated result of billions of years of competing processes that create, modify, and destroy landforms. By reading this record, we can reconstruct a body's geological history even without visiting it in person {cite}`Melosh2011`.

Surface processes fall into two broad categories:

- **Endogenic processes** are driven by a body's internal heat ({ref}`lecture03`): volcanism builds new terrain by erupting molten material, and tectonics deforms the crust through faulting and folding. Bodies with more internal heat (larger size, more radioactive elements, stronger tidal heating) show more vigorous endogenic activity.
- **Exogenic processes** are driven by external forces: impact cratering reshapes surfaces through hypervelocity collisions, while erosion (by wind, water, ice, or radiation) gradually wears them down. These processes dominate on bodies with little internal heat.

The relative importance of these processes varies dramatically across the solar system, depending on a body's size, composition, atmosphere, and distance from the Sun:

| Body | Dominant surface process | Key evidence |
|------|:------------------------:|:------------:|
| Moon | Impact cratering | Saturated highland craters, preserved for $>$4 Gyr |
| Earth | Plate tectonics + erosion | Youngest ocean floors $<$200 Myr; rapid weathering |
| Mars | Volcanism + impacts | Olympus Mons, cratered southern highlands |
| Venus | Volcanism | Volcanic plains cover $\sim$80% of surface |
| Io | Tidal volcanism | $\sim$400 active volcanoes, surface age $<$1 Myr |
| Europa | Ice tectonics | Lineae, chaos terrain, very few craters |

```{figure} figures/surface_processes_montage.jpg
:name: fig:surface-processes
:width: 550px
:align: center

The surface of Mars as seen by NASA's *Curiosity* rover, showing aeolian dune deposits sculpted by wind — one of the key exogenic processes shaping planetary surfaces across the solar system. On Mars, wind erosion and deposition dominate the surface today, while ancient volcanism and impacts shaped the deeper geological record. Credit: NASA/JPL-Caltech/MSSS, public domain.
```


## Impact cratering

Impact cratering is the most universal geological process in the solar system. Every solid body bears the scars of hypervelocity collisions, from Mercury's heavily cratered surface to Pluto's ancient terrains. On bodies without atmospheres or active geology (like the Moon), impact craters are preserved for billions of years, making them invaluable tools for dating surfaces {cite}`Melosh2011`.

### Impact mechanics

When a projectile strikes a planetary surface at typical solar system velocities of 10–70 km s$^{-1}$ (set by orbital mechanics; {ref}`lecture02`), the collision releases enormous energy in a fraction of a second. The impact process unfolds in three stages:

1. **Contact and compression:** The projectile makes contact and a shock wave propagates into both the target and the impactor, compressing them to pressures of $\sim$100 GPa (comparable to pressures at Earth's core–mantle boundary). The shock wave converts kinetic energy into internal energy, vaporising and melting material near the impact point.

2. **Excavation:** The shock wave expands hemispherically outward and reflects off the free surface, generating a rarefaction wave that accelerates material upward and outward. A transient cavity forms, with a depth-to-diameter ratio of roughly 1:3. Material is ejected in a cone-shaped curtain, creating the **ejecta blanket**.

3. **Modification:** The transient cavity is gravitationally unstable. In small craters, the walls simply slump inward, producing a bowl-shaped **simple crater**. In larger craters, the floor rebounds upward (forming a **central peak**) and the walls collapse in terraces, producing a **complex crater**.

The kinetic energy of an impactor is:

$$
E_k = \frac{1}{2}mv^2
$$

For a 1 km diameter rocky asteroid ($\rho \approx 3000$ kg m$^{-3}$, $m \approx 1.6 \times 10^{12}$ kg) hitting at 20 km s$^{-1}$:

$$
E_k = \frac{1}{2} \times 1.6 \times 10^{12} \times (2 \times 10^4)^2 \approx 3 \times 10^{20} \text{ J}
$$

This is roughly 100 times the energy of the largest nuclear weapon ever detonated — released in less than a second and concentrated at a single point.


### Blackboard derivation: crater scaling law

```{admonition} Blackboard derivation (~10 min)
:class: tip

**Goal:** Use dimensional analysis to derive how crater diameter $D$ depends on impact energy $E$, target density $\rho$, and surface gravity $g$, then apply the result to estimate the crater produced by a 1 km asteroid impact on the Moon.
```

#### Setup

We want to find the diameter $D$ of the crater (a length) produced by an impact with kinetic energy $E$ into a target with density $\rho$ under surface gravity $g$. In the **gravity regime** (where crater size is limited by gravity rather than material strength — valid for craters larger than $\sim$100 m), dimensional analysis requires:

$$
D = C \, E^a \, \rho^b \, g^c
$$

where $C$ is a dimensionless constant of order unity and $a$, $b$, $c$ are exponents to be determined.

#### Dimensional analysis

Writing the dimensions of each quantity in terms of mass $M$, length $L$, and time $T$:

- $[D] = L$
- $[E] = M L^2 T^{-2}$
- $[\rho] = M L^{-3}$
- $[g] = L T^{-2}$

Requiring $[E^a \rho^b g^c] = L$:

**Mass:** $a + b = 0 \implies b = -a$

**Time:** $-2a - 2c = 0 \implies c = -a$

**Length:** $2a - 3b + c = 1$

Substituting $b = -a$ and $c = -a$:

$$
2a - 3(-a) + (-a) = 1 \implies 2a + 3a - a = 1 \implies 4a = 1 \implies a = \frac{1}{4}
$$

Therefore $a = 1/4$, $b = -1/4$, $c = -1/4$, and:

$$
\boxed{D \sim \left(\frac{E}{\rho g}\right)^{1/4}}
$$ (eq:crater-scaling)

**Dimensional check:** $[E/\rho g] = [M L^2 T^{-2}/(M L^{-3} \cdot L T^{-2})] = [L^4]$. Taking the fourth root gives $[L]$ — the dimensions of length. $\checkmark$

This is the **crater scaling law** in the gravity regime {cite}`Holsapple1993`. It tells us that crater diameter scales as the fourth root of impact energy — doubling the energy increases the crater diameter by only a factor of $2^{1/4} \approx 1.19$ (about 19%). This weak dependence on energy explains why craters have a relatively narrow size range even though impactor energies span many orders of magnitude.

#### Worked example: 1 km asteroid on the Moon

For our 1 km asteroid ($E \approx 3 \times 10^{20}$ J) impacting the Moon ($\rho \approx 2500$ kg m$^{-3}$ for the regolith, $g = 1.62$ m s$^{-2}$):

$$
D \sim \left(\frac{3 \times 10^{20}}{2500 \times 1.62}\right)^{1/4} = \left(7.4 \times 10^{16}\right)^{1/4} \approx 1.65 \times 10^{4} \text{ m} \approx 17 \text{ km}
$$

This is consistent with the observed sizes of lunar craters formed by $\sim$1 km impactors. For comparison, the 85 km crater Tycho was formed by a much larger impactor ($\sim$8 km). The dimensionless prefactor $C$ in the full scaling law depends on target material properties and is of order unity for rocky surfaces.

The more complete **pi-scaling framework** of {cite}`Holsapple1993` parameterises the transition between the gravity regime and the strength regime (where material cohesion, not gravity, limits crater growth) and accounts for target porosity and impactor properties.


### Crater morphology

Craters come in three morphological classes, determined primarily by their diameter relative to the **transition diameter** $D_t$ {cite}`Melosh2011`:

- **Simple craters** ($D \lesssim D_t$): Bowl-shaped depressions with smooth walls and a depth-to-diameter ratio of $\sim$1:5. On the Moon, simple craters have $D \lesssim 15$ km.
- **Complex craters** ($D_t \lesssim D \lesssim 300$ km on the Moon): Feature central peaks (formed by rebound of the crater floor), terraced walls (from gravitational collapse), and flat floors. The transition from simple to complex occurs because gravity overcomes the strength of the crater walls.
- **Multi-ring basins** ($D \gtrsim 300$ km): The largest impacts produce concentric ring structures. Examples include the Orientale basin on the Moon (930 km), Caloris on Mercury (1550 km), and the Hellas basin on Mars (2300 km).

The transition diameter scales inversely with surface gravity:

$$
D_t \approx D_{t,\text{Moon}} \cdot \frac{g_{\text{Moon}}}{g}
$$ (eq:transition-diameter)

where $D_{t,\text{Moon}} \approx 15$ km and $g_{\text{Moon}} = 1.62$ m s$^{-2}$. On Earth ($g = 9.81$ m s$^{-2}$), $D_t \approx 15 \times 1.62/9.81 \approx 2.5$ km — explaining why virtually all terrestrial craters larger than a few kilometres are complex.

```{figure} figures/crater_morphology.jpg
:name: fig:crater-morphology
:width: 450px
:align: center

The boundary between the lunar highlands and Mare Imbrium as imaged by NASA's Lunar Reconnaissance Orbiter (LRO), showing impact craters of various sizes and morphologies. Smaller craters are simple bowl-shaped depressions, while larger craters show more complex features including central peaks and terraced walls. The flat mare surface (lower right) is flooded by basaltic lava flows that buried earlier craters. Credit: NASA/GSFC/Arizona State University, public domain.
```


### Crater counting and surface ages

The key principle of **crater chronology** is simple: older surfaces have had more time to accumulate impact craters, so they have higher crater densities. By counting craters as a function of diameter, we can determine relative ages — and, with calibration, absolute ages {cite}`Neukum2001`.

The **crater size-frequency distribution (SFD)** follows a power law:

$$
N(>D) = a \, D^{-b}
$$ (eq:crater-sfd)

where $N(>D)$ is the cumulative number of craters per unit area with diameter greater than $D$, and $a$ and $b$ are constants. For the production population (before saturation), $b \approx 2$–3, depending on the size range and the impactor population.

The **lunar chronology** provides the critical calibration. Samples returned by the Apollo and Luna missions give radiometric ages for specific lunar surfaces. By counting craters on those same surfaces and measuring their crater density, we establish the relationship between crater density and absolute age. This calibrated lunar chronology can then be extrapolated (with corrections for different impact rates and gravity) to other solar system bodies.

Key results from crater counting include:
- The lunar highlands are **saturated** with craters (crater density has reached an equilibrium where new craters destroy old ones) and are $>$4 Gyr old.
- The lunar maria have ages of 3.9–3.1 Gyr, confirmed by Apollo sample dating.
- Mars's southern highlands are heavily cratered ($\sim$4 Gyr), while the northern lowlands are much younger.
- Venus has a remarkably **uniform** crater density across its entire surface, implying a mean surface age of $\sim$300–700 Myr — suggesting a global resurfacing event (see {ref}`lecture09`).

```{figure} figures/crater_counting.jpg
:name: fig:crater-counting
:width: 450px
:align: center

The lunar farside as imaged by NASA's Lunar Reconnaissance Orbiter, showing a heavily cratered surface. The high crater density of the farside highlands ($>$4 Gyr) contrasts with the smoother nearside maria (3.1–3.9 Gyr), illustrating how crater counting reveals relative and absolute surface ages. Forward references: crater chronology is applied to Mars in {ref}`lecture10`. Credit: NASA/GSFC/Arizona State University, public domain.
```


## Volcanism

Volcanism is the primary mechanism by which a planet's internal heat reaches the surface ({ref}`lecture03`). The style of volcanic activity — whether gentle lava flows or explosive eruptions — depends on the magma composition, volatile content, and the body's gravity and atmospheric pressure {cite}`Melosh2011`.

### Effusive vs. explosive volcanism

The key variable is **magma viscosity**, which is controlled primarily by the $\mathrm{SiO_2}$ (silica) content:

- **Low-viscosity (basaltic) magma** ($\sim$50% $\mathrm{SiO_2}$): Flows easily, producing broad, flat **shield volcanoes** and extensive **flood basalt** plains. Dissolved volatiles ($\mathrm{H_2O}$, $\mathrm{CO_2}$) escape gradually from the fluid magma, so eruptions are typically **effusive** (gentle lava flows). This is the dominant style on the Moon, Mars, and Io.
- **High-viscosity (silicic) magma** ($>$65% $\mathrm{SiO_2}$): Traps dissolved volatiles until the pressure exceeds the magma's strength, producing violent **explosive** eruptions (e.g., Mount St. Helens, Krakatoa). These build steep **stratovolcanoes** and deposit widespread ash layers. Explosive volcanism requires both high-silica magma *and* significant volatile content — conditions met primarily on Earth.

### Volcanic landforms across the solar system

**Olympus Mons (Mars)** is the largest volcano in the solar system: a shield volcano with a base diameter of $\sim$600 km and a height of $\sim$21.9 km above the surrounding terrain (2.5 times the height of Mount Everest above sea level). It grows so large because Mars lacks plate tectonics — the volcanic hotspot remains stationary beneath the lithosphere for billions of years, piling up lava in one location. On Earth, plate motion carries the crust over the hotspot, creating chains of smaller volcanoes (e.g., the Hawaiian Islands) rather than a single massive edifice {cite}`dePaterLissauer2010`.

**Lunar maria** are vast flood basalt plains that fill ancient impact basins on the Moon's nearside. Radiometric dating of Apollo samples shows they erupted between 3.9 and 3.1 Ga, during a period of residual internal heating. The maria cover $\sim$16% of the lunar surface but are visible from Earth as the dark patches that form the "face" of the Moon.

**Venus** is dominated by volcanic landforms: lava plains cover $\sim$80% of the surface, with $>$1600 identified volcanic centres. The uniform crater density suggests that much of the surface was resurfaced in a relatively short interval, possibly through a catastrophic global volcanic episode $\sim$300–700 Myr ago (see {ref}`lecture09`).

**Io** is the most volcanically active body in the solar system, powered by intense tidal heating from its orbital resonance with Europa and Ganymede ({ref}`lecture03`). With $\sim$400 active volcanic centres, Io's surface is continuously resurfaced by lava flows — its mean surface age is estimated at $<$1 Myr, making it one of the youngest surfaces in the solar system {cite}`dePaterLissauer2010`.

```{figure} figures/io_volcanism.jpg
:name: fig:io-volcanism
:width: 500px
:align: center

Jupiter's moon Io as observed across multiple NASA missions spanning decades. Io is the most volcanically active body in the solar system, with $\sim$400 active volcanic centres powered by tidal heating from its orbital resonance with Europa and Ganymede. The colourful surface — yellows, reds, and blacks — is composed of sulfur and silicate lava deposits that are continuously resurfaced, giving Io a mean surface age of $<$1 Myr. Credit: NASA/JPL-Caltech, public domain.
```

| Body | Volcanic style | Driving mechanism | Example landforms |
|------|:--------------:|:-----------------:|:-----------------:|
| Earth | Effusive + explosive | Internal heat + plate recycling | Hawaii, Yellowstone, mid-ocean ridges |
| Moon | Flood basalts (extinct) | Residual heat (3.9–3.1 Ga) | Maria (Imbrium, Serenitatis) |
| Mars | Shield volcanoes (extinct?) | Mantle plumes, no plate motion | Olympus Mons, Tharsis Montes |
| Venus | Lava plains + shield volcanoes | Internal heat, stagnant lid | Maat Mons, pancake domes |
| Io | Ultramafic lava flows (active) | Tidal heating | Loki Patera, Pele |

```{figure} figures/olympus_mons.jpg
:name: fig:olympus-mons
:width: 450px
:align: center

Olympus Mons on Mars, the largest volcano in the solar system, imaged by NASA's Mars Reconnaissance Orbiter. The shield volcano has a base diameter of $\sim$600 km and rises $\sim$21.9 km above the surrounding terrain. The caldera complex at the summit contains multiple nested collapse craters formed by magma withdrawal. Olympus Mons grew to this immense size because Mars lacks plate tectonics — the volcanic source remained fixed beneath the lithosphere for billions of years. Credit: NASA/JPL/University of Arizona, public domain.
```


## Tectonics

Tectonics encompasses the large-scale deformation of a planet's crust and lithosphere, driven by forces arising from internal convection, thermal contraction, tidal stresses, and (on Earth) the motion of lithospheric plates.

### Plate tectonics: Earth's unique regime

Earth is the **only body** in the solar system with active plate tectonics — the lithosphere is divided into $\sim$15 rigid plates that move at velocities of 1–10 cm yr$^{-1}$, driven by mantle convection. Three types of plate boundary exist:

- **Divergent boundaries** (mid-ocean ridges): Plates move apart; new crust is created by seafloor spreading.
- **Convergent boundaries** (subduction zones): One plate descends beneath another into the mantle; associated with volcanism and mountain building.
- **Transform boundaries** (e.g., San Andreas Fault): Plates slide horizontally past each other.

Plate tectonics enables the **carbonate-silicate cycle** ({ref}`lecture06`) by recycling carbon through subduction and volcanic outgassing — a critical component of Earth's long-term climate regulation. Why Earth has plate tectonics while other terrestrial bodies do not remains one of the central open questions in geophysics. Contributing factors likely include Earth's size, water content (which weakens the lithosphere), and the specific rheology of its mantle {cite}`Stern2018`.

```{figure} figures/plate_tectonics.png
:name: fig:plate-tectonics
:width: 600px
:align: center

Earth's major tectonic plates and their boundaries. **Divergent boundaries** (red lines) mark mid-ocean ridges where new crust is created; **convergent boundaries** (blue lines with triangles) mark subduction zones where one plate descends beneath another; **transform boundaries** (green lines) mark where plates slide past each other. Earth is the only known body with active plate tectonics — all other terrestrial planets and moons operate in the stagnant-lid regime. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

### Stagnant-lid convection

All other terrestrial bodies in the solar system operate in the **stagnant-lid regime**: the mantle convects beneath a single, rigid, immobile lithospheric lid. Heat escapes primarily by conduction through the lid and by occasional volcanic eruptions that breach it. The stagnant lid grows thicker over time as the interior cools, eventually shutting down surface volcanism {cite}`Stern2018`.

The stagnant-lid regime is the *default* outcome of mantle convection with strongly temperature-dependent viscosity. At the base of the lithosphere, the viscosity contrast between the cold lid and the hot interior is so large ($\sim$10$^{10}$) that the lid effectively decouples from the convecting mantle below. Earth's plate tectonics requires a mechanism to *break* the lid — likely involving water weakening and self-sustained damage along plate boundaries.

### Tectonic features across the solar system

**Mars** displays dramatic tectonic features despite lacking plate tectonics. The **Tharsis bulge** — a volcanic plateau $\sim$5000 km across and $\sim$10 km high — may have been uplifted by a mantle plume. **Valles Marineris**, the solar system's largest canyon system ($\sim$4000 km long, up to 7 km deep, and 200 km wide), formed by extensional rifting associated with the Tharsis bulge {cite}`dePaterLissauer2010`.

**Venus** shows a puzzling tectonic style. The uniform crater density across the surface implies a mean age of $\sim$300–700 Myr, leading to the **episodic resurfacing hypothesis**: Venus may experience periodic catastrophic overturns where the stagnant lid founders and the entire surface is volcanic resurfaced in a geologically short interval. Between these episodes, the surface remains tectonically quiet. This idea remains debated — we will discuss Venus's geology in detail in {ref}`lecture09`.

**Mercury** has undergone significant **global contraction** as its large iron core cooled and solidified over time, shrinking the planet's radius by $\sim$7 km. This contraction compressed the crust, producing **lobate scarps** — thrust faults up to several hundred kilometres long and 1–3 km high, discovered by Mariner 10 and mapped extensively by MESSENGER. We will discuss Mercury's surface in {ref}`lecture10`.

```{figure} figures/valles_marineris.jpg
:name: fig:valles-marineris
:width: 600px
:align: center

Valles Marineris, the solar system's largest canyon system, stretching $\sim$4000 km across the Martian surface — roughly the distance from Lisbon to Moscow. The canyon is up to 7 km deep and 200 km wide, dwarfing Earth's Grand Canyon. It formed primarily through extensional rifting associated with the Tharsis volcanic bulge, with subsequent widening by mass wasting and possibly fluvial erosion. This Viking Orbiter mosaic shows the full extent of the canyon system. Credit: NASA/JPL/USGS, public domain.
```


## Erosion and weathering

Erosion is the removal and transport of surface material by wind, water, ice, or chemical reactions. On bodies with thick atmospheres, erosion can be the dominant surface-modifying process — Earth's surface is almost entirely shaped by erosion on timescales of millions of years. On airless bodies, the only "erosion" comes from impact gardening and space weathering (see below).

### Aeolian (wind) processes

Wind-driven erosion and deposition require an atmosphere with sufficient density to mobilise surface particles. Active aeolian processes shape the surfaces of {cite}`Catling2017`:

- **Mars:** Extensive dune fields in craters and polar regions. Global dust storms can loft particles to 30 km altitude. Sand dunes in Gale Crater show active migration observed by the Curiosity rover.
- **Titan:** Vast equatorial dune fields composed of organic particles (tholins) produced by atmospheric photochemistry. The dunes are longitudinal, up to 150 m tall and hundreds of kilometres long.
- **Venus:** Despite its dense atmosphere, surface winds are only $\sim$1 m s$^{-1}$ due to the sluggish near-surface dynamics, limiting aeolian activity. However, the thick atmosphere allows even these slow winds to mobilise fine particles.

### Fluvial (water) processes

Liquid water is the most powerful erosive agent on Earth, and evidence for past fluvial activity on Mars is one of the most important discoveries in planetary science:

- **Earth:** Rivers, glacial meltwater, and coastal waves continuously reshape the surface. The Grand Canyon was carved by the Colorado River over $\sim$5–6 Myr.
- **Mars:** **Valley networks** on the Noachian-aged southern highlands ($>$3.7 Ga) resemble terrestrial river drainage systems, implying sustained liquid water flow. **Outflow channels** (e.g., Ares Vallis, Kasei Valles) are enormous flood features, hundreds of kilometres long and tens of kilometres wide, carved by catastrophic releases of groundwater {cite}`Grotzinger2014`. These features are discussed further in {ref}`lecture10`.
- **Titan:** Saturn's largest moon has **methane rivers** that carve channels into its icy surface — the Huygens probe imaged rounded ice pebbles in a dry riverbed during its 2005 landing. Titan's methane hydrological cycle is the only known active fluvial system beyond Earth.

```{figure} figures/mars_valley_networks.jpg
:name: fig:mars-valley-networks
:width: 500px
:align: center

Fluvial channels in Mars's Margaritifer Terra region, imaged by NASA's Mars Reconnaissance Orbiter. These dendritic drainage patterns resemble terrestrial river networks and provide evidence for sustained liquid water flow on early Mars during the Noachian period ($>$3.7 Ga). Such valley networks are concentrated in Mars's ancient southern highlands and are among the strongest geological evidence that the early Martian climate was warmer and wetter than today. Credit: NASA/JPL-Caltech/University of Arizona, public domain.
```

### Glacial processes

Ice can flow slowly under its own weight, carving valleys and transporting debris:

- **Earth:** Glaciers and ice sheets have profoundly shaped mid- and high-latitude landscapes. During the Last Glacial Maximum ($\sim$20 ka), ice sheets covered $\sim$30% of Earth's land area.
- **Mars:** Polar ice caps of $\mathrm{CO_2}$ and $\mathrm{H_2O}$ ice. Mid-latitude features including lobate debris aprons and lineated valley fill strongly resemble terrestrial rock glaciers, suggesting subsurface ice flow.

### Chemical weathering

Chemical reactions between surface rocks and atmospheric or liquid agents alter mineral compositions:

- **Earth:** Silicate weathering by carbonic acid is the critical carbon sink in the carbonate-silicate cycle ({ref}`lecture06`), regulating climate over geological time.
- **Mars:** Orbital spectroscopy (OMEGA on Mars Express, CRISM on MRO) has detected hydrated minerals — phyllosilicates (clays), sulfates, and carbonates — formed by aqueous alteration of basaltic rock, providing mineralogical evidence for past liquid water.
- **Venus:** The high surface temperature ($\sim$735 K) and dense $\mathrm{CO_2}$ atmosphere drive surface–atmosphere chemical reactions that may alter rock compositions on relatively short timescales.


## Remote sensing of surfaces

Most of what we know about planetary surfaces comes from remote sensing — observing from orbit or from Earth. Different wavelengths and measurement techniques reveal different properties of the surface {cite}`dePaterLissauer2010`.

### Reflectance spectroscopy

Every mineral has a characteristic pattern of absorption features in the visible and near-infrared (VIS/NIR, 0.3–5 $\mu$m) caused by electronic transitions and molecular vibrations. By measuring the reflected sunlight spectrum from orbit, we can identify minerals remotely:

- **CRISM** (Compact Reconnaissance Imaging Spectrometer for Mars, on MRO) and **OMEGA** (on Mars Express) have mapped the distribution of phyllosilicates (clays), sulfates, and other hydrated minerals across the Martian surface — providing definitive evidence that liquid water chemically altered the rocks during Mars's early history {cite}`Grotzinger2014`.
- Similar instruments on lunar orbiters have mapped the distribution of pyroxene, olivine, and plagioclase across the Moon's surface.

```{figure} figures/crism_mineral_map.jpg
:name: fig:crism-mineral-map
:width: 600px
:align: center

Six views of the Nili Fossae region on Mars from NASA's CRISM (Compact Reconnaissance Imaging Spectrometer for Mars) instrument on the Mars Reconnaissance Orbiter. Different colour composites highlight different mineral signatures: iron- and magnesium-rich phyllosilicates (clays), olivine, and carbonate minerals are mapped from their characteristic near-infrared absorption features. These minerals formed through aqueous alteration of basaltic rock, providing some of the strongest mineralogical evidence for past liquid water on Mars. Credit: NASA/JPL-Caltech/Johns Hopkins APL, public domain.
```

### Radar imaging (SAR)

Synthetic aperture radar (SAR) transmits microwave pulses and records the reflected signal, producing images independent of illumination or cloud cover:

- **Magellan** (1990–1994) used SAR to map 98% of Venus's surface at $\sim$100 m resolution, penetrating the permanent cloud deck. All our knowledge of Venus's surface geology comes from this mission (see {ref}`lecture09`).
- **Cassini** used SAR to reveal Titan's surface through its opaque organic haze, discovering methane lakes and seas at the poles.

### Laser altimetry

Laser altimeters measure the round-trip travel time of a laser pulse to determine surface elevation with metre-scale vertical precision:

- **MOLA** (Mars Orbiter Laser Altimeter, on Mars Global Surveyor) produced the definitive topographic map of Mars, revealing the $\sim$6 km elevation difference between the southern highlands and northern lowlands (the hemispheric dichotomy), the Tharsis bulge, and the full extent of Valles Marineris {cite}`Smith2001`.
- **LOLA** (Lunar Orbiter Laser Altimeter, on LRO) has mapped the Moon's topography at unprecedented resolution, revealing permanently shadowed craters at the poles that may harbour water ice deposits.

### Gravity field mapping

Precise tracking of spacecraft orbits reveals variations in a body's gravitational field, which reflect lateral density variations in the interior:

- **GRAIL** (Gravity Recovery and Interior Laboratory, 2012) mapped the Moon's gravity field to extraordinary precision, revealing the crustal thickness variations and the structure of impact basins and mascons (mass concentrations).
- **GRACE** (Gravity Recovery and Climate Experiment) performed the same measurement for Earth, revealing ice sheet mass loss, groundwater depletion, and post-glacial rebound.

We will discuss gravity field measurements and their interpretation further in {ref}`lecture08`.

```{figure} figures/mars_topography.jpg
:name: fig:mars-topography
:width: 550px
:align: center

Global topographic map of Mars from the Mars Orbiter Laser Altimeter (MOLA), with colour indicating elevation: blue/green for lowlands, yellow/red for highlands, and white for the highest elevations. The Tharsis bulge with its four giant volcanoes dominates the western hemisphere, Valles Marineris stretches across the equator, and the Hellas impact basin (the deepest point on Mars at $\sim$8.2 km below datum) is visible in the southern hemisphere. The $\sim$6 km elevation difference between the northern lowlands and southern highlands — the **hemispheric dichotomy** — remains one of the major unsolved problems in Martian geology. Credit: NASA/JPL/GSFC, public domain.
```


## Regolith formation and space weathering

On airless bodies (the Moon, Mercury, asteroids), the surface is not bedrock but a loose, fragmented layer called **regolith**, produced by billions of years of impact processing and radiation exposure {cite}`Hapke2001`.

### Regolith

The lunar regolith is a layer of unconsolidated debris — rock fragments, mineral grains, and glass beads — produced by the cumulative effect of impacts at all scales, from micrometeorite bombardment to basin-forming events. This process is called **impact gardening**: each impact excavates material, mixes the surface layer, and breaks rocks into progressively finer particles. The lunar regolith is 5–15 m thick in the maria and potentially deeper in the ancient highlands.

The Hayabusa2 (asteroid Ryugu) and OSIRIS-REx (asteroid Bennu) sample return missions revealed that even small ($\sim$500 m) rubble-pile asteroids have regolith — a surprising finding, since these bodies have negligible gravity and were expected to lose ejecta to space rather than retain it.

```{figure} figures/lunar_regolith.jpg
:name: fig:lunar-regolith
:width: 400px
:align: center

Apollo 11 astronaut Buzz Aldrin on the lunar surface in July 1969. The fine-grained lunar regolith — a 5–15 m thick layer of unconsolidated debris produced by billions of years of meteorite impacts — is visible as the grey surface material. Bootprints and equipment disturbances in the regolith have been preserved essentially unchanged for over 50 years due to the absence of wind or water erosion on the Moon. Credit: NASA/Apollo 11, public domain.
```

### Space weathering

The surfaces of airless bodies are continuously exposed to the space environment: solar wind ions (primarily protons and $\mathrm{He}^{2+}$), micrometeorite impacts, and galactic cosmic rays. These agents collectively produce **space weathering** — a set of physical and chemical changes that modify the optical properties of the surface over time {cite}`Hapke2001`:

- **Solar wind implantation:** Energetic ions are implanted into the top $\sim$100 nm of mineral grains, creating crystal damage and amorphous coatings.
- **Micrometeorite melting:** Tiny impacts at 10–70 km s$^{-1}$ melt and vaporise surface material, creating **nanophase iron** (np-Fe$^0$) particles — metallic iron droplets just 3–30 nm in diameter, embedded in glassy rims on mineral grains.
- **Cosmic ray damage:** High-energy particles create lattice defects in crystal structures.

The net effect is that space-weathered surfaces become **darker and redder** over time. This is why fresh impact craters (e.g., Tycho on the Moon, with its bright ray system) stand out as brighter features against the darker, mature regolith surrounding them. Space weathering complicates the spectroscopic identification of surface minerals, since the absorption features are weakened and shifted — a significant challenge for remote sensing.


## Cryovolcanism on icy bodies

In the outer solar system, where surface temperatures are far below the freezing point of water, volcanic processes take a different form. **Cryovolcanism** involves the eruption of volatile-rich "magma" — liquid water, ammonia–water mixtures, or methane — rather than silicate melts. The energy source is typically tidal heating ({ref}`lecture03`), which can maintain subsurface oceans beneath icy shells.

### Enceladus

Saturn's small moon Enceladus ($R \approx 252$ km) provides the most dramatic example of active cryovolcanism in the solar system. NASA's Cassini spacecraft discovered that Enceladus ejects powerful geysers of water vapour and ice particles from four parallel fractures — the **"tiger stripes"** — near its south pole {cite}`Porco2006`.

The plumes are sourced from a **global subsurface ocean** in contact with the rocky core, maintained by tidal heating from Enceladus's orbital resonance with Dione ({ref}`lecture03`). Cassini's mass spectrometer detected molecular hydrogen ($\mathrm{H_2}$), silica nanoparticles, and complex organic molecules in the plume material — consistent with active hydrothermal vents on the ocean floor, similar to those that support chemosynthetic ecosystems in Earth's deep oceans {cite}`NimmoPappalardo2016`.

The measured thermal emission from the tiger stripes corresponds to a heat flow of $\sim$15 GW {cite}`Howett2011` — far more than can be explained by radiogenic heating alone, confirming the importance of tidal dissipation. Enceladus is one of the most promising targets in the search for extraterrestrial life ({ref}`lecture14`).

### Europa

Jupiter's moon Europa ($R \approx 1561$ km) possesses a **global ocean** $\sim$100 km deep beneath an ice shell $\sim$10–30 km thick, maintained by tidal heating from the Laplace resonance with Io and Ganymede {cite}`NimmoPappalardo2016`. Europa's surface shows:

- **Lineae:** Long linear features, possibly cracks in the ice shell that were filled by upwelling ocean water or warm ice.
- **Chaos terrain:** Regions where the ice appears to have broken up, rotated, and refrozen — possibly formed by localised melting from below.
- **Very few impact craters:** Indicating a geologically young surface ($\sim$40–90 Myr), continuously resurfaced by cryovolcanic and tectonic processes.

Hubble Space Telescope observations have detected possible water vapour plumes above Europa's surface {cite}`Sparks2017`, though these detections are intermittent and less dramatic than Enceladus's persistent geysers. NASA's **Europa Clipper** mission (launched 2024) will perform dozens of close flybys to characterise the ice shell, ocean, and habitability.

### Triton

Neptune's largest moon Triton shows **nitrogen geysers** that were observed by Voyager 2 during its 1989 flyby — plumes of nitrogen gas and dark dust rising $\sim$8 km above the surface before being carried downwind by thin atmospheric currents. Triton's very young surface, retrograde orbit (suggesting it is a captured Kuiper Belt object), and possible subsurface ocean make it an intriguing target for future exploration.

```{figure} figures/enceladus_cryovolcanism.jpg
:name: fig:enceladus-cryovolcanism
:width: 500px
:align: center

Dramatic plumes of water vapour and ice particles erupting from the south polar region of Saturn's moon Enceladus, captured by NASA's *Cassini* spacecraft. The geysers originate from four parallel fractures called "tiger stripes" and are sourced from a global subsurface ocean in contact with the rocky core. The plumes contain molecular hydrogen, silica nanoparticles, and complex organic molecules — ingredients consistent with active hydrothermal chemistry on the ocean floor. Enceladus is one of the most promising targets in the search for life beyond Earth ({ref}`lecture14`). Credit: NASA/JPL-Caltech/SSI, public domain.
```


## References

```{bibliography}
:filter: docname in docnames
```
