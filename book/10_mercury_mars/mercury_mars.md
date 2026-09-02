(lecture10)=
# Rocky Planets, Mercury & Mars

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to explain Mercury's unusual spin-orbit resonance and metal-rich interior, reconstruct the geological history of Mars across its three main epochs, derive and apply the Jeans escape flux formula, interpret the seismic structure of Mars from {ref}`InSight <lecture08>` data, and use Mercury and Mars as limiting cases that isolate the roles of planet size, distance, and timing in rocky-planet evolution.
```

```{seealso}
**Slides:** [Download Lecture 10 (PDF)](../_static/slides/lecture10.pdf)
```

## Why Mercury and Mars together?

In {ref}`Lecture 9 <lecture09>` we examined Earth and Venus as a near-twin pair with similar mass but divergent surface conditions.
Mercury and Mars represent **limiting cases**.
They are extreme bodies that bracket Earth and Venus in size, heliocentric distance, volatile inventory, and dynamo longevity.
Mercury is the smallest and densest terrestrial planet.
It sits closest to the Sun, stripped of almost all volatiles.
Mars has roughly half the diameter of Earth and sits at the outer edge of the habitable zone.
It preserves a sedimentary and atmospheric record of a wetter, warmer past.

The lecture is divided into three parts.
Part 1 examines Mercury as a metal-world case study, covering orbital dynamics, interior structure, surface morphology, polar volatiles, and the exosphere.
Part 2 focuses on Mars, exploring its interior, geological epochs, evidence for past water, and thermal atmospheric loss via the Jeans escape flux.
Part 3 compares these extremes to show how size, heliocentric distance, and dynamo longevity govern planetary evolution and habitability.

Our understanding of both planets has advanced dramatically over the last fifteen years.
NASA's *MESSENGER* mission explored Mercury between 2011 and 2015, while ESA/JAXA's *BepiColombo* arrives for orbit insertion in 2026.
NASA's *InSight* lander constrained the Martian interior between 2018 and 2021, and *Curiosity* and *Perseverance* continue surface exploration.

## Part 1: Mercury, the metal world

### Mercury overview: the smallest, densest, closest

Mercury is a small planet with mass $0.0553\,\Mearth$, mean radius $0.3829\,\Rearth = 2440\ \mathrm{km}$, and bulk density $5.43\ \mathrm{g\ cm^{-3}}$.
Correcting for internal compression gives an **uncompressed density** (density corrected for internal pressure) of $\sim 5.3\ \mathrm{g\ cm^{-3}}$.
This is the highest value in the solar system, well above Earth's $\sim 4.0\ \mathrm{g\ cm^{-3}}$ {cite:p}`Solomon2018`.
This density requires a much larger iron mass fraction than any other terrestrial planet.
How Mercury acquired so much iron is the **iron-enrichment problem**.

Mercury's orbit is also extreme.
The semi-major axis is $a = 0.387\ \mathrm{AU}$ and the eccentricity $e = 0.2056$, the highest of any planet.
Distance to the Sun varies from $0.307\ \mathrm{AU}$ at perihelion to $0.467\ \mathrm{AU}$ at aphelion.
Solar flux changes by more than a factor of two over a Mercurian year.
This orbital eccentricity and tidal evolution drove the planet into its spin-orbit resonance.
Mercury's near-zero obliquity (about $2$ arcminutes) keeps the rotation axis perpendicular to the orbital plane.
This allows polar ice to survive close to the Sun.

### Orbit and the 3:2 spin-orbit resonance

Mercury rotates once every $58.65$ Earth days and orbits the Sun once every $87.97$ Earth days.
Planetary scientists expected tidal dissipation to produce a $1:1$ synchronous resonance like Earth's Moon.
Instead, 1965 radar observations revealed a $3:2$ **spin-orbit resonance** (a ratio where rotation and orbital frequencies are locked).

Tidal torques act on a planet's **permanent quadrupole moment** (an equatorial bulge) most strongly at perihelion.
In a $3:2$ resonance, this bulge points Sunward at alternate perihelia.
The capture probability during Mercury's orbital evolution is $\sim 55\%$ {cite:p}`CorreiaLaskar2004`.

Let $n_{\mathrm{spin}}$ and $n_{\mathrm{orb}}$ be the spin and mean orbital frequencies.
Expanding the orbit-averaged torque in eccentricity Fourier components yields non-zero torque only when:

$$
\frac{n_{\mathrm{spin}}}{n_{\mathrm{orb}}} \;=\; 1 + \frac{p}{2}\, , \qquad p \in \mathbb{Z}\, .
$$ (eq:spin-orbit-ladder)

The allowed states in {eq}`eq:spin-orbit-ladder` are $1{:}1$ ($p=0$), $3{:}2$ ($p=1$), and $2{:}1$ ($p=2$).
Resonance strength scales as a constant for $1{:}1$, as $e$ for $3{:}2$, and as $e^2$ for $2{:}1$.
With eccentricity $e = 0.206$, the wide $3{:}2$ resonance dominates.
Tidal dissipation cannot despin Mercury to $1{:}1$.

Consequently, a **solar day** (time between local noons) lasts $\sim 176$ Earth days, twice the orbital year.
Longitudes $0^\circ$ and $180^\circ$ face the Sun at alternate perihelia.
These **hot poles** reach peak temperatures of $\sim 700$ K.
Longitudes offset by $90^\circ$ reach perihelion at midnight, reaching peak temperatures of $\sim 570$ K.
This thermal contrast shapes surface temperatures, exospheric sodium emission, and volatile distribution.

```{figure} figures/margot2007_libration.avif
:name: fig:margot-libration
:width: 600px
:align: center

Mercury spin rate deviations from the resonant rate of $3/2$ times the mean orbital frequency, measured by Earth-based radar speckle interferometry. Each data point is one observing epoch with its error bar; the red curve is a numerical integration of the torque equation whose phase is set by the time of pericentre passage. Panel **A** is a one-parameter fit that allows only the $88$-day forced libration, panel **B** a three-parameter fit that adds a $\approx 12$-year free libration component. The fitted forced-libration amplitude, $35.8 \pm 2$ arcseconds, is about twice the value a fully solid Mercury would show, so the mantle must be decoupled from a partially molten core. Reproduced from {cite:t}`Margot2007`, Fig. 3.
```

```{figure} figures/margot2007_libdata.avif
:name: fig:margot-libdata
:width: 600px
:align: center

Histograms of best-fit values for the diagnostic moment-of-inertia ratio $C_m/C$ (where $C_m$ is the moment of inertia of the silicate mantle alone and $C$ is the total moment of inertia, so $C_m/C$ is the fraction of the total moment of inertia contributed by the mantle), drawn from $10^5$ Monte Carlo draws on the measured libration amplitude and the gravity coefficient $C_{22}$. Panel **A** uses the radar measurements alone, panel **B** adds the relation between the gravitational harmonic coefficients and the obliquity that holds in a Cassini state, which tightens the result. Each panel shows two histograms, for the two extremes of the plausible total moment of inertia adopted in 2007: $C/MR^2 = 0.325$ in red and $0.380$ in blue. Radio science with *MESSENGER* has since put $C/MR^2 \approx 0.346$ between those two extremes, and that is the value used in the body text and in the interior structure inversion below. Every distribution peaks near $C_m/C \approx 0.5$, far from the value of unity a fully solid Mercury requires, so the core must be decoupled and at least partly liquid. Reproduced from {cite:t}`Margot2007`, Fig. 4.
```

Mercury's rotation also probes its interior through its **forced libration in longitude**, a periodic wobble over its $88$-day year.
Earth-based radar measurements yielded a libration amplitude of $35.8 \pm 2$ arcseconds ({numref}`fig:margot-libration`) {cite:p}`Margot2007`.
This amplitude is roughly twice the value for a solid planet.
The mantle therefore decouples from a liquid outer core ({numref}`fig:margot-libdata`).

### Interior: a giant iron core

Gravity and libration measurements yield a normalised moment of inertia $C/MR^2 \approx 0.346$ {cite:p}`Margot2007`.
As shown in {ref}`Lecture 8 <lecture08>`, $C/MR^2 < 0.4$ indicates that mass is concentrated toward the centre.
While comparable to Earth's $0.331$, Mercury's value implies a much thinner silicate shell around an unusually large metallic core.
The core radius is approximately $2020\ \mathrm{km}$, $83\%$ of the planet's radius.
The mantle and crust are only $420\ \mathrm{km}$ thick ($17\%$) ({numref}`fig:margot2018-layers`).
By mass, the core represents roughly $74\%$ of Mercury against $32\%$ for Earth.

```{figure} figures/margot2018_mercury_layers.avif
:name: fig:margot2018-layers
:width: 380px
:align: center

Schematic representation of Mercury's internal layering used in modern interior structure models from {cite:t}`MargotHauck2018`. From the centre outward, $R_{\mathrm{ic}}$ is the inner solid core boundary, $R_{\mathrm{oc}}$ separates the liquid outer core from the solid outer shell, $R_{\mathrm{b}}$ marks the optional dense compositional layer at the base of the silicate mantle, and $R_{\mathrm{m}}$ is the crust-mantle boundary. The radially varying densities of the inner and outer core ($\rho_{\mathrm{ic}}(r)$ and $\rho_{\mathrm{oc}}(r)$) capture compression and composition effects with depth.
```

Gravity and libration data are consistent with a liquid outer core surrounding a small solid inner core.
Its existence and size remain debated.
Mercury also possesses an intrinsic dipolar magnetic field aligned with the rotation axis, with about $1\%$ of Earth's surface field strength.
This field is powered by an active **dynamo**, the self-sustaining generation of a magnetic field by convective motion of an electrically conducting fluid.
Sustaining convection after $\sim 4.5$ Gyr of cooling requires that the core has not fully frozen.
Thermal evolution models indicate that light elements such as sulfur, silicon, or carbon depress the freezing point and slow inner-core growth {cite:p}`Wicht2017`.

### Why is Mercury so iron-rich?

Mercury has a core mass fraction of $\sim 74\%$, compared to $32\%$ for Earth and Venus and $24\%$ for Mars {cite:p}`MargotHauck2018`.
Three hypotheses have been proposed:

1. **Selective condensation in the inner solar nebula.** Hot inner-disc temperatures could condense Fe-Ni metal before silicates.
Modern models find no steep gradient at $0.4$ AU.

2. **Vapour and aerosol stripping by the early Sun.** Solar luminosity or stellar winds could evaporate the silicate mantle.
*MESSENGER* data show volatile enrichment (Na, S, K) {cite:p}`Solomon2018` ({numref}`fig:nittler-chemistry`).
This is in tension with the thermal-stripping hypothesis.

```{figure} figures/nittler2020_mercury_chemistry.avif
:name: fig:nittler-chemistry
:width: 480px
:align: center

