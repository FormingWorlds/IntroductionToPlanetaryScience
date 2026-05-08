(lecture09)=
# Lecture 9: Rocky Planets, Earth & Venus

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe Earth's unique properties as a reference planet, explain how Venus diverged from Earth despite similar bulk composition and size, apply the Simpson-Nakajima runaway greenhouse limit, and evaluate the role of water loss history, tectonic regime, and the carbonate-silicate cycle in comparative habitability.
```

```{seealso}
**Slides:** [Download Lecture 9 (PDF)](../_static/slides/lecture09.pdf)
```

Earth and Venus are nature's best controlled experiment in comparative planetology.
They formed from the same nebular reservoir within roughly $0.3$ AU of each other, contain similar bulk inventories of silicate, iron, and volatile elements, and have masses and radii within $20\%$ of each other.
Yet their present-day surface conditions could not be more different.
Earth is wet, geologically active, magnetically shielded, and inhabited; Venus is dry, encased in a $92$ bar carbon-dioxide atmosphere at a surface temperature of $737$ K, and the only one of the rocky planets without a global magnetic field.
Identifying what set these two nearly identical starting points on such radically different evolutionary paths is the central question of this lecture.
This lecture works through that question in three parts.
Part 1 reviews Earth as a reference planet, Part 2 surveys Venus as the alien twin, and Part 3 brings the comparison together to extract the underlying physics.
The blackboard derivation in the middle introduces the Simpson-Nakajima runaway greenhouse limit, a thermodynamic boundary in phase space that, once crossed, makes the divergence essentially irreversible.

```{figure} figures/lammer2018_venus_earth_mars_accretion.avif
:name: fig:lammer-accretion
:width: 60%
:align: center

Schematic accretion histories of **Venus** (top), **Earth** (middle), and Mars (bottom) during the first $\sim$110 Myr of the Solar System.
Each panel sketches the buildup from undifferentiated planetesimals through differentiated planetary embryos to the final magma-ocean stage.
Volatile species ($\mathrm{H_2O}$, $\mathrm{CO_2}$, noble gases) outgas from the interior to form a primary steam-rich atmosphere; their fate during the cooling of the magma ocean determines the long-term volatile inventory of each planet.
Reproduced from {cite:t}`Lammer2018`.
```





## Part 1: Earth as reference

### Earth's bulk properties and what makes it habitable

Earth is the third planet from the Sun, with a semimajor axis of $1$ AU, a mass of $\Mearth = 5.97 \times 10^{24}$ kg, and an equatorial radius of $\Rearth = 6378$ km.
Its mean density is $5.51$ g/cm$^3$, the highest of any planet in the Solar System, indicating a strongly differentiated interior with a metallic iron-nickel core ({ref}`lecture08`) {cite:p}`Dziewonski1981,NASAEarthFactSheet`.
Its dimensionless moment of inertia factor $C/MR^2 = 0.331$ confirms the strong central concentration of mass and is a direct consequence of having an iron core that occupies roughly $17\%$ of the planet's volume but $32\%$ of its mass.
The surface conditions are easy to memorise: a global mean surface temperature of $T_s \approx 288$ K, a mean atmospheric pressure of $P_s = 1.013$ bar, and an atmospheric composition dominated by molecular nitrogen ($78\%$ $\mathrm{N_2}$) and oxygen ($21\%$ $\mathrm{O_2}$), with trace species (argon, water vapour, $\mathrm{CO_2}$) making up the remainder.

These bulk numbers, taken on their own, are unremarkable.
What makes Earth distinctive is the combination of three properties that, together, are unique to Earth in the Solar System today: an active mobile-lid plate tectonic regime, a global biosphere, and persistent liquid surface water covering roughly $71\%$ of the planet.
None of the other rocky planets, no moon, and no dwarf planet has even one of these features today; only Earth has all three.
The deep insight from comparative planetology is that **the three are coupled**.
Plate tectonics requires hydration of the lithosphere by liquid water to weaken the rocks enough that subduction can occur ({ref}`lecture07`); the biosphere has set and maintained the atmospheric balance of $\mathrm{O_2}$ and $\mathrm{CO_2}$ for the last $\sim$2.4 billion years {cite:p}`Lyons2014`; and the persistence of liquid water on $4$-Gyr timescales is in turn stabilised by the carbonate-silicate cycle ({ref}`lecture06`), a negative feedback that requires both volcanic outgassing of $\mathrm{CO_2}$ and silicate weathering on a wet surface {cite:p}`Walker1981`.
The three legs of the tripod hold each other up.
Remove any one and the system collapses.
This coupling is the essential reason Earth has remained habitable for billions of years and the essential reason we suspect Venus, lacking all three legs today, lost the configuration early.

### Plate tectonics in action

We covered the dynamical basis of mantle convection and the surface expression of mobile-lid tectonics in {ref}`lecture07`.
Here we recap only the elements that matter for the comparison with Venus.
Earth's lithosphere is divided into roughly a dozen major rigid plates that move horizontally at speeds of order $1\text{--}10$ cm/yr over an underlying ductile asthenosphere.
New oceanic crust is created at mid-ocean ridges by partial melting of the upwelling mantle, and old oceanic crust is consumed at subduction zones, where one plate descends back into the mantle beneath another.
The result is that no oceanic crust on Earth is older than $\sim$200 Myr, despite the planet itself being $4.54$ Gyr old; oceanic lithosphere is the most short-lived component of the solid Earth, recycled completely roughly twenty times over the planet's history.
Continental crust, by contrast, is buoyant relative to the mantle, resists subduction, and contains rocks as old as $4.0$ Gyr.

For the Earth-Venus comparison, the key role of plate tectonics is climatological, not just geological.
Subduction is the **return leg of the carbon cycle**.
$\mathrm{CO_2}$ released to the atmosphere by volcanism reacts with silicate minerals in the presence of liquid water to form carbonate sediments on the seafloor; these are subsequently subducted into the mantle, where the carbon is partly returned to the deep interior and partly recycled back to the atmosphere through arc volcanism over hundreds of millions of years {cite:p}`Walker1981,KrissansenTotton2018`.
The cycle's timescale to equilibrate atmospheric $\mathrm{CO_2}$ in response to a perturbation is $\sim$0.5 Myr {cite:p}`Walker1981`.
Without an active subduction system, the sink half of the cycle stops working, and the carbon released from the interior accumulates in the atmosphere indefinitely.
Holding this thought is essential for understanding Venus, where there is no observed subduction and no observed carbonate sink.

```{figure} figures/honing2021_carbon_cycle_diagram.avif
:name: fig:honing-carbon-cycle
:width: 85%
:align: center

Schematic of the carbon cycle on a stagnant-lid Venus from {cite:t}`Honing2021`.
**Left:** the three carbon reservoirs (mantle, crust, atmosphere) are coupled by mantle degassing (volcanism), surface weathering of fresh basaltic crust, and decarbonation of buried carbonate when the crust heats up.
**Right:** the destabilising positive feedback loop. Increasing surface temperature shifts the geotherm upward, which pushes the decarbonation isotherm to *shallower* depth in the crust, releasing buried $\mathrm{CO_2}$ to the atmosphere and raising the surface temperature further. Without subduction, there is no return leg to the mantle to break the loop.
Reproduced from {cite:t}`Honing2021`.
```

### Earth's magnetic field and its consequences

Earth has a global, dipole-dominated magnetic field generated by convection in the liquid outer core, with surface field strengths in the range $25\text{--}65$ microtesla and a dipole tilt of about $11^\circ$ from the geographic axis.
The geodynamo has been continuously active for at least $3.4$ Gyr, on the basis of palaeomagnetic measurements of single zircon crystals.
We discussed the physics of the dynamo mechanism in {ref}`lecture04`; what matters here is its consequences at the planetary surface and for atmospheric escape.

The magnetosphere deflects most of the solar wind around the planet, creating a teardrop-shaped cavity that extends to roughly $10\, \Rearth$ on the dayside and many tens of $\Rearth$ in the magnetotail on the nightside.
Trapped energetic particles populate the Van Allen radiation belts, but at the surface the geomagnetic field reduces the atmospheric ionising-radiation dose by orders of magnitude relative to what would be experienced on an unshielded planet.
More importantly for long-term planetary evolution, the magnetosphere suppresses several pathways of atmospheric loss: ion-pickup escape, in which atmospheric ions are accelerated by the solar-wind motional electric field, is essentially eliminated for the upper-atmospheric region magnetically connected to closed field lines.
Hydrogen escape from Earth still occurs, by Jeans escape and polar wind, but at rates many orders of magnitude lower than the loss rates that have desiccated Mars (which lost its dynamo around $4.1\text{--}3.9$ Ga; {ref}`lecture10`) and that may have helped strip Venus of its water during periods of intense solar EUV radiation in the early Solar System {cite:p}`Lammer2018`.
The contrast with Venus, which has no detectable internal magnetic field today, is stark, and we will return to it in Part 2.

### The hydrosphere and cryosphere

Earth's surface water inventory is dominated by the oceans, which hold $1.34 \times 10^{21}$ kg of water (about $97\%$ of the total) at an average depth of $3.7$ km.
Polar ice caps, mountain glaciers, sea ice, and permafrost together (the **cryosphere**) account for another $\sim$2%, and groundwater, lakes, rivers, and atmospheric vapour collectively contribute the remaining $\sim$1%.
Spreading the oceans evenly over the entire surface of the planet would give a global equivalent water layer of about $2.7$ km thickness; this is the natural unit for comparing total water inventories across planets.

The thermohaline circulation (driven by gradients in temperature and salinity) and the wind-driven surface circulation together transport heat poleward, smoothing the equator-to-pole temperature gradient and stabilising the climate against local instabilities.
Sea ice and continental ice exhibit the **ice-albedo feedback** that we covered in {ref}`lecture06`: ice has a much higher reflectivity than open ocean or bare ground, so growing ice cools the climate further and shrinking ice warms it.
This feedback is positive (it amplifies perturbations in either direction), and it played the central role in the Snowball Earth glaciations described below.

Ocean chemistry is dominated by the carbonate buffer system: dissolved $\mathrm{CO_2}$ exists in equilibrium with carbonate ($\mathrm{CO_3^{2-}}$) and bicarbonate ($\mathrm{HCO_3^-}$) ions, with a present-day surface ocean $\mathrm{pH}$ of about $8.1$.
This buffer keeps the ocean mildly alkaline and provides the chemical machinery for the carbonate-silicate cycle to operate.
The Urey reaction, the textbook prototype for the silicate weathering sink, is a simplification of the actual mineral chemistry but captures the essential mass balance: silicate rocks plus water plus atmospheric $\mathrm{CO_2}$ produce dissolved bicarbonate, which precipitates as carbonate sediments on the seafloor.

```{figure} figures/lammer2018_carbonate_silicate.avif
:name: fig:lammer-carbsil
:width: 75%
:align: center

Cartoon of the **carbonate-silicate cycle** on a planet with active plate tectonics.
Atmospheric $\mathrm{CO_2}$ dissolves in rainwater to form weak carbonic acid, which weathers continental silicates into bicarbonate ions; rivers transport these to the ocean, where they are precipitated as carbonate rocks; subduction then returns the carbon to the mantle.
Volcanism completes the cycle by outgassing fresh $\mathrm{CO_2}$.
On geological timescales (of order $0.5$ Myr), this cycle stabilises the surface temperature against perturbations.
Reproduced from {cite:t}`Lammer2018`.
```

### Earth's climate system

We covered the foundations of planetary energy balance and the greenhouse effect in {ref}`lecture05` and the dynamics of clouds, weather, and climate feedbacks in {ref}`lecture06`.
Here we collect only what is needed to set up the Venus comparison.
The present-day Earth absorbs about $240$ W/m$^2$ of incoming solar radiation (after accounting for the planetary albedo of $\sim$0.30) and emits the same average flux back to space in the thermal infrared.
Without an atmospheric greenhouse, the equilibrium surface temperature would be about $255$ K, well below the freezing point of water.
The natural greenhouse effect of water vapour, $\mathrm{CO_2}$, methane, and other trace gases warms the surface by about $33$ K to its observed value of $288$ K.

A persistent puzzle is the **faint young Sun problem**: standard stellar evolution models predict that the Sun was about $30\%$ less luminous at $4.4$ Ga than today, which would have led to a frozen Earth surface for the first half of the planet's history if greenhouse forcing had been the same as now.
The geological record tells the opposite story: there is good evidence for liquid water at the surface of Earth from at least $4.3$ Ga onwards, including detrital zircons with hydrothermal alteration signatures {cite:p}`Feulner2012,Zahnle2007`.
The standard resolution is a higher concentration of greenhouse gases (most likely $\mathrm{CO_2}$ and possibly $\mathrm{CH_4}$) in the early atmosphere, drawn down over time as the Sun brightened, by silicate weathering and biological feedbacks.

```{figure} figures/zahnle2007_solar_evolution.avif
:name: fig:zahnle-solar
:width: 75%
:align: center

