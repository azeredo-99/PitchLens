"""PitchLens: an open football analytics lab."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pitchlens")
except PackageNotFoundError:  # pragma: no cover - only when running from a source tree
    __version__ = "0.0.0+unknown"

__all__ = ["__version__"]
