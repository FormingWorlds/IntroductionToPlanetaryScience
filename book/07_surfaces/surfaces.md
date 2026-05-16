(lecture07)=
# Planetary Surfaces: Geology, Geomorphology, & Geophysics

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the major surface processes shaping planetary bodies, derive the crater scaling law from dimensional analysis and apply it to estimate crater sizes, use crater counting to constrain surface ages, and compare tectonic, volcanic, and erosional styles across the solar system.
```

```{seealso}
**Slides:** [Download Lecture 7 (PDF)](../_static/slides/lecture07.pdf)
```

## Surface processes

A planet's surface is its geological record: the integrated result of billions of years of competing processes that create, modify, and destroy landforms. By reading this record, we can reconstruct a body's geological history even without visiting it in person {cite:p}`Melosh2011`.

Surface processes fall into two broad categories:

- **Endogenic processes** are driven by a body's internal heat ({ref}`Lecture 3 <lecture03>`): volcanism builds new terrain by erupting molten material, and tectonics deforms the crust through faulting and folding. Bodies with more internal heat (larger size, more radioactive elements, stronger tidal heating) show more vigorous endogenic activity.
- **Exogenic processes** are driven by external forces: impact cratering reshapes surfaces through hypervelocity collisions, while erosion (by wind, water, ice, or radiation) gradually wears them down. These processes dominate on bodies with little internal heat.

The relative importance of these processes varies dramatically across the solar system, depending on a body's size, composition, atmosphere, and distance from the Sun. {numref}`fig:surface-processes` uses Mars as a single-body anchor for the four-way taxonomy (volcanism, tectonics, impacts, erosion) developed in this lecture.

| Body | Dominant surface process | Key evidence |
|------|:------------------------:|:------------:|
| Moon | Impact cratering | Saturated highland craters, preserved for $>$4 Gyr |
| Earth | Plate tectonics + erosion | Youngest ocean floors $<$200 Myr; rapid weathering |
| Mars | Volcanism + impacts | Olympus Mons, cratered southern highlands |
| Venus | Volcanism | Volcanic plains cover $\sim$80% of surface |
| Io | Tidal volcanism | $\sim$300–400 active volcanoes, surface age $<$1 Myr |
| Europa | Ice tectonics | Lineae, chaos terrain, very few craters |

```{figure} figures/surface_processes_montage.avif
:name: fig:surface-processes
:width: 500px
:align: center

Viking Orbiter global colour mosaic of Mars (PIA00407), an orthographic projection of the Valles Marineris hemisphere centred near 20$^\circ$N, 60$^\circ$W. The image is used here as an anchor for the four-way taxonomy of surface processes. Endogenic processes are evident in Valles Marineris, the dark extensional canyon system running west-to-east across the lower middle of the disk, and in the Tharsis shield volcanoes near the western limb (visible as dark patches at left, foreshortened by the limb). Exogenic processes are recorded in the heavily cratered southern highlands and in the bright water-ice north polar cap (top). Mars preserves all four major process classes (volcanism, tectonics, impact cratering, erosion) on a single body and is therefore a useful template for the rest of this lecture. Credit: NASA/JPL/USGS, public domain.
```





## Impact cratering

Impact cratering is the most universal geological process in the solar system. Every solid body bears the scars of hypervelocity collisions, from Mercury's heavily cratered surface to Pluto's ancient terrains. On bodies without atmospheres or active geology (like the Moon), impact craters are preserved for billions of years, making them invaluable tools for dating surfaces {cite:p}`Melosh2011`.

### Impact mechanics

When a projectile strikes a planetary surface at typical solar system velocities of 10–70 km s$^{-1}$ (set by orbital mechanics; {ref}`Lecture 2 <lecture02>`), the collision releases enormous energy in a fraction of a second. The impact process unfolds in three stages:

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

This is roughly $10^3$ times the energy of the largest nuclear weapon ever detonated (Tsar Bomba, $\sim$50 Mt $\approx 2 \times 10^{17}$ J), released in less than a second and concentrated at a single point.


## Blackboard derivation: Crater scaling law

```{admonition} Blackboard derivation: Crater scaling law from dimensional analysis
:class: tip

**Goal:** Use dimensional analysis to derive how crater diameter $D$ depends on impact energy $E$, target density $\rho$, and surface gravity $g$, then apply the result to estimate the crater produced by a 1 km asteroid impact on the Moon.

**Setup.**

We want to find the diameter $D$ of the crater (a length) produced by an impact with kinetic energy $E$ into a target with density $\rho$ under surface gravity $g$. In the **gravity regime** (where crater size is limited by gravity rather than material strength, valid for craters larger than $\sim$100 m), dimensional analysis requires:

$$
D = C \, E^a \, \rho^b \, g^c
$$

where $C$ is a dimensionless constant of order unity and $a$, $b$, $c$ are exponents to be determined.

**Dimensional analysis.**

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

**Dimensional check:** $[E/\rho g] = [M L^2 T^{-2}/(M L^{-3} \cdot L T^{-2})] = [L^4]$. Taking the fourth root gives $[L]$, the dimensions of length. $\checkmark$

This is the **crater scaling law** in the gravity regime {cite:p}`Holsapple1993`. It tells us that crater diameter scales as the fourth root of impact energy: doubling the energy increases the crater diameter by only a factor of $2^{1/4} \approx 1.19$ (about 19%). This weak dependence on energy explains why craters have a relatively narrow size range even though impactor energies span many orders of magnitude.

**Worked example: 1 km asteroid on the Moon.**

For our 1 km asteroid ($E \approx 3 \times 10^{20}$ J) impacting the Moon ($\rho \approx 2500$ kg m$^{-3}$ for the regolith, $g = 1.62$ m s$^{-2}$):

$$
D \sim \left(\frac{3 \times 10^{20}}{2500 \times 1.62}\right)^{1/4} = \left(7.4 \times 10^{16}\right)^{1/4} \approx 1.65 \times 10^{4} \text{ m} \approx 17 \text{ km}
$$

This is consistent with the observed sizes of lunar craters formed by $\sim$1 km impactors. For comparison, the 85 km crater Tycho was formed by a much larger impactor ($\sim$8 km). The dimensionless prefactor $C$ in the full scaling law depends on target material properties and is of order unity for rocky surfaces.

