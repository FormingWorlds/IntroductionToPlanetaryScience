"""Shared helpers for the exam arithmetic checkers.

The per-exam scripts ``check_*.py`` recompute every printed number and report
through the helpers here, so all checkers count, print, and fail the same way.
This module is imported, never run: the CI glob picks up only ``check_*.py``.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

# Stefan-Boltzmann constant as printed in each exam's data box, W m^-2 K^-4.
SIGMA = 5.670e-8

_n_checks = 0
_failures: list[str] = []


def check(name: str, got: float, printed: float, rtol: float = 5e-4) -> None:
    """Compare a recomputed value against the printed one within rtol."""
    global _n_checks
    _n_checks += 1
    ok = math.isfinite(got) and abs(got - printed) <= rtol * abs(printed)
    tag = "ok " if ok else "FAIL"
    print(f"  [{tag}] {name}: got {got:.5g}, printed {printed:.5g}")
    if not ok:
        _failures.append(name)


def teq(flux: float, albedo: float) -> float:
    """Equilibrium temperature in K for absorbed flux S(1-A)/4."""
    return (flux * (1.0 - albedo) / (4.0 * SIGMA)) ** 0.25


def check_points(content_tex: str, expected: float, each: float | None = None) -> None:
    """Sum the ``\\pts{n}`` marks in an exam content file against the total.

    Comment lines are stripped first, so a commented-out part cannot keep
    the sums looking right.

    Parameters
    ----------
    content_tex : str
        Path of the content file relative to the ``exams`` directory,
        e.g. ``"mockexam02/mockexam02_content.tex"``.
    expected : float
        The advertised points total of the exam.
    each : float, optional
        The advertised points total of every single question. When given,
        the marks inside each ``\\problem`` block must sum to this value.
    """
    path = Path(__file__).resolve().parents[2] / "exams" / content_tex
    text = re.sub(r"(?<!\\)%.*", "", path.read_text())
    if each is not None:
        blocks = re.split(r"\\problem\{", text)[1:]
        for i, block in enumerate(blocks, start=1):
            q_marks = [int(m) for m in re.findall(r"\\pts\{(\d+)\}", block)]
            check(f"points sum question {i}", float(sum(q_marks)), each)
    marks = [int(m) for m in re.findall(r"\\pts\{(\d+)\}", text)]
    check(f"points sum over {len(marks)} parts", float(sum(marks)), expected)


def verdict() -> None:
    """Print the pass/fail summary and exit nonzero on any failed check."""
    print()
    if _failures:
        print(f"FAILED: {len(_failures)} of {_n_checks} checks")
        for name in _failures:
            print(f"  - {name}")
        sys.exit(1)
    print(f"ALL OK ({_n_checks} checks)")