Solar luminosity (left axis, solid black curve) and EUV/X-ray flux (right axis, coloured curves) over the first $\sim$5 Gyr after the Sun reached the main sequence, normalised to present values.
The bolometric luminosity has risen by about $30\%$ since $4.5$ Ga, while the EUV and X-ray fluxes have dropped by factors of $10$--$1000$ from the young, magnetically active Sun.
The faint-young-Sun problem is the apparent contradiction between this lower bolometric flux and geological evidence for liquid water on early Earth.
Reproduced from {cite:t}`Zahnle2007`.
```

```{figure} figures/charnay2013_archean_temperature.avif
:name: fig:charnay-archean
:width: 70%
:align: center

Three-dimensional general-circulation model results for the global mean surface temperature of the Archean Earth between $3.8$ Ga and $2.5$ Ga, from {cite:t}`Charnay2013`.
Curves show solutions for three atmospheric compositions: $0.9$ mbar $\mathrm{CO_2}$ with $0.9$ mbar $\mathrm{CH_4}$ (blue), $10$ mbar $\mathrm{CO_2}$ with $2$ mbar $\mathrm{CH_4}$ (orange), and $0.1$ bar $\mathrm{CO_2}$ with $2$ mbar $\mathrm{CH_4}$ (red); solid lines include methane and dashed lines omit it.
The dotted green line marks the freezing point of water.
A few mbar of $\mathrm{CO_2}$ together with trace methane is marginal at $3.8$ Ga but warms by $3$ Ga, while $\sim$0.1 bar of $\mathrm{CO_2}$ together with trace methane comfortably resolves the faint-young-Sun problem at all three epochs.
Reproduced from {cite:t}`Charnay2013`.
```

On shorter timescales, **Milankovitch cycles** in Earth's orbit (eccentricity, axial obliquity, and the precession of the equinoxes, with periods of $\sim$100 kyr, $41$ kyr, and $19\text{--}23$ kyr respectively) modulate the seasonal and latitudinal distribution of solar insolation and pace the Pleistocene glacial-interglacial cycles of the last $\sim$2.6 Myr.
These are the cycles imprinted on the Vostok and EPICA ice cores, with surface temperature swings of $\sim$8 K between glacial maxima and interglacials.
Crucially, **Earth's climate has been remarkably stable on long timescales** in the sense that liquid water has persisted continuously for at least $4$ Gyr.
But "stable" does not mean "constant".
Surface temperatures have ranged from $\sim$240 K during deep Snowball Earth episodes to perhaps $\sim$300 K during Phanerozoic hothouses, and biosphere composition has changed dramatically (from the Archean anoxic ocean through the Great Oxidation Event to the present oxic atmosphere).
The climate system explores a wide range of states, but the carbonate-silicate thermostat keeps the surface within the liquid-water window.
This is a key conceptual point we will come back to when comparing with Venus.

### Snowball Earth episodes

Earth came perilously close to a different climate failure mode (ice rather than heat) during the Cryogenian period.
At least two global glaciations are well documented, the **Sturtian** (lasting from roughly $717$ Ma to $660$ Ma) and the **Marinoan** (around $645$ Ma to $635$ Ma), and a third, the **Huronian** glaciation around $2.4$ Ga, may have been similarly extensive {cite:p}`Hoffman1998,Hoffman2017`.
The geological evidence is striking: glacial diamictites (poorly sorted glacial deposits) are found at palaeolatitudes within $10^\circ$ of the equator, banded iron formations re-appear in the rock record after a billion-year absence, and the glacial deposits are capped by thick "cap carbonates" that record an abrupt return to high-$\mathrm{CO_2}$, high-temperature greenhouse conditions immediately after deglaciation.

The mechanism is straightforward in concept.
Once the polar ice caps grow to roughly $30^\circ$ latitude, the ice-albedo feedback runs away: the increased reflectivity cools the climate, more ice forms, which cools the climate further, and so on, until ice covers most or all of the ocean and the surface temperature drops to $\sim$240 K.
During the snowball state, silicate weathering essentially shuts down (because the surface is frozen), but volcanism continues to outgas $\mathrm{CO_2}$ at roughly its normal rate.
Atmospheric $\mathrm{CO_2}$ accumulates over $\sim$10 Myr (Hoffman2017's preferred number from coupled hysteresis modelling), until the greenhouse forcing eventually overcomes the ice-albedo cooling, the ice melts catastrophically (over only $\sim$2 kyr once the tropical ocean reopens), and the planet swings into a hothouse state.
The cap carbonates record the rapid drawdown of the post-snowball $\mathrm{CO_2}$ excess by extremely intense weathering of newly exposed silicate surfaces.

The Snowball Earth episodes are pedagogically important for two reasons.
First, they show that Earth's carbonate-silicate thermostat can rescue the planet from extreme cold states as well as warm ones; the Walker feedback ({ref}`lecture06`) is symmetric in this sense.
Second, they show that Earth came close to a catastrophic failure mode different from that of Venus.
Where Venus failed by overheating, Earth nearly failed by freezing.
That Earth survived both possibilities is a measure of how robust the carbonate-silicate feedback is, provided liquid water and active volcanism both persist.
There is also a tantalising correlation with biological evolution: the first multicellular animals appear in the fossil record shortly after the Marinoan deglaciation, and some authors have argued that the dramatic environmental swings of the snowball episodes drove evolutionary innovation.

### Earth today in its long-term context

To set up the Venus comparison properly, it helps to look at present-day Earth in the same physical language we will use for Venus.
Anthropogenic climate change is best understood as a planetary-scale forcing experiment in real time, and the physics is the same as for any other greenhouse perturbation.

The atmospheric concentration of $\mathrm{CO_2}$ has risen from a pre-industrial value of about $280$ ppm to over $420$ ppm in $2024$, a level higher than at any time in the last $\sim$3 Myr based on direct ice-core records {cite:p}`NOAACO2,IPCC2021`.
The current rate of change, roughly $2\text{--}3$ ppm/yr, is approximately $100$ times faster than the natural rate of $\mathrm{CO_2}$ rise during deglaciation at the end of the last ice age.
The net anthropogenic radiative forcing (greenhouse gases plus aerosols) is about $2.7$ W/m$^2$ at the top of the atmosphere {cite:p}`IPCC2021`.
The observed surface temperature response, about $1.1$ K of warming since the late nineteenth century {cite:p}`IPCC2021`, is consistent with what radiative-convective climate models predict for this forcing once ocean heat uptake is accounted for.

```{figure} figures/lyons2014_oxygen_history.avif
:name: fig:lyons-oxygen
:width: 90%
:align: center

Evolution of Earth's atmospheric oxygen content through time, on a logarithmic scale of $p\mathrm{O_2}$ relative to present atmospheric level (PAL).
The atmosphere remained essentially anoxic ($p\mathrm{O_2} < 10^{-5}$ PAL) for the first $\sim$2 Gyr of Earth history, then rose abruptly during the **Great Oxidation Event** at $\sim$2.4 Ga, plateaued at intermediate values through the mid-Proterozoic, and rose again to near-modern levels in the Neoproterozoic and Phanerozoic.
The two-stage rise reflects the gradual buildup of the photosynthetic biosphere and shifting redox balance with the deep ocean and crust.
Reproduced from {cite:t}`Lyons2014`.
```

The crucial point for comparative planetology is that the carbonate-silicate thermostat will not save us on human timescales.
Silicate weathering equilibrates atmospheric $\mathrm{CO_2}$ on a timescale of order $\sim$0.5 Myr, which is roughly five orders of magnitude longer than the duration of the current anthropogenic perturbation.
Earth's climate system is responding to a well-understood radiative forcing on a timescale set by ocean heat uptake (decades to centuries) and ice-sheet response (centuries to millennia), not by the geological feedbacks that have buffered deep-time climate.
A second consequence of the rapid $\mathrm{CO_2}$ rise is **ocean acidification**: dissolution of atmospheric $\mathrm{CO_2}$ has raised seawater $\mathrm{H^+}$ concentrations by about $30\%$ since pre-industrial times, dropping the surface ocean $\mathrm{pH}$ from about $8.2$ to $8.1$.
The point is not political but physical: the same radiative-transfer machinery that warms Venus to $737$ K, given enough $\mathrm{CO_2}$, is operating on Earth right now, and the long-term geological feedbacks that bound Earth's climate over $4$ Gyr operate too slowly to compensate for it on timescales relevant to human civilisation.

### The biosphere's geological footprint

Although this lecture is mainly about physical and geological evolution, the biosphere has rewritten the surface chemistry of Earth in ways that we cannot ignore when comparing with Venus.
The most spectacular biotic event is the **Great Oxidation Event** at $\sim$2.4 Ga, when atmospheric $\mathrm{O_2}$ rose from negligible Archean levels (pre-GOE $p_{\mathrm{O_2}} < 10^{-5}$ atm) to roughly $0.1\text{--}1\%$ of modern values in the mid-Proterozoic plateau, with a transient overshoot to $10\text{--}20\times$ modern during the Lomagundi excursion at $2.3\text{--}2.1$ Ga {cite:p}`Lyons2014`.
The mechanism is oxygenic photosynthesis by cyanobacteria, which had already been present for several hundred million years before the event itself.
The trigger for the rise is debated (changes in oxygen sinks, in continental weathering, in volcanic outgassing redox state, or in the burial of organic carbon are all candidates), but the consequences are unmistakable in the rock record: banded iron formations disappear, redbeds appear, and the biosphere acquires the oxidising redox state that has dominated ever since.
A second oxygenation step in the late Neoproterozoic raised $\mathrm{O_2}$ to near-modern values just before the Cambrian explosion of complex animal life.


Carbonate platforms, formed primarily by the calcification of marine organisms over the past $\sim$540 Myr, represent a substantial planetary $\mathrm{CO_2}$ sink.
On Earth, the total carbon stored in surface and crustal reservoirs (overwhelmingly in marine carbonate sediments, with smaller contributions from organic-rich shales and the dispersed carbon in oceanic crust) is on the order of $10^{20}$ kg, equivalent to a $\mathrm{CO_2}$ partial pressure of order $\sim 100$ bar if it were all returned to the atmosphere {cite:p}`Catling2017`.
This is a striking number, because it is comparable in order of magnitude to the $92$ bar of $\mathrm{CO_2}$ in the present-day Venus atmosphere.
The arithmetic is suggestive but not exact: it tells us that Earth and Venus probably acquired comparable carbon inventories during accretion, and that the difference in atmospheric carbon today is largely due to where the carbon ended up (in carbonates on Earth, in the atmosphere on Venus) rather than how much was originally present.
We will return to this in Part 3.
The connection between the biosphere and biosignatures (the spectroscopic signatures of life that future telescopes might use to characterise exoplanets) is taken up explicitly in {ref}`lecture13` and {ref}`lecture14`.


## Part 2: Venus, the alien twin

### Venus overview: why it is the twin and why it is not

Venus is the second planet from the Sun, with a semimajor axis of $0.723$ AU, a mass of $0.815\, \Mearth = 4.87 \times 10^{24}$ kg, an equatorial radius of $0.950\, \Rearth = 6052$ km, and a mean density of $5.24$ g/cm$^3$ {cite:p}`NASAVenusFactSheet`.
By every bulk measure, Venus is Earth's near-twin: a similar size, a similar density (suggesting a similar bulk composition of silicate mantle and iron core), and a formation distance only $0.28$ AU closer to the Sun than Earth.
First-order theory says it should look much like Earth.

It does not.
The contrast is dramatic on every observable axis.
The surface pressure on Venus is $92$ bar, about $90$ times the pressure at the bottom of Earth's atmosphere, comparable to the pressure under $\sim$1 km of water on Earth.
The surface temperature is $737$ K, hot enough to melt lead and well above the temperature at which any organic chemistry survives.
The atmospheric composition is almost entirely $\mathrm{CO_2}$ ($96.5\%$), with $\mathrm{N_2}$ ($3.5\%$) as the only major minor constituent and trace amounts of $\mathrm{SO_2}$, water vapour, and noble gases.
The cloud layers are not water clouds but **sulfuric acid** ($\mathrm{H_2SO_4}$) droplets, formed by photochemistry of $\mathrm{SO_2}$ and water vapour at altitudes between roughly $48$ and $70$ km.
Venus rotates retrograde (against the orbital direction) with a sidereal rotation period of $243.0$ Earth days, longer than its orbital period of $224.7$ Earth days, so a single solar day on Venus lasts $116.75$ Earth days.
There is no detectable global magnetic field; the upper limit on any internal dipole is roughly $10^{-5}$ of Earth's surface field {cite:p}`Smrekar2018`.
And the present surface water inventory is staggeringly small: roughly $20\text{--}30$ ppm of water vapour in the lower atmosphere, equivalent to a global ocean about $1$--$3$ cm deep if it were condensed onto the surface.
For comparison, Earth's water inventory is about $2.7$ km of global equivalent depth, or roughly $10^5$ times more.

Each of these contrasts deserves explanation, and that is the project of this part of the lecture.

```{figure} figures/widemann2023_three_missions_render.avif
:name: fig:venus-render
:width: 70%
:align: center

