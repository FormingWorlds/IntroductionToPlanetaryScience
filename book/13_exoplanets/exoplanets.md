(lecture13)=
# Exoplanets, Detection Methods, Demographics & Characterisation

```{highlights}
**Learning objectives:** By the end of this lecture, you will be able to describe the main exoplanet detection methods and their observational biases, interpret the period-radius diagram and its key features (radius valley, hot Neptune desert, peas-in-a-pod), apply the transit and radial velocity geometry to derive planetary mass, radius, and bulk density, and evaluate JWST-era atmospheric characterisation results and their implications for habitability and biosignatures.
```

```{seealso}
**Slides:** [Download Lecture 13 (PDF)](../_static/slides/lecture13.pdf)
```

In all the lectures so far we have studied a single planetary system in extraordinary detail.
We know its age, its eight planets, its hundreds of moons, its Kuiper belt, its formation history.
We do not yet know whether any of this is typical.
Lecture 13 finally turns the question outward.
We ask how planets are detected around other stars, what the resulting catalogue looks like, how it can be physically interpreted, and where the solar system sits in that picture.
The lecture follows the same descriptive-first, payoff-at-the-end structure as Lectures 9 to 12: detection methods first (Part 1), then demographics and architectures (Part 2), then atmospheric characterisation, habitability, and the comparative payoff (Part 3).

## Part 1: How we find exoplanets

### Historical context

The first confirmed planets outside the solar system were announced in 1992 by Aleksander Wolszczan and Dale Frail around the radio pulsar PSR B1257+12 {cite:p}`Wolszczan1992`.
The system contains two planets with minimum masses of about $3.4$ and $2.8\,\Mearth$ in $66$ and $98$ day orbits, plus a lunar-mass third body ($\sim 0.015\,\Mearth$) in a $25.34$ day orbit {cite:p}`Wolszczan1994`.
These post-supernova planets showed that planetary bodies can exist in environments far removed from the standard star and disk framework of {ref}`Lecture 2 <lecture02>`.

In 1995 Michel Mayor and Didier Queloz used the ELODIE spectrograph to detect 51 Pegasi b, the first confirmed planet orbiting a main-sequence star, earning the 2019 Nobel Prize in Physics {cite:p}`MayorQueloz1995`.
The planet has roughly half the mass of Jupiter on a 4.23-day orbit.
A gas giant so close to its star contradicted standard models where gas giants form beyond the ice line during **runaway accretion** (the rapid intake of surrounding nebular gas by a growing core) {cite:p}`Pollack1996`.
This discovery motivated the **planetary migration** interpretation, which won out over in-situ formation within a few years: planets form at large orbital distances and move inward through disk interactions ({ref}`Lecture 2 <lecture02>`).

```{figure} figures/hd209458b_first_transit.avif
:align: center
:name: fig:hd209458b
:width: 70%

The first ground-based detection of a transiting exoplanet, **HD 209458 b**, observed with the STARE photometer over two nights in September 1999. Each successive transit dropped the relative flux of the host star by approximately 1.7 per cent, exactly the depth predicted from the radial velocity mass and an inferred Jupiter-like radius. From {cite:t}`Charbonneau2000`; an independent simultaneous detection was reported by {cite:t}`Henry2000`. After this point exoplanets were no longer abstract Doppler signals: they were physical objects whose sizes could be measured directly.
```

In 1999 the first transit detection of HD 209458 b combined transit depth and radial velocity to determine the first planetary **bulk density** (total mass divided by volume) ({numref}`fig:hd209458b`).
This confirmed that **hot Jupiters** (Jupiter-mass planets on orbits of only a few days) are gas-dominated bodies rather than high-density objects.
By 2026 the NASA Exoplanet Archive recorded more than 6000 confirmed exoplanets in more than 4500 planetary systems {cite:p}`NASAExoArchive2025`.

### Radial velocity method

A planet of mass $m_p$ and host star of mass $M_\star$ orbit their common **barycentre** with stellar orbit radius $a_\star = (m_p / M_\star)\,a_p$, spanning about one solar radius for a Jupiter analogue and less than a thousandth of a solar radius for an Earth analogue.
This stellar reflex motion causes periodic Doppler shifts in stellar absorption lines, yielding the orbital period $P$, eccentricity $e$, and semi-amplitude $K_\star$.

Derived from Kepler's third law and momentum conservation, the semi-amplitude for an orbit of eccentricity $e$ and inclination $i$ is

$$
K_\star = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}} \frac{1}{\sqrt{1 - e^2}},
$$

Around the Sun, a Jupiter analogue produces $K_\star \approx 12.5$ m/s, Saturn at $9.5$ AU produces $2.7$ m/s, and Earth at 1 AU produces $0.09$ m/s.

Instrumental precision has improved by two orders of magnitude over three decades, from 10 m/s with ELODIE to 1 m/s with HARPS {cite:p}`Mayor2003` and 10 cm/s with ESPRESSO {cite:p}`Pepe2021`.
Precision is now limited by **stellar noise**, velocity jitter at the 10 cm/s to 1 m/s level from granulation, oscillations, and starspots, requiring activity diagnostics or long baselines to mitigate.

Because radial velocities constrain only $m_p \sin i$, a face-on system ($i = 0$, $\sin i = 0$) produces no Doppler signal while an edge-on system ($i = 90^\circ$, $\sin i = 1$) yields the true mass.
This **$m \sin i$ degeneracy** prevents distinguishing a low-mass edge-on planet from a more massive inclined planet until inclination is measured independently from transits (where $\sin i \approx 1$), astrometry, or direct imaging.

Radial velocity surveys are biased toward massive planets on short orbits around bright, quiet stars, requiring at least a decade of baseline for long-period Jupiter analogues.
Because optical **M dwarfs** have complex molecular spectra and rapidly rotating F dwarfs lack sharp lines, surveys achieve their strongest yields around quiet G and K stars in the 5 to 10 parsec neighbourhood.

### Transit method

A **transit** occurs when an exoplanet passes in front of its host star, blocking a fraction of stellar light ({numref}`fig:transitgeom`).
The fractional flux drop for a planet of radius $R_p$ crossing a star of radius $R_\star$ is:

$$
\delta = \frac{\Delta F}{F} = \left(\frac{R_p}{R_\star}\right)^2.
$$

```{figure} figures/transit_geometry.avif
:align: center
:name: fig:transitgeom
:width: 90%

Geometry of a transit. **Left:** the orbit, viewed from above, defines a "shadow band" within which an observer sees transits. The half-angle of the band is $\Theta \approx (R_\star + R_p)/r$, where $r$ is the instantaneous star-planet distance. **Right:** detail of grazing and full transits relative to the stellar limb. The probability that a randomly oriented orbit produces a visible transit scales as $R_\star / a$. From the Winn (2010) review {cite:p}`Winn2010`.
```

For a Jupiter-radius planet around a Sun-like star, the transit depth is $\delta \approx 1\%$, measurable from the ground.
For an Earth-Sun analogue, $\delta \approx 8.4 \times 10^{-5}$ (84 parts per million), achievable only from space.
Around an M dwarf ($R_\star \approx 0.15\,\Rsun$), an Earth-radius planet yields $\delta \approx 4 \times 10^{-3}$ (4000 ppm), favouring M-dwarf systems for characterisation.

Four contact times ($t_\mathrm{I}$ through $t_\mathrm{IV}$) in the light curve ({numref}`fig:transitlc`) constrain the orbital inclination $i$, impact parameter $b$, and planetary radius.
The transit is also shaped by **limb darkening**, where the stellar limb appears dimmer because lines of sight probe cooler upper photospheric layers.

```{figure} figures/transit_lightcurve_schematic.avif
:align: center
:name: fig:transitlc
:width: 75%

Schematic of a transit light curve. The four contact times $t_\mathrm{I}$ through $t_\mathrm{IV}$ define the ingress, total duration, and egress. The depth $\delta = (R_p / R_\star)^2$ gives the planet's radius if the stellar radius is known; the duration and ingress shape constrain the impact parameter $b$ and the orbital geometry. The flat bottom assumes a uniform source; in practice the curved bottom of a real transit reveals limb darkening of the host star. From {cite:t}`Winn2010`.
```