**(a)** Global maps of Mg/Si (left) and Al/Si (right) elemental ratios on Mercury's surface, derived from four years of *MESSENGER* X-Ray Spectrometer measurements by {cite:t}`Nittler2020`. White contours mark the High-Mg Region (HMR), the Caloris Basin (CB), the Northern Smooth Plains, and the Low-Mg Northern Smooth Plains (LM-NSP). **(b)** A higher-resolution Mg/Si zoom around the Gaudi and Stieglitz craters within the Low-Mg Northern Smooth Plains (LM-NSP), showing that compositional variations exist on small spatial scales as well. Mercury's surface is volatile-element rich and does not match the expectations of a planet that lost its silicate mantle by thermally driven evaporation, undermining the strongest version of the vaporisation-stripping hypothesis for Mercury's iron enrichment.
```

3. **One or more giant impacts.** Late collisions could strip the silicate mantle, leaving a metallic core.
**Smoothed-particle hydrodynamics** simulations (modeling fluids as particles) show impacts reproduce the core fraction {cite:p}`Chau2018`.
However, single impacts occur in well below $1\%$ of dynamical histories ({numref}`fig:franco-mercury`).
This favours multiple impacts {cite:p}`Franco2022`.

```{figure} figures/franco2022_mercury_outcomes.avif
:name: fig:franco-mercury
:width: 700px
:align: center

Final mass distribution of remnant bodies at the end of N-body integrations of inner-solar-system formation, plotted against semi-major axis, for six different surface density profile slopes ($x = 0.5$ to $5.5$). Open circles are larger ($> 0.3\,\Mearth$) bodies, crosses are smaller ones, and solid triangles mark the masses of the actual terrestrial planets in our solar system. Reproducing a Mercury-mass body in the right orbital location with the observed iron enrichment occurs in well below $1\%$ of all trial histories. From {cite:t}`Franco2022`, Fig. A1.
```

We cannot yet decide between these mechanisms.
*BepiColombo* data will test whether volatile abundances match single-impact or multiple-impact scenarios.

### A weak, offset dynamo

Mercury's magnetic dipole is aligned with the rotation axis within $\sim 1^\circ$.
Yet it is offset northward from the geometric centre by $479 \pm 6\ \mathrm{km}$, roughly $20\%$ of the planetary radius {cite:p}`Anderson2012`.
The equatorial surface dipole strength is only $\sim 200\ \mathrm{nT}$ (about $1\%$ of Earth's value), far weaker than a naive extrapolation of the magnetic Reynolds number criterion from {ref}`Lecture 4 <lecture04>` would suggest (the criterion only tells us that a dynamo *can* operate, not how strong its surface field will be).

```{figure} figures/wicht_offset_dipole.avif
:name: fig:wicht-offset
:width: 380px
:align: center

Mollweide maps of the radial magnetic field at the surface of Mercury (top) compared with two of {cite:t}`Wicht2017`'s numerical dynamo models (CW3, middle, and CW4, bottom) that incorporate a thermally stratified outer core layer. The hemispheric asymmetry of the radial field, with positive equatorial flux (yellow/orange) concentrated in the southern hemisphere and weaker, opposite-sign flux in the north (blue), is the surface signature of the dipole that is offset $\sim 480$ km northward of the planetary centre: the southern surface lies closer to the magnetic-pole end of the dipole and therefore samples a stronger field. Models with a stably stratified upper core can reproduce both the weakness and the asymmetry of the observed field.
```

Two mechanisms explain these features: a **thermally stratified outer layer** at the top of the liquid core, in which heat is carried by conduction rather than convection, and a stable inner core boundary that introduces a north-south asymmetry.
Numerical simulations combining these ingredients reproduce both the weakness and offset of the field {cite:p}`Wicht2017` ({numref}`fig:wicht-offset`).

Mercury demonstrates that even small bodies with partially molten cores can sustain long-lived dynamos ({ref}`Lecture 13 <lecture13>`).
Its offset dipole also shows that centered axial dipoles are not universal for rocky planets.

### The surface: ancient cratering, smooth plains, lobate scarps, and hollows

Mercury's heavily cratered surface resembles the lunar highlands.
A thick blanket of **regolith**, the loose layer of fragmented impact debris, covers it.
Global topography ({numref}`fig:mla-global`) reveals distinct features that record the planet's thermal and geological history.

```{figure} figures/messenger_mla_global.avif
:name: fig:mla-global
:width: 700px
:align: center

Global topographic measurement coverage of Mercury from the *MESSENGER* Mercury Laser Altimeter (MLA) projected on a Hammer equal-area map. The northern hemisphere is densely covered by direct laser altimetry; topographic relief on Mercury spans roughly $10\ \mathrm{km}$ from the lowest to highest points measured. Image courtesy NASA/JHUAPL/Carnegie Institution; reproduced from {cite:t}`ZuberMLA2012`.
```

The **smooth plains** are large, lightly cratered volcanic regions that resemble lunar maria.
These flood-basalt provinces were emplaced between $\sim 3.7$ and $\sim 3.9$ billion years ago.
That is near the end of the **late heavy bombardment**, an early period of elevated impact flux.
Large-scale effusive volcanism on Mercury ceased after about $3.5$ Ga {cite:p}`Solomon2018`.

The **lobate scarps** are long, sinuous cliffs produced by thrust faults.
The faults accommodate global contraction as Mercury's interior cooled.
Mapping of these scarps indicates a total radial contraction of $5$ to $7\ \mathrm{km}$ {cite:p}`ByrneTectonics2014`.
Small, unweathered scarps crosscut young craters.
Tectonic contraction is therefore ongoing today {cite:p}`Watters2016`.
Mercury is the only planet besides Earth currently known to host active tectonic deformation.

The **Caloris basin** ($\sim 1550\ \mathrm{km}$ in diameter) is one of the largest impact basins in the solar system.
Its interior is filled by smooth plains and deformed by ridges and **graben**, down-dropped crustal blocks bounded by faults.
Seismic waves from the Caloris impact were focused at the antipodal point to produce jumbled "weird terrain".
The Moon's Imbrium and South Pole-Aitken basins show similar antipodal focusing.

The **hollows** are shallow, flat-floored bright depressions found on crater walls, peaks, and floors {cite:p}`Blewett2011`.
They likely form through the loss of volatile compounds from the upper crust.
Solar heating, micrometeorite gardening, and ion sputtering drive the loss.
Their fresh appearance indicates that hollow formation actively modifies the surface today.

These surface features record early differentiation and heavy cratering, widespread effusive volcanism ending around $3.5$ Ga, sustained global contraction, and ongoing modification by tectonics and volatile loss.

### Polar volatiles: ice on the hottest planet

In 1991, radar observations from the Arecibo and Goldstone telescopes revealed polarisation-inverting echoes inside Mercury's polar craters.
Such echoes are characteristic of water ice.
Between 2011 and 2015, the *MESSENGER* spacecraft confirmed these deposits directly ({numref}`fig:mla-polar`).
Topography from the Mercury Laser Altimeter showed that polar crater floors are **permanently shadowed**.
Because of Mercury's nearly zero obliquity, they never receive direct sunlight {cite:p}`Paige2013`.
The Neutron Spectrometer detected a fast-neutron deficit.
This indicates hydrogen-rich material in the upper $\sim 1\ \mathrm{m}$ of regolith {cite:p}`Lawrence2013`.

```{figure} figures/messenger_mla_polar.avif
:name: fig:mla-polar
:width: 500px
:align: center

Mercury's north polar region in polar projection (latitude $\sim 65^\circ$N to the pole), from {cite:t}`Neumann2013` Fig. 1.
**(A)** MLA topography (colour scale in km above the reference sphere), showing the cratered high-northern-latitude terrain with several impact craters visible along the polar circle.
**(B)** MLA $1064$-nm surface reflectance on the same polar projection (colour scale $0$ to $0.10$). Dark spots (low reflectance, red markers) are located inside permanently shadowed crater floors.
**(C)** Biannual-average insolation at the surface, expressed as a percentage of the 1 AU solar constant. The darkest regions coincide with the low-reflectance spots in panel B: the crater floors receive essentially zero direct sunlight year-round.
**(D)** Biannual maximum illumination temperature, again showing permanently cold regions coinciding with the anomalously dark reflectance in B.
The spatial coincidence of low reflectance, zero insolation, and low temperature is interpreted as evidence that Mercury's permanently shadowed crater floors host **surface-near volatiles**: a thin lag of organic-rich material (responsible for the low 1064-nm reflectance) overlying a **water-ice** deposit. Combined with MESSENGER neutron-spectrometer evidence of hydrogen enrichment at the same craters {cite:p}`Lawrence2013`, this establishes Mercury as a rocky body that retains cold-trapped volatiles despite its proximity to the Sun. From {cite:t}`Neumann2013`.
```

Mercury hosts an estimated $\sim 10^{16}$ to $10^{18}\ \mathrm{g}$ of polar water across $\sim 5\times10^4\ \mathrm{km^2}$ of permanently shadowed terrain {cite:p}`Lawrence2013`.
In a **cold trap**, water molecules delivered by comets, asteroids, or interior dehydration wander via ballistic hops and freeze onto crater floors at $\sim 100\ \mathrm{K}$.
These deposits persist because Mercury's obliquity has stayed close to zero throughout history.
The crater floors stay permanently cold despite intense equatorial solar heating.

### Exosphere and magnetosphere

Mercury has a **surface-bounded exosphere**.
Its column density is so low that gas particles follow ballistic trajectories without colliding before hitting the surface or escaping.
Its composition includes atomic Na, K, Ca, Mg, H, and He.
These atoms are released from the surface by **solar wind sputtering** (energetic ions knocking atoms loose near magnetic cusps), **micrometeorite impact vaporisation** (releasing volatiles from the regolith), **photon-stimulated desorption** by ultraviolet sunlight, and **thermal desorption** of volatile species.

Solar radiation pressure sweeps neutral sodium antisunward into a comet-like **sodium tail** observable from Earth.
Ground-based and *MESSENGER* observations show that this tail varies with orbital phase and solar wind conditions.
This makes it a tracer of space-weather coupling.

Mercury possesses a compact **magnetosphere** (a region dominated by the planetary magnetic field).
Because the intrinsic field is weak and solar wind dynamic pressure is large at $0.4$ AU, the magnetopause standoff distance is only $\sim 1.5\ R_M$ ($R_M = 2440\ \mathrm{km}$), compared to $\sim 10\ R_E$ at Earth.
*MESSENGER* observed reconnection rates ten times higher than at Earth.
Magnetic substorms unfold on timescales of just a few minutes ({numref}`fig:wicht-mag`).

```{figure} figures/wicht_magnetosphere.avif
:name: fig:wicht-mag
:width: 450px
:align: center