Artist's rendering of three new missions in the **Venus exploration decade** of the 2030s, against a global view of the planet from Akatsuki UV imaging.
NASA's VERITAS (left, top) will provide high-resolution radar topography and near-infrared surface emissivity; NASA's DAVINCI (right, top) will release an atmospheric descent probe; and ESA's EnVision (below) will provide synthetic-aperture radar mapping, atmospheric spectroscopy, and subsurface sounding.
Together these three missions will revolutionise Venus science, the first new orbital missions since Venus Express (2006--2014) and the first in-situ probes since Vega in 1985.
Reproduced from {cite:t}`Widemann2023`.
```

### Exploring Venus: the mission history

The history of Venus exploration breaks neatly into three eras.
The first era, from $1962$ to $1985$, was dominated by Soviet Venera and Vega missions and produced essentially all of the in-situ measurements we have today.
Mariner 2 in $1962$ was the first successful interplanetary flyby of any planet; it confirmed the high surface temperature inferred from earlier ground-based microwave observations and ruled out the possibility (popular until then) of a habitable Venusian surface beneath thick clouds.
Venera 4 in $1967$ was the first probe to enter the atmosphere of another planet and report in-situ measurements.
Venera 7 in $1970$ was the first lander to transmit data from the surface of another planet.
Venera 9 in $1975$ returned the first surface images, showing a fractured rocky landscape under sulfuric-acid haze.
Venera 13 in $1982$ took colour panoramas and analysed the surface chemistry, finding basaltic compositions consistent with volcanic plains.
The Vega missions in $1985$ deployed instrumented balloons that floated through the cloud layer for $\sim$2 days, a unique and to-date unrepeated measurement of cloud-level dynamics.

The second era, the orbital radar era, was dominated by NASA's Pioneer Venus Orbiter ($1978$--$1992$) and Magellan ($1990$--$1994$).
Magellan in particular was a transformational mission: it mapped $\sim$98% of the Venusian surface at $\sim$100 m horizontal resolution using synthetic-aperture radar, providing the global topographic and morphological dataset that all subsequent Venus geology has been built on.
Pioneer Venus also carried an atmospheric probe whose mass spectrometer measured the noble gas isotopic ratios that anchor much of what we know about Venus' atmospheric history.

The third era, after a long gap, began with ESA's Venus Express ($2006$--$2014$) and JAXA's Akatsuki ($2015$--present).
Venus Express measured atmospheric dynamics, polar vortices, thermal emission from the surface in near-IR spectral windows, and the present-day rates of hydrogen and oxygen escape to space.
Akatsuki has produced ongoing UV cloud imaging and infrared maps of the lower atmosphere.
Critically, **no orbital mission flew between 1994 and 2006**, and **no in-situ probe has visited Venus since Vega in 1985**.
The Venus dataset is therefore old by the standards of modern planetary science, and many of the open questions are direct consequences of this gap.
Three new orbiters and one or more probes are planned for the 2030s (NASA's VERITAS and DAVINCI, and ESA's EnVision), forming the Venus decade we discuss at the end of Part 3.

### Venus surface morphology

The single most diagnostic observation about Venus' surface is its **hypsometry**: the global statistical distribution of surface elevations.
Earth has a famously **bimodal** hypsometry, with two distinct populations of surface elevations corresponding to ocean basins (around $-4$ km) and continental crust (around $0$ to $+1$ km), separated by a sharp transition at the continental margins.
This bimodality is a direct fingerprint of plate tectonics: the two distinct crustal types (basaltic oceanic crust and granitic continental crust) have different densities, undergo different histories, and reach different isostatic equilibria.
Venus, by contrast, has a **unimodal** hypsometry, a single broad peak with a narrow tail to higher elevations.
There is no equivalent of Earth's continent-ocean dichotomy.
This is the most direct, observation-based argument that Venus does not have plate tectonics in the Earth-like sense {cite:p}`Smrekar2018`.

```{figure} figures/smrekar2018_earth_venus_topography.avif
:name: fig:earth-venus-topo
:width: 75%
:align: center

Global topographic maps of **Earth** (top), **Venus** (middle, from Magellan radar altimetry), and the gravity-derived geoid of Venus (bottom), all displayed at the same horizontal resolution and on the same colour scale.
Earth's bimodal pattern (deep ocean basins vs. continents) is conspicuously absent on Venus, which shows broad volcanic plains, scattered highlands, and a narrow elevation range.
Reproduced from {cite:t}`Smrekar2018`.
```


The Venus surface is dominated by **volcanic plains**, which cover about $80\%$ of the planet, formed from successive flood-basalt eruptions over hundreds of millions of years.
Embedded in these plains are several distinctive terrain types unique to Venus or unusually prominent here:

**Tesserae** are the oldest mapped terrain on Venus, characterised by intersecting sets of ridges and grooves that record multiple episodes of compressional and extensional deformation.
They form roughly $8\%$ of the surface, occur as elevated plateaus (Aphrodite Terra, Ovda Regio, Thetis Regio), and are stratigraphically older than the surrounding plains.
The compositional nature of tessera material is debated: VIRTIS infrared emissivity measurements from Venus Express suggested that some tessera regions have higher emissivity in the $1$-$\mu$m near-infrared window than the surrounding plains, which is consistent with felsic (more silicic, possibly granitic) compositions and would point to ancient water-rock interaction {cite:p}`Widemann2023`.
If confirmed, this would imply that early Venus had liquid surface water, which is a cornerstone observational test for the wet-Venus scenarios discussed below.
A direct surface measurement by a future lander (or near-IR spectroscopy from VERITAS) is needed to settle the question.

**Coronae** are circular volcano-tectonic features unique to Venus, ranging in diameter from about $100$ to $1000$ km.
They are generally thought to be the surface expression of mantle plumes or upwellings, with a complex annular structure of fractures, raised rims, and central volcanic edifices.
The largest coronae occupy the same diameter range as oceanic large igneous provinces on Earth, and they may be a distinctive expression of stagnant-lid volcanism in which heat escapes through localised plume upwellings rather than through global plate-tectonic recycling.
Recent analysis of Magellan gravity data has identified coronae that appear to overlie active mantle plumes today, suggesting that some are still volcanically active.

```{figure} figures/widemann2023_venus_geological_terrains.avif
:name: fig:venus-terrains
:width: 95%
:align: center

Global geological-terrain map of Venus from {cite:t}`Widemann2023` Fig. 15, overlaid on a Magellan radar base. Coloured polygons are the Regions of Interest (RoIs) defined in the ESA EnVision Science Operations Reference Scenario; together they cover roughly 30% of Venus's surface and span the major terrain classes: **plains** (light green), **tessera** highlands (tan), **deformed terrain** (pale yellow), **rift zones** (red), **Artemis chasma** (purple), and **craters** (grey). Named regional landmarks (Maxwell Montes, Fortuna Tessera, Ishtar Terra, Beta Regio, Aphrodite Terra, Alpha Regio, and others) are labelled. Terrain classification after {cite:t}`IvanovHead2015`; reproduced from {cite:t}`Widemann2023`.
```

**Impact crater density** on Venus is low, corresponding to a global average crater retention age of $150\text{--}250$ Myr in recent reanalyses {cite:p}`Smrekar2018`, with older crater-counting estimates extending to $300\text{--}1000$ Myr {cite:p}`Widemann2023`.
This is a striking number: it implies that the surface of Venus was effectively wiped clean some time in the geologically recent past, and that the present surface dates from the resurfacing event rather than from accretion.
There are essentially two competing interpretations of this resurfacing.
The **catastrophic resurfacing** model (sometimes called the global lithospheric overturn model) proposes that the planet experienced a brief, planet-wide volcanic and tectonic event roughly $500$ Myr ago that resurfaced essentially all of the crust at once.
The **steady-state** model, by contrast, proposes that resurfacing has been continuous and roughly uniform over time.
The crater statistics alone cannot distinguish these decisively because the spatial distribution of craters is consistent with random within statistical uncertainty.
The latest modelling and the structural analysis of crater rims suggest that something between these two extremes (perhaps episodic regional resurfacing) is most likely {cite:p}`Smrekar2018,Widemann2023`.


### Venus interior and tectonic regime

What we know about Venus' interior structure comes almost entirely from gravity data and the rotation rate, augmented by theoretical extrapolation from Earth.
The Magellan gravity field (combined with the geoid in {numref}`fig:earth-venus-topo`) has been mapped to spherical harmonic degree $\sim$70 globally and higher locally; the long-wavelength gravity field is strongly correlated with topography on Venus, indicating that surface topography is supported in part by deep mantle density anomalies (mantle plumes and downwellings) rather than by purely flexural support of a rigid lithosphere {cite:p}`Smrekar2018`.
The strength of this gravity-topography correlation is unusual compared with Earth and points to a very different style of mantle dynamics.

The bulk composition of Venus is probably close to Earth's, given the similar bulk density once compressional effects are removed.
The presumption is that Venus has a metallic iron-nickel core of roughly Earth-like fractional size, surrounded by a silicate mantle and a basaltic crust.
But several key parameters are unknown.
We do not know whether Venus' core is fully liquid, partly solid, or fully solid, because the moment of inertia factor of Venus is not well determined from current data (the slow rotation rate makes the determination difficult).
We also do not know the present-day mantle temperature, the composition of the lower mantle, or whether there is any inner-core nucleation.
Future radio-science measurements from VERITAS and EnVision are designed to pin down the moment of inertia and the tidal Love numbers, which together would constrain the size and state of the core.

The tectonic regime of present-day Venus is **stagnant-lid**: there are no continuous plate boundaries, no observed subduction zones, and no observed seafloor-spreading equivalents.
The lithosphere appears to be a single, globally connected layer that does not subduct.
We discussed the physics of mobile- vs. stagnant-lid regimes in {ref}`lecture07`; what matters for Venus is that the choice of regime is set by a combination of mantle viscosity (which depends sensitively on water content; a dry mantle is much stiffer) and the state of the lithosphere (which can become either dry and brittle or wet and ductile).
The leading hypothesis for why Venus is in stagnant-lid mode today is that the dehydration of the mantle following the loss of surface water (which we will come to in the runaway greenhouse discussion) raised the mantle viscosity to a value at which the Earth-like mobile-lid regime cannot be sustained.
On this view, Venus may once have had Earth-like mobile-lid tectonics (when its mantle was wet), and it transitioned to stagnant lid as a consequence of losing its water.

```{figure} figures/smrekar2018_venus_tectonic_evolution.avif
:name: fig:venus-tectonic-evol
:width: 85%
:align: center

