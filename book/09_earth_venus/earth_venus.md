(lecture09)=
# Rocky Planets, Earth & Venus

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe Earth's unique properties as a reference planet, explain how Venus diverged from Earth despite similar bulk composition and size, apply the Simpson-Nakajima runaway greenhouse limit, and evaluate the role of water loss history, tectonic regime, and the carbonate-silicate cycle in comparative habitability.
```

```{seealso}
**Slides:** [Download Lecture 9 (PDF)](../_static/slides/lecture09.pdf)
```

Earth and Venus are nature's best controlled experiment in comparative planetology.
They formed from the same nebular reservoir within roughly $0.3$ AU of each other ({numref}`fig:lammer-accretion`), contain similar bulk inventories of silicate, iron, and volatile elements, and have masses and radii within $20\%$ of each other.
Yet their present-day surface conditions could not be more different.
Earth is wet, geologically active, magnetically shielded, and inhabited.
Venus is dry, encased in a $92$ bar carbon-dioxide atmosphere at a surface temperature of $737$ K, and the only one of the rocky planets without a global magnetic field.
Identifying what set these two nearly identical starting points on such radically different evolutionary paths is the central question of this lecture.
This lecture works through that question in three parts.
Part 1 reviews Earth as a reference planet, Part 2 surveys Venus as the alien twin, and Part 3 brings the comparison together to extract the underlying physics.
The blackboard derivation in the middle introduces the Simpson-Nakajima runaway greenhouse limit, a thermodynamic boundary in phase space that, once crossed, makes the divergence essentially irreversible.

```{figure} figures/lammer2018_venus_earth_mars_accretion.avif
:name: fig:lammer-accretion
:width: 100%
:align: center

Schematic accretion histories of **Venus** (top), **Earth** (middle), and Mars (bottom) during the first $\sim$110 Myr of the Solar System.
Each panel sketches the buildup from undifferentiated planetesimals through differentiated planetary embryos to the final magma-ocean stage, in which intense early heating leaves the planet's outer layers wholly or partly molten.
Volatile species ($\mathrm{H_2O}$, $\mathrm{CO_2}$, noble gases) outgas from the interior to form a primary steam-rich atmosphere; their fate during the cooling of the magma ocean determines the long-term volatile inventory of each planet.
Reproduced from {cite:t}`Lammer2018`.
```

## Part 1: Earth as reference

### Earth's bulk properties and what makes it habitable

Earth has a semimajor axis of $1$ AU, mass $\Mearth = 5.97 \times 10^{24}$ kg, and equatorial radius $\Rearth = 6378$ km.
Its mean density of $5.51$ g/cm$^3$, the highest in the Solar System, indicates a differentiated interior with a metallic iron-nickel core ({ref}`Lecture 8 <lecture08>`) {cite:p}`Dziewonski1981`.
The dimensionless moment of inertia factor is $C/MR^2 = 0.331$, compared to $0.4$ for a uniform sphere.
This indicates that an iron core holds $32\%$ of Earth's mass in $17\%$ of its volume.
Mean surface conditions are $T_s \approx 288$ K and $P_s = 1.013$ bar, under an atmosphere of $78\%$ $\mathrm{N_2}$, $21\%$ $\mathrm{O_2}$, and trace species (argon, water vapour, $\mathrm{CO_2}$).

Earth is unique today in combining three coupled systems: an active **mobile-lid** plate tectonic regime, where the rigid outer shell is broken into independently moving plates; persistent liquid surface water covering $71\%$ of the planet; and a global biosphere.
Liquid water hydrates the **lithosphere**, the rigid outer shell comprising the crust and uppermost mantle.
This enables **subduction**, the sinking of one plate beneath another into the mantle ({ref}`Lecture 7 <lecture07>`).
The biosphere has maintained atmospheric $\mathrm{O_2}$ and $\mathrm{CO_2}$ for the last $\sim$2.4 billion years {cite:p}`Lyons2014`.
Persistent liquid water on $4$-Gyr timescales is stabilised by the **carbonate-silicate cycle** ({ref}`Lecture 6 <lecture06>`), a negative feedback requiring volcanic outgassing of $\mathrm{CO_2}$ and silicate weathering on a wet surface {cite:p}`Walker1981`.
This mutual coupling maintains Earth's habitability over billions of years.
Removing any component causes the system to collapse, as likely occurred early on Venus.

### The geologic eons of Earth

Geologists divide the $4.54$ Gyr of Earth history into four **eons**, the primary formal subdivisions of geologic time ({numref}`fig:earth-eons`).
Boundary ages are calibrated by radiometric dating ({ref}`Lecture 12 <lecture12>`) and standardised in the Geologic Time Scale {cite:p}`Gradstein2020`.

```{figure} figures/earth_eons_timeline.avif
:name: fig:earth-eons
:width: 100%
:align: center

The geologic eons and eras of Earth.
**Top bar:** the four eons spanning the full $4.54$ Gyr of Earth history, with the eras of the Archean and Proterozoic marked above; note that the Hadean, Archean, and Proterozoic together (the informal "Precambrian") occupy almost $90\%$ of the timeline.
**Bottom bar:** the Phanerozoic eon stretched to the full figure width, divided into the Paleozoic, Mesozoic, and Cenozoic eras at the end-Permian ($252$ Ma) and end-Cretaceous ($66$ Ma) mass extinctions.
Boundary ages follow the Geologic Time Scale 2020 {cite:p}`Gradstein2020`.
```

The **Hadean** eon ($4.54$ to $4.0$ Ga) covers accretion, the Moon-forming impact ({ref}`Lecture 4 <lecture04>`), magma ocean solidification, and early crust and oceans.
Intact rocks are absent.
The record therefore relies on detrital **zircon** grains, chemically resistant zirconium-silicate minerals eroded from ancient crust.
Detrital zircons from Jack Hills date to $4.4$ Ga, with oxygen isotopes indicating liquid surface water and continental crust formed within $\sim$150 Myr of formation {cite:p}`Wilde2001`.

The **Archean** eon ($4.0$ to $2.5$ Ga) preserves the oldest continental rocks ($4.0$ Gyr), an active geodynamo by $3.45$ Ga {cite:p}`Tarduno2010`, early life, and an anoxic $\mathrm{N_2}$ and $\mathrm{CO_2}$ atmosphere with methane {cite:p}`Catling2020`.
The **Proterozoic** eon ($2.5$ Ga to $539$ Ma) spans from the Great Oxidation Event and Huronian glaciations ($\sim$2.4 Ga) to Neoproterozoic Snowball Earth episodes and the first macroscopic animals.
The **Phanerozoic** eon ($539$ Ma to present, meaning "visible life") encompasses animal and plant evolution, punctuated by mass extinctions at $252$ Ma and $66$ Ma ({ref}`Lecture 12 <lecture12>`).
Precambrian milestones in {numref}`fig:catling-precambrian` provide the foundation for habitability in {ref}`Lecture 13 <lecture13>` and {ref}`Lecture 14 <lecture14>`.

```{figure} figures/catling2020_precambrian_events.avif
:name: fig:catling-precambrian
:width: 100%
:align: center

Geologic time scale of the Precambrian with the major environmental and biological events, from the Moon-forming impact and the earliest evidence for life through the Great Oxidation Event ($\sim$2.4 Ga) to the Neoproterozoic glaciations and the first Ediacaran biota.
The left columns give the eons and eras; the annotations mark the atmospheric transition from an anoxic, reducing composition to an oxidising one with an ozone layer.
Reproduced from {cite:t}`Catling2020`.
```

{numref}`fig:earth-eons` highlights an extreme temporal imbalance.
Complex multicellular life occupies only the final $\sim$12% of Earth history, following $\sim$4 Gyr of microbial dominance.
Earth has represented distinct states over time: a Hadean water-world, an anoxic Archean planet, an oxygenating Proterozoic world, and the modern biosphere.
These distinct evolutionary stages govern the observable biosignatures discussed in {ref}`Lecture 14 <lecture14>`.

### Plate tectonics in action

As covered in {ref}`Lecture 7 <lecture07>`, Earth's lithosphere is divided into rigid plates that move over the ductile **asthenosphere**, the hotter mantle layer beneath.
New oceanic crust is created at mid-ocean ridges and consumed at subduction zones.
No oceanic crust is older than $\sim$200 Myr.
Continental crust resists subduction and contains rocks as old as $4.0$ Gyr.

Subduction is also the return leg of the carbon cycle.
Volcanic $\mathrm{CO_2}$ reacts with silicate minerals in the presence of liquid water to form carbonate sediments, which are subducted into the mantle and partly recycled to the atmosphere {cite:p}`KrissansenTotton2018`.
This cycle equilibrates atmospheric $\mathrm{CO_2}$ on a timescale of $\sim$0.5 Myr {cite:p}`Walker1981`.
Without subduction, carbon released from the interior accumulates in the atmosphere indefinitely, as on Venus ({numref}`fig:honing-carbon-cycle`).

```{figure} figures/honing2021_carbon_cycle_diagram.avif
:name: fig:honing-carbon-cycle
:width: 100%
:align: center

