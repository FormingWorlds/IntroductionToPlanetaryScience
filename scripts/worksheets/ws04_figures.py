"""Generate the figure embedded in Worksheet 4 as a vector PDF.

The figure comes from the Lecture 7 chronology script, so the sheet stays
numerically consistent with the lecture notes by construction:

- ``neukum_chronology_noreadoff.pdf`` drops the worked read-off
  construction, because Problem 2(b) asks the student to perform the
  read-off; the formula box and the coefficient labels stay on the plot.

Run from the repository root:  python3 scripts/worksheets/ws04_figures.py
Rerun whenever the source figure script changes.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

OUT_DIR = ROOT / "worksheets/worksheet04/figures"


def build(module_name: str, out_name: str, **kwargs) -> None:
    import scripts.figures._shared.style as style

    captured = {}
    orig = style.save_figure

    def _capture(fig, out, **kw):
        captured["fig"] = fig
        return out

    style.save_figure = _capture
    try:
        mod = importlib.import_module(module_name)
        importlib.reload(mod)
        mod.make_plot(**kwargs)
    finally:
        style.save_figure = orig
    fig = captured["fig"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / out_name
    fig.savefig(out, bbox_inches="tight")
    print(f"  {out}")


def main() -> None:
    build("scripts.figures.L07_surfaces.fig_neukum_chronology",
          "neukum_chronology_noreadoff.pdf", show_readoff=False)


if __name__ == "__main__":
    main()