Surface temperature evolution of Venus over $\sim$4.5 Gyr from a numerical tectonic-regime model, from the bottom panel of {cite:t}`Smrekar2018`.
The boxed labels mark successive **stagnant-lid**, **mobile-lid**, **stagnant-lid**, and **episodic-lid** intervals.
The episodic-lid phase produces the resurfacing pulses inferred from present-day crater statistics; the mantle-temperature and volcanic-production-rate panels of the same model (not reproduced here) show the corresponding pulses in interior heat transport.
```

There is a related possibility, the **episodic-lid** or catastrophic-overturn model, in which the lithosphere is normally stagnant but becomes unstable on long timescales (every $\sim$500 Myr) and undergoes a brief episode of global subduction and volcanism, after which it returns to stagnant-lid behaviour.
This model is attractive because it naturally explains the resurfacing inferred from crater statistics, but it is not unique, and other models can fit the same observations.
The point is that we do not yet have the seismic, heat-flow, or detailed gravity data needed to distinguish these scenarios.
There is also no Venus seismic record of any kind: no marsquake-equivalent dataset exists for Venus, although several mission concepts (including a long-lived surface seismic station and a balloon-based atmospheric pressure-wave detector) are under consideration for future flights.

Finally, the absence of a Venusian magnetic field is consistent with several of these scenarios.
We discussed the geodynamo in {ref}`lecture04`.
For a planetary dynamo to operate, the core must be convecting, which generally requires either thermal cooling (the outer mantle must be cool enough that heat is being efficiently extracted from the core) or compositional buoyancy (an inner core is freezing, releasing light elements that drive convection in the outer core).
On Venus, the stagnant lid insulates the core from efficient cooling, slowing the heat flow out of the core and possibly preventing the core convection that would drive a dynamo.
Alternatively, Venus may simply not have an inner core nucleation, depriving it of the compositional convection that helps power Earth's dynamo.
The slow rotation rate (which sets the planet's Coriolis force and thus the geometry of dynamo flows) is not by itself fatal: theoretical models and dynamo simulations show that dynamo action can persist at much slower rotation rates than Venus.
The most likely explanation is the combination of inefficient core cooling (because of the stagnant lid) and possibly a lack of inner-core nucleation, but pinning down which factor dominates requires interior data we do not yet have.

### Venus atmosphere: structure and dynamics

The Venusian atmosphere is the most thoroughly studied non-Earth planetary atmosphere in the Solar System.
The vertical structure is well characterised down to the surface from in-situ Venera and Pioneer Venus probe data and from atmospheric occultation profiles by orbiting spacecraft.
We will not repeat the radiative-transfer derivations from {ref}`lecture05` and {ref}`lecture06`; instead we collect the key facts that distinguish Venus from Earth and motivate the runaway greenhouse derivation that follows.

The composition is overwhelmingly $\mathrm{CO_2}$ ($96.5\%$), with $\mathrm{N_2}$ ($3.5\%$) the only other major species.
Trace gases include $\mathrm{SO_2}$ at $\sim$150 ppm, water vapour at $\sim$30 ppm in the lower atmosphere (rising slightly to $\sim$80 ppm in the cloud-deck region), and noble gases (argon, neon, krypton, xenon) at concentrations that are comparable to or much higher than terrestrial values, depending on the species.
The high primordial $^{36}$Ar concentration argues that Venus has had less efficient atmospheric escape than Earth, while the low radiogenic $^{40}$Ar (only $\sim$24% of the mantle inventory has been outgassed, compared with $\sim$50% on Earth) argues that Venus has outgassed less of its mantle volatile inventory than Earth {cite:p}`Lammer2018,Widemann2023`.

The thermal profile is roughly adiabatic from the surface ($T_s = 737$ K, $P_s = 92$ bar) up to about $65$ km altitude, where the cloud tops sit and the troposphere meets the stratosphere.
The atmospheric scale height at the surface is about $16$ km, much larger than Earth's $\sim$8 km, mainly because the surface temperature is so much higher (gas molecules are more energetic), in spite of the larger mean molecular weight of $\mathrm{CO_2}$ ($M = 44$ g/mol vs $\sim 29$ g/mol for air); the scale height is a competition between these factors, and the temperature wins.
We can verify the Venus number directly from the hydrostatic scale height derived in {ref}`lecture05`:

$$
H = \frac{\kB T}{m\, g}.
$$

Plugging in $T = 737$ K, $m = 44 \times 1.66 \times 10^{-27}$ kg $= 7.30 \times 10^{-26}$ kg for $\mathrm{CO_2}$, and $g = 8.87$ m/s$^2$ gives $H \approx 1.57 \times 10^4$ m, or $\sim 16$ km.
The same formula applied to Earth's near-surface air ($T = 288$ K, $m = 4.81 \times 10^{-26}$ kg for a mean molecular weight of $29$, $g = 9.81$ m/s$^2$) gives $H \approx 8.4$ km.
The factor-of-two contrast between the two planets is set almost entirely by the temperature ratio $T_{\mathrm{Venus}} / T_{\mathrm{Earth}} \approx 2.55$, partly offset by the heavier molecule and the slightly weaker Venusian gravity.
Above the cloud tops the temperature drops with altitude through the mesosphere, then rises again in the thermosphere where solar EUV is absorbed.

The cloud system is one of the most distinctive features of Venus.
**Sulfuric acid droplets** form three vertically stacked layers between roughly $48$ and $70$ km altitude: a lower cloud deck dominated by larger particles, a middle deck of intermediate sizes, and an upper deck of smaller particles.
They are produced by photochemistry in the upper atmosphere: solar UV photolyses $\mathrm{SO_2}$ to atomic sulfur and oxygen, the products combine with water vapour to form $\mathrm{SO_3}$ and then $\mathrm{H_2SO_4}$, which condenses to form droplets.
The clouds are optically thick (the visible-band albedo is $\sim$0.77, the highest of any planet in the Solar System), and they are the effective radiating surface of the planet for visible and near-IR wavelengths.
An unidentified UV absorber (sometimes called the "blue absorber") gives the cloud tops their characteristic banded appearance in UV imagery; its identity is one of the long-standing puzzles of Venus atmospheric chemistry.
Phosphine ($\mathrm{PH_3}$) was claimed in 2020 as a possible cloud-layer trace species, with potential biological implications, but the detection has been contested and remains the subject of an active and unresolved debate that we touched on in {ref}`lecture06`.

The atmospheric circulation is dominated by **super-rotation**: the cloud-top atmosphere circles the planet in roughly $4$ Earth days, despite the solid planet rotating in $243$ Earth days.
This means that at the cloud tops, the atmosphere is moving roughly $60$ times faster than the surface beneath it, in a direction opposed to the planet's rotation.
The maintenance of super-rotation against frictional drag at the surface is one of the deep open problems of planetary atmospheric dynamics; the leading explanation involves thermal tides and planetary-scale waves transporting angular momentum upward from the lower atmosphere to the cloud-deck region.

### The runaway greenhouse and how Venus locked into it

We come to the central piece of physics in this lecture: why and how Venus' climate ended up where it is.
The blackboard derivation in the next subsection makes the argument quantitative, but it helps to state the conclusion first.

A planet with surface water and an atmospheric absorber (water vapour itself, in the simplest case) has a feedback loop: warming raises the water vapour concentration via the Clausius-Clapeyron relation, which strengthens the greenhouse effect, which warms the surface further, and so on.
On modern Earth, this feedback is bounded because the troposphere only carries water vapour up to a saturation profile that decreases with altitude, and the outgoing longwave radiation (OLR) that escapes to space rises with surface temperature roughly fast enough to balance increasing absorbed solar flux.

It is worth pausing to ask whether a textbook one-layer grey greenhouse, of the kind we built in {ref}`lecture05`, can already explain the Venus surface temperature.
In that model the surface is in radiative balance with a single optically thick atmospheric layer, which gives the well-known result

$$
T_s^4 = 2\, T_{\mathrm{eq}}^4,
\qquad
T_{\mathrm{eq}} = \left[ \frac{S\, (1-A)}{4\, \sigma} \right]^{1/4},
$$

so that $T_s = 2^{1/4}\, T_{\mathrm{eq}} \approx 1.19\, T_{\mathrm{eq}}$.
For Earth, $S_\oplus = 1361$ W/m$^2$ and $A = 0.30$ give $T_{\mathrm{eq}} \approx 255$ K and $T_s \approx 303$ K, within $\sim 15$ K of the observed $288$ K.
For Venus, $S_{\mathrm{Venus}} = 2604$ W/m$^2$ but the present cloud albedo is $A \approx 0.77$, so $T_{\mathrm{eq}} \approx 227$ K and the one-layer model predicts only $T_s \approx 270$ K.
The observed surface temperature is $737$ K, almost $500$ K hotter than the simple model allows.
The one-layer picture fails by hundreds of kelvin, and the failure is not a small correction: it tells us that Venus is not on the same equilibrium branch as Earth, and that we need a different kind of solution, in which the atmosphere is dense enough that the IR photosphere lifts far above the surface.
That is the runaway-greenhouse branch, and the next derivation makes the threshold quantitative.

But the bound is not infinite.
There is a maximum OLR that a water-rich atmosphere can radiate to space, set by the saturation vapour pressure of water at the temperature of the IR-photosphere; if the absorbed solar flux exceeds this limit, no surface temperature can balance the radiation budget, the ocean evaporates entirely, and the planet enters a **runaway greenhouse** state.
This maximum OLR is the **Simpson-Nakajima limit**.

```{figure} figures/kopparapu2013_runaway_panels.avif
:name: fig:kopparapu-runaway
:width: 80%
:align: center

Climate-model calculation of the runaway greenhouse limit and the inner edge of the habitable zone for an Earth-like planet, from {cite:t}`Kopparapu2013` Fig. 3.
Panel (a): outgoing longwave radiation (OLR) as a function of surface temperature, showing the asymptote to a maximum value of $\sim 291$ W/m$^2$ at high surface temperatures (the corresponding {cite:t}`Goldblatt2013` line-by-line calculation gives $\sim 282$ W/m$^2$; the small offset is due to the H$_2$O continuum treatment).
Panel (b): planetary albedo.
Panel (c): the ratio of stellar flux to the present solar constant required for radiative equilibrium, with the **runaway greenhouse** limit at $S_{\mathrm{eff}} = 1.06$ ($\Rightarrow$ inner habitable-zone edge at $\sim$0.97 AU for present-day solar luminosity) and the **moist greenhouse** limit at $S_{\mathrm{eff}} = 1.015$ ($\sim$0.99 AU).
Panel (d): the corresponding atmospheric water vapour mixing ratio profile at $T_s = 320$, $340$, and $360$ K.
Once $S_{\mathrm{eff}}$ exceeds the runaway threshold, no equilibrium with liquid surface water is possible.
Reproduced from {cite:t}`Kopparapu2013`.
```

```{figure} figures/goldblatt2013_olr_spectrum.avif
:name: fig:goldblatt-spectrum
:width: 446px
:align: center

Thermal-radiance spectra of an Earth-like atmosphere as a function of wavelength for surface temperatures $T_\mathrm{s} = 280, 310, 340, 370, 400$ K (bottom to top), from {cite:t}`Goldblatt2013` Fig. 3(b).
Black and red curves are two independent line-by-line model calculations; grey dotted curves show the blackbody reference at each $T_\mathrm{s}$.
As $T_\mathrm{s}$ rises from 280 K to 400 K, the H$_2$O continuum absorbs an ever-larger fraction of the thermal emission across the infrared, and the 8–14 $\mu$m atmospheric window closes.
Above $T_\mathrm{s} \sim 340$ K the integrated outgoing flux saturates at the **runaway-greenhouse asymptote** of $\sim 282$ W m$^{-2}$ (cf. {numref}`fig:kopparapu-runaway`): further surface warming no longer produces a compensating increase in emission to space.
Reproduced from {cite:t}`Goldblatt2013`.
```

In numbers, the Simpson-Nakajima limit comes out to about $280\text{--}310$ W/m$^2$, depending on details of the radiative transfer model and the assumed atmospheric composition {cite:p}`Goldblatt2013,Kasting1988`.
Earth today absorbs about $240$ W/m$^2$ of stellar flux, comfortably below the limit.
Venus, at $0.723$ AU, absorbs roughly $1.91 \times$ more stellar flux per unit area than Earth would at the top of its atmosphere; the absorbed solar flux at Venus is much higher than the Simpson-Nakajima limit, which is precisely why Venus cannot host liquid water at the surface today.
Once Venus crossed the limit some time in its history, the runaway became a one-way process: the ocean evaporated to space, water photolysed in the upper atmosphere, hydrogen escaped (preferentially over deuterium, leaving the residual D/H ratio strongly enriched), and the surface dried out permanently.
What is left is the dry, $\mathrm{CO_2}$-dominated, $737$ K hothouse we observe today.

A subtlety is that the runaway greenhouse state is a thermodynamic feature of the water phase diagram and the radiative transfer through a saturated atmosphere; it is not an artefact of any particular climate model or numerical scheme.
{cite:t}`Goldblatt2013` showed that even the most modern line-by-line radiative-transfer codes converge on a limit in the same range as the original {cite:t}`Kasting1988` and {cite:t}`Kasting1993` calculations.
The robustness of the limit across very different model assumptions is one of the strongest theoretical arguments that the runaway greenhouse on Venus was inevitable given enough solar flux.

```{figure} figures/zahnle2007_runaway_threshold.avif
:name: fig:zahnle-runaway
:width: 75%
:align: center

