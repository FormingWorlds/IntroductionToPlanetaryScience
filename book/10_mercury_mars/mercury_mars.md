(lecture10)=
# Lecture 10: Rocky Planets, Mercury & Mars

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to explain Mercury's unusual spin-orbit resonance and metal-rich interior, reconstruct the geological history of Mars across its three main epochs, derive and apply the Jeans escape flux formula, interpret the seismic structure of Mars from {ref}`InSight <lecture08>` data, and use Mercury and Mars as limiting cases that isolate the roles of planet size, distance, and timing in rocky-planet evolution.
```

## Why Mercury and Mars together?

In {ref}`lecture09` we treated Earth and Venus as a near-twin pair: very similar in mass and bulk composition, yet wildly divergent in surface conditions. This lecture takes the opposite approach. Mercury and Mars are nature's *limiting cases* for rocky planets in our solar system. Mercury is the smallest and the densest, sitting closest to the Sun and stripped of almost all volatiles. Mars is roughly half the diameter of Earth, sits at the outer edge of the classical habitable zone, and preserves a sedimentary and atmospheric record that points to a wetter, warmer past. Together they bracket Earth and Venus on every axis that matters for terrestrial-planet evolution: size, heliocentric distance, volatile inventory, and dynamo longevity.

The structure of the lecture follows that ambition. Part 1 takes Mercury as a metal-world case study, threading the needle from orbital dynamics through interior structure, surface morphology, polar volatiles, exosphere, and exploration history. Part 2 turns to Mars and walks through its interior, geological epochs, surface highlights, evidence for past water, the early-climate puzzle, modern atmospheric loss, and exploration. The blackboard derivation, on the Jeans escape flux, sits naturally in the Mars half because thermal escape is the textbook entry point for understanding Mars' atmospheric history. Part 3 then steps back and uses the comparison between the two extremes (and their contrast with Earth and Venus) to extract the general lessons that the rest of the course will need: size and distance set the trajectory; timing and dynamo longevity modulate the outcome; and habitability is a multidimensional question with at least four largely independent ingredients.

A note on the data underlying this lecture: of all the rocky bodies in the solar system, Mercury and Mars have changed the most dramatically in our understanding over the last fifteen years. NASA's *MESSENGER* mission revolutionised Mercury science between 2011 and 2015; ESA/JAXA's *BepiColombo* is now en route for orbit insertion in 2026. NASA's *InSight* lander placed a seismometer on Mars in 2018 and produced the first reliable internal-structure constraints for the planet by 2021. *Curiosity* and *Perseverance* are still operating on the surface as of this writing. Where I quote numbers, they reflect the post-*MESSENGER*, post-*InSight* state of the art; where the numbers remain contested, I say so explicitly.


## Part 1: Mercury, the metal world

### Mercury overview: the smallest, densest, closest

Mercury is a small planet on a hot, eccentric orbit. Its mass is $0.0553\,\Mearth$, its mean radius is $0.3829\,\Rearth = 2440\ \mathrm{km}$, and its bulk density is $5.43\ \mathrm{g\ cm^{-3}}$. That density is the second-highest in the solar system after Earth's, but Earth's high density is largely a consequence of self-compression. Once you correct for the smaller pressures inside Mercury, its **uncompressed density** ($\sim 5.3\ \mathrm{g\ cm^{-3}}$) is actually the highest of any solar-system body, and significantly higher than Earth's uncompressed value of $\sim 4.0\ \mathrm{g\ cm^{-3}}$ {cite:p}`Solomon2018`. This single number is the strongest constraint we have on Mercury's bulk composition: the planet must contain a great deal more iron, by mass fraction, than any of the other terrestrial planets.

Mercury's orbit is also extreme. The semi-major axis is $a = 0.387\ \mathrm{AU}$, but the eccentricity is $e = 0.2056$, the highest of any planet (Pluto excluded). At perihelion the distance to the Sun drops to $0.307\ \mathrm{AU}$; at aphelion it rises to $0.467\ \mathrm{AU}$. The instantaneous solar flux varies by more than a factor of two over a Mercurian year, and the obliquity is essentially zero (about $2$ arcminutes), so the rotation axis stays perpendicular to the orbital plane to within measurement error. Both numbers will matter later: the eccentricity drove the planet into its peculiar spin-orbit resonance, and the near-zero obliquity is what allows polar ice to survive on a planet so close to the Sun.

These two facts (the highest uncompressed density and the most eccentric orbit) frame everything we discuss about Mercury. The first immediately raises the question of how the planet ended up with so much iron, the so-called **iron-enrichment problem**, to which we return when we discuss giant-impact and evaporation hypotheses. The second, combined with tidal evolution, explains the spin-orbit resonance that defines a Mercurian "day."


### Orbit and the 3:2 spin-orbit resonance

Mercury rotates once every $58.65$ Earth days and orbits the Sun once every $87.97$ Earth days. The ratio is exactly $3:2$, which is highly suspicious from a dynamical point of view. Before *Mariner 10* reached Mercury in 1974 and 1975, most planetary scientists assumed that tidal dissipation would have driven a small planet so close to the Sun into the simpler $1:1$ resonance, with one face permanently turned toward the Sun, just as Earth's Moon shows one face permanently to Earth. The radar discovery in 1965 that Mercury rotates three times for every two orbits, rather than one for one, was at first a surprise.

The explanation was worked out by Peale and others in the 1960s and 1970s and brought to its modern form by {cite:t}`CorreiaLaskar2004`. Tidal torques try to drag the planet's spin into synchronisation with its orbital motion, but the eccentricity matters. At perihelion the planet moves much faster along its orbit than near aphelion, and the tidal torque acting on a slightly elongated body is strongest there. For a planet with a permanent quadrupole moment (a small "bulge" along its long axis) and an eccentricity comparable to Mercury's, the lowest-energy stable state is not $1:1$ but $3:2$: the planet rotates such that, every other perihelion passage, the same bulge points toward the Sun. {cite:t}`CorreiaLaskar2004` showed that capture into the $3:2$ state is the most likely outcome of Mercury's chaotic orbital evolution under perturbations from the other planets, with a probability of order $50\%$, against $\sim 25\%$ for $2:1$ and only a few percent for $1:1$.

A consequence is that a *solar day* on Mercury, the time from one local noon to the next, lasts $\sim 176$ Earth days, twice as long as the orbital year. Two specific longitudes ($0^\circ$ and $180^\circ$) are at perihelion at noon on alternate Mercurian years; these are the **hot poles**, where peak surface temperatures reach $\sim 700$ K. Two longitudes offset by $90^\circ$ are at perihelion at midnight; these "warm poles" reach a peak of only $\sim 570$ K. The thermal contrast between hot and warm poles, established by these geometric facts, leaves a signature in surface temperature, exospheric sodium emission, and (we suspect) the distribution of subsurface volatiles.

```{figure} figures/margot2007_libration.avif
:name: fig:margot-libration
:width: 600px
:align: center

Radar speckle correlation functions from {cite:t}`Margot2007` demonstrating the longitudinal libration of Mercury at the $88$-day orbital period. The amplitude of this libration ($35.8 \pm 2$ arcseconds) is twice as large as predicted for a fully solid Mercury, demonstrating that the mantle is decoupled from a partially molten core.
```

```{figure} figures/margot2007_libdata.avif
:name: fig:margot-libdata
:width: 600px
:align: center

Histograms of best-fit values for the diagnostic moment-of-inertia ratio $C_m/C$ (the fraction of the total moment carried by the silicate mantle alone), drawn from Monte Carlo realisations of {cite:t}`Margot2007`'s data with two different sets of constraints. The distributions are inconsistent with a fully solid Mercury and require a decoupled, at least partly liquid core.
```

A second consequence is that the rotation rate itself is a sensitive probe of Mercury's interior. {cite:t}`Margot2007` used Earth-based radar to track surface speckle features across multiple Mercurian rotations and measured the **forced libration in longitude**, the small back-and-forth wobble of the planet over its $88$-day year. The amplitude of that wobble depends on whether the entire planet (mantle plus core) responds rigidly to the time-varying solar torque, or whether a fluid core decouples from a thinner librating mantle. The measured value of $35.8 \pm 2$ arcseconds is roughly twice what a fully solid Mercury would show. This was the first direct observational evidence that Mercury's outer core is liquid today, in contradiction to the picture (held since *Mariner 10*) that such a small body would have cooled and frozen completely.


### Interior: a giant iron core

The combination of *Mariner 10* gravity coefficients, the *MESSENGER* radio science campaign, and the libration measurements of {cite:t}`Margot2007` allowed planetary scientists to invert for the moment of inertia of Mercury and the moment of inertia of just the silicate mantle. The result is a normalised moment of inertia $C/MR^2 \approx 0.346$, considerably below the value of $0.4$ for a uniform sphere. As we showed in {ref}`lecture08`, $C/MR^2 < 0.4$ implies that mass is concentrated toward the centre, and the smaller the value the more strongly differentiated the body. Mercury's $0.346$ is comparable to Earth's $0.331$ but, given Mercury's much higher core mass fraction, implies a much thinner silicate shell wrapped around an unusually large metallic core.

Putting numbers on it: the core radius is approximately $2020\ \mathrm{km}$, or about $83\%$ of the planet's radius. The mantle plus crust is therefore only about $420\ \mathrm{km}$ thick, or $17\%$ of the radius. By mass, the core represents roughly $70\%$ of Mercury, against only $32\%$ for Earth. Mercury is essentially a metal ball with a thin silicate shell. There is no other planet in the solar system that looks like this {cite:p}`Solomon2018`.

```{figure} figures/margot2018_mercury_layers.avif
:name: fig:margot2018-layers
:width: 380px
:align: center

