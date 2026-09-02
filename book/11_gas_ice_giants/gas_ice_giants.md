(lecture11)=
# Gas & Ice Giants: Jupiter, Saturn, Uranus, Neptune

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to compare the internal structures and atmospheric dynamics of the four giant planets, describe the diversity of their satellite systems, derive the Roche limit and apply it to Saturn's rings, and use the gas giant / ice giant dichotomy as a natural laboratory for exoplanet analogues.
```

```{seealso}
**Slides:** [Download Lecture 11 (PDF)](../_static/slides/lecture11.pdf)
```

The four giant planets of our solar system together hold more than 99.5% of the planetary mass beyond the Sun.
They are not, however, four examples of the same kind of object.
Jupiter and Saturn are dominated by hydrogen and helium.
They are best thought of as failed stars whose envelopes never collapsed gravitationally.
Uranus and Neptune are roughly an order of magnitude less massive, contain only modest hydrogen and helium envelopes, and are dominated by what astronomers loosely call "ices".
The split between gas giants and ice giants is one of the most informative features of the solar system: it reflects the timing of core formation, the migration history of the outer planets, and the lifetime of the protoplanetary disk that we discussed in {ref}`Lecture 2 <lecture02>`.
This lecture treats each subgroup in turn, integrates the diverse satellite and ring systems into the planetary narratives, and closes with a comparative payoff and a survey of the missions that will define outer solar system science for the next two decades.

## Part 1: The gas giants, Jupiter and Saturn

### Gas giant overview: what makes them different

Jupiter has a mass of $1.898 \times 10^{27}$ kg (318 $\Mearth$), an equatorial radius of 71,492 km (11.2 $\Rearth$), and a mean density of 1326 kg m$^{-3}$ {cite:p}`NASAFactSheet`.
Saturn has a mass of 95 $\Mearth$, an equatorial radius of 60,268 km (9.4 $\Rearth$), and a mean density of 687 kg m$^{-3}$, lower than water.
These low densities indicate bulk compositions of hydrogen and helium rather than rock.
Together, the two gas giants account for about 92% of total planetary mass in the solar system.

Their envelopes are dominated by molecular hydrogen ($\mathrm{H_2}$) and helium (He) in near-solar proportions, with slight enrichment in heavier elements ({ref}`Lecture 2 <lecture02>`).
Neither planet has a solid surface.
Pressure and temperature rise smoothly with depth.
The gas becomes a **supercritical fluid** (where liquid and gas become indistinguishable) and then a metallic plasma.
By convention, the planetary surface is defined as the level where atmospheric pressure reaches 1 bar {cite:p}`Stevenson2020`.

Both gas giants rotate rapidly, with periods of about 9 h 56 min for Jupiter and 10 h 33 min for Saturn.
Strong Coriolis forces organize atmospheric circulation into alternating east-west bands of bright zones and darker belts.
This rapid rotation makes both planets visibly oblate.
The flattening is about 6.5% for Jupiter and 9.8% for Saturn.
This oblateness constrains the interior density distribution through **zonal harmonics** ($J_2, J_4, J_6, \dots$), gravitational coefficients measured by Juno and Cassini {cite:p}`Iess2018,Iess2019`.

Both planets radiate more energy than they absorb from the Sun, roughly 1.7 (Jupiter) and 1.8 (Saturn) times the absorbed solar flux.
For Jupiter, this excess heat is explained by **Kelvin-Helmholtz contraction**, the slow planetary contraction releasing gravitational potential energy as heat {cite:p}`FortneyNettelmann2010`.
For Saturn, contraction alone is insufficient.
The additional energy comes from **helium rain**, the immiscibility of helium in metallic hydrogen as droplets settle inward {cite:p}`Stevenson1980`.

### Jupiter interior structure

Jupiter's interior consists of fluid layers separated by smooth transitions in composition and physical state {cite:p}`Stevenson2020`.
Below the molecular $\mathrm{H_2}$ and He envelope, increasing pressure compresses hydrogen into **metallic hydrogen**, an electrically conducting state in which electrons become delocalised.
This gradual transition occurs near $100$ GPa and $5000$ K.
That corresponds to a fractional radius of about $0.85\,R_J$ {cite:p}`Wahl2017`.
Below this depth, the conducting fluid powers the **dynamo**, the self-sustaining process by which fluid motion generates a magnetic field ({ref}`Lecture 4 <lecture04>`), while central conditions reach $\sim4000$ GPa and $\sim20{,}000$ K {cite:p}`Wahl2017,Militzer2022`.

```{figure} figures/jupiter_dilute_core_wahl2017.avif
:align: center
:name: fig:jupiter_dilute_core
:width: 70%

Density as a function of fractional radius for representative Jupiter interior models from {cite:t}`Wahl2017`, comparing two equations of state (MH13 and REOS3). The compact-core models (dashed curves) exhibit a sharp density discontinuity at the inner core boundary near $r/r_J \approx 0.15$, while the dilute-core models (solid curves) show a smooth, gradual increase in density across roughly the inner half of the planet. The inset cartoon sketches the layered structure inferred for Jupiter: an outer molecular hydrogen envelope, an intermediate metallic-hydrogen layer with helium-rain droplets, and a dilute core in which heavy elements are mixed throughout the inner region rather than concentrated in a discrete central body.
```

Traditional interior models assumed a compact core of heavy elements at fractional radii of less than 0.2, but Juno gravity measurements of zonal harmonics ($J_4$, $J_6$, $J_8$, and $J_{10}$) cannot be matched by compact-core models.
Instead, the data require a **dilute core**, in which $20\text{--}40\,\Mearth$ of heavy elements are distributed across the inner $30$ to $50$% of Jupiter's radius and smoothly grade into the envelope ({numref}`fig:jupiter_dilute_core`) {cite:p}`Militzer2022`.

The dilute core has direct implications for planetary formation.
A compact core of $\sim10\,\Mearth$ assembled by **core accretion**, the formation pathway in which a solid core gravitationally binds a surrounding gas envelope ({ref}`Lecture 2 <lecture02>`), is buoyantly stable against mixing and cannot naturally erode into metallic hydrogen.
The distributed heavy elements therefore imply either efficient early mixing from a giant impact or the late hydrodynamic accretion of an envelope containing dissolved heavy elements {cite:p}`Militzer2022`.

### Jupiter atmosphere and weather

Jupiter's visible atmosphere is the cloud-bearing layer between 0.1 and 10 bar.
As discussed in {ref}`Lecture 6 <lecture06>`, condensation curves set three cloud decks: ammonia ice ($\mathrm{NH_3}$) near 0.5 to 1 bar, ammonium hydrosulfide ($\mathrm{NH_4SH}$) near 2 to 3 bar, and water ice at $\sim 5$ to 7 bar.
Galileo probe measurements confirmed this layered structure during atmospheric entry in 1995.
The entry site, however, was unusually dry.
This is a reminder that local meteorology can deviate strongly from horizontally averaged models {cite:p}`Niemann1998`.

```{figure} figures/jupiter_grs_juno.avif
:align: center
:name: fig:jupiter_grs
:width: 437px

Crescent Jupiter and the Great Red Spot imaged by Juno's JunoCam during the third close perijove in December 2016. The image is a citizen-science processing of public Juno data and shows the GRS, the train of white ovals known informally as the "string of pearls", and the long-lived storm Oval BA below the GRS. Image credit: NASA/JPL-Caltech/SwRI/MSSS, processed by Roman Tkachenko.
```

About fifteen alternating **zonal jets** reach velocities of order 180 m s$^{-1}$ {cite:p}`dePaterLissauer2010`, and bright **zones** (rising air topped by ammonia clouds) alternate with darker **belts** (descending air exposing deeper haze).
Embedded in this flow is the **Great Red Spot** (GRS).
It is an anticyclonic vortex (a storm rotating opposite to a cyclone at the same latitude).
It has been observed continuously since at least 1830.
The GRS has contracted from about 40,000 km at the start of the twentieth century to roughly 14,000 km today.
The mechanisms driving this contraction remain debated ({numref}`fig:jupiter_grs`).

```{figure} figures/jupiter_north_pole_cyclones_juno.avif
:align: center
:name: fig:jupiter_n_pole
:width: 75%