An orbit transits only if aligned within an angle $\Theta \approx R_\star / a$ of our line of sight.
This probability is $\sim 0.005$ (one in 200) for an Earth-Sun analogue and $\sim 0.1$ (ten per cent) for a hot Jupiter at 0.05 AU, biasing detections toward short periods.
Space photometry reaches parts-per-million precision.

Kepler monitored 150,000 stars to deliver the first statistical sample of small exoplanets {cite:p}`Borucki2010`.
TESS surveys bright nearby stars for atmospheric follow-up, while CHEOPS refines planet radii.
PLATO is designed to detect Earth-sized planets in the **habitable zones**, the orbital distances at which a rocky planet could plausibly sustain liquid surface water, of bright Sun-like stars {cite:p}`Rauer2014`.

## Blackboard derivation: Transit depth, radial velocity, and bulk density

````{admonition} Blackboard derivation: Transit depth, radial velocity, and bulk density
:class: tip

This derivation is the central conceptual payoff of the lecture.
Both the transit method and the radial velocity method have an obvious individual limitation: a transit alone gives a radius but not a mass, and a radial velocity alone gives only a minimum mass.
Combining the two breaks the degeneracy, gives both quantities for the same planet, and turns an exoplanet detection into a physical object whose internal composition can be discussed.
We work through this in three steps.

**Step 1: transit depth (~2 min).**
Treat the star as a uniformly bright disk of radius $R_\star$ and the planet as an opaque circular disk of radius $R_p$.
When the planet is fully in front of the star, the area blocked is $\pi R_p^2$ and the area of the star is $\pi R_\star^2$.
The fractional flux drop is therefore the ratio of areas:

$$
\frac{\Delta F}{F} = \frac{\pi R_p^2}{\pi R_\star^2} = \left(\frac{R_p}{R_\star}\right)^2.
$$

The depth is the directly measured observable.
If we know the stellar radius (typically from spectroscopy combined with stellar evolution models, or in the best cases from interferometric angular diameters and parallax distances), we immediately get the planet radius.
Limb darkening, ingress shape, and orbital eccentricity all introduce $\sim$10\% level corrections, but the leading-order picture is just the area ratio.

**Step 2: radial velocity semi-amplitude (~5 min).**
Now we attack the dynamical side.
The two bodies orbit their common centre of mass.
Let $a$ denote the relative (planet-to-star) semi-major axis, and let $a_\star$ and $a_p$ denote the distances of the star and planet from the barycentre, with $a = a_\star + a_p$.
Conservation of momentum at any instant requires

$$
M_\star a_\star = m_p a_p,
$$

so $a_\star = (m_p/(M_\star + m_p))\,a$ and $a_p = (M_\star/(M_\star + m_p))\,a$.
Both bodies move on circles (assuming a circular orbit) around the barycentre with the same orbital period $P$, and the orbital speed of the star is

$$
v_\star = \frac{2\pi a_\star}{P} = \frac{m_p}{M_\star + m_p} \cdot \frac{2\pi a}{P}.
$$

We do not measure $v_\star$ directly: we measure only the line-of-sight projection $v_\star \sin i$, where $i$ is the inclination of the orbit normal to our line of sight.
The maximum line-of-sight reflex velocity is therefore

$$
K_\star = v_\star \sin i = \frac{m_p \sin i}{M_\star + m_p} \cdot \frac{2\pi a}{P}.
$$

To eliminate $a$ in favour of measurable quantities we use Kepler's third law for the **relative** semi-major axis,

$$
a^3 = \frac{G(M_\star + m_p) P^2}{4\pi^2}, \qquad a = \left(\frac{G(M_\star + m_p) P^2}{4\pi^2}\right)^{1/3}.
$$

Substituting into $K_\star$ gives

$$
K_\star = \frac{m_p \sin i}{M_\star + m_p} \cdot \frac{2\pi}{P} \cdot \left(\frac{G(M_\star + m_p) P^2}{4\pi^2}\right)^{1/3} = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{(M_\star + m_p)^{2/3}}.
$$

For the case $m_p \ll M_\star$, which holds for almost all known exoplanets, we can approximate $(M_\star + m_p)^{2/3} \approx M_\star^{2/3}$.
For an eccentric orbit a factor of $1/\sqrt{1 - e^2}$ multiplies the right-hand side.
The full expression in the literature includes that eccentricity factor:

$$
K_\star = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p \sin i}{M_\star^{2/3}} \frac{1}{\sqrt{1 - e^2}}.
$$

Two things should be clear from this expression.
First, $K_\star \propto P^{-1/3}$, so short-period planets give a larger reflex than long-period planets at the same mass.
Second, $K_\star \propto m_p \sin i$, so a radial velocity measurement alone gives only the **minimum** mass $m_p \sin i$, not the true mass $m_p$.

**Step 3: combining the two observables (~3 min).**
Suppose now that the same planet **both transits and produces a measurable radial velocity signal**.
The transit immediately tells us that the orbital plane is nearly edge-on: the impact parameter is small and $\sin i \approx 1$ to better than a few per cent (a non-grazing transit requires $i$ within roughly $R_\star / a$ of $90^\circ$).
This single piece of information collapses the $m_p \sin i$ degeneracy: with $\sin i \approx 1$ the inferred $m_p \sin i$ is the true mass $m_p$.
We now have, for the same object:

- $R_p$ from the transit depth and the stellar radius.
- $m_p$ from the radial velocity semi-amplitude, the orbital period, and the stellar mass.

The bulk density follows immediately from elementary geometry:

$$
\bar{\rho}_p = \frac{m_p}{\frac{4}{3}\pi R_p^3} = \frac{3 m_p}{4\pi R_p^3}.
$$

This is the central observational quantity that turns an abstract exoplanet detection into a physically meaningful object.
A density of about $5.5$ g/cm$^3$ matches an Earth-like silicate-iron rocky composition.
A density of about $1.3$ g/cm$^3$ matches Jupiter and is consistent with a hydrogen-helium envelope around a small dense core.
A density of $0.5$ g/cm$^3$, lower than water, indicates an inflated or low-mass H/He envelope.
A density between rocky and gas, near $2$--$4$ g/cm$^3$, is typical of "sub-Neptunes" and indicates a substantial water-ice or H/He volatile component on top of a rocky core.
Without the joint transit-plus-RV measurement, we cannot tell any of these apart ({numref}`fig:ck17massradius` collects the empirical mass-radius relation across the four major compositional regimes).

```{figure} figures/chenkipping_mass_radius.avif
:align: center
:name: fig:ck17massradius
:width: 90%

Empirical mass-radius relation across the full range of solar-system bodies, exoplanets, brown dwarfs, and stars, from {cite:t}`ChenKipping2017`. The shaded regions mark four distinct compositional regimes: terran ($M \lesssim 2\,\Mearth$, scaling roughly as $R \propto M^{0.28}$), Neptunian ($2\,\Mearth \lesssim M \lesssim 0.4\,\Mjup$, $R \propto M^{0.59}$), Jovian ($0.4\,\Mjup \lesssim M \lesssim 80\,\Mjup$, $R \propto M^{-0.04}$, where electron degeneracy and self-compression flatten the relation), and stellar ($M > 80\,\Mjup$, hydrogen burning sets in). Each break corresponds to a different dominant pressure source. The "Neptunian" segment is the modern compositional location of the sub-Neptune family, the population that has no analogue in the solar system.
```

The pedagogical message is this.
The transit-plus-RV combination is the **single piece of observational machinery** that took exoplanet science from an exotic claim about a few hot Jupiters in 1995 to a quantitative compositional census of thousands of planets by 2020.
Every demographic structure we will discuss in Part 2, including the radius valley and the sub-Neptune family, exists as a discovery only because we can measure both $R_p$ and $m_p$ for the same object.
````

## Part 1, continued: imaging, astrometry and timing

### Direct imaging

**Direct imaging** spatially separates planetary photons from stellar light on a detector.
Contrast reaches $10^{-9}$ for a Jupiter at 5 AU and $10^{-10}$ for an Earth analogue at 10 pc, at angular separations of $0.1$ arcsecond.

