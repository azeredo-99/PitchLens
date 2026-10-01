"""The ``pitchlens`` command-line interface.

Phase 0 ships ``info``. Later phases add ``ingest``, ``validate``, ``train``,
``evaluate``, ``publish``, ``forecast``, ``notes`` and ``export`` (SPEC §10).
"""

from __future__ import annotations

from typing import Annotated

import typer

from pitchlens import __version__
from pitchlens.config import FORECAST_COMPETITION_CODE, MVP_COMPETITIONS, data_dir

app = typer.Typer(
    help="PitchLens data pipeline: ingest, validate, model and publish football data.",
    no_args_is_help=True,
    add_completion=False,
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"pitchlens {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=_version_callback,
            is_eager=True,
            help="Show the version and exit.",
        ),
    ] = False,
) -> None:
    """PitchLens data pipeline."""


@app.command()
def info() -> None:
    """Show the version, data directory and configured competitions."""
    typer.echo(f"pitchlens {__version__}")
    typer.echo(f"data directory: {data_dir()}")
    typer.echo("StatsBomb competitions (ADR 0006):")
    for c in MVP_COMPETITIONS:
        flag = "360" if c.has_360 else "   "
        typer.echo(f"  {c.key:>7}  {flag}  {c.name}  ({c.role})")
    typer.echo(f"forecast league: football-data.org {FORECAST_COMPETITION_CODE}")
