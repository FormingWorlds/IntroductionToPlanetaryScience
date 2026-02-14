# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

University course materials repository for "Introduction to Planetary Science" at the Kapteyn Institute (course code WBAS002-05). Part of the [FormingWorlds](https://github.com/FormingWorlds) organization.

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

## Build System

Uses **Jupyter Book v1** (`jupyter-book<2`) with Sphinx backend. Dependencies in `requirements.txt`.

```bash
make html       # Build browsable HTML → book/_build/html/
make pdflatex   # Build PDF via XeLaTeX → book/_build/latex/
make clean      # Remove build artifacts
```

Build artifacts in `book/_build/` are gitignored.

## Key Details

- The course covers 14 lectures spanning planet formation through exoplanets and astrobiology (see `planning/course_development.md` for full curriculum, schedule, homework, and exam structure).
- Each lecture includes a ~10 min blackboard derivation of a foundational concept.
- Lecture notes use MyST Markdown with cross-reference labels `(lecture01)=` through `(lecture14)=`.
- Math macros are defined in both `mathjax3_config` (HTML) and `latex_elements.preamble` (PDF) in `_config.yml` — new macros must be added to both.
- The `physics` LaTeX package conflicts with Sphinx output; custom `\dv`, `\dd`, `\pdv` macros are used instead.
- LaTeX packages available: `amsmath`, `amssymb`, `mhchem` (for chemical formulae like `\ce{CO2}`).