Surface temperature as a function of net insolation plus geothermal heat flow for a steam atmosphere over a magma ocean, from {cite:t}`Zahnle2007` (after {cite:t}`Kasting1988` and Abe \& Matsui 1988).
The radiated cooling rate is equal to the sum of absorbed sunlight and geothermal heat flow.
The plot shows the surface temperature as a function of this combined heat input for different amounts of atmospheric $\mathrm{H_2O}$ (in bars).
The runaway greenhouse threshold appears as a *vertical* boundary near $\sim$300 W/m$^2$ on the heat-flow axis (the "Runaway Greenhouse Limit" line in the figure): no steady state with a solid crust exists to its left, and for net heat fluxes only modestly above this value the surface stays molten beneath a thick steam atmosphere.
Reproduced from {cite:t}`Zahnle2007`.
```

### Blackboard derivation: the Simpson-Nakajima runaway greenhouse limit

```{admonition} Blackboard derivation: the Simpson-Nakajima limit
:class: tip

**Goal:** Show that the outgoing longwave radiation from a water-rich atmosphere has a maximum value, set by the saturation vapour pressure profile, that is independent of the surface temperature above some threshold.

**Setup.** Consider a water-rich planet with a wet adiabatic atmosphere.
The water vapour partial pressure is everywhere set by the local saturation vapour pressure $p_{\mathrm{sat}}(T)$, given by the Clausius-Clapeyron relation:

$$
\frac{\dd p_{\mathrm{sat}}}{\dd T} = \frac{L\, p_{\mathrm{sat}}}{R_v\, T^2}
$$ (eq:clausius-clapeyron-venus)

where $L \approx 2.5 \times 10^6$ J/kg is the latent heat of vaporisation of water and $R_v = 461$ J/(kg K) is the specific gas constant for water vapour.
Integrating gives the familiar exponential dependence:

$$
p_{\mathrm{sat}}(T) \approx p_{\mathrm{ref}}\, \exp\!\left[ -\frac{L}{R_v}\!\left(\frac{1}{T} - \frac{1}{T_{\mathrm{ref}}}\right) \right]
$$ (eq:saturation-pressure)

with $p_{\mathrm{ref}} = 611$ Pa and $T_{\mathrm{ref}} = 273.16$ K (the triple point of water, rounded to $273$ K below).

**Step 1: The IR optical depth and the photosphere temperature.**
The outgoing longwave radiation emerges from a thermal photosphere, defined as the level where the IR optical depth, integrated downward from the top of the atmosphere, reaches order unity.
For a vertically uniform absorption coefficient $\kappa$ (the effective infrared mass absorption coefficient of water vapour, with units of m$^2$/kg), the photosphere lies at column density $N_{\mathrm{phot}} \sim 1/\kappa$.

Because water vapour is a strong IR absorber over a wide range of wavelengths, the photosphere of a water-rich atmosphere is set by the water vapour column density alone.
At the photosphere, the water vapour pressure is set by Clausius-Clapeyron at the local temperature $T_{\mathrm{phot}}$:

$$
p_{\mathrm{sat}}(T_{\mathrm{phot}}) = \frac{g}{\kappa}
$$ (eq:photosphere-pressure)

where $g$ is the surface gravity.
This equation says: the photosphere occurs at the level where the saturation vapour pressure equals the local hydrostatic pressure required to give an optical depth of order unity.

Solving Eq. {eq}`eq:photosphere-pressure` for $T_{\mathrm{phot}}$ via Clausius-Clapeyron:

$$
T_{\mathrm{phot}} \approx \frac{L/R_v}{\ln(p_{\mathrm{ref}} \kappa / g) + L/(R_v T_{\mathrm{ref}})}
$$ (eq:photosphere-temperature)

For Earth-like values ($g = 10$ m/s$^2$, and a band-averaged $\kappa \sim 5 \times 10^{-2}$ m$^2$/kg representative of the strong rotational and vibrational water-vapour bands), this gives $T_{\mathrm{phot}} \approx 260$ K.

**Step 2: The outgoing longwave radiation.**
The OLR is approximately the blackbody emission at $T_{\mathrm{phot}}$:

$$
F_{\mathrm{OLR}} \approx \sigma\, T_{\mathrm{phot}}^4
$$ (eq:OLR)

where $\sigma = 5.67 \times 10^{-8}$ W/(m$^2$ K$^4$) is the Stefan-Boltzmann constant.

The crucial observation is that $T_{\mathrm{phot}}$ depends on the atmospheric properties (the absorption coefficient $\kappa$ and the gravity $g$) and on the water vapour saturation curve, but **not on the surface temperature**.
As the surface warms, the photosphere just moves to a higher altitude (because the saturation curve is exponentially steep), and its temperature stays clamped near the value set by Eq. {eq}`eq:photosphere-temperature`.

**Step 3: The Simpson-Nakajima limit.**
Combining Eqs. {eq}`eq:photosphere-temperature` and {eq}`eq:OLR` and plugging in numerical values:

$$
F_{\mathrm{OLR}}^{\max} \approx \sigma\, (260\,\mathrm{K})^4 \approx 260\, \mathrm{W/m^2}
$$ (eq:simpson-nakajima)

A more careful radiative-transfer calculation, including the wavelength dependence of water vapour absorption and the wings of the rotational and vibrational bands, gives a refined value of $280\text{--}310$ W/m$^2$ {cite:p}`Kasting1988,Kasting1993,Goldblatt2013`.
This is the Simpson-Nakajima limit: the maximum thermal flux that a water-saturated atmosphere can radiate to space.

**Step 4: Habitable zone implications.**
Compare this to the absorbed stellar flux at Earth's distance.
With a present solar constant of $S_\odot = 1361$ W/m$^2$ and an Earth-like Bond albedo $A = 0.30$:

$$
F_{\mathrm{abs}}^{\oplus} = \frac{S_\odot}{4}\, (1 - A) \approx 240\, \mathrm{W/m^2}
$$

Earth is comfortably below the runaway greenhouse limit, by about $40$--$70$ W/m$^2$.
At the orbit of Venus, the same calculation gives $F_{\mathrm{abs}}^{\mathrm{Venus}} \approx 460$ W/m$^2$ (assuming an Earth-like albedo, which is wrong for present Venus but is the relevant comparison for an early ocean-bearing Venus), well above the limit.
Setting $F_{\mathrm{abs}} = F_{\mathrm{OLR}}^{\max}$ and solving for the orbital distance gives the **inner edge of the classical habitable zone** for present-day solar luminosity: the moist greenhouse limit lies at $0.95$--$0.99$ AU {cite:p}`Kasting1993,Kopparapu2013` and the runaway greenhouse limit slightly inside, at $0.84$--$0.97$ AU depending on radiative-transfer assumptions {cite:p}`Kasting1993,Kopparapu2013,Goldblatt2013`.
Venus, at $0.723$ AU, sits well inside the inner edge.

**Key insight.**
The runaway greenhouse is not an artefact of one model or one parameter choice; it is a thermodynamic feature of the water phase diagram combined with the elementary physics of radiative transfer through a saturated atmosphere.
The maximum OLR is set by the temperature where the water vapour saturation curve produces the right column density to give an IR optical depth of order unity, and that temperature, and hence the maximum flux, is essentially independent of the surface temperature.
Once a planet's absorbed stellar flux exceeds this limit, no steady state with liquid surface water is possible: the atmosphere cannot lose heat fast enough, the surface temperature rises, the ocean evaporates, and the runaway proceeds to completion.
The boundary is one-way: there is no thermodynamic path back to the wet state without removing the water from the atmosphere, and the only natural removal mechanism is photodissociation followed by hydrogen escape, which is irreversible on geological timescales.
```

The numerical value of the Simpson-Nakajima limit, around $280$ W/m$^2$ from the line-by-line calculations of {cite:t}`Goldblatt2013` and consistent with the Kopparapu et al.\ 2013 reanalysis, has implications well beyond Venus.
It defines the inner edge of the **classical habitable zone** for any star at any age.
For the present-day Sun, this corresponds to the runaway greenhouse limit at $S_{\mathrm{eff}} = 1.06$ (about $0.97$ AU), with the moist greenhouse limit slightly inside Earth's orbit at $S_{\mathrm{eff}} = 1.015$ (about $0.99$ AU) {cite:p}`Kopparapu2013`.
For a younger and fainter Sun (say at $4$ Ga, with $L_\star \approx 0.75 L_{\star,\mathrm{today}}$), the inner edge sat closer to the Sun, near $\sim 0.83$ AU.
The inner habitable zone edge has therefore been moving **outward** over Solar System history as the Sun brightens, and the question of whether Venus was once inside the habitable zone (and if so, for how long) becomes a question of when the receding inner edge crossed the orbit of Venus from the inside.

```{figure} figures/wordsworth2013_OLR_ASR_equilibria.avif
:name: fig:wordsworth-equilibria
:width: 75%
:align: center

OLR (red), ASR (absorbed shortwave radiation, blue), and OLR$-$ASR (bottom) as a function of surface temperature for an atmosphere with $100$ ppm $\mathrm{CO_2}$ at a stellar flux of $F = 1.025\, F_0$, from {cite:t}`Wordsworth2013`.
There are three thermal equilibria (two stable, marked by crosses, and one unstable, marked by the open circle), illustrating that runaway-greenhouse atmospheres can have multiple solutions for the same incoming stellar flux.
This bistability is one mechanism for the **hysteresis** between wet and dry climate states discussed below.
Reproduced from {cite:t}`Wordsworth2013`.
```

### When did Venus lose its water?

The Simpson-Nakajima derivation tells us that runaway greenhouse on Venus was inevitable given enough solar flux.
What it does not tell us is **when** the transition happened.
Two competing scenarios are physically plausible and remain unresolved.

The **early loss** scenario, championed by {cite:t}`Hamano2013`, assumes that Venus formed with a hot, magma-ocean surface and a primordial steam atmosphere.
Because Venus is closer to the Sun, the absorbed flux is high enough that the atmosphere stays above the Simpson-Nakajima limit indefinitely; the magma ocean never solidifies because the optically thick steam atmosphere prevents efficient heat loss.
Water vapour photolyses in the upper atmosphere, hydrogen escapes hydrodynamically under the strong EUV flux of the young Sun, and Venus is desiccated within a few hundred million years of its formation.
On this view, Venus never had liquid surface water, and the present-day desiccation reflects the original failure of the magma ocean to crystallise into a solid surface with a condensed ocean.
{cite:t}`Hamano2013` quantified this scenario and showed that for water-rich planets at distances less than about $0.76$ AU, the magma ocean phase becomes self-sustaining and the planet becomes a "Type II" world, distinct from the "Type I" worlds (like Earth, at greater distances) that crystallise normally and develop a condensed ocean.

```{figure} figures/hamano2013_two_types.avif
:name: fig:hamano-two-types
:width: 537px
:align: center

The two types of terrestrial planet identified by {cite:t}`Hamano2013` from coupled magma-ocean and atmosphere thermal-evolution models.
**Top panel:** magma-ocean solidification time as a function of orbital distance (lower $x$-axis) and, equivalently, of net stellar radiation at the tropopause $\tau_0$ (upper $x$-axis). **Bottom panel:** final water inventory retained on the planet. Coloured curves show different initial water inventories from 0.01 to 10 Earth-ocean masses ($M_\mathrm{EO}$).
For orbital distances larger than the critical value $a_\mathrm{cr} \approx 0.77$ AU (or net stellar radiation below the tropospheric limit $F_\mathrm{lim}$) the magma ocean crystallises within a few Myr and most of the initial water is retained: this is the **Type I** (Earth-like) regime.
Inside $a_\mathrm{cr}$ the solidification time diverges and the atmosphere loses essentially all its water to hydrodynamic escape: this is the **Type II** (Venus-like) regime.
The sharp transition at $a_\mathrm{cr}$ corresponds to the Simpson-Nakajima runaway-greenhouse threshold ({numref}`fig:kopparapu-runaway`) and provides a natural explanation for the Earth-Venus dichotomy.
Reproduced from {cite:t}`Hamano2013`.
```

```{figure} figures/hamano2013_typeI_evolution.avif
:name: fig:hamano-typeI
:width: 70%
:align: center