The more complete **pi-scaling framework** of {cite:p}`Holsapple1993` parameterises the transition between the gravity regime and the strength regime (where material cohesion, not gravity, limits crater growth) and accounts for target porosity and impactor properties. The two regimes are illustrated in {numref}`fig:holsapple-piscaling`.
```

```{figure} figures/holsapple1993_strength_gravity_regimes.avif
:name: fig:holsapple-piscaling
:width: 700px
:align: center

The regimes of cratering for a material with strength: cratering efficiency $\pi_V = \rho V/m$ as a function of gravity-scaled size $\pi_2 = g a / U^2$. The three curves correspond to three impact velocities ($U = 2.5$, 10, and 40 km s$^{-1}$). In the **strength regime** (small craters, left), $\pi_V$ depends on the impact velocity $U$ but is essentially independent of $\pi_2$, so the curves separate. For increasing size at fixed velocity, the system transitions to the **gravity regime** (large craters, right) where $\pi_V \propto \pi_2^{-\alpha}$ and the curves converge to a common law. Most laboratory experiments in geological materials are necessarily in the strength regime; planetary-scale craters are firmly in the gravity regime. Reproduced from {cite:p}`Holsapple1993`, Fig. 3.
```


### Crater morphology

Craters come in three morphological classes, determined primarily by their diameter relative to the **transition diameter** $D_t$ {cite:p}`Melosh2011`:

- **Simple craters** ($D \lesssim D_t$): Bowl-shaped depressions with smooth walls and a depth-to-diameter ratio of $\sim$1:5. On the Moon, simple craters have $D \lesssim 15$ km.
- **Complex craters** ($D_t \lesssim D \lesssim 300$ km on the Moon): Feature central peaks (formed by rebound of the crater floor), terraced walls (from gravitational collapse), and flat floors. The transition from simple to complex occurs because gravity overcomes the strength of the crater walls.
- **Multi-ring basins** ($D \gtrsim 300$ km): The largest impacts produce concentric ring structures. Examples include the Orientale basin on the Moon (930 km), Caloris on Mercury (1550 km, {numref}`fig:caloris-basin`), and the Hellas basin on Mars (2300 km).

```{figure} figures/mercury_caloris_basin.avif
:name: fig:caloris-basin
:width: 450px
:align: center

The Caloris basin on Mercury, $\sim$1550 km in diameter, imaged in enhanced colour by NASA's MESSENGER spacecraft. Caloris is one of the largest and best-preserved multi-ring impact basins in the solar system; the orange interior plains are smooth volcanic deposits emplaced after the impact, while the surrounding annulus shows ejecta and concentric ring structures. The basin's antipode on Mercury contains chaotic "weird terrain" thought to have formed from the focused seismic shock of the same event. Credit: NASA/Johns Hopkins APL/Carnegie Institution of Washington, public domain.
```

The transition diameter scales inversely with surface gravity:

$$
D_t \approx D_{t,\text{Moon}} \cdot \frac{g_{\text{Moon}}}{g}
$$ (eq:transition-diameter)

where $D_{t,\text{Moon}} \approx 15$ km and $g_{\text{Moon}} = 1.62$ m s$^{-2}$ {cite:p}`Melosh2011`. On Earth ($g = 9.81$ m s$^{-2}$), this gravity-only scaling gives $D_t \approx 15 \times 1.62/9.81 \approx 2.5$ km; target rock strength shifts the transition between $\sim 2$ km in crystalline rock and $\sim 4$ km in sedimentary targets, but virtually all terrestrial craters larger than a few kilometres are complex. The morphological signature of a complex crater (central peak + terraced walls) is shown in {numref}`fig:crater-morphology`.

```{figure} figures/crater_morphology.avif
:name: fig:crater-morphology
:width: 600px
:align: center

Oblique view of the central peak of Tycho Crater (~85 km diameter), imaged by NASA's Lunar Reconnaissance Orbiter Camera (LROC) in low Sun illumination. The prominent ~2 km tall central peak in the foreground formed by gravitational rebound of the crater floor immediately after the impact, and the surrounding rim shows the terraced walls characteristic of complex craters (visible as stepped scarps in the background). The transition from simple bowl-shaped craters to complex craters with central peaks and terraced walls occurs near $D_t \approx 15$ km on the Moon and scales inversely with surface gravity (Eq. {eq}`eq:transition-diameter`). Credit: NASA/GSFC/Arizona State University, public domain.
```


### Crater counting and surface ages

The key principle of **crater chronology** is simple: older surfaces have had more time to accumulate impact craters, so they have higher crater densities. By counting craters as a function of diameter, we can determine relative ages, and with calibration, absolute ages {cite:p}`Neukum2001`.

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
- Venus has a remarkably **uniform** crater density across its entire surface, implying a mean surface age of $\sim$300–700 Myr, suggesting a global resurfacing event (see {ref}`Lecture 9 <lecture09>`).

The contrast between heavily cratered farside highlands and smoother nearside maria is shown in {numref}`fig:crater-counting`; the calibrated lunar-chronology curve relating cumulative crater density to surface age is shown in {numref}`fig:neukum-chronology`.

```{figure} figures/crater_counting.avif
:name: fig:crater-counting
:width: 450px
:align: center

The lunar farside as imaged by NASA's Lunar Reconnaissance Orbiter, showing a heavily cratered surface. The high crater density of the farside highlands ($>$4 Gyr) contrasts with the smoother nearside maria (3.1–3.9 Gyr), illustrating how crater counting reveals relative and absolute surface ages. Forward references: crater chronology is applied to Mars in {ref}`Lecture 10 <lecture10>`. Credit: NASA/GSFC/Arizona State University, public domain.
```

```{figure} figures/neukum_chronology.avif
:name: fig:neukum-chronology
:width: 600px
:align: center