Cluster of cyclones encircling Jupiter's north pole, imaged by Juno's JIRAM thermal infrared instrument. A central polar cyclone is surrounded by eight cyclones in a stable polygonal arrangement. The pattern persisted across multiple Juno perijove flybys and demonstrates the rotational organization of Jovian polar weather. Compare to {numref}`fig:jupiter_s_pole`. Image credit: NASA/JPL-Caltech/SwRI/ASI/INAF/JIRAM. See {cite:t}`Adriani2018`.
```

```{figure} figures/jupiter_south_pole_juno.avif
:align: center
:name: fig:jupiter_s_pole
:width: 75%

Jupiter's south pole as seen by JunoCam in visible light. A central cyclone (diameter $\sim$5,800 km) is surrounded by five companion cyclones, each $\sim$5,600--7,000 km across. Unlike the north pole (where the central cyclone is encircled by eight companions $\sim$4,000--4,600 km in diameter), the south pole hosts a pentagonal arrangement, which shows that the polar cyclone clusters are stable but not unique solutions of the deep-jet dynamics. Image credit: NASA/JPL-Caltech/SwRI/MSSS/Betsy Asher Hall/Gervasio Robles. See {cite:t}`Adriani2018`.
```

Both poles host stable polygonal cyclone clusters: a central cyclone surrounded by eight others at the north pole and five at the south pole {cite:p}`Adriani2018` ({numref}`fig:jupiter_n_pole` and {numref}`fig:jupiter_s_pole`).
{cite:t}`Kaspi2018` showed that zonal jets penetrate several thousand kilometres, decaying by $\sim$2,000 km and vanishing by $\sim$3,000 km, and below this depth magnetic stresses in metallic hydrogen damp differential rotation into solid-body rotation.

Jupiter's powerful aurorae are driven by magnetospheric processes ({ref}`Lecture 4 <lecture04>`) and volcanic mass loading from Io of about $1\text{ tonne s}^{-1}$ of sulfur and oxygen.
Ultraviolet auroral footprints of Io, Europa, and Ganymede demonstrate electromagnetic coupling between Jupiter and its moons.
Juno also mapped the equatorial "Great Blue Spot", an intense magnetic anomaly that probably reflects unusual structure in the dynamo source region {cite:p}`Connerney2022`.

### Io

Io is the most volcanically active body in the solar system.
Its global heat output is about $10^{14}$ W.
This heat is dissipated as tidally driven volcanism rather than radiogenic heat ({ref}`Lecture 3 <lecture03>`).
It is sustained by tidal flexing in the **Laplace resonance**, an orbital resonance with Europa and Ganymede (orbital periods 1:2:4) {cite:p}`Peale1979`.

```{figure} figures/io_loki_volcano.avif
:align: center
:name: fig:io_loki
:width: 70%

Loki Patera, the largest volcanic depression on Io, imaged by Voyager 1 in 1979. Loki is a periodically resurfacing lava lake about 200 km across that contributes a substantial fraction of Io's global thermal output. Image credit: NASA/JPL.
```

```{figure} figures/io_tvashtar_eruption.avif
:align: center
:name: fig:io_tvashtar
:width: 65%

Composite Galileo view of the active fire fountain at Tvashtar Catena on Io, combining low-resolution colour imaging from orbit C21 with visible and infrared data from orbits I25 (26 Nov 1999) and I27 (22 Feb 2000) that captured the active lava flow in the act. Tvashtar is one of the most dramatic active volcanic eruptions documented in the solar system. Image credit: NASA/JPL/University of Arizona.
```

Volcanic resurfacing on $\sim$Myr timescales leaves Io with essentially no impact craters ({numref}`fig:io_loki` and {numref}`fig:io_tvashtar`).
Io's tenuous $\mathrm{SO_2}$ atmosphere is supplied by volcanic plumes and sublimating surface frosts.

```{figure} figures/io_tidal_park2024.avif
:align: center
:name: fig:io_tidal
:width: 90%

Io's measured tidal response compared with interior models **without** (a) and **with** (b) a global magma ocean. The sketches show the layering of each model. The plots show the dissipation factor $|k_2|/Q$ (vertical axis, logarithmic) against the real part of the tidal Love number, $\mathrm{Re}(k_2)$ (horizontal axis). Separate curves correspond to different lithosphere thicknesses $d$ (a) or to different depths $h$ of a 100 km thick magma ocean (b); the markers along each curve mark models with different values of the mantle rheology parameter $\beta$, which sets how strongly the mantle dissipates tidal energy. Green boxes are the 1$\sigma$ and 3$\sigma$ Juno constraints, and grey bands mark the earlier astrometry-only constraint. Models without a magma ocean pass through the Juno box for low values of $\beta$, whereas a magma ocean shallower than about 500 km produces a far larger $\mathrm{Re}(k_2)$ than measured. The data therefore **preclude a shallow magma ocean** and are consistent with a mostly solid mantle: a single gravity measurement can rule out a whole class of interior structures. Reproduced from {cite:t}`Park2024`.
```

Juno measured the gravitational **$k_2$ tidal Love number** (a dimensionless measure of tidal deformation) to be $k_2 \approx 0.125 \pm 0.047$ {cite:p}`Park2024`.
This rules out a global shallow magma ocean.
It requires a mostly solid silicate mantle with localised partial melting ({numref}`fig:io_tidal`).

### Europa

Europa is an icy Galilean moon ($R = 1561$ km).
Low crater counts indicate a young surface age of 40–90 Myr {cite:p}`Pappalardo1999`.
Its water-ice surface is marked by **lineae** (long fracture systems) and **chaos terrain** (disrupted regions of broken and refrozen ice) ({numref}`fig:europa_galileo` and {numref}`fig:europa_chaos`).

```{figure} figures/europa_galileo_mosaic.avif
:align: center
:name: fig:europa_galileo
:width: 326px

High-resolution view of Europa's surface from the Galileo orbiter, showing the network of dark and bright lineae (long fractures), patches of chaos terrain, and the limited density of impact craters indicative of a young surface. Image credit: NASA/JPL-Caltech/SETI Institute.
```

```{figure} figures/europa_chaos_terrain.avif
:align: center
:name: fig:europa_chaos
:width: 75%

The Conamara Chaos region on Europa imaged at high resolution by the Galileo orbiter (PIA01640). Polygonal blocks of ice have rotated and translated relative to one another and refrozen into a darker matrix material. The morphology is consistent with brief episodes of partial melting and refreezing of the ice shell, possibly driven by warm rising plumes within the ice, by intrusions of ocean water, or by the foundering of slabs of icy crust. Image credit: NASA/JPL-Caltech/ASU.
```

Galileo magnetometer data revealed an induced magnetic moment requiring a global, electrically conducting subsurface ocean beneath the ice shell {cite:p}`Khurana1998`.
The ice shell is estimated at 6–25 km thick and the underlying ocean at $\sim$100 km deep.
This liquid water is sustained by tidal heating generated by Europa's orbital eccentricity in the Laplace resonance with Io and Ganymede.

NASA's Europa Clipper mission, launched in October 2024, will arrive at Jupiter in 2030 to conduct approximately fifty close flybys {cite:p}`HowellPappalardo2020`.
Its payload includes ice-penetrating radar, a magnetometer, mass spectrometers, and high-resolution imaging to characterise the ice shell and subsurface ocean.

### Ganymede

Ganymede is the largest moon in the solar system.
Its radius is 2634 km.
It is the only moon with an **intrinsic dynamo magnetic field**, an internally generated field ({ref}`Lecture 4 <lecture04>`, {ref}`Lecture 8 <lecture08>`).
Its interior is fully differentiated into a metallic iron core, silicate mantle, and outer ice shell ({numref}`fig:ganymede_juno` and {numref}`fig:ganymede_grooves`).

```{figure} figures/ganymede_juno_closeup.avif
:align: center
:name: fig:ganymede_juno
:width: 412px

Ganymede imaged by JunoCam during the 7 June 2021 close flyby, the first close encounter with the moon since Galileo's mission ended in 2003. The image highlights the contrast between bright grooved terrain and darker ancient cratered terrain. Image credit: NASA/JPL-Caltech/SwRI/MSSS.
```

```{figure} figures/ganymede_grooves.avif
:align: center
:name: fig:ganymede_grooves
:width: 75%

