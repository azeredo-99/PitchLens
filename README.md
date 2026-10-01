# PitchLens

**An open football analytics lab: our own xG model, match reports anyone can read, and a forecast that publicly keeps score of itself.**

> 🚧 Phase 0: Foundations. Nothing is deployed yet. Follow along in the [interactive roadmap](https://claude.ai/artifact/Urx1KmpVF5bWprfzegkESR) (`roadmap/index.html`).

PitchLens is built by two software engineers learning football data analysis in public. The principle is *show the numbers and show the method*:
- every match page explains itself
- the xG model is ours and is benchmarked against a professional one
- the forecasts publish their own track record, bad weeks included

## Status

| Phase | Outcome | Status |
|---|---|---|
| 0 · Foundations | Repo, CI, first shot map | In progress |
| 1 · Data foundations | One-command dataset | — |
| 2 · First xG model | Model card + write-up #1 | — |
| 3 · App MVP | Public URL | — |
| 4 · Live forecasts | Premier League forecasts scored in public | — |
| 5 · AI match notes | Faithfulness-tested notes | — |
| 6 · Polish and launch | Launch-ready portfolio | — |
| 7 · Video lab (optional) | Tracking data from our own footage | — |

## Run it

Requires [uv](https://docs.astral.sh/uv/). It installs Python 3.12 for you.

```bash
git clone https://github.com/azeredo-99/PitchLens && cd PitchLens
uv sync
uv run pitchlens info
uv run pytest
uv run pre-commit install        # once, so checks run on every commit
```

For notebooks: `uv sync --group notebooks && uv run jupyter lab`. Start with [`notebooks/README.md`](notebooks/README.md).

## Repository map

| Path | What |
|---|---|
| `docs/SPEC.md` | The project specification: the source of truth |
| `docs/adr/` | Architecture decision records |
| `docs/DATA_SOURCES.md` | Every data source, its terms and attribution |
| `roadmap/index.html` | Interactive learning/build roadmap |
| `pipeline/` | Python package and `pitchlens` CLI |
| `notebooks/` | Exploration (outputs stripped) |
| `CLAUDE.md` | Conventions for humans and Claude Code |

## Team

- **Person A**: data and models lead.
- **Person B (João)**: product and platform lead.

## Data and licence

Code is [MIT](LICENSE). Data keeps its own terms: PitchLens uses **StatsBomb open data**, which must be credited with the StatsBomb logo on anything published. See [`docs/DATA_SOURCES.md`](docs/DATA_SOURCES.md).