Schematic representation of Mercury's internal layering used in modern interior structure models from {cite:t}`MargotHauck2018`. From the centre outward, $R_{\mathrm{ic}}$ is the inner solid core boundary, $R_{\mathrm{oc}}$ separates the liquid outer core from the solid outer shell, $R_{\mathrm{b}}$ marks the optional dense compositional layer at the base of the silicate mantle, and $R_{\mathrm{m}}$ is the crust-mantle boundary. The radially varying densities of the inner and outer core ($\rho_{\mathrm{ic}}(r)$ and $\rho_{\mathrm{oc}}(r)$) capture compression and composition effects with depth.
```

Within the core, *MESSENGER* gravity and libration data are consistent with a layered structure: a **liquid outer core** (the part that decouples to give the libration signal), surrounding a small **solid inner core** whose existence and size remain debated. *MESSENGER* magnetometer measurements show that Mercury has a present-day intrinsic magnetic field, weak (about $1\%$ of Earth's surface field strength) but unmistakably global, dipolar, and aligned with the rotation axis. A weak active dynamo therefore operates in Mercury today. We will return to its peculiar geometry in a moment. For now, the main lesson is that the dynamo requires convection in the liquid outer core, which in turn requires that the core has not finished freezing despite Mercury's small size and $\sim 4.5$ Gyr of cooling. The geophysical implication, supported by detailed thermal-evolution models {cite:p}`Solomon2018,Wicht2017`, is that Mercury's core contains a significant fraction of light elements (most likely sulfur, possibly silicon or carbon) that lower the freezing point and slow the growth of a solid inner core.


### Why is Mercury so iron-rich?

The single most striking fact about Mercury is its iron enrichment. Earth, Venus, and Mars have core mass fractions of $32\%$, $32\%$, and $24\%$ respectively. Mercury sits at $\sim 70\%$. Three families of explanations have been proposed:

1. **Selective condensation in the inner solar nebula.** In the early condensation models of the 1970s and 1980s, an inner disc midplane that was hot enough to inhibit silicate condensation but cool enough to condense Fe-Ni metal could naturally produce iron-enriched solids close to the Sun. Modern dynamical and chemical models do not, however, support a steep enough condensation gradient at $0.4$ AU, and this hypothesis is no longer favoured.

2. **Vapour and aerosol stripping by the early Sun.** A very luminous young Sun, or strong stellar winds, could in principle have evaporated and blown away part of an originally silicate-rich proto-Mercury. The geochemical predictions of this scenario (heavy elements such as potassium should be depleted relative to volatiles like sodium) are partly in tension with *MESSENGER* surface composition measurements, which actually find Mercury enriched in moderately volatile elements such as Na, S, and K {cite:p}`Solomon2018`. This makes thermally driven mantle stripping increasingly hard to defend.

```{figure} figures/nittler2020_mercury_chemistry.avif
:name: fig:nittler-chemistry
:width: 480px
:align: center

**(a)** Global maps of Mg/Si (left) and Al/Si (right) elemental ratios on Mercury's surface, derived from four years of *MESSENGER* X-Ray Spectrometer measurements by {cite:t}`Nittler2020`. White contours mark the High-Mg Region (HMR), the Caloris Basin (CB), the Northern Smooth Plains, and the Low-Mg Northern Smooth Plains (LM-NSP). **(b)** A higher-resolution Mg/Si zoom around the Gaudi and Stieglitz craters within the Caloris province, showing that compositional variations exist on small spatial scales as well. Mercury's surface is volatile-element rich and does not match the expectations of a planet that lost its silicate mantle by thermally driven evaporation, undermining the strongest version of the vaporisation-stripping hypothesis for Mercury's iron enrichment.
```

3. **One or more giant impacts.** A high-energy collision late in accretion could have stripped most of an originally Earth-like silicate mantle from a proto-Mercury, leaving a body dominated by its metallic core. This idea has been around since the 1980s and remains the leading hypothesis. {cite:t}`Chau2018` and others have run smoothed-particle hydrodynamics simulations to test specific scenarios, finding that a single hit-and-run encounter with a much larger projectile, or a sequence of moderate impacts, can in principle produce the right core mass fraction. {cite:t}`Franco2022` recently emphasised, however, that such configurations are dynamically rare in N-body integrations of the inner solar system: explaining Mercury via a single giant impact happens in well below $1\%$ of plausible histories. Multiple smaller impacts may be statistically more likely.

```{figure} figures/franco2022_mercury_outcomes.avif
:name: fig:franco-mercury
:width: 700px
:align: center

Final mass distribution of remnant bodies at the end of N-body integrations of inner-solar-system formation, plotted against semi-major axis, for six different surface density profile slopes ($x = 0.5$ to $5.5$). Open circles are larger ($> 0.3\,\Mearth$) bodies, crosses are smaller ones, and solid triangles mark the masses of the actual terrestrial planets in our solar system. Reproducing a Mercury-mass body in the right orbital location with the observed iron enrichment occurs in well below $1\%$ of all trial histories. From {cite:t}`Franco2022`.
```

The honest summary is that we know Mercury is iron-rich, we have several plausible mechanisms, and we cannot yet decide between them. *BepiColombo*'s detailed compositional measurements should sharpen the constraints by revealing whether the volatile-element abundances at the surface match a single-impact scenario (which tends to lose more volatiles), a multiple-impact scenario, or something else entirely.


### A weak, offset dynamo

Mercury's magnetic field is unique among solar system bodies in two ways. First, it is dipole-dominated, axisymmetric, and aligned with the rotation axis to within $\sim 1^\circ$, but the dipole is *offset* from the geometric centre by $479 \pm 6\ \mathrm{km}$ northward {cite:p}`Anderson2012`. That is roughly $20\%$ of the planetary radius, an asymmetry far larger than seen for any other planet. Second, the field is much weaker than the dynamo scaling laws of {ref}`lecture04` would naively predict: the surface dipole strength is only $\sim 200\ \mathrm{nT}$ at the magnetic equator, about $1\%$ of Earth's value.

```{figure} figures/wicht_offset_dipole.avif
:name: fig:wicht-offset
:width: 380px
:align: center

Maps of the radial magnetic field at the surface of Mercury (top) compared with two of {cite:t}`Wicht2017`'s numerical dynamo models (CW3, middle, and CW4, bottom) that incorporate a thermally stratified outer core layer. The hemispheric asymmetry of the radial field, with red equatorial flux concentrated in the northern hemisphere, is the surface signature of the offset dipole. Models with a stably stratified upper core can reproduce both the weakness and the asymmetry of the observed field.
```

Both features are difficult to explain with the standard convection-driven, $\alpha$-$\Omega$ dynamo picture used to model Earth's field. Two mechanisms are usually invoked. The first is a **thermally stratified outer layer** at the top of Mercury's liquid core, in which heat is carried by conduction rather than convection. Such a layer can act as a low-pass filter on the dynamo, suppressing high-degree harmonics and damping rapid time variations. The second is a **stable, conductive inner core boundary** that introduces a north-south asymmetry into the convecting region, perhaps because of latitude-dependent freezing of the solid inner core under Mercury's distinctive thermal regime. Numerical dynamo simulations that combine these ingredients can reproduce both the weakness and the offset of Mercury's field, but the parameter space is large and several competing models exist {cite:p}`Wicht2017`.

The astrophysical relevance is twofold. First, Mercury demonstrates that even a small body with a partially molten core can sustain a dynamo for billions of years, which has implications for the rocky-exoplanet population in {ref}`lecture13`. Second, the offset dipole is a cautionary tale: the simple "axial dipole at the centre" picture is a very specific limit, and we should not assume that other rocky planets, including unseen ones around other stars, must look the same way.


### The surface: ancient cratering, smooth plains, lobate scarps, and hollows

Mercury's surface, as seen first by *Mariner 10* in 1974 and 1975 and then in global high resolution by *MESSENGER* between 2011 and 2015, looks at first glance very much like the lunar highlands. It is heavily cratered, dominated by ancient terrain, and shows a thick blanket of impact ejecta and regolith. On closer inspection, however, several features are distinctly Mercurian and tell a coherent story about the planet's geological history.

```{figure} figures/messenger_mla_global.avif
:name: fig:mla-global
:width: 700px
:align: center

Global topographic measurement coverage of Mercury from the *MESSENGER* Mercury Laser Altimeter (MLA) projected on a Hammer equal-area map. The northern hemisphere is densely covered by direct laser altimetry; topographic relief on Mercury spans roughly $10\ \mathrm{km}$ from the lowest to highest points measured. Image courtesy NASA/JHUAPL/Carnegie Institution; reproduced from {cite:t}`ZuberMLA2012`.
```

The **smooth plains** are large, lightly cratered, intercrater regions (the largest covering parts of the northern hemisphere) which superficially resemble the lunar maria. *MESSENGER* imaging and spectroscopy showed that they are volcanic in origin: vast flood-basalt provinces emplaced between $\sim 3.7$ and $\sim 3.9$ billion years ago, near the end of the late heavy bombardment. Stratigraphic relations and crater counting place most of the smooth plains in this narrow time window. After about $3.5$ Ga, large-scale effusive volcanism on Mercury appears to have stopped {cite:p}`Solomon2018`.

The **lobate scarps** are perhaps the most striking single class of feature. They are long, sinuous cliffs, hundreds of kilometres long and one to three kilometres high, with a curved ("lobate") map-view planform and an asymmetric cross-section that betrays a thrust fault dipping shallowly into the subsurface. They are everywhere on Mercury, on every terrain type, and they cut across craters of all ages, indicating that they are tectonic features rather than impact-related. The interpretation is straightforward: as Mercury's interior cooled, the planet contracted, and the brittle outer shell accommodated the contraction by thrust faulting. {cite:t}`ByrneTectonics2014` used the global *MESSENGER* image catalogue to map the full population of lobate scarps and infer a total radial contraction of $5$ to $7\ \mathrm{km}$. This is much larger than estimates from *Mariner 10* data alone. {cite:t}`Watters2016` then identified a sub-population of small (tens of metres relief), unweathered scarps that crosscut very young craters, suggesting that contraction is *still ongoing today*. Mercury, far from being a frozen, geologically dead world, is the only planet besides Earth currently known to host active tectonic deformation.

The **Caloris basin**, $\sim 1550\ \mathrm{km}$ in diameter, is one of the largest impact basins in the solar system. Its interior is partly filled by smooth plains and shows complex tectonic structures including ridges and graben. The seismic energy from the Caloris-forming impact appears to have been refocused on the antipodal point of Mercury, where *Mariner 10* discovered a region of jumbled, broken-up "weird terrain" that has no analogue elsewhere on the planet. This is a textbook example of antipodal focusing of impact-generated seismic waves, an effect also seen at the antipodes of the Imbrium basin on the Moon and South Pole-Aitken on the Moon's far side.

Finally, the **hollows** are uniquely Mercurian. *MESSENGER* discovered these small (tens of metres to a few kilometres across), shallow, flat-floored, irregularly-shaped bright depressions clustered on crater walls, peaks, and floors {cite:p}`Blewett2011`. They are unlike anything seen elsewhere in the inner solar system. The leading interpretation is that they form by loss of a volatile component (sulphides, perhaps) from the upper crust, with the host material destabilised by some combination of solar heating, micrometeorite gardening, and ion sputtering. Their fresh appearance and relationship to bright crater material suggests they are forming actively today, though the exact volatile species and the ultimate sink for the lost material remain open questions.

The combination of these features tells a coherent story: Mercury accreted, differentiated, and cratered very early; it underwent widespread effusive volcanism that ended around $3.5$ Ga; it has been contracting and faulting ever since as the interior cooled; and its surface is still slowly modified today by both ongoing tectonics and the volatile-loss processes that produce hollows.


### Polar volatiles: ice on the hottest planet

One of the most counterintuitive results in modern planetary science is that Mercury, the planet closest to the Sun, hosts substantial deposits of water ice at its poles. The story began with Earth-based radar observations from the Arecibo and Goldstone telescopes in 1991, which revealed bright, polarisation-inverting radar echoes in the polar regions of Mercury. The radar signature was characteristic of cold, clean water ice: a clear telescopic detection of polar volatiles, but in the form of small radar-bright "deposits" inside otherwise unidentified craters.

What *MESSENGER* did, between 2011 and 2015, was confirm the radar interpretation directly. The Mercury Laser Altimeter (MLA) measured the topography of the polar regions, allowing thermal modelling of which crater floors are *permanently shadowed* (never see direct sunlight, given Mercury's nearly zero obliquity) {cite:p}`Paige2013`. The Neutron Spectrometer measured a deficit of fast neutrons over the same regions, the unmistakable signature of hydrogen-rich material in the upper $\sim 1\ \mathrm{m}$ of regolith {cite:p}`Lawrence2013`. Direct visible-wavelength imaging from *MESSENGER*'s wide-angle camera, taken with very long exposures to capture light scattered from crater walls, showed bright deposits at the floor of permanently shadowed craters that match the radar-bright extent at metre-scale resolution.

```{figure} figures/messenger_mla_polar.avif
:name: fig:mla-polar
:width: 500px
:align: center

