# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University course materials repository for "Introduction to Planetary Science" at the Kapteyn Astronomical Institute of the University of Groningen. The main lecturer is Tim Lichtenberg from the Kapteyn Institute. This course is a BSc Astronomy mandatory course for 2nd-year students, covering fundamental concepts in planetary science, including planet formation, solar system dynamics, exoplanets, and astrobiology. The repository contains lecture notes, figures, and planning documents for the course. The lecture notes are written in MyST Markdown and built into HTML and PDF formats using Jupyter Book. The course emphasizes scientific accuracy, proper citation of sources, and clear explanations suitable for undergraduate students.

## Repository Structure

- `book/` — Jupyter Book source (MyST Markdown lecture notes, built to HTML and PDF)
  - `book/_config.yml` — Jupyter Book configuration (XeLaTeX, MathJax3, bibliography)
  - `book/_toc.yml` — Table of contents
  - `book/intro.md` — Landing page
  - `book/01_introduction/` through `book/14_synthesis/` — 14 lecture chapters, each with a `.md` file and `figures/` directory
  - `book/references.bib` — BibTeX bibliography
  - `book/_static/custom.css` — Custom styles
- `planning/` — Curriculum outlines and course planning documents
- `content/course2025` — Symlink to Google Drive containing previous lecture materials (slides, data, etc.); gitignored and not tracked
- `.github/workflows/book.yml` — GitHub Actions workflow deploying HTML to GitHub Pages

## High-level Instructions