Equatorial cross-section of Mercury's compact magnetosphere. The standoff distance is only about $1.5\,R_M$ and the magnetotail is correspondingly short. Reconnection at the dayside magnetopause and in the tail is fast and frequent compared to Earth. Reproduced from {cite:t}`Wicht2017`.
```

### Mission history at Mercury

*Mariner 10* flew past Mercury three times in 1974 and 1975.
Because its orbit was resonant with Mercury, the same hemisphere was illuminated at each encounter.
Only $\sim 45\%$ of the surface was imaged.
The mission discovered Mercury's intrinsic magnetic field and revealed its heavily cratered surface.

The *MESSENGER* mission transformed our understanding of the planet during its orbital phase from 2011 to 2015.
It mapped the entire surface at high resolution, measured global topography and elemental composition, and characterized the magnetic field and exosphere.
*MESSENGER* data established Mercury's offset dipole, polar ice deposits, hollows, global contraction, and unexpectedly high volatile content.

*BepiColombo*, a joint ESA/JAXA mission launched in 2018, will enter orbit in late 2026 {cite:p}`Benkhoff2021`, and it carries two separate spacecraft: the Mercury Planetary Orbiter (MPO) for surface and interior science, and the Mercury Magnetospheric Orbiter (Mio) for magnetospheric science.
Operating two orbiters simultaneously will allow correlated measurements of the magnetosphere and exosphere at different distances.
Key objectives include measuring the moment of inertia to constrain core structure, refining polar ice inventories, and testing origin scenarios through surface volatile abundances.

## Part 2: Mars, the watery past

### Mars overview: half Earth, one tenth the mass

Mars is the second-smallest planet, with a mass of $0.107\,\Mearth$, radius of $0.532\,\Rearth = 3389\ \mathrm{km}$, and mean density of $3.93\ \mathrm{g\ cm^{-3}}$.
The orbit sits near the outer edge of the conservative habitable zone of {ref}`Lecture 13 <lecture13>`.
The semi-major axis is $a = 1.524\ \mathrm{AU}$ and the eccentricity $e = 0.0934$.
The atmosphere is thin ($\sim 6\ \mathrm{mbar}$ surface pressure) and dominated by $\mathrm{CO_2}$.
The global mean surface temperature is near $210\ \mathrm{K}$.
Mars has two small natural satellites, Phobos and Deimos.

Compared to Mercury and Venus, Mars has an Earth-like day length ($24$ h $37$ min) and a current obliquity of $25.19^\circ$ (close to Earth's $23.4^\circ$).
The result is Earth-like seasons.
However, resonance with planetary perturbations causes Martian obliquity to oscillate chaotically on $\sim 100$ Myr timescales between near-zero and over $60^\circ$.
This drives periodic ice ages.
Although cold, dry, and uninhabitable today, early Mars hosted abundant liquid water for at least $\sim 100$ Myr, perhaps episodically for a billion years.
Mars offers the best preserved record of an Earth-like planet losing its atmosphere and drying out.
This makes it an essential target for astrobiology.

### Phobos and Deimos: the twin moons

Because Phobos orbits faster than Mars rotates, tidal torques pull it inward ($1.8\ \mathrm{cm/yr}$) toward disruption within $30$ to $50$ Myr.
Deimos, by contrast, recedes.
Both moons are dark, primitive-looking rubble piles.
Phobos has a low bulk density of $1.89 \pm 0.05\ \mathrm{g\ cm^{-3}}$, which implies high porosity {cite:p}`Kuramoto2022`.

The **captured asteroid** hypothesis matches their primitive spectra.
Capturing circular orbits, however, is dynamically difficult.
The **giant-impact debris** hypothesis produces their orbits from an impact disc ({numref}`fig:hyodo-phobos`) {cite:t}`Hyodo2017`.
However, it predicts a Mars-mantle composition.

```{figure} figures/hyodo2017_phobos_impact.avif
:name: fig:hyodo-phobos
:width: 528px
:align: center

Two snapshots of entropy gain (in $\mathrm{J\,K^{-1}\,kg^{-1}}$) from a smoothed-particle hydrodynamics simulation of a Borealis-scale giant impact onto early Mars by {cite:t}`Hyodo2017`, at $t = 0.17\ \mathrm{h}$ (left, immediately post-impact) and $t = 20\ \mathrm{h}$ (right, after the debris disc has expanded). The impact drives an entropy increase of $\sim 1500\ \mathrm{J\,K^{-1}\,kg^{-1}}$ in the disc material and ejects a circumplanetary disc containing both impactor and Martian-mantle material. Disc fragments collide at $1$--$5\ \mathrm{km\,s^{-1}}$ and grind down to $\sim 100\ \mu$m grains, providing the building blocks from which Phobos and Deimos may subsequently accrete. Two panels selected from the original 4 columns $\times$ 4 rows grid (composition, temperature, entropy, pressure across four times).
```

The **Martian Moons eXploration** (MMX) mission will sample Phobos to test these models ({numref}`fig:mmx-orbit` and {numref}`fig:mmx-timeline`) {cite:p}`Kuramoto2022`.

```{figure} figures/mmx_orbit.avif
:name: fig:mmx-orbit
:width: 480px
:align: center

Planned observation orbits for the JAXA MMX spacecraft around Phobos, drawn in a Phobos-fixed frame with Phobos at the centre, the $xy$ plane taken as the Phobos orbital plane and the $x$ axis pointing away from Mars. **Top:** the five quasi-satellite orbits confined to the $xy$ plane, from QSO-H at about $200\ \mathrm{km}$ along $y$ down to QSO-Lc at a few tens of kilometres; the low orbits support the sampling phase. **Bottom:** one three-dimensional quasi-satellite trajectory, at the QSO-M effective radius and an inclination of $45^\circ$, which carries the spacecraft over the whole surface rather than over the equatorial band alone. Reproduced from {cite:t}`Kuramoto2022`, Fig. 3.
```

```{figure} figures/mmx_timeline.avif
:name: fig:mmx-timeline
:width: 700px
:align: center

Operation plan for MMX during its three-year stay in the Martian system, in five mission phases. Both panels share the same time axis, with the arrival and the departure marked by red triangles on the lower axis. **Top:** eclipse duration for an assumed QSO-L orbit, with eclipses by Mars in orange and by Phobos in blue; N25, S25, and NS0 give the subsolar latitude on Phobos at the Martian solstices and equinoxes, and the arrows mark the landing site selection (LSS), the two touchdowns (TD1, TD2), a science observation block, and the Deimos flyby (DM). The bar below gives the orbit sequence: check out (CO), QSO-H, QSO-M, QSO-H again, QSO-La, QSO-Lb and QSO-Lc together, then the three-dimensional QSO-M (3D-M), with a long Mars observation block in the second half. **Bottom:** the Phobos to Earth distance (purple) and the Sun to Earth to Phobos separation angle (green); the grey bands are the solar conjunctions, when that angle falls to zero and the radio link is interrupted. The dates are those of the 2024 launch baseline, so they shift by about two years for the current launch date. Reproduced from {cite:t}`Kuramoto2022`, Fig. 4.
```

### Mars' interior: the InSight revolution

Before in situ seismology, Mars' interior was constrained by orbital gravity and topography {cite:p}`Smith2001`.
These data yielded crustal thickness maps through **isostatic compensation**, the buoyant equilibrium where low-density crust floats on the mantle.
The moment of inertia $C/MR^2 \approx 0.364$ ({ref}`Lecture 8 <lecture08>`) indicated a smaller relative core than Earth.
Interior layering remained unknown.
In 2018, the InSight lander placed a seismometer on Mars.
It recorded over a thousand marsquakes that probed the deep interior.

```{figure} figures/stahler2021_marsquakes.avif
:name: fig:stahler-quakes
:width: 700px
:align: center

Detection of core-reflected $S$ waves ($ScS$) in InSight marsquake recordings. **Left**: the raw and polarisation-filtered transverse-component velocity for marsquake $S0173a$ (top), together with the polarisation-filtered envelope stack across multiple events (bottom), with the predicted $ScS$ arrival window marked in grey. **Right**: the stacked $ScS$ energy as a function of assumed core-radius offset (in km), with the best-fit and 95% confidence band; the maximum energy near the central value pins the core-mantle boundary at $r_{\mathrm{core}} \approx 1830\ \mathrm{km}$. From {cite:t}`Stahler2021`. The original figure also includes a six-event spectrogram panel and a residual-time panel; only the stack and the energy curve are reproduced here.
```

From core-reflected shear waves ($ScS$), {cite:t}`Stahler2021` measured a core radius of $1830 \pm 40\ \mathrm{km}$ ({numref}`fig:stahler-quakes`).
Reanalyses {cite:p}`Khan2023,Samuel2023` reinterpret this reflection as the top of a $150 \pm 15\ \mathrm{km}$ thick molten silicate layer, revising the metallic core radius to $\sim 1650$ to $1675\ \mathrm{km}$ ({ref}`Lecture 8 <lecture08>`).
Detecting $ScS$ waves indicates a liquid outer core, as fluids do not transmit shear waves, and the core density ($5.7$ to $6.3\ \mathrm{g\ cm^{-3}}$) requires light elements dissolved in the iron.

In a planet of radius $R$, direct shear waves cannot cross the liquid core of radius $r_{\mathrm{core}}$.
The straight-ray limit for a ray grazing the core yields:

$$
\cos\!\left(\frac{\Delta_{\max}}{2}\right) \;=\; \frac{r_{\mathrm{core}}}{R}\, .
$$ (eq:core-shadow)

Setting $r_{\mathrm{core}} = 1830\ \mathrm{km}$ and $R = 3389\ \mathrm{km}$ gives $\Delta_{\max} \approx 115^\circ$.
Quakes beyond $115^\circ$ fall into a shadow zone where only reflected $ScS$ waves reach InSight ({numref}`fig:stahler-schematic`).
{cite:t}`Stahler2021` combined $ScS$ arrival times and the direct-$S$ cutoff to constrain $r_{\mathrm{core}}$ to $\pm 40\ \mathrm{km}$.

```{figure} figures/stahler2021_mars_structure.avif
:name: fig:stahler-schematic
:width: 480px
:align: center