Schematic of the carbon cycle on a **stagnant-lid** Venus, a planet whose rigid outer shell forms a single immobile plate rather than being broken into moving tectonic plates, from {cite:t}`Honing2021`.
**Left:** the three carbon reservoirs (mantle, crust, atmosphere) are coupled by mantle degassing (volcanism), surface weathering of fresh basaltic crust, and decarbonation of buried carbonate when the crust heats up.
**Right:** the destabilising positive feedback loop. Increasing surface temperature shifts the geotherm (the profile of temperature with depth) upward, which pushes the decarbonation isotherm to *shallower* depth in the crust, releasing buried $\mathrm{CO_2}$ to the atmosphere and raising the surface temperature further. Without subduction, there is no return leg to the mantle to break the loop.
Reproduced from {cite:t}`Honing2021`.
```

### Earth's magnetic field and its consequences

Earth possesses a global magnetic field driven by the **geodynamo**, convection in the liquid outer core ({ref}`Lecture 4 <lecture04>`).
Surface field strengths are $25$ to $65$ microtesla.
Palaeomagnetic measurements of single zircon crystals show that this dynamo has operated for at least $3.45$ Gyr {cite:p}`Tarduno2010`.

The resulting **magnetosphere** deflects the solar wind into a cavity extending roughly $10\, \Rearth$ on the dayside.
It shields the surface from ionising radiation.
It suppresses atmospheric loss by eliminating **ion-pickup escape**, the acceleration of atmospheric ions by the solar-wind motional electric field across closed field lines.
Earth still loses hydrogen through **Jeans escape** (thermal loss of high-velocity atoms) and **polar wind** (ion outflow along open magnetic field lines near the poles).
These loss rates are far lower than the escape that desiccated Mars after its dynamo died around $4.1$ to $3.9$ Ga ({ref}`Lecture 10 <lecture10>`) and stripped early Venus under solar EUV radiation {cite:p}`Lammer2018`.
Venus lacks a detectable internal magnetic field today, a contrast explored in Part 2.

```{figure} figures/magnetosphere_anatomy_esa.avif
:name: fig:earth-magnetosphere
:width: 100%
:align: center