The lunar crater chronology of {cite:t}`Neukum2001`. The black curve gives the cumulative density of craters with $D \geq 1$ km expected on a surface of model age $T$ (in Gyr); red points mark Apollo and Luna sample sites where radiometric ages of returned basalts and breccias calibrate the curve. The function has two regimes: a roughly linear segment for $T \lesssim 3$ Gyr (steady impact flux) and a steep exponential upturn at $T \gtrsim 3.5$ Gyr that reflects the much higher impact rate during the early bombardment of the inner solar system. Surface ages on other bodies are estimated by counting craters in a chosen size bin and inverting this relation, with corrections for the local impact flux and gravity. Reproduced from {cite:p}`Neukum2001`.
```


## Volcanism

Volcanism is the primary mechanism by which a planet's internal heat reaches the surface ({ref}`Lecture 3 <lecture03>`). The style of volcanic activity (whether gentle lava flows or explosive eruptions) depends on the magma composition, volatile content, and the body's gravity and atmospheric pressure {cite:p}`Melosh2011`.

### Effusive vs. explosive volcanism

The key variable is **magma viscosity**, which is controlled primarily by the $\mathrm{SiO_2}$ (silica) content:

- **Low-viscosity (basaltic) magma** ($\sim$50% $\mathrm{SiO_2}$): Flows easily, producing broad, flat **shield volcanoes** and extensive **flood basalt** plains. Dissolved volatiles ($\mathrm{H_2O}$, $\mathrm{CO_2}$) escape gradually from the fluid magma, so eruptions are typically **effusive** (gentle lava flows). This is the dominant style on the Moon, Mars, and Io.
- **High-viscosity (silicic) magma** ($>$65% $\mathrm{SiO_2}$): Traps dissolved volatiles until the pressure exceeds the magma's strength, producing violent **explosive** eruptions (e.g., Mount St. Helens, Krakatoa). These build steep **stratovolcanoes** and deposit widespread ash layers. Explosive volcanism requires both high-silica magma *and* significant volatile content, conditions met primarily on Earth.

### Volcanic landforms across the solar system

**Olympus Mons (Mars)** is the largest volcano in the solar system: a shield volcano with a base diameter of $\sim$600 km and a summit elevation of $\sim$21.2 km above the Mars datum (2.4 times the height of Mount Everest above sea level). It grows so large because Mars lacks plate tectonics: the volcanic hotspot remains stationary beneath the lithosphere for billions of years, piling up lava in one location. On Earth, plate motion carries the crust over the hotspot, creating chains of smaller volcanoes (e.g., the Hawaiian Islands) rather than a single massive edifice {cite:p}`dePaterLissauer2010`.

**Lunar maria** are vast flood basalt plains that fill ancient impact basins on the Moon's nearside. Radiometric dating of Apollo samples shows they erupted between 3.9 and 3.1 Ga, during a period of residual internal heating. The maria cover $\sim$16% of the lunar surface but are visible from Earth as the dark patches that form the "face" of the Moon.

**Venus** is dominated by volcanic landforms: lava plains cover $\sim$80% of the surface, with $>$1600 identified volcanic centres. The uniform crater density suggests that much of the surface was resurfaced in a relatively short interval, possibly through a catastrophic global volcanic episode $\sim$300–700 Myr ago (see {ref}`Lecture 9 <lecture09>`).

**Io** is the most volcanically active body in the solar system, powered by intense tidal heating from its orbital resonance with Europa and Ganymede ({ref}`Lecture 3 <lecture03>`). With $\sim$300–400 active volcanic centres ({numref}`fig:io-volcanism-surface`), Io's surface is continuously resurfaced by lava flows; its mean surface age is estimated at $<$1 Myr, making it one of the youngest surfaces in the solar system {cite:p}`dePaterLissauer2010,Davies2024PSJ`.

```{figure} figures/io_volcanism.avif
:name: fig:io-volcanism-surface
:width: 500px
:align: center

Full-disk view of Jupiter's moon Io from NASA's Galileo spacecraft (PIA00583), revealing a surface dominated by sulfur and silicate volcanism. Yellow, white, and pale-green regions are sulfur and sulfur-dioxide deposits; darker patches mark recent silicate lava flows and active volcanic centres (a few of which have visible halos of fresh pyroclastic deposits). With $\sim$300–400 active volcanic centres powered by tidal heating in the Laplace resonance with Europa and Ganymede, Io's mean surface age is below 1 Myr {cite:p}`dePaterLissauer2010,Davies2024PSJ`. Credit: NASA/JPL-Caltech/University of Arizona, public domain.
```

| Body | Volcanic style | Driving mechanism | Example landforms |
|------|:--------------:|:-----------------:|:-----------------:|
| Earth | Effusive + explosive | Internal heat + plate recycling | Hawaii, Yellowstone, mid-ocean ridges |
| Moon | Flood basalts (extinct) | Residual heat (3.9–3.1 Ga) | Maria (Imbrium, Serenitatis) |
| Mars | Shield volcanoes (extinct?) | Mantle plumes, no plate motion | Olympus Mons, Tharsis Montes |
| Venus | Lava plains + shield volcanoes | Internal heat, stagnant lid | Maat Mons, pancake domes |
| Io | Ultramafic lava flows (active) | Tidal heating | Loki Patera, Pele |

The size and morphology of Olympus Mons are shown in {numref}`fig:olympus-mons`, with a scale comparison to Earth's largest mountains in {numref}`fig:olympus-comparison`. Venus's volcanically resurfaced surface mapped by Magellan SAR is shown in {numref}`fig:venus-magellan`.

```{figure} figures/olympus_mons.avif
:name: fig:olympus-mons
:width: 450px
:align: center

Olympus Mons on Mars, the largest volcano in the solar system, seen from above in this Viking Orbiter colour mosaic. The shield volcano has a base diameter of $\sim$600 km and a summit elevation of $\sim$21.2 km above the Mars datum. The caldera complex at the summit (centre) contains multiple nested collapse craters formed by episodic magma withdrawal. The steep basal escarpment (up to 6 km high) is visible as the sharp boundary encircling the edifice. Olympus Mons grew to this immense size because Mars lacks plate tectonics: the volcanic source remained fixed beneath the lithosphere for billions of years. Credit: NASA/JPL/USGS, public domain.
```

```{figure} figures/olympus_mons_size_comparison.svg
:name: fig:olympus-comparison
:width: 600px
:align: center