Surface reflectance of Mercury at $1064\ \mathrm{nm}$ measured by the *MESSENGER* Mercury Laser Altimeter, projected to $72^\circ$N polar projection. The dark spots correspond to permanently shadowed crater floors. Combined with neutron-spectrometer data, these floors are interpreted as cold-trapped water ice deposits. From {cite:t}`ZuberMLA2012`.
```

The total mass of polar water on Mercury is estimated at $\sim 10^{16}$ to $10^{18}$ g, the equivalent of one to several billion tonnes spread across $\sim 5\times10^4\ \mathrm{km^2}$ of permanently shadowed terrain {cite:p}`Lawrence2013`. The cold-trap mechanism is straightforward: water molecules delivered by comet impacts, asteroids, or dehydration of Mercury's interior wander randomly around the planet via ballistic hops, and any molecule that lands in a permanently shadowed crater floor (with an equilibrium temperature of $\sim 100$ K) is effectively frozen out for billions of years. The persistence of the deposit requires both that Mercury's obliquity has stayed close to zero throughout its history, so that no crater floor has been temporarily illuminated, and that the total delivery rate of cometary and asteroidal volatiles has been sufficient to keep up with sputtering and photodesorption losses from the exposed deposits.

The paradox, worth pausing on, is that the planet most exposed to the Sun's radiation hosts some of the coldest stably-shadowed surfaces in the inner solar system. The very same near-zero obliquity that makes Mercury so dramatically heated near the equator (because there is no seasonal cycle to spread the heat out in latitude) is what allows ice to survive close to the poles.


### Exosphere and magnetosphere

Mercury has no real atmosphere. The collisional regime fails at the surface itself: the column density is so low that gas particles fly on independent ballistic trajectories, with negligible chance of bumping into one another before they hit the ground or escape. We call such an envelope a **surface-bounded exosphere**.

The exosphere contains identifiable amounts of atomic Na, K, Ca, Mg, H, He, and a few other species. Each is sourced and lost by a different combination of processes:

- **Solar wind sputtering** delivers energetic protons and alpha particles to the surface, knocking surface atoms loose. This is most efficient near the magnetic cusps where solar wind ions reach the surface most easily.
- **Micrometeorite impact vaporisation** continuously delivers volatiles to the exosphere from the regolith.
- **Photon-stimulated desorption** by ultraviolet sunlight liberates loosely-bound surface atoms.
- **Thermal desorption** is significant for the most volatile species (helium and hydrogen).

The most spectacular feature of the exosphere is the **sodium tail**, a comet-like extension of neutral sodium atoms swept antisunward by solar radiation pressure that can be seen with ground-based telescopes from Earth. The tail is variable in space and time: ground-based and *MESSENGER* monitoring show that it brightens substantially when Mercury is at certain orbital phases or when solar wind conditions energise sputtering. The Na exosphere therefore acts as a real-time tracer of space-weather coupling at Mercury.

The **magnetosphere** is small and dynamic. Because the field strength at the planet is weak and the solar wind dynamic pressure is large at $0.4$ AU, the magnetopause standoff distance is only $\sim 1.5\ R_M$, where $R_M = 2440\ \mathrm{km}$ is Mercury's radius. By comparison, Earth's magnetopause sits at $\sim 10\ R_E$. Mercury's tiny magnetosphere is so close to the planet that its dynamics are dominated by reconnection, not by the slow internal dynamics that govern Earth's. *MESSENGER* observed reconnection rates ten times higher (relative to the field strength) than at Earth, with full magnetic substorms playing out on timescales of just a few minutes. The combination of weak intrinsic field, conducting interior, and strong reconnection makes Mercury a unique plasma laboratory.

```{figure} figures/wicht_magnetosphere.avif
:name: fig:wicht-mag
:width: 450px
:align: center

Equatorial cross-section of Mercury's compact magnetosphere. The standoff distance is only about $1.5\,R_M$ and the magnetotail is correspondingly short. Reconnection at the dayside magnetopause and in the tail is fast and frequent compared to Earth. Reproduced from {cite:t}`Wicht2017`.
```


### Mission history at Mercury

The exploration history of Mercury is short but highly impactful. **Mariner 10** flew past Mercury three times in 1974 and 1975. Because the spacecraft's orbit was locked into a specific resonance with Mercury, the same hemisphere was illuminated at each encounter, and only $\sim 45\%$ of the surface was imaged. Mariner 10 nevertheless discovered Mercury's intrinsic magnetic field, mapped large-scale topography from limb profiles, and revealed the heavily cratered character of the surface.

The decisive transformation came with **MESSENGER** (MErcury Surface, Space ENvironment, GEochemistry, and Ranging), which launched in 2004, made three Mercury flybys between 2008 and 2009, and entered orbit in March 2011. Until its planned impact onto the surface in April 2015, *MESSENGER* mapped the entire planet at high resolution, measured global topography from the MLA, made elemental and mineralogical measurements with the gamma-ray, neutron, and X-ray spectrometers, mapped the magnetic field, and characterised the exosphere. Most of what we know about Mercury today comes from *MESSENGER*. The discoveries we have already discussed, the offset dipole, the polar ice, the hollows, the global contraction, the high volatile content, and the smooth plains, all came from this mission.

**BepiColombo**, a joint ESA/JAXA mission launched in 2018, is currently en route to Mercury. The cruise has involved gravity assists at Earth, Venus, and Mercury itself; six Mercury flybys between 2021 and 2024 returned new images and field measurements as the spacecraft slowed down for orbit insertion in late 2026 {cite:p}`Benkhoff2021`. Once in orbit, *BepiColombo* will release two separate spacecraft: the Mercury Planetary Orbiter (MPO, ESA-led) for surface and interior science, and the Mercury Magnetospheric Orbiter (Mio, JAXA-led) for magnetosphere and exosphere science. The combination of two simultaneously-operating orbiters is unique in solar-system exploration and will allow direct correlation of phenomena observed at different distances from the planet. Key targets for *BepiColombo* include the long-term variability of the magnetosphere, an improved measurement of the moment of inertia (which constrains the size of the inner core), better estimates of polar ice inventories, and a determination of whether the surface volatile abundances are consistent with the giant-impact origin scenario.


## Part 2: Mars, the watery past

### Mars overview: half Earth, one tenth the mass

Mars is the second-smallest planet, with a mass of $0.107\,\Mearth$ and a radius of $0.532\,\Rearth = 3389\ \mathrm{km}$. Its mean density is $3.93\ \mathrm{g\ cm^{-3}}$, the lowest of the four terrestrial planets. The orbit is well within the habitable zone of {ref}`lecture05`, with semi-major axis $a = 1.524\ \mathrm{AU}$ and eccentricity $e = 0.0934$. Crucially, the obliquity is currently $25.19^\circ$, almost identical to Earth's $23.4^\circ$, so Mars has Earth-like seasons. The atmosphere is thin ($\sim 6\ \mathrm{mbar}$ surface pressure) and dominated by $\mathrm{CO_2}$, with a global mean surface temperature near $210\ \mathrm{K}$.

Mars has two small natural satellites, Phobos and Deimos, which we will discuss as a separate topic below. We will also see that the Martian obliquity, although similar to Earth's today, has been chaotically variable on $\sim 100$ Myr timescales, oscillating between near-zero and over $60^\circ$ as a consequence of resonance with planetary perturbations. This is essential to keep in mind when interpreting evidence for past water at the poles or for periodic ice ages on Mars.

Compared to Mercury and Venus, Mars is at first glance more obviously Earth-like: a similar day length (24h 37min), similar obliquity, polar ice caps, dust storms, and a thin but meteorologically active atmosphere. Yet the surface is cold, dry, and uninhabitable today, and the most exciting Mars science of the last two decades has been the discovery that this was not always so. Reading the geological record, we now know that early Mars hosted abundant surface and near-surface liquid water for at least $\sim 100$ Myr, perhaps episodically for a billion years. Mars therefore offers the best preserved record we have of what an Earth-like planet looks like once it loses its atmosphere and dries out. That makes it both an irreplaceable target for astrobiology and a cautionary tale for assessments of habitability around other stars.


### Phobos and Deimos: the twin moons

Phobos is the larger and inner of Mars' two moons, with a mean radius of $11.27\ \mathrm{km}$ and an orbital period of only $7$ hours and $39$ minutes, considerably shorter than the Martian rotation period of $24$ hours and $37$ minutes. Because Phobos orbits faster than the planet rotates beneath it, the tidal bulge it raises on Mars lags behind, and the resulting torque pulls Phobos *inward* rather than outward. The orbital radius is decreasing by approximately $1.8\ \mathrm{cm/yr}$, and the moon will be tidally disrupted or impact the planet within $30$ to $50$ Myr.

Deimos is smaller (mean radius $6.2\ \mathrm{km}$), has a longer orbital period of about $30$ hours, and is slowly receding from Mars on a much longer timescale. Both bodies are irregular in shape, very dark (reflectance under $7\%$), and spectroscopically similar to D-type asteroids, the most primitive class of small bodies in the outer solar system. Their bulk densities are low, $\sim 1.86\ \mathrm{g\ cm^{-3}}$ for Phobos, implying high porosity (perhaps $25\%$ to $35\%$), consistent with a rubble-pile internal structure {cite:p}`Kuramoto2022`.

The origin of Phobos and Deimos has been debated for decades and remains genuinely unresolved. Two main hypotheses are on the table. The **captured asteroid** hypothesis is supported by the spectral resemblance to D-type and C-type primitive asteroids and by the low density. Its weakness is dynamical: capturing two objects into the very specific near-circular, near-equatorial orbits actually observed would require either very efficient gas drag (with dynamical implications for the early Martian atmosphere) or improbable sequences of three-body interactions. The **giant-impact debris** hypothesis postulates that a large collision early in Mars history threw silicate material into orbit, where it accreted into one or two larger moons that then evolved tidally outward and/or were broken up and re-accreted into Phobos and Deimos as we see them today. {cite:t}`Rosenblatt2016` showed that this scenario can produce both moons in their observed orbits. Its weakness is compositional: the simulated debris should be Mars-mantle-like in composition, not D-type-asteroid-like.

```{figure} figures/hyodo2017_phobos_impact.avif
:name: fig:hyodo-phobos
:width: 650px
:align: center

