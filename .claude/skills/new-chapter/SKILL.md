---
name: new-chapter
description: Create a new chapter directory with template and update _toc.yml
disable-model-invocation: true
---

Create a new chapter for the Jupyter Book. The user provides a chapter number and topic title.

Steps:
1. Determine the directory name following the convention: `book/NN_topic_name/` (e.g., `book/15_moons/`)
2. Create the chapter directory under `book/`
3. Create the main markdown file inside it (e.g., `book/15_moons/moons.md`) using the structure of existing chapters as a template, including:
   - A top-level heading with the chapter title
   - Placeholder sections for key content
   - Proper MyST Markdown syntax
   - Use of the project's custom LaTeX macros where relevant (`\Msun`, `\Rearth`, `\Mjup`, `\kB`, `\dv`, `\pdv`, etc.)
4. Create a `figures/` subdirectory inside the chapter directory
5. Add the chapter to `book/_toc.yml` in the correct position (ordered by chapter number)
6. Report what was created
