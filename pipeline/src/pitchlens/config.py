"""Project configuration: data locations and the competitions PitchLens covers.

The competition list is a recorded decision (ADR 0006); change it there first.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

DATA_DIR_ENV = "PITCHLENS_DATA_DIR"


@dataclass(frozen=True)
class Competition:
    """A StatsBomb open-data competition season used by PitchLens."""

    name: str
    competition_id: int
    season_id: int
    has_360: bool
    role: str

    @property
    def key(self) -> str:
        """Stable identifier used in file paths, e.g. ``55-282``."""
        return f"{self.competition_id}-{self.season_id}"


MVP_COMPETITIONS: tuple[Competition, ...] = (
    Competition("UEFA Euro 2024", 55, 282, True, "xG training, xG v2"),
    Competition("UEFA Women's Euro 2025", 53, 315, True, "held-out xG test, xG v2"),
    Competition("Premier League 2015/16", 2, 27, False, "xG training, full-season per-90 tables"),
)

FORECAST_COMPETITION_CODE = "PL"  # football-data.org code for the Premier League (ADR 0006)


def data_dir() -> Path:
    """Root of the local data store (raw cache, staged Parquet, DuckDB).

    Defaults to ``./data`` relative to the working directory; override with
    the ``PITCHLENS_DATA_DIR`` environment variable.
    """
    return Path(os.environ.get(DATA_DIR_ENV, "data")).expanduser().resolve()