Smoothed-particle hydrodynamics snapshots of a Borealis-scale giant impact onto early Mars from {cite:t}`Hyodo2017`, at four times after the collision (columns: $t = 0.17$, $0.5$, $5$, and $20$ hours). The rows show particle composition (top), temperature in $\mathrm{K}$, entropy gain in $\mathrm{J\,K^{-1}\,kg^{-1}}$, and pressure in $\mathrm{GPa}$. The impact heats disc material to $\sim 2000\ \mathrm{K}$, drives an entropy increase of $\sim 1500\ \mathrm{J\,K^{-1}\,kg^{-1}}$, and ejects a circumplanetary disc that contains both impactor and Martian-mantle material. Disc fragments collide at $3$--$5\ \mathrm{km\,s^{-1}}$ and grind down to $\sim 100\ \mu$m grains, providing the building blocks from which Phobos and Deimos may subsequently accrete.
```

JAXA's **Martian Moons eXploration** (MMX) mission, scheduled for launch in $2026$ and return in $2031$, is designed to settle the origin question {cite:p}`Kuramoto2022`. MMX will land on Phobos, collect at least $10\ \mathrm{g}$ of regolith from at least two locations, and return that material to Earth for laboratory analysis. The isotopic and mineralogical composition of even a few grams of Phobos material will allow direct testing of the capture-versus-impact hypotheses with the same techniques used for Hayabusa2's Ryugu samples and OSIRIS-REx's Bennu samples. MMX will also fly multiple close passes by Deimos and remotely characterise its surface.

```{figure} figures/mmx_orbit.avif
:name: fig:mmx-orbit
:width: 480px
:align: center

Quasi-satellite orbits planned for the JAXA MMX spacecraft around Phobos. The QSO trajectories allow safe close-range observation of the moon, and lower-altitude QSOs (down to $\sim 20\ \mathrm{km}$) enable the sampling phase. From {cite:t}`Kuramoto2022`.
```

```{figure} figures/mmx_timeline.avif
:name: fig:mmx-timeline
:width: 700px
:align: center

Timeline of MMX operations at Mars, showing the cruise phase, the multiple Phobos-relative orbital phases, the Deimos flybys, the sampling and ascent operations, and the return cruise to Earth. From {cite:t}`Kuramoto2022`.
```


### Mars' interior: the InSight revolution

Until recently, our knowledge of Mars' interior structure rested almost entirely on remote sensing. Spacecraft tracking of *Mars Global Surveyor* (1997--2006) and later orbiters constrained the gravity field with high precision. Combined with topography from the Mars Orbiter Laser Altimeter (MOLA) {cite:p}`Smith2001`, this gave maps of crustal thickness inferred from isostatic compensation, and a rough estimate of the moment of inertia. The bulk Mars value $C/MR^2 \approx 0.3645$ was already known (from {ref}`lecture08`) to be more uniform than Earth's, indicating less central mass concentration and a smaller relative core. But the mass of the core, the radius of the core, the composition of the core, and the layering of the mantle were essentially unknown.

That changed when NASA's **InSight** lander, the first dedicated geophysical mission to another planet, set its seismometer on the Martian surface in late 2018. Over four years of operation, *InSight*'s SEIS instrument recorded over a thousand marsquakes, ranging from very small high-frequency events from local crustal sources to a handful of large, low-frequency events that interrogated the deep interior. The largest of these (a magnitude $\sim 4.7$ event in May 2022) probed the entire planet.

```{figure} figures/stahler2021_marsquakes.avif
:name: fig:stahler-quakes
:width: 600px
:align: center

Detection of core-reflected $S$ waves ($ScS$) in InSight marsquake recordings. Stacking the polarisation-filtered envelopes of multiple events on a common time axis reveals a clear secondary arrival that matches the predicted travel time of waves reflected off the core-mantle boundary. The right-hand panels show the energy and the corresponding inferred core radius. From {cite:t}`Stahler2021`.
```

By the summer of 2021, the InSight team had announced three landmark results, all published together in *Science* {cite:p}`Stahler2021,Khan2021,Knapmeyer-Endrun2021`. {cite:t}`Stahler2021` used $ScS$ phases (shear waves reflected off the core-mantle boundary) from several large quakes to measure the core radius directly: $1830 \pm 40\ \mathrm{km}$, considerably *larger* than most pre-InSight thermal-evolution models had predicted, and corresponding to about $54\%$ of the planet's radius. The fact that $ScS$ waves are detected means the outer core is liquid; if the entire core were solid, these waves would propagate freely across the boundary and the strong reflection signature would be absent. The measurement implies a mean core density of $5.7$ to $6.3\ \mathrm{g\ cm^{-3}}$, well below pure iron, requiring a significant complement of light elements (sulfur, oxygen, carbon, hydrogen) dissolved in the iron core.

```{figure} figures/stahler2021_mars_structure.avif
:name: fig:stahler-schematic
:width: 480px
:align: center

Schematic interior of Mars constrained by InSight seismic observations from {cite:t}`Stahler2021`. The core radius is $1830 \pm 40\ \mathrm{km}$, marking a low-density, light-element-rich liquid metallic core. $S$ waves reflect off the core-mantle boundary, while $P$ waves transmit through and have been used to bound mantle structure. The $S$-wave shadow zone defines the "core shadow" cast by InSight at its landing site in Elysium Planitia.
```

{cite:t}`Khan2021` used the same dataset to invert for the velocity structure of the upper mantle and identify a thick, slow lithosphere ($\sim 500$ km) underlain by a relatively cool upper mantle. {cite:t}`Knapmeyer-Endrun2021` analysed surface waves and high-frequency body waves to determine the thickness of the crust beneath the InSight landing site, finding either $20 \pm 5$ km (if the crust ends at the first major seismic discontinuity) or $39 \pm 8$ km (if it extends to a deeper one). When extrapolated to the planet as a whole using gravity-and-topography mapping, the global average crust thickness of Mars is between $24$ and $72$ km, thinner in the northern lowlands and thicker in the southern highlands.

These three measurements together produce the modern picture of Mars: a thin to moderately thick crust enriched in heat-producing elements; a partially molten silicate mantle with a relatively shallow base ($\sim 1560$ km depth); and a large, light-element-rich, fully or nearly fully liquid core. The conclusion that the core has not yet begun to crystallise an inner core is consistent with the *absence* of a present-day Martian magnetic field: no inner-core nucleation means no compositional buoyancy to drive a vigorous dynamo, even though the core is still liquid.

The youthful interior structure that InSight reveals is consistent with a separate, much older line of evidence: Mars formed and differentiated very fast. The hafnium-tungsten ($^{182}\mathrm{Hf}$-$^{182}\mathrm{W}$) chronometer applied to Martian meteorites and bulk silicate Mars indicates that Mars accreted and segregated its metallic core within only $\sim 2$--$4$ Myr of CAI formation {cite:p}`Kruijer2017Mars`. This is a remarkably short timescale, much shorter than the $\sim 30$--$100$ Myr accretion time of Earth, and it implies that **Mars is essentially a planetary embryo that never grew into a fully fledged terrestrial planet**. The small core fraction, the short dynamo lifetime, and the apparent lack of late giant impacts on Mars are all consistent with a body that finished its main accretion phase before the Solar System's terrestrial-planet region had even started to consolidate.

```{figure} figures/plesa2022_crustalthickness.avif
:name: fig:plesa-crust
:width: 700px
:align: center

Predicted maps of crustal thickness, basement topography, and surface heat flow for Mars from {cite:t}`Plesa2022`'s 3-D thermal-evolution models, anchored to the InSight crustal-thickness measurement at the landing site. The dichotomy between thin (blue) northern lowlands and thicker (red) southern highlands is a robust feature of all model variants.
```

```{figure} figures/plesa2022_convection.avif
:name: fig:plesa-convection
:width: 700px
:align: center

