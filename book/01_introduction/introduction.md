(lecture01)=
# Introduction & History of Planetary Science

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the scope of planetary science, explain how the field has evolved from antiquity to the space age, and identify the key properties and classification of solar system bodies.
```

```{seealso}
**Slides:** [Download Lecture 1 (PDF)](../_static/slides/lecture01.pdf)
```

## A pale blue dot

On 14 February 1990, the Voyager 1 spacecraft turned its camera back toward the inner solar system one last time. From a distance of 6 billion km, about 40 AU, it captured an image in which Earth appears as a tiny speck, less than a single pixel, suspended in a scattered beam of sunlight ({numref}`fig:pale-blue-dot`). Carl Sagan, who had campaigned for years to have the photograph taken, wrote: *"Look again at that dot. That's here. That's home. That's us"* {cite:p}`Sagan1994`. Minutes later, Voyager's cameras were switched off for good.

```{figure} figures/pale_blue_dot.avif
:name: fig:pale-blue-dot
:width: 350px
:align: center

The Pale Blue Dot. Earth appears as a tiny bright speck roughly halfway down the rightmost sunbeam. Captured by Voyager 1 on 14 February 1990 from approximately 6 billion km (40 AU). Image PIA00452. Credit: NASA/JPL-Caltech.
```





The Pale Blue Dot is one frame in a much larger 60-frame "Family Portrait" mosaic that Voyager 1 returned the same day, the only time a spacecraft has imaged the entire planetary system from outside ({numref}`fig:family-portrait`).

```{figure} figures/family_portrait.avif
:name: fig:family-portrait
:width: 700px
:align: center

The Voyager 1 "Family Portrait" of the solar system, 14 February 1990, taken from approximately 6 billion km. Six planets are visible across this 60-frame mosaic spanning roughly 70 degrees of sky: Venus, Earth, Jupiter, Saturn, Uranus, and Neptune. Mercury was lost in the Sun's glare, and Mars was too small to be detected. The Pale Blue Dot ({numref}`fig:pale-blue-dot`) is a zoom into the Earth frame. Credit: NASA/JPL-Caltech, PIA00451.
```

A second image taken from lunar orbit two decades earlier captured the same essential idea from much closer in: Earth as a finite, fragile world set against an empty sky ({numref}`fig:earthrise-apollo8`).

```{figure} figures/earthrise_apollo8.avif
:name: fig:earthrise-apollo8
:width: 500px
:align: center

"Earthrise", Apollo 8, 24 December 1968. Earth rises above the lunar limb during the first crewed mission to leave Earth orbit. The image is widely credited with shifting public perception of Earth as a single, finite system, an early articulation of the comparative-planetology perspective that this course adopts throughout. NASA image AS8-14-2383. Credit: NASA / William Anders.
```

That image captures something essential about planetary science: it asks us to see our own world not as the centre of the universe, but as one planet among many, a physical system that can be studied, compared, and understood. This course is built around three questions that drive that effort:

1. **How did our solar system form, and is it typical?** Before 1992, we knew of exactly zero planets outside our solar system. Today we have confirmed more than 6,000 exoplanets in over 4,500 systems {cite:p}`NASAExoplanetArchive2026`. Statistical analyses of the Kepler survey suggest that roughly 0.37–0.60 rocky, habitable-zone planets exist per Sun-like star ({numref}`fig:eta-earth`) {cite:p}`Bryson2021`, implying hundreds of millions of such worlds in the Milky Way alone. Yet we have detailed knowledge of only one planetary system.

2. **What determines whether a planet becomes habitable?** Venus, Earth, and Mars all formed from the same protoplanetary disk, likely with similar initial compositions. All three may have had early liquid water. Yet today Venus has a 464 °C surface beneath 92 bar of CO$_2$, Earth has oceans and a biosphere, and Mars is a cold desert with an atmosphere thinner than 1% of Earth's. Understanding why they diverged is one of the central puzzles of planetary science.

3. **Are we alone?** JWST is currently attempting to detect and characterise atmospheres on rocky exoplanets, including the TRAPPIST-1 system. Within your careers, this question may become answerable, but only if we understand what makes a planet habitable in the first place.

```{figure} figures/eta_earth_posterior.avif
:name: fig:eta-earth
:width: 100%
:align: center

