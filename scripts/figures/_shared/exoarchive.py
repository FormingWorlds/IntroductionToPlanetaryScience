"""Download exoplanet data from the NASA Exoplanet Archive TAP service.

The Archive's TAP endpoint accepts ADQL via HTTP GET and can return CSV
directly. We use only the `pscomppars` table (planetary systems
composite parameters), which is the canonical "default-row-per-planet"
table for the Archive. Reference:
https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html

Each download writes:

    <out_dir>/nasa_exoplanet_archive_<table>_<YYYY-MM-DD>.csv
    <out_dir>/nasa_exoplanet_archive_<table>_<YYYY-MM-DD>.json   (metadata)

The metadata sidecar carries the source URL, ADQL query, retrieval
date, row count, column dictionary, and reference citation key. This is
what makes every value traceable.
"""
from __future__ import annotations

import datetime as _dt
import json
import socket
import subprocess
from pathlib import Path
from urllib.parse import quote_plus

TAP_HOST = "exoplanetarchive.ipac.caltech.edu"
TAP_BASE = f"https://{TAP_HOST}/TAP/sync"


def _resolve_via_public_dns(host: str) -> str | None:
    """Resolve `host` via Google DNS (8.8.8.8) using `nslookup` as a fallback
    when the local resolver fails (sometimes happens inside sandboxes).
    """
    try:
        out = subprocess.check_output(
            ["nslookup", host, "8.8.8.8"],
            stderr=subprocess.DEVNULL,
            timeout=10,
        ).decode()
    except Exception:
        return None
    last_address = None
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("Address:") and "#" not in line:
            last_address = line.split(":", 1)[1].strip()
    return last_address


def _curl_get(url: str, *, timeout: int = 120) -> bytes:
    """Fetch `url` via curl, with a public-DNS fallback if local DNS fails."""
    cmd = ["curl", "-fsSL", "--max-time", str(timeout), "-o", "-", url]
    try:
        return subprocess.check_output(cmd)
    except subprocess.CalledProcessError:
        # Try with explicit --resolve via public DNS
        ip = _resolve_via_public_dns(TAP_HOST)
        if ip is None:
            raise
        cmd = [
            "curl", "-fsSL", "--max-time", str(timeout),
            "--resolve", f"{TAP_HOST}:443:{ip}",
            "-o", "-", url,
        ]
        return subprocess.check_output(cmd)

DEFAULT_TABLE = "pscomppars"
DEFAULT_CITATION_KEY = "NASAExoArchive2025"


def fetch(
    columns: list[str],
    out_dir: Path,
    *,
    table: str = DEFAULT_TABLE,
    where: str | None = None,
    citation_key: str = DEFAULT_CITATION_KEY,
    column_descriptions: dict[str, str] | None = None,
    purpose: str = "",
    figure_id: str = "",
) -> tuple[Path, Path]:
    """Download an Archive table slice and write a metadata sidecar.

    Parameters
    ----------
    columns
        ADQL column list (e.g. ["pl_name", "disc_year", "discoverymethod"]).
    out_dir
        Directory to write the CSV + JSON metadata.
    table
        Archive table name. Default is `pscomppars`.
    where
        Optional ADQL WHERE clause (no leading "WHERE").
    citation_key
        BibTeX key in book/references.bib to associate with the data.
    column_descriptions
        Per-column human-readable description and units, included in the
        sidecar JSON. Keyed by column name.
    purpose
        One-line description of what figure / analysis this download is
        for. Recorded in the sidecar.

    Returns
    -------
    (csv_path, json_path)
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    select = ", ".join(columns)
    query = f"select {select} from {table}"
    if where:
        query += f" where {where}"

    url = f"{TAP_BASE}?query={quote_plus(query)}&format=csv"
    payload = _curl_get(url)

    today = _dt.date.today().isoformat()
    figure_tag = f"_{figure_id}" if figure_id else ""
    base = f"nasa_exoplanet_archive_{table}{figure_tag}_{today}"
    csv_path = out_dir / f"{base}.csv"
    json_path = out_dir / f"{base}.json"

    csv_path.write_bytes(payload)

    text = payload.decode("utf-8", errors="replace")
    n_rows = max(0, text.count("\n") - 1)
    meta = {
        "source": "NASA Exoplanet Archive (Caltech-IPAC)",
        "endpoint": TAP_BASE,
        "table": table,
        "adql_query": query,
        "retrieved_utc": _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "retrieved_date": today,
        "n_rows": n_rows,
        "columns": columns,
        "column_descriptions": column_descriptions or {},
        "citation_key": citation_key,
        "purpose": purpose,
        "license_note": (
            "NASA Exoplanet Archive data are public domain. Cite the "
            "Archive (Akeson et al. 2013) and the individual discovery "
            "papers as appropriate."
        ),
    }
    json_path.write_text(json.dumps(meta, indent=2))

    return csv_path, json_path


def latest_snapshot(
    out_dir: Path,
    table: str = DEFAULT_TABLE,
    figure_id: str = "",
) -> Path | None:
    """Return the most recent matching CSV snapshot in `out_dir`, or None."""
    out_dir = Path(out_dir)
    figure_tag = f"_{figure_id}" if figure_id else ""
    candidates = sorted(out_dir.glob(f"nasa_exoplanet_archive_{table}{figure_tag}_*.csv"))
    return candidates[-1] if candidates else None