Three-dimensional snapshots and equatorial cross-sections of mantle temperature in {cite:t}`Plesa2022`'s thermal-evolution models, constrained by the InSight crustal-thickness and core-radius measurements. The depth slices below the surface, at mid-mantle depth, and just above the core-mantle boundary all show small-number long-wavelength upwellings, consistent with the persistence of the Tharsis volcanic province as the surface expression of a stable plume.
```

The geodynamic interpretation of these results, developed in detail by {cite:t}`Plesa2022`, is that Mars sits in a stagnant-lid regime: the lithosphere is thick and immobile, mantle convection is sluggish, and heat is escaping primarily by conduction through the lid, with secondary contributions from a long-lived plume beneath Tharsis. The crust is significantly enriched in radioactive heat-producing elements (uranium, thorium, potassium) compared to the bulk silicate Mars, which both heats the crust directly and depletes the mantle of long-term radiogenic energy. This combination of features explains why Mars cooled fast enough that the dynamo died early, but slow enough that some volcanism persisted into the recent past.


### Mars' geological epochs: Noachian, Hesperian, Amazonian

Mars has been carved into three major geological epochs based on crater densities, calibrated against the lunar cratering chronology of {cite:t}`Neukum2001` and refined for Mars by {cite:t}`Hartmann2001`. The most recent global compilation is the geologic map of {cite:t}`Tanaka2014`, which underlies most modern discussions of Mars' history.

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

The **Noachian** epoch ($\sim 4.1$ to $\sim 3.7$ Ga) is the oldest. It dates from the period of heavy bombardment, when impact craters of all sizes formed at high rates on the southern highlands. Noachian terrain is identified by its high crater density and is preserved primarily in the older, higher-elevation southern hemisphere of Mars. The Noachian was the period when most of the planet's water-related features formed: dendritic valley networks, open-basin lakes, and clay-mineral assemblages that point to chemical weathering by liquid water. The Noachian also coincides with the active phase of Mars' core dynamo (see below).

The **Hesperian** epoch ($\sim 3.7$ to $\sim 3.0$ Ga) is the intermediate period, characterised by widespread effusive volcanism that resurfaced large parts of the northern hemisphere with basaltic flood lavas, and by catastrophic outflow channels that incised the surface in spectacular bursts. The Hesperian also marks a major transition in surface chemistry from clay-forming (water-rock interaction at near-neutral pH) to sulfate-forming (more acidic, evaporative aqueous environments). The dynamo had probably shut off by the Hesperian, and the atmosphere was thinning rapidly.

The **Amazonian** epoch ($\sim 3.0$ Ga to present) covers two thirds of Mars' history but represents only a small fraction of its total geological activity. Amazonian-aged surfaces are characterised by very low crater densities, sporadic volcanism (concentrated in the Tharsis region, where eruptions continued well into the last $1$ Gyr), modest aeolian and periglacial activity, and a thin, dry atmosphere essentially indistinguishable from the modern one.

A simple but powerful idea emerges from the Tanaka maps: the rate at which Mars renewed its surface fell by more than an order of magnitude across these three periods. Most of Mars' interesting geology, and in particular all the evidence for liquid surface water, is concentrated in the Noachian. Mars was a different planet then.


### Mars surface highlights: dichotomy, Tharsis, Olympus, Valles

Mars' topography, mapped at uniform vertical resolution by MOLA between 1997 and 2001 {cite:p}`Smith2001`, shows two features at the largest scale that dominate the planet's geological identity. The first is the **hemispheric dichotomy**: a $\sim 6$-km elevation difference between the heavily cratered southern highlands (older, higher) and the smooth northern lowlands (younger, lower). The transition zone is sharply defined and runs roughly along a great circle inclined to the rotation axis. Two main classes of explanation have been proposed. **Endogenic mantle convection** patterns can in principle generate a degree-1 hemispheric asymmetry but struggle to make it as sharp and elliptical as the observed dichotomy boundary. **Exogenic giant impact** scenarios, championed by {cite:t}`AndrewsHanna2008`, propose a single very large oblique impact early in Mars history that created the entire northern lowlands as a vast impact basin, the **Borealis basin**, with semi-axes of $\sim 10\,600 \times 8\,500\ \mathrm{km}$. This basin would be the largest known impact structure in the solar system. The giant-impact origin is consistent with the elliptical shape of the boundary and with the thinner crust beneath the lowlands (now confirmed by the InSight crustal-thickness extrapolation), but no direct measurement (e.g. shock-metamorphosed material from the basin floor) has yet been made.

The second large-scale feature is **Tharsis**, a continent-sized volcanic province covering roughly a quarter of Mars' surface and standing several kilometres above the Martian datum. Tharsis hosts the largest volcanoes in the solar system, including:

- **Olympus Mons**, a shield volcano $\sim 21.9\ \mathrm{km}$ tall (above the surrounding plains, or about $26\ \mathrm{km}$ above the Mars datum) and roughly $600\ \mathrm{km}$ in diameter at its base;
- The three Tharsis Montes (**Arsia, Pavonis, Ascraeus**), each $\sim 14$--$18\ \mathrm{km}$ tall and aligned along the Tharsis crest;
- **Alba Mons**, a much lower-relief but enormous volcanic edifice covering several million $\mathrm{km^2}$.

These volcanoes are huge for two related reasons. First, in the absence of plate tectonics, a long-lived stationary mantle plume can keep delivering magma to the same surface location for hundreds of millions of years, building up an unbroken edifice instead of moving across the surface and producing a chain of separate volcanoes (as the Hawaiian-Emperor chain does on Earth). Second, Mars' lower gravity ($g = 3.71\ \mathrm{m\,s^{-2}}$, $\sim 38\%$ of Earth's) lets a magma body of a given volume support a higher topographic load before the underlying lithosphere flexes downward.

The Tharsis bulge is so massive that its formation imposed enormous stresses on the surrounding lithosphere. One result of those stresses, on the eastern flank of Tharsis, is **Valles Marineris**, a system of canyons stretching $\sim 4000\ \mathrm{km}$ along the equator, up to $200\ \mathrm{km}$ wide and $7\ \mathrm{km}$ deep. Valles Marineris is the largest canyon system in the solar system. Despite some superficial resemblances to terrestrial fluvial canyons such as the Grand Canyon, it is fundamentally a *tectonic rift*, opened by the lithospheric stresses from Tharsis. Water erosion (and possibly catastrophic flooding) modified some of its features later, but the original architecture is structural.

Other notable features include **Hellas Planitia**, a $2300$-km-diameter, $\sim 8$-km-deep impact basin in the southern hemisphere that is the largest unambiguous impact crater on Mars; the **polar caps**, which are layered ice deposits with seasonal $\mathrm{CO_2}$ ice on top of permanent water ice; and the **chaotic terrain** at the heads of several outflow channels, where collapsed and broken-up surface blocks mark the site of catastrophic volume loss.


### Evidence for past water

The transformative discovery of the last two decades is that liquid water once flowed across Mars' surface, accumulated in basins, weathered the rocks, and left a globally distributed record. The lines of evidence are diverse and reinforcing.

```{figure} figures/kite2022_valley_distribution.avif
:name: fig:kite-distribution
:width: 700px
:align: center

Distribution of fluvial features as a function of age from {cite:t}`KiteCarter2022`. **Top**: Late Noachian / Early Hesperian valley networks ($> 3.6$ Ga), concentrated in the southern highlands but globally distributed. **Bottom**: Late Hesperian / Amazonian alluvial fans and deltas ($3.5$ to $3$ Ga), concentrated in mid-latitudes. The shift in the spatial distribution reflects a major change in Mars' greenhouse effect and meteorology.
```

**Valley networks**, branching channels reminiscent of terrestrial drainage systems, are concentrated in the Noachian highlands. Their morphology (high drainage density, dendritic geometry, integrated catchment areas) most plausibly requires precipitation-fed runoff, which in turn requires sustained warm conditions over thousands or tens of thousands of years.

**Outflow channels** such as Kasei Valles and Ares Vallis are large-scale, scoured features that record catastrophic single events: the discharge of confined sub-permafrost aquifers in volumes orders of magnitude greater than any historical terrestrial flood. They are mostly Hesperian.

**Clay minerals (phyllosilicates)** were mapped from orbit by the OMEGA imaging spectrometer on *Mars Express* {cite:p}`Bibring2006` and the higher-resolution CRISM instrument on *Mars Reconnaissance Orbiter*. Clays form by aqueous alteration of basaltic rocks at near-neutral pH and require sustained or repeated contact with liquid water. Their distribution is overwhelmingly in Noachian terrain, with clay-rich patches scattered across the southern highlands. {cite:t}`Bibring2006` proposed a three-stage classification of Mars' aqueous history:

- the **phyllosian** (early Noachian): widespread clay formation, neutral pH water, the longest-duration wet phase;
- the **theiikian** (late Noachian / Hesperian): sulfate formation, acidic and evaporative water, much shorter duration;
- the **siderikian** (Amazonian): essentially dry, with anhydrous ferric oxides forming slowly through atmospheric weathering.

```{figure} figures/bibring2006_timeline.avif
:name: fig:bibring-timeline
:width: 550px
:align: center

The three-stage aqueous history of Mars proposed by {cite:t}`Bibring2006` from OMEGA imaging-spectrometer mineralogy: phyllosian (clays, neutral wet), theiikian (sulfates, acidic), siderikian (anhydrous ferric oxides, dry). The boundaries are correlated to but distinct from the chronostratigraphic Noachian / Hesperian / Amazonian divisions; surface volcanic activity and the global change toward an oxidising environment are marked above the bands.
```

```{figure} figures/bibring2006_globalmap.avif
:name: fig:bibring-global
:width: 700px
:align: center

OMEGA hyperspectral mapping of Mars from {cite:t}`Bibring2006`, showing the spatial distribution of phyllosilicate (clay) detections (top) and sulfate detections (bottom) across the global longitude range. Clays cluster in the Noachian southern highlands; sulfates are concentrated in lower-latitude and equatorial sites consistent with later, more acidic and evaporative aqueous environments.
```

**Sulfate deposits** record a later, drier, more acidic phase of Mars' history, often associated with evaporative settings. Both the *Opportunity* rover at Meridiani Planum and the *Curiosity* rover at Gale crater have made extensive in-situ measurements of sulfate-bearing strata.

**Deltas, fans, and lakebeds** are unambiguous evidence for standing surface water. The most spectacular are the deltas at Eberswalde, Jezero (now being explored by *Perseverance*), and the lakebed sediments at Yellowknife Bay in Gale crater (where *Curiosity* found mudstones interpreted as a long-lived, habitable lacustrine environment {cite:p}`Grotzinger2014`). Crucially, the existence of well-formed deltas and laminated lake sediments requires that water persisted in standing bodies for thousands to perhaps millions of years, far longer than transient melt events.

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

Global distribution of olivine on the Martian surface from TES and OMEGA spectroscopic mapping, with detail panels showing localised olivine-rich units exposed in impact craters. Fresh olivine implies limited aqueous alteration, helping to identify regions where water was rare or absent. From {cite:t}`EhlmannEdwards2014`.
```

The combined geological, mineralogical, and topographic record converges on a picture of a wetter, warmer, and more chemically active Mars during the Noachian, with progressively drier and colder conditions thereafter. Crater-counting based timing puts the wet period in the range $\sim 3.8$ to $3.6$ Ga, although episodic water activity may have continued well into the Hesperian (e.g. with the Hesperian outflow channels) and possibly later in localised hydrothermal systems.


### The early Mars climate puzzle

The geological evidence for surface liquid water on early Mars sits in apparent contradiction to a simple radiative argument. The Sun was about $30\%$ less luminous at $4$ Ga than today (the **faint young Sun** problem; {cite:p}`Feulner2012`). The Martian equilibrium temperature, which already lies near $200\ \mathrm{K}$ for the modern Sun, was therefore even colder back then. To maintain liquid water on the surface for the durations implied by valley networks and lake deposits, you need a strong greenhouse effect.

The textbook candidate is a thicker $\mathrm{CO_2}$ atmosphere. Increasing atmospheric $\mathrm{CO_2}$ raises infrared opacity and warms the surface. Early models suggested that a few-bar $\mathrm{CO_2}$ atmosphere could plausibly maintain near-freezing temperatures. {cite:t}`Wordsworth2016` reviewed this picture in detail and showed that pure $\mathrm{CO_2}$ atmospheres run into a serious problem: at high pressures and low temperatures, $\mathrm{CO_2}$ condenses into ice clouds, which raise the planetary albedo and *cool* the surface further, instead of warming it. There is a hard upper limit to how warm you can make Mars by piling on $\mathrm{CO_2}$, and that limit falls short of $273\ \mathrm{K}$ at most latitudes for the early-Noachian solar flux.