Posterior probability density on $\eta_\oplus$, the average number of rocky habitable-zone planets per Sun-like star, derived from Kepler data. **Left panel:** *conservative* habitable-zone definition (moist-greenhouse inner edge to maximum-greenhouse outer edge, the range over which liquid water can be reliably maintained at the surface). **Right panel:** *optimistic* habitable-zone definition (inner edge extended to the recent-Venus insolation bound and outer edge to early-Mars, capturing the wider range over which surface water may have been transiently stable). The two coloured posteriors bracket the unknown survey completeness at orbital periods beyond Kepler's 500-day calibration limit: the **blue** curve (legend `extrap_const`) assumes that the detection completeness stays constant at its 500-day value, which overestimates completeness for longer periods and therefore gives a *lower* bound on $\eta_\oplus$; the **orange** curve (legend `extrap_zero`) assumes that completeness drops to zero beyond 500 days, underestimating completeness and therefore giving an *upper* bound on $\eta_\oplus$. The posterior peak shifts from $\eta_\oplus \approx 0.37$ planets per star for the conservative HZ to $\approx 0.60$ for the optimistic HZ, the range quoted in the text. Either way, habitable-zone rocky planets around Sun-like stars are common. Credit: {cite:t}`Bryson2021`.
```

Every topic in this course, from orbital dynamics and interior structure to atmospheric physics and surface geology, connects back to these three questions. By the end, you will have the tools to think about them quantitatively.

## What is a planet?

The word "planet" derives from the Greek *planetes* (πλανήτης), meaning "wanderer." To ancient observers, the planets were the five visible points of light (Mercury, Venus, Mars, Jupiter, and Saturn) that moved against the fixed background of stars. Together with the Sun and Moon, these seven wanderers gave us the seven days of the week.

For over two millennia, the list of planets seemed settled. That changed with the invention of the telescope. William Herschel discovered Uranus in 1781, the first planet found in modern times. In 1846, Johann Galle observed Neptune at a position predicted independently by Urbain Le Verrier and John Couch Adams from perturbations in Uranus's orbit, a triumph of Newtonian mechanics. And in 1930, Clyde Tombaugh discovered Pluto at Lowell Observatory after a painstaking photographic search.

But Pluto was always an oddity: small, icy, with an eccentric and inclined orbit that crosses Neptune's. When astronomers began discovering other large objects in the Kuiper Belt in the 1990s and 2000s, culminating in the discovery of Eris in 2005 by {cite:t}`Brown2005`, which appeared comparable in size to Pluto, the question became unavoidable: either these new objects were also planets, or Pluto was not. The 2015 New Horizons flyby ({numref}`fig:pluto-new-horizons`) revealed an unexpectedly active world, complicating the debate further.

```{figure} figures/pluto_new_horizons.avif
:name: fig:pluto-new-horizons
:width: 500px
:align: center

Pluto in enhanced colour from NASA's New Horizons spacecraft, July 2015. The dark reddish region on the left (Cthulhu Macula) and the bright nitrogen-ice plains visible to the right (the western edge of Tombaugh Regio, the "heart") highlight a surface diversity that was completely unexpected for a body of Pluto's size. New Horizons revealed water-ice mountains, glacial flows, and possible cryovolcanism, reigniting debate over Pluto's planetary status. Credit: NASA/JHUAPL/SwRI.
```

### The IAU definition

On 24 August 2006, the International Astronomical Union (IAU) adopted Resolution 5A, establishing three criteria for a body in the solar system to be classified as a **planet** {cite:p}`IAU2006`:

1. It is in orbit around the Sun.
2. It has sufficient mass for its self-gravity to overcome rigid body forces, so that it assumes a hydrostatic equilibrium (nearly round) shape.
3. It has **cleared the neighbourhood** around its orbit.

A body satisfying criteria 1 and 2 but not 3 is a **dwarf planet**. Under this definition, the solar system has eight planets and five officially recognised dwarf planets: Ceres, Pluto, Eris, Makemake, and Haumea. Many additional candidates exist in the Kuiper Belt.

The definition remains debated. Critics note that "clearing the neighbourhood" is not precisely defined and depends on heliocentric distance: Earth would not clear its zone if placed at Neptune's orbit. An alternative **geophysical definition** proposes that any body massive enough to achieve hydrostatic equilibrium should count as a planet, regardless of its orbital dynamics {cite:p}`Runyon2017`. Under this broader definition, the solar system would have well over 100 planets.

For this course, the exact classification matters less than the physics. The important point is that the solar system contains a continuous spectrum of objects, from dust grains to gas giants, governed by the same physical laws.

## Brief history of planetary science

Planetary science as a discipline is remarkably young, but its roots reach back to the earliest recorded observations.

### Ancient and pre-telescopic astronomy

Babylonian astronomers systematically tracked planetary positions as early as 1800 BCE, developing arithmetical methods to predict conjunctions and oppositions. Greek natural philosophers constructed geometric models: Aristotle's geocentric spheres (~350 BCE) and Ptolemy's epicyclic system (~150 CE) remained the standard framework for over a millennium.

The Copernican revolution began in 1543, when Nicolaus Copernicus published *De revolutionibus*, placing the Sun at the centre ({numref}`fig:copernican-system`). Johannes Kepler refined this model into his three empirical laws of planetary motion (1609–1619), replacing circles with ellipses. Isaac Newton's *Principia* (1687) showed that all three of Kepler's laws follow from a single universal law of gravitation, the first grand unification in physics.

```{figure} figures/copernican_system.avif
:name: fig:copernican-system
:width: 350px
:align: center

Heliocentric model of the solar system from Copernicus's *De revolutionibus orbium coelestium* (1543). The Sun sits at the centre, with the planets orbiting outward in concentric spheres. The Latin inscriptions, from the centre out, read *Sol* (Sun), *Mercurius* (Mercury), *Venus*, *Terra* (Earth, with the Moon as a small orbit attached), *Mars*, *Iupiter* (Jupiter), *Saturnus* (Saturn), and the outer band *Stellarum Fixarum Sphaera Immobilis* (the immobile sphere of the fixed stars). This woodcut marks the conceptual shift from the geocentric cosmology that had dominated for over a millennium. Credit: Nicolaus Copernicus, public domain.
```

### The telescopic era

Galileo Galilei's telescope observations in 1610 transformed planetary science from mathematics into a physical science. He discovered four moons orbiting Jupiter (now called the Galilean moons; see {numref}`fig:sidereus-nuncius`), observed the phases of Venus (confirming it orbits the Sun), and resolved Saturn's rings (though he could not interpret their structure).

```{figure} figures/sidereus_nuncius.avif
:name: fig:sidereus-nuncius
:width: 334px
:align: center