**Adaptive optics** correct atmospheric turbulence with deformable mirrors to achieve diffraction-limited resolution.
**Coronagraphs** suppress central starlight, while **angular differential imaging** (ADI) and **spectral differential imaging** (SDI) subtract residual stellar speckles.

```{figure} figures/hr8799_discovery.avif
:align: center
:name: fig:hr8799
:width: 80%

Discovery image of the **HR 8799** planetary system from {cite:t}`Marois2008`, showing planets b, c, and d at projected separations of $24$, $38$, and $68$ AU after angular differential imaging PSF subtraction. The three were found in 2004 to 2008 Keck and Gemini observations; planet e, at $\sim 14$ AU, was added in 2010, and the four young giants have masses of roughly $5$--$10\,\Mjup$ and span orbital separations of $14$--$68$ AU.
```

Because young giant planets ($\lesssim 100$ Myr old) still radiate formation heat, direct imaging favours massive ($> 1\,\Mjup$), wide-orbit ($> 10$ AU) giants such as HR 8799 {cite:p}`Marois2008` ({numref}`fig:hr8799`) and $\beta$ Pictoris b {cite:p}`Lagrange2010` ({numref}`fig:betapic`).

```{figure} figures/betapic_imaging.avif
:align: center
:name: fig:betapic
:width: 80%

Direct image of $\beta$ Pictoris b from {cite:t}`Lagrange2010`, showing clear orbital motion between 2003 (left) and 2009 (right) that confirms a bound $\sim 9\pm 3\,\Mjup$ companion at $\sim 9$ AU. The host star also harbours an extensively imaged debris disk and an interior second giant planet (c) at $\sim 2.7$ AU.
```

PDS 70 contains the first planets detected directly inside a cleared protoplanetary disk gap {cite:p}`Keppler2018,Haffert2019`.
Accretion onto b and c produces shock H$\alpha$ emission confirming planet-disk interaction models {cite:p}`Haffert2019` ({ref}`Lecture 2 <lecture02>`; {numref}`fig:pds70disk`).

```{figure} figures/pds70_disk.avif
:align: center
:name: fig:pds70disk
:width: 65%

Composite scattered-light image of the PDS 70 protoplanetary disk from {cite:t}`Haffert2019`, showing the parent disk and two embedded protoplanets (b and c) inside the cleared gap. The cleared central cavity and accreting protoplanets provide direct confirmation of planet-disk interaction models in transition disks.
```

### Astrometry

**Astrometry** measures the angular reflex motion of the host star against background reference stars.
The expected angular amplitude is

$$
\alpha = \frac{m_p}{M_\star} \cdot \frac{a_p}{d},
$$

where $d$ is the distance to the system.
For a Jupiter analogue around the Sun at 10 pc, this is about half a milli-arcsecond, whereas for an Earth analogue it is $0.3$ micro-arcseconds.
Astrometric exoplanet detection therefore demands microarcsecond precision over years to decades.

Gaia, launched in 2013, performs an all-sky astrometric survey of more than a billion stars with a final precision of $\sim 10$ microarcseconds for bright stars.
This is the precision regime in which Jupiter analogues become accessible.

Early Gaia data releases provided five-parameter astrometry and orbital fits for substellar companions {cite:p}`GaiaDR3`.
Future Gaia data releases (DR4 and DR5) will deliver astrometric time series to provide a census of long-period gas giants {cite:p}`Perryman2014`.

Astrometry is complementary to radial velocity because it directly measures the inclination of the orbit, breaking the $m \sin i$ degeneracy without requiring a transit.
A planet that produces both a Gaia astrometric signal and a radial velocity signal yields a true mass, an orbit inclination, and a complete three-dimensional orbital solution.
The combination is particularly powerful for wide-orbit Jupiter analogues that fall in the blind spot of transit surveys.

### Microlensing

In **gravitational microlensing**, the gravitational field of a foreground star (the **lens**) bends light from a distant background star, briefly magnifying its brightness.
If the lens star hosts a planet, planetary gravity introduces an additional short-duration spike lasting hours to days.
The amplitude and timing of this spike determine the planet's mass and projected separation in units of the **Einstein ring radius**, set by the lens mass and distance.

Microlensing detects planets at distances of kiloparsecs and projected separations of $0.5$ to $10$ AU, mapping onto the snow-line region where giant planets form.
The Nancy Grace Roman Space Telescope, launched in August 2026, will conduct a dedicated survey of the Galactic bulge expected to discover $\sim 1400$ bound exoplanets down to lunar-mass bodies {cite:p}`Penny2019`.

### Timing methods

When a planet has a companion in the same system, gravitational interactions periodically perturb its transit times, producing **transit timing variations** (TTVs) {cite:p}`Holman2005`.
Because TTVs encode the masses of interacting planets, they yield a **dynamical mass** measurement without requiring radial velocity follow-up.
This is essential for small planets around faint stars where radial velocity observations are infeasible, such as the seven planets of the TRAPPIST-1 system.

A second timing approach is **pulsar timing**, the technique that detected the first exoplanets {cite:p}`Wolszczan1992`.

In eclipsing binaries, circumbinary planets perturb eclipse timing and can transit both stars; Kepler-16 b, found in 2011 through its transits, was the first such planet {cite:p}`Doyle2011`.

### Detection biases summary

Each detection method introduces a **detection bias**, selecting planets in different regions of parameter space.
Radial velocity is most sensitive to massive planets on short-period orbits (since $K \propto P^{-1/3}$) around bright Sun-like stars.
Transit photometry is most sensitive to short periods (less than $\sim 100$ days) and large $R_p / R_\star$ ratios.
Direct imaging detects young, self-luminous giants on wide orbits ($> 10$ AU).
Astrometry is most sensitive to wide orbits matching the mission baseline.
Microlensing detects planets at 1 to 10 AU at any host distance, but is unrepeatable.
Timing is sensitive to compact multi-planet systems or circumbinary configurations.
The distribution of confirmed exoplanets across mass and orbital period illustrates how these observational biases shape the detected population ({numref}`fig:l13-exoplanet-mass-period`).

```{figure} figures/exoplanet_mass_period.avif
:align: center
:name: fig:l13-exoplanet-mass-period
:width: 80%

Confirmed exoplanet masses (or minimum masses $m_p \sin i$) plotted against orbital period, colour-coded by detection technique, with the solar-system planets shown for comparison. Detection biases concentrate discoveries in the high-mass and short-period regimes, leaving Earth analogues in a sparsely sampled region. Credit: NASA Exoplanet Archive {cite:p}`NASAExoplanetArchive2026`. Course-original figure.
```

The observed exoplanet archive reflects these combined biases rather than the true physical distribution.
Demographic claims in Part 2 therefore require **bias correction**, reporting underlying occurrence rather than raw catalogue counts.
This correction is reliable for Kepler, but much less certain for other surveys.

## Part 2: Demographics and architectures

### The Kepler revolution and the TRAPPIST-1 laboratory

On average, at least one planet exists per main-sequence star, with small planets below 4 Earth radii being the most common {cite:p}`Petigura2018`.
**Hot Jupiters** occur around only 0.5% to 1% of Sun-like stars {cite:p}`Fressin2013`.
The habitable-zone Earth-size planet occurrence rate is estimated at $\eta_\oplus \sim 0.4$ ({numref}`fig:petigura` and {numref}`fig:bryson`) {cite:p}`Bryson2021`.

```{figure} figures/petigura_occurrence.avif
:align: center
:name: fig:petigura
:width: 90%

Kepler-derived planet occurrence rates as a function of orbital period and planet size, from the California-Kepler Survey {cite:p}`Petigura2018`. Small planets are far more common than giants at every period, and the typical Sun-like star hosts at least one small planet inside 1 AU despite Kepler's $\sim 4$ years of baseline.
```

```{figure} figures/bryson_etaearth.avif
:align: center
:name: fig:bryson
:width: 90%

Marginalised differential occurrence rate of small planets from {cite:t}`Bryson2021`, showing occurrence per unit radius $\dd N / \dd R$ ($\Delta R = 0.25\,\Rearth$, left) and per unit instellation flux $\dd N / \dd I$ ($\Delta I = 0.18$, right). Shaded bands mark 68\% and 95\% credible intervals, yielding central values of $\eta_\oplus \sim 0.4$ with 68\% intervals of $0.2$--$0.9$ for conservative habitable-zone Earth analogues.
```