```{figure} figures/wordsworth2016_schematic.avif
:name: fig:wordsworth-schematic
:width: 700px
:align: center

Cartoon of the major climate processes operating on Mars in the Noachian and early Hesperian as conceived by {cite:t}`Wordsworth2016`. The "icy highlands" picture: snow accumulates in the elevated southern highlands, where adiabatic cooling makes them effective cold traps; episodic warming from impacts and volcanism delivers transient meltwater that flows downhill into the northern lowlands as standing bodies of water. $\mathrm{CO_2}$ clouds at high altitude can scatter or absorb infrared radiation but in net cool more than they warm.
```

Several escape routes from this contradiction have been proposed. One important class of solutions invokes additional reducing greenhouse gases such as $\mathrm{H_2}$ or $\mathrm{CH_4}$, supplied by volcanic outgassing or by serpentinisation of ultramafic rocks. {cite:t}`Wordsworth2017` showed that **collisionally induced absorption (CIA)** between $\mathrm{H_2}$ and $\mathrm{CO_2}$, in particular, has a much larger effect than previously appreciated and can significantly raise surface temperatures with modest concentrations of $\mathrm{H_2}$ ($\sim 1\%$ to $10\%$ by volume). This allows a warm or warm-and-episodic early Mars without unphysical $\mathrm{CO_2}$ pressures.

```{figure} figures/wordsworth2016_phasediagram.avif
:name: fig:wordsworth-phase
:width: 600px
:align: center

Idealised two-dimensional phase diagram for the long-term state of early Mars from {cite:t}`Wordsworth2016`, with surface temperature on the vertical axis and total surface $\mathrm{H_2O}$ inventory on the horizontal axis. Each quadrant corresponds to a distinct end-member regime: warm-and-wet (with a northern ocean), cold-and-wet (with extensive wet-based glaciation), cold-and-dry (the "icy highlands" scenario), and warm-and-dry. The geomorphological constraints favour the cold-and-dry regime as the time-averaged state, with episodic excursions to wetter conditions.
```

A second class of solutions relies on **episodic warm intervals** rather than sustained warmth. Large impacts deliver enough energy to melt and vaporise water locally for years to centuries, and explosive volcanism injects warming gases into the atmosphere on similar timescales. Models in this family predict that Mars was cold and icy on average, but punctuated by bursts of warmer climate during which valley networks formed. {cite:t}`KiteEpisodic2022` showed that such episodic warming, combined with high-altitude water-ice clouds, can be consistent with the observed valley distribution and with the constraint that the planet not stay warm for too long.

A third element is the dramatic shift in the spatial distribution of fluvial features from the Noachian to the Hesperian, mapped by {cite:t}`KiteCarter2022`. In the Noachian, fluvial activity is widespread across the southern highlands. In the late Hesperian and Amazonian, what little fluvial activity remains is concentrated in mid-latitude alluvial fans and deltas. {cite:t}`KiteCarter2022` argued that this latitudinal migration encodes a fundamental change in Mars' greenhouse mechanism between the two epochs: an early greenhouse sustained over the whole planet, followed by a late one that worked only seasonally and only at certain latitudes.

```{figure} figures/kite2022_schematic.avif
:name: fig:kite-schematic
:width: 700px
:align: center

A graphical summary of {cite:t}`KiteCarter2022`'s model for Mars climate evolution. **Left**: an early stage with high-elevation valleys feeding through lowlands during a warmer atmosphere, and a later stage with localised alluvial fans driven by episodic seasonal melting. **Right**: a phase diagram showing that, within a wide range of $\mathrm{CO_2}$ pressures, shifts to colder and drier states explain the observed geomorphology.
```

The current consensus is that early Mars climate was complex, with multiple greenhouse mechanisms operating, large fluctuations in opacity and temperature on $10^4$ to $10^7$-year timescales, and ultimately a one-way transition to the cold dry state of the modern planet. The exact balance between sustained warm conditions, episodic warming, and impact-driven hydrology remains under active debate. Mars climate is one of the major unsolved problems of planetary science.


### Modern Mars: thin atmosphere, dust, and methane

Mars today has a $\sim 6\ \mathrm{mbar}$ surface pressure, $95\%$ $\mathrm{CO_2}$, with traces of $\mathrm{N_2}$, $\mathrm{Ar}$, and $\mathrm{O_2}$. The mean surface temperature is $\sim 210\ \mathrm{K}$ and varies dramatically with latitude, season, and time of day.

**Dust** is a key climate player. Suspended dust grains heat the atmosphere by absorbing visible sunlight; the heated atmosphere expands and develops winds; the winds loft more dust. This positive feedback occasionally produces **global dust storms** that can obscure most of the planet's surface for weeks to months. The most recent global dust storm in 2018 was responsible for the death of the *Opportunity* rover, which lost solar power when its panels were shrouded.

The **seasonal $\mathrm{CO_2}$ cycle** is dramatic: roughly $25\%$ of the entire atmospheric mass condenses out onto the winter pole each Martian year and sublimates back during local spring. The pressure variations are large enough to be measured easily by surface meteorology stations. The polar caps themselves are layered structures of $\mathrm{CO_2}$ ice on top of permanent water-ice deposits, with finer-scale layering that records past obliquity and orbital cycles.

**Recurring slope lineae (RSL)** are dark streaks that form on steep, sun-facing slopes during warm seasons and fade in winter. When discovered by *MRO*, they were initially interpreted as the surface signature of seasonal briny water flows and were considered a possible biosignature target. Subsequent work has revised the interpretation toward **dry granular flows** triggered by thermal stress or saltation, with no need for liquid water (see also {ref}`lecture06`). The story is a useful methodological lesson: extraordinary claims require correspondingly thorough alternative tests.

**Methane** on Mars has a controversial history. The *Curiosity* rover's tunable laser spectrometer (TLS) reported detections of background methane at $\sim 0.4$ to $0.7\ \mathrm{ppb}$ inside Gale crater, with occasional spikes up to a few ppb. These detections, if accurate and global, would imply an active source on Mars (since photochemical destruction of $\mathrm{CH_4}$ has a lifetime of only $\sim 300$ years). The ESA *Trace Gas Orbiter*, launched in 2016 specifically to follow up these claims, has reported much lower upper limits over the same epochs ($< 0.05\ \mathrm{ppb}$ globally averaged). The two results are not strictly incompatible: the *Curiosity* detections may reflect highly localised, transient releases that do not mix to global scales before being destroyed, or (less satisfyingly) instrumental effects. The methane question is genuinely unresolved as of this writing, and the honest position is to flag both sets of measurements and the inconsistency between them.

**Dust devils** and other sub-grid meteorological phenomena have been monitored by *InSight*'s pressure and seismic sensors, providing the first sustained record of high-frequency atmospheric variability on another planet.


### Blackboard derivation: the Jeans escape flux

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

When $\lambda \gg 1$, the exponential dominates and the flux falls off as $e^{-\lambda}$. The dependence on $\lambda$ is steep: a change in $\lambda$ from $5$ to $10$ reduces the escape flux by a factor of $\sim 150$.

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

A few comments on the derivation. The factor $(1+\lambda)$ in equation {eq}`eq:jeans` reflects the fact that the escaping molecules carry away not only their kinetic energy (the raw Maxwellian tail) but also the work done against gravity as they climb out, which biases the escaping population toward higher initial velocities. In the limit $\lambda \to \infty$ the formula reduces to $\Phi_J \sim n v_{\mathrm{th}} \lambda e^{-\lambda}$, which is the standard high-$\lambda$ asymptotic form often quoted in textbooks.

The exobase concept is crucial: collisions below the exobase scramble velocities and prevent the high-velocity tail from accumulating, so escape effectively only happens at and above the exobase. The exobase altitude itself is set by where the mean free path equals the scale height, which depends on temperature, composition, and gravity. For Mars the modern exobase sits about $200\ \mathrm{km}$ above the surface; for Earth it is around $500$--$700\ \mathrm{km}$.

Finally, the temperature $T_{\mathrm{exo}}$ in the formula is the *exospheric* temperature, which is set primarily by absorption of solar EUV radiation in the upper atmosphere. The exospheric temperature varies with solar activity and was almost certainly much higher in the early solar system, when the young Sun emitted $10$--$100$ times more EUV than today. Hydrogen escape from early Mars would therefore have been much faster than the modern formula gives, and an early hydrogen-rich greenhouse (see above) could have lost its $\mathrm{H_2}$ on a timescale of only a few tens of Myr.


### Atmospheric escape and the loss of Mars' atmosphere

Jeans escape removes only the lightest species. Because Mars *has* lost a substantial mass of $\mathrm{CO_2}$ and water over its history, other escape mechanisms must dominate the heavier atoms. NASA's **MAVEN** orbiter (Mars Atmosphere and Volatile EvolutioN), in orbit since 2014, was designed to measure these escape channels directly {cite:p}`Jakosky2018`. The main non-thermal channels are:

- **Photochemical escape of atomic oxygen**, in which dissociative recombination of $\mathrm{O_2^+}$ ions in the upper atmosphere produces neutral O atoms with kinetic energy of a few eV, enough to exceed the escape velocity. This is the dominant loss channel for oxygen today.
- **Ion escape via the solar wind**: $\mathrm{O^+}$, $\mathrm{O_2^+}$, and $\mathrm{CO_2^+}$ ions produced by ionisation of the upper atmosphere are picked up by the convective electric field of the solar wind and accelerated to escape velocity.
- **Sputtering** by solar wind ions impacting the upper atmosphere, which knocks out neutral atoms and molecules.
- **Jeans escape of hydrogen** (the only light species relevant), supplied by photolysis of water vapour throughout the atmosphere.

```{figure} figures/jakosky2018_loss.avif
:name: fig:jakosky-loss
:width: 500px
:align: center

Total atmospheric loss rate from Mars as a function of time since the formation of the planet, extrapolating MAVEN-measured present-day rates back through solar system history using estimates of the past solar EUV flux. Loss rates were $10$ to $100$ times higher in the first billion years than today. Integrated over $4$ Gyr, the cumulative loss is consistent with $\sim 0.5$ to $1$ bar of $\mathrm{CO_2}$ and $\sim 23$ m global equivalent layer of $\mathrm{H_2O}$. From {cite:t}`Jakosky2018`.
```

```{figure} figures/jakosky2018_hloss.avif
:name: fig:jakosky-h
:width: 500px
:align: center

H corona column density at Mars as a function of solar longitude over a Mars year. Hydrogen escape varies by an order of magnitude over the seasonal cycle, peaking near perihelion when the lower atmosphere is warmer and water vapour rises to higher altitudes where it is photolysed. From {cite:t}`Jakosky2018`.
```