Grooved bright terrain (Lagash Sulcus) cutting through ancient cratered dark terrain in the Marius Regio of Ganymede, imaged at $\sim$288 m/pixel by the Galileo orbiter on 6 June 1997 (PIA01617). The parallel ridges and troughs record episodes of tectonic extension early in Ganymede's history and stand in stark contrast to Callisto's heavily cratered, undisturbed surface. Image credit: NASA/JPL-Caltech/Brown University.
```

Hubble UV observations of auroral rocking require an ocean approximately 100 km deep beneath a 150 km ice shell {cite:p}`Saur2015`.
ESA's JUICE mission, launched in 2023, will orbit Ganymede in 2034 to map its interior {cite:p}`Grasset2013`.

### Callisto

Callisto, the outermost Galilean moon, is only **partially differentiated**.
Rock and ice are incompletely separated ({numref}`fig:callisto` and {numref}`fig:callisto_cutaway`).
Its bulk density of 1834 kg m$^{-3}$ and dimensionless moment of inertia $C/MR^2 \approx 0.355$, compared to 0.4 for a uniform sphere, reflect this incomplete separation {cite:p}`Anderson2001`.

```{figure} figures/callisto_global.avif
:align: center
:name: fig:callisto
:width: 60%

Callisto in global colour view, assembled from Galileo and Voyager images. The surface is dominated by ancient impact craters and lacks the tectonic features that betray subsurface activity on Europa and Ganymede. The bulk density and moment of inertia indicate only partial differentiation. Image credit: NASA/JPL-Caltech.
```

```{figure} figures/callisto_cutaway.avif
:align: center
:name: fig:callisto_cutaway
:width: 85%

Schematic interior structures of the four Galilean moons (left to right: Io, Europa, Ganymede, Callisto) at comparable scale, NASA/JPL artist concept (PIA01082). Callisto, on the right, is only partially differentiated, in contrast to the fully differentiated Ganymede next to it. Its inferred subsurface ocean (blue layer near the surface) comes from Galileo magnetometer data showing an induced magnetic field similar to that of Europa, although the conducting layer in Callisto is plausibly less massive and less salty. Image credit: NASA/JPL-Caltech.
```

Callisto's heavily cratered surface shows no evidence of tectonic resurfacing.
Because Callisto lies outside the 1:2:4 Laplace resonance with Io, Europa, and Ganymede, its eccentricity damps and tidal dissipation is negligible.
However, Callisto induces a time-varying magnetic field in the ambient Jovian field, which is most easily explained by a conducting layer near the surface, presumably a salty subsurface ocean {cite:p}`Khurana1998`.

Callisto sits outside Jupiter's main radiation belts and experiences a much lower radiation dose than the inner Galileans, which is why it is sometimes proposed as the safest site for a future crewed outpost in the Jovian system.

### Jupiter's rings and small moons

Unlike Saturn's bright icy rings, Jupiter's are faint **dusty rings** (transient debris clouds) ejected from inner moons like Amalthea ({numref}`fig:amalthea`) by micrometeorite impacts.
Atmospheric drag and radiation pressure remove this dust.

```{figure} figures/amalthea_juno.avif
:align: center
:name: fig:amalthea
:width: 70%