The **TRAPPIST-1** system hosts seven transiting Earth-sized planets within 0.06 AU of an ultra-cool dwarf, three of which (e, f, g) orbit in the temperate habitable zone {cite:p}`Gillon2017`.
The planets form a chain of **mean-motion resonances**, orbital periods locked near ratios of small integers, consistent with capture during an early disk-migration phase.
All seven planets transit ({numref}`fig:trappist1transits`), a configuration with probability below $10^{-3}$ for random orientations, which indicates that compact M-dwarf systems are intrinsically flat, while transit timing variations yield dynamical masses ({numref}`fig:trappist1ttvs`).

```{figure} figures/trappist1_transits.avif
:align: center
:name: fig:trappist1transits
:width: 80%

Transit light curves of the seven **TRAPPIST-1** planets (b through h) from {cite:t}`Gillon2017`, observed with Spitzer at $4.5\,\mu$m and ground-based facilities. Successive transit depths trace planetary sizes, showing that all seven are Earth-sized to within a factor of $\sim 1.5$.
```

```{figure} figures/trappist1_ttvs.avif
:align: center
:name: fig:trappist1ttvs
:width: 80%

Transit timing variations (TTVs) of **TRAPPIST-1 e** from {cite:t}`Gillon2017`, with observed deviations (black points) and a dynamical model coupled to the other six planets (red curve). TTV amplitudes reaching tens of minutes over hundreds of days invert to yield **dynamical masses** for all seven planets without radial velocity measurements.
```

### The period-radius diagram

The **period-radius diagram** plots orbital period against planetary radius for confirmed transiting planets ({numref}`fig:fultonpr`).
Gas giants ($R_p > 10\,\Rearth$) include short-period **hot Jupiters** ($P < 10$ days).
Small planets split into **sub-Neptunes** ($R_p \approx 2$ to $4\,\Rearth$), which have no solar system analogue, and rocky **super-Earths** ($R_p \approx 1$ to $1.8\,\Rearth$).
The **terrestrial analogue** regime ($R_p \lesssim 1.5\,\Rearth$ at periods longer than $\sim 100$ days) remains largely unexplored.

```{figure} figures/fulton_period_radius.avif
:align: center
:name: fig:fultonpr
:width: 70%

Period-radius distribution of small Kepler planets after stellar parameter refinement and bias correction, from {cite:t}`Fulton2017`. The colour scale indicates detection completeness. The clear deficit of planets at $R_p \approx 1.8\,\Rearth$ across all orbital periods is the **radius valley** or **Fulton gap**, the central empirical structure that splits the small-planet population into super-Earths and sub-Neptunes.
```

### The radius valley (Fulton gap)

The **radius valley** (or **Fulton gap**) is a deficit of small exoplanets at $R_p \approx 1.5$ to $2\,\Rearth$ separating rocky super-Earths (peaking near $1.3\,\Rearth$) from volatile-rich sub-Neptunes (peaking near $2.4\,\Rearth$) ({numref}`fig:fultongap`) {cite:p}`Fulton2017`.

```{figure} figures/fulton_gap.avif
:align: center
:name: fig:fultongap
:width: 80%

The **radius valley**: histogram of planet radii in the Kepler sample after stellar parameter refinement, from {cite:t}`Fulton2017`. The deficit at $R_p \approx 1.8\,\Rearth$ splits small planets into a rocky **super-Earth** group at $\sim 1.3\,\Rearth$ and a volatile-rich **sub-Neptune** group at $\sim 2.4\,\Rearth$.
```

The valley is produced by atmospheric escape via two mechanisms: first, **photoevaporation**, where stellar XUV (ultraviolet and X-ray) radiation heats the upper envelope to drive hydrodynamic escape {cite:p}`OwenWu2013`.
In **energy-limited escape**, a fraction $\epsilon \sim 0.1$ of the absorbed XUV flux converts into the gravitational work needed to lift gas out of the potential well:

$$
\dot{M} \approx \frac{\epsilon \, \pi F_\mathrm{XUV} R_p^3}{G M_p}.
$$

The $R_p^3$ scaling indicates that low-density, low-mass planets are stripped most easily.
For a $10\,\Mearth$ sub-Neptune with $R_p \approx 2.5\,\Rearth$ at $0.1$ AU, an initial saturated flux of $F_\mathrm{XUV} \sim 300$ W m$^{-2}$ yields $\dot{M} \sim 10^{8}$ kg s$^{-1}$, removing $\sim 3 \times 10^{23}$ kg over the $\sim 100$ Myr saturated phase to strip the envelope ({numref}`fig:owenvalley`).

```{figure} figures/owen_evaporation_valley.avif
:align: center
:name: fig:owenvalley
:width: 70%

Photoevaporation theory prediction of the radius valley from {cite:t}`OwenWu2013`. Planets with envelopes survive above $\sim 2\,\Rearth$, while stripped bare rocky cores settle below $\sim 1.8\,\Rearth$ to produce the observed valley.
```

{numref}`fig:owenmassloss` shows how a young sub-Neptune loses its envelope in the photoevaporation model.

```{figure} figures/owen_xuv_massloss.avif
:align: center
:name: fig:owenmassloss
:width: 90%

Photoevaporation-driven evolution of a young sub-Neptune in the {cite:t}`OwenWu2013` model. **Top**: planetary radius as a function of time since disc clearing, for two host XUV histories (line styles) and two starting orbital separations. **Bottom**: planet mass over the same evolution. The thin vertical line marks the end of the saturated XUV phase at $\sim 100$ Myr. After this time the radius and mass plateau; planets that have lost their envelopes by then settle as bare rocky cores below the radius valley.
```

The second mechanism is **core-powered mass loss**, where heat released from the cooling interior over hundreds of Myr powers hydrodynamic escape without external XUV flux, reproducing the gap at $\sim 1.8\,\Rearth$ ({numref}`fig:ginzburg`) {cite:p}`Ginzburg2018`.

```{figure} figures/ginzburg_corepowered.avif
:align: center
:name: fig:ginzburg
:width: 80%

Core-powered mass loss model from {cite:t}`Ginzburg2018`. Envelope mass loss driven by the cooling rocky interior produces a bimodal distribution with a gap at $\sim 1.8\,\Rearth$ separating bare rocky cores from sub-Neptunes.
```

Precise **asteroseismic** stellar radii show that the radius valley shifts to smaller radii at longer orbital periods, a negative slope consistent with both photoevaporation and core-powered mass loss ({numref}`fig:vaneylen`) {cite:p}`VanEylen2018`.

```{figure} figures/vaneylen_radius_valley.avif
:align: center
:name: fig:vaneylen
:width: 90%

Slope of the **radius valley** with orbital period, from the asteroseismic Kepler subsample of {cite:t}`VanEylen2018`. The empirical valley boundary descends to smaller radii at longer periods, separating super-Earths from sub-Neptunes.
```

{numref}`fig:vaneylenmodels` overlays the model predictions for the slope of the valley on these data.

```{figure} figures/vaneylen_models.avif
:align: center
:name: fig:vaneylenmodels
:width: 70%

Model predictions for the slope of the radius valley with orbital period, overlaid on the {cite:t}`VanEylen2018` data. The black curves are different theoretical predictions; both photoevaporation and core-powered mass loss predict broadly compatible slopes, and the data alone cannot decisively prefer one over the other.
```

Because stripping removes primordial envelopes, many close-in super-Earths are remnant cores rather than primordially rocky planets, although for any single planet the two origins cannot be told apart from bulk density alone.

### The hot Neptune desert

The **hot Neptune desert** is a deficit of Neptune-mass planets ($M_p \approx 10$ to $100\,\Mearth$) at orbital periods shorter than 5 days.
While hot Jupiters and rocky planets occur at these periods, {cite:t}`Mazeh2016` showed that hot Neptunes are absent ({numref}`fig:neptunedesert`).

