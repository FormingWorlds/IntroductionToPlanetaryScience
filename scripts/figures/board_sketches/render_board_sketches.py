"""Render the setup sketch of every blackboard derivation to an AVIF figure.

Each ``lectureNN_setup.tikz`` file in this directory holds the TikZ sketch
that opens the lecturer's board derivation (the goal-and-strategy panel).
The script wraps each sketch in a standalone XeLaTeX document that uses the
course colours and fonts, compiles it, rasterises the page with ImageMagick
and writes ``book/<lecture dir>/figures/board_sketch_lNN.avif``.

Usage
-----
    PATH=/Library/TeX/texbin:$PATH PYTHONPATH=. .venv/bin/python \\
        scripts/figures/board_sketches/render_board_sketches.py [NN ...]

Without arguments every lecture with a ``lectureNN_setup.tikz`` file is
rendered. Requires ``xelatex`` and ``magick`` on the PATH.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from scripts.figures._shared.style import _encode_avif

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
BOOK = REPO_ROOT / "book"
DPI = 900

PREAMBLE = r"""
\documentclass[tikz, border=6pt]{standalone}
\usepackage{fontspec}
\usepackage{unicode-math}
\setsansfont{Inter-Regular.otf}[BoldFont=Inter-Bold.otf, ItalicFont=Inter-Italic.otf]
\setmathfont{FiraMath-Regular.otf}
\setmathfont{latinmodern-math.otf}[range={"22C6}]
\renewcommand{\familydefault}{\sfdefault}
\usetikzlibrary{arrows.meta}
\definecolor{ipsPrimary}{HTML}{1B2A4A}
\definecolor{ipsAccent}{HTML}{2C7A7B}
\definecolor{ipsText}{HTML}{2D3748}
\definecolor{ipsLightFill}{HTML}{EDF2F7}
\definecolor{ipsOrange}{HTML}{DD6B20}
\AtBeginDocument{\let\mathrm\mathsf\color{ipsText}}
\begin{document}
"""


def lecture_dir(nn: str) -> Path:
    """Return the book directory of lecture ``nn`` (two digits)."""
    matches = sorted(BOOK.glob(f"{nn}_*"))
    if len(matches) != 1:
        raise FileNotFoundError(f"no unique book directory for lecture {nn}")
    return matches[0]


def render(nn: str) -> Path:
    """Compile the sketch of lecture ``nn`` and write its AVIF; return the path."""
    tikz = (HERE / f"lecture{nn}_setup.tikz").read_text()
    out = lecture_dir(nn) / "figures" / f"board_sketch_l{nn}.avif"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "sketch.tex").write_text(PREAMBLE + tikz + "\\end{document}\n")
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "sketch.tex"],
            cwd=tmp, check=True, stdout=subprocess.DEVNULL,
        )
        png = tmp / "sketch.png"
        subprocess.run(
            ["magick", "-density", str(DPI), str(tmp / "sketch.pdf"),
             "-background", "white", "-alpha", "remove", "-alpha", "off", str(png)],
            check=True,
        )
        _encode_avif(png, out, quality=80)
    return out


def main(argv: list[str]) -> None:
    """Render the lectures named on the command line, or all of them."""
    lectures = argv or sorted(p.stem[7:9] for p in HERE.glob("lecture??_setup.tikz"))
    for nn in lectures:
        print(render(nn).relative_to(REPO_ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])
