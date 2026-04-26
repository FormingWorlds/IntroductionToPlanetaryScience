(lecture_slides)=
# Lecture Slides

Downloadable PDF slide decks for each lecture.
Each deck contains $\sim 60$--$90$ frames matching the lecture-notes structure on this site, with the same figures and the same blackboard derivations.

The slides are designed for $90$ minute classroom delivery and complement, rather than duplicate, the written lecture notes.
For full prose and bibliography, use the lecture pages.
For visual material in classroom format, use the slide decks.

| # | Lecture | Slides |
|---|---|---|
| 1 | {ref}`lecture01` | [Download (PDF)](_static/slides/lecture01.pdf) |
| 2 | {ref}`lecture02` | [Download (PDF)](_static/slides/lecture02.pdf) |
| 3 | {ref}`lecture03` | [Download (PDF)](_static/slides/lecture03.pdf) |
| 4 | {ref}`lecture04` | [Download (PDF)](_static/slides/lecture04.pdf) |
| 5 | {ref}`lecture05` | [Download (PDF)](_static/slides/lecture05.pdf) |
| 6 | {ref}`lecture06` | [Download (PDF)](_static/slides/lecture06.pdf) |
| 7 | {ref}`lecture07` | [Download (PDF)](_static/slides/lecture07.pdf) |
| 8 | {ref}`lecture08` | [Download (PDF)](_static/slides/lecture08.pdf) |
| 9 | {ref}`lecture09` | [Download (PDF)](_static/slides/lecture09.pdf) |
| 10 | {ref}`lecture10` | [Download (PDF)](_static/slides/lecture10.pdf) |
| 11 | Lecture 11 | _coming soon_ |
| 12 | Lecture 12 | _coming soon_ |
| 13 | Lecture 13 | _coming soon_ |
| 14 | Lecture 14 | _coming soon_ |

The decks share a common visual style (custom Beamer theme `beamerthemeIPS`) and use AVIF figures rendered via XeLaTeX.
LaTeX source for each deck lives at `slides/lectureNN/lectureNN.tex` in the [GitHub repository](https://github.com/FormingWorlds/IntroductionToPlanetaryScience).

## Build instructions

To rebuild a single deck locally:

```bash
cd slides
make lectureNN  # e.g. make lecture09
```

To rebuild all decks at once:

```bash
make slides     # from project root
```

Both targets handle the AVIF $\rightarrow$ PNG conversion automatically.
The build requires XeLaTeX with `fontspec` and `unicode-math` (TeX Live $\geq 2020$ is sufficient).