Detection of Amalthea (small silhouette indicated by arrows in both panels) against Jupiter's cloud bands by JunoCam during the 59th perijove flyby on 7 March 2024 from a distance of $\sim$$265{,}000$ km (PIA25728). Amalthea is unresolved at this geometry: the image documents the moon's position rather than its shape. Amalthea has a mean radius of $\sim$84 km, an irregular shape ($\sim$250 $\times$ 146 $\times$ 128 km from Galileo data), and a reddish surface believed to reflect contamination from Io's volcanic plumes; it is one of the principal sources of dust for Jupiter's faint ring system through micrometeorite gardening of its surface. Image credit: NASA/JPL-Caltech/SwRI/MSSS, processed by Gerald Eichst{\"a}dt.
```

### Saturn interior and rotation

Like Jupiter, Saturn has a hydrogen and helium envelope.
Its lower mass, however, limits the peak interior pressure to a third of Jupiter's.
The metallic hydrogen transition therefore occurs at a smaller fractional radius.
Cassini gravity measurements and ring seismology constrain its interior {cite:p}`Mankovich2021`.

At 1 to 3 Mbar and 5000 to 10,000 K, helium becomes immiscible.
It forms **helium rain**: droplets that condense and sink under gravity.
Their sinking releases gravitational energy as heat, explaining Saturn's excess luminosity {cite:p}`Stevenson1980`.
This process depletes upper-envelope helium, matching Voyager measurements.
Jupiter undergoes less helium rain because its hotter interior limits immiscibility.

```{figure} figures/saturn_interior_mankovich2021.avif
:align: center
:name: fig:saturn_interior
:width: 70%

Saturn's heavy-element distribution $Z(r)$ (top), density $\rho(r)$ (middle), and Brunt-Vaisala frequency $N$ (bottom) as a function of fractional radius from {cite:t}`Mankovich2021`. The colour scale is the relative log-likelihood of each model, the yellow track is the maximum-likelihood profile, and the grey envelope is the prior. The heavy elements form a stably stratified, dilute distribution extending out to roughly 60% of Saturn's radius rather than being concentrated in a compact central core.
```

```{figure} figures/saturn_kronoseismology_mankovich2021.avif
:align: center
:name: fig:kronoseismology
:width: 90%

Kronoseismology constraints on Saturn's interior from {cite:t}`Mankovich2021`. Left: family of allowed heavy-element profiles $Z(r)$ and Brunt-Vaisala frequencies $N(r)/\omega_{\rm dyn}$. Right: pattern speeds and resonance radii of the f-mode oscillations of Saturn that drive observable density waves in the C ring at $\sim 75{,}000$--$95{,}000$ km radius. The observed waves (red dashed lines, labelled with their ring positions) are reproduced only by interior models with a stably stratified, dilute heavy-element distribution extending to roughly 60% of Saturn's radius. The figure is the most quantitative external probe of any giant planet interior to date.
```

Saturn's interior is probed by **kronoseismology**.
The method detects f-mode oscillations through C-ring density waves ({numref}`fig:kronoseismology`).
These waves require a stably stratified, dilute core extending to roughly 60% of Saturn's radius with $\sim$17 $\Mearth$ of rock and ice ({numref}`fig:saturn_interior`) {cite:p}`Mankovich2021`.
Like Jupiter, Saturn has an extended dilute core rather than a compact central core.

Saturn's rotation period is hard to measure.
The reason is that its magnetic dipole aligns with its rotation axis, which suppresses modulated radio emissions.
Ring seismology yields the best value: $10$ h $33$ min $38$ s {cite:p}`Mankovich2019` ({numref}`fig:saturn_rotation`).

```{figure} figures/saturn_rotation_mankovich2019.avif
:align: center
:name: fig:saturn_rotation
:width: 70%

Determination of Saturn's bulk rotation period from C-ring seismology by {cite:t}`Mankovich2019`. Each black curve shows the RMS pattern-speed residual between an interior model and the set of observed C-ring density waves identified with Saturnian $f$-modes, plotted as a function of the assumed rotation period. The thick blue curve gives the cumulative distribution of best-fit rotation periods. The seismological median is $P_{\rm S} \approx 10\,{\rm h}\,33\,{\rm min}\,38\,{\rm s}$, well separated from the older Voyager and Cassini magnetospheric estimates indicated by the coloured vertical bars.
```

The near-perfect axisymmetry of Saturn's field is puzzling because Cowling's anti-dynamo theorem requires non-axisymmetric flow to sustain a dynamo ({ref}`Lecture 4 <lecture04>`), and a stably stratified helium-rain layer likely filters out non-axisymmetric magnetic fields above the convecting metallic hydrogen.

### Saturn atmosphere and weather

Saturn's $\mathrm{NH_3}$, $\mathrm{NH_4SH}$, and $\mathrm{H_2O}$ cloud decks parallel Jupiter's.
Yet lower gravity stretches them vertically.
Lower temperatures push them deeper.
Visible contrast across belts and zones is muted, though infrared imaging reveals rich atmospheric texture below the haze.

```{figure} figures/saturn_hexagon_jet.avif
:align: center
:name: fig:saturn_hexagon
:width: 75%

Saturn's hexagonal polar jet imaged by Cassini, false-colour view (PIA14946). The hexagon, centred at about $78^\circ$ N, is a standing Rossby wave on a strong eastward zonal jet and has been continuously present since Voyager first observed it in 1981. The false-colour rendering brings out the hexagonal jet boundary that is harder to discern in true-colour imagery. Image credit: NASA/JPL-Caltech/SSI/Hampton University.
```

The **hexagonal jet stream** at $\sim 78^\circ$ N latitude is a six-sided standing wave observed by Voyager and mapped by Cassini ({numref}`fig:saturn_hexagon`).
The hexagon is a **Rossby wave** locked to an eastward zonal jet.
Such a large-scale wave arises because the effective rotation felt by a fluid parcel varies with latitude.

Saturn's equatorial jet reaches $\sim$400 m s$^{-1}$.
That is more than double Jupiter's equatorial speed.
**Great White Storms** are massive convective outbursts.
They erupt every $\sim$30 years (one Saturnian year) and circle the planet within months.
The 2010 to 2011 storm constrained moist convection of water vapour at depth.
Saturn's $26.7^\circ$ axial tilt drives strong seasonal forcing.
Northern latitudes brighten as they emerge from polar winter.

### Saturn's rings: structure and composition

Saturn's main ring system extends from the D ring at $\sim$67,000 km to the F ring at $\sim$140,000 km.
Arranged radially as D, C, B, A, F, G, and E, the bright A and B rings are separated by the **Cassini Division** at $\sim$118,000 km ({numref}`fig:cassini_division`).
The B and C rings lie inside the fluid **Roche limit** ($\sim$126,000 km), while the A ring is bounded by a 7:6 **mean-motion resonance** with Janus.

```{figure} figures/saturn_cassini_division.avif
:align: center
:name: fig:cassini_division
:width: 95%

Natural-colour radial scan across Saturn's main rings as imaged by Cassini (PIA08389). The C ring appears as the inner faint band, followed by the bright B ring, the dark Cassini Division at $\sim$118,000 km from Saturn's centre, and the outer A ring. The Cassini Division is maintained by a 2:1 mean-motion resonance with the moon Mimas: ring particles inside the gap are perturbed onto eccentric orbits and are eventually swept out, leaving the gap as a persistent feature. Image credit: NASA/JPL-Caltech/Space Science Institute.
```

```{figure} figures/saturn_propeller_targeted.avif
:align: center
:name: fig:propeller_ring
:width: 80%

Two close-up Cassini views of the same large "propeller" feature in Saturn's A ring. The asymmetric S-shape is the gravitational wake carved by an embedded $\sim$1 km moonlet that is too small to clear a gap entirely. Tracking these features over the Cassini mission has provided one of the few direct measurements of the orbital evolution of small bodies embedded in a planetary disk {cite:p}`Tiscareno2013`. Image credit: NASA/JPL-Caltech/Space Science Institute.
```

The rings are composed overwhelmingly of water ice ($>$95% by mass), with minor silicates and organics.
Particle sizes span 1 cm to 10 m under a power-law distribution.
The rings are remarkably thin.
Their vertical thickness is $\sim$10 m across $\sim$10$^5$ km radially.
The total ring mass is $\sim$$1.5 \times 10^{19}$ kg, about 40% of the mass of Mimas {cite:p}`Iess2019`.

Gravitational interactions with small moons sculpt ring structures.
Prometheus and Pandora shepherd the F ring, while Pan clears the Encke Gap in the A ring.
A 2:1 mean-motion resonance with Mimas perturbs particle orbits to clear the Cassini Division.
Embedded moonlets carve **propeller features** (partial wakes on either side of their orbit), revealing orbital migration in a planetary disk {cite:p}`Tiscareno2013` ({numref}`fig:propeller_ring`).

### Saturn's rings: age and evolution

Saturn's rings were long assumed to be **primordial** (formed at the same time as Saturn 4.5 Gyr ago).
{cite:t}`Iess2019` measured a small ring mass from Cassini gravity data, arguing that micrometeorite infall over 4.5 Gyr would have darkened older rings, which favours an age of order $10^8$ years.
However, {cite:t}`Crida2019` showed that viscous evolution from a massive primordial ring can also produce the present-day mass, so mass alone does not uniquely date the rings.

The young-rings hypothesis is supported by direct observations of **ring rain** (the ongoing transfer of mass from the rings into Saturn's upper atmosphere).
{cite:t}`Waite2018` measured a large flux of water and organic molecules falling into Saturn from the inner D ring during Cassini Grand Finale orbits.
Combined with ionospheric $\mathrm{H_3^+}$ measurements {cite:p}`ODonoghue2019`, this mass loss indicates a remaining ring lifetime and total age of order $300$ Myr, with a large uncertainty ($\sim 170$--$1100$ Myr at $1\sigma$).
If correct, Saturn's rings are temporary.
They exist for only a fraction of the planet's age.

The ring formation mechanism remains debated.
{cite:t}`Wisdom2022` proposed that an icy moon comparable to Iapetus (named "Chrysalis") was destabilised by a 3:1 resonance with Titan, scattered inside Saturn's Roche limit, and tidally disrupted.
Alternatively, {cite:t}`Charnoz2009` suggested a 1-to-5 Mimas-mass satellite was disrupted during the Late Heavy Bombardment around 4 Gyr ago, with subsequent viscous spreading producing the present-day low mass.
Solar system structures do not all date from 4.5 Gyr ago: dramatic events on $\lesssim$Gyr timescales continue to shape what we see today.

## Blackboard derivation: The Roche limit

```{admonition} Blackboard derivation: The Roche limit
:class: tip

The Roche limit is the orbital distance inside which the tidal field of a primary body exceeds the self-gravity of a fluid satellite, so that the satellite cannot hold itself together gravitationally and is instead disrupted into a disk of particles.
The concept was introduced by {cite:t}`Roche1849` and is the key piece of physics behind the existence and location of planetary rings.
We derive it here for the simplest case of a fluid (zero-strength) satellite of uniform density.

**Setup.**
Consider a planet of mass $M_p$, radius $R_p$, and density $\rho_p$.
A small spherical satellite of mass $M_s$, radius $R_s$, and density $\rho_s$ orbits at distance $d$ from the planet's centre, with $d \gg R_s$ so that we can use a leading-order Taylor expansion of the planet's gravitational potential across the satellite.
We work in the satellite's rest frame and ask: at what distance $d$ does the planetary tide stretch the satellite's surface elements faster than the satellite's own gravity can pull them back?

**Tidal acceleration across the satellite.**
The gravitational acceleration from the planet at the satellite's centre is

$$
g_{\rm centre} = \frac{G M_p}{d^2}.
$$

At the point on the satellite's surface closest to the planet, at distance $d - R_s$, the planetary acceleration is

$$
g_{\rm near} = \frac{G M_p}{(d - R_s)^2}.
$$

The differential acceleration across the satellite, that is, the tidal acceleration that tends to stretch the satellite along the planet-satellite line, is

$$
\Delta a_{\rm tidal} = g_{\rm near} - g_{\rm centre} = G M_p \left[ \frac{1}{(d-R_s)^2} - \frac{1}{d^2} \right].
$$

Expanding to first order in the small quantity $R_s/d$,

$$
\frac{1}{(d-R_s)^2} = \frac{1}{d^2} \left( 1 - \frac{R_s}{d} \right)^{-2} \approx \frac{1}{d^2} \left( 1 + \frac{2 R_s}{d} \right),
$$

so the tidal acceleration becomes

$$
\Delta a_{\rm tidal} \approx \frac{2 G M_p R_s}{d^3}.
$$

This is the standard result that tidal forces fall off as $d^{-3}$ rather than $d^{-2}$.

**Self-gravity at the satellite's surface.**
For a uniform satellite of density $\rho_s$, the gravitational acceleration at its surface is

$$
a_{\rm self} = \frac{G M_s}{R_s^2} = \frac{G \cdot \tfrac{4}{3}\pi R_s^3 \rho_s}{R_s^2} = \frac{4}{3} \pi G \rho_s R_s.
$$

**Setting the two equal.**
The Roche limit corresponds to the distance at which the tidal stretching just overcomes self-gravity, $\Delta a_{\rm tidal} = a_{\rm self}$:

$$
\frac{2 G M_p R_s}{d^3} = \frac{4}{3} \pi G \rho_s R_s.
$$

Cancel $G$ and $R_s$, and substitute $M_p = (4/3)\pi R_p^3 \rho_p$:

$$
\frac{2 \cdot (4/3)\pi R_p^3 \rho_p}{d^3} = \frac{4}{3} \pi \rho_s,
$$

which simplifies to

$$
d^3 = 2\, R_p^3 \frac{\rho_p}{\rho_s} \quad \Longrightarrow \quad d_R^{\rm rigid} = 2^{1/3}\, R_p \left( \frac{\rho_p}{\rho_s} \right)^{1/3} \approx 1.26\, R_p \left( \frac{\rho_p}{\rho_s} \right)^{1/3}.
$$

This is the **rigid-body Roche limit**: the minimum orbital distance at which a satellite held together only by its own gravity, treated as a rigid sphere, can survive without surface elements being pulled away.

**Fluid Roche limit.**
A more careful analysis for a fluid satellite, which deforms into an elongated ellipsoid before disruption rather than remaining spherical, was first carried out by Roche himself {cite:p}`Roche1849`.
The fluid case is analytically much more involved because it requires solving for the equilibrium shape of a self-gravitating fluid in a tidal field, but the result is that the prefactor changes from $1.26$ to roughly $2.46$:

$$
\boxed{ d_R \approx 2.46\, R_p \left( \frac{\rho_p}{\rho_s} \right)^{1/3}. }
$$

The rigid-body case underestimates the critical distance because it ignores the additional stress imposed by the tidal deformation itself.
For most realistic cases, including ice or rock satellites, the answer lies between the two extremes.

**Application to Saturn's rings.**
Saturn has equatorial radius $R_p = 60{,}268$ km, but for the Roche calculation we use the volumetric mean radius $R_p \approx 58{,}232$ km (which is the spherical-equivalent value entering the bulk-density definition $\rho_p = M_p/(4\pi R_p^3/3) = 687$ kg m$^{-3}$).
For ring particles dominated by water ice, $\rho_s \approx 1000$ kg m$^{-3}$, so

$$
d_R \approx 2.46 \times 58{,}232 \,\mathrm{km} \times \left( \frac{687}{1000} \right)^{1/3} \approx 2.46 \times 58{,}232 \,\mathrm{km} \times 0.883 \approx 126{,}000 \,\mathrm{km}.
$$

This matches the observed outer edge of the A ring (at $\sim 137{,}000$ km) to within $\sim$10%, the discrepancy being plausibly accounted for by the finite material strength of cold ice (which gives the satellite a non-zero rigidity), by the fact that the ring particles have lower density than pure ice because they are porous, and by the density wave structure at the very edge of the A ring.
The faint G ring at $\sim$170,000 km lies outside the formal Roche limit; it is held together by the small moon Aegaeon embedded within it rather than by self-gravity.

The physical interpretation is that, interior to $d_R$, the differential pull of the planet across any solid agglomerate is so strong that the agglomerate cannot grow above $\sim$$10$ m without being torn apart.
Ring particles therefore orbit as a collisional disk maintained by mutual scattering rather than as a single coalesced moon.
This is the key explanation for why rings exist where they do: not because anything special happened locally, but because tidal forces inside the Roche limit forbid the particles from doing what they would otherwise do, namely accrete into a single body.
```

### Titan

Titan ($R = 2575$ km) is Saturn's largest moon.
It is the only moon in the solar system with a substantial atmosphere.
Cassini and Huygens explored it during a 13-year tour and an atmospheric descent in January 2005.

```{figure} figures/huygens_titan_descent.avif
:align: center
:name: fig:huygens
:width: 75%

Stereographic projection mosaic of Huygens DISR descent images, taken on 14 January 2005 from an altitude of $\sim$3 km above Titan's surface (PIA07870). The brighter, elevated terrain at top is criss-crossed by dendritic drainage channels carved by methane runoff, which empty into a darker, flatter region resembling a coastline with offshore "islands" and shoals. The methane hydrology of Titan was confirmed in situ for the first time. Image credit: ESA/NASA/JPL-Caltech/University of Arizona.
```

```{figure} figures/titan_lakes_cassini.avif
:align: center
:name: fig:titan_lakes
:width: 75%

Lakes and seas of liquid methane and ethane near Titan's north pole, mapped by the Cassini RADAR instrument. The dark patches are radar-smooth liquid surfaces. Ligeia Mare and Kraken Mare are the largest, comparable in size to the Caspian Sea. Image credit: NASA/JPL-Caltech/ASI/Cornell.
```

Titan's $\mathrm{N_2}$ atmosphere has a surface pressure of 1.5 bar and a temperature of $\sim$94 K; the cold makes the surface air density ($\sim$5 kg m$^{-3}$) about four times that of Earth's near-surface air.
Near its triple point at 94 K, methane ($\mathrm{CH_4}$) drives an active hydrological cycle of rain and river channels ({ref}`Lecture 6 <lecture06>`) {cite:p}`Stofan2007` ({numref}`fig:huygens`).
Cassini RADAR mapped polar liquid hydrocarbon lakes including Kraken Mare and Ligeia Mare ({numref}`fig:titan_lakes`).

Solar ultraviolet radiation breaks $\mathrm{CH_4}$ apart.
The products include HCN, $\mathrm{C_2H_2}$, $\mathrm{C_2H_4}$, and $\mathrm{C_2H_6}$.
These condense into **tholins**, solid aerosol particles that produce Titan's orange haze and settle into dunes.
This haze obscures the surface in visible light.
Observers need infrared windows and radar.

Cassini gravity and tidal measurements established a global subsurface ocean beneath an ice shell of order 100 km thick {cite:p}`Iess2012`.
Titan therefore joins Europa, Ganymede, Callisto, and Enceladus as an ocean world.
Surface organics above a subsurface ocean make Titan a prime astrobiology target.

NASA's Dragonfly rotorcraft mission, launching in 2028 and arriving in 2034, will fly in Titan's dense atmosphere and low gravity {cite:p}`Lorenz2018`.
Dragonfly will hop tens of kilometres across Selk crater to sample organics, dunes, and impact melt for prebiotic chemistry.

### Enceladus

Enceladus is a small moon of 252 km radius.
In 2005, Cassini discovered active geysers erupting from south polar fractures called **tiger stripes** {cite:p}`PorcoEnc2006` ({numref}`fig:tiger_stripes` and {numref}`fig:geyser_basin`).

```{figure} figures/enceladus_tiger_stripes.avif
:align: center
:name: fig:tiger_stripes
:width: 75%

The "tiger stripes" of Enceladus: four parallel fracture zones near the south pole that are the source regions of the active plumes. The fractures are warmer than the surrounding terrain by tens of kelvins, and their ages and orientations track the stress field induced by Enceladus's eccentric orbit around Saturn. Image credit: NASA/JPL-Caltech/SSI.
```

```{figure} figures/enceladus_tiger_thermal.avif
:align: center
:name: fig:tiger_thermal
:width: 75%

Map of Enceladus's south polar region showing the correlation between jet sources identified in Cassini imaging (coloured diamonds; white circles indicate location uncertainty) and the hot spots located along the four "tiger stripe" fractures by Cassini's Composite Infrared Spectrometer (CIRS) (PIA08385). The jets erupt from the warmest portions of the fractures, which are tens of kelvins warmer than the surrounding terrain. The localised heat output is essential evidence that tidal heating is concentrated at the fracture system rather than distributed across the whole moon. Image credit: NASA/JPL-Caltech/GSFC/SwRI/SSI.
```

```{figure} figures/enceladus_geyser_basin.avif
:align: center
:name: fig:geyser_basin
:width: 80%

Cassini image of dozens of individual geyser jets erupting from the tiger stripes of Enceladus, observed against a dark background. The plumes deposit material into Saturn's E ring and feed the magnetospheric plasma with water-group ions. Image credit: NASA/JPL-Caltech/SSI.
```

The plumes contain water vapour (about 90%), salts (NaCl, KCl), and organic molecules.
Detection of $\mathrm{H_2}$ is consistent with **serpentinisation**, water-rock reactions at the seafloor {cite:p}`Waite2017`.
Phosphates and silica nanoparticles imply hydrothermal activity and the presence of biochemical building blocks {cite:p}`Postberg2023`.

A global ocean lies beneath an ice shell of 20 to 30 km.
The shell thins at the south pole.
A 2:1 **mean-motion resonance** with Dione drives tidal heating concentrated at the south pole ({numref}`fig:tiger_thermal`).
There, heat flow exceeds 10 GW.

Water, rock contact, energy, and organics make Enceladus a prime candidate for life beyond Earth.
Cassini sampled the plumes without detecting biosignatures.
The question of life stays open ({ref}`Lecture 14 <lecture14>`).

### Other Saturnian moons

Saturn's mid-sized moons form a comparative laboratory.
Mimas is dominated by the 130 km Herschel crater on a 200 km radius moon ({numref}`fig:mimas`).
Evidence for a subsurface ocean is contested.

```{figure} figures/mimas_close.avif
:align: center
:name: fig:mimas
:width: 60%

Mimas dominated by the giant Herschel impact crater, imaged by Cassini during its 13 February 2010 close flyby. The crater is $\sim$130 km across on a moon with mean radius $\sim$200 km, and the impact that formed Herschel was probably close to the catastrophic disruption threshold. Image credit: NASA/JPL-Caltech/Space Science Institute.
```

```{figure} figures/iapetus_bright_dark.avif
:align: center
:name: fig:iapetus
:width: 70%

Iapetus showing the two-toned hemispheric pattern, Cassini global mosaic from the 31 December 2004 flyby (PIA06166). The leading hemisphere (the dark Cassini Regio, covering nearly the entire visible disc here) is coated with material believed to be infall from the distant outer retrograde moon Phoebe, while the trailing hemisphere is bright water ice. A thermal-segregation feedback amplifies the contrast: the dark side absorbs more sunlight, gets warmer, sublimates ice, and becomes darker still, while the bright side stays cold and accumulates frost. The narrow ridge running along the equator is also visible. Image credit: NASA/JPL-Caltech/Space Science Institute.
```

```{figure} figures/phoebe_cassini.avif
:align: center
:name: fig:phoebe
:width: 55%

Phoebe, an outer irregular moon of Saturn, meaning its distant, retrograde, and highly inclined orbit marks it as captured rather than formed in place around the planet. Phoebe is widely interpreted as a captured Kuiper Belt object and is the source of dark dust that infalls onto Iapetus's leading hemisphere. Image credit: NASA/JPL-Caltech/Space Science Institute.
```

Iapetus has a dark leading hemisphere coated by infall from Phoebe and a bright icy trailing hemisphere.
The contrast is amplified by **thermal segregation**: dark material absorbs sunlight, sublimating ice onto the colder bright side.
It also features a $\sim$20 km high equatorial ridge ({numref}`fig:iapetus`).

Hyperion is a **chaotic rotator**.
Its irregular shape and resonance with Titan cause its spin axis to tumble unpredictably.
Phoebe's distant, retrograde, inclined orbit strongly suggests a captured Kuiper Belt object, now on a retrograde orbit at $\sim$13 million km {cite:p}`Agnor2006`.
It provides a trans-Neptunian sample ({ref}`Lecture 12 <lecture12>`, {numref}`fig:phoebe`).

Tethys, Dione, and Rhea show variable cratering and tectonism at intermediate sizes, and they illustrate how size, distance, and orbital history govern tidal heating and ocean retention.

## Part 2: The ice giants, Uranus and Neptune

### Ice giant overview: the exotic twins

Uranus ($14.5\,\Mearth$, $4.0\,\Rearth$) and Neptune ($17.1\,\Mearth$, $3.9\,\Rearth$) are **ice giants**, planets whose bulk composition is distinct from the gas giants {cite:p}`NASAFactSheet`.
Hydrogen and helium envelopes account for only $\sim$10 to 20% of their mass.
The bulk, by contrast, consists of "ices": water, ammonia, and methane.
These "ices" are dense fluids at interior conditions; the name records their origin as solid grains in the outer protoplanetary disk {cite:p}`Helled2020`.

Both planets were visited by only one spacecraft, Voyager 2, which flew past Uranus in January 1986 and Neptune in August 1989 {cite:p}`Stone1989`.
With no return mission in 35 to 40 years, the ice giants remain the most under-explored major planets.
Detailed knowledge of their atmospheres, magnetic fields, and satellites comes from these flybys, supplemented by ground-based, Hubble, and JWST observations {cite:p}`DePater2022`.

### Uranus: the tilted planet

```{figure} figures/uranus_voyager.avif
:align: center
:name: fig:uranus_voyager
:width: 60%

Uranus as seen by Voyager 2 in 1986. The planet appeared remarkably featureless at the time of the flyby, a consequence of being seen near solstice with one pole pointing nearly toward the Sun. Image credit: NASA/JPL-Caltech.
```

Uranus has an **axial tilt** of $97.8^\circ$.
Its rotation axis lies almost in the orbital plane.
Over its 84-year orbit, each pole experiences 42 years of continuous daylight followed by 42 years of darkness.
At least two giant impacts, an earlier partial tilt and a final oblique one, likely produced the tilt and spun up an equatorial debris disk from which regular satellites re-accreted ({numref}`fig:uranus_impact`) {cite:p}`Morbidelli2012`.

```{figure} figures/uranus_impact_kegerreis2018.avif
:align: center
:name: fig:uranus_impact
:width: 85%

Smoothed-particle-hydrodynamics simulation of a giant impact on the proto-Uranus, from {cite:t}`Kegerreis2018`. Snapshots are shown from $t = 1$ h to $t = 40$ h after first contact for a $2\,\Mearth$ impactor on a low angular momentum trajectory. Particles are coloured by material and origin: light and dark grey are target ice and rock, light blue is target H/He atmosphere, and purple and brown are the corresponding impactor materials. The white dashed circle marks Uranus's present-day Roche radius. Such oblique collisions deliver enough angular momentum to tilt the proto-Uranus's spin axis by tens of degrees, can deposit impactor rock into the deep interior, and (for higher angular momentum cases) eject a debris disk in the new equatorial plane from which the regular Uranian satellites later re-accrete.
```

```{figure} figures/uranus_clouds_voyager.avif
:align: center
:name: fig:uranus_clouds
:width: 60%

Voyager 2 view of Uranus from the January 1986 flyby (PIA18182). The planet appears almost featureless even in this reprocessed image; a near-pole-on viewing geometry combined with the muted, methane-dominated upper atmosphere give Uranus its bland appearance, and discrete cloud features are visible only after extreme contrast enhancement. Uranus in 1986 was far less active than Neptune was when Voyager 2 reached it in 1989. Image credit: NASA/JPL-Caltech.
```

```{figure} figures/uranus_cyclone.avif
:align: center
:name: fig:uranus_cyclone
:width: 70%

A cyclonic feature near Uranus's north pole detected by ground-based radio observations and confirmed by JWST imaging. As Uranus has approached northern summer over the past two decades, an increasing number of discrete cloud features and storm systems have become visible, in contrast to the muted appearance during the Voyager flyby. Image credit: NASA/JPL-Caltech/VLA.
```

During the 1986 Voyager 2 flyby near solstice, Uranus appeared featureless with its south pole pointing toward the Sun ({numref}`fig:uranus_voyager` and {numref}`fig:uranus_clouds`).
As equinox approached, observations revealed increasing cloud activity, including storms in 2014, a polar cyclone ({numref}`fig:uranus_cyclone`), and distinct polar cap structure {cite:p}`DePater2022`.

Uranus has an anomalously low **internal heat flow**.
It radiates only 1.06 times the absorbed solar flux {cite:p}`Pearl1990`.
By contrast, Neptune radiates 2.6 times the absorbed flux despite being further from the Sun.
This suppressed heat loss may result from a stratified interior that inhibits convective cooling, from deep latent heat release, or from a late perturbation that reset the thermal history.
None of these explanations is confirmed.
A dedicated Uranus orbiter would be the most direct test.

### Neptune: the active ice giant

```{figure} figures/neptune_great_dark_spot.avif
:align: center
:name: fig:neptune_dark
:width: 70%

The Great Dark Spot of Neptune (centre left), an anticyclonic storm in the southern hemisphere, imaged by Voyager 2 in August 1989. The dark spot was comparable in size to Earth and was bordered by bright methane cirrus clouds. The small bright cloud below the Great Dark Spot is Scooter (see {numref}`fig:neptune_scooter`), and the second dark storm at lower right is Dark Spot 2. Image credit: NASA/JPL-Caltech.
```

```{figure} figures/neptune_scooter.avif
:align: center
:name: fig:neptune_scooter
:width: 70%

Neptune's southern hemisphere with the small bright cloud feature known informally as "Scooter" visible below the Great Dark Spot. Scooter is at about $42^\circ$ S latitude and circles the planet in about 16 h, slightly faster than the 16.1 h interior rotation measured from the magnetic field, so it drifts slowly eastward (prograde) at roughly 10 m s$^{-1}$; it is one of the tracers used to map Neptune's mid-latitude zonal winds. Image credit: NASA/JPL-Caltech.
```

Voyager 2 revealed an active atmosphere on Neptune in 1989.
This contrasted with Uranus.
The **Great Dark Spot** was an Earth-sized anticyclonic storm bordered by methane cirrus clouds ({numref}`fig:neptune_dark`).
Tracked cloud features such as "Scooter" (which circles the planet in about 16 h, slightly faster than the interior) trace Neptune's **zonal flow** (winds aligned with latitude) ({numref}`fig:neptune_scooter`).
The spot vanished by 1994.
This is a sign of vigorous, transient atmospheric convection.

Neptune hosts the fastest winds in the solar system.
Peak westward speeds reach $\sim$400 m s$^{-1}$ in its equatorial jet {cite:p}`Smith1989`.
Because Neptune receives only $1/900$ of Earth's solar constant, this circulation is thought to be driven by **internal heat flow** (energy escaping from the interior), consistent with the planet radiating 2.6 times the absorbed solar flux {cite:p}`Pearl1991`.
Proposed sources for this excess luminosity include slow contraction, helium-hydrogen separation analogous to Saturn, differentiation, or internal phase transitions.
None has been directly verified.

### Ice giant interiors

Ice giants are typically modeled with three layers: a rocky core (1 to 3 $\Mearth$), an **ice mantle** of fluid water, ammonia, and methane, and a thin $\mathrm{H_2}$/He envelope.
Because Voyager 2 measured only the lowest gravity moments ($J_2$ and $J_4$), interior structures remain degenerate between discrete layers and gradual compositional gradients {cite:p}`Helled2020` ({numref}`fig:ice_giant_structures`, {numref}`fig:ice_giant_density`).

```{figure} figures/ice_giant_structures_helled2020.avif
:align: center
:name: fig:ice_giant_structures
:width: 85%

Schematic possible internal structures of an ice giant from {cite:t}`Helled2020`. Panels (a) through (d) illustrate increasingly gradual compositional transitions: (a) sharp boundaries between H/He envelope, ices, and rock; (b) sharp envelope/ice boundary but a gradual ice/rock transition; (c) gradual envelope/ice transition with a sharp ice/rock boundary; (d) fully gradual transitions from envelope through ice to rock with a global composition gradient. The Voyager-era gravity data alone cannot distinguish among these possibilities, which is one of the central motivations for a dedicated ice giant orbiter.
```

```{figure} figures/ice_giant_density_helled2020.avif
:align: center
:name: fig:ice_giant_density
:width: 70%

Density as a function of radius for Uranus (blue) and Neptune (black) from {cite:t}`Helled2020`. Solid curves are the empirical density profiles derived in earlier work, dashed curves are three-layer models with discrete envelope, ice, and rock layers. The two profiles match the gravity data equally well, illustrating the strong degeneracy between smooth and layered interior models that prevents us from uniquely identifying the bulk composition of the ice giants.
```

At high pressures ($\sim 100$ to 400 GPa and several thousand kelvins), water enters a **superionic state** where oxygen forms a rigid lattice while protons diffuse as a fluid {cite:p}`Millot2019`, and this conducting layer sustains a dynamo without metallic hydrogen {cite:p}`Soderlund2020`.

Unlike dipole-dominated Jupiter and Saturn, Uranus and Neptune have multipolar magnetic fields.
At Uranus, the dipole is tilted $\sim 59^\circ$ and offset by one-third of the planetary radius {cite:p}`StoneUranus1986`.
At Neptune, the dipole is tilted $\sim 47^\circ$ and offset by roughly half a planetary radius {cite:p}`Connerney1991`.
This geometry indicates that the dynamo operates in a thin outer shell of conducting fluid rather than a deep core.

### Triton

Triton, the largest moon of Neptune, is a captured Kuiper Belt object.
It is the only large moon in the solar system in a **retrograde orbit** (orbiting opposite to planetary rotation), inclined at $\sim 157^\circ$.
Early capture likely occurred through binary disruption during a close pass to Neptune {cite:p}`Agnor2006`.

```{figure} figures/triton_map.avif
:align: center
:name: fig:triton
:width: 75%

Triton's southern hemisphere as imaged by Voyager 2 in August 1989. Image credit: NASA/JPL-Caltech.
```

Crater counts indicate a maximum surface age of about 100 Myr ({numref}`fig:triton`).
Voyager 2 observed 8 km tall dark plumes near the south pole, interpreted as nitrogen geysers driven by solar sublimation of $\mathrm{N_2}$ ice {cite:p}`Smith1989`.
Beside Io and Enceladus, Triton is the only outer solar system body known to host active surface eruptions.
A tenuous $\sim 14$ microbar nitrogen atmosphere supports an active cycle between ice and atmosphere.

Post-capture tidal heating damped Triton's eccentricity within a few hundred Myr, possibly melting the interior to produce a subsurface water and ammonia ocean {cite:p}`McKinnon1995`.
Triton shares compositional ancestry with Pluto ({ref}`Lecture 12 <lecture12>`).
Yet tidal forces shaped it into an active world.
Its retrograde orbit is decaying.
On a timescale of order 3.6 Gyr Triton will reach the Roche limit and disrupt into a ring system.

### Ice giant rings

Both Uranus and Neptune have ring systems that are much fainter and darker than Saturn's.
The first nine Uranian rings were discovered in 1977 from **stellar occultations**, the dimming of a star passing behind the planet; thirteen narrow rings ($\lesssim$10 km wide) are known today.
The prominent epsilon ring at $\sim$51,000 km is confined by **shepherd moonlets**, small moons that gravitationally constrain ring edges.

Neptune's rings were first detected as discontinuous arcs during stellar occultations.
Voyager 2 showed that the outermost Adams ring contains five bright arcs trapped by resonances with Galatea ({numref}`fig:neptune_rings`).
The brighter arcs have visibly faded since Voyager ({numref}`fig:neptune_arcs`).

```{figure} figures/neptune_rings_voyager.avif
:align: center
:name: fig:neptune_rings
:width: 70%

Backscattered-light view of Neptune's rings from Voyager 2 in 1989. The two brightest features are the Adams ring (outer) and the Le Verrier ring (inner). The arcs in the Adams ring are gravitationally trapped at specific longitudes by resonances with the inner moon Galatea. Image credit: NASA/JPL-Caltech.
```

```{figure} figures/neptune_rings_voyager_arc.avif
:align: center
:name: fig:neptune_arcs
:width: 75%

Long-exposure forward-scattered view of Neptune's rings showing the full ring system, including the arcs in the Adams ring and the diffuse material between the named rings. Image credit: NASA/JPL-Caltech.
```

Both ice giant ring systems are dominated by dark, carbon-rich material rather than Saturn's water ice.
This compositional difference suggests that ice giant rings form from the disruption of small inner moons.
In 2023, JWST observations resolved fine ring structure at Uranus {cite:p}`DePater2022` and imaged Neptune's Adams arcs and Le Verrier ring.

## Part 3: Comparative payoff and exploration frontier

### Why gas giants and ice giants diverged

In **core accretion** ({ref}`Lecture 2 <lecture02>`), giant planets begin as solid cores that accrete gas from the protoplanetary disk.
When a core reaches a **critical mass** ($\sim$10 $\Mearth$), the attracted gas contracts dynamically and triggers **runaway gas accretion** to capture a massive $\mathrm{H_2}$/He envelope.
Because disk lifetimes are only $\sim$3 to 5 Myr, envelope growth must occur before the gas disperses.

Jupiter and Saturn reached the critical mass early.
They captured massive envelopes before disk dispersal.
Uranus and Neptune reached critical mass too late or formed where gas surface density was low, capturing only a few Earth masses of gas.
Under the **Nice model** of post-formation orbital migration ({ref}`Lecture 2 <lecture02>`; {cite:p}`Tsiganis2005,Nesvorny2018`), the ice giants migrated late and scattered trans-Neptunian planetesimals after disk dispersal.
Their 10 to 20 $\Mearth$ masses therefore represent a natural intermediate outcome of core accretion in the outer solar system.

### Common themes across all four giants

Despite the gas/ice dichotomy, the four giants share key commonalities.

1. Thermal emission exceeds absorbed sunlight on Neptune ($\sim 2.6\times$), Saturn ($\sim 1.8\times$, driven by helium rain), and Jupiter ($\sim 1.7\times$, driven by Kelvin-Helmholtz contraction).
Uranus is the sole exception with an anomalously low excess.

2. All four bodies host banded atmospheres with strong **zonal jets** (east-west winds).
Equatorial winds blow eastward on Jupiter ($\sim 180$ m s$^{-1}$) and Saturn ($\sim 400$ m s$^{-1}$), but westward on Neptune ($\sim 400$ m s$^{-1}$) and Uranus ($\sim 50$ to $100$ m s$^{-1}$).
Peak mid-latitude jets on Uranus reach $\sim 250$ m s$^{-1}$.

3. Electrically conducting fluid interiors generate global magnetic fields on all four planets.
The dynamo source is metallic hydrogen in Jupiter and Saturn, but ionic fluid in Uranus and Neptune.
Gas giants produce dipole-dominated fields, whereas ice giants exhibit multipolar, off-axis fields.

4. Moon and ring systems record each giant's dynamical history.
Jupiter hosts the four Galilean moons and a faint dust ring; Saturn possesses the A through F rings, dozens of icy moons, and Titan.
Uranus has narrow rings and five mid-sized moons, while Neptune has ring arcs and the captured Triton.

5. The four giants are laboratories for exoplanet populations.
As shown in {ref}`Lecture 13 <lecture13>`, the most common exoplanets are sub-Neptunes and Neptunes ($\sim 2$ to $4\,\Rearth$) alongside hot Jupiters ($\sim 1\,\Rjup$).
Our giant planets provide the only spatially resolved ground truth for these systems.

### What we still don't know

Major open questions include:

- How are heavy elements partitioned between rock, ice, and gas inside Uranus and Neptune?
- What sustains Neptune's strong internal heat flow compared to Uranus?
- When did Saturn's rings form, and how long will they persist?
- How did the dilute cores of Jupiter and Saturn arise during formation?
- Does Callisto host a subsurface ocean, or did incomplete differentiation prevent one?
- What deep structure maintains Saturn's hexagonal jet on multi-decade timescales?
- Are the chemistry in Enceladus's plumes and on Titan compatible with life?

These questions require new in-situ probes or dedicated orbiters.

### Exploration frontier: ongoing missions

Juno is in an extended mission through 2025, using gravity, magnetic, and microwave radiometer data alongside flybys of Io and Europa to constrain Jupiter's interior and atmosphere.
Cassini ended its mission with the 2017 Grand Finale, but its data archive continues to yield new constraints on ring mass, seismology, and atmospheric chemistry.
JWST began observing Uranus and Neptune in 2022, producing new data on their ring systems and atmospheric chemistry.

### JUICE vs Europa Clipper: two ocean-world missions

```{figure} figures/europa_clipper_concept.avif
:align: center
:name: fig:europa_clipper
:width: 75%

Artist's concept of NASA's Europa Clipper at Europa, with Jupiter in the background. Clipper launched in October 2024, will arrive at Jupiter in 2030, and will conduct $\sim$50 close flybys of Europa from a Jovian orbit while sampling any plumes, mapping the ice shell, and constraining the ocean. Image credit: NASA/JPL-Caltech.
```

In the early 2030s, two complementary missions will arrive at Jupiter to explore the icy Galilean moons.
NASA's **Europa Clipper** is dedicated to Europa, performing $\sim$50 close flybys from Jovian orbit to characterise the ice shell, subsurface ocean, and active plumes ({numref}`fig:europa_clipper`) {cite:p}`HowellPappalardo2020`.

ESA's **JUICE** characterises the broader Jovian satellite system, performing multiple flybys of Europa, Callisto, and Ganymede before entering orbit around Ganymede in 2034 {cite:p}`Grasset2013`.
Operating simultaneously in the Jovian system during the mid-2030s enables cross-calibration of magnetic and plasma measurements across the icy Galilean moons.

### Dragonfly to Titan

Dragonfly, scheduled for launch in 2028 and arrival in 2034, will use a **rotorcraft** (a propelled aerial vehicle) to hop tens of kilometres across Titan's Selk crater region {cite:p}`Lorenz2018`.
Impact heat at Selk crater briefly generated liquid water that transformed organic molecules, providing an analogue for prebiotic chemistry on Earth.

Dragonfly's mass spectrometer detects organic molecules at concentrations far lower than Cassini's instrument, while its mobility enables sampling across distinct geological settings.
The mission investigates the nature and complexity of this organic chemistry.

### The Voyager legacy

Voyager 1 and 2 were launched in 1977; only Voyager 2 visited Uranus (1986) and Neptune (1989), while Voyager 1 left the ecliptic after its 1980 Saturn flyby.
Both spacecraft operate in the interstellar medium.
Declining power, however, is expected to end contact around 2030.
Voyager 2 flyby data continue to be reanalysed with modern techniques, yielding new discoveries about ice giant dynamics, composition, and magnetospheres.

The lesson of Voyager is twofold.
First, the scientific return from a **flyby** (a single short visit) is finite and cannot substitute for sustained investigation.
Ice giant knowledge is 35 years out of date.
Gas giant knowledge, by contrast, has been continuously refreshed by Galileo, Cassini, Juno, and JWST.
Second, data from a well-designed mission continue to yield new science when combined with new theoretical tools and laboratory experiments.
A single mission to the ice giants in the 2030s could anchor science for the rest of the twenty-first century.

### Future ice giant missions

The 2022 US Planetary Science Decadal Survey identified a **Uranus orbiter and probe** (a mission combining an orbiter and atmospheric entry probe) as the highest-priority flagship mission for the 2030s {cite:p}`NationalAcademies2022`.
Launch in the early 2030s with a Jupiter gravity assist would reach Uranus in the late 2030s or early 2040s to measure deep noble gas, isotopic, and molecular composition.

A Neptune orbiter is currently of lower priority.
This is because gravity assist launch windows are less favourable, and Triton represents a different scientific target.
Either mission would constrain the deep interior, magnetic field, ring system, and moons, advancing our understanding of a planetary class that statistically dominates the sub-Jovian exoplanet population.

## Summary and takeaways

- **Gas giants and ice giants form a compositional continuum**, from the H/He-dominated Jupiter and Saturn to the ice-dominated Uranus and Neptune; the sequence records the timing of core formation, the available disk gas, and the migration history.
- **Both gas giants now appear to host extended, dilute heavy-element distributions** rather than compact cores, a major reinterpretation driven by Juno (Jupiter) and Cassini Grand Finale + ring seismology (Saturn). The fuzzy core picture has direct implications for how the giants formed and evolved.
- **Saturn's rings are young and transient**, with current best estimates of $\sim$100 Myr age and a comparable remaining lifetime. They are not a permanent feature of Saturn but a phase in its evolution that we happen to observe.
- **The Galilean moons span a remarkable diversity**: tidally heated and volcanic Io, ocean-bearing Europa, dynamo-generating Ganymede, and ancient, partially differentiated Callisto. Together with Titan, Enceladus, and Triton, they offer a wider variety of geological and potentially habitable environments than the inner rocky planets.
- **The ice giants are the most under-explored planets** in the solar system; everything we know in detail about Uranus and Neptune comes from single 1980s flybys. A dedicated orbiter mission is overdue and is the top recommendation of the 2022 US Planetary Science Decadal Survey.
- **The Roche limit** explains why rings exist where they do and why small bodies cannot coalesce close to their host planet. Applied to Saturn it predicts the outer edge of the A ring to within $\sim$10%.
- **The exploration frontier is extraordinary**: Juno's extended mission, JUICE, Europa Clipper, Dragonfly, and a future Uranus orbiter will collectively transform outer solar system science between now and 2045.

## References

```{bibliography}
:filter: docname in docnames
```