Cross-sectional comparison of Olympus Mons (Mars), Mauna Kea (Hawaii, measured from its base on the ocean floor at $\sim$10.2 km total relief), and Mount Everest (Earth, $\sim$8.85 km above sea level). At $\sim$21.2 km summit elevation above the Mars datum and $\sim$600 km base diameter, Olympus Mons stands roughly twice as tall as Mauna Kea (measured edifice-to-summit) and dwarfs Earth's tallest subaerial mountain. The contrast is set by the absence of plate tectonics on Mars: a stationary mantle plume has continuously fed the same volcanic edifice for billions of years, whereas the Pacific plate carries Hawaiian volcanoes off the underlying hotspot in $\sim$10$^6$ yr, capping their possible size. Vertical scale exaggerated for clarity. Credit: Wikimedia Commons, public domain.
```

```{figure} figures/venus_magellan.avif
:name: fig:venus-magellan
:width: 450px
:align: center

Hemispheric view of Venus from NASA's Magellan radar mission (1990–1994), with colour from Soviet Venera lander surface measurements. Magellan used synthetic aperture radar to penetrate Venus's permanent cloud deck and map 98% of the surface at $\sim$100 m resolution, revealing more than 1600 volcanic centres, extensive lava plains covering $\sim$80% of the surface, and a remarkably uniform crater population implying a global mean surface age of only 300–700 Myr. Venus's surface geology is discussed in detail in {ref}`Lecture 9 <lecture09>`. Credit: NASA/JPL, public domain.
```


## Tectonics

Tectonics encompasses the large-scale deformation of a planet's crust and lithosphere, driven by forces arising from internal convection, thermal contraction, tidal stresses, and (on Earth) the motion of lithospheric plates.

### Plate tectonics: Earth's unique regime

Earth is the **only body** in the solar system with active plate tectonics: the lithosphere is divided into $\sim$15 rigid plates that move at velocities of 1–10 cm yr$^{-1}$, driven by mantle convection. Three types of plate boundary exist:

- **Divergent boundaries** (mid-ocean ridges): Plates move apart; new crust is created by seafloor spreading.
- **Convergent boundaries** (subduction zones): One plate descends beneath another into the mantle; associated with volcanism and mountain building.
- **Transform boundaries** (e.g., San Andreas Fault): Plates slide horizontally past each other.

Plate tectonics enables the **carbonate-silicate cycle** ({ref}`Lecture 6 <lecture06>`) by recycling carbon through subduction and volcanic outgassing, a critical component of Earth's long-term climate regulation. The global plate-boundary network is shown in {numref}`fig:plate-tectonics`. Why Earth has plate tectonics while other terrestrial bodies do not remains one of the central open questions in geophysics. Contributing factors likely include Earth's size, water content (which weakens the lithosphere), and the specific rheology of its mantle {cite:p}`Stern2018`.

```{figure} figures/plate_tectonics.avif
:name: fig:plate-tectonics
:width: 600px
:align: center

Earth's major tectonic plates and their boundaries. **Divergent boundaries** (red lines) mark mid-ocean ridges where new crust is created; **convergent boundaries** (blue lines with triangles) mark subduction zones where one plate descends beneath another; **transform boundaries** (green lines) mark where plates slide past each other. Earth is the only known body with active plate tectonics; all other terrestrial planets and moons operate in the stagnant-lid regime. Credit: Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
```

### Stagnant-lid convection

All other terrestrial bodies in the solar system operate in the **stagnant-lid regime**: the mantle convects beneath a single, rigid, immobile lithospheric lid. Heat escapes primarily by conduction through the lid and by occasional volcanic eruptions that breach it. The stagnant lid grows thicker over time as the interior cools, eventually shutting down surface volcanism {cite:p}`Stern2018`.

The stagnant-lid regime is the *default* outcome of mantle convection with strongly temperature-dependent viscosity. At the base of the lithosphere, the viscosity contrast between the cold lid and the hot interior is large enough (many orders of magnitude) that the lid effectively decouples from the convecting mantle below. Earth's plate tectonics requires a mechanism to *break* the lid, likely involving water weakening and self-sustained damage along plate boundaries.

### Tectonic features across the solar system

**Mars** displays dramatic tectonic features despite lacking plate tectonics. The **Tharsis bulge** (a volcanic plateau $\sim$5000 km across and $\sim$10 km high) may have been uplifted by a mantle plume. **Valles Marineris**, the solar system's largest canyon system ($\sim$4000 km long, up to 7 km deep, and 200 km wide), formed by extensional rifting associated with the Tharsis bulge {cite:p}`dePaterLissauer2010`.

**Venus** shows a puzzling tectonic style. The uniform crater density across the surface implies a mean age of $\sim$300–700 Myr, leading to the **episodic resurfacing hypothesis**: Venus may experience periodic catastrophic overturns where the stagnant lid founders and the entire surface is volcanically resurfaced in a geologically short interval. Between these episodes, the surface remains tectonically quiet. This idea remains debated; we will discuss Venus's geology in detail in {ref}`Lecture 9 <lecture09>`.

**Mercury** has undergone significant **global contraction** as its large iron core cooled and solidified over time, shrinking the planet's radius by up to $\sim$7 km (with method-dependent estimates spanning $\sim$4–7 km) {cite:p}`Byrne2014`. This contraction compressed the crust, producing **lobate scarps** ({numref}`fig:mercury-scarp`), thrust faults up to several hundred kilometres long and 1–3 km high, discovered by Mariner 10 and mapped extensively by MESSENGER. We will discuss Mercury's surface in {ref}`Lecture 10 <lecture10>`.

The Tharsis-related rifting on Mars is recorded in Valles Marineris ({numref}`fig:valles-marineris`).

```{figure} figures/mercury_lobate_scarp.avif
:name: fig:mercury-scarp
:width: 400px
:align: center

A lobate scarp near Pourquoi-Pas crater on Mercury, imaged by the MESSENGER spacecraft. The scarp (running diagonally across the field of view) is the surface expression of a thrust fault formed during global contraction as Mercury's interior cooled and the radius shrank by $\sim$7 km. The scarp clearly cross-cuts and offsets pre-existing impact craters, demonstrating that the contraction continued long after the early bombardment. Credit: NASA/Johns Hopkins APL/Carnegie Institution of Washington, public domain.
```

```{figure} figures/valles_marineris.avif
:name: fig:valles-marineris
:width: 650px
:align: center