Schematic interior of Mars constrained by InSight seismic observations from {cite:t}`Stahler2021`. The seismic discontinuity at $1830 \pm 40\ \mathrm{km}$ was originally interpreted as the core-mantle boundary marking a low-density, light-element-rich liquid metallic core; the 2023 reanalyses {cite:p}`Khan2023,Samuel2023` reinterpret it as the top of a molten silicate layer ({cite:t}`Khan2023`: $150 \pm 15$ km thick) overlying the metallic core, with the iron-core radius revised down to $\sim$1650–1675 km (see preceding text). $S$ waves reflect off this discontinuity, while $P$ waves transmit through and have been used to bound mantle structure. The $S$-wave shadow zone defines the "core shadow" cast by InSight at its landing site in Elysium Planitia.
```

Seismic velocity inversions indicate a $\sim 500\ \mathrm{km}$ thick lithosphere over a cool upper mantle {cite:p}`Khan2021`.
Crustal thickness beneath InSight is $20 \pm 5\ \mathrm{km}$ or $39 \pm 8\ \mathrm{km}$, depending on which seismic discontinuity marks the base of the crust; the corresponding global mean crustal thickness is $24$ to $38\ \mathrm{km}$ or $39$ to $72\ \mathrm{km}$, in both cases thinner under the northern lowlands and thicker under the southern highlands {cite:p}`Knapmeyer-Endrun2021`.

These observations establish a silicate mantle extending to $\sim 1560\ \mathrm{km}$ depth and a liquid metallic core.
Without a solid inner core to drive compositional convection, Mars lacks a modern dynamo.

The $^{182}\mathrm{Hf}$-$^{182}\mathrm{W}$ chronometer shows that Mars differentiated within $\sim 2$ to $4\ \mathrm{Myr}$ of CAI formation, far faster than Earth's $\sim 30$ to $100\ \mathrm{Myr}$ accretion {cite:p}`Kruijer2017Mars`.
Mars is therefore a **planetary embryo**, a protoplanet that stopped growing before consolidating into a full-sized terrestrial planet, and this rapid formation is consistent with its small core fraction and short-lived dynamo.

```{figure} figures/plesa2022_crustalthickness.avif
:name: fig:plesa-crust
:width: 700px
:align: center

Present-day crustal thickness of Mars in Mollweide projection (colourbar in km, dark blue thin, yellow thick), for three models that all match the gravity and topography data and are all anchored to the three-layer seismic crustal thickness under the InSight landing site (white triangle). Panel **a** is the thin end-member: $31\ \mathrm{km}$ under InSight, a uniform crustal density of $2550\ \mathrm{kg\,m^{-3}}$, and a global mean thickness of $40.6\ \mathrm{km}$. Panel **b** takes $47\ \mathrm{km}$ under InSight with separate densities for the northern lowlands ($3000\ \mathrm{kg\,m^{-3}}$) and the southern highlands ($2600\ \mathrm{kg\,m^{-3}}$), for a mean of $43.1\ \mathrm{km}$. Panel **c** is the thick end-member: $49\ \mathrm{km}$ under InSight, a uniform density of $3000\ \mathrm{kg\,m^{-3}}$, and a mean of $71.4\ \mathrm{km}$. The white and grey contours mark the zero level of MOLA topography. The thickness contrast across the dichotomy boundary is small in **a**, almost absent in **b**, where the density contrast absorbs it, and clear in **c**, so how strong a crustal dichotomy the map shows depends on the assumed density structure. Reproduced from {cite:t}`Plesa2022`, Fig. 1a-c; the heat flow and elastic lithosphere rows of the original are not shown.
```

```{figure} figures/plesa2022_convection.avif
:name: fig:plesa-convection
:width: 700px
:align: center

Cut-away renderings of the present-day mantle convection pattern in three thermal-evolution models of Mars. The dark red sphere is the core, the orange surfaces are the hot upwellings, and the outer shell shows the surface topography. All three models use the same crust, of mean thickness $61.3\ \mathrm{km}$ and density $2800\ \mathrm{kg\,m^{-3}}$, and differ only in core radius: $1500\ \mathrm{km}$ in **a**, $1700\ \mathrm{km}$ in **b**, and $1850\ \mathrm{km}$ in **c**. Only the largest core agrees with the InSight core-radius estimate. The larger the core, the more numerous and the smaller the plumes and downwellings become, which is hard to reconcile with building the crustal dichotomy by mantle convection alone and so favours an impact origin for it. Reproduced from {cite:t}`Plesa2022`, Fig. 10a-c; the mantle temperature-variation slices of the original are not shown.
```

Thermal models indicate that Mars is in a **stagnant-lid regime**, where an immobile lithosphere encloses a slowly convecting mantle and heat escapes by conduction ({numref}`fig:plesa-crust` and {numref}`fig:plesa-convection`) {cite:p}`Plesa2022`.
Radioactive heat-producing elements (uranium, thorium, and potassium) are concentrated in the crust.
The mantle is correspondingly depleted.
This explains why core cooling halted the early dynamo while volcanic activity persisted into the recent past.

Planetary thermal evolution is characterized by the **Urey number**, the ratio of internal radiogenic heat production to total surface heat loss:

$$
\mathrm{Ur} \;\equiv\; \frac{H_{\mathrm{rad}}}{Q_{\mathrm{surf}}}\, .
$$ (eq:urey)

A value $\mathrm{Ur} < 1$ indicates that a planet loses heat faster than it produces it.
It draws on stored primordial energy.
For Mars, the modern radiogenic heat production is $H_{\mathrm{rad}} \sim 2.5 \times 10^{12}\ \mathrm{W}$.
Thermal models {cite:p}`Plesa2022` estimate a global surface heat loss of $Q_{\mathrm{surf}} \approx 20 \times 10^{-3}\ \mathrm{W\,m^{-2}} \times 1.45 \times 10^{14}\ \mathrm{m^2} \approx 3 \times 10^{12}\ \mathrm{W}$.
Evaluating the ratio yields:

$$
\mathrm{Ur}_{\mathrm{Mars}} \;\sim\; \frac{2.5 \times 10^{12}}{3 \times 10^{12}} \;\approx\; 0.8\, ,
$$

With a value below unity, Mars is losing heat slightly faster than radioactive decay deposits it, but its cooling rate is substantially slower than Earth's ($\mathrm{Ur}_\oplus \approx 0.3$ to $0.5$).
This slow secular cooling reflects a stagnant-lid regime where an insulating lithosphere impedes heat loss from the interior.

### Mars' geological epochs: Noachian, Hesperian, Amazonian

Mars is divided into three major geological epochs based on impact crater density {cite:p}`Hartmann2001`, compiled globally by {cite:t}`Tanaka2014` ({numref}`fig:tanaka-global` and {numref}`fig:tanaka-periods`).

```{figure} figures/tanaka2014_geomap.avif
:name: fig:tanaka-global
:width: 800px
:align: center

Global geologic map of Mars from the chronostratigraphic mapping of {cite:t}`Tanaka2014`, in a Robinson projection. Noachian units (red and brown shades) dominate the southern highlands; Hesperian units (greens and blues) cover the northern lowlands and large volcanic provinces; Amazonian units (yellows and tans) include the youngest volcanic and polar deposits. The dichotomy between the heavily cratered south and the smoother north is the dominant first-order feature.
```

```{figure} figures/tanaka2014_periods.avif
:name: fig:tanaka-periods
:width: 700px
:align: center