```{figure} figures/mazeh_neptune_desert.avif
:align: center
:name: fig:neptunedesert
:width: 90%

The **hot Neptune desert** in the period-mass and period-radius planes from {cite:t}`Mazeh2016`. The shaded triangular region is empirically depleted of Neptune-mass planets. The upper edge follows a tight power law, plausibly set by Roche-lobe overflow on inflated hot Jupiters; the lower edge is more diffuse and has been variously attributed to photoevaporation, in-situ formation, and high-eccentricity migration with tidal circularization. The desert is one of the strongest pieces of evidence for atmospheric mass loss as a major sculptor of close-in planets.
```

Photoevaporation strips envelopes from lower-mass planets below the desert, leaving bare super-Earths.
At the upper edge, inflated planets fill their **Roche lobe**, the region where gas stays gravitationally bound to the planet rather than the star, losing mass through tidal stripping.

### Planetary system architectures

Multi-planet systems observed by Kepler enable statistical studies of planetary architecture.
{cite:t}`Weiss2018` identified a **peas in a pod** architecture, in which planets within the same system share similar sizes ({numref}`fig:weisspeas`) and regular orbital period spacing ({numref}`fig:weiss_spacing`).

```{figure} figures/weiss_peas_in_pod.avif
:align: center
:name: fig:weisspeas
:width: 75%

The **peas in a pod** correlation from {cite:t}`Weiss2018`: the radius of an inner Kepler multi-planet $R_i$ versus the radius of its immediately outer neighbour $R_{i+1}$. The clear positive correlation along the diagonal means that within a system the planets tend to be the same size as each other, far more so than randomly drawn pairs of planets from the Kepler sample. The Pearson correlation coefficient is 0.65 and the null-hypothesis probability is $p < 10^{-7}$.
```

```{figure} figures/weiss_spacing.avif
:align: center
:name: fig:weiss_spacing
:width: 75%

Period-ratio correlation in Kepler multi-planet systems, from {cite:t}`Weiss2018`. Each point is a triple of consecutive transiting planets in the same system: the horizontal axis is the period ratio of the inner pair ($P_{j+1}/P_j$) and the vertical axis is the period ratio of the next pair out ($P_{j+2}/P_{j+1}$). The clustering along the diagonal (Pearson $R = 0.46$, $p < 10^{-5}$) means that within a system, neighbouring period ratios are similar, supporting the view that compact inner systems form by a smooth, local process rather than by stochastic large impacts.
```

This regularity indicates that compact inner systems form through smooth growth and disk migration rather than stochastic giant impacts.
In contrast, terrestrial planet assembly in the solar system was dominated by giant impacts ({ref}`Lecture 2 <lecture02>`), suggesting the inner solar system may be dynamically unusual.

This pattern is a statistical trend for compact systems rather than a universal rule.
Radial-velocity samples of wider systems and exceptional Kepler architectures exhibit greater diversity.

Resonant chains provide direct evidence that early disk migration locked planets into place before gas dispersal.
For example, TRAPPIST-1 contains seven Earth-sized planets in mean-motion resonances within 0.06 AU {cite:p}`Gillon2017`.

### Hot Jupiters and migration

The inner edge of the surviving population is set by the **fluid Roche limit**, the orbital separation where stellar tides tear a planet apart:

$$
d_R \approx 2.46\,R_\star \left(\frac{\rho_\star}{\rho_p}\right)^{1/3}.
$$

For a Sun-like star ($\rho_\star \approx 1.4$ g cm$^{-3}$) and a hot Jupiter ($\rho_p \approx 1$ g cm$^{-3}$), this limit gives $d_R \approx 2.7\,R_\star \approx 0.013$ AU.
The observed pile-up of hot Jupiters at $\sim 0.04$ to $0.05$ AU sits a factor of three to four outside this limit, where orbits survive over Gyr timescales without tidal disruption.

In **disk migration** (Type II), net torques in a gaseous disk drive inward migration ({ref}`Lecture 2 <lecture02>`), preserving low eccentricities and alignment with the stellar equator.

In **high-eccentricity migration**, Kozai-Lidov oscillations over $10^{6}$ to $10^{8}$ years drive perihelion near the star, where **tidal dissipation** circularises the orbit while freezing in large misalignments.

In **planet-planet scattering**, dynamical instabilities in multi-giant systems eject planets and leave misaligned survivors circularised by tides ({numref}`fig:obliquitypathways`).

```{figure} figures/obliquity_pathways.avif
:align: center
:name: fig:obliquitypathways
:width: 90%

Schematic of the three migration pathways for hot Jupiters and the **stellar obliquities** they produce, from the review of {cite:t}`Albrecht2022`. Disk migration preserves spin-orbit alignment, whereas high-eccentricity migration and planet-planet scattering produce large misalignments.
```

These pathways are distinguished observationally by the **stellar obliquity** (spin-orbit angle), measured via the **Rossiter-McLaughlin effect** ({numref}`fig:rmgeom`) as a transiting planet sequentially occults the blueshifted and redshifted stellar hemispheres.
Hot Jupiters around cool stars ($T_\mathrm{eff} < 6250$ K) are mostly well aligned, reflecting disk migration or tidal realignment in convective envelopes.
Hot Jupiters around hot stars ($T_\mathrm{eff} > 6250$ K) show wide misalignments spanning prograde to retrograde orbits {cite:p}`Albrecht2022` ({numref}`fig:obliquitydist`).

```{figure} figures/rossiter_mclaughlin.avif
:align: center
:name: fig:rmgeom
:width: 80%

Geometry of the **Rossiter-McLaughlin effect**, from the {cite:t}`Triaud2018` review chapter. As a transiting planet sequentially occults the approaching (blueshifted) and receding (redshifted) stellar hemispheres, the resulting line-profile distortion traces the sky-projected spin-orbit angle $\lambda$.
```

```{figure} figures/obliquity_distribution.avif
:align: center
:name: fig:obliquitydist
:width: 90%

Projected stellar obliquity $\lambda$ as a function of scaled orbital separation $a/R_\star$ for the hot Jupiter sample, from {cite:t}`Albrecht2022`. Tight orbits around cool stars cluster near zero obliquity from tidal realignment, whereas wider scatter around hotter hosts indicates a wide primordial obliquity distribution.
```

### Super-Earth and sub-Neptune composition

Bulk-density measurements combining transit and radial-velocity data enable a compositional census of small planets.
**Super-Earths** below the radius valley have rocky compositions with densities of $4$ to $8$ g/cm$^3$, similar to Earth and Venus.
**Sub-Neptunes** above the valley have lower densities, typically $1$ to $3$ g/cm$^3$, requiring a volatile envelope of $\mathrm{H_2}$/He or $\mathrm{H_2O}$ over a rocky core.
Bulk density alone is degenerate: multiple internal structures can match the same bulk density, as shown by comparing observed planet masses and radii against theoretical composition curves ({numref}`fig:l13-massradius-composition`).

```{figure} figures/lichtenberg2025_mass_radius.avif
:align: center
:name: fig:l13-massradius-composition
:width: 90%

Mass-radius distribution of small exoplanets compared with theoretical interior models ranging from pure iron to volatile-rich envelopes, categorized by thermal regime. Rocky super-Earths align closely with silicate-iron curves, whereas sub-Neptunes require substantial volatile envelopes or water-rich layers to explain their larger radii. Reproduced from {cite:t}`Lichtenberg2025`.
```

Sub-Neptunes with $\gtrsim 10$ to $20\%$ $\mathrm{H_2O}$ by mass are candidate water worlds.
In the proposed **hycean** scenario, a planet hosts a shallow liquid water ocean beneath a thick $\mathrm{H_2}$-rich atmosphere {cite:p}`Madhusudhan2021`.
The strong $\mathrm{H_2}$ greenhouse effect can keep the ocean liquid at equilibrium temperatures below 273 K, extending the candidate habitable region.
This interpretation is contested: observations of K2-18 b may reflect mini-Neptunes without a surface, or an $\mathrm{H_2}$ envelope over a deep **magma ocean** {cite:p}`Shorttle2024`.

### M dwarf planets

M dwarfs account for roughly 75\% of main-sequence stars and are the easiest targets for discovering small habitable-zone planets.
Because the habitable-zone semi-major axis scales as $\sqrt{L_\star}$, closer orbits around low-luminosity M dwarfs increase the geometric transit probability $R_\star / a$.
The transit depth $(R_p / R_\star)^2$ for an Earth-sized planet is also much larger than around a Sun-like star.