Valles Marineris, the solar system's largest canyon system, stretching $\sim$4000 km across the Martian surface (roughly the distance from Lisbon to Moscow). The canyon is up to 7 km deep and 200 km wide, dwarfing Earth's Grand Canyon. It formed primarily through extensional rifting associated with the Tharsis volcanic bulge to the west, with subsequent widening by mass wasting and possibly fluvial erosion. This Viking Orbiter mosaic is a horizontal strip showing the canyon along its full $\sim$2000 km central extent, from the fractured terrain of Noctis Labyrinthus on the west (left) through the main Melas, Candor, and Coprates chasmata, to the chaotic terrain at the canyon's eastern outflow into Chryse Planitia (right); the Tharsis Montes lie off the left edge of the frame. Credit: NASA/JPL/USGS, public domain.
```


## Erosion and weathering

Erosion is the removal and transport of surface material by wind, water, ice, or chemical reactions. On bodies with thick atmospheres, erosion can be the dominant surface-modifying process; Earth's surface is almost entirely shaped by erosion on timescales of millions of years. On airless bodies, the only "erosion" comes from impact gardening and space weathering (see below).

### Aeolian (wind) processes

Wind-driven erosion and deposition require an atmosphere with sufficient density to mobilise surface particles. Active aeolian processes shape the surfaces of {cite:p}`Catling2017`:

- **Mars:** Extensive dune fields in craters and polar regions. Global dust storms can loft particles to 30 km altitude. Sand dunes in Gale Crater show active migration observed by the Curiosity rover.
- **Titan:** Vast equatorial dune fields composed of organic particles (tholins) produced by atmospheric photochemistry. The dunes are longitudinal, up to 150 m tall and hundreds of kilometres long.
- **Venus:** Despite its dense atmosphere, surface winds are only $\sim$1 m s$^{-1}$ due to the sluggish near-surface dynamics, limiting aeolian activity. However, the thick atmosphere allows even these slow winds to mobilise fine particles.

Repeat HiRISE imaging of Martian dune fields from the Mars Reconnaissance Orbiter has shown that these dunes migrate at sand fluxes comparable to those of terrestrial dunes despite Mars's $\sim$170$\times$ thinner atmosphere (Mars surface pressure $\sim$600 Pa vs Earth's $\sim$10$^5$ Pa), overturning the long-held view that Mars dunes are inactive {cite:p}`Bridges2012`. {numref}`fig:mars-dunes` shows an example of a sand sheet streaming through Nili Patera; Titan's massive equatorial dune fields are visible in Cassini SAR imagery ({numref}`fig:titan-dunes`).

```{figure} figures/mars_dunes_bridges.avif
:name: fig:mars-dunes
:width: 600px
:align: center

A streaming sand sheet ("river of sand") within the Nili Patera caldera on Mars, imaged by HiRISE on the Mars Reconnaissance Orbiter. Time-resolved imaging of dune fields like this established that present-day Martian sand fluxes can match terrestrial values despite the thin atmosphere, settling the long-standing debate over whether Mars dunes are presently active {cite:p}`Bridges2012`. Credit: NASA/JPL-Caltech/University of Arizona, public domain.
```

```{figure} figures/titan_dunes.avif
:name: fig:titan-dunes
:width: 600px
:align: center

Cassini Synthetic Aperture Radar (SAR) image of longitudinal dune fields in the Shangri-La region near Titan's equator (PIA20710). The dark, parallel ridges are dunes of organic particles (tholins) that settled out of Titan's atmospheric photochemistry; they reach up to $\sim$150 m in height and stretch hundreds of kilometres along the prevailing winds. Bright patches are topographic high-standing islands of water-ice bedrock that the dune-forming sand flows around. Credit: NASA/JPL-Caltech/ASI, public domain.
```

### Fluvial (water) processes

Liquid water is the most powerful erosive agent on Earth, and evidence for past fluvial activity on Mars is one of the most important discoveries in planetary science:

- **Earth:** Rivers, glacial meltwater, and coastal waves continuously reshape the surface. The Grand Canyon was carved by the Colorado River over $\sim$5–6 Myr.
- **Mars:** **Valley networks** on the Noachian-aged southern highlands resemble terrestrial river drainage systems, implying sustained liquid water flow during the late Noachian to early Hesperian, with localised reactivation continuing into the Amazonian for individual systems such as Warrego Valles {cite:p}`Ansan2006`. **Outflow channels** (e.g., Ares Vallis, Kasei Valles) are enormous flood features, hundreds of kilometres long and tens of kilometres wide, carved by catastrophic releases of groundwater. These features are discussed further in {ref}`Lecture 10 <lecture10>`.
- **Titan:** Saturn's largest moon has **methane rivers** that carve channels into its icy surface. The Huygens probe imaged rounded ice pebbles in a dry riverbed during its 2005 landing ({numref}`fig:titan-huygens`). Titan's methane hydrological cycle is the only known active fluvial system beyond Earth. The two flavours of Martian water-carved features (catastrophic outflow channels and sustained-discharge dendritic valley networks) are shown in {numref}`fig:mars-outflow` and {numref}`fig:mars-valley-networks`.

```{figure} figures/mars_outflow_aram.avif
:name: fig:mars-outflow
:width: 400px
:align: center

A Martian outflow channel cutting through Aram Chaos. The braided streamlined islands and broad scoured trough are the geomorphological signature of catastrophic flood discharges, plausibly fed by sudden release of subsurface ice or groundwater on early Mars. Such channels are tens of kilometres wide and hundreds of kilometres long, dwarfing any terrestrial flood feature, and are distinct from the dendritic valley networks ({numref}`fig:mars-valley-networks`) which formed under more sustained, lower-discharge conditions. Credit: NASA/JPL-Caltech/MSSS, public domain.
```

```{figure} figures/titan_huygens_surface.avif
:name: fig:titan-huygens
:width: 400px
:align: center

Scale composite of three progressively enlarged crops from the post-landing surface image returned by ESA's Huygens probe on 14 January 2005, the only in-situ image ever taken from the surface of an outer-solar-system body. The rounded, decimetre-scale "rocks" in the foreground (bottom panel, shown at their actual apparent size) are blocks of water-ice rounded by methane fluvial transport; the surface is a damp dark plain of methane-soaked organic sediment in a dried-out riverbed. Together with the descent imagery showing dendritic drainage networks, this image confirmed that liquid methane actively shapes Titan's surface today. Credit: ESA/NASA/JPL-Caltech/University of Arizona, public domain.
```

```{figure} figures/mars_valley_networks.avif
:name: fig:mars-valley-networks
:width: 600px
:align: center