Page from Galileo's *Sidereus Nuncius* (1610) showing his observations of Jupiter and its four largest moons, named here the *Medicea Sidera* (Medicean Stars) in honour of Galileo's Medici patrons. Each row records the positions of the moons (small dots) relative to Jupiter (open circle) on successive nights. The systematic motion of the four points, repeating with periods of days, was direct evidence that not all celestial bodies orbit the Earth. Simon Marius proposed the mythological names *Io*, *Europa*, *Ganymede*, and *Callisto* in 1614; these gradually replaced the Medicean designation and are the names you will meet in {ref}`Lecture 11 <lecture11>`. Credit: Galileo Galilei, public domain.
```

Over the following centuries, improving telescopes revealed surface features on Mars, the Great Red Spot on Jupiter, and the detailed ring structure of Saturn.

The 19th century brought spectroscopy, allowing astronomers to determine atmospheric compositions remotely for the first time. Photography enabled systematic surveys, and the discoveries of Uranus, Neptune, and Pluto progressively expanded the known solar system.

### The space age

The modern era of planetary science began on 14 December 1962, when NASA's Mariner 2 flew past Venus, the first spacecraft to successfully visit another planet. This flyby revealed Venus's extreme surface temperature, overturning earlier speculation about habitable conditions beneath its clouds.

The pace of exploration accelerated rapidly. Mariner 4 returned the first close-up images of Mars in 1965 ({numref}`fig:mariner4-mars`), revealing a cratered, apparently dead world, not the canal-laced surface some had imagined. The Soviet Venera 7 achieved the first landing on another planet (Venus, 1970). NASA's Viking landers (1976) conducted the first experiments searching for life on Mars. The twin Voyager spacecraft (launched 1977) exploited a rare planetary alignment to conduct a grand tour of the outer solar system, visiting Jupiter, Saturn, Uranus, and Neptune between 1979 and 1989 ({numref}`fig:voyager2-trajectory`).

```{figure} figures/mariner4_mars.avif
:name: fig:mariner4-mars
:width: 350px
:align: center

The first close-up image of another planet's surface: Mariner 4, 15 July 1965. Mariner 4 returned 21 frames during the brief Mars encounter, of which this is one of the most reproduced. The heavily cratered, Moon-like terrain visible here decisively ended speculation about Martian canals and surface vegetation. Mars's geology and atmosphere are revisited in {ref}`Lecture 10 <lecture10>`. Credit: NASA/JPL.
```

```{figure} figures/voyager2_trajectory.avif
:name: fig:voyager2-trajectory
:width: 500px
:align: center

Trajectory of NASA's Voyager 2 spacecraft during its grand tour of the outer solar system, with the spacecraft itself shown schematically as the small grey silhouette near the Uranus-Neptune segment of the trajectory. Gravity assists at Jupiter (1979), Saturn (1981), Uranus (1986), and Neptune (1989) successively redirected the spacecraft to each subsequent target, a trajectory made possible by a rare alignment of the outer planets that occurs roughly once every 175 years. Voyager 1, launched two weeks earlier on a faster trajectory, flew only by Jupiter (1979) and Saturn (1980) before being deflected northward out of the ecliptic. Both spacecraft are now in interstellar space: Voyager 1 crossed the heliopause in 2012, Voyager 2 in 2018. Credit: NASA/JPL, public domain.
```

### The exoplanet revolution

In 1992, Aleksander Wolszczan and Dale Frail announced the discovery of planets orbiting a pulsar, the first confirmed exoplanets {cite:p}`Wolszczan1992`. Three years later, Michel Mayor and Didier Queloz detected 51 Pegasi b, the first planet orbiting a Sun-like star: a "hot Jupiter" with a 4.2-day orbit that challenged all existing formation theories {cite:p}`MayorQueloz1995`. The French-led CoRoT space mission then announced the first transiting rocky exoplanet, CoRoT-7b, in 2009, a super-Earth with a measured radius of $1.58\,\Rearth$ and a 0.85-day orbit {cite:p}`Leger2009`. NASA's Kepler mission {cite:p}`Borucki2010` operated from 2009 to 2018 and discovered thousands of transiting exoplanets, while the ongoing TESS mission (launched 2018) surveys the brightest nearby stars. JWST, launched in December 2021, is now characterising exoplanet atmospheres through transmission and emission spectroscopy ({ref}`Lecture 13 <lecture13>`).
The cumulative tally of confirmed detections is shown in {numref}`fig:exoplanet-cumulative`.

```{figure} figures/exoplanet_cumulative.avif
:name: fig:exoplanet-cumulative
:width: 700px
:align: center

Cumulative number of confirmed exoplanets per discovery year, colour-coded by detection method. The first detection (1992, pulsar timing) was followed by the radial-velocity revolution of the late 1990s and 2000s, and then the explosion of transit discoveries during and after NASA's Kepler mission (2009 to 2018). The visible step-jumps in 2014 and 2016 are the Kepler team's statistical-validation batch releases, in which hundreds (2014) and over a thousand (2016) Kepler candidates were promoted to confirmed planets simultaneously rather than one-by-one. Credit: NASA Exoplanet Archive (Caltech), accessed 2026-05-08 {cite:p}`NASAExoplanetArchive2026`.
```

The same set of detections plotted in mass-period space ({numref}`fig:exoplanet-mass-period`) reveals strong selection biases: large short-period planets dominate the upper-left of the diagram, while Earth analogues in the lower-right remain sparsely populated.

```{figure} figures/exoplanet_mass_period.avif
:name: fig:exoplanet-mass-period
:width: 700px
:align: center