```{figure} figures/dressing_mdwarf_occurrence.avif
:align: center
:name: fig:dressing
:width: 75%

Cumulative occurrence rate of small planets around M dwarfs as a function of orbital period from the full Kepler sample, from {cite:t}`Dressing2015`. Each curve is a different planet-radius bin from $0.5$--$1\,\Rearth$ (black) to $3$--$4\,\Rearth$ (red). M dwarfs host on average $\sim 2$ small planets per star inside 200 days, and roughly one Earth-size planet per star in or near the habitable zone. M dwarf small-planet occurrence rates exceed those around Sun-like stars by roughly a factor of 2--3.
```

Kepler occurrence rates indicate roughly $2.5$ small planets ($R_p < 4\,\Rearth$) per M dwarf inside 200 days, with $0.16^{+0.17}_{-0.07}$ Earth-size planets in the conservative habitable zone ({numref}`fig:dressing`) {cite:p}`Dressing2015`.

The main challenge for habitability is **stellar activity**, the elevated magnetic and high-energy emission of the host star.
M dwarfs spend hundreds of Myr in an early phase with luminosities up to ten times their main-sequence values.
Habitable-zone planets sit inside their **runaway-greenhouse boundary** during this phase, causing severe water loss.
High XUV flux can strip an Earth-equivalent ocean of water, leaving an abiotic oxygen atmosphere as a false-positive **biosignature** (a chemical sign mimicking life) {cite:p}`LugerBarnes2015`.

A second challenge is **tidal locking**, the synchronization of rotation and orbit into a $1{:}1$ spin-orbit resonance.
Close-in orbits produce permanent daysides and nightsides, requiring atmospheric heat transport to prevent volatile collapse on the nightside.
Three-dimensional climate models show that substellar clouds can stabilize climates and extend the habitable zone closer to the star {cite:p}`Yang2013`.
The seven planets of TRAPPIST-1 are a primary laboratory to study these climate regimes.

## Part 3: Characterisation, habitability, and the comparative payoff

### Transmission spectroscopy during transit

During transit, atmospheric absorption along the terminator sets the **wavelength-dependent transit depth**:

$$
\delta(\lambda) = \frac{[R_p + n_H H(\lambda)]^2}{R_\star^2},
$$

where $H = \kB T / (\mu m_u g)$ is the atmospheric **scale height** (the density e-folding scale, derived in {ref}`Lecture 5 <lecture05>`).
For a hot Jupiter ($T \approx 1500$ K, $\mu \approx 2.3$, $g \approx 25$ m s$^{-2}$):

$$
H = \frac{\kB T}{\mu m_u g} = \frac{(1.38 \times 10^{-23})(1500)}{(2.3)(1.66 \times 10^{-27})(25)} \approx 2 \times 10^{5}\ \mathrm{m},
$$

With $R_p \approx 1.2\,\Rjup$, $R_\star \approx 1\,\Rsun$, and $n_H \approx 5$:

$$
\frac{\Delta\delta}{\delta} \approx \frac{2 n_H H}{R_p} \approx \frac{2 \times 5 \times 2 \times 10^{5}\ \mathrm{m}}{8.6 \times 10^{7}\ \mathrm{m}} \approx 2 \times 10^{-2},
$$

The absolute depth change $(\Delta\delta / \delta) \times \delta \approx 2 \times 10^{-4}$ (a few hundred ppm) is detectable with JWST.
Sub-Neptunes reach 10 to 100 ppm, while terrestrial planets around M dwarfs fall below 10 ppm.

High-altitude **clouds and hazes** flatten transmission spectra via continuum opacity, spanning from clear to cloudy atmospheres ({cite:t}`Sing2016`, {numref}`fig:sing`; {numref}`fig:gj1214`).

```{figure} figures/sing_hotjup_spectra.avif
:align: center
:name: fig:sing
:width: 70%

Transmission spectra of ten hot Jupiters observed with HST and Spitzer across wavelengths from $0.3$ to $5$ $\mu$m on a logarithmic scale, plotted as relative altitude $z(\lambda)/H_{\rm eq}$ with $1\sigma$ uncertainties and offset vertically, from Figure 1 of {cite:t}`Sing2016`. Spectra are ordered from top to bottom by increasing altitude difference $\Delta Z_{\rm UB-LM}$ between the blue-optical and mid-infrared, showing a continuum from clear atmospheres with Na and K resonance lines ($0.59$ and $0.77$ $\mu$m) and $\mathrm{H_2O}$ absorption ($1.4$ $\mu$m) in WASP-17 b to aerosol-dominated scattering slopes in WASP-6 b.
```

```{figure} figures/gj1214b_clouds.avif
:align: center
:name: fig:gj1214
:width: 80%

Featureless transmission spectrum of the warm sub-Neptune **GJ 1214 b** from {cite:t}`Kreidberg2014`, showing how high-altitude clouds or hazes erase atmospheric absorption features in high-precision HST data. Three cloud-free model atmospheres ($\mathrm{H_2O}$, $\mathrm{CH_4}$, $\mathrm{CO_2}$) are ruled out at high significance, demonstrating that the flat spectrum requires an optically thick cloud or haze layer at high altitude.
```

### Emission spectroscopy and phase curves

**Emission spectroscopy** observes planetary thermal radiation during **secondary eclipse**, when the planet passes behind the star.
The flux drop yields the dayside **brightness temperature**, the equivalent blackbody temperature.
A **phase curve** tracks orbital brightness, where day-night contrast reveals heat redistribution efficiency ({numref}`fig:wasp43`).

```{figure} figures/wasp43b_phase_curve.avif
:align: center
:name: fig:wasp43
:width: 90%

JWST MIRI **phase curve** of the hot Jupiter **WASP-43 b**, from {cite:t}`Bell2024`. The top panel is the spectroscopic phase curve as a function of wavelength and orbital phase. The middle panel is the band-integrated white light curve, showing one transit, two secondary eclipses, and the smooth phase modulation of the planet's thermal flux as the dayside rotates in and out of view. The bottom panels are the dayside and nightside emission spectra and best-fit blackbody models. The retrieved nightside temperature is much colder than the dayside, evidence of a strong day-night contrast despite an atmosphere thick enough to imprint clear spectral features on the dayside.
```

Combining transmission, emission, and phase curves constrains atmospheric thermal structure, composition, and circulation.

### JWST era results (2022--2025)

The James Webb Space Telescope has transformed exoplanet atmospheric characterisation since mid-2022.
Transmission spectroscopy of the hot Saturn WASP-39 b revealed $\mathrm{H_2O}$, $\mathrm{CO_2}$, Na, and CO, while the absence of $\mathrm{CH_4}$ indicates super-solar metallicity {cite:p}`Rustamkulov2023,Alderson2023` ({numref}`fig:wasp39prism`) ({numref}`fig:wasp39species`).

```{figure} figures/wasp39b_prism_spectrum.avif
:align: center
:name: fig:wasp39prism
:width: 90%

The JWST/NIRSpec PRISM transmission spectrum of **WASP-39 b**, from Figure 4 of {cite:t}`Rustamkulov2023`, plots measured transit depths in per cent with $1\sigma$ uncertainties from $0.5$ to $5.5\ \mu\mathrm{m}$ against the best-fitting PICASO 3.0 grid model with shaded species opacity contributions. The data confirm clear detections of $\mathrm{H_2O}$ ($33\sigma$, $1$--$2.2\ \mu\mathrm{m}$), $\mathrm{CO_2}$ ($28\sigma$, $4.3\ \mu\mathrm{m}$), a flat grey cloud deck ($21\sigma$), Na ($19\sigma$, $0.58\ \mu\mathrm{m}$), and CO ($7\sigma$, $4.7\ \mu\mathrm{m}$), whereas K, $\mathrm{H_2S}$, and $\mathrm{CH_4}$ model contributions are not favoured despite detector saturation between $0.8$ and $1.9\ \mu\mathrm{m}$.
```

