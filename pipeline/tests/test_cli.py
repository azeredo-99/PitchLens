from pathlib import Path

import pytest
from typer.testing import CliRunner

from pitchlens import __version__
from pitchlens.cli import app

runner = CliRunner()


def test_version_flag_prints_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == f"pitchlens {__version__}"


def test_no_arguments_shows_help() -> None:
    result = runner.invoke(app, [])
    assert "info" in result.output


def test_info_lists_every_mvp_competition() -> None:
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    for key in ("55-282", "53-315", "2-27"):
        assert key in result.output
    assert "football-data.org PL" in result.output


def test_info_respects_data_dir_override(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PITCHLENS_DATA_DIR", str(tmp_path))
    result = runner.invoke(app, ["info"])
    assert str(tmp_path.resolve()) in result.output
