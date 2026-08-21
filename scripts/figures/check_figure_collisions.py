"""Check that no figure text collides with plotted lines or markers.

For every course figure script, the figure is rebuilt, each text artist
inside the axes region is hidden in turn, and the remaining dark ink
under the (slightly padded) text bounding box is measured. A text box
whose footprint covers more than ``MAX_INK_FRACTION`` dark ink sits on a
line, curve, marker, or another annotation and fails the check. Light
fills, alpha-dimmed grid lines, and legend frames stay below the ink
threshold, so panels and shaded bands do not trigger false alarms.

Run from the repository root:  python3 scripts/figures/check_figure_collisions.py
Optionally pass lecture directory names (e.g. L06_atmospheres_2) to
restrict the sweep.

Rules for new figures:
- Every text or annotation must sit clear of all drawn geometry; place
  labels by measured bounding box, not by eye.
- If a label cannot clear the ink, move it outside the crowded region
  and tie it back with a thin leader line.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

# Scripts that author an SVG directly and never build a matplotlib
# figure; their geometry is checked at the SVG level instead
SKIP = {
    "scripts.figures.L02_formation_orbits.fig_kepler_laws",
    # Needs the fwl-calliope package, which is not part of the default
    # figure-build environment
    "scripts.figures.L04_differentiation_magnetospheres.fig_outgassing_speciation_fO2",
}

# Ink darker than this luminance (0-255) counts as line work; light
# fills and 30%-alpha grid lines stay above it
INK_LUMINANCE = 180.0
# Fraction of the padded text box that may contain foreign ink
MAX_INK_FRACTION = 0.005
# At or above this coverage the text sits on a solid fill; that is a
# deliberate contrast label only when the text colour clears the WCAG
# large-text contrast ratio against the fill it sits on
SOLID_FILL_FRACTION = 0.85
MIN_SOLID_FILL_CONTRAST = 3.0
PAD_PX = 2

# Not covered by this check: axes titles and axis labels (outside the
# data region), tick labels, and annotation leader lines crossing
# other text. Figure-level text (suptitle, fig.text) is checked when
# it overlaps an axes data region. Legends are checked as whole
# artists: hiding the legend reveals any geometry its box would cover,
# framed or not.


def _luminance(rgb: np.ndarray) -> np.ndarray:
    return 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]


def _render(fig) -> np.ndarray:
    fig.canvas.draw()
    return np.asarray(fig.canvas.buffer_rgba())[..., :3].astype(float)


def _text_bbox(t):
    """Text-only bounding box (an Annotation's extent unions its arrow)."""
    from matplotlib.text import Text

    return Text.get_window_extent(t)


def _has_halo(t) -> bool:
    """A filled bbox patch masks the ink beneath it (contour-label halo)."""
    patch = getattr(t, "get_bbox_patch", lambda: None)()
    if patch is None:
        return False
    face = patch.get_facecolor()
    return face[3] > 0.8


def _wcag_luminance(rgb) -> float:
    """WCAG 2.x relative luminance of an sRGB colour in [0, 1]."""
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
           for c in rgb]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def _solid_fill_contrast(t, patch: np.ndarray) -> float:
    """WCAG contrast ratio between the text colour and the median
    colour of the fill it sits on."""
    from matplotlib.colors import to_rgb

    lum_text = _wcag_luminance(to_rgb(t.get_color()))
    lum_fill = _wcag_luminance(np.median(patch / 255.0, axis=(0, 1)))
    hi, lo = max(lum_text, lum_fill), min(lum_text, lum_fill)
    return (hi + 0.05) / (lo + 0.05)


def _text_artists(fig):
    """Text artists that live inside an axes data region, including
    figure-level text (suptitle, fig.text) overlapping any axes."""
    arts = []
    ax_bbs = [ax.get_window_extent() for ax in fig.axes]
    for ax, ax_bb in zip(fig.axes, ax_bbs):
        for t in ax.texts:
            if not t.get_text().strip() or not t.get_visible():
                continue
            if _has_halo(t):
                continue
            if _text_bbox(t).overlaps(ax_bb):
                arts.append(t)
    for t in fig.texts:
        if not t.get_text().strip() or not t.get_visible():
            continue
        if _has_halo(t):
            continue
        if any(_text_bbox(t).overlaps(bb) for bb in ax_bbs):
            arts.append(t)
    return arts