The detection of $4$ $\mu$m absorption from $\mathrm{SO_2}$ is the first identification of a **photochemical product**, a molecule generated by stellar irradiation rather than thermochemical equilibrium, in an exoplanet atmosphere {cite:p}`Tsai2023` ({numref}`fig:wasp39so2`).
The signal is modest in each instrument ($2.7\sigma$ to $4.8\sigma$), and the case rests on two instruments seeing the same feature and on four photochemistry codes reproducing it.
Its formation requires ultraviolet photolysis of $\mathrm{H_2S}$ followed by oxidation of sulfur to SO and $\mathrm{SO_2}$.

```{figure} figures/wasp39b_so2_spectrum.avif
:align: center
:name: fig:wasp39so2
:width: 90%

Terminator-averaged theoretical transmission spectra of WASP-39 b from photochemical models comparing four codes (VULCAN, KINETICS, ARGO, ATMO) against NIRSpec PRISM, NIRSpec G395H, and optical HST and VLT/FORS2 data, from Figure 3 of {cite:t}`Tsai2023`. All four independent codes reproduce the observed $4.05\ \mu\mathrm{m}$ $\mathrm{SO_2}$ feature, confirming the role of sulfur photochemistry in atmospheric opacity, and predict stronger bands across the $5$--$15\ \mu\mathrm{m}$ MIRI range near $7.5$ and $8.7\ \mu\mathrm{m}$.
```

```{figure} figures/wasp39b_alderson_species.avif
:align: center
:name: fig:wasp39species
:width: 80%

Contribution of individual opacity sources to the JWST/NIRSpec G395H transmission spectrum of WASP-39 b, from Figure 4 of {cite:t}`Alderson2023`. Panel a is the full spectrum. Grey points with error bars are the measurement, the black curve is the best-fitting model with an injected $\mathrm{SO_2}$ volume mixing ratio of $10^{-5.6}$, and each coloured curve is that same model with one opacity source removed: cloud, $\mathrm{CH_4}$, $\mathrm{H_2O}$, $\mathrm{SO_2}$, $\mathrm{CO_2}$, or CO. The left axis is transit depth in per cent and the right axis is the same quantity in planetary scale heights; the horizontal axis is wavelength in $\mu$m. The wavelength range where a coloured curve separates from the black one is the range in which that species absorbs. Panel d is the $\mathrm{CO_2}$ band near 4.3 $\mu$m on its own: black points are the measurement and the shaded orange region is the difference that the $\mathrm{CO_2}$ opacity makes to the model. The band is detected at $28.5\sigma$, above the $21.5\sigma$ of $\mathrm{H_2O}$ and the $4.8\sigma$ of $\mathrm{SO_2}$ in the same spectrum.
```

For TRAPPIST-1 b, $15\ \mu\mathrm{m}$ thermal emission is consistent with a **bare rock dayside** in radiative equilibrium with no atmospheric heat redistribution, ruling out a thick $\mathrm{CO_2}$ atmosphere {cite:p}`Greene2023`; the same measurement for TRAPPIST-1 c {cite:p}`Zieba2023` rules out a thick Venus-like atmosphere and suggests that the innermost rocky planets of active M dwarfs are stripped ({ref}`Lecture 5 <lecture05>`) ({numref}`fig:trappist1beclipse`).

```{figure} figures/trappist1b_eclipse.avif
:align: center
:name: fig:trappist1beclipse
:width: 90%

JWST MIRI $15\ \mu\mathrm{m}$ secondary eclipse light curve of **TRAPPIST-1 b** from {cite:t}`Greene2023`, marking the first thermal emission detection of an Earth-sized exoplanet. The eclipse depth $f_p / f_\star = 861 \pm 99$ ppm corresponds to a dayside brightness temperature of $T_B = 503^{+26}_{-27}$ K, matching the $508$ K bare-rock prediction in radiative equilibrium with no significant heat redistribution.
```

The habitable-zone sub-Neptune K2-18 b exhibits $\mathrm{CH_4}$ and $\mathrm{CO_2}$ alongside a marginal $2\sigma$ detection of **dimethyl sulfide** (DMS), initially interpreted as evidence for a **hycean world** with a liquid-water ocean {cite:p}`Madhusudhan2023` ({numref}`fig:k218b`).

```{figure} figures/k218b_spectrum.avif
:align: center
:name: fig:k218b
:width: 90%

JWST transmission spectrum of **K2-18 b** from {cite:t}`Madhusudhan2023`, combining NIRISS SOSS and NIRSpec G395H observations with colour-coded model spectra containing $\mathrm{CH_4}$, $\mathrm{CO_2}$, and tentatively dimethyl sulfide (DMS). While the $\mathrm{CH_4}$ and $\mathrm{CO_2}$ detections are clear, the tentative DMS feature lies near the JWST sensitivity floor and remains heavily dependent on retrieval assumptions.
```

Subsequent reanalyses disputed the DMS detection, showing the data are also consistent with an uninhabitable mini-Neptune {cite:p}`Wogan2024`, with an interior too hot to hold a liquid water ocean {cite:p}`Glein2024`, or with an atmosphere overlying a **magma ocean**, a molten interior that depletes $\mathrm{NH_3}$ by dissolving nitrogen {cite:p}`Shorttle2024`.
Like past debates over Martian methane ({ref}`Lecture 10 <lecture10>`) and Venusian phosphine ({ref}`Lecture 14 <lecture14>`), K2-18 b illustrates how tentative biosignature claims undergo community scrutiny and revision.

### The habitable zone revisited

The **classical habitable zone** is the range of stellar fluxes where a rocky planet can maintain liquid surface water ({ref}`Lecture 9 <lecture09>`).
{cite:t}`Kasting1993` identified two boundaries using a one-dimensional radiative-convective model.
The **inner edge** is set by the **runaway greenhouse limit**: rising water vapour caps outgoing longwave radiation at $280$ to $310$ W/m$^2$, evaporating the ocean.
For a Sun-like star, this occurs at $\sim 1.06$ times Earth's flux ($\sim 0.97$ AU), with the conservative moist greenhouse limit at $\sim 0.99$ AU.
The **outer edge** is set by the **maximum $\mathrm{CO_2}$ greenhouse**, where $\mathrm{CO_2}$ condenses into ice clouds and greenhouse warming saturates, at $S_{\mathrm{eff}} \approx 0.35\,S_\oplus$ or $\sim 1.69$ AU for the present Sun.

```{figure} figures/kopparapu_hz.avif
:align: center
:name: fig:kopparapu
:width: 80%

The **classical habitable zone** as a function of stellar effective temperature and effective stellar flux, from {cite:t}`Kopparapu2013`. The green-shaded region is the habitable zone bounded on the inside by the moist greenhouse limit and on the outside by the maximum $\mathrm{CO_2}$ greenhouse limit. Symbols mark known potentially habitable exoplanets including GJ 581 d/g, GJ 667C c, Kepler-22 b, Tau Ceti e/f, and the solar system planets Earth, Venus, and Mars. The "Recent Venus" and "Early Mars" empirical limits are shown by the dotted boundaries.
```

{cite:t}`Kopparapu2013` updated these 1D boundaries across stellar effective temperatures, including M dwarfs ({numref}`fig:kopparapu`).
Two important caveats apply to these classical estimates.

First, evolutionary history matters rather than snapshot conditions alone.
A planet in the habitable zone today may have suffered early runaway greenhouse desiccation ({ref}`Lecture 9 <lecture09>`).
M dwarf planets spend hundreds of Myr in runaway greenhouse conditions during the pre-main-sequence phase, potentially losing their water inventory {cite:p}`LugerBarnes2015`.
Habitability is therefore a trajectory through climate space rather than a static present-day line.

Second, one-dimensional calculations neglect three-dimensional circulation and cloud feedbacks.
General circulation models show that cloud feedbacks shift boundaries by 5 to 20% depending on rotation rate, atmospheric composition, and surface albedo {cite:p}`Way2016,Turbet2021`.
For tidally locked M dwarf planets, substellar clouds extend the inner edge to fluxes well above the 1D moist greenhouse limit.
The classical habitable zone is thus a first-order screening tool rather than a precise boundary.

### Biosignature gases and the challenge of false positives