Branching valley networks in the Martian highlands imaged by NASA's Viking Orbiter (PIA02810). The dendritic tributary pattern, with multiple stream orders feeding into trunk valleys, closely resembles terrestrial fluvial drainage and is among the strongest geomorphological evidence for sustained surface runoff (and hence precipitation) during the late Noachian to Hesperian on early Mars; for the Warrego Valles type locality, formation continued to $\lesssim$3.0 Ga {cite:p}`Ansan2006`. Such networks are concentrated in the ancient southern highlands and are central to the case that early Mars had a warmer and wetter climate than today. Credit: NASA/JPL/USGS, public domain.
```

### Glacial processes

Ice can flow slowly under its own weight, carving valleys and transporting debris:

- **Earth:** Glaciers and ice sheets have profoundly shaped mid- and high-latitude landscapes. During the Last Glacial Maximum ($\sim$20 ka), ice sheets covered $\sim$30% of Earth's land area.
- **Mars:** Polar ice caps of $\mathrm{CO_2}$ and $\mathrm{H_2O}$ ice. Mid-latitude features including lobate debris aprons and lineated valley fill strongly resemble terrestrial rock glaciers, suggesting subsurface ice flow.

### Chemical weathering

Chemical reactions between surface rocks and atmospheric or liquid agents alter mineral compositions:

- **Earth:** Silicate weathering by carbonic acid is the critical carbon sink in the carbonate-silicate cycle ({ref}`Lecture 6 <lecture06>`), regulating climate over geological time.
- **Mars:** Orbital spectroscopy (OMEGA on Mars Express, CRISM on MRO) has detected hydrated minerals (phyllosilicates or clays, sulfates, and carbonates) formed by aqueous alteration of basaltic rock, providing mineralogical evidence for past liquid water.
- **Venus:** The high surface temperature ($\sim$735 K) and dense $\mathrm{CO_2}$ atmosphere drive surface–atmosphere chemical reactions that may alter rock compositions on relatively short timescales.


## Remote sensing of surfaces

Most of what we know about planetary surfaces comes from remote sensing: observing from orbit or from Earth. Different wavelengths and measurement techniques reveal different properties of the surface {cite:p}`dePaterLissauer2010`.

### Reflectance spectroscopy

Every mineral has a characteristic pattern of absorption features in the visible and near-infrared (VIS/NIR, 0.3–5 $\mu$m) caused by electronic transitions and molecular vibrations. By measuring the reflected sunlight spectrum from orbit, we can identify minerals remotely:

- **CRISM** (Compact Reconnaissance Imaging Spectrometer for Mars, on MRO) and **OMEGA** (on Mars Express) have mapped the distribution of phyllosilicates (clays), sulfates, and other hydrated minerals across the Martian surface, providing definitive evidence that liquid water chemically altered the rocks during Mars's early history ({numref}`fig:crism-mineral-map`) {cite:p}`Ehlmann2008`.
- Similar instruments on lunar orbiters have mapped the distribution of pyroxene, olivine, and plagioclase across the Moon's surface.

```{figure} figures/crism_mineral_map.avif
:name: fig:crism-mineral-map
:width: 600px
:align: center

Two complementary views of carbonate-bearing terrain near Nili Fossae on Mars (PIA19816). (a) Thermal-infrared composite from the THEMIS instrument on Mars Odyssey, showing surface morphology and thermal-inertia variations. (b) Spectral classification map from the CRISM instrument on the Mars Reconnaissance Orbiter, where colour codes indicate the dominant mineralogy: Mg-carbonates (green), olivine-bearing sands (brown/yellow), and basaltic terrain (purple). The carbonates form by aqueous alteration of basaltic crust and provide direct mineralogical evidence for sustained liquid water on early Mars; nearby Mg/Fe-phyllosilicates (clays) detected in the same Nili Fossae region by CRISM further constrain the alteration history {cite:p}`Ehlmann2008`. Credit: NASA/JPL-Caltech/ASU/JHU APL, public domain.
```

### Radar imaging (SAR)

Synthetic aperture radar (SAR) transmits microwave pulses and records the reflected signal, producing images independent of illumination or cloud cover:

- **Magellan** (1990–1994) used SAR to map 98% of Venus's surface at $\sim$100 m resolution, penetrating the permanent cloud deck. All our knowledge of Venus's surface geology comes from this mission (see {ref}`Lecture 9 <lecture09>`).
- **Cassini** used SAR to reveal Titan's surface through its opaque organic haze, discovering methane lakes and seas at the poles.

### Laser altimetry

Laser altimeters measure the round-trip travel time of a laser pulse to determine surface elevation with metre-scale vertical precision:

- **MOLA** (Mars Orbiter Laser Altimeter, on Mars Global Surveyor) produced the definitive topographic map of Mars ({numref}`fig:mars-topography`), revealing the $\sim$6 km elevation difference between the southern highlands and northern lowlands (the hemispheric dichotomy), the Tharsis bulge, and the full extent of Valles Marineris {cite:p}`Smith2001`.
- **LOLA** (Lunar Orbiter Laser Altimeter, on LRO) has mapped the Moon's topography at unprecedented resolution, revealing permanently shadowed craters at the poles that may harbour water ice deposits.

### Gravity field mapping

Precise tracking of spacecraft orbits reveals variations in a body's gravitational field, which reflect lateral density variations in the interior:

- **GRAIL** (Gravity Recovery and Interior Laboratory, 2012) mapped the Moon's gravity field to extraordinary precision, revealing the crustal thickness variations ({numref}`fig:grail-crust`) and the structure of impact basins and mascons (mass concentrations).
- **GRACE** (Gravity Recovery and Climate Experiment) performed the same measurement for Earth, revealing ice sheet mass loss, groundwater depletion, and post-glacial rebound.

We will discuss gravity field measurements and their interpretation further in {ref}`Lecture 8 <lecture08>`.

```{figure} figures/grail_crustal_thickness.avif
:name: fig:grail-crust
:width: 600px
:align: center