{cite:t}`Jakosky2018` summarised the integrated loss of the Martian atmosphere through history using the present-day MAVEN measurements scaled with reasonable assumptions about the evolution of the young Sun's EUV output. The headline result is that, over $4$ Gyr, Mars has lost the equivalent of $\sim 0.5$ to $1$ bar of $\mathrm{CO_2}$ and the equivalent of a $\sim 23$ m global ocean of water. Both numbers come with substantial uncertainty (factors of two or so), but they are large enough to bridge the gap between an early Mars with a thick wet atmosphere and the cold dry planet we see today. The escape was strongly enhanced in the first $\sim 1$ Gyr of solar system history, when the young Sun's EUV output was $10$ to $100$ times higher than today.

```{figure} figures/hu2015_carbon_evolution.avif
:name: fig:hu-carbon
:width: 650px
:align: center

Reconstructed history of carbon partitioning on Mars from {cite:t}`Hu2015`, using the modern atmospheric $^{13}\mathrm{C}/^{12}\mathrm{C}$ ratio and known carbonate measurements as boundary conditions. **(a)** Atmospheric surface pressure of $\mathrm{CO_2}$ as a function of time since $3.8\ \mathrm{Ga}$ for a family of self-consistent solutions; **(b)** integrated $\mathrm{CO_2}$ loss to space by sputtering; **(c)** integrated loss by photochemical escape; **(d)** equivalent column of $\mathrm{CO_2}$ stored in carbonates. The solutions imply a Late Noachian / Early Hesperian atmospheric pressure of less than $1\ \mathrm{bar}$ in scenarios with surface (open-lake) carbonate formation, or up to $\sim 1.8\ \mathrm{bar}$ if substantial subsurface carbonate sequestration is allowed. The picture is consistent with the MAVEN-based escape budget but explicitly invokes the heavy-isotope enrichment of carbon as an independent constraint.
```

The Martian dynamo plays a critical role in this story. As long as Mars had a global magnetic field, the solar wind was deflected around the planet at a magnetopause analogous to (though smaller than) Earth's. Atmospheric ions in the upper Martian atmosphere were largely shielded from direct solar wind interaction, and ion escape was suppressed. Once the dynamo died (as we see next), the magnetic shield collapsed, the solar wind began interacting directly with the upper atmosphere, and ion escape became efficient. The link between dynamo cessation and atmospheric loss is one of the cleanest causal narratives in comparative planetology.


### Mars magnetism and the death of the dynamo

Although Mars has no global magnetic field today, the *Mars Global Surveyor* magnetometer discovered in 1999 that large parts of the southern highlands carry intense **crustal magnetic anomalies** {cite:p}`Acuna1999`. These are remanent fields, frozen into the Noachian crust when basaltic rocks cooled through their Curie temperatures in the presence of an ancient core dynamo. The magnetic anomalies are spectacularly strong (locally reaching $\sim 1500\ \mathrm{nT}$ at $400\ \mathrm{km}$ altitude, an order of magnitude stronger than the strongest crustal anomalies on Earth), confirming that the Martian dynamo, while it operated, produced a vigorous magnetic field.

```{figure} figures/acuna1999_magmap.avif
:name: fig:acuna-map
:width: 700px
:align: center

Map of the radial component of the magnetic field measured by *Mars Global Surveyor* MAG/ER instrument at $400\ \mathrm{km}$ altitude. Strong remanent crustal magnetisation (red and blue patches) is concentrated in the Noachian-aged southern highlands; the younger northern lowlands and the Hellas and Argyre impact basins are essentially demagnetised. From {cite:t}`Acuna1999`. Courtesy NASA Goddard Space Flight Center.
```

```{figure} figures/acuna1999_dipoles.avif
:name: fig:acuna-dipoles
:width: 600px
:align: center

Equivalent dipole sources fitted to the strongest crustal anomalies, showing concentration in Terra Cimmeria and Terra Sirenum. The lack of crustal magnetisation across Hellas, Argyre, and the Borealis lowlands implies that the dynamo had switched off before those basins formed and reset their thermal state. From {cite:t}`Acuna1999`. Courtesy NASA Goddard Space Flight Center.
```

The spatial pattern is the key to dating the dynamo. The Hellas, Argyre, and Isidis impact basins, each of which formed by very large impacts in the late Noachian, are essentially *demagnetised* relative to the surrounding terrain. The interpretation is that these impacts heated the underlying crust above the magnetite Curie temperature ($\sim 850\ \mathrm{K}$) and erased its remanent magnetisation; when the crust cooled back down, there was no longer an active dynamo to record. Bracketing the basin ages places the death of the Martian dynamo around $4.1$--$3.9\ \mathrm{Ga}$ in the original {cite:t}`Acuna1999` analysis.

This picture has been refined over time. {cite:t}`Mittelholz2020` analysed *MAVEN* magnetometer data from low-altitude passes over the $\sim 3.7\ \mathrm{Ga}$ Lucus Planum lava flow and detected a small but significant remanent field, suggesting that the dynamo (or at least episodes of it) was still operating at $3.7\ \mathrm{Ga}$, somewhat later than the basin-based estimate. {cite:t}`Lillis2024` very recently proposed that the apparent demagnetisation of the impact basins might instead reflect a *reversing* dynamo, in which the geometry of the field was changing on timescales short compared to basin cooling times, smearing out the recorded direction. Both findings push the death of the Martian dynamo somewhat later, possibly into the early Hesperian, and reduce the temporal gap between the loss of the dynamo and the loss of the atmosphere.

The connection to atmospheric loss is direct. Once the dynamo failed, the magnetic shield collapsed and the solar wind began to interact directly with the upper atmosphere of Mars, accelerating ion escape and (over hundreds of Myr to Gyr) stripping the planet of much of its $\mathrm{CO_2}$ and water inventory. Mars is the textbook case of a world where the loss of internal magnetism was followed by the loss of habitability.


### Mars exploration: a brief history

Mars exploration is the longest-running campaign of planetary science. The *Mariner 4* flyby in 1965 returned the first close-up images of Mars, dispelling pre-spacecraft visions of canals and Earth-like surface conditions and revealing instead a heavily cratered, desert-like world. The *Mariner 9* orbiter in 1971--72 revealed the volcanoes, the canyons, and the polar caps for the first time and showed how dramatic the contrast was between the cratered south and the smoother north.

The **Viking program** (1976) landed two spacecraft on the Martian surface and conducted the first dedicated experiments to look for biology in Martian soil. The biology results were ambiguous (small chemical reactions were detected, but their interpretation as biological versus chemical remained unresolved); the meteorology and imaging results were extraordinarily productive and set the framework for everything that followed.

The 1990s were the decade of orbital mapping. **Mars Global Surveyor** (1997--2006) carried MOLA, the Mars Orbiter Camera, and the Mars Orbiter Laser Altimeter, producing global topography {cite:p}`Smith2001` and discovering the crustal magnetic anomalies {cite:p}`Acuna1999`. **Mars Pathfinder** (1997) tested entry-descent-landing technology and operated the first Mars rover, *Sojourner*. **Mars Odyssey** (2001--present, the longest-running Mars mission) mapped subsurface hydrogen with its gamma-ray and neutron spectrometers, providing the first direct evidence for buried water ice in mid-latitudes.

The 2000s were the decade of rovers. **Spirit** and **Opportunity** (Mars Exploration Rovers, 2004) demonstrated that small mobile platforms could conduct sustained surface science and traversed many kilometres each. Both found in-situ evidence for past water in their respective landing sites. **Mars Express** (ESA, 2003--present) carried the OMEGA imaging spectrometer, which revealed the global mineralogy summarised by {cite:t}`Bibring2006`. **Mars Reconnaissance Orbiter** (2006--present) provided the first sub-metre imaging of the Martian surface and the higher-resolution CRISM spectrometer, refining the OMEGA-era mineralogy.

The 2010s and 2020s have been dominated by **Curiosity** at Gale crater (2012--present) and **Perseverance** at Jezero crater (2021--present). *Curiosity*, with its analytical laboratory suite, established the long-duration habitable lacustrine environment at Yellowknife Bay {cite:p}`Grotzinger2014` and has now provided more than a dozen years of continuous in-situ environmental monitoring. *Perseverance* is exploring the delta deposits at the mouth of Jezero crater and *caching* selected rock cores in sealed sample tubes for future return to Earth. The **Ingenuity** helicopter that arrived with Perseverance demonstrated, for the first time, powered atmospheric flight on another planet.

Other recent additions to the Mars fleet include China's **Tianwen-1** (2021), which delivered the *Zhurong* rover to Utopia Planitia in the first national Mars-orbit-and-rover mission outside the US. The UAE's **Hope** orbiter (2021) studies Mars meteorology from a high orbit. **InSight** operated as a stationary geophysical station from 2018 to 2022, generating the seismic and heat-flow results discussed above. ESA's **Trace Gas Orbiter** (2016--present) measures atmospheric trace gases including the controversial methane, and ESA's **Rosalind Franklin** rover (delayed by the cancellation of the Russian-supplied lander, now scheduled for the late 2020s) will carry a deep-drilling capability to look for organic biosignatures meters below the surface, where solar UV radiation cannot reach.


### Mars Sample Return and the question of biosignatures

Mars Sample Return (MSR) is the joint NASA-ESA campaign to retrieve the rock samples that *Perseverance* is currently caching at Jezero. The scientific case is essentially undisputed: bringing Mars rocks back to Earth would let us apply the full arsenal of terrestrial laboratory instruments (high-resolution mass spectrometers, electron microscopes, chemical-isotope-imaging tools, microbiology assays) to materials selected for the highest astrobiological potential. The primary scientific goal is to determine whether the samples contain definitive biosignatures from past or present Martian life {cite:p}`Beaty2019`. Even a confident negative result would tightly constrain models of the origin of life and would inform the search for biosignatures elsewhere.

The **subglacial liquid water** debate is a relevant counterpoint. {cite:t}`Orosei2018` reported reflections in radar data from the *MARSIS* instrument on *Mars Express* that, if interpreted as a dielectric contrast at the base of the south polar cap, would imply a $\sim 20\ \mathrm{km}$-wide subglacial lake of liquid water. This would have been the first detection of stable liquid water on Mars and would have strong implications for habitability. Subsequent reanalyses, however, have argued that the same radar signature can be reproduced by conductive (clay-rich) basal layers without liquid water. As of writing the interpretation is contested, and the broader question of whether stable liquid water exists anywhere on or beneath the Martian surface today is open.