Typical evolution of a Type I planet at $1$ AU with initial water inventory $\approx 5$ Earth-ocean masses, from {cite:t}`Hamano2013` Fig. 1.
**Top panel:** atmospheric pressure (grey shading left axis) and temperature (right axis), together with the cumulative mantle fractions that exist as melts vs solidified cumulates.
**Middle panel:** size of the magma ocean (green), atmospheric water (red), and water in the solidified mantle (blue), as fractions of the initial water reservoir.
**Bottom panel:** planetary radiation (red) and net incident stellar radiation (green dashed), with the asymptotic stratospheric and tropospheric radiation limits (dotted lines). The difference between planetary radiation and net stellar radiation (arrow) is the surplus that can be radiated from the magma ocean.
The magma ocean reaches the tropospheric radiation limit after $\sim 0.7$ Myr and is fully solidified by $\sim 4$ Myr; the steam atmosphere then condenses to form a permanent surface ocean.
Type II planets inside $a_\mathrm{cr}$ never reach this end-state because the absorbed flux exceeds the tropospheric radiation limit (cf. {numref}`fig:hamano-two-types`).
Reproduced from {cite:t}`Hamano2013`.
```

```{figure} figures/lebrun2013_magma_ocean_evolution.avif
:name: fig:lebrun-magma
:width: 60%
:align: center

Time evolution of potential temperature (black line) and surface temperature (grey line) for a crystallising magma ocean coupled to its outgassed steam atmosphere on a Venus-mass planet at the orbital distance of Venus, from panel (a) of {cite:t}`Lebrun2013` Fig. 12.
The three vertical regions ("totally molten", "partially molten", "mush") track the planetary mantle as it crystallises; condensation of water vapour occurs at the boundary between the partially molten and mush stages.
The dashed vertical line marks the time at which the magma ocean reaches $98\%$ solidification, $\sim 10$ Myr at Venus' orbital distance (compared with $\sim 1.5$ Myr at Earth's and $\sim 0.1$ Myr at Mars' for the corresponding panels (b) and (c) of the same figure, not shown).
The longer magma-ocean lifetime at smaller heliocentric distances gives the steam atmosphere ample time to photolyse and lose hydrogen to space, providing the foundation of the early-loss scenario for Venus.
{cite:t}`Lebrun2013` further showed (their Fig. 11, not shown) that below a critical distance of about $0.66$ AU around a Sun-like star, an Earth-mass planet's magma ocean cannot freeze at all and the planet remains molten indefinitely; Venus at $0.72$ AU sits just outside this limit.
```

The **late loss** scenario, championed by {cite:t}`Way2016`, takes the opposite view.
On this picture, Venus formed with a cooler, water-bearing surface and condensed a global ocean at the end of its magma ocean stage, just as Earth did.
Three-dimensional climate model simulations by {cite:t}`Way2016` demonstrated that, with the slower rotation rate of Venus and a thick day-side cloud cover, surface conditions on Venus could remain temperate (with surface temperatures from $\sim$280 K to $310$ K, depending on the assumed solar constant and topography) for billions of years, even at solar fluxes that are well above the Simpson-Nakajima limit obtained from one-dimensional models.
The key physics in their three-dimensional simulations is the formation of optically thick water clouds on the substellar dayside that reflect a large fraction of the incoming solar flux back to space, raising the planetary albedo and reducing the absorbed flux below the runaway limit.
On the late-loss picture, Venus then loses its water gradually as the Sun brightens and the cloud feedback weakens, and the runaway is triggered some time within the last $\sim$1 Gyr, leaving the planet looking exactly like the early-loss case today.

```{figure} figures/way2016_paleo_venus_temperature.avif
:name: fig:way-paleo
:width: 504px
:align: center

Three-dimensional climate model simulation of the surface air temperature on a hypothetical paleo-Venus at $2.9$ Ga with $75\%$ of present solar irradiance, from panel (a) of {cite:t}`Way2016` Fig. 2, plotted on a Mollweide global projection.
Surface temperatures range from below freezing in polar regions to about $40^\circ$C at the equator, suggesting that an early Venus could have hosted long-lived liquid surface water.
{cite:t}`Way2016` confirmed similar temperate conditions for several variants (different epochs, modern Earth topography in place of Venusian topography, faster rotation), shown in panels (b)-(d) of the same figure (not reproduced here).
```

The {cite:t}`Turbet2021` paper revisited the question with a different physical conclusion.
Their three-dimensional simulations focused on the **night-side** of an early Venus and showed that water clouds preferentially form there, where they cool the atmosphere by long-wave radiative loss and prevent water condensation on the surface.
The day-side, by contrast, has a much weaker cloud cover and so absorbs nearly all incoming sunlight.
On their picture, the asymmetric day-night cloud distribution prevents an ocean from condensing on Venus from the start, even if the planet enters the post-magma-ocean phase with a low surface temperature; the runaway greenhouse therefore traps Venus from the very beginning.
Their main result is summarised in a hysteresis diagram showing the conditions under which an ocean can form: Venus is on the wrong side of the hysteresis loop for ocean formation throughout its history, while Earth is on the right side.

```{figure} figures/turbet2021_hysteresis.avif
:name: fig:turbet-hysteresis
:width: 90%
:align: center

Hysteresis loops for ocean formation on early Earth and Venus, from {cite:t}`Turbet2021`.
**Panel (a)** shows surface temperature as a function of incoming solar flux for Earth: at $4$ Ga, water condenses from a steam atmosphere if the atmosphere is initially condensed (operating point near present-day) but enters the runaway greenhouse if it starts hot (red branch).
**Panel (b)** shows the same for Venus: the runaway and condensed branches do not overlap, so an early Venus that started in the runaway state (the natural endpoint of magma ocean cooling at high solar flux) cannot reach the condensed branch even at $4$ Ga, when the insolation at Venus was $\sim$25% lower than today and Venus still received $\sim$500 W/m$^2$, well above the cloud-modified condensation threshold of $\sim$325 W/m$^2$.
Reproduced from {cite:t}`Turbet2021`.
```

```{figure} figures/turbet2021_water_clouds_emission.avif
:name: fig:turbet-clouds
:width: 55%
:align: center

Three-dimensional simulation of an early Venus near the runaway threshold from {cite:t}`Turbet2021`, showing vertically integrated water-cloud column density (top, panel b) and thermal emission to space (bottom, panel d) at a stellar flux $S = 340.5$ W/m$^2$, with subsolar longitudes near $0^\circ$.
The night-side dominates the emission: the substellar dayside has thick water clouds that reflect sunlight back to space, while the cooler night-side radiates the thermal flux.
This day-night asymmetry is the mechanism by which the runaway state is preserved; on Earth, the corresponding panels of the same figure (not reproduced here) show a more zonally distributed cloud cover that allows the planet to sit on the condensed branch of the hysteresis curve.
```

These three papers illustrate the current state of the field: there are strong theoretical arguments on both sides, the evidence from Venus itself is ambiguous, and definitive resolution will require new observations (the most decisive being noble-gas measurements from a future descent probe, which would constrain the time-integrated escape history, and high-resolution near-IR emissivity mapping of tessera regions, which would test for ancient felsic crust formed in the presence of liquid water).
For the purposes of this lecture, we should treat both the early-loss and late-loss scenarios as physically plausible and observationally untested, and accept that one of the central questions of comparative rocky-planet evolution remains open.

```{figure} figures/gillmann2022_dry_wet_venus_scenarios.avif
:name: fig:gillmann-scenarios
:width: 75%
:align: center

The two main scenarios for Venus' early evolution as summarised by {cite:t}`Gillmann2022`.
**Top branch** (Dry Venus, Hamano-style): the magma ocean never crystallises with a condensed surface, water photolyses early, and the planet emerges desiccated within $\sim$100 Myr.
**Bottom branch** (Wet Venus, Way-style): the magma ocean crystallises, an ocean condenses, the planet remains habitable for several Gyr, and the runaway greenhouse is triggered later by gradual loss of water and the slow rise of solar luminosity.
Both end at the present state of Venus, and current data cannot distinguish them definitively.
Reproduced from {cite:t}`Gillmann2022`.
```

```{figure} figures/honing2021_reference_evolution.avif
:name: fig:honing-reference
:width: 90%
:align: center

Reference scenario for the coupled interior-atmosphere evolution of a stagnant-lid Venus from panels (a) and (b) of {cite:t}`Honing2021` Fig. 3.
**Left panel:** carbon reservoirs (atmosphere, crust, atmosphere+crust, atmosphere with weathering switched off) as a function of time after solidification.
**Right panel:** surface temperature with (blue) and without (green) silicate weathering.
Surface weathering keeps the planet temperate for $\sim 0.9$ Gyr; once water is lost, decarbonation drives the runaway accumulation of $\mathrm{CO_2}$ to a Venus-like end state.
The remaining panels (c)-(f) of the original figure (not reproduced here) show the corresponding evolution of carbon fluxes, atmospheric water vapour, layer depths, and interior temperatures.
```

```{figure} figures/constantinou2024_venus_pathways.avif
:name: fig:constantinou-pathways
:width: 90%
:align: center

The two dichotomous climate pathways for Venus from {cite:t}`Constantinou2024`, ending in interiors with very different water inventories.
**Upper branch (dry Venus):** the planet emerges from its magma-ocean stage at $t \approx 100$ Myr without ever condensing a surface ocean; water is lost early via photolysis and hydrogen escape, leaving an interior depleted in hydrogen and a present-day mantle that degasses S- and C-rich, $\mathrm{H_2O}$-poor volcanic gases.
**Lower branch (temperate, wet Venus):** the magma ocean crystallises with a condensed ocean at the surface, the planet remains habitable for several Gyr, and the present-day mantle still contains significant water that emerges in $\mathrm{H_2O}$-rich volcanic gases.
The two interior signatures map onto observable differences in the chemistry of Venus' atmosphere. {cite:t}`Constantinou2024` argue from the destruction rates of $\mathrm{H_2O}$, $\mathrm{CO_2}$, and $\mathrm{OCS}$ in the present atmosphere that the volcanic source must be water-poor (at most $\sim$6\% $\mathrm{H_2O}$ mole fraction), favouring the dry-Venus branch.
Reproduced from {cite:t}`Constantinou2024`.
```

### The D/H ratio: smoking gun for water loss

Whichever scenario is correct, there is one strong piece of empirical evidence that Venus once had at least $100\times$ more water than it does today: the deuterium-to-hydrogen ratio.
The original Pioneer Venus mass spectrometer measurement of {cite:t}`Donahue1982` gave $D/H \approx 1.6 \times 10^{-2}$, about $100$ times the terrestrial standard mean ocean water value of $D/H = 1.6 \times 10^{-4}$.
Subsequent Earth-based near-IR night-side spectroscopy refined the value to $(1.9 \pm 0.6) \times 10^{-2}$, corresponding to $\sim 120 \pm 40$ times terrestrial {cite:p}`deBergh1991`; later high-resolution measurements have converged on the now widely quoted enrichment factor of $\sim 150 \pm 30$ relative to Earth {cite:p}`Widemann2023`.

The physical reason is straightforward.
In hydrodynamic escape (or any escape mechanism in which the energy per particle is comparable to the escape energy), the lighter isotope escapes more efficiently than the heavier one, because the lighter molecules acquire higher thermal velocities for a given temperature.
In the limit of efficient mass fractionation, the residual water in the planet becomes progressively enriched in deuterium relative to its initial isotopic composition.
The textbook description is **Rayleigh distillation** {cite:p}`Hunten1987`: if $f$ is the fraction of the original hydrogen reservoir still left, and $\alpha < 1$ is the fractionation factor (the ratio of deuterium to hydrogen escape efficiencies), then the present isotopic ratio $R$ relative to the initial ratio $R_0$ obeys

$$
\frac{R}{R_0} = f^{(\alpha - 1)}.
$$

The fractionation factor $\alpha$ depends on the escape regime, and two limiting cases give very different answers.
In a **mass-ratio limit** (the strongest defensible fractionation), $\alpha \approx m_{\mathrm{H}}/m_{\mathrm{D}} \approx 0.5$.
In a **thermal-velocity limit** (the weakest defensible fractionation, using only the Maxwell-Boltzmann velocity ratio at fixed temperature), $\alpha \approx \sqrt{m_{\mathrm{H}}/m_{\mathrm{D}}} \approx 0.71$.
Setting $R/R_0 = 150$ and solving $f = 150^{1/(\alpha-1)}$ gives $f_{\mathrm{diff}} \approx 150^{-2} \approx 4 \times 10^{-5}$ in the diffusion-limited limit, and $f_{\mathrm{Jeans}} \approx 150^{-3.4} \approx 4 \times 10^{-8}$ in the bare thermal-velocity limit.
Multiplying the present water column ($\sim 2$ cm of global equivalent layer in the lower atmosphere) by $1/f$ then implies an initial water inventory of order *several hundred metres* of global equivalent depth in the diffusion-limited case (a shallow Earth ocean), or order *several hundred kilometres* in the bare thermal-velocity case, which corresponds to more than 100 Earth-ocean masses and is plainly unphysical for a delivery scenario.
The contradiction in the second case is itself instructive: a pure velocity-tail interpretation of hydrogen escape cannot be the full story.
The actual integrated escape history of Venus likely combined an early **hydrodynamic** phase (with $\alpha$ close to unity, requiring large total losses but producing little fractionation per escaping atom) with a later **diffusion-limited** phase that produced most of the observed enrichment.
This is therefore a *lower-bound* argument: even under the most-fractionating defensible single-regime assumption, the present hydrogen reservoir is at most $\sim 4 \times 10^{-5}$ of the original, requiring an initial inventory of at least several hundred metres global equivalent.
The exact number also depends on the integration time and on the rate at which fresh deuterium-rich water might have been added by cometary impact, but **all such models require the original Venusian water inventory to have been at least $\sim$100 times the present value**, equivalent to a global ocean of at least a few metres depth.

This is the strongest direct observational constraint we have that Venus has lost most of its primordial water to space.
What it does not tell us is when the loss happened: hydrogen escape rates change over time as the EUV flux of the Sun decreases, and the integrated escape history can equally well be early (during a magma-ocean phase) or distributed over billions of years.
Future noble gas measurements, particularly $^{36}$Ar/$^{38}$Ar and Xe isotopic ratios from a descent probe (planned by DAVINCI), are expected to discriminate between these histories, because different escape regimes leave different fractionation signatures across the noble gas series.

```{figure} figures/wordsworth2014_abiotic_o2_schematic.avif
:name: fig:wordsworth-abiotic-o2
:width: 50%
:align: center