Planet mass (or $M\sin i$) versus orbital period for all confirmed exoplanets, colour-coded by detection method, with the eight solar-system planets shown as gold stars for reference. Selection effects favour large, short-period planets in the upper-left of the diagram. The Earth-analogue regime, near mass $\sim 1\,\Mearth$ and orbital period $\sim 1$ year, sits in the lower-middle of the plot and remains sparsely populated because radial-velocity and transit surveys with multi-year baselines have only recently begun to access it; future direct-imaging missions (in particular the Habitable Worlds Observatory and the LIFE interferometer concept) are explicitly designed to fill this region by spatially separating reflected or thermal planet light from the host star. Credit: NASA Exoplanet Archive (Caltech), accessed 2026-05-17 {cite:p}`NASAExoplanetArchive2026`.
```

Within the small-planet regime, the Kepler sample reveals a bimodal radius distribution ({numref}`fig:radius-gap`) with peaks near $1.3\,\Rearth$ and $2.4\,\Rearth$ separated by a "radius valley", interpreted as the boundary between rocky planets and those retaining a thin H/He envelope.

```{figure} figures/radius_gap_fulton.avif
:name: fig:radius-gap
:width: 600px
:align: center

Completeness-corrected histogram of planet radii from the California-Kepler Survey, restricted to planets with orbital periods $< 100$ d around FGK host stars. The bimodal distribution shows two peaks near $1.3\,\Rearth$ (super-Earths) and $2.4\,\Rearth$ (sub-Neptunes) separated by a "radius valley" near $1.8\,\Rearth$, interpreted as the boundary between rocky planets and those that retain a thin H/He envelope. Error bars are 1-$\sigma$ from Poisson statistics on the binned detection counts; the light-grey segment below $1.14\,\Rearth$ marks the radius range where the Kepler survey suffers from low completeness and the inferred occurrence is unreliable. The "typical uncert." marker in the upper right is the median radius measurement uncertainty for an individual planet. The radius valley and its implications for atmospheric escape are revisited in {ref}`Lecture 13 <lecture13>`. Reproduced from {cite:t}`Fulton2017`, Fig. 7 (top panel).
```

Beyond the demographics, ALMA imaging of the young star HL Tauri ({numref}`fig:hl-tau-alma`) provides direct visual evidence of planet formation in progress: concentric gaps in the protoplanetary disk are widely interpreted as carved by forming protoplanets.

```{figure} figures/hl_tau_alma.avif
:name: fig:hl-tau-alma
:width: 450px
:align: center

ALMA 1.3 mm continuum image of the protoplanetary disk around the young star HL Tauri (distance $\sim 140$ pc). The concentric dark gaps are widely interpreted as carved by forming protoplanets, although alternative explanations involving local pile-ups of dust grains at ice lines and other disk substructures remain on the table. ALMA's $\sim 5$ AU angular resolution at HL Tau's distance is what made this multi-ringed substructure visible for the first time. Protoplanetary disks and planet formation are covered in {ref}`Lecture 2 <lecture02>`. Credit: ALMA (ESO/NAOJ/NRAO); {cite:t}`ALMAPartnership2015`.
```

The most recent step in exoplanet science has been the direct chemical characterisation of atmospheres. JWST measures the absorption spectrum of starlight that filters through a transiting planet's atmosphere and identifies individual molecules in it. In August 2022, JWST recorded the first unambiguous detection of carbon dioxide in an exoplanet atmosphere on the hot gas giant WASP-39 b ({numref}`fig:wasp39b-spectrum`) {cite:p}`Rustamkulov2023`. The 4.3 $\mu$m $\mathrm{CO_2}$ absorption feature is unmistakable; it was the prototype result for the wider JWST exoplanet-atmosphere programme that is now examining dozens of planets and is the principal subject of {ref}`Lecture 13 <lecture13>`.

```{figure} figures/wasp39b_jwst_co2.avif
:name: fig:wasp39b-spectrum
:width: 600px
:align: center

NASA outreach graphic of the first unambiguous detection of carbon dioxide in an exoplanet atmosphere, from JWST/NIRSpec observations of the hot gas giant WASP-39 b in July 2022. The "amount of light blocked" (transit depth) is plotted as a function of wavelength from 3.0 to 5.5 $\mu$m. The prominent peak near 4.3 $\mu$m is the $\mathrm{CO_2}$ absorption band. White points are data with uncertainty bars; the blue curve is the best-fit atmospheric model {cite:p}`Rustamkulov2023`. Image credit: NASA, ESA, CSA, Joseph Olmsted (STScI).
```

Today, planetary science integrates astronomy, physics, chemistry, geology, and atmospheric science. It spans scales from dust grains in protoplanetary disks to the demographics of planetary systems across the Galaxy.

## Overview of the solar system

### Architecture and scale

The solar system extends from the Sun (radius $\Rsun = 6.96 \times 10^8$ m) to the Oort Cloud, a hypothetical reservoir of comets at roughly $10^4$–$10^5$ AU. Its principal components, from the inside out, are:

- **The inner solar system:** Four rocky (terrestrial) planets (Mercury, Venus, Earth, Mars) with semi-major axes between 0.39 and 1.52 AU. These are small, dense, and composed primarily of rock and metal.
- **The asteroid belt:** A population of rocky and metallic bodies between roughly 2.1 and 3.3 AU, dominated by the dwarf planet Ceres (diameter ~940 km). The total mass of the asteroid belt is only ~$4 \times 10^{-4}$ $\Mearth$.
- **The outer solar system:** Four giant planets, Jupiter and Saturn (gas giants) and Uranus and Neptune (ice giants), between 5.2 and 30.1 AU. These are massive, with thick hydrogen–helium envelopes and extensive moon systems.
- **The Kuiper Belt:** A disk of icy bodies beyond Neptune (~30–50 AU), including the dwarf planets Pluto, Eris, and Makemake. The scattered disk extends to greater distances with more eccentric orbits.
- **The Oort Cloud:** A spherical shell of icy bodies at $10^4$–$10^5$ AU, believed to be the source of long-period comets. Its existence is inferred from cometary orbits but has not been directly observed.

The principal solar-system bodies span more than two orders of magnitude in size, from Jupiter (diameter $\sim 143{,}000$ km, roughly $29\times$ that of Mercury) down to the largest Kuiper Belt and scattered-disk objects (diameters $\sim 2{,}000$ to $2{,}400$ km). {numref}`fig:solar-system-composite` brings the four populations introduced above together at true relative size.

```{figure} figures/solar_system_composite.avif
:name: fig:solar-system-composite
:width: 100%
:align: center