Correlation chart of Mars map units across the three main epochs from {cite:t}`Tanaka2014`. Columns separate the major terrain categories (lowland, impact, polar, basin, volcanic, apron, transition, highland) and rows correspond to the Amazonian, Hesperian, and Noachian periods (with subdivisions into early, middle, late). The progressive contraction of unit ages from the Noachian to the Amazonian is itself a key constraint on Mars' thermal and atmospheric evolution.
```

The **Noachian** epoch ($\sim 4.1$ to $\sim 3.7$ Ga) is the oldest period, preserved in the heavily cratered southern highlands.
It hosted an active core dynamo.
Most water-related features formed then: valley networks, open-basin lakes, and clay minerals.

The **Hesperian** epoch ($\sim 3.7$ to $\sim 3.0$ Ga) is marked by widespread volcanism and catastrophic outflow channels.
Surface chemistry shifted from clay-forming to sulfate-forming environments as the dynamo shut off and the atmosphere thinned.

The **Amazonian** epoch ($\sim 3.0$ Ga to present) covers two thirds of Mars' history with minimal geological activity.
Surfaces exhibit low crater densities, cold and dry conditions, and sporadic Tharsis volcanism within the last $1$ Gyr.

Across these epochs, surface renewal fell by over an order of magnitude.
Liquid water was concentrated in the Noachian.

### Mars surface highlights: dichotomy, Tharsis, Olympus, Valles

Mars' topography {cite:p}`Smith2001` is dominated by two large-scale geological features.
The first is the **hemispheric dichotomy**, a $\sim 6$-km elevation difference between the cratered southern highlands and the smooth northern lowlands.
While mantle convection can produce degree-1 asymmetry, an exogenic giant impact {cite:p}`AndrewsHanna2008` is the more widely favoured explanation.
The question is not settled.
In this scenario, an early oblique impact excavated the elliptical Borealis basin ($\sim 10\,600 \times 8\,500\ \mathrm{km}$).
This produced the thinner crust of the northern lowlands.

The second feature is **Tharsis**, a continent-sized volcanic province covering roughly a quarter of Mars' surface and standing several kilometres above the datum.
Tharsis hosts the solar system's largest volcanoes, including **Olympus Mons**, a shield volcano rising $\sim 21.3\ \mathrm{km}$ above the datum ($\sim 22\ \mathrm{km}$ above surrounding plains) with a base diameter of roughly $600\ \mathrm{km}$.
Other major edifices include the three Tharsis Montes (Arsia, Pavonis, and Ascraeus, each $14$ to $18\ \mathrm{km}$ tall) and Alba Mons.

These volcanoes grew to enormous sizes for two reasons.
First, without plate tectonics, a stationary mantle plume delivers magma to the same location for hundreds of millions of years, building a single massive structure rather than a chain of separate volcanoes as on Earth.
Second, Mars' lower gravity ($g = 3.71\ \mathrm{m\,s^{-2}}$, $\sim 38\%$ of Earth's) allows the lithosphere to support larger topographic loads before flexing downward.

Enormous lithospheric stresses from Tharsis opened **Valles Marineris**, a canyon system on its eastern flank.
It stretches $\sim 4000\ \mathrm{km}$ along the equator and is up to $200\ \mathrm{km}$ wide and $7\ \mathrm{km}$ deep.
Despite resembling fluvial canyons like the Grand Canyon, Valles Marineris is fundamentally a tectonic rift.
Water erosion and catastrophic flooding later modified some features.
The primary architecture, however, is structural.

Other notable features include **Hellas Planitia**, a $2300$-km-diameter, $\sim 7$-km-deep impact basin.
It is the largest unambiguous impact crater on Mars.
The **polar caps** are layered deposits of permanent water ice overlain by seasonal $\mathrm{CO_2}$ ice.
Finally, **chaotic terrain** at outflow channel heads consists of collapsed surface blocks produced by catastrophic volume loss.

### Evidence for past water

**Valley networks** are branching channels in Noachian highlands formed by precipitation-fed runoff {cite:p}`Hynek2010`.
**Outflow channels** are large scoured features carved during the Hesperian by catastrophic aquifer discharges.

**Clay minerals** (phyllosilicates) formed by aqueous alteration of basalt at near-neutral pH during the Noachian ({numref}`fig:bibring-global`).
{cite:t}`Bibring2006` divided Martian aqueous history into the clay-forming **phyllosian** (neutral pH), sulfate-rich **theiikian** (acidic, evaporative), and dry **siderikian** ({numref}`fig:bibring-timeline`).

```{figure} figures/bibring2006_globalmap.avif
:name: fig:bibring-global
:width: 700px
:align: center