Atmospheric biosignatures are classically identified through **disequilibrium gas combinations**, mixtures of reactive gases that cannot persist without continuous biological replenishment.
On modern Earth, the coexistence of $\mathrm{O_2}$ ($\sim 21\%$) and $\mathrm{CH_4}$ ($\sim 1.8$ ppm) is the canonical example, because both react photochemically within decades and require continuous biological production.
Classical biosignature gases include $\mathrm{O_2}$, $\mathrm{O_3}$, $\mathrm{CH_4}$, and $\mathrm{N_2O}$, though a single gas in isolation almost never constitutes a biosignature.
{numref}`fig:l13-biosignature-gases` shows where these gases absorb: each has bands in the infrared that a transmission or emission spectrum can pick up, which is what makes them observable at all.

```{figure} figures/schwieterman2018_biosignature_gases.avif
:align: center
:name: fig:l13-biosignature-gases
:width: 85%

Absorption cross-sections from optical to mid-infrared wavelengths (0.4 to 20 $\mu$m) for ten candidate biosignature gases: $\mathrm{O_2}$, $\mathrm{O_3}$, $\mathrm{N_2O}$, $\mathrm{CH_4}$, $\mathrm{CH_3Cl}$, $\mathrm{C_2H_6}$, $\mathrm{NH_3}$, dimethyl sulfide, dimethyl disulfide and $\mathrm{CH_3SH}$. Oxygen absorbs only in narrow optical bands; the others have their strongest features in the infrared. Reproduced from {cite:t}`Schwieterman2018`.
```

The central challenge in biosignature detection is **false positives**, abiotic processes that mimic biological gas signatures.
{cite:t}`Wordsworth2014` showed that water vapour photolysis followed by hydrogen escape can build up substantial abiotic $\mathrm{O_2}$ on dry planets around M dwarfs.
Likewise, $\mathrm{CO_2}$ photolysis in dry atmospheres produces abiotic $\mathrm{O_2}$ by splitting $\mathrm{CO_2}$ into CO and O, driven by stellar XUV irradiation.
Abiotic $\mathrm{CH_4}$ can similarly arise from volcanic outgassing, hydrothermal serpentinisation reactions, and impact shocks ({ref}`Lecture 10 <lecture10>`).

Biosignature identification is fundamentally an **inverse problem** where candidate gases must be distinguished from abiotic false positives ({ref}`Lecture 14 <lecture14>`).

### Comparative payoff: the solar system in the exoplanet landscape

Whether the solar system is typical has been an open question since {ref}`Lecture 1 <lecture01>`.
If "typical" means the most common configuration in the bias-corrected exoplanet archive, the answer is no.
The most common stars are M dwarfs rather than G dwarfs like the Sun.
The most common planet class is the **sub-Neptune** ($2$ to $3\,\Rearth$), which the solar system lacks between Earth ($1\,\Rearth$) and Neptune ($3.88\,\Rearth$).
Inner exoplanet systems often form compact **peas-in-a-pod** configurations ($\sim 5$ to $8$ similarly sized planets within $\sim 0.2$ AU), whereas the solar system has four irregularly spaced terrestrial planets out to $1.5$ AU.
The solar system also lacks hot Jupiters or hot Neptunes, and its giant planets occupy wide ($\geq 5$ AU), nearly circular orbits rather than eccentric paths.
Comparing Kepler multi-planet architectures directly with the inner solar system highlights this contrast in planet size and orbital spacing ({numref}`fig:l13-peas-in-a-pod-solarsys`).

```{figure} figures/raymond2022_peas_in_a_pod.avif
:align: center
:name: fig:l13-peas-in-a-pod-solarsys
:width: 75%

Compact multi-planet systems containing four or more transiting planets out to about 1.5 AU, ordered by the dispersion of planet sizes within each system. The solar system terrestrial planets show significantly greater size diversity and wider spacing than typical compact exoplanet architectures. Reproduced from {cite:t}`Weiss2023`.
```

However, the observed archive is shaped by detection biases that work against finding solar system analogues.
A Jupiter analogue at $5$ AU produces a radial velocity signal of $\sim 12$ m/s with a 12-year period, requiring more than a decade to detect (fewer than a hundred are known).
Saturn analogues at $9.5$ AU and Earth analogues at 1 AU around Sun-like stars sit at the edge of current sensitivity.
Whether the solar system is truly rare or merely undersampled in parameter space remains an open question ({ref}`Lecture 14 <lecture14>`).

### Frontier missions, part 1: surveys and atmospheres (2026--2035)

**PLATO** (PLAnetary Transits and Oscillations of stars) is an ESA mission scheduled for launch in January 2027 {cite:p}`Rauer2014`.
Using 26 cameras as a multi-aperture photometric array, PLATO will monitor bright Sun-like stars over 2 to 3 year baselines to detect Earth analogues in the habitable zones of G dwarfs.
Ariel will survey approximately 1000 exoplanet atmospheres to provide a statistical census of composition.
The **Nancy Grace Roman Space Telescope** Galactic bulge microlensing survey will deliver $\sim 1400$ bound exoplanets at separations of $\sim 0.5$ to $10$ AU down to lunar masses {cite:p}`Penny2019`.

### Frontier missions, part 2: direct imaging of Earth analogues (2030s--2040s)

The **Habitable Worlds Observatory** (HWO) is a planned $\sim 6$ m NASA flagship space telescope targeted for launch in the 2040s to directly image Earth analogues.
Using a coronagraph or external starshade to achieve contrasts of $10^{-10}$ at sub-arcsecond separations from nearby Sun-like stars, HWO will directly image and obtain spectra of approximately $25$ Earth analogues to search for atmospheric biosignatures.
The **Large Interferometer For Exoplanets** (LIFE) will complement reflected-light imaging by using a mid-infrared nulling interferometer to detect thermal emission from terrestrial exoplanets.

Ground-based Extremely Large Telescopes will further resolve habitable-zone planets around nearby M dwarfs, complementing the space-based direct-imaging concepts of {ref}`Lecture 14 <lecture14>`.

### Open questions for the next lecture

A central open question is what constitutes a convincing detection of life on another world.
It is debated whether a single biosignature gas, gas abundance ratios, seasonal cycles, or photosynthetic surface features are sufficient.
The answer depends on how much we trust atmospheric models and catalogues of false positives.
{ref}`Lecture 14 <lecture14>` addresses how to move from a candidate biosignature to detecting life through Bayesian frameworks that combine observational data with planetary context.

## Summary

- Exoplanet science went from the first confirmed detection in 1992 to more than 6000 confirmed planets by 2026, a complete observational revolution in three decades.
- **Each detection method has a distinct bias**: radial velocity and transits favour short periods and large planets, direct imaging targets wide young giants, astrometry finds Jupiter analogues, and microlensing probes wide separations.
- The combined transit-plus-radial-velocity measurement breaks the $m \sin i$ degeneracy and gives bulk densities, the central observational quantity that turns exoplanet detections into physical objects with measurable composition.
- **Kepler showed that planets are common.** Most main-sequence stars host at least one planet, and the small-planet population dominates by number. Hot Jupiters occur around only $\sim 1\%$ of Sun-like stars.
- The **radius valley** at $\sim 1.8\,\Rearth$ indicates atmospheric stripping (photoevaporation and core-powered mass loss) that converts sub-Neptunes into bare super-Earth cores.
- The **hot Neptune desert**, the **peas-in-a-pod** correlation, and the **TRAPPIST-1** resonant chain are the other three central architectural results that any planet formation theory must explain.
- **JWST has made atmospheric characterisation routine**, detecting photochemical $\mathrm{SO_2}$ on WASP-39 b, ruling out a thick atmosphere on TRAPPIST-1 b, and testing biosignature claims on K2-18 b.
- **The solar system is not obviously typical**, lacking sub-Neptunes and compact inner systems, though whether it is rare or undersampled remains an open question.
- **Habitability is a history-dependent trajectory**, not a snapshot line on the HR diagram, and biosignature detection is an inverse problem with unavoidable false-positive challenges.
- Upcoming missions will push from demography to characterisation of habitable worlds, framing the biosignature detection criteria examined in {ref}`Lecture 14 <lecture14>`.

## References

```{bibliography}
:filter: docname in docnames
```