Lunar crustal thickness derived from the GRAIL mission, shown for the nearside (left) and farside (right) hemispheres {cite:p}`Wieczorek2013`. GRAIL measured the Moon's gravity field at unprecedented precision by tracking the inter-spacecraft distance between two co-orbiting satellites; combined with topography, the gravity solution yields the depth to the crust-mantle interface. The map reveals an average crustal thickness of $\sim$34-43 km {cite:p}`Wieczorek2013`, with strong thinning beneath the largest impact basins (deep blue), a thicker farside crust, and the Procellarum KREEP Terrane on the nearside (cooler colours within the Procellarum outline). Credit: NASA/MIT/GSFC/JPL-Caltech, public domain.
```

```{figure} figures/mars_topography.avif
:name: fig:mars-topography
:width: 650px
:align: center

Global cylindrical topographic map of Mars from the Mars Orbiter Laser Altimeter (MOLA) on Mars Global Surveyor {cite:p}`Smith2001`. Elevations span $\sim$21 km, from the summit of Olympus Mons (white, left) to the floor of the Hellas basin ($\sim$8 km below datum, deep blue, lower right). The Tharsis bulge and its four shield volcanoes dominate the western hemisphere; Valles Marineris stretches eastward across the equator. The $\sim$6 km elevation difference between the cratered southern highlands and the smooth northern lowlands (the **hemispheric dichotomy**) remains one of the major unsolved problems in Martian geology. Credit: NASA/JPL/GSFC/MOLA Science Team, public domain.
```


## Regolith formation and space weathering

On airless bodies (the Moon, Mercury, asteroids), the surface is not bedrock but a loose, fragmented layer called **regolith**, produced by billions of years of impact processing and radiation exposure {cite:p}`Hapke2001`.

### Regolith

The lunar regolith is a layer of unconsolidated debris (rock fragments, mineral grains, and glass beads) produced by the cumulative effect of impacts at all scales, from micrometeorite bombardment to basin-forming events. This process is called **impact gardening**: each impact excavates material, mixes the surface layer, and breaks rocks into progressively finer particles. The lunar regolith is 5–15 m thick in the maria and potentially deeper in the ancient highlands ({numref}`fig:lunar-regolith`).

The Hayabusa2 (asteroid Ryugu) and OSIRIS-REx (asteroid Bennu) sample return missions revealed that even small ($\sim$500 m) rubble-pile asteroids have regolith, a surprising finding since these bodies have negligible gravity and were expected to lose ejecta to space rather than retain it.

```{figure} figures/lunar_regolith.avif
:name: fig:lunar-regolith
:width: 400px
:align: center

Apollo 11 photograph AS11-40-5878 of an astronaut bootprint in the lunar regolith, taken by Buzz Aldrin during the first crewed lunar EVA on 20 July 1969 as part of an in-situ soil mechanics experiment. The cohesive, fine-grained regolith preserves the boot impression in sharp relief, demonstrating both its low bearing strength and the absence of erosion (no wind, water, or atmosphere). Such bootprints will remain visible on the lunar surface for millions of years. Credit: NASA/Apollo 11, public domain.
```

### Space weathering

The surfaces of airless bodies are continuously exposed to the space environment: solar wind ions (primarily protons and $\mathrm{He}^{2+}$), micrometeorite impacts, and galactic cosmic rays. These agents collectively produce **space weathering**, a set of physical and chemical changes that modify the optical properties of the surface over time {cite:p}`Hapke2001`:

- **Solar wind implantation:** Energetic ions are implanted into the top $\sim$100 nm of mineral grains, creating crystal damage and amorphous coatings.
- **Micrometeorite melting:** Tiny impacts at 10–70 km s$^{-1}$ melt and vaporise surface material, creating **nanophase iron** (np-Fe$^0$) particles: metallic iron droplets ranging from a few nm (single-domain, the FMR carriers) up to several hundred nm (polycrystalline, dominating the optical effects), embedded in glassy rims on mineral grains.
- **Cosmic ray damage:** High-energy particles create lattice defects in crystal structures.

The net effect is that space-weathered surfaces become **darker and redder** over time. This is why fresh impact craters (e.g., Tycho on the Moon, with its bright ray system) stand out as brighter features against the darker, mature regolith surrounding them. Space weathering complicates the spectroscopic identification of surface minerals, since the absorption features are weakened and shifted, a significant challenge for remote sensing.


## Cryovolcanism on icy bodies

In the outer solar system, where surface temperatures are far below the freezing point of water, volcanic processes take a different form. **Cryovolcanism** involves the eruption of volatile-rich "magma" (liquid water, ammonia-water mixtures, or methane) rather than silicate melts. The energy source is typically tidal heating ({ref}`Lecture 3 <lecture03>`), which can maintain subsurface oceans beneath icy shells.

### Enceladus

Saturn's small moon Enceladus ($R \approx 252$ km) provides the most dramatic example of active cryovolcanism in the solar system. NASA's Cassini spacecraft discovered that Enceladus ejects powerful geysers of water vapour and ice particles from four parallel fractures, the **"tiger stripes"**, near its south pole {cite:p}`Porco2006`.

The plumes are sourced from a **global subsurface ocean** in contact with the rocky core, maintained by tidal heating from Enceladus's orbital resonance with Dione ({ref}`Lecture 3 <lecture03>`). Cassini's mass spectrometer detected molecular hydrogen ($\mathrm{H_2}$), silica nanoparticles, and complex organic molecules in the plume material, consistent with active hydrothermal vents on the ocean floor similar to those that support chemosynthetic ecosystems in Earth's deep oceans {cite:p}`NimmoPappalardo2016`.

The measured thermal emission from the tiger stripes corresponds to an endogenic heat flow of $\sim$15.8 GW in the Cassini CIRS analysis of {cite:t}`Howett2011`; the heat flow is far more than can be explained by radiogenic heating alone, confirming the importance of tidal dissipation. Enceladus is one of the most promising targets in the search for extraterrestrial life ({ref}`Lecture 14 <lecture14>`).

### Europa

Jupiter's moon Europa ($R \approx 1561$ km) possesses a **global ocean** $\sim$100 km deep beneath an ice shell $\sim$15–25 km thick, maintained by tidal heating from the Laplace resonance with Io and Ganymede {cite:p}`NimmoPappalardo2016`. Europa's surface shows:

- **Lineae:** Long linear features ({numref}`fig:europa-chaos`), possibly cracks in the ice shell that were filled by upwelling ocean water or warm ice.
- **Chaos terrain:** Regions where the ice appears to have broken up, rotated, and refrozen, possibly formed by localised melting from below.
- **Very few impact craters:** Indicating a geologically young surface ($\sim$40–90 Myr), continuously resurfaced by cryovolcanic and tectonic processes.

Hubble Space Telescope ultraviolet transit observations have reported candidate water vapour plumes above Europa's surface at a $\sim$4.9$\sigma$ level (i.e. statistically marginal at the standard $5\sigma$ discovery threshold) and only on a fraction of observed transits {cite:p}`Sparks2017`; these detections are intermittent and far less dramatic than Enceladus's persistent geysers. NASA's **Europa Clipper** mission (launched 2024) will perform dozens of close flybys to characterise the ice shell, ocean, and habitability.

```{figure} figures/europa_chaos.avif
:name: fig:europa-chaos
:width: 450px
:align: center