The **MSR programme itself** is going through difficulties. The original NASA-ESA architecture targeted return of the cached samples in the early 2030s. In 2024, NASA announced a major rebaselining of the programme: the reference mission was deemed too expensive and too slow, and an architecture-review process was launched. As of early 2026 the architecture, the schedule, and the total cost are all uncertain, with industry studies and competing concepts under evaluation {cite:p}`NASAESAMSR2024`. The scientific imperative remains, but the path from a *Perseverance* sample tube on Mars to a clean-room laboratory on Earth has become much more uncertain than it appeared a few years ago.


## Part 3: Comparative payoff for terrestrial planet evolution

### Mercury and Mars as opposite limiting cases

Stepping back from the details of each planet, what does the comparison teach us?

**Mercury** is the smallest of the rocky planets, sitting closest to the Sun, with the lowest volatile inventory, the shortest cooling timescale (smallest body), and the strongest stellar irradiation. It has cooled rapidly, contracted, frozen most of its core, lost essentially all its volatiles, and yet (against naive expectations) it sustains a small active dynamo and hosts polar ice. Each of these "yet" features turned out to require physical mechanisms that are individually well-understood (a thin convecting outer core for the dynamo, near-zero obliquity and cold-trapping for the ice) but are not what you would have predicted from a one-line description of "small, hot, inner planet."

**Mars** is medium-sized, sits at the outer edge of the habitable zone with substantial volatile delivery from the icy regions of the early disc, cooled more slowly, and hosted both a dynamo and surface liquid water for the first $\sim 700$ Myr of its history. Then, in a sequence we cannot yet date precisely, it lost the dynamo, lost most of its atmosphere, and dried out. Mars therefore serves as a tragic mirror for Earth: a planet that had the ingredients for habitability and lost them.

Both bracket Earth and Venus on the scaling relations of {ref}`lecture03` and {ref}`lecture04`:

- **Cooling rate** scales (very approximately) as $L^2/\kappa$ for diffusive heat loss with $L$ the body size. A factor of two smaller body cools four times faster.
- **Atmospheric retention** depends exponentially on the escape parameter $\lambda$ from equation {eq}`eq:lambda`, and $\lambda \propto M / (T r_{\mathrm{exo}})$. Smaller and hotter bodies hold less.
- **Volatile inventory** at formation depends on heliocentric distance through the ice line and through the timing of volatile delivery from outer-disc bodies (compare with {ref}`lecture02`).

Mercury fails the first two of these on every count. Mars fails the second and third: its mass is enough to hold a thick atmosphere if it can keep the dynamo running, but not enough once the dynamo dies and ion escape takes over.


### Size and distance set the trajectory

If we had to summarise the comparative lesson in one sentence, it would be this: **size and distance from the central star are the two parameters that primarily determine the long-term evolution of a rocky planet, and most other properties (interior structure, atmospheric composition, climate, habitability) are consequences of those two.**

Size controls the rate of interior cooling, the heat budget available to drive a dynamo, the surface gravity (and hence the escape parameter $\lambda$), and the amount of long-lived radiogenic heating in absolute terms. Distance from the Sun controls the equilibrium temperature, the volatile delivery during accretion, the strength of stellar wind erosion of the upper atmosphere, and the dynamics of the early hot phase of the planet's history.

Tectonic regime, dynamo longevity, atmospheric retention, and surface habitability are mostly downstream consequences of these two parameters, modulated by stochastic events such as giant impacts, the timing of accretion, and the chaotic dynamics of obliquity.

This is the framework we will need in {ref}`lecture13` and {ref}`lecture14` when we look at what we can infer about exoplanets, where size and orbital distance are typically the *only* two parameters we know.


### The timing problem: dynamo lifetimes and habitability

The four rocky planets in the inner solar system show four distinct dynamo histories. **Earth** has an active dynamo today, sustained by inner-core crystallisation that releases compositional buoyancy. **Mercury** has an active but very weak dynamo today, sustained by some combination of partial inner-core freezing and convection in a thin liquid shell, with possible thermal stratification. **Mars** had a strong dynamo for the first $\sim 500$--$800$ Myr of its history and then lost it. The original basin-demagnetisation analysis of {cite:t}`Acuna1999` placed the cessation around $4.1$--$3.9$ Ga, while more recent re-analyses by {cite:t}`Mittelholz2020` and {cite:t}`Lillis2024` push the dynamo's last activity somewhat later, possibly into the early Hesperian around $4.0$--$3.7$ Ga. The exact end date is uncertain in between. **Venus** has no detectable intrinsic field today, but the timing of its dynamo cessation (and whether one ever existed) remains genuinely unknown ({ref}`lecture09`).

The pattern is striking. **Dynamo longevity correlates with atmospheric retention and surface habitability** across the rocky planets in our solar system. Earth, the only one with a long-lived dynamo, is also the only one with a thick atmosphere stable on Gyr timescales and (so far as we know) the only one with surface life. Mars and Venus, both of which lack present-day dynamos, have lost most of their atmospheric inventories (Mars to space, Venus to runaway greenhouse and chemical lock-in) and are uninhabitable today. Mercury never had a chance to develop an Earth-like atmosphere because its small size and proximity to the Sun gave it neither the volatile inventory nor the gravitational retention to begin with.

This correlation does not by itself prove a causal link between dynamo longevity and habitability. The escape rates measured by *MAVEN* show that even an unmagnetised Mars-sized planet only loses its atmosphere on $10^9$-year timescales, so the loss of the dynamo is not always immediate atmospheric collapse. But the magnetic shield does suppress ion escape by up to an order of magnitude, and over Gyr timescales an order of magnitude matters.


### What makes a rocky planet habitable?

Synthesising the lessons of {ref}`lecture09` and this lecture, we can identify at least four largely independent ingredients that a rocky planet appears to need for long-term surface habitability:

1. **Liquid water at the surface for an extended duration.** This requires (a) a sufficient volatile inventory at formation, (b) an equilibrium temperature in the right range (or compensating greenhouse gases), and (c) a surface pressure high enough that water is stable as a liquid against vacuum boiling.

2. **Active geology that recycles volatiles between the surface, atmosphere, and interior.** On Earth this is plate tectonics with carbonate-silicate weathering. On other bodies, alternative recycling mechanisms (heat-pipe volcanism, repeated lithospheric overturn, cryovolcanism on icy worlds) might in principle do similar work. The key is that volatiles must not be permanently sequestered in any single reservoir.

3. **Magnetic shielding from stellar wind erosion**, especially around active stars or close-in planets. The role of magnetic shielding is debated quantitatively (the dependence on field strength and stellar conditions is complex), but the comparison between magnetised Earth and unmagnetised Mars is one of the strongest empirical cases that magnetism matters.

4. **Long-term climate stability**, normally provided by some negative feedback loop on temperature. The textbook Earth example is the carbonate-silicate cycle (the Walker thermostat; {cite:p}`Walker1981`), in which higher temperature accelerates silicate weathering, removes more $\mathrm{CO_2}$ from the atmosphere, and cools the planet back down. Equivalent feedbacks must exist on any habitable planet.

Earth ticks all four ingredients. Venus and Mars each fail on at least two. Mercury never even started: too small, too close, no volatiles, no atmosphere. The four ingredients are not strictly independent in nature, but they are conceptually distinct enough that thinking through them is a useful exercise when assessing the habitability of an exoplanet.

We will return to this list explicitly in {ref}`lecture14` when we put together the synthesis of habitability across the diverse rocky-planet population that the next decade of observation will reveal.


### Recent advances and upcoming missions

The next decade is likely to be a golden era for comparative rocky-planet science:

- **BepiColombo** (ESA/JAXA): orbit insertion at Mercury in late 2026, followed by simultaneous operation of the MPO and Mio orbiters until at least 2028. New maps of the magnetic field, the surface composition, the polar ice inventory, and the moment of inertia.
- **JAXA MMX**: launch in 2026, sample return from Phobos in 2031. The first sample return from the Mars system. Should resolve the captured-asteroid versus giant-impact-debris debate for the origin of the Martian moons.
- **ExoMars Rosalind Franklin** (ESA): the rebooted European Mars rover, now scheduled for launch in $\sim 2028$. Subsurface drilling for biosignatures.
- **Mars Sample Return**: architecture under review as of 2026, with a return date now uncertain but unlikely before the early-to-mid 2030s. The scientific stakes remain extremely high; any positive biosignature detection would be among the most consequential results in the history of science.
- **Curiosity and Perseverance** continue operating; *Curiosity* now has more than thirteen years of continuous environmental data from Gale crater, the longest-baseline single-location record of another planet's climate ever assembled.
- **Subsurface water radar**: continued analysis of MARSIS and SHARAD data is refining our maps of buried polar and mid-latitude ice. The interpretation of bright reflections at the south polar cap base remains contested but is observationally tractable with future missions.
- **Ingenuity legacy**: the success of the *Ingenuity* helicopter has spawned several mission concepts for larger rotorcraft and aerial platforms on Mars and other planets.


## Summary and takeaways

- **Mercury and Mars are limiting cases for rocky-planet evolution.** Mercury is too small, too close, and too volatile-poor; Mars is too small to retain its atmosphere once the dynamo died. Both bracket Earth and Venus on the parameters that matter most for long-term habitability: size, distance, dynamo longevity, atmospheric retention.
- **Each of Mercury's oddities points to a specific physical mechanism.** The high uncompressed density requires non-standard formation, plausibly involving giant impacts. The persistent weak dynamo requires a thin convecting shell with thermal stratification. The polar ice survives because the obliquity is essentially zero. The lobate scarps and active faulting record ongoing global contraction.
- **Mars preserves the geological record of an Earth-like planet that lost its habitability.** The Noachian was wet enough to form valley networks, lakes, and clays. The Hesperian saw transitional, more acidic conditions and the bulk of the volcanic resurfacing. The Amazonian is the cold dry modern Mars. The dynamo died sometime between $4.1$ and $3.7$ Ga (the basin-demagnetisation estimate of $4.1$--$3.9$ Ga, refined by more recent magnetometer analyses to as late as $\sim 3.7$ Ga), and atmospheric loss to space (now measured in real time by MAVEN) accumulated to $\sim 0.5$--$1$ bar of $\mathrm{CO_2}$ and $\sim 23$ m of water over geological time.
- **The Jeans escape formula, equation {eq}`eq:jeans`, is selective.** Light species escape; heavy species do not. Mars' atmospheric loss is dominated by non-thermal (photochemical and ion-escape) processes, not by Jeans escape, except for hydrogen.
- **Comparative planetology with the four rocky planets gives us four independent natural experiments** on the parameters that determine planetary evolution. This is the best calibration we will have for the inevitable next step of comparing those four solar-system worlds with the much larger sample of rocky exoplanets we will see in {ref}`lecture13` and {ref}`lecture14`.


## References

```{bibliography}
:filter: docname in docnames
```