Schematic of the abiotic build-up of an $\mathrm{O_2}$-dominated atmosphere by photolytic water loss on a terrestrial habitable-zone planet, from {cite:t}`Wordsworth2014`.
**Top:** during the early phase, stellar XUV flux photolyses atmospheric water vapour into hydrogen and oxygen; the lighter hydrogen escapes preferentially to space, while oxygen accumulates either in the atmosphere or condenses onto surface regions of low net instellation.
**Bottom:** once enough $\mathrm{O_2}$ has built up, the planet enters a stable state in which continued $\mathrm{H_2O}$ photolysis and hydrogen escape are balanced by oxidation of the planetary interior.
The same chain of processes (water photolysis, hydrogen escape, oxygen sinks) is the operative mechanism for desiccating Venus, and it leaves the residual D/H ratio enriched by the factor of $\sim$150 observed on present-day Venus.
Reproduced from {cite:t}`Wordsworth2014`.
```


### Volcanic activity today: is Venus alive?

A long-standing question in Venus science is whether the planet is volcanically active right now, or whether the geologically recent volcanic activity inferred from crater statistics has died out.
Several lines of indirect evidence have suggested ongoing activity over the years.
$\mathrm{SO_2}$ concentrations in the upper atmosphere have varied by factors of several over the $40$-year baseline of Pioneer Venus, Magellan, and Venus Express observations, and the simplest explanation for the variability is episodic volcanic injection of $\mathrm{SO_2}$ from below.
Thermal emission anomalies detected by Venus Express in near-IR atmospheric windows over Idunn Mons and other Venus volcanoes are consistent with cooling from recent (geologically speaking) lava flows, although the dating of those flows from the thermal data alone is not precise.

The decisive observation came in $2023$, when {cite:t}`HerrickHensley2023` reanalysed archival Magellan radar data from $1990$ to $1992$ and identified a clear morphological change in a volcanic vent on the flank of **Maat Mons**.
A vent that appeared roughly circular in early Magellan cycles had become irregularly shaped and substantially enlarged in later cycles, with surrounding terrain consistent with a fresh lava flow.
This is the first direct evidence of an active volcanic eruption on Venus from spacecraft data, and it establishes that Venus is volcanically active today rather than in a quiescent interval.
The implications are significant: any model of Venus that posits a long-dead surface is wrong, the resurfacing process is at least episodic, and the present-day volcanism provides an ongoing source of $\mathrm{CO_2}$ and $\mathrm{SO_2}$ to the atmosphere.

The natural question then is: is this active volcanism comparable to Earth's volcanic flux, or is it much smaller?
This question is central to the carbon and sulfur balance of Venus, because the volcanic source has to be in steady state (or near it) with whatever sinks operate today, and the only known sinks for $\mathrm{CO_2}$ and $\mathrm{SO_2}$ on Venus are the weathering reactions of surface basalts and the chemistry of the cloud-deck region.
The rates of these reactions are uncertain by orders of magnitude, and pinning them down is one of the main scientific objectives of EnVision and DAVINCI.


## Part 3: Comparative payoff

### Why did Earth and Venus diverge?

We are now in a position to answer the question that opened this lecture, namely what set two nearly identical starting points onto such radically different evolutionary paths.
The answer involves four physical inputs that differed (or differed slightly) between Earth and Venus, plus the nonlinear couplings that turned modest input differences into runaway outcomes.

The first input is the **solar flux**.
At $0.723$ AU, Venus receives $1.91 \times$ the solar flux per unit area that Earth does at $1$ AU.
This is the single biggest lever, and it is the only input where the two planets are very different at the start.
With the present-day Sun, Venus is comfortably above the Simpson-Nakajima limit and Earth is comfortably below.
With a young, faint Sun, the picture is more nuanced: Venus may have been just above or just below the threshold, depending on cloud cover and atmospheric composition, and the question of whether early Venus was habitable becomes a question of how the solar flux interacted with the cloud feedback and the carbonate-silicate cycle.
If Venus had formed even $0.05$ AU farther from the Sun, the runaway might have been delayed for billions of years and Venus might today look much more Earth-like; conversely, if Earth had formed $0.05$ AU closer to the Sun, Earth might have followed the Venus trajectory.
The two planets are at the very edge of the Simpson-Nakajima boundary, on opposite sides of the line.

The second input is the **timing of water delivery and loss**.
Both planets accreted in roughly the same region of the protoplanetary disk and likely had similar primordial water inventories (though we cannot measure this directly for Venus).
The difference is in what happened to the water as the planet cooled.
On Earth, the water survived the magma-ocean phase, condensed at the surface, and persisted as an ocean for the next $4$ Gyr.
On Venus, the water either failed to condense in the first place (the Hamano-Turbet picture) or condensed and was subsequently lost during a slow runaway over billions of years (the Way picture).
The end result is the same, but the timing changes our interpretation of habitability: in the first case, Venus was never habitable, while in the second case, it was for billions of years.
The D/H ratio confirms that water was lost; the noble gas isotopes (yet to be measured) will eventually tell us when.

The third input is the **rotation rate**.
Venus rotates retrograde with a $243$-day period, dramatically slower than Earth's $24$-hour rotation.
This affects the planet in two ways.
First, it changes the atmospheric circulation pattern: the Coriolis force, which dominates Earth's mid-latitude weather, is much weaker on slowly rotating Venus, and the cloud-top circulation is dominated by zonal super-rotation rather than by Hadley-Ferrel cells.
This changes the cloud distribution and hence the planetary albedo.
Second, the slow rotation may suppress dynamo action in the core: Earth's geodynamo benefits from the strong Coriolis force that organises the convective flow, while a slowly rotating planet may struggle to maintain a coherent dynamo even if the core is convecting.
The slow rotation is itself a puzzle (it may be the result of a giant impact, of solid-body tidal interaction with the Sun, or of atmospheric thermal tides braking the spin), but its consequences for the climate and the magnetic field are at least qualitatively understood.

A useful way to visualise the consequences of the diverging water history is the **redox pump** sketched in {numref}`fig:wordsworth-n2pump`.
Earth and Venus may have started from a similar reducing steam atmosphere over a magma ocean, but the choice of whether the surface ocean condenses (Earth) or whether photolysis and hydrogen escape destroy the steam atmosphere first (Venus) drives the planet through very different sequences of redox states.
On Earth, the surface ends up moderately oxidising with most of the nitrogen partitioned into a $1$-bar $\mathrm{N_2}$ atmosphere; on Venus, the loss of hydrogen and oxidation of the interior leaves a much smaller $\mathrm{N_2}$ inventory in a hot, $\mathrm{CO_2}$-dominated atmosphere {cite:p}`WordsworthN2016`.

```{figure} figures/wordsworth2016_n2_redox_pump.avif
:name: fig:wordsworth-n2pump
:width: 80%
:align: center

Schematic of the **water-loss redox pump** linking the differing atmospheric $\mathrm{N_2}$ inventories of Earth and Venus to their early water-loss histories, from {cite:t}`WordsworthN2016`.
Both planets begin in **state A** with a reducing steam atmosphere over a magma ocean.
Earth evolves directly to **state C**, a $1$-bar $\mathrm{N_2}$ atmosphere over a moderately oxidising mantle ($f_{\mathrm{O_2}} \approx$ FMQ) with surface liquid water and a substantial pool of nitrogen sequestered in the interior.
Venus, on the other hand, passes through **state B**, in which intense hydrogen escape oxidises the upper mantle, before reaching **state D**, a hot $\mathrm{CO_2}$- and $\mathrm{N_2}$-rich atmosphere over a highly oxidised interior ($f_{\mathrm{O_2}} \approx$ MH).
The diagram emphasises that the present atmospheric composition contrast between Earth and Venus is a downstream consequence of the water history operating through the planetary redox budget.
The four-panel layout is retained because the redox sequence A$\to$C (Earth) versus A$\to$B$\to$D (Venus) is the central pedagogical content of the figure.
Reproduced from {cite:t}`WordsworthN2016`.
```

The fourth input is the **tectonic regime**.
Earth is in mobile-lid mode and Venus is in stagnant-lid mode.
The two regimes correspond to different climate-coupling structures: Earth's plate tectonic system supports the carbonate-silicate cycle, while Venus' stagnant-lid system breaks the cycle once the oceans are gone.
The crucial point is that **the tectonic regime is not independent of the water inventory**.
A wet mantle is much weaker than a dry mantle (water reduces the viscosity of olivine by orders of magnitude at upper-mantle conditions), and a wet lithosphere is more likely to undergo subduction.
Loss of surface water (and the associated dehydration of the mantle by recycling of dehydrated lithosphere) makes the planet stiffer, slows down the convective heat loss, and may eventually shut off plate tectonics altogether.
On this view, the tectonic regimes of Earth and Venus are not independent inputs; they are partly consequences of the water inventory and the runaway greenhouse history.

```{figure} figures/gillmann2022_earth_venus_systems.avif
:name: fig:earth-venus-systems
:width: 95%
:align: center