Galileo SSI image of Europa's surface near Pwyll crater (the bright ray system at lower right), showing the network of dark double ridges and lineae that crisscross the moon's icy crust. The criss-crossing lineae record successive episodes of fracturing and resurfacing as tidal stresses flexed the brittle ice shell over a $\sim$100 km deep subsurface ocean {cite:p}`NimmoPappalardo2016`. Europa's crater density implies a mean surface age of only 40–90 Myr, making it among the youngest surfaces in the solar system. Credit: NASA/JPL-Caltech/University of Arizona/University of Colorado, public domain.
```

### Triton

Neptune's largest moon Triton shows **nitrogen geysers** that were observed by Voyager 2 during its 1989 flyby: plumes of nitrogen gas and dark dust rising $\sim$8 km above the surface before being carried downwind by thin atmospheric currents ({numref}`fig:triton-surface`). Triton's very young surface, retrograde orbit (suggesting it is a captured Kuiper Belt object), and possible subsurface ocean make it an intriguing target for future exploration. The active plume activity on Enceladus is shown in {numref}`fig:enceladus-cryovolcanism`.

```{figure} figures/triton_voyager.avif
:name: fig:triton-surface
:width: 450px
:align: center

Voyager 2 colour mosaic of Neptune's moon Triton (PIA00317), captured during the 1989 flyby. The pinkish southern polar cap (lower half) is a thin $\mathrm{N_2}$/$\mathrm{CH_4}$ frost; the dark streaks pointing northeast across the cap are wind-deposited dust from active nitrogen geysers, the only confirmed cryovolcanic plumes outside Enceladus. North of the cap, the "cantaloupe terrain" of dimples and ridges is unique in the solar system and remains poorly understood. Triton's retrograde orbit suggests it is a captured Kuiper-belt object, making it a probable analogue for Pluto-class dwarf planets. Credit: NASA/JPL/Voyager 2, public domain.
```

```{figure} figures/enceladus_cryovolcanism.avif
:name: fig:enceladus-cryovolcanism
:width: 500px
:align: center

Dramatic plumes of water vapour and ice particles erupting from the south polar region of Saturn's moon Enceladus, captured by NASA's *Cassini* spacecraft. The geysers originate from four parallel fractures called "tiger stripes" and are sourced from a global subsurface ocean in contact with the rocky core. The plumes contain molecular hydrogen, silica nanoparticles, and complex organic molecules: ingredients consistent with active hydrothermal chemistry on the ocean floor. Enceladus is one of the most promising targets in the search for life beyond Earth ({ref}`Lecture 14 <lecture14>`). Credit: NASA/JPL-Caltech/SSI, public domain.
```


## Recent advances

NASA's Perseverance rover, operating in Jezero crater since 2021, has confirmed that the crater floor is composed of igneous rock (olivine-bearing cumulates) that was subsequently altered by liquid water {cite:p}`Farley2022`. The rover has cached over 20 sample tubes for eventual return to Earth by the Mars Sample Return campaign, a joint NASA/ESA effort that, if successful, would provide the first laboratory analysis of Martian rocks and address questions about past habitability and possible biosignatures ({ref}`Lecture 10 <lecture10>`).

The **DART** (Double Asteroid Redirection Test) mission in 2022 demonstrated the first successful planetary defence experiment: a kinetic impactor deliberately crashed into the asteroid moonlet Dimorphos, shortening its orbital period around the larger asteroid Didymos by $33.0 \pm 1.0$ minutes {cite:p}`Thomas2023`. Companion analyses derived a momentum enhancement factor $\beta \sim 3.6$ from ejecta carrying away momentum well beyond the impactor's own {cite:p}`Cheng2023` and reconstructed the impact site from pre-impact imagery to constrain the mechanical properties of Dimorphos's rubble-pile surface {cite:p}`Daly2023`. Together these results confirmed that kinetic impact is a viable deflection strategy for hazardous near-Earth asteroids.

Ongoing monitoring of Io by the Juno extended mission and ground-based adaptive optics has revealed new details of Io's volcanic activity, including the discovery of previously unknown eruption sites ({numref}`fig:io-nusku`) and constraints on the spatial distribution of heat flow. For Venus, planned radar mapping missions (VERITAS, EnVision) in the early 2030s will provide the first high-resolution surface data since Magellan, enabling tests of whether Venus has experienced recent or ongoing volcanic activity ({ref}`Lecture 9 <lecture09>`).

```{figure} figures/io_nusku_change.avif
:name: fig:io-nusku
:width: 600px
:align: center

JunoCam imagery of the Nusku volcanic region on Io taken two months apart in early 2024 (PIA26488). A new bright red ring of fresh sulfur-rich pyroclastic deposits appears around the central vent in the April image but is absent in February, recording a single eruptive event observed in real time. JunoCam now acquires high-resolution Io flyby data each Juno orbit, providing the first sustained spatial monitoring of Io's volcanism since Galileo. Credit: NASA/JPL-Caltech/SwRI/MSSS/Jason Perry, public domain.
```


## References

```{bibliography}
:filter: docname in docnames
```