Global map of hydrated minerals on Mars from OMEGA/*Mars Express*. **Top:** detections only, on a black background. **Bottom:** the same detections overlaid on an MGS/MOLA altitude reference map. **Red** points mark phyllosilicate (clay) detections, **blue** points mark sulfate detections, and **yellow** points mark other hydrated minerals whose spectral signatures are not driven by metal-OH vibrations. Clays cluster preferentially in the Noachian southern highlands, consistent with neutral-pH aqueous alteration during the **phyllosian** stage. Sulfates are concentrated at lower-latitude and equatorial sites, consistent with later, drier, more acidic evaporative settings of the **theiikian** stage ({numref}`fig:bibring-timeline`). Reproduced from {cite:t}`Bibring2006`, Fig. 3.
```

```{figure} figures/bibring2006_timeline.avif
:name: fig:bibring-timeline
:width: 550px
:align: center

The three-stage aqueous history of Mars from OMEGA imaging-spectrometer mineralogy: phyllosian (clays, neutral wet), theiikian (sulfates, acidic), and siderikian (anhydrous ferric oxides, dry). The coloured band gives the dominant alteration product of each stage, the row above it the mineralogical era, and the row below the chronostratigraphic Noachian, Hesperian, and Amazonian divisions, whose boundaries are related to but distinct from the mineralogical ones. Two arrows point down into the short cross-hatched interval that separates the clays from the sulfates: a red one labelled *surface volcanic activity* near its start, and a blue one labelled *Mars global change* near its end. The figure therefore places the peak of volcanism and the global change of surface chemistry together, inside that one narrow interval. Reproduced from {cite:t}`Bibring2006`, Fig. 5.
```

**Sulfate deposits** record later acidic and evaporative settings at Meridiani Planum and Gale crater.
**Lakebed sediments** and deltas at Jezero and Gale crater require standing water bodies that persisted for thousands of years {cite:p}`Grotzinger2014`.

```{figure} figures/ehlmann2014_spectra.avif
:name: fig:ehlmann-spectra
:width: 600px
:align: center

Summary of Mars surface compositional spectra from infrared remote sensing and rover instruments, compiled by {cite:t}`EhlmannEdwards2014`. The diversity of spectral classes (basalts, hydrated silicates, sulfates, carbonates, hematite, opaline silica) is evidence for a wide range of aqueous and igneous environments through Mars history.
```

```{figure} figures/ehlmann2014_olivine.avif
:name: fig:ehlmann-olivine
:width: 700px
:align: center

Global distribution of olivine on the Martian surface from TES and OMEGA spectroscopic mapping, projected over a topographic basemap with major regional features labelled (Acidalia, Arabia Terra, Utopia, Tharsis, Terra Meridiani, Isidis, Hellas, Terra Sirenum, Argyre, Elysium). Olivine-rich units (coloured pixels) cluster in the equatorial-to-southern band including impact-exposed terrain around Hellas, Isidis, and Terra Sirenum. Fresh olivine implies limited aqueous alteration, helping identify regions where water was rare or absent. From {cite:t}`EhlmannEdwards2014`.
```

Mineralogical and topographic records ({numref}`fig:ehlmann-spectra` and {numref}`fig:ehlmann-olivine`) indicate a warmer, wetter Noachian between $\sim 3.8$ and $3.6$ Ga.
Conditions were colder and drier thereafter.

### The early Mars climate puzzle

Valley networks indicate surface liquid water on early Mars despite $25\%$ lower solar luminosity at $4$ Ga (the **faint young Sun problem**, the reduced solar output) {cite:p}`Feulner2012`.
Because $\mathrm{CO_2}$ ice clouds raise albedo and cap temperatures below $273\ \mathrm{K}$ {cite:p}`Wordsworth2016`, the "icy highlands" model proposes snow accumulation with episodic melting ({numref}`fig:wordsworth-schematic`).

```{figure} figures/wordsworth2016_schematic.avif
:name: fig:wordsworth-schematic
:width: 700px
:align: center

Schematic of the major climate processes on early Mars in the Noachian and early Hesperian periods, reproduced from Figure 5 of the {cite:t}`Wordsworth2016` AREPS review (Wordsworth's own hand-drawn cartoon). The "icy highlands" picture: snow accumulates in the elevated southern highlands, where adiabatic cooling under a thicker atmosphere makes them effective cold traps; episodic warming from impacts and volcanism delivers transient meltwater that flows downhill into the northern lowlands as standing bodies of water. $\mathrm{CO_2}$ clouds at high altitude can scatter or absorb infrared radiation but in net cool more than they warm.
```

One proposed solution invokes reducing gases such as $\mathrm{H_2}$ or $\mathrm{CH_4}$, supplied by volcanic outgassing or by **serpentinisation** (water-rock reactions altering ultramafic minerals), which warm the surface through **collisionally induced absorption (CIA)** with $\mathrm{CO_2}$, transient absorption during molecular collisions ({numref}`fig:wordsworth-phase`) {cite:p}`Wordsworth2017`.

```{figure} figures/wordsworth2016_phasediagram.avif
:name: fig:wordsworth-phase
:width: 600px
:align: center

Idealised two-dimensional phase diagram for the steady-state climate of early Mars under a denser atmosphere, with steady-state mean surface temperature on the horizontal axis and total surface $\mathrm{H_2O}$ inventory on the vertical axis. The two dividers are drawn at $T_{\mathrm{surf}} \approx 280$ K and at a water inventory of $\approx 200$ m global equivalent layer, so each quadrant is one end-member regime: cold-and-wet (top left, thick highland icesheets with basal melting), warm-and-wet (top right, extreme greenhouse warming required), cold-and-relatively-dry (bottom left, thin highland ice and snow with episodic melting), and warm-and-dry (bottom right, liquid water only in low-lying regions). The schematic cross-section in each quadrant runs from the northern lowlands on the left to the southern highlands on the right and shows the resulting distribution of rock (orange), surface ice (grey), and liquid water (blue). The cold and relatively dry state, combined with episodic melting, fits most of the geological evidence; the cold-and-wet state conflicts with it. Reproduced from {cite:t}`Wordsworth2016`, Fig. 7.
```

Alternatively, **episodic warming** (transient heating from impacts or volcanism) could form valleys on a cold planet {cite:p}`KiteEpisodic2021`.
Fluvial features shifted from Noachian valleys to late Hesperian **alluvial fans** (deposits where channels slow) at mid-latitudes ({numref}`fig:kite-distribution`), indicating a transition from global to seasonal greenhouse warming ({numref}`fig:kite-schematic`) {cite:p}`KiteCarter2022`.

```{figure} figures/kite2022_valley_distribution.avif
:name: fig:kite-distribution
:width: 700px
:align: center

Changing spatial distribution of water-worn landforms on Mars. **Top:** early-stage valley networks, about $3.6$ Ga and older (Late Noachian and Early Hesperian). **Bottom:** late-stage alluvial fans and deltas, $3.5$ to $3$ Ga and perhaps younger (Late Hesperian and Amazonian). Each feature is coloured by its elevation, from $-6$ km (blue) to $+6$ km (yellow). Grey marks the region excluded because the detection probability there is low or zero, and the elevation contours are spaced $3$ km apart. The rover letters are C for *Curiosity* at Gale crater, P for *Perseverance* at Jezero crater, and T-1 for the *Tianwen-1* rover *Zhurong*. Once the detection bias is corrected, the early features favour high ground, while the late ones lie lower and form bands at mid-latitude in both hemispheres. The control therefore passes from elevation to latitude, and that shift is what constrains the change in the greenhouse effect. Reproduced from {cite:t}`KiteCarter2022`, Fig. 1.
```

```{figure} figures/kite2022_schematic.avif
:name: fig:kite-schematic
:width: 700px
:align: center

Graphical summary of the {cite:t}`KiteCarter2022` model for the climate evolution of Mars. **Left:** geographically idealised cross-sections of the two eras, with the early-stage valley networks (blue) cut into the highlands at about $3.6$ Ga, and the late-stage alluvial fans (orange) confined to lower ground at $3.5$ to $3$ Ga; the grey subsurface band is the cryosphere. **Right:** the climate states of the model as a function of $\mathrm{CO_2}$ loss (horizontal, from $1000$ to $10$ mbar) and loss of non-$\mathrm{CO_2}$ warming (vertical, gray-gas column optical depth $\tau$ from $5$ down to $0$), with the present-day state marked at the bottom right. The bands run from warm and wet at the top, through warm lowlands with cold highlands, then cold and wet, to cold and dry at the bottom. The blue outline encloses the states that match the early era and the orange outline those that match the late era. The two can be connected with or without a change in $p\mathrm{CO_2}$, but a decline in non-$\mathrm{CO_2}$ radiative forcing is very probably required. Reproduced from {cite:t}`KiteCarter2022`, Fig. 6.
```

Early Mars climate probably fluctuated on $10^4$ to $10^7$-year timescales before a one-way transition to modern cold, dry conditions.
The balance between sustained warm conditions, episodic warming, and impact-driven hydrology remains debated.

### Modern Mars: thin atmosphere, dust, and methane

Mars today has a $\sim 6\ \mathrm{mbar}$ surface pressure, $95\%$ $\mathrm{CO_2}$, with traces of $\mathrm{N_2}$, $\mathrm{Ar}$, and $\mathrm{O_2}$.
The mean surface temperature is $\sim 210\ \mathrm{K}$ and varies with latitude, season, and time of day.

Suspended **dust** heats the atmosphere by absorbing visible sunlight, driving winds that loft more dust.
This positive feedback occasionally produces **global dust storms** that obscure the surface for weeks to months.
The 2018 storm ended the *Opportunity* rover mission.

In the **seasonal $\mathrm{CO_2}$ cycle**, roughly $25\%$ of the atmospheric mass condenses onto the winter pole and sublimates back in spring.
The polar caps are layered structures of $\mathrm{CO_2}$ ice over permanent water-ice deposits that record past obliquity and orbital cycles.

**Recurring slope lineae (RSL)** are dark streaks that form on steep, sun-facing slopes during warm seasons and fade in winter.
RSL were initially interpreted as briny water flows.
They are now explained by **dry granular flows** triggered by thermal stress or saltation without liquid water.

**Methane** on Mars has a photochemical destruction lifetime of only $\sim 300$ years.
Any detection implies an active source.
The *Curiosity* rover reported background methane of $\sim 0.4$ to $0.7\ \mathrm{ppb}$ with occasional spikes inside Gale crater.
However, the ESA *Trace Gas Orbiter*, launched in 2016, reported global upper limits of $< 0.05\ \mathrm{ppb}$ over the same epochs.
This unresolved discrepancy may reflect localized, transient releases or instrumental effects.

**Dust devils** and other sub-grid meteorological phenomena monitored by *InSight* provide a sustained record of high-frequency atmospheric variability.

## Blackboard derivation: The Jeans escape flux

```{admonition} Blackboard derivation: Jeans escape flux from Mars
:class: tip

**Goal:** Derive the formula for the rate at which thermal energy alone allows molecules to escape from a planetary atmosphere, and apply it to Mars to see why hydrogen is lost on geological timescales but $\mathrm{CO_2}$ essentially is not.

**Setup.**

Consider a thin layer at the **exobase**, the altitude in the atmosphere where the mean free path of a gas molecule becomes comparable to the local atmospheric scale height. Above the exobase, the gas is collisionless: any molecule moving fast enough to escape simply leaves. We assume the gas at the exobase is in local thermal equilibrium at temperature $T = T_{\mathrm{exo}}$.

For a molecule of mass $m$, the **most probable speed** in the Maxwell-Boltzmann distribution is

$$
v_{\mathrm{th}} = \sqrt{\frac{2\,\kB\, T}{m}}\, ,
$$

and the **escape velocity** at the exobase radius $r_{\mathrm{exo}}$ is

$$
v_{\mathrm{esc}} = \sqrt{\frac{2\,G\,M}{r_{\mathrm{exo}}}}\, ,
$$

where $M$ is the planet mass. We define the dimensionless **escape parameter** as the ratio of the gravitational potential energy at the exobase to the thermal energy per molecule:

$$
\lambda \equiv \left(\frac{v_{\mathrm{esc}}}{v_{\mathrm{th}}}\right)^{\!2} = \frac{G\,M\,m}{\kB\,T\,r_{\mathrm{exo}}}\, .
$$ (eq:lambda)

With $v_{\mathrm{th}} = \sqrt{2 \kB T / m}$ (the most-probable thermal speed) and $v_{\mathrm{esc}}^2 = 2 G M / r_{\mathrm{exo}}$, the algebra collapses cleanly to the right-hand side. A molecule with kinetic energy comparable to $\kB T$ is gravitationally bound when $\lambda \gg 1$ and free to escape when $\lambda \lesssim 1$.

**The integration.**

The Maxwell-Boltzmann distribution gives the number density of molecules with speed between $v$ and $v + \dd v$ as

$$
f(v)\,\dd v = n\,\left(\frac{m}{2\pi \kB T}\right)^{\!3/2}\,4\pi v^2 \exp\left(-\frac{m v^2}{2\kB T}\right)\,\dd v\, ,
$$

where $n$ is the total number density at the exobase. The number flux of molecules crossing an upward-facing imaginary surface from below, with vertical component of velocity $v_z > 0$, is

$$
\Phi = \int_{\mathrm{upward}} v_z\, f(\mathbf{v})\,\dd^3 v\, .
$$

For molecules to escape, we need $v_z$ such that the speed $v \geq v_{\mathrm{esc}}$. Using spherical coordinates in velocity space and integrating over the upper hemisphere of directions, the calculation reduces to a one-dimensional integral over speed, with an extra factor of $1/4$ from the average over directions:

$$
\Phi_J = n\,\langle v\rangle\,\frac{1}{4}\,(1+\lambda)\,e^{-\lambda}\, .
$$

Here $\langle v\rangle = \sqrt{8\kB T / (\pi m)}$ is the mean speed of the Maxwell-Boltzmann distribution. Substituting and simplifying:

$$
\boxed{\,\Phi_J \;=\; n\,\sqrt{\frac{\kB T}{2\pi m}}\,(1+\lambda)\,e^{-\lambda}\,}
$$ (eq:jeans)

This is the **Jeans escape flux**, named after James Jeans who derived it in 1925. It is the foundational formula of atmospheric escape theory.

**Checking the limits.**

When $\lambda \to 0$ (the planet's gravity is irrelevant), the factor $(1+\lambda)e^{-\lambda} \to 1$ and the formula reduces to $n\sqrt{\kB T/(2\pi m)}$, which is exactly one quarter of $n\langle v\rangle$, the standard kinetic-theory result for the flux of molecules through an aperture in a gas. So the formula behaves correctly in the no-gravity limit.

When $\lambda \gg 1$, the exponential dominates and the flux falls off as $e^{-\lambda}$. The dependence on $\lambda$ is steep: a change in $\lambda$ from $5$ to $10$ reduces the escape flux by a factor of $\sim 80$ (the ratio $(1+\lambda_1)e^{-\lambda_1}/[(1+\lambda_2)e^{-\lambda_2}]$ for $\lambda_1 = 5$, $\lambda_2 = 10$ gives $(6/11)\,e^{5} \approx 81$).

**Application to Mars.**

For Mars: $M = 6.4\times 10^{23}\ \mathrm{kg}$, $r_{\mathrm{exo}} \approx R_{\mathrm{Mars}} + 200\ \mathrm{km} \approx 3.6\times 10^6\ \mathrm{m}$, $T_{\mathrm{exo}} \approx 270\ \mathrm{K}$ (modern; somewhat higher under solar storms). The escape velocity at the exobase is

$$
v_{\mathrm{esc}} = \sqrt{\frac{2\,(6.67\times 10^{-11})\,(6.4\times 10^{23})}{3.6\times 10^6}} \approx 4.9\ \mathrm{km/s}\, .
$$

For atomic hydrogen, $m = 1.67 \times 10^{-27}\ \mathrm{kg}$ and

$$
\lambda_H = \frac{G M m}{\kB T r_{\mathrm{exo}}} \approx \frac{(6.67 \times 10^{-11})(6.4 \times 10^{23})(1.67 \times 10^{-27})}{(1.38 \times 10^{-23})(270)(3.6 \times 10^6)} \approx 5.3\, .
$$

So $e^{-\lambda_H} \approx 5 \times 10^{-3}$, modest but significant. The most-probable thermal speed of atomic hydrogen at $270$ K is $v_{\mathrm{th}}^H = \sqrt{2 \kB T / m_H} \approx 2.1$ km/s, roughly $40\%$ of $v_{\mathrm{esc}}$, so a non-negligible fraction of the high-velocity tail of the Maxwell-Boltzmann distribution exceeds escape velocity. Hydrogen can escape Mars' atmosphere by Jeans escape, and over geological timescales the cumulative loss is enormous.

For molecular hydrogen ($\mathrm{H_2}$, $m = 2$ amu) the escape parameter doubles: $\lambda_{H_2} \approx 10$, $e^{-\lambda} \approx 5 \times 10^{-5}$. Still escaping, but more slowly than atomic H.

For $\mathrm{CO_2}$, with molecular mass $44$ amu, the escape parameter is

$$
\lambda_{CO_2} = \frac{m_{CO_2}}{m_H}\,\lambda_H = 44 \times 5.3 \approx 230\, .
$$

The exponential is then $e^{-230} \approx 10^{-100}$, which is *zero* for any practical purpose. **Mars cannot lose $\mathrm{CO_2}$ by Jeans escape on any reasonable timescale.** The same applies to nitrogen ($\lambda \approx 150$, $e^{-\lambda} \sim 10^{-65}$), oxygen ($\lambda \approx 170$), and water vapour ($\lambda \approx 95$, although $\mathrm{H_2O}$ is photolysed in the upper atmosphere and lost as H plus O via different channels).

**Lesson.**

Jeans escape is selective. Light species (H, He, $\mathrm{H_2}$, possibly $\mathrm{D}$) are stripped by thermal escape on Gyr timescales; heavy species (C, N, O, Ar, $\mathrm{CO_2}$) are essentially immune. If Mars has lost a substantial inventory of $\mathrm{CO_2}$ over its history, the loss must have happened by **non-thermal** processes that bypass the Maxwell-Boltzmann velocity distribution entirely. We turn to those processes next.
```

A few comments on the derivation.
The factor $(1+\lambda)$ in equation {eq}`eq:jeans` reflects the fact that the escaping molecules carry away their kinetic energy (the raw Maxwellian tail) together with the work done against gravity as they climb out.
This biases the escaping population toward higher initial velocities.
In the limit $\lambda \to \infty$ the formula reduces to $\Phi_J \sim n\,v_{\mathrm{th}}\,\lambda\,e^{-\lambda}$, the standard high-$\lambda$ asymptotic form often quoted in textbooks.
Note that the "$\sim$" hides a numerical prefactor.
Written exactly, $(1+\lambda)e^{-\lambda} \to \lambda e^{-\lambda}$ for $\lambda \gg 1$, and $\sqrt{\kB T/(2\pi m)} = v_{\mathrm{th}}/(2\sqrt{\pi})$ with $v_{\mathrm{th}}$ the most-probable speed defined above, so the textbook scaling carries an implicit $1/(2\sqrt{\pi})$ that we have absorbed into the proportionality.

The exobase concept is crucial.
Collisions below the exobase scramble velocities and prevent the high-velocity tail from accumulating, so escape effectively only happens at and above the exobase.
The exobase altitude itself is set by where the mean free path equals the scale height, which depends on temperature, composition, and gravity.
For Mars the modern exobase sits about $200\ \mathrm{km}$ above the surface; for Earth it is around $500$--$700\ \mathrm{km}$.

Finally, the temperature $T_{\mathrm{exo}}$ in the formula is the *exospheric* temperature, which is set primarily by absorption of solar EUV radiation in the upper atmosphere.
The exospheric temperature varies with solar activity and was almost certainly much higher in the early solar system, when the young Sun emitted $10$--$100$ times more EUV than today.
Hydrogen escape from early Mars would therefore have been much faster than the modern formula gives.
An early hydrogen-rich greenhouse (see above) could have lost its $\mathrm{H_2}$ on a timescale of only a few tens of Myr.

### Atmospheric escape and the loss of Mars' atmosphere

Because Jeans escape removes only light species, heavier Martian volatiles escape through non-thermal channels {cite:p}`Jakosky2018`, which include **photochemical escape** (dissociative reactions producing fast neutrals), **ion escape** (acceleration by the solar wind), and **sputtering** (knockout by impacting ions).

```{figure} figures/jakosky2018_loss.avif
:name: fig:jakosky-loss
:width: 500px
:align: center

Oxygen escape rates from Mars (in particles per second) for the four MAVEN-resolved channels (dissociative recombination, pick-up ions, ion outflow, and sputtering) extrapolated from present-day measurements back to $\sim 3.5$ Ga using estimates of the past solar EUV flux. All four channels were one to two orders of magnitude higher in the early Hesperian than today; the pick-up loss has dropped most steeply over time. From {cite:t}`Jakosky2018`. The integrated total atmospheric loss over $\sim 4$ Gyr (combining the oxygen channels shown here with hydrogen, carbon, and nitrogen loss inferred from other MAVEN datasets and isotopic constraints) is summarised in the body text below.
```

```{figure} figures/jakosky2018_hloss.avif
:name: fig:jakosky-h
:width: 500px
:align: center

H corona column density at Mars as a function of solar longitude over a Mars year. Hydrogen escape varies by an order of magnitude over the seasonal cycle, peaking near perihelion when the lower atmosphere is warmer and water vapour rises to higher altitudes where it is photolysed. From {cite:t}`Jakosky2018`.
```

Extrapolating escape rates across solar EUV history indicates Mars lost $\sim 0.5$ to $1$ bar of $\mathrm{CO_2}$ and $\sim 23$ m of water equivalent over $4$ Gyr {cite:p}`Jakosky2018` ({numref}`fig:jakosky-loss` and {numref}`fig:jakosky-h`).
Carbon isotope ratios independently require an early atmospheric pressure below $\sim 1\ \mathrm{bar}$ {cite:p}`Hu2015` ({numref}`fig:hu-carbon`).

```{figure} figures/hu2015_carbon_evolution.avif
:name: fig:hu-carbon
:width: 650px
:align: center

Reconstructed history of Martian carbon evolution since $3.8$ Ga (the conventional Late Heavy Bombardment epoch adopted as the starting point of the model) from {cite:t}`Hu2015`, using the modern atmospheric $^{13}\mathrm{C}/^{12}\mathrm{C}$ ratio and known carbonate constraints as boundary conditions. **(a)** Atmospheric $\delta^{13}\mathrm{C}$ evolution, with the present-day Curiosity-MSL measurement marked at right; **(b)** sputtering and photochemical escape rates (cumulative totals: $232$ mbar lost via sputtering, $8.2$ mbar via photochemistry); **(c)** carbonate formation rate for two precipitation environments (open-water systems in blue, shallow-subsurface aquifers in red), with associated total carbonate masses; **(d)** reconstructed equivalent atmospheric surface pressure of free carbon (atmosphere plus polar caps plus regolith) for two solution families with initial pressures $0.32$--$0.50$ bar (red dashed) and $0.25$--$0.29$ bar (blue solid). The solutions imply a Late Noachian / Early Hesperian atmospheric pressure that is below $\sim 1\ \mathrm{bar}$ for most of the parameter space (carbonate-conservative scenarios give $\lesssim 0.3\ \mathrm{bar}$), with an absolute upper bound of $\sim 1.8\ \mathrm{bar}$ requiring extensive subsurface carbonate sequestration ($5\ \mathrm{wt\%}$ globally in the top 500 m). The picture is consistent with the MAVEN-based escape budget but explicitly invokes the heavy-isotope enrichment of carbon as an independent constraint.
```

Atmospheric loss is regulated by the **Martian dynamo**, the internal process generating a global magnetic field, and once this magnetic shield collapsed, direct solar wind interaction drove efficient ion escape.

### Mars magnetism and the death of the dynamo

Although Mars lacks a global magnetic field today, its southern highlands retain intense **crustal magnetic anomalies**.
These are remanent fields acquired below the Curie temperature in an ancient dynamo {cite:p}`Acuna1999`.
The fields exceed $\sim 1500\ \mathrm{nT}$ at $\sim 100\ \mathrm{km}$ altitude ({numref}`fig:acuna-map` and {numref}`fig:acuna-dipoles`).
That is an order of magnitude stronger than Earth's crustal anomalies.

```{figure} figures/acuna1999_magmap.avif
:name: fig:acuna-map
:width: 700px
:align: center

Map of the radial component of the magnetic field measured by *Mars Global Surveyor* MAG/ER instrument during low-altitude aerobraking and science-phasing orbits (periapsis $\sim 100$--$200\ \mathrm{km}$). Strong remanent crustal magnetisation (red and blue patches) is concentrated in the Noachian-aged southern highlands; the younger northern lowlands and the Hellas and Argyre impact basins are essentially demagnetised. From {cite:t}`Acuna1999`. Courtesy NASA Goddard Space Flight Center.
```

```{figure} figures/acuna1999_dipoles.avif
:name: fig:acuna-dipoles
:width: 600px
:align: center

Polar stereographic projection of the radial component $B_r$ of the Martian crustal magnetic field measured during low-altitude *MGS* orbits (periapsis $\sim 100$--$200\ \mathrm{km}$; left, colour-saturated at $\pm 1500$ nT) and the corresponding topographic basemap (right, greyscale), showing concentric latitude rings at $60^\circ$, $70^\circ$, $80^\circ$ and longitude meridians at $0^\circ$, $90^\circ\mathrm{W}$, $180^\circ$, $270^\circ\mathrm{W}$. Strong Noachian-age remanent magnetisation appears as concentrated red and blue patches confined to one azimuthal sector; the rest of the polar cap and the basin-reset terrains are essentially demagnetised. The lack of crustal magnetisation across Hellas, Argyre, and the Borealis lowlands implies that the dynamo had switched off before those basins formed and reset their thermal state. From {cite:t}`Acuna1999`. Courtesy NASA Goddard Space Flight Center.
```

The Hellas, Argyre, and Isidis impact basins ($4.0$ to $4.1\ \mathrm{Ga}$) are demagnetised relative to surrounding terrain.
Impact heating above the magnetite Curie temperature ($\sim 850\ \mathrm{K}$) erased crustal magnetisation after the dynamo died.
This originally dated dynamo shutdown to $4.1$ to $3.9\ \mathrm{Ga}$ {cite:p}`Acuna1999`.

*MAVEN* data revealed crustal fields at $\sim 4.5\ \mathrm{Ga}$ and $\sim 3.7\ \mathrm{Ga}$.
This suggests a longer-lived or episodic dynamo {cite:p}`Mittelholz2020`.
Basin demagnetisation may also reflect impact excavation or a reversing dynamo rather than thermal erasure {cite:p}`Steele2024`.
These mechanisms place dynamo shutdown in the early Hesperian.

Collapse of the magnetic shield exposed the upper atmosphere to the solar wind.
Ion escape accelerated and stripped $\mathrm{CO_2}$ and water.
Mars is the textbook case of a world where the loss of internal magnetism was followed by the loss of habitability.

### Mars exploration: a brief history

Mars exploration is the longest-running campaign of planetary science.
The *Mariner 4* flyby in 1965 returned the first close-up images.
They revealed a heavily cratered, desert-like world rather than Earth-like conditions.
The *Mariner 9* orbiter in 1971--72 revealed volcanoes, canyons, and polar caps.
It showed the dramatic contrast between the cratered south and smoother north.
The *Viking* program (1976) landed two spacecraft to look for biology in Martian soil, yielding ambiguous results, while its meteorology and imaging set the framework for everything that followed.

The 1990s were the decade of orbital mapping.
*Mars Global Surveyor* (1997 to 2006) produced global topography {cite:p}`Smith2001` and discovered crustal magnetic anomalies {cite:p}`Acuna1999`.
*Mars Pathfinder* (1997) operated the first Mars rover, *Sojourner*.
*Mars Odyssey* (2001 to present) mapped subsurface hydrogen.
This gave the first direct evidence for buried water ice in mid-latitudes.

The 2000s were the decade of rovers.
*Spirit* and *Opportunity* (2004) demonstrated sustained surface science and found in-situ evidence for past water.
*Mars Express* (2003 to present) revealed global mineralogy summarised by {cite:t}`Bibring2006`, which *Mars Reconnaissance Orbiter* (2006 to present) refined with sub-metre imaging.

The 2010s and 2020s have been dominated by *Curiosity* at Gale crater and *Perseverance* at Jezero crater.
*Curiosity* (2012 to present) established a long-duration habitable lacustrine environment at Yellowknife Bay {cite:p}`Grotzinger2014`.
*Perseverance* (2021 to present) is exploring delta deposits and caching rock cores for future return to Earth.
The *Ingenuity* helicopter accompanied it and demonstrated powered atmospheric flight.
Other recent additions include *InSight* (2018 to 2022), which operated as a stationary geophysical station, and China's *Tianwen-1* (2021), which delivered the *Zhurong* rover to Utopia Planitia.

### Mars Sample Return and the question of biosignatures

**Mars Sample Return** (MSR) is the joint NASA-ESA campaign to retrieve rock samples cached by *Perseverance* at Jezero.
Returning samples to Earth allows terrestrial laboratory instruments to analyze materials selected for high astrobiological potential.
The primary scientific goal is to determine whether the samples contain definitive biosignatures from past or present Martian life {cite:p}`Beaty2019`.
Even a confident negative result would tightly constrain models of the origin of life.

{cite:t}`Orosei2018` reported *MARSIS* radar reflections at the south polar cap interpreted as a $\sim 20\ \mathrm{km}$-wide subglacial lake of liquid water.
This would have been the first detection of stable liquid water on Mars.
The implications for habitability would be strong.
Subsequent reanalyses argued that conductive, clay-rich basal layers can reproduce the reflections without liquid water.
The interpretation remains contested.

The Mars Sample Return (MSR) programme itself is in difficulty.
The original NASA-ESA architecture targeted return of the cached samples in the early 2030s.
In 2023, an Independent Review Board concluded that the reference mission was too expensive and too slow {cite:p}`NASAESAMSR2023`.
An architecture-review process followed in 2024.
As of early 2026, the architecture, schedule, and cost remain uncertain while competing concepts are evaluated.

## Part 3: Comparative payoff for terrestrial planet evolution

### Mercury and Mars as opposite limiting cases

As the smallest rocky planet closest to the Sun, Mercury cooled rapidly, froze most of its core, and lost its volatiles.
Yet it maintains an active dynamo in a thin convecting outer core and hosts polar ice in cold traps from near-zero obliquity.

Mars accreted volatiles at the outer edge of the habitable zone.
It cooled more slowly than Mercury.
It sustained a dynamo and surface liquid water for the first $\sim 700$ Myr of its history before losing its dynamo and atmosphere.

Both bracket Earth and Venus on the scaling relations of {ref}`Lecture 3 <lecture03>` and {ref}`Lecture 4 <lecture04>`:

- **Cooling timescale** scales as $\tau \sim L^2/\kappa$ for diffusive heat loss with body size $L$, so a factor of two smaller body cools four times faster.
- **Atmospheric retention** depends exponentially on the escape parameter $\lambda \propto M / (T r_{\mathrm{exo}})$ from equation {eq}`eq:lambda`.
- **Volatile inventory** at formation depends on heliocentric distance across the ice line and volatile delivery from the outer disc ({ref}`Lecture 2 <lecture02>`).

Mercury fails the first two scaling relations.
Mars fails the second and third, as its mass cannot retain a thick atmosphere once its dynamo dies and ion escape takes over.

### Size and distance set the trajectory

Size and distance from the central star primarily determine the long-term evolution of a rocky planet, and most properties, including interior structure, atmospheric composition, climate, and habitability, follow from these two parameters.

Size controls interior cooling rate, the dynamo heat budget, absolute radiogenic heating, and surface gravity (setting the escape parameter $\lambda$), whereas distance from the Sun controls equilibrium temperature, volatile delivery during accretion, stellar wind erosion, and early hot-phase dynamics.

These outcomes are modulated by stochastic events such as giant impacts, accretion timing, and chaotic obliquity dynamics.
This framework applies in {ref}`Lecture 13 <lecture13>` and {ref}`Lecture 14 <lecture14>` to exoplanets, where size and orbital distance are typically the only known parameters.

### The timing problem: dynamo lifetimes and habitability

The four rocky planets show distinct dynamo histories.
Earth has an active dynamo sustained by **compositional buoyancy**, buoyancy released by inner-core crystallisation.
Mercury has a weak dynamo sustained by partial core freezing and convection in a thin liquid shell.
Mars had a dynamo for its first $\sim 500$ to $800$ Myr.
It ceased around $4.0$ to $3.7$ Ga {cite:p}`Steele2024`.
Venus lacks a detectable intrinsic field, and its dynamo history remains unknown ({ref}`Lecture 9 <lecture09>`).

Dynamo longevity correlates with atmospheric retention and surface habitability.
Earth has a long-lived dynamo, a thick atmosphere stable on Gyr timescales, and surface life.
Mars and Venus lack present-day dynamos, have lost most of their atmospheres (Mars to space, Venus to runaway greenhouse), and are uninhabitable today.
Mercury never developed an Earth-like atmosphere because its small size and proximity to the Sun gave it neither volatile inventory nor gravitational retention.

This correlation does not prove a causal link between dynamo longevity and habitability: *MAVEN* escape rates show that an unmagnetised Mars-sized planet loses its atmosphere on $10^9$-year timescales rather than through immediate collapse.
However, a magnetic shield suppresses **ion escape** by up to an order of magnitude over Gyr timescales.

### What makes a rocky planet habitable?

Synthesising {ref}`Lecture 9 <lecture09>` and this lecture, a rocky planet requires four principal ingredients for long-term surface habitability:

1. **Liquid water**: maintaining surface water requires an adequate volatile inventory at formation, a suitable equilibrium temperature (or compensating greenhouse gases), and surface pressure high enough to prevent vacuum boiling.

2. **Volatile recycling**: active geology must exchange volatiles between the surface, atmosphere, and interior (such as via plate tectonics) so they are not permanently sequestered in a single reservoir.

3. **Magnetic shielding**: a global magnetic field mitigates stellar wind erosion; its quantitative role is debated, but the contrast between magnetised Earth and unmagnetised Mars is one of the strongest empirical cases that magnetism matters.

4. **Climate stability**: negative temperature feedbacks, notably the **carbonate-silicate cycle** (the Walker thermostat; {cite:p}`Walker1981`), regulate atmospheric $\mathrm{CO_2}$ by accelerating silicate weathering at higher temperatures to cool the surface.

Earth satisfies all four ingredients.
Venus and Mars each fail on at least two, and Mercury lacks volatiles and an atmosphere.
These four ingredients provide a conceptual framework for evaluating exoplanet habitability.

We will return to this synthesis in {ref}`Lecture 14 <lecture14>` when exploring habitability across the broader rocky-planet population.

### Recent advances and upcoming missions

The next decade will advance comparative rocky-planet science across several upcoming missions.
BepiColombo enters orbit at Mercury in late 2026 to map the magnetic field, surface composition, polar ice inventory, and moment of inertia.
JAXA MMX launches in 2026 for sample return from Phobos in 2031.
It aims to resolve whether the Martian moons originated as captured asteroids or giant-impact debris.

Exploration of Mars continues through orbital, surface, and sample return missions.
ExoMars Rosalind Franklin is scheduled for launch in 2028 to perform subsurface drilling for biosignatures, and Mars Sample Return remains planned to return samples for biosignature detection.
On the surface, Curiosity and Perseverance continue operations.
*Curiosity* provides a long-baseline climate record from Gale crater.
Orbital radar from MARSIS and SHARAD continues to map buried polar and mid-latitude ice.
The success of the *Ingenuity* helicopter has also demonstrated aerial platforms for planetary exploration.

## Summary and takeaways

- **Mercury and Mars are limiting cases for rocky-planet evolution.** Mercury is too small, too close, and too volatile-poor. Mars is too small to retain its atmosphere once the dynamo died. Both bracket Earth and Venus on the parameters that matter most for long-term habitability: size, distance, dynamo longevity, atmospheric retention.
- **Each of Mercury's oddities points to a specific physical mechanism.** The high uncompressed density requires non-standard formation, plausibly involving giant impacts. The persistent weak dynamo requires a thin convecting shell with thermal stratification. The polar ice survives because the obliquity is essentially zero. The lobate scarps and active faulting record ongoing global contraction.
- **Mars preserves the geological record of an Earth-like planet that lost its habitability.** The Noachian was wet enough to form valley networks, lakes, and clays. The Hesperian saw transitional, more acidic conditions and the bulk of the volcanic resurfacing. The Amazonian is the cold dry modern Mars. The dynamo died sometime between $4.1$ and $3.7$ Ga (the basin-demagnetisation estimate of $4.1$--$3.9$ Ga, refined by more recent magnetometer analyses to as late as $\sim 3.7$ Ga), and atmospheric loss to space (now measured in real time by MAVEN) accumulated to $\sim 0.5$--$1$ bar of $\mathrm{CO_2}$ and $\sim 23$ m of water over geological time.
- **The Jeans escape formula, equation {eq}`eq:jeans`, is selective.** Light species escape; heavy species do not. Mars' atmospheric loss is dominated by non-thermal (photochemical and ion-escape) processes, not by Jeans escape, except for hydrogen.
- **Comparative planetology with the four rocky planets gives us four independent natural experiments** on the parameters that determine planetary evolution. This is the best calibration we will have for the inevitable next step of comparing those four solar-system worlds with the much larger sample of rocky exoplanets we will see in {ref}`Lecture 13 <lecture13>` and {ref}`Lecture 14 <lecture14>`.

## References

```{bibliography}
:filter: docname in docnames
```