Structure of Earth's magnetosphere. The solar wind (orange arrows, arriving from the left) is deflected at the bow shock, and the shocked plasma flows around the planet through the magnetosheath. The magnetopause, where the solar-wind ram pressure balances the magnetic pressure of Earth's field, stands at roughly $10\,\Rearth$ on the dayside, while the nightside field is drawn out into the long magnetotail. This cavity shields the surface from most solar-wind particles and suppresses ion-pickup escape from the regions of closed field lines, in contrast to the open field lines at the poles that permit polar wind.
Credit: [ESA](https://www.esa.int/ESA_Multimedia/Images/2026/02/Anatomy_of_Earth_s_magnetosphere), [CC BY-SA 3.0 IGO](https://creativecommons.org/licenses/by-sa/3.0/igo/).
```

### The hydrosphere and cryosphere

The oceans hold $1.34 \times 10^{21}$ kg of water (about $97\%$).
This is a $2.7$ km global equivalent layer.
The **cryosphere** (the frozen water reservoir) holds $\sim$2% ({numref}`fig:blue-marble-apollo17`), with remaining water contributing $\sim$1%.

```{figure} figures/blue_marble_apollo17.avif
:name: fig:blue-marble-apollo17
:width: 100%
:align: center

"The Blue Marble", Apollo 17, 7 December 1972. Earth photographed by the crew en route to the Moon, with the hydrosphere and cryosphere visible together. Ocean covers most of the sunlit disk on both sides of Africa, from the South Atlantic in the west to the Indian Ocean in the east, while the Antarctic ice cap forms the bright cryosphere along the lower limb. Africa, the Arabian Peninsula, and Madagascar lie near the centre of the disk. NASA image AS17-148-22727. Credit: NASA / Apollo 17 crew.
```

Ocean circulation transports heat poleward, smoothing equator-to-pole temperature gradients.
The **ice-albedo feedback** ({ref}`Lecture 6 <lecture06>`), a positive feedback where growing ice amplifies cooling and shrinking warms, drove Snowball Earth glaciations.

The carbonate buffer balances dissolved $\mathrm{CO_2}$, $\mathrm{CO_3^{2-}}$, and $\mathrm{HCO_3^-}$.
Ocean $\mathrm{pH}$ stays near $8.1$.
This enables the carbonate-silicate cycle, whose Urey reaction sink precipitates atmospheric $\mathrm{CO_2}$ as seafloor carbonates ({numref}`fig:lammer-carbsil`).

```{figure} figures/lammer2018_carbonate_silicate.avif
:name: fig:lammer-carbsil
:width: 100%
:align: center

Cartoon of the **carbonate-silicate cycle** on a planet with active plate tectonics.
Atmospheric $\mathrm{CO_2}$ dissolves in rainwater to form weak carbonic acid, which weathers continental silicates into bicarbonate ions; rivers transport these to the ocean, where they are precipitated as carbonate rocks; subduction then returns the carbon to the mantle.
Volcanism completes the cycle by outgassing fresh $\mathrm{CO_2}$.
On geological timescales (of order $0.5$ Myr), this cycle stabilises the surface temperature against perturbations.
Reproduced from {cite:t}`Lammer2018`.
```

### Earth's climate system

Following {ref}`Lecture 5 <lecture05>` and {ref}`Lecture 6 <lecture06>`, Earth absorbs $240$ W/m$^2$ of solar radiation (albedo $\sim$0.30) and emits equally in the infrared.
Without an atmospheric greenhouse, the equilibrium temperature is $255$ K.
The natural greenhouse effect of water vapour and $\mathrm{CO_2}$ warms the surface by $33$ K to $288$ K.

The **faint young Sun problem** is the contradiction between a $30\%$ fainter early Sun at $4.4$ Ga and geological evidence for liquid water from at least $4.3$ Ga {cite:p}`Feulner2012`.
Higher early levels of $\mathrm{CO_2}$, and possibly $\mathrm{CH_4}$, most likely resolved this.
Silicate weathering then drew them down as the Sun brightened ({numref}`fig:zahnle-solar` and {numref}`fig:charnay-archean`).

```{figure} figures/zahnle2007_solar_evolution.avif
:name: fig:zahnle-solar
:width: 100%
:align: center

Solar luminosity (left axis, solid black curve) and EUV/X-ray flux (right axis, coloured curves) over the first $\sim$5 Gyr after the Sun reached the main sequence, normalised to present values.
The bolometric luminosity has risen by about $30\%$ since $4.5$ Ga, while the EUV and X-ray fluxes have dropped by factors of $10$--$1000$ from the young, magnetically active Sun.
The faint-young-Sun problem is the apparent contradiction between this lower bolometric flux and geological evidence for liquid water on early Earth.
Reproduced from {cite:t}`Zahnle2007`.
```

```{figure} figures/charnay2013_archean_temperature.avif
:name: fig:charnay-archean
:width: 100%
:align: center

Three-dimensional general-circulation model results for the global mean surface temperature of the Archean Earth between $3.8$ Ga and $2.5$ Ga, from {cite:t}`Charnay2013`.
Curves show solutions for three atmospheric compositions: $0.9$ mbar $\mathrm{CO_2}$ with $0.9$ mbar $\mathrm{CH_4}$ (blue), $10$ mbar $\mathrm{CO_2}$ with $2$ mbar $\mathrm{CH_4}$ (orange), and $0.1$ bar $\mathrm{CO_2}$ with $2$ mbar $\mathrm{CH_4}$ (red); solid lines include methane and dashed lines omit it.
The dotted green line marks the freezing point of water.
A few mbar of $\mathrm{CO_2}$ together with trace methane is marginal at $3.8$ Ga but warms by $3$ Ga, while $\sim$0.1 bar of $\mathrm{CO_2}$ together with trace methane comfortably resolves the faint-young-Sun problem at all three epochs.
Reproduced from {cite:t}`Charnay2013`.
```

On shorter timescales, **Milankovitch cycles** in orbital eccentricity, obliquity, and precession ($\sim$100 kyr, $41$ kyr, and $19\text{--}23$ kyr) pace Pleistocene glacial cycles with $\sim$8 K variations.
Over long timescales, liquid water has persisted continuously for at least $4$ Gyr.
Despite excursions from $\sim$240 K Snowball episodes to $\sim$300 K hothouses, the carbonate-silicate thermostat maintains surface liquid water.
This sets up the Venus comparison.

### Snowball Earth episodes

During the Cryogenian period, Earth experienced global glaciations documented by the **Sturtian** (roughly $717$ to $660$ Ma) and **Marinoan** ($645$ to $635$ Ma) episodes {cite:p}`Hoffman2017`.
Geological evidence includes **glacial diamictites** (poorly sorted glacial deposits) preserved within $10^\circ$ of the equator.
Banded iron formations returned after a billion-year absence.
These glacial layers are capped by thick **cap carbonates** that record an abrupt transition to warm greenhouse conditions immediately after deglaciation.

```{figure} figures/snowball_earth.avif
:name: fig:snowball-earth-cryogenian
:width: 100%
:align: center

Artist's impression of a fully ice-covered "snowball" Earth, with the continents buried under ice and only faint outlines visible. The bright frozen surface reflects most of the incoming sunlight; this high albedo is what makes the snowball state self-sustaining until volcanic $\mathrm{CO_2}$ accumulates enough to force deglaciation.
Credit: Oleg Kuznetsov (3depix.com), [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Snowball_Huronian.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

When polar ice caps expand past roughly $30^\circ$ latitude, runaway **ice-albedo feedback** (where increased surface reflectivity drives cooling) covers the globe in ice.
Surface temperatures drop to $\sim$240 K.
During this snowball state, frozen surfaces shut down silicate weathering.
Volcanism continues to outgas $\mathrm{CO_2}$ at roughly its normal rate.
Atmospheric $\mathrm{CO_2}$ accumulates over $\sim$10 Myr {cite:p}`Hoffman2017` until greenhouse forcing overcomes the ice albedo.
The ice then melts catastrophically in only $\sim$2 kyr.
Intense weathering of newly exposed silicate surfaces then rapidly draws down atmospheric $\mathrm{CO_2}$ to form cap carbonates.

These episodes demonstrate that the carbonate-silicate thermostat (the Walker feedback, {ref}`Lecture 6 <lecture06>`) operates symmetrically to rescue the planet from extreme cold states as well as warm ones.
While Venus failed by overheating, Earth nearly failed by freezing.
That Earth survived both is a measure of how robust the carbonate-silicate feedback is, provided liquid water and active volcanism both persist.

### Earth today in its long-term context

Anthropogenic climate change is a planetary-scale perturbation governed by the same greenhouse physics as Venus.

Atmospheric $\mathrm{CO_2}$ has risen from $280$ ppm pre-industrial to over $420$ ppm in $2024$.
This is the highest level in $\sim$3 Myr {cite:p}`IPCC2021`.
The current rate of $2$ to $3$ ppm/yr is roughly $100$ times faster than natural deglacial rates.
The net anthropogenic radiative forcing is about $2.7$ W/m$^2$, and the observed $1.1$ K of warming since the late nineteenth century is consistent with the response that climate models predict for this forcing {cite:p}`IPCC2021`.

```{figure} figures/lyons2014_oxygen_history.avif
:name: fig:lyons-oxygen
:width: 100%
:align: center

Evolution of Earth's atmospheric oxygen content through time, on a logarithmic scale of $p\mathrm{O_2}$ relative to present atmospheric level (PAL).
The atmosphere remained essentially anoxic ($p\mathrm{O_2} < 10^{-5}$ PAL) for the first $\sim$2 Gyr of Earth history, then rose abruptly during the **Great Oxidation Event** at $\sim$2.4 Ga, plateaued at intermediate values through the mid-Proterozoic, and rose again to near-modern levels in the Neoproterozoic and Phanerozoic.
The two-stage rise reflects the gradual buildup of the photosynthetic biosphere and shifting redox balance with the deep ocean and crust.
Reproduced from {cite:t}`Lyons2014`.
```

The carbonate-silicate thermostat cannot buffer climate on human timescales.
Silicate weathering equilibrates $\mathrm{CO_2}$ over $\sim$0.5 Myr, roughly five orders of magnitude slower than the perturbation.
Earth responds instead on timescales of ocean heat uptake (decades to centuries) and ice sheets (centuries to millennia).
Dissolution of $\mathrm{CO_2}$ also drives **ocean acidification**.
Seawater $\mathrm{H^+}$ rises by $30\%$, and surface ocean $\mathrm{pH}$ falls from $8.2$ to $8.1$.
The radiative physics that warms Venus to $737$ K operates on Earth.
The $4$-Gyr geological feedbacks cannot compensate on human timescales.

### The biosphere's geological footprint

The biosphere has rewritten Earth's surface chemistry in ways that distinguish it from Venus.
The **Great Oxidation Event** at $\sim$2.4 Ga marks the rise of atmospheric $\mathrm{O_2}$ from negligible Archean levels (pre-GOE $p_{\mathrm{O_2}} < 10^{-5}$ atm) to roughly $0.1\text{--}1\%$ of modern values, driven by oxygenic photosynthesis by cyanobacteria {cite:p}`Lyons2014` ({numref}`fig:lyons-oxygen`).
In the rock record, banded iron formations disappeared.
Redbeds (sediments reddened by iron oxide in an oxidising environment) appeared.
A second oxygenation step in the late Neoproterozoic raised $\mathrm{O_2}$ to near-modern values just before the Cambrian explosion.

Carbonate platforms, formed primarily by the calcification of marine organisms over the past $\sim$540 Myr, represent a substantial planetary $\mathrm{CO_2}$ sink.
On Earth, total carbon stored in surface and crustal reservoirs is on the order of $10^{20}$ kg, equivalent to a $\mathrm{CO_2}$ partial pressure of $\sim 100$ bar if returned to the atmosphere {cite:p}`Catling2017`.
This is comparable in order of magnitude to the $92$ bar of $\mathrm{CO_2}$ in the present-day Venus atmosphere.
Earth and Venus probably acquired comparable carbon inventories during accretion.
Earth stored its carbon in carbonates, but Venus retained it in the atmosphere.
The link between the biosphere and **biosignatures** (spectroscopic signatures of life used to characterise exoplanets) is taken up in {ref}`Lecture 13 <lecture13>` and {ref}`Lecture 14 <lecture14>`.

### The history of life on Earth

Earth's biosphere spans geological history, and its major transitions define the eon framework ({numref}`fig:earth-life-history`).

```{figure} figures/earth_life_timeline.avif
:name: fig:earth-life-history
:width: 100%
:align: center

Major events in the history of life on Earth, plotted on the eon strip of {numref}`fig:earth-eons`.
Stemmed markers give representative ages for the milestones discussed in the text, from the formation of Earth and the first liquid water oceans through the earliest biosignatures, the Great Oxidation Event, the first eukaryotes and multicellular algae, to the Ediacaran biota, the Cambrian explosion, and the end-Cretaceous impact.
Blue bands on the strip mark the Huronian and Neoproterozoic snowball glaciations.
Event ages are representative values from the cited literature {cite:p}`Mojzsis1996,Dodd2017,Nutman2016,Lyons2014,Catling2020,Hoffman2017`; eon boundaries follow {cite:t}`Gradstein2020`.
```

Crustal recycling destroyed most rocks from life's origin.
Traces older than $3.7$ Gyr are contested.
The oldest accepted fossils are **stromatolites**, layered mounds built by microbial mats, from the Pilbara at $3.48$ Ga {cite:p}`Catling2020`.
Modern stromatolites in Shark Bay ({numref}`fig:stromatolites`) provide an analogue for this dominant early life form.

```{figure} figures/stromatolites_shark_bay.avif
:name: fig:stromatolites
:width: 100%
:align: center

Modern stromatolites in the hypersaline waters of Shark Bay, Western Australia.
Microbial mats trap and bind sediment into these layered mounds; fossil stromatolites of the same construction, dated to $3.48$ Ga in the nearby Pilbara region, are the oldest widely accepted evidence for life on Earth.
Photo by Paul Harrison (Wikimedia Commons), [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/).
```

Life arose within a billion years after liquid oceans formed at $4.3$ to $4.4$ Ga.
Yet microbes dominated alone for $3$ Gyr.
The earliest **eukaryotes**, cells with nuclei and organelles, date to $\sim$1.87 Ga, and multicellular algae to $\sim$1.05 Ga {cite:p}`Catling2020`.
Animals appeared after the Neoproterozoic glaciations.
The soft-bodied **Ediacaran biota** date to $\sim$571 Ma, and the **Cambrian explosion** to $539$ Ma.
Complex life, punctuated by mass extinctions like the end-Cretaceous impact at $66$ Ma ({ref}`Lecture 12 <lecture12>`), spans only the final $12\%$ of Earth's history.

This history offers two lessons for planetary science.
First, because life arose fast while complexity arose slowly, microbial biospheres may be far more common than complex ones ({ref}`Lecture 13 <lecture13>`, {ref}`Lecture 14 <lecture14>`).
Second, atmospheric oxygen was negligible during life's first $2$ Gyr.
The inhabited Archean Earth therefore lacked an oxygen biosignature.
Both points build on the records in {numref}`fig:lyons-oxygen` and {numref}`fig:catling-precambrian`.

## Part 2: Venus, the alien twin

### Venus overview: why it is the twin and why it is not

Venus is the second planet from the Sun, with a semimajor axis of $0.723$ AU, mass $0.815\, \Mearth$, radius $0.950\, \Rearth$, and mean density $5.24$ g/cm$^3$ {cite:p}`NASAVenusFactSheet`.
By bulk measure, Venus is Earth's near-twin with a silicate mantle and iron core.

However, its surface and atmospheric conditions contrast sharply with Earth.
Surface pressure is $92$ bar and surface temperature reaches $737$ K.
The atmosphere is $96.5\%$ $\mathrm{CO_2}$ and $3.5\%$ $\mathrm{N_2}$, with sulfuric acid ($\mathrm{H_2SO_4}$) cloud droplets between $48$ and $70$ km altitude.
Venus exhibits **retrograde rotation** (rotation against the orbital direction).
The sidereal period is $243.0$ Earth days and the solar day $116.75$ Earth days.
It lacks a global magnetic field.
The internal dipole upper limit is $10^{-5}$ of Earth's field {cite:p}`Smrekar2018`.
The water inventory is only $20$ to $30$ ppm ($1$ to $3$ cm equivalent depth).
That is roughly $10^5$ times less than Earth's $2.7$ km.

```{figure} figures/widemann2023_three_missions_render.avif
:name: fig:venus-render
:width: 100%
:align: center

Artist's rendering of three new missions in the **Venus exploration decade** of the 2030s, against a global view of the planet from Akatsuki UV imaging.
NASA's VERITAS (left, top) will provide high-resolution radar topography and near-infrared surface emissivity; NASA's DAVINCI (right, top) will release an atmospheric descent probe; and ESA's EnVision (below) will provide synthetic-aperture radar mapping, atmospheric spectroscopy, and subsurface sounding.
Together these three missions will revolutionise Venus science, the first new orbital missions since Venus Express (2006--2014) and the first in-situ probes since Vega in 1985.
Reproduced from {cite:t}`Widemann2023`.
```

### Exploring Venus: the mission history

The history of Venus exploration breaks into three eras.
The first era, from $1962$ to $1985$, was dominated by Soviet Venera and Vega missions alongside early flybys.
Mariner 2 in $1962$ confirmed high surface temperatures.
This ruled out a habitable surface beneath the clouds.
Venera probes and landers between $1967$ and $1982$ returned the first in-situ atmospheric measurements, surface images, and basaltic chemical analyses.
The Vega missions in $1985$ deployed balloons that tracked cloud dynamics for $\sim$2 days.

The second era focused on orbital radar mapping, dominated by NASA's Pioneer Venus ($1978$ to $1992$) and Magellan ($1990$ to $1994$).
Magellan mapped $\sim$98% of the surface at $\sim$100 m resolution using **synthetic-aperture radar** (radar imaging that penetrates cloud cover).
This mapping provides the global topographic dataset for Venus geology.
Pioneer Venus also carried an atmospheric probe that measured noble gas isotopic ratios to constrain atmospheric history.

The third era began after a long gap with ESA's Venus Express ($2006$ to $2014$) and JAXA's Akatsuki ($2015$ to present).
Venus Express measured atmospheric dynamics, surface thermal emission, and hydrogen and oxygen escape rates.
Akatsuki provided UV and infrared imaging.
Because no orbital mission flew between 1994 and 2006 and no in-situ probe has visited since 1985, the planetary dataset has substantial observational gaps.
Three new orbiters and probes planned for the 2030s (NASA's VERITAS and DAVINCI, and ESA's EnVision) aim to resolve these questions ({numref}`fig:venus-render`).

### Venus surface morphology

The primary diagnostic observation of Venus' surface is its **hypsometry**, the statistical distribution of surface elevations across a planet.
Earth displays a bimodal hypsometry because plate tectonics produces low basaltic ocean basins (around $-4$ km) and high granitic continents (around $0$ to $+1$ km) in distinct isostatic equilibria.
In contrast, Venus exhibits a unimodal hypsometry with a single broad elevation peak and no continent-ocean dichotomy.
This unimodal distribution indicates that Venus lacks Earth-like plate tectonics {cite:p}`Smrekar2018`.

```{figure} figures/smrekar2018_earth_venus_topography.avif
:name: fig:earth-venus-topo
:width: 75%
:align: center

Global topographic maps of **Earth** (top), **Venus** (middle, from Magellan radar altimetry), and the gravity-derived geoid of Venus (bottom, the equipotential surface defined by the planet's gravity field), all displayed at the same horizontal resolution and on the same colour scale.
Earth's bimodal pattern (deep ocean basins vs. continents) is conspicuously absent on Venus, which shows broad volcanic plains, scattered highlands, and a narrow elevation range.
Reproduced from {cite:t}`Smrekar2018`.
```

The surface of Venus is dominated by **volcanic plains**, broad flood-basalt expanses that cover about $80\%$ of the planet ({numref}`fig:venus-terrains`).
Embedded within these plains are **tesserae**, elevated plateaus covering roughly $8\%$ of the surface that represent the oldest mapped terrain and record complex tectonic deformation.
Near-infrared emissivity measurements suggest that some tesserae may have felsic compositions, which would indicate ancient water-rock interaction and early liquid surface water {cite:p}`Widemann2023`.

**Coronae** are circular volcano-tectonic structures unique to Venus.
They range from about $100$ to $1000$ km in diameter.
They represent the surface expression of upwelling mantle plumes, characterized by annular fractures, raised rims, and volcanic edifices.
These structures reflect stagnant-lid volcanism, where internal heat escapes through localized plumes rather than plate-tectonic recycling.
Gravity observations indicate that some coronae overlie active mantle plumes today.

```{figure} figures/widemann2023_venus_geological_terrains.avif
:name: fig:venus-terrains
:width: 100%
:align: center

Global geological-terrain map of Venus from {cite:t}`Widemann2023` Fig. 15, overlaid on a Magellan radar base. Coloured polygons are the Regions of Interest (RoIs) defined in the ESA EnVision Science Operations Reference Scenario; together they cover roughly 30% of Venus's surface and span the major terrain classes: **plains** (light green), **tessera** highlands (tan), **deformed terrain** (pale yellow), **rift zones** (red), **Artemis chasma** (purple), and **craters** (grey). Named regional landmarks (Maxwell Montes, Fortuna Tessera, Ishtar Terra, Beta Regio, Aphrodite Terra, Alpha Regio, and others) are labelled. Terrain classification after {cite:t}`IvanovHead2015`; reproduced from {cite:t}`Widemann2023`.
```

Venus has a low **impact crater density**.
This corresponds to a young average crater retention age of $150$ to $250$ Myr {cite:p}`Smrekar2018`.
This young surface age implies that widespread resurfacing erased the earlier cratering record.
Two end-member models explain this resurfacing: **catastrophic resurfacing**, proposing a global lithospheric overturn roughly $500$ Myr ago, and **steady-state resurfacing**, proposing continuous and uniform volcanic renewal.
Because the spatial distribution of craters is consistent with random, intermediate models involving episodic regional resurfacing are considered most likely {cite:p}`Widemann2023`.

### Venus interior and tectonic regime

Venus' interior structure is inferred primarily from gravity data, rotation rate, and theoretical extrapolation from Earth.
The Magellan gravity field ({numref}`fig:earth-venus-topo`) is mapped to spherical harmonic degree $\sim$70.
It shows a strong correlation between long-wavelength gravity and topography {cite:p}`Smrekar2018`.
This correlation indicates that topography is supported by deep mantle density anomalies (mantle plumes and downwellings) rather than purely lithospheric flexure, pointing to mantle dynamics distinct from Earth's.

Given its similar uncompressed bulk density, Venus likely has an Earth-like bulk composition with an iron-nickel core, silicate mantle, and basaltic crust.
However, whether the core is liquid or solid remains unknown.
This is because the slow rotation rate makes the moment of inertia difficult to determine.
We also lack constraints on mantle temperature, lower mantle composition, and **inner-core nucleation**, the onset of solid-core crystallisation from the surrounding liquid core.
Future radio-science measurements from VERITAS and EnVision aim to determine the moment of inertia and tidal **Love numbers**, dimensionless parameters describing how much a planet deforms under tidal forcing, to constrain core state.

Present-day Venus operates in a **stagnant-lid** regime, where the lithosphere forms a single globally connected shell without plate boundaries or subduction zones.
As discussed in {ref}`Lecture 7 <lecture07>`, the tectonic regime depends on mantle viscosity and lithospheric state, which vary strongly with water content because dry rock is much stiffer.
The leading hypothesis suggests that mantle dehydration following the loss of surface water raised mantle viscosity.
This would prevent mobile-lid convection.
Under this scenario, Venus may have transitioned from an early mobile-lid regime to a stagnant lid as it dried ({numref}`fig:venus-tectonic-evol`).

```{figure} figures/smrekar2018_venus_tectonic_evolution.avif
:name: fig:venus-tectonic-evol
:width: 100%
:align: center

Surface temperature evolution of Venus over $\sim$4.5 Gyr from a numerical tectonic-regime model, from the bottom panel of {cite:t}`Smrekar2018`.
The boxed labels mark successive **stagnant-lid**, **mobile-lid**, **stagnant-lid**, and **episodic-lid** intervals.
The episodic-lid phase produces the resurfacing pulses inferred from present-day crater statistics; the mantle-temperature and volcanic-production-rate panels of the same model (not reproduced here) show the corresponding pulses in interior heat transport.
```

Alternatively, an **episodic-lid** model proposes that a normally stagnant lithosphere becomes unstable every $\sim$500 Myr, undergoing brief episodes of global subduction and volcanism before returning to stagnant behaviour.
This model naturally explains the resurfacing inferred from crater statistics.
Other models remain viable, however.
Distinguishing between these tectonic scenarios is currently hindered by the lack of seismic, heat-flow, or detailed gravity data.

The absence of a Venusian magnetic field is also tied to its interior state ({ref}`Lecture 4 <lecture04>`).
For a planetary dynamo to operate, core convection requires either efficient thermal cooling by the mantle or compositional buoyancy from inner-core freezing.
On Venus, the stagnant lid insulates the core and impedes heat flow across the core-mantle boundary.
This can suppress thermal convection.
Without inner-core nucleation, the core lacks the compositional buoyancy that helps power Earth's dynamo.
Because dynamo action can persist even at slow rotation rates, inefficient core cooling and a possible lack of inner-core nucleation are the leading explanations for the lack of a dynamo.

### Venus atmosphere: structure and dynamics

The vertical structure of the Venusian atmosphere provides key contrasts with Earth that motivate the runaway greenhouse derivation following {ref}`Lecture 5 <lecture05>` and {ref}`Lecture 6 <lecture06>`.

The composition is overwhelmingly $\mathrm{CO_2}$ ($96.5\%$), with $\mathrm{N_2}$ ($3.5\%$) the only other major species.
Trace gases include $\mathrm{SO_2}$ at $\sim$150 ppm, water vapour at $\sim$30 ppm, and noble gases that preserve the history of volatile delivery and degassing.
A high primordial $^{36}$Ar abundance shows that Venus holds a larger primordial noble-gas inventory than Earth {cite:p}`Lammer2018`.
In contrast, the atmospheric $^{40}$Ar/$^{36}$Ar ratio of $\approx 1.1$ (compared with $\approx 300$ on Earth) indicates that only $\sim 10$ to $34$% of radiogenic $^{40}$Ar has outgassed compared with $\sim 50$% on Earth, so Venus has outgassed less of its mantle volatile inventory {cite:p}`Gillmann2022`.

The thermal profile is roughly adiabatic from the surface ($T_s = 737$ K, $P_s = 92$ bar) up to about $65$ km altitude at the cloud tops.
The atmospheric **scale height**, the characteristic vertical distance over which pressure decreases by a factor of $e$, is about $16$ km at the surface compared with $\sim 8$ km on Earth.
This difference is evaluated using the hydrostatic scale height from {ref}`Lecture 5 <lecture05>`:

$$
H = \frac{\kB T}{m\, g}.
$$

Plugging in $T = 737$ K, $m = 7.30 \times 10^{-26}$ kg for $\mathrm{CO_2}$, and $g = 8.87$ m/s$^2$ gives $H \approx 1.57 \times 10^4$ m, or $\sim 16$ km.
For Earth ($T = 288$ K, $m = 4.81 \times 10^{-26}$ kg, $g = 9.81$ m/s$^2$), $H \approx 8.4$ km.
This factor-of-two difference is set primarily by the higher temperature ratio $T_{\mathrm{Venus}} / T_{\mathrm{Earth}} \approx 2.55$, which outweighs the heavier molecular weight of $\mathrm{CO_2}$.
Above the clouds, temperature decreases through the mesosphere and rises in the thermosphere where solar EUV is absorbed.

The cloud system consists of three vertically stacked layers between roughly $48$ and $70$ km altitude.
Solar UV photolyses $\mathrm{SO_2}$ to form $\mathrm{SO_3}$.
This combines with water vapour to produce $\mathrm{H_2SO_4}$ droplets.
These clouds are optically thick with a visible-band albedo of $\sim 0.77$.
They form the effective radiating surface at visible and near-IR wavelengths.
An unidentified UV absorber produces banded features at the cloud tops, while contested trace detections such as phosphine ($\mathrm{PH_3}$) were examined in {ref}`Lecture 6 <lecture06>`.

Atmospheric circulation is dominated by **super-rotation**, where the atmosphere rotates substantially faster than the underlying solid planet.
The cloud-top atmosphere circles Venus in roughly $4$ Earth days (moving roughly $60$ times faster than the surface), in a direction opposed to the solid planet rotation of $243$ Earth days.
Maintaining this circulation against surface friction requires upward angular momentum transport by thermal tides and planetary-scale waves.

### The runaway greenhouse and how Venus locked into it

A one-layer grey greenhouse model ({ref}`Lecture 5 <lecture05>`) gives:

$$
T_s^4 = 2\, T_{\mathrm{eq}}^4,
\qquad
T_{\mathrm{eq}} = \left[ \frac{S\, (1-A)}{4\, \sigma} \right]^{1/4},
$$

yielding $T_s \approx 1.19\, T_{\mathrm{eq}}$.
For Earth ($S_\oplus = 1361$ W/m$^2$, $A = 0.30$), this gives $T_s \approx 303$ K, close to the observed $288$ K.
For Venus ($S_{\mathrm{Venus}} = 2604$ W/m$^2$, $A \approx 0.77$), it predicts $T_s \approx 270$ K.
The observed Venus surface temperature of $737$ K is far hotter than predicted.
The reason is that a dense atmosphere lifts the infrared photosphere far above the surface.

Warming increases atmospheric water vapour via the Clausius-Clapeyron relation.
This strengthens the greenhouse effect.
When absorbed solar flux exceeds the maximum outgoing longwave radiation (OLR) that a moist atmosphere can emit, the planet enters a **runaway greenhouse**, a state where oceans evaporate completely.
This upper bound is the **Simpson-Nakajima limit**, the maximum OLR a water-rich atmosphere can radiate to space ({cite:t}`NakajimaIngersoll1992`; {numref}`fig:kopparapu-runaway`, {numref}`fig:goldblatt-spectrum`).

```{figure} figures/kopparapu2013_runaway_panels.avif
:name: fig:kopparapu-runaway
:width: 100%
:align: center

Climate-model calculation of the runaway greenhouse limit and the inner edge of the habitable zone for an Earth-like planet, from {cite:t}`Kopparapu2013` Fig. 3.
Panel (a): outgoing longwave radiation (OLR) as a function of surface temperature, showing the asymptote to a maximum value of $\sim 291$ W/m$^2$ at high surface temperatures (the corresponding {cite:t}`Goldblatt2013` line-by-line calculation gives $\sim 282$ W/m$^2$; the small offset is due to the H$_2$O continuum treatment).
Panel (b): planetary albedo.
Panel (c): the ratio of stellar flux to the present solar constant required for radiative equilibrium, with the **runaway greenhouse** limit at $S_{\mathrm{eff}} = 1.06$ ($\Rightarrow$ inner habitable-zone edge at $\sim$0.97 AU for present-day solar luminosity) and the **moist greenhouse** limit, reached at slightly lower flux, where the stratosphere becomes wet enough to drive enhanced hydrogen escape without full ocean vaporisation, at $S_{\mathrm{eff}} = 1.015$ ($\sim$0.99 AU).
Panel (d): the corresponding atmospheric water vapour mixing ratio profile at $T_s = 320$, $340$, and $360$ K.
Once $S_{\mathrm{eff}}$ exceeds the runaway threshold, no equilibrium with liquid surface water is possible.
Reproduced from {cite:t}`Kopparapu2013`.
```

```{figure} figures/goldblatt2013_olr_spectrum.avif
:name: fig:goldblatt-spectrum
:width: 100%
:align: center

Thermal-radiance spectra of an Earth-like atmosphere as a function of wavelength for surface temperatures $T_\mathrm{s} = 280, 310, 340, 370, 400$ K (bottom to top), from {cite:t}`Goldblatt2013` Fig. 3(b).
Black and red curves are two independent line-by-line model calculations; grey dotted curves show the blackbody reference at each $T_\mathrm{s}$.
As $T_\mathrm{s}$ rises from 280 K to 400 K, the H$_2$O continuum absorbs an ever-larger fraction of the thermal emission across the infrared, and the 8–14 $\mu$m atmospheric window closes.
Above $T_\mathrm{s} \sim 340$ K the integrated outgoing flux saturates at the **runaway-greenhouse asymptote** of $\sim 282$ W m$^{-2}$ (cf. {numref}`fig:kopparapu-runaway`): further surface warming no longer produces a compensating increase in emission to space.
Reproduced from {cite:t}`Goldblatt2013`.
```

Radiative transfer calculations place the Simpson-Nakajima limit at approximately $280\text{--}310$ W/m$^2$ {cite:p}`Goldblatt2013`.
Earth absorbs about $240$ W/m$^2$, remaining below this limit.
Venus, at $0.723$ AU, absorbs roughly $1.91 \times$ more stellar flux per unit area.
This exceeds the threshold ({numref}`fig:zahnle-runaway`).
Upper-atmospheric water photolysed and hydrogen escaped to space.
The result is the dry, $\mathrm{CO_2}$-dominated, $737$ K surface observed today.

```{figure} figures/zahnle2007_runaway_threshold.avif
:name: fig:zahnle-runaway
:width: 100%
:align: center

Surface temperature as a function of net insolation plus geothermal heat flow for a steam atmosphere over a magma ocean, from {cite:t}`Zahnle2007` (after {cite:t}`Kasting1988` and Abe \& Matsui 1988).
The radiated cooling rate is equal to the sum of absorbed sunlight and geothermal heat flow.
The plot shows the surface temperature as a function of this combined heat input for different amounts of atmospheric $\mathrm{H_2O}$ (in bars).
The runaway greenhouse threshold appears as a *vertical* boundary near $\sim$300 W/m$^2$ on the heat-flow axis (the "Runaway Greenhouse Limit" line in the figure): no steady state with a solid crust exists to its left, and for net heat fluxes only modestly above this value the surface stays molten beneath a thick steam atmosphere.
Reproduced from {cite:t}`Zahnle2007`.
```

## Blackboard derivation: The Simpson-Nakajima runaway greenhouse limit

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

To solve Eq. {eq}`eq:photosphere-pressure` for $T_{\mathrm{phot}}$, substitute the Clausius-Clapeyron form of the saturation curve and take the logarithm of both sides:

$$
\ln p_{\mathrm{ref}} - \frac{L}{R_v}\left(\frac{1}{T_{\mathrm{phot}}} - \frac{1}{T_{\mathrm{ref}}}\right) = \ln\frac{g}{\kappa}
$$

Collecting the $1/T_{\mathrm{phot}}$ term on one side, $\frac{L}{R_v T_{\mathrm{phot}}} = \ln(p_{\mathrm{ref}} \kappa / g) + L/(R_v T_{\mathrm{ref}})$, and inverting:

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
The inner habitable zone edge has therefore been moving **outward** over Solar System history as the Sun brightens.
The question of whether Venus was once inside the habitable zone (and if so, for how long) becomes a question of when the receding inner edge crossed the orbit of Venus from the inside.

```{figure} figures/wordsworth2013_OLR_ASR_equilibria.avif
:name: fig:wordsworth-equilibria
:width: 100%
:align: center

OLR (red), ASR (absorbed shortwave radiation, blue), and OLR$-$ASR (bottom) as a function of surface temperature for an atmosphere with $100$ ppm $\mathrm{CO_2}$ at a stellar flux of $F = 1.025\, F_0$, from {cite:t}`Wordsworth2013`.
There are three thermal equilibria (two stable, marked by crosses, and one unstable, marked by the open circle), illustrating that runaway-greenhouse atmospheres can have multiple solutions for the same incoming stellar flux.
This bistability is one mechanism for the **hysteresis** between wet and dry climate states discussed below.
Reproduced from {cite:t}`Wordsworth2013`.
```

### When did Venus lose its water?

The Simpson-Nakajima limit makes a runaway greenhouse inevitable.
The timing of the transition remains unresolved ({numref}`fig:wordsworth-equilibria`).

In the **early loss** scenario, a primordial steam atmosphere prevents magma-ocean solidification, sustaining rapid water loss ({numref}`fig:hamano-two-types` and {numref}`fig:hamano-typeI`) {cite:p}`Hamano2013`.
Coupled magma-ocean models find a prolonged lifetime of $\sim$10 Myr ({numref}`fig:lebrun-magma`) {cite:p}`Lebrun2013`.

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
:width: 100%
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
:width: 100%
:align: center

Time evolution of potential temperature (black line) and surface temperature (grey line) for a crystallising magma ocean coupled to its outgassed steam atmosphere on a Venus-mass planet at the orbital distance of Venus, from panel (a) of {cite:t}`Lebrun2013` Fig. 12.
The three vertical regions ("totally molten", "partially molten", "mush") track the planetary mantle as it crystallises; condensation of water vapour occurs at the boundary between the partially molten and mush stages.
The dashed vertical line marks the time at which the magma ocean reaches $98\%$ solidification, $\sim 10$ Myr at Venus' orbital distance (compared with $\sim 1.5$ Myr at Earth's and $\sim 0.1$ Myr at Mars' for the corresponding panels (b) and (c) of the same figure, not shown).
The longer magma-ocean lifetime at smaller heliocentric distances gives the steam atmosphere ample time to photolyse and lose hydrogen to space, providing the foundation of the early-loss scenario for Venus.
{cite:t}`Lebrun2013` further showed (their Fig. 11, not shown) that below a critical distance of about $0.66$ AU around a Sun-like star, an Earth-mass planet's magma ocean cannot freeze at all and the planet remains molten indefinitely; Venus at $0.72$ AU sits just outside this limit.
```

In the **late loss** scenario, Venus condensed a surface ocean and remained temperate for billions of years {cite:p}`Way2016`, and substellar clouds reflected sunlight until water loss occurred within the last $\sim$1 Gyr ({numref}`fig:way-paleo`).

```{figure} figures/way2016_paleo_venus_temperature.avif
:name: fig:way-paleo
:width: 100%
:align: center

Three-dimensional climate model simulation of the surface air temperature on a hypothetical paleo-Venus at $2.9$ Ga with $75\%$ of present solar irradiance, from panel (a) of {cite:t}`Way2016` Fig. 2, plotted on a Mollweide global projection.
Surface temperatures range from below freezing in polar regions to about $40^\circ$C at the equator, suggesting that an early Venus could have hosted long-lived liquid surface water.
{cite:t}`Way2016` confirmed similar temperate conditions for several variants (different epochs, modern Earth topography in place of Venusian topography, faster rotation), shown in panels (b)-(d) of the same figure (not reproduced here).
```

Three-dimensional simulations show that water clouds preferentially form on the nightside ({numref}`fig:turbet-clouds`) {cite:p}`Turbet2021`.
Nightside cloud warming prevents ocean condensation.
This traps Venus in a runaway state ({numref}`fig:turbet-hysteresis`).

```{figure} figures/turbet2021_water_clouds_emission.avif
:name: fig:turbet-clouds
:width: 100%
:align: center

Three-dimensional simulations of an initially hot and steamy Earth (**a**, **c**) and Venus (**b**, **d**), both forced to a stellar flux $S = 340.5$ W/m$^2$, the present-day Earth insolation.
The upper row shows the vertically integrated water-cloud column and the lower row the thermal emission to space.
The maps are in the heliocentric frame, so subsolar longitude $0^\circ$ is the substellar point and $\pm 180^\circ$ the antistellar point.
In both cases the clouds are concentrated on the night-side, where they act as a greenhouse blanket and cut the thermal cooling to space, so the emission maps are anticorrelated with the cloud maps.
The substellar region stays comparatively cloud-free, which keeps the planetary albedo low.
The two planets rotate at very different rates, Earth with $P_\mathrm{rot} \approx 24$ h and Venus with $P_\mathrm{rot} \approx 5833$ h, about 243 times longer, yet the same night-side cloud pattern appears in both, so the mechanism does not depend on slow rotation.
Reproduced from {cite:t}`Turbet2021`, Fig. 2a-d.
```

```{figure} figures/turbet2021_hysteresis.avif
:name: fig:turbet-hysteresis
:width: 100%
:align: center

Hysteresis loops for ocean formation on early Earth and Venus, from {cite:t}`Turbet2021`.
**Panel (a)** shows surface temperature as a function of incoming solar flux for Earth: at $4$ Ga, water condenses from a steam atmosphere if the atmosphere is initially condensed (operating point near present-day) but enters the runaway greenhouse if it starts hot (red branch).
**Panel (b)** shows the same for Venus: the runaway and condensed branches do not overlap, so an early Venus that started in the runaway state (the natural endpoint of magma ocean cooling at high solar flux) cannot reach the condensed branch even at $4$ Ga, when the insolation at Venus was $\sim$25% lower than today and Venus still received $\sim$500 W/m$^2$, well above the cloud-modified condensation threshold of $\sim$325 W/m$^2$.
Reproduced from {cite:t}`Turbet2021`, Fig. 4.
```

Both early-loss and late-loss scenarios remain observationally untested ({numref}`fig:gillmann-scenarios`), and future measurements of noble gases and crustal composition may distinguish between an early ocean ({numref}`fig:honing-reference`) and a dry history ({numref}`fig:constantinou-pathways`).

```{figure} figures/gillmann2022_dry_wet_venus_scenarios.avif
:name: fig:gillmann-scenarios
:width: 100%
:align: center

The two main scenarios for Venus' early evolution as summarised by {cite:t}`Gillmann2022`.
**Top branch** (Dry Venus, Hamano-style): the magma ocean never crystallises with a condensed surface, water photolyses early, and the planet emerges desiccated within $\sim$100 Myr.
**Bottom branch** (Wet Venus, Way-style): the magma ocean crystallises, an ocean condenses, the planet remains habitable for several Gyr, and the runaway greenhouse is triggered later by gradual loss of water and the slow rise of solar luminosity.
Both end at the present state of Venus, and current data cannot distinguish them definitively.
Reproduced from {cite:t}`Gillmann2022`.
```

```{figure} figures/honing2021_reference_evolution.avif
:name: fig:honing-reference
:width: 100%
:align: center

Reference scenario for the coupled interior-atmosphere evolution of a stagnant-lid Venus from panels (a) and (b) of {cite:t}`Honing2021` Fig. 3.
**Left panel:** carbon reservoirs (atmosphere, crust, atmosphere+crust, atmosphere with weathering switched off) as a function of time after solidification.
**Right panel:** surface temperature with (blue) and without (green) silicate weathering.
Surface weathering keeps the planet temperate for $\sim 0.9$ Gyr; once water is lost, decarbonation drives the runaway accumulation of $\mathrm{CO_2}$ to a Venus-like end state.
The remaining panels (c)-(f) of the original figure (not reproduced here) show the corresponding evolution of carbon fluxes, atmospheric water vapour, layer depths, and interior temperatures.
```

```{figure} figures/constantinou2024_venus_pathways.avif
:name: fig:constantinou-pathways
:width: 100%
:align: center

The two dichotomous climate pathways for Venus from {cite:t}`Constantinou2024`, ending in interiors with very different water inventories.
**Upper branch (dry Venus):** the planet emerges from its magma-ocean stage at $t \approx 100$ Myr without ever condensing a surface ocean; water is lost early via photolysis and hydrogen escape, leaving an interior depleted in hydrogen and a present-day mantle that degasses S- and C-rich, $\mathrm{H_2O}$-poor volcanic gases.
**Lower branch (temperate, wet Venus):** the magma ocean crystallises with a condensed ocean at the surface, the planet remains habitable for several Gyr, and the present-day mantle still contains significant water that emerges in $\mathrm{H_2O}$-rich volcanic gases.
The two interior signatures map onto observable differences in the chemistry of Venus' atmosphere. {cite:t}`Constantinou2024` argue from the destruction rates of $\mathrm{H_2O}$, $\mathrm{CO_2}$, and $\mathrm{OCS}$ in the present atmosphere that the volcanic source must be water-poor (at most $\sim$6\% $\mathrm{H_2O}$ mole fraction), favouring the dry-Venus branch.
Reproduced from {cite:t}`Constantinou2024`.
```

### The D/H ratio: evidence for water loss

The **deuterium-to-hydrogen ratio** (D/H) provides strong empirical evidence that Venus once possessed at least $100\times$ more water than today.
Early measurements gave an atmospheric $D/H \approx 1.6 \times 10^{-2}$ for Venus, about $100$ times the terrestrial standard mean ocean water value ($D/H = 1.56 \times 10^{-4}$) {cite:p}`Donahue1982`, and later analyses revised the enrichment factor to $\sim 150 \pm 30$ {cite:p}`Donahue1997`.

Lighter hydrogen molecules acquire higher thermal velocities, so they escape more efficiently than deuterium.
The remaining reservoir is progressively enriched in deuterium.
This process follows **Rayleigh distillation** (isotopic fractionation during reservoir loss) {cite:p}`Hunten1987`.
If $f$ is the remaining hydrogen fraction and $\alpha < 1$ is the fractionation factor (the ratio of deuterium to hydrogen escape efficiencies), the present isotopic ratio $R$ relative to the initial ratio $R_0$ obeys

$$
\frac{R}{R_0} = f^{(\alpha - 1)}.
$$

The fractionation factor $\alpha$ depends on the escape regime: $\alpha \approx m_{\mathrm{H}}/m_{\mathrm{D}} \approx 0.5$ in the mass-ratio limit, and $\alpha \approx \sqrt{m_{\mathrm{H}}/m_{\mathrm{D}}} \approx 0.71$ in the thermal-velocity limit.
Setting $R/R_0 = 150$ and solving $f = 150^{1/(\alpha-1)}$ yields $f_{\mathrm{mass}} \approx 150^{-2} \approx 4 \times 10^{-5}$ and $f_{\mathrm{thermal}} \approx 150^{-3.4} \approx 4 \times 10^{-8}$.
Multiplying the present water column ($\sim 2$ cm of global equivalent layer) by $1/f$ implies an initial inventory of several hundred metres for the mass-ratio case, but an unphysical several hundred kilometres (more than 100 Earth-ocean masses) for the thermal-velocity case.
This contradiction shows that Venusian escape combined an early hydrodynamic phase with $\alpha$ near unity and a later diffusion-limited phase that produced the observed enrichment.
Under this lower-bound argument, the original Venusian water inventory was at least $\sim 100$ times the present value.

The D/H ratio provides direct evidence that Venus lost most of its primordial water to space.
Photolytic $\mathrm{O_2}$ buildup and interior oxidation accompanied the loss ({numref}`fig:wordsworth-abiotic-o2`).
However, D/H alone cannot determine whether water loss occurred early during a magma-ocean phase or over billions of years as solar EUV flux declined.
Future noble gas measurements, particularly $^{36}$Ar/$^{38}$Ar and Xe isotopic ratios from the DAVINCI probe, will help distinguish between these escape histories.

```{figure} figures/wordsworth2014_abiotic_o2_schematic.avif
:name: fig:wordsworth-abiotic-o2
:width: 100%
:align: center

Schematic of the abiotic build-up of an $\mathrm{O_2}$-dominated atmosphere by photolytic water loss on a terrestrial habitable-zone planet, from {cite:t}`Wordsworth2014`.
**Top:** during the early phase, stellar XUV flux photolyses atmospheric water vapour into hydrogen and oxygen; the lighter hydrogen escapes preferentially to space, while oxygen accumulates either in the atmosphere or condenses onto surface regions of low net instellation.
**Bottom:** once enough $\mathrm{O_2}$ has built up, the planet enters a stable state in which continued $\mathrm{H_2O}$ photolysis and hydrogen escape are balanced by oxidation of the planetary interior.
The same chain of processes (water photolysis, hydrogen escape, oxygen sinks) is the operative mechanism for desiccating Venus, and it leaves the residual D/H ratio enriched by the factor of $\sim$150 observed on present-day Venus.
Reproduced from {cite:t}`Wordsworth2014`.
```

### Volcanic activity today: is Venus alive?

Whether Venus is currently volcanically active has long been debated.
Indirect evidence includes factor-of-several variations in upper-atmosphere $\mathrm{SO_2}$ concentrations over the $40$-year baseline of Pioneer Venus, Magellan, and Venus Express observations.
Episodic volcanic outgassing is the likely cause.
Venus Express detected near-IR thermal emission anomalies over Idunn Mons consistent with cooling from recent lava flows.

Direct evidence arrived in $2023$, when {cite:t}`HerrickHensley2023` reanalysed Magellan radar data from $1990$ to $1992$ and identified morphological changes in a volcanic vent on the flank of Maat Mons.
Between observation cycles, the vent enlarged, changed from circular to irregular, and developed surrounding terrain consistent with a fresh lava flow.
This spacecraft observation provides the first direct evidence of an active eruption on Venus.
Modern resurfacing is at least episodic and continues to supply $\mathrm{CO_2}$ and $\mathrm{SO_2}$ to the atmosphere.

A key open question is whether this volcanic flux is comparable to Earth's or much smaller.
Because volcanic outgassing must roughly balance atmospheric sinks in steady state, the gas flux is tied to surface basalt weathering and cloud-deck chemistry.
The rates of these reactions remain uncertain by orders of magnitude.
Their measurement is a primary goal of EnVision and DAVINCI.

## Part 3: Comparative payoff

### Why did Earth and Venus diverge?

Earth and Venus began from similar initial conditions but followed divergent paths.
This divergence arose from four physical inputs and the nonlinear feedbacks that amplified their differences.

The first input is **solar flux**, the solar power received per unit area.
At $0.723$ AU, Venus receives $1.91 \times$ the solar flux of Earth at $1$ AU.
Today, Venus lies above the Simpson-Nakajima limit and Earth sits below it, but under a faint young Sun early Venus was near this threshold, governed by cloud feedbacks.
An orbital difference of $0.05$ AU could have swapped their evolutionary outcomes.

The second input is the timing of water delivery.
Both planets accreted in the same disk region with similar initial water inventories.
Mantle isotopic tracers suggest that water, if it arrived with the carbonaceous material, was delivered mainly during main accretion rather than with the late veneer ({numref}`fig:dauphas-accretion`).

```{figure} figures/dauphas2017_earth_accreting_material.avif
:name: fig:dauphas-accretion
:width: 100%
:align: center

Probability density function for the chromium-bearing fraction of Earth's accreting mass as a function of the cumulative accreted mass fraction, from {cite:t}`Dauphas2017` (Cr panel of their five-isotope Fig. 1).
In the paper's notation, $x_{0.95} = 0.85$ for Cr: $95\%$ of Earth's present mantle Cr inventory arrived during the final $85\%$ of accretion, and the red triangle on the $x$-axis marks the start of this terminal window at $1 - x_{0.95} = 0.15$.
Mass-proportional delivery would give $x_{0.95} = 0.95$, so Cr is delivered approximately proportionally to accreted mass (described by the paper as "nearly linear"), in contrast to Mo and Ru, which are strongly back-loaded toward the final stages of accretion.
Combined with the O, Ti, Ni, Mo, and Ru tracers from the same study (not reproduced here), {cite:t}`Dauphas2017` reconstruct three accretion stages: stage I ($0\text{--}60\%$ of Earth's mass) is best fit by $\sim 51\%$ enstatite-meteorite-like (E-type) plus $\sim 40\%$ ordinary-chondrite plus $\sim 9\%$ carbonaceous-chondrite (CO/CV) material; stages II ($60\text{--}99.5\%$) and III (the last $0.5\%$, the "late veneer") are essentially $100\%$ E-type.
The carbonaceous component, and therefore the bulk of Earth's water if it was delivered with that material, was concentrated in the early stages of main accretion rather than in the late veneer.
```

The divergence lies in water retention as each planet cooled.
On Earth, water condensed after the magma ocean and persisted as an ocean for $4$ Gyr, whereas on Venus water either never condensed or was lost during a runaway greenhouse.
The D/H ratio records water loss.
Noble gas isotopes will date when it occurred.

The third input is the rotation rate.
Venus rotates retrograde with a $243$-day period, much slower than Earth's $24$-hour rotation, and the weak Coriolis force drives zonal super-rotation instead of mid-latitude cells, altering cloud albedo.
Slow rotation may also weaken the organisation of core convection, which may help explain why Venus lacks an intrinsic magnetic field.

A **redox pump**, a mechanism linking volatile loss to planetary oxidation, connects atmospheric evolution to early water loss ({numref}`fig:wordsworth-n2pump`).
Retaining surface water left Earth with a moderately oxidising mantle and a $1$-bar $\mathrm{N_2}$ atmosphere.
On Venus, hydrogen escape oxidised the interior, generating a hot $\mathrm{CO_2}$-dominated atmosphere with depleted $\mathrm{N_2}$ {cite:p}`WordsworthN2016`.

```{figure} figures/wordsworth2016_n2_redox_pump.avif
:name: fig:wordsworth-n2pump
:width: 100%
:align: center

Schematic of the **water-loss redox pump** linking the differing atmospheric $\mathrm{N_2}$ inventories of Earth and Venus to their early water-loss histories, from {cite:t}`WordsworthN2016`.
Both planets begin in **state A** with a reducing steam atmosphere over a magma ocean.
Earth evolves directly to **state C**, a $1$-bar $\mathrm{N_2}$ atmosphere over a moderately oxidising mantle ($f_{\mathrm{O_2}} \approx$ FMQ) with surface liquid water and a substantial pool of nitrogen sequestered in the interior.
Venus, on the other hand, passes through **state B**, in which intense hydrogen escape oxidises the upper mantle, before reaching **state D**, a hot $\mathrm{CO_2}$- and $\mathrm{N_2}$-rich atmosphere over a highly oxidised interior ($f_{\mathrm{O_2}} \approx$ MH).
The diagram emphasises that the present atmospheric composition contrast between Earth and Venus is a downstream consequence of the water history operating through the planetary redox budget.
The four-panel layout is retained because the redox sequence A$\to$C (Earth) versus A$\to$B$\to$D (Venus) is the central pedagogical content of the figure.
Reproduced from {cite:t}`WordsworthN2016`.
```

The fourth input is the tectonic regime.
Earth operates in mobile-lid plate tectonics, whereas Venus is in a stagnant-lid regime.
Tectonic mode depends on water inventory.
This is because water weakens mantle olivine and enables subduction.
Desiccation may have stiffened Venus' lithosphere and shut down plate tectonics and the climate-buffering cycles ({numref}`fig:earth-venus-systems`).

```{figure} figures/gillmann2022_earth_venus_systems.avif
:name: fig:earth-venus-systems
:width: 100%
:align: center

System diagram comparing the climate and interior couplings of Earth (left) and Venus (right), from {cite:t}`Gillmann2022`.
Earth's system is closed by the active feedback loop between mantle convection, plate tectonics, surface volcanism, the atmosphere, the hydrosphere, the biosphere, and the magnetic dynamo.
Venus' system is open: subduction is absent, the hydrosphere is essentially zero, the biosphere is empty, and the magnetic dynamo is shut down.
The cycles that buffer Earth's climate cannot operate on present Venus.
Reproduced from {cite:t}`Gillmann2022`.
```

### The carbonate-silicate cycle failure mode on Venus

The **carbonate-silicate cycle** is the negative feedback that has stabilised Earth's climate over $4$ Gyr ({ref}`Lecture 6 <lecture06>`).
The cycle requires three essential components: a $\mathrm{CO_2}$ source (volcanism), a sink (silicate weathering and carbonate burial), and a return leg (subduction).
Earth has all three, whereas Venus retains only the source.

When Venus lost its surface liquid water, the silicate weathering sink stopped operating.
The reason is that dissolving silicate minerals to precipitate carbonates requires water.
Volcanism continued releasing $\mathrm{CO_2}$ from the interior, and with the source active and the sink shut down, atmospheric $\mathrm{CO_2}$ accumulated to the present level of $\sim 92$ bar.
In the absence of subduction, Venus also lacks a return leg to recycle crustal carbon back into the mantle.

Earth and Venus acquired similar amounts of carbon during accretion, but the carbon is distributed differently.
Earth's crustal and surface carbon reservoir totals on the order of $10^{20}$ kg, equivalent to $\sim 100$ bar of atmospheric $\mathrm{CO_2}$ {cite:p}`Catling2017`.
Venus holds a comparable inventory of $92$ bar entirely in its atmosphere.
On Earth, almost all carbon is stored in crustal carbonates and the mantle, leaving only a few hundred ppm in the atmosphere.
On Venus, cycle failure has left nearly all carbon in the atmosphere.

This cycle failure is irreversible.
There is no thermodynamic path back to an Earth-like state because Venus lacks surface oceans, plate tectonics, and geochemical recycling.
Once runaway greenhouse conditions push a planet past the inner edge of the habitable zone, it cannot recover.
The carbonate-silicate thermostat operates only within bounded conditions, outside of which it breaks irreversibly.

### What this means for habitability

The **habitable zone** is classically defined as the range of orbital distances where an Earth-like planet can support liquid surface water.
However, stellar luminosity increases over time.
This shifts the inner edge outward.
A planet that enters a runaway greenhouse and loses its water cannot become habitable again later simply because stellar conditions evolve.
Habitability is therefore determined by the integrated history of solar flux, water inventory, and feedback systems rather than instantaneous orbital location ({numref}`fig:trappist1`).

```{figure} figures/nasa_trappist1_solarsystem_comparison.avif
:name: fig:trappist1
:width: 100%
:align: center

Comparison of the seven TRAPPIST-1 planets (b through h) with the inner Solar System (Mercury, Venus, Earth, Mars), in the plane of planetary density (vertical) versus stellar illumination (horizontal, in units of Earth's illumination).
The blue band marks the classical habitable zones for the two systems.
Three of the TRAPPIST-1 planets (e, f, g) lie within the habitable zone, and TRAPPIST-1 c receives an illumination similar to Venus.
Whether any of these planets actually retain surface water depends on their history (formation, atmospheric evolution, escape) and not just on their current orbital location.
Image credit: NASA/JPL-Caltech.
```

Earth and Venus exemplify this principle.
Earth remains habitable inside the inner edge because the carbonate-silicate thermostat has regulated its climate.
Venus sits outside the inner edge today, and either was always outside it or crossed it at some point in the past.
The contrast between Earth at $1$ AU and Venus at $0.7$ AU is the result of a sensitive balance between radiative input, water inventory, tectonic regime, and biospheric feedback.
Applying these lessons to exoplanets requires climate-evolution models that follow a planet through its full history, which is the focus of {ref}`Lecture 13 <lecture13>`.

### Recent advances and upcoming missions

The 2030s will see three new orbital missions and one in-situ descent probe to Venus.
NASA's DAVINCI is scheduled to launch in $2029$--$2030$ and will send an instrumented probe into the atmosphere to measure noble gas isotopic abundances and atmospheric chemistry.
These noble gas measurements record atmospheric escape over time.
They distinguish between early-loss and late-loss scenarios for Venus' water history.
NASA's VERITAS, launching no earlier than $2031$, will obtain global radar topography and near-infrared surface emissivity to determine tessera composition and constrain mantle convection through the tidal Love numbers and moment of inertia.
ESA's EnVision is expected to launch in $2031$, combining synthetic-aperture radar, atmospheric spectroscopy, and a subsurface sounder to search for active volcanism, characterise tessera regions, and map the gravity field.

In parallel, 3D climate models and coupled magma-ocean interior models are clarifying how Earth and Venus diverged early in their history {cite:p}`Turbet2021,Gillmann2022`.
Another active area of research is the search for biosignatures in the Venus cloud layer at $50$-$60$ km altitude, where temperature and pressure conditions match surface Earth conditions.
Although the $2020$ detection of phosphine ({ref}`Lecture 6 <lecture06>`) remains contested, the possibility of an aerial biosphere first proposed in $1967$ will be tested by upcoming missions.

## Summary and takeaways

Earth and Venus are the closest analogue we have to a controlled experiment in comparative planetology.
They started from the same protoplanetary reservoir, accreted to similar masses and densities, and probably acquired comparable inventories of water and carbon.
Today they could not look more different.
Earth is wet, geologically active, magnetically shielded, and inhabited.
Venus is dry, encased in $92$ bar of $\mathrm{CO_2}$, surface temperature $737$ K, with no global magnetic field and no plate tectonics.
The divergence is due to a small set of physical inputs (solar flux, water history, rotation rate, and tectonic regime) coupled by nonlinear feedbacks that turned modest differences in input into qualitatively different end states.

The central piece of physics is the **Simpson-Nakajima runaway greenhouse limit**.
It is the maximum thermal flux that a water-saturated atmosphere can radiate to space, set by the saturation vapour pressure curve at the temperature of the IR photosphere.
This limit, in the range $280\text{--}310$ W/m$^2$, defines the inner edge of the habitable zone and is essentially independent of the surface temperature once the atmosphere becomes optically thick in the IR.
A planet whose absorbed solar flux exceeds the limit cannot host a steady state with liquid surface water; the runaway greenhouse drives the ocean into the upper atmosphere, photolyses the water, and loses the hydrogen to space.
The process is one-way.
There is no thermodynamic path back to the wet state.
Earth, at $1$ AU, sits below the limit.
Venus, at $0.723$ AU, sits well above it.

The **carbonate-silicate cycle** is the negative feedback that has stabilised Earth's climate within the liquid-water window for $4$ Gyr, but it cannot operate on present Venus because the cycle requires both liquid surface water (for the weathering sink) and active plate tectonics (for the subduction return leg).
Once Venus lost its water, the sink was destroyed.
Once the subduction stopped, the return leg was destroyed.
Volcanic outgassing of $\mathrm{CO_2}$ continued, and atmospheric $\mathrm{CO_2}$ accumulated to its present $92$ bar value over hundreds of millions of years.
The total carbon inventory of Earth (mostly stored as carbonate rocks) is comparable in magnitude to the atmospheric carbon inventory of Venus, suggesting that the two planets have similar carbon inventories and the difference is where the carbon ended up.

The **D/H ratio** of Venus, enriched by a factor of $\sim$150 over the terrestrial value, is the clearest evidence for water loss.
It implies that Venus has lost at least $100\times$ more water than its present inventory, regardless of the loss mechanism or timing.
The remaining open question is whether the loss happened early (during a perpetual magma ocean phase, the Hamano scenario) or late (after a few-Gyr period of habitability, the Way scenario), and the answer matters for whether early Venus was ever habitable.
This question will be addressed in the next decade by the new wave of Venus missions (DAVINCI, VERITAS, EnVision), particularly the noble-gas isotopic measurements that DAVINCI will return from its descent probe.

For exoplanets, the lesson is that **the habitable zone is not a region in space but a region in history**.
A planet's habitability today depends on the entire integrated history of its solar flux, water inventory, tectonic regime, and feedback systems, not on a single snapshot of where it sits relative to a static habitable zone boundary.
Earth sits comfortably inside the habitable zone today, and Venus sits comfortably outside.
Yet a few percent change in solar flux, or a slightly different impact and accretion history, could have placed either of them in the other's role.
What we learn from Venus directly informs our framework for assessing exoplanet habitability and, indirectly, our understanding of the long-term stability of Earth's own climate system, including the question of how robust the carbonate-silicate thermostat is to anthropogenic forcing on human timescales.

**Key physics takeaway**: The Simpson-Nakajima limit is a thermodynamic boundary in phase space, not a model artefact.
It defines the irreversible threshold beyond which the runaway greenhouse drives a wet planet to a dry, hot end state, and Venus is the textbook example.

**Key comparative takeaway**: Earth's long-term habitability rests on a coupled set of feedbacks (carbonate-silicate cycle, plate tectonics, biosphere, dynamo) that all require liquid water and active volcanism to operate.
Loss of any one of these feedbacks risks losing the others; Earth has been lucky, and Venus shows what happens when you are not.

## References

```{bibliography}
:filter: docname in docnames
```