- When editing lecture content, ensure scientific accuracy by verifying all claims against authoritative sources and citing them properly in the `## References` section.
- When adding new lectures or sections, maintain the established structure and formatting conventions (MyST Markdown, math macros, citation style).
- When updating the curriculum or schedule, reflect changes in `planning/course_development.md` to keep the course plan up to date.
- When searching for literature to cite, prioritize peer-reviewed journal articles, review papers, and authoritative databases (NASA, IAU) over textbooks or web sources. Always include a DOI when available.
- When looking for literature, check `contens/books` for authorative sources, but verify that they are still accurate and relevant before citing.
- When looking for literature, check `contens/course2025` for previously used sources and lecture materials, but verify that they are still accurate and relevant before citing.
- When looking for literature, use the NASA ADS database (https://ui.adsabs.harvard.edu/) to find recent papers on planetary science topics. Give some weight to the articles and referenced papers in `https://ui.adsabs.harvard.edu/public-libraries/L2e3RhUYQnqmpIyMpWUG3A`. Use the `bibtex` export option to generate BibTeX entries for new sources.
- When adding or editing content, ensure that all numerical values, equations, and historical claims are verified against primary sources or authoritative databases. Do not rely on training data alone for factual accuracy.
- All lectures should have good visuals (figures, diagrams) where appropriate. When adding figures, ensure they are properly referenced in the text and included in the `figures/` directory of the corresponding lecture.
- For all figures prioritize original sources (e.g., from NASA missions, published papers) and figures from the public domain. Ensure proper attribution in the caption. Avoid using low-quality or uncredited images.
- Double and triple check all citations for accuracy, including author names, publication year, journal, and DOI. Do not invent DOIs — if unsure whether a DOI exists, omit it and flag for manual verification with a comment: `% TODO: verify DOI`.
- Double and triple check all links (DOIs, URLs) to ensure they resolve correctly. For web resources, use the most stable/canonical URL available and note the access date in the BibTeX `note` field if the content is known to change frequently.
- Double and trip check all math equations for dimensional consistency and physical correctness. After writing a derivation, verify that the units on both sides match and check limiting cases to ensure the equation behaves as expected.


## Build System

Uses **Jupyter Book v1** (`jupyter-book<2`) with Sphinx backend. Dependencies in `pyproject.toml`.

### Environment setup

Requires Python 3.12+.

```bash
pip install .
```

### Build commands

```bash
make html       # Build browsable HTML → book/_build/html/
make pdf        # Build PDF via pdfhtml → book/_build/pdf/
make pdflatex   # Build PDF via XeLaTeX → book/_build/latex/
make clean      # Remove build artifacts
```

Build artifacts in `book/_build/` are gitignored.

### Deployed site

HTML is auto-deployed to GitHub Pages on push to `main`:
https://formingworlds.github.io/IntroductionToPlanetaryScience/

## Key Technical Details

- The course covers 14 lectures spanning planet formation through exoplanets and astrobiology (see `planning/course_development.md` for full curriculum, schedule, homework, and exam structure).
- Each lecture includes a ~10 min blackboard derivation of a foundational concept.
- Lecture notes use MyST Markdown with cross-reference labels `(lecture01)=` through `(lecture14)=`.
- Math macros are defined in both `mathjax3_config` (HTML) and `latex_elements.preamble` (PDF) in `_config.yml` — new macros must be added to both.
- The `physics` LaTeX package conflicts with Sphinx output; custom `\dv`, `\dd`, `\pdv` macros are used instead.
- LaTeX packages available: `amsmath`, `amssymb`, `mhchem` (for chemical formulae like `\ce{CO2}`).
- Custom math macros defined in `_config.yml` (available in both HTML and PDF):
  - `\dv{f}{x}` — total derivative, `\dd` — differential d, `\pdv{f}{x}` — partial derivative
  - `\Msun`, `\Rsun`, `\Lsun` — solar mass, radius, luminosity
  - `\Mearth`, `\Rearth` — Earth mass, radius
  - `\Mjup`, `\Rjup` — Jupiter mass, radius
  - `\kB` — Boltzmann constant
- The `sphinx-proof` extension is loaded, providing theorem-like directives: `{prf:theorem}`, `{prf:proof}`, `{prf:definition}`, `{prf:example}`, etc.
- Figures live in `<lecture_dir>/figures/` and are referenced with MyST syntax: `` ```{figure} figures/filename.png``` ``

## References & Citations

### Every lecture must have a "References" section

Each lecture `.md` file in `book/` **must** end with a dedicated `## References` section that lists all sources cited in that lecture. This section:

- Appears as the **final section** of the lecture, after all content sections
- Uses BibTeX citations via `sphinxcontrib-bibtex` (configured in `book/_config.yml`)
- All BibTeX entries live in `book/references.bib` (the single shared bibliography file)
- Citations in the text use MyST syntax: `` {cite}`AuthorYear` ``
- The references section renders the bibliography for that lecture using:

  ````markdown
  ## References

  ```{bibliography}
  :filter: docname in docnames
  ```
  ````

  The `:filter: docname in docnames` directive ensures only sources cited in that specific lecture are listed — not the entire bibliography.

### Citation style

- Use `author_year` style (configured in `_config.yml` as `bibtex_reference_style: author_year`)
- BibTeX keys follow the format `AuthorYear` (e.g., `Lichtenberg2021`, `Raymond2022`), or `AuthorYearLetter` when there are multiple papers by the same first author in the same year (e.g., `Wordsworth2013a`, `Wordsworth2013b`)
- Prefer DOI-bearing entries; include `doi = {}` field in every BibTeX entry where available
- Prefer peer-reviewed journal articles over textbooks or web sources; use review articles where appropriate for broad topics

### When adding or editing lecture content

1. Every factual claim, equation, or dataset that originates from a specific source **must** be cited
2. Add the corresponding BibTeX entry to `book/references.bib` if it does not already exist
3. Verify that the `## References` section with the `{bibliography}` directive is present at the end of the lecture file
4. **Always update `planning/course_development.md`** to reflect the changes — this includes:
   - The lecture outline (section 2) if topics are added, removed, or reordered
   - The status table (section 5) to track progress (e.g., "Not started" → "In progress" → "Draft complete")
   - The homework or exam sections if related content changes

## Scientific Accuracy & Source Verification

### Verification requirements

When writing or editing lecture content, invest substantial effort in verifying scientific accuracy. This is a university-level course — errors in the notes directly mislead students.

Specifically:

- **Numerical values** (physical constants, planetary parameters, orbital elements, isotopic ratios, etc.) must be checked against authoritative sources (NASA Planetary Fact Sheets, IAU standards, recent review articles). Do not rely on training data alone — look up and cite the source.
- **Equations and derivations** must be dimensionally consistent and physically correct. After writing a derivation, verify units on both sides and check limiting cases.
- **Historical claims** (discovery dates, mission timelines, naming conventions) must be verified against primary or well-established secondary sources.
- **Planetary data** should preferably reference NASA/JPL Solar System Dynamics, the Planetary Fact Sheet, or equivalent authoritative databases, with the access date noted where relevant.
- **Exoplanet statistics** (occurrence rates, demographics, detection counts) change frequently — always cite the specific study and year, and note that numbers are approximate.

### Common pitfalls to check

- Confusing mass and weight, or mixing up $M_\oplus$ and $M_J$ scales
- Using outdated values (e.g., number of confirmed exoplanets, Hubble constant, atmospheric compositions updated by recent missions)
- Incorrect unit conversions (AU ↔ km, bar ↔ Pa, K ↔ °C)
- Attributing discoveries or models to the wrong author or year
- Citing retracted or superseded results without noting the update
- Broken or non-persistent URLs — prefer DOIs over direct URLs for journal articles

### Link and DOI verification

- All DOIs should resolve correctly (format: `https://doi.org/10.xxxx/...`)
- Do not invent DOIs — if unsure whether a DOI exists, omit it and flag for manual verification with a comment: `% TODO: verify DOI`
- For web resources (NASA fact sheets, mission pages), use the most stable/canonical URL available
- If a URL is known to change frequently, note the access date in the BibTeX `note` field

## Content Style

- Write at the level of a 2nd-year BSc Astronomy student (see prerequisites in `planning/course_development.md`)
- Define technical terms on first use
- Use SI units throughout; use astronomical conventions where standard (AU, solar masses, etc.)
- Chemical formulae use `\ce{}` from mhchem (e.g., `$\ce{CO2}$`, `$\ce{H2O}$`)
- Cross-reference other lectures using MyST labels: `` {ref}`lecture01` `` through `` {ref}`lecture14` ``
