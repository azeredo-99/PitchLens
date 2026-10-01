# pitchlens (pipeline)

The Python package behind PitchLens: a `pitchlens` CLI that ingests, validates, models and publishes football data.
See `docs/SPEC.md` §10 for the full command list and the phase each command arrives in.

```bash
uv sync                 # from the repo root
uv run pitchlens --help
uv run pitchlens info   # version, data directory, configured competitions
uv run pytest
```