def _legends(fig):
    """Every legend on the figure, checked as one opaque artist."""
    legs = [ax.get_legend() for ax in fig.axes]
    legs += list(fig.legends)
    return [lg for lg in legs if lg is not None and lg.get_visible()]


def check_module(mod_name: str) -> list[str]:
    """Rebuild one figure and measure ink under each text box."""
    import scripts.figures._shared.style as style

    captured = {}
    orig_save = style.save_figure

    def _capture(fig, out, **kw):
        captured["fig"] = fig
        return out

    style.save_figure = _capture
    try:
        mod = importlib.import_module(mod_name)
        importlib.reload(mod)
        import inspect

        sig = inspect.signature(mod.make_plot)
        needs_args = any(
            p.default is p.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
            for p in sig.parameters.values()
        )
        if needs_args and hasattr(mod, "fetch_data"):
            # Data figures take a CSV path; reuse the committed snapshot
            mod.make_plot(mod.fetch_data(refresh=False))
        else:
            mod.make_plot()
    finally:
        style.save_figure = orig_save

    fig = captured.get("fig")
    if fig is None:
        return [f"{mod_name}: no figure captured"]

    failures = []
    texts = _text_artists(fig)
    full = _render(fig)
    for t in texts:
        bb = _text_bbox(t)
        t.set_visible(False)
        bare = _render(fig)
        t.set_visible(True)
        h, w = bare.shape[:2]
        x0 = max(int(bb.x0) - PAD_PX, 0)
        x1 = min(int(bb.x1) + PAD_PX, w)
        # buffer_rgba row 0 is the TOP of the figure; bbox y is from the bottom
        y0 = max(int(h - bb.y1) - PAD_PX, 0)
        y1 = min(int(h - bb.y0) + PAD_PX, h)
        patch = bare[y0:y1, x0:x1]
        if patch.size == 0:
            continue
        ink = (_luminance(patch) < INK_LUMINANCE).mean()
        if (ink >= SOLID_FILL_FRACTION
                and _solid_fill_contrast(t, patch) >= MIN_SOLID_FILL_CONTRAST):
            # Readable text on a solid fill is contrast design
            continue
        if ink > MAX_INK_FRACTION:
            failures.append(
                f"{mod_name}: text {t.get_text()[:40]!r} sits on ink "
                f"(fraction {ink:.3f} > {MAX_INK_FRACTION})"
            )
    for lg in _legends(fig):
        bb = lg.get_window_extent(fig.canvas.get_renderer())
        lg.set_visible(False)
        bare = _render(fig)
        lg.set_visible(True)
        h, w = bare.shape[:2]
        x0 = max(int(bb.x0) - PAD_PX, 0)
        x1 = min(int(bb.x1) + PAD_PX, w)
        y0 = max(int(h - bb.y1) - PAD_PX, 0)
        y1 = min(int(h - bb.y0) + PAD_PX, h)
        patch = bare[y0:y1, x0:x1]
        if patch.size == 0:
            continue
        ink = (_luminance(patch) < INK_LUMINANCE).mean()
        if ink > MAX_INK_FRACTION:
            failures.append(
                f"{mod_name}: legend covers ink "
                f"(fraction {ink:.3f} > {MAX_INK_FRACTION})"
            )
    plt.close(fig)
    return failures


def main() -> int:
    fig_dir = REPO_ROOT / "scripts" / "figures"
    only = set(sys.argv[1:])
    failures: list[str] = []
    n_figs = 0
    for lecture_dir in sorted(fig_dir.glob("L*")):
        if only and lecture_dir.name not in only:
            continue
        for script in sorted(lecture_dir.glob("fig_*.py")):
            mod_name = f"scripts.figures.{lecture_dir.name}.{script.stem}"
            if mod_name in SKIP:
                continue
            n_figs += 1
            try:
                failures += check_module(mod_name)
            except Exception as exc:  # a build failure is a failure
                failures.append(f"{mod_name}: build error: {exc}")
    if n_figs == 0:
        # An empty sweep means the layout moved or the arguments are wrong;
        # exiting 0 here would let CI pass without checking anything.
        print("ERROR: no figure scripts matched")
        return 1
    print(f"checked {n_figs} figure scripts")
    for f in failures:
        print(f"FAIL {f}")
    if not failures:
        print("ALL OK: no text-ink collisions")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