System diagram comparing the climate and interior couplings of Earth (left) and Venus (right), from {cite:t}`Gillmann2022`.
Earth's system is closed by the active feedback loop between mantle convection, plate tectonics, surface volcanism, the atmosphere, the hydrosphere, the biosphere, and the magnetic dynamo.
Venus' system is open: subduction is absent, the hydrosphere is essentially zero, the biosphere is empty, and the magnetic dynamo is shut down.
The cycles that buffer Earth's climate cannot operate on present Venus.
Reproduced from {cite:t}`Gillmann2022`.
```

### The carbonate-silicate cycle failure mode on Venus

The carbonate-silicate cycle is the central feedback that has stabilised Earth's climate over $4$ Gyr.
We covered the mechanism in {ref}`lecture06`; here we ask why it cannot save Venus.
The cycle has three essential ingredients: a source of $\mathrm{CO_2}$ (volcanism), a sink (silicate weathering followed by carbonate burial), and a return leg (subduction).
Earth has all three.
Venus, in its present state, has only the source.

When Venus' surface ocean was lost (whenever that happened), the silicate weathering sink stopped operating because silicate weathering requires liquid water at the surface to dissolve the silicate minerals into the ions that are eventually precipitated as carbonates.
Volcanism continued, however, releasing $\mathrm{CO_2}$ from the interior at roughly its normal rate.
With the source running and the sink shut down, atmospheric $\mathrm{CO_2}$ accumulated until it reached the present level of $\sim 92$ bar.
In the absence of subduction, even if the weathering sink were somehow restored (by a hypothetical re-watering of the planet), there would be no return leg to recycle the carbon back to the mantle, and the system would not relax to a thermostat-controlled steady state.

The arithmetic of the carbon inventory is striking.
Earth's total surface and crustal carbon, including the carbonate platforms accumulated over $\sim$540 Myr of marine biology, is on the order of $10^{20}$ kg of carbon, equivalent to a $\mathrm{CO_2}$ partial pressure of order $\sim 100$ bar if it were all in the atmosphere {cite:p}`Catling2017`.
Venus' atmospheric $\mathrm{CO_2}$ inventory of $92$ bar is comparable to this number.
The implication is that Earth and Venus probably acquired roughly similar amounts of carbon during accretion, and the difference is in where it ended up.
On Earth, almost all of the carbon is in the crustal carbonates and the deep mantle reservoir; in the atmosphere only a few hundred ppm.
On Venus, almost all of the carbon is in the atmosphere.
This is the central comparative result of the lecture: **the difference between Earth and Venus is not how much carbon they have, but how the carbon is distributed**, and the distribution is set by whether the carbonate-silicate cycle is operating or has failed.

The irreversibility of the failure is what makes Venus a cautionary tale.
There is no thermodynamic path from the present Venus atmosphere back to a wet, Earth-like state; even if some unknown mechanism removed all of the atmospheric $\mathrm{CO_2}$, the resulting planet would still lack a surface ocean, would still have a stagnant lid, and would lack the geochemical machinery to maintain a habitable surface.
Once a planet drops below the inner habitable zone edge in the runaway sense, it does not climb back out without an external rescue.
The carbonate-silicate thermostat that protects Earth is not infinitely robust; it is a feedback that operates within a specific set of conditions, and outside those conditions, it breaks irreversibly.

### What this means for habitability

The traditional concept of the **habitable zone** as a fixed annulus around a star, defined by the orbital distances at which an Earth-like planet could host liquid surface water, is a useful first cut but it is not enough.
For one thing, the boundaries of the zone evolve with the host star's luminosity over its main-sequence lifetime (the inner edge moves outward as the star brightens).
For another, whether a planet is habitable at any given moment depends on its history: a planet that was once inside the runaway greenhouse limit and lost its water cannot become habitable again just because the inner edge later sweeps past it as the star ages.
The habitable zone is not a region in space but a region in **history**, and the relevant calculation is not "is this planet inside the habitable zone today" but "does the integrated history of this planet's solar flux, water inventory, and feedback systems leave it in a habitable state today".

```{figure} figures/nasa_trappist1_solarsystem_comparison.avif
:name: fig:trappist1
:width: 80%
:align: center

Comparison of the seven TRAPPIST-1 planets (b through h) with the inner Solar System (Mercury, Venus, Earth, Mars), in the plane of planetary density (vertical) versus stellar illumination (horizontal, in units of Earth's illumination).
The blue band marks the classical habitable zones for the two systems.
Three of the TRAPPIST-1 planets (e, f, g) lie within the habitable zone, and TRAPPIST-1 c receives an illumination similar to Venus.
Whether any of these planets actually retain surface water depends on their history (formation, atmospheric evolution, escape) and not just on their current orbital location.
Image credit: NASA/JPL-Caltech.
```

Earth and Venus exemplify this distinction.
Earth sits comfortably inside the inner edge of the long-term habitable zone, and the carbonate-silicate thermostat has kept it habitable throughout its history.
Venus sits outside the inner edge today and (depending on which scenario you favour) either was always outside or crossed it at some point in the past.
A few percent change in solar flux, or a slightly different impact history, would have shifted the dividing line.
The Earth-Venus contrast is not the result of a deep, predictable physical law that says "Earth-like planets at $1$ AU are habitable and Venus-like planets at $0.7$ AU are not"; it is the result of a sensitive balance between radiative input, water inventory, tectonic regime, and biospheric feedback.
When we apply the lessons of Earth and Venus to exoplanets, the message is that **single-snapshot habitable zone arguments are insufficient** and that climate-evolution models that follow a planet through its full history are essential.
This is the agenda we will pursue in {ref}`lecture13`.

### Recent advances and upcoming missions

The 2030s will be a transformative decade for Venus science, with three new orbital missions and at least one in-situ probe planned.
**NASA's DAVINCI** (Deep Atmosphere Venus Investigation of Noble gases, Chemistry, and Imaging) is expected to launch in $2029$--$2030$ and will release an instrumented descent probe into the atmosphere of Venus to measure noble gas isotopic abundances, atmospheric chemistry, and surface morphology during the descent.
The noble gas measurements are particularly important: they provide the time-integrated record of atmospheric escape that should distinguish between the early-loss and late-loss scenarios for Venus' water history.
**NASA's VERITAS** (Venus Emissivity, Radio Science, InSAR, Topography, and Spectroscopy) is currently scheduled for launch no earlier than $2031$ and will provide global high-resolution radar topography and near-infrared surface emissivity, which will resolve the tessera composition question and constrain the present-day style of mantle convection through high-precision measurement of the moment of inertia and the tidal Love numbers.
**ESA's EnVision** is expected to launch in May $2032$ and combines synthetic-aperture radar at multiple frequencies, atmospheric spectroscopy, and a subsurface radar sounder; its science goals include searching for ongoing volcanism, mapping near-surface water (if any), characterising the radar properties of tessera regions, and measuring the gravity field at unprecedented resolution.


In parallel, theoretical modelling is advancing rapidly: 3D climate models of early Venus {cite:p}`Way2016,Turbet2021`, coupled magma-ocean atmosphere-interior models {cite:p}`Hamano2013,Gillmann2022`, and thermo-chemical models of the long-term atmospheric evolution {cite:p}`Lammer2018,Gillmann2022` are converging on a coherent picture of how the early divergence of Earth and Venus could have happened and what observations would distinguish the remaining alternatives.
A separate active research front is the search for biosignatures in the Venus cloud layer: the temperature and pressure conditions at $50$-$60$ km altitude are similar to surface Earth conditions, and the question of whether Venus could harbour an aerial biosphere there has been an open one since the original Sagan and Morowitz proposal in $1967$.
The phosphine controversy of $2020$ ({ref}`lecture06`) brought this question briefly into the spotlight, and although the original detection has been contested, the question itself remains and will be addressed by the new missions.


```{figure} figures/dauphas2017_earth_accreting_material.avif
:name: fig:dauphas-accretion
:width: 45%
:align: center

Probability density function for the chromium-bearing fraction of Earth's accreting mass as a function of the cumulative accreted mass fraction, from {cite:t}`Dauphas2017` (Cr panel of their five-isotope Fig. 1).
The red triangle on the $x$-axis marks $x_{0.95} = 0.85$, the mass fraction at which $95\%$ of Earth's present mantle Cr inventory was delivered, demonstrating that Cr is back-loaded toward the second half of accretion.
Combined with the O, Ti, Ni, Mo, and Ru tracers from the same study (not reproduced here), {cite:t}`Dauphas2017` reconstruct three accretion stages: stage I ($0\text{--}60\%$ of Earth's mass) is best fit by $\sim 51\%$ enstatite-meteorite-like (E-type) plus $\sim 40\%$ ordinary-chondrite plus $\sim 9\%$ carbonaceous-chondrite (CO/CV) material; stages II ($60\text{--}99.5\%$) and III (the last $0.5\%$, the "late veneer") are essentially $100\%$ E-type.
The carbonaceous component, and therefore the bulk of Earth's water if it was delivered with that material, was concentrated in the early stages of main accretion rather than in the late veneer.
```


## Summary and takeaways

Earth and Venus are the closest analogue we have to a controlled experiment in comparative planetology.
They started from the same protoplanetary reservoir, accreted to similar masses and densities, and probably acquired comparable inventories of water and carbon.
Today they could not look more different: Earth is wet, geologically active, magnetically shielded, and inhabited; Venus is dry, encased in $92$ bar of $\mathrm{CO_2}$, surface temperature $737$ K, with no global magnetic field and no plate tectonics.
The divergence is due to a small set of physical inputs (solar flux, water history, rotation rate, and tectonic regime) coupled by nonlinear feedbacks that turned modest differences in input into qualitatively different end states.

The central piece of physics is the **Simpson-Nakajima runaway greenhouse limit**: the maximum thermal flux that a water-saturated atmosphere can radiate to space, set by the saturation vapour pressure curve at the temperature of the IR photosphere.
This limit, in the range $280\text{--}310$ W/m$^2$, defines the inner edge of the habitable zone and is essentially independent of the surface temperature once the atmosphere becomes optically thick in the IR.
A planet whose absorbed solar flux exceeds the limit cannot host a steady state with liquid surface water; the runaway greenhouse drives the ocean into the upper atmosphere, photolyses the water, and loses the hydrogen to space.
The process is one-way: there is no thermodynamic path back to the wet state.
Earth, at $1$ AU, sits below the limit; Venus, at $0.723$ AU, sits well above it.

The **carbonate-silicate cycle** is the negative feedback that has stabilised Earth's climate within the liquid-water window for $4$ Gyr, but it cannot operate on present Venus because the cycle requires both liquid surface water (for the weathering sink) and active plate tectonics (for the subduction return leg).
Once Venus lost its water, the sink was destroyed; once the subduction stopped, the return leg was destroyed.
Volcanic outgassing of $\mathrm{CO_2}$ continued, and atmospheric $\mathrm{CO_2}$ accumulated to its present $92$ bar value over hundreds of millions of years.
The total carbon inventory of Earth (mostly stored as carbonate rocks) is comparable in magnitude to the atmospheric carbon inventory of Venus, suggesting that the two planets have similar carbon inventories and the difference is where the carbon ended up.

The **D/H ratio** of Venus, enriched by a factor of $\sim$150 over the terrestrial value, is the smoking gun for water loss: it implies that Venus has lost at least $100\times$ more water than its present inventory, regardless of the loss mechanism or timing.
The remaining open question is whether the loss happened early (during a perpetual magma ocean phase, the Hamano scenario) or late (after a few-Gyr period of habitability, the Way scenario), and the answer matters for whether early Venus was ever habitable.
This question will be addressed in the next decade by the new wave of Venus missions (DAVINCI, VERITAS, EnVision), particularly the noble-gas isotopic measurements that DAVINCI will return from its descent probe.

For exoplanets, the lesson is that **the habitable zone is not a region in space but a region in history**.
A planet's habitability today depends on the entire integrated history of its solar flux, water inventory, tectonic regime, and feedback systems, not on a single snapshot of where it sits relative to a static habitable zone boundary.
Earth sits comfortably inside the habitable zone today; Venus sits comfortably outside; but a few percent change in solar flux, or a slightly different impact and accretion history, could have placed either of them in the other's role.
What we learn from Venus directly informs our framework for assessing exoplanet habitability and, indirectly, our understanding of the long-term stability of Earth's own climate system, including the question of how robust the carbonate-silicate thermostat is to anthropogenic forcing on human timescales.

**Key physics takeaway**: The Simpson-Nakajima limit is a thermodynamic boundary in phase space, not a model artefact. It defines the irreversible threshold beyond which the runaway greenhouse drives a wet planet to a dry, hot end state, and Venus is the textbook example.

**Key comparative takeaway**: Earth's long-term habitability rests on a coupled set of feedbacks (carbonate-silicate cycle, plate tectonics, biosphere, dynamo) that all require liquid water and active volcanism to operate. Loss of any one of these feedbacks risks losing the others; Earth has been lucky, and Venus shows what happens when you are not.


## References

```{bibliography}
:filter: docname in docnames
```
