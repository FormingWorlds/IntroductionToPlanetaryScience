"""Generate the two figures embedded in Worksheet 3 as vector PDFs.

Both figures come from the Lecture 6 figure scripts, so the sheet stays
numerically consistent with the lecture notes by construction:

- ``psat_curves.pdf`` is the saturation-curve figure as published.
- ``snowball_bistability_unlabeled.pdf`` drops the three stability
  labels, because Problem 5(b) asks the student to classify the
  crossings; the temperature values stay on the plot.

Run from the repository root:  python3 scripts/worksheets/ws03_figures.py
Rerun whenever the source figure scripts change.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

OUT_DIR = ROOT / "worksheets/worksheet03/figures"


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
    build("scripts.figures.L06_atmospheres_2.fig_psat_curves", "psat_curves.pdf")
    build("scripts.figures.L06_atmospheres_2.fig_snowball_bistability",
          "snowball_bistability_unlabeled.pdf", label_states=False)


if __name__ == "__main__":
    main()