Composite at true relative size of the principal bodies of the solar system, mapping onto the four populations introduced in the text. **Inner solar system:** Mercury, Venus, Earth (with the Moon), and Mars (with Phobos and Deimos). **Asteroid belt:** represented by the dwarf planet Ceres. **Outer solar system:** Jupiter, Saturn, Uranus, and Neptune, each shown with their largest moons (Io, Europa, Ganymede, Callisto for Jupiter; Mimas, Enceladus, Tethys, Dione, Rhea, Titan for Saturn; Miranda, Ariel, Umbriel, Titania, Oberon for Uranus; Triton for Neptune). **Kuiper Belt, scattered disk, and detached objects:** Pluto (with Charon), Haumea (with Namaka and Hi'iaka), Makemake, Quaoar (with Weywot), Orcus (with Vanth), Eris (with Dysnomia), Gonggong (with Xiangliu), and Sedna. The Sun's limb is shown at right for scale. Body sizes are to scale relative to each other; **distances between bodies are not to scale**. The Oort Cloud is not depicted since its constituent comet nuclei are individually too small to image. Composite by CactiStaccingCrane (Wikimedia Commons, CC BY-SA 4.0); source imagery: NASA, ESA, ISRO.
```

### Planetary properties

The table below summarises the key physical and orbital properties of the eight planets. Note the enormous dynamic range: Jupiter is over 5,700 times more massive than Mercury, yet both orbit the same star.

**Key properties of the eight solar system planets.** Data from {cite:p}`NASAFactSheet`.

| Planet | Mass ($\Mearth$) | Radius ($\Rearth$) | $a$ (AU) | $P$ (yr) | $e$ | $\rho$ (kg m$^{-3}$) |
|--------|------:|--------:|------:|------:|------:|------:|
| Mercury | 0.055 | 0.383 | 0.387 | 0.241 | 0.206 | 5427 |
| Venus | 0.815 | 0.949 | 0.723 | 0.615 | 0.007 | 5243 |
| Earth | 1.000 | 1.000 | 1.000 | 1.000 | 0.017 | 5514 |
| Mars | 0.107 | 0.532 | 1.524 | 1.881 | 0.093 | 3934 |
| Jupiter | 317.8 | 11.21 | 5.203 | 11.86 | 0.049 | 1326 |
| Saturn | 95.16 | 9.45 | 9.537 | 29.46 | 0.054 | 687 |
| Uranus | 14.54 | 4.01 | 19.19 | 84.01 | 0.047 | 1271 |
| Neptune | 17.15 | 3.88 | 30.07 | 164.8 | 0.009 | 1638 |

Two patterns stand out immediately. First, **density decreases with distance** ({numref}`fig:density-vs-distance`): the inner planets have $\rho > 3900$ kg m$^{-3}$ (rock and metal), while the outer planets have $\rho < 1700$ kg m$^{-3}$ (gas and ice). Saturn is famously less dense than water. The **canonical** interpretation is that this gradient reflects the temperature structure of the protoplanetary disk: rock condenses everywhere, ices only beyond the snow line at $\sim 3$ to $5$ AU, and hydrogen and helium are accreted as gas by the cores that form quickly enough to capture it before the disk dispersed. This picture is the starting point developed in {ref}`Lecture 2 <lecture02>`; we will see there that modern formation models continue to refine, and in some places challenge, several parts of it. Second, **mass is concentrated in Jupiter** ({numref}`fig:mass-vs-distance`): it contains more than twice the mass of all other planets combined. We will quantify this in the blackboard derivation below.

```{figure} figures/density_vs_distance.avif
:name: fig:density-vs-distance
:width: 600px
:align: center

Bulk density of the eight solar-system planets versus orbital semi-major axis (log $x$). The terrestrial planets (red) cluster at $\rho > 3900$ kg m$^{-3}$; the giant planets (blue) sit below 1700 kg m$^{-3}$, with Saturn the lowest at 687 kg m$^{-3}$, below the density of liquid water (grey dashed line). The brown dashed line marks the **uncompressed density of typical silicate mantle rock** ($\sim 3300$ kg m$^{-3}$, the 1-bar density of olivine and peridotite): Mars sits close to this value, while Earth, Venus, and Mercury exceed it because (a) iron-rich cores raise the bulk density and (b) self-gravity compresses their interiors. The formation context of this density gradient is developed in {ref}`Lecture 2 <lecture02>`. Data from {cite:p}`NASAFactSheet`.
```

```{figure} figures/mass_vs_distance.avif
:name: fig:mass-vs-distance
:width: 600px
:align: center

Planetary mass versus orbital semi-major axis on a log-log scale, on the same x-axis as {numref}`fig:density-vs-distance`. The grey dashed line marks the **sum of all planetary masses except Jupiter** ($\approx 129\,\Mearth$); Jupiter alone, at $317.83\,\Mearth$, exceeds this sum by a factor of $\approx 2.5$ and sits well above the line. Jupiter and Saturn together account for more than $90\%$ of the total planetary mass in the solar system. The formation context of this mass concentration is developed in {ref}`Lecture 2 <lecture02>`. Data from {cite:p}`NASAFactSheet`.
```

### Classification

Planets are broadly classified by composition and structure:

- **Terrestrial planets** (Mercury, Venus, Earth, Mars): Rocky surfaces, iron cores, thin or no atmospheres (Venus being the exception with its massive CO$_2$ atmosphere). Covered in {ref}`Lecture 9 <lecture09>` and {ref}`Lecture 10 <lecture10>`.
- **Gas giants** (Jupiter, Saturn): Massive hydrogen–helium envelopes with no well-defined solid surface, likely rocky/icy cores at high pressure. Covered in {ref}`Lecture 11 <lecture11>`.
- **Ice giants** (Uranus, Neptune): Smaller than gas giants, with interiors dominated by heavier volatiles (H$_2$O, NH$_3$, CH$_4$) under extreme pressures, topped by hydrogen–helium atmospheres. Also covered in {ref}`Lecture 11 <lecture11>`.

## Blackboard derivation: Solar mass from planetary orbits

```{admonition} Blackboard derivation: Solar mass from Kepler's third law
:class: tip

**Goal:** Use Kepler's third law to estimate the mass of the Sun from Earth's orbital parameters, then evaluate the planet-to-star mass ratio for the solar system.

**Setup.**

Consider a planet of mass $M_p$ in a circular orbit of radius $r$ around a star of mass $M_*$. The gravitational force provides the centripetal acceleration:

$$
\frac{G M_* M_p}{r^2} = \frac{M_p v^2}{r}
$$

where $v = 2\pi r / P$ is the orbital velocity and $P$ is the orbital period.

**Derivation.**

Substituting $v = 2\pi r / P$ and cancelling $M_p$:

$$
\frac{G M_*}{r^2} = \frac{4\pi^2 r}{P^2}
$$

Solving for the stellar mass:

$$
\boxed{M_* = \frac{4\pi^2 r^3}{G P^2}}
$$ (eq:kepler-mass)

This is Newton's form of Kepler's third law (for $M_p \ll M_*$). The planet's mass cancels: the orbital period depends only on the central mass and the orbital radius.

**Note:** For elliptical orbits, the same relation holds with $r$ replaced by the semi-major axis $a$. The derivation of the general case requires the vis-viva equation, which we will cover in {ref}`Lecture 2 <lecture02>`.

**Application.**

Using Earth's orbital parameters:

| Quantity | Value |
|----------|-------|
| Semi-major axis $a_\oplus$ | $1.496 \times 10^{11}$ m |
| Orbital period $P_\oplus$ | $3.156 \times 10^7$ s |
| Gravitational constant $G$ | $6.674 \times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ |

$$
\Msun = \frac{4\pi^2 \times (1.496 \times 10^{11})^3}{6.674 \times 10^{-11} \times (3.156 \times 10^7)^2} \approx 1.99 \times 10^{30} \text{ kg}
$$

This agrees with the accepted value $\Msun = 1.989 \times 10^{30}$ kg, a remarkably accurate estimate from just two measurable quantities.

**The planet-to-star mass ratio.**

The more precise form of Kepler's third law is $P^2 = 4\pi^2 a^3 / [G(M_* + M_p)]$, which gives $M_* + M_p$ rather than $M_*$ alone. The approximation $M_* + M_p \approx M_*$ is justified because the planet-to-star mass ratio is tiny:

- Jupiter, the most massive planet: $\Mjup \approx 318 \, \Mearth \approx 1.90 \times 10^{27}$ kg, giving $\Mjup / \Msun \approx 9.5 \times 10^{-4}$.
- Total mass of all eight planets: $\approx 446 \, \Mearth \approx 2.7 \times 10^{27}$ kg, giving $M_\mathrm{planets}/\Msun \approx 1.3 \times 10^{-3}$.

The Sun contains **99.87%** of the solar system's total mass. Jupiter alone accounts for 71% of the planetary mass ({numref}`fig:ss-mass-budget`). This extreme concentration of mass in the central star is a fundamental property of planetary systems, and one that planet formation theory must explain ({ref}`Lecture 2 <lecture02>`).
```

```{figure} figures/ss_mass_budget.avif
:name: fig:ss-mass-budget
:width: 700px
:align: center

Mass budget of the solar system. *Left:* the Sun contains 99.87% of the total mass; the eight planets together contribute the remaining 0.13%. *Right:* among the planets, Jupiter accounts for $\sim 71\%$ and Saturn $\sim 21\%$; the ice giants Neptune ($3.8\%$) and Uranus ($3.3\%$) make up most of the rest; the four terrestrial planets (Mercury, Venus, Earth, Mars) together contribute only $0.44\%$ of the planetary mass and are grouped into a single wedge for legibility. Data from {cite:p}`NASAFactSheet`.
```


## Comparative planetology as a methodology

Understanding a single planet in isolation is difficult: we cannot perform controlled experiments on entire worlds. **Comparative planetology** addresses this by treating the planets as a natural set of experiments: similar objects subjected to different conditions.

Consider the terrestrial planets ({numref}`fig:terrestrial-planets`). Venus, Earth, and Mars have broadly similar compositions and formed in the same protoplanetary disk, yet their surfaces and atmospheres are radically different:

```{figure} figures/terrestrial_planets.avif
:name: fig:terrestrial-planets
:width: 600px
:align: center

The four terrestrial planets at approximate relative scale. From left to right: Mercury, Venus, Earth, and Mars. Despite forming in the same protoplanetary disk, these worlds span a factor of about 18 in mass and have followed dramatically different evolutionary paths. Earth and Venus are studied in detail in {ref}`Lecture 9 <lecture09>`; Mercury and Mars in {ref}`Lecture 10 <lecture10>`. Credit: NASA/JPL, public domain.
```

| Property | Venus | Earth | Mars |
|----------|-------|-------|------|
| Surface temperature | 464 °C | 15 °C | $-60$ °C |
| Surface pressure | 92 bar | 1 bar | 0.006 bar |
| Dominant atmosphere | CO$_2$ (96.5%) | N$_2$/O$_2$ (99%) | CO$_2$ (95%) |
| Magnetic field | None | Strong dipole | Remnant crustal |
| Tectonics | Episodic resurfacing | Plate tectonics | Stagnant lid |

The atmospheric divergence is striking: {numref}`fig:vem-atmospheres` shows that the three planets span four orders of magnitude in surface pressure and several hundred kelvin in surface temperature.

```{figure} figures/venus_earth_mars_atmospheres.avif
:name: fig:vem-atmospheres
:width: 700px
:align: center

Surface temperature (red bars, left axis) and surface pressure (blue bars, right axis, log scale) for Venus, Earth, and Mars, with the dominant atmospheric species labelled below. Despite similar bulk compositions and shared formation environment, the three terrestrial planets span a factor of $\sim 10^4$ in surface pressure and $\sim 500$ K in surface temperature. Data from {cite:p}`NASAFactSheet`.
```

By comparing these three cases, we can isolate which differences arise from distance to the Sun, planetary mass, internal activity, or historical contingency. The same logic applies to moons: comparing Io, Europa, Ganymede, and Callisto ({numref}`fig:galilean-moons`), all orbiting Jupiter but differing in composition and tidal heating, reveals how a single variable can drive vastly different geological outcomes.

```{figure} figures/galilean_moons.avif
:name: fig:galilean-moons
:width: 700px
:align: center

The four Galilean moons of Jupiter at correct relative size. Left to right: Io (volcanically active), Europa (icy crust over a global liquid-water ocean), Ganymede (largest moon in the solar system at 5268 km in diameter, larger than Mercury at 4880 km; intrinsic magnetic field), Callisto (heavily cratered, geologically inert). Despite a common formation environment, tidal heating and ice content drive vastly different geological outcomes; the giant-planet moon systems are revisited in {ref}`Lecture 11 <lecture11>`. Credit: NASA/JPL/DLR, Galileo mission.
```

This comparative approach now extends to thousands of exoplanets, where we can study how planetary properties vary as a function of stellar type, orbital distance, and system architecture ({ref}`Lecture 13 <lecture13>`). It is one of the most powerful tools in modern planetary science, and we will apply it throughout this course.

## Observational techniques

Planetary science draws on a wide range of observational methods, from ground-based telescopes to robotic landers.

### Telescopes

Ground-based telescopes observe planets across the electromagnetic spectrum. Optical imaging resolves surface and atmospheric features, infrared spectroscopy probes thermal emission and atmospheric composition, and radio observations measure subsurface properties and atmospheric dynamics. Adaptive optics on large telescopes (e.g., VLT, Keck) achieve angular resolutions approaching those of space telescopes.

Space-based observatories avoid atmospheric absorption and distortion. The Hubble Space Telescope has monitored atmospheric changes on the giant planets for decades. JWST, operating at infrared wavelengths from the Sun–Earth L2 point, is now the primary tool for exoplanet atmospheric characterisation.

### Spacecraft exploration

Spacecraft provide the most detailed planetary data. Mission types include, in order of increasing complexity and cost:

- **Flyby:** The spacecraft passes a target once, collecting data during a brief encounter. Example: Voyager 2 at Neptune (1989).
- **Orbiter:** The spacecraft enters orbit, enabling long-term monitoring. Example: Cassini at Saturn (2004–2017).
- **Lander:** The spacecraft lands on the surface and measures conditions in situ. Example: Viking 1 on Mars (1976).
- **Rover:** A mobile lander that traverses the surface. Example: Perseverance on Mars (2021–present).
- **Sample return:** Material is collected and returned to Earth for laboratory analysis. Example: Hayabusa2 returned samples from asteroid Ryugu (2020).

### Remote sensing methods

Key remote sensing techniques used across these platforms include:

- **Spectroscopy:** Identifies materials by their characteristic absorption and emission features. Reveals atmospheric composition, surface mineralogy, and thermal properties.
- **Radar:** Penetrates clouds and maps surface topography (e.g., Magellan at Venus) and detects subsurface features (e.g., MARSIS on Mars).
- **Gravimetry:** Maps the gravity field from spacecraft orbital perturbations, revealing interior density variations and subsurface mass concentrations.
- **Magnetometry:** Measures magnetic fields, constraining dynamo activity and interior conductivity.

## Key spacecraft missions

The table below lists landmark missions that have shaped our understanding of the solar system.

**Selected landmark planetary missions.**

| Mission | Agency | Year(s) | Target | Key achievement |
|---------|--------|---------|--------|-----------------|
| Mariner 2 | NASA | 1962 | Venus | First successful planetary flyby |
| Mariner 4 | NASA | 1965 | Mars | First close-up images of another planet |
| Apollo 11 | NASA | 1969 | Moon | First crewed landing on another world |
| Venera 7 | USSR | 1970 | Venus | First successful landing on another planet |
| Viking 1 & 2 | NASA | 1976 | Mars | First Mars landers; life-detection experiments |
| Voyager 1 & 2 | NASA | 1977–1989 | Outer planets | Grand tour of Jupiter, Saturn, Uranus, Neptune |
| Galileo | NASA | 1995–2003 | Jupiter | First Jupiter orbiter; Europa's subsurface ocean |
| Cassini-Huygens | NASA/ESA | 2004–2017 | Saturn | Huygens landed on Titan; Enceladus plumes |
| Spirit & Opportunity | NASA | 2004–2018 | Mars | Long-duration rovers; evidence for past water |
| New Horizons | NASA | 2015 | Pluto | First Pluto flyby; revealed geological complexity |
| Hayabusa2 | JAXA | 2018–2020 | Ryugu | Returned samples from a carbonaceous asteroid |
| Perseverance | NASA | 2021– | Mars | Sample caching for future return; Ingenuity helicopter |
| JWST | NASA/ESA/CSA | 2021– | Exoplanets | Atmospheric characterisation of exoplanets |
| Europa Clipper | NASA | 2024– | Europa | Investigating habitability of Europa's ocean |

Two iconic mission products illustrate the breadth of these efforts: the Cassini orbiter's backlit view of Saturn from inside the planet's shadow ({numref}`fig:cassini-saturn`), and the first colour view from Perseverance on Mars ({numref}`fig:perseverance-mars`) showing the rocky plain in Jezero crater where samples for eventual return are being cached.

```{figure} figures/cassini_saturn.avif
:name: fig:cassini-saturn
:width: 600px
:align: center

Backlit view of Saturn imaged by the Cassini spacecraft on 19 July 2013, with Earth visible as a faint pale point through the rings (lower right). Cassini operated in Saturn orbit from 2004 to 2017 and discovered the global subsurface ocean of Enceladus and the hydrocarbon lakes of Titan. Credit: NASA/JPL-Caltech/Space Science Institute.
```

```{figure} figures/perseverance_mars.avif
:name: fig:perseverance-mars
:width: 600px
:align: center

First colour view of Mars from NASA's Perseverance rover, taken from one of its hazard-avoidance cameras shortly after landing in Jezero crater on 18 February 2021. The rover's shadow is visible in the foreground; the rocky plain ahead is part of an ancient lake-delta system. Perseverance is caching rock and regolith samples for eventual return to Earth via the Mars Sample Return campaign. Credit: NASA/JPL-Caltech.
```

Several missions are in flight or planned for the coming decade, including ESA's JUICE (Jupiter Icy Moons Explorer, launched 2023, Jupiter arrival 2031), the Mars Sample Return campaign, and the Dragonfly rotorcraft to Titan (launch ~2028).

## Recent advances

Planetary science is advancing rapidly, driven by new space missions and observatories. The **James Webb Space Telescope** (JWST), launched in 2021, has begun characterising the atmospheres of rocky exoplanets for the first time, including thermal emission measurements of planets in the TRAPPIST-1 system {cite:p}`Greene2023` (see also {ref}`Lecture 13 <lecture13>`). The system architecture, with seven roughly Earth-sized planets in tightly-packed orbits around a cool M-dwarf, is shown in {numref}`fig:trappist1-system`. These observations are providing the first direct constraints on whether Earth-sized planets around other stars retain atmospheres; the first such measurement, the dayside thermal emission of TRAPPIST-1 b, is shown in {numref}`fig:trappist1b-jwst`.

```{figure} figures/trappist1_system.avif
:name: fig:trappist1-system
:width: 700px
:align: center

The seven planets of the TRAPPIST-1 system (top row, b through h) compared with the inner solar system (bottom row), shown with measured or estimated orbital periods, distances, radii, masses, densities, and surface gravities. All seven TRAPPIST-1 planets are roughly Earth-sized and orbit closer to their cool M-dwarf host than Mercury does to the Sun, with three planets (e, f, g) inside the conservative habitable zone and a fourth (d) near its inner edge. Credit: NASA/JPL-Caltech.
```

```{figure} figures/trappist1b_jwst.avif
:name: fig:trappist1b-jwst
:width: 600px
:align: center

JWST MIRI F1500W secondary-eclipse measurement of TRAPPIST-1 b (data point near 15 μm) compared with model dayside spectra. The measurement is consistent with a 503 K bare-rock blackbody and excludes thick CO$_2$-dominated atmospheres (cyan) and hybrid O$_2$+CO$_2$ atmospheres (magenta) at the level shown. Credit: {cite:t}`Greene2023`.
```

Closer to home, NASA's **OSIRIS-REx** mission returned samples from the carbon-rich asteroid Bennu in September 2023, revealing hydrated minerals and organic compounds that illuminate the primordial building blocks of planets ({ref}`Lecture 12 <lecture12>`). NASA's **Europa Clipper**, launched in October 2024, is en route to Jupiter's moon Europa to investigate its subsurface ocean and assess habitability {cite:p}`HowellPappalardo2020` (see also {ref}`Lecture 14 <lecture14>`). ESA's **JUICE** mission, launched in 2023, will arrive at the Jupiter system in 2031 to study Ganymede, Europa, and Callisto.

The Mars exploration programme continues with the **Perseverance** rover caching samples in Jezero crater for eventual return to Earth {cite:p}`Farley2022`, while NASA's **Dragonfly** rotorcraft (a nuclear-powered drone that will explore Titan's surface chemistry) is planned for launch in 2028 ({ref}`Lecture 6 <lecture06>`). These missions collectively address the three driving questions of this course: how planetary systems form, what makes a planet habitable, and whether life exists beyond Earth.


## References

```{bibliography}
:filter: docname in docnames
```
