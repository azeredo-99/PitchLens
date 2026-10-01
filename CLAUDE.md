# CLAUDE.md: working conventions for PitchLens

Read `docs/SPEC.md` first. It is the source of truth. Decisions live in `docs/adr/`.

## Who writes what (SPEC §27)
- Claude implements scaffolding: tooling, CI/CD, CLI plumbing, I/O and caching, migrations, API boilerplate, deploy workflows, test scaffolding, docs upkeep.
- Person A and Person B write the analytical core: features, xG and forecast models, evaluation and its interpretation, notebooks, write-ups, model cards. Claude prepares an exercise brief (goal, inputs, hints, acceptance tests) and reviews.
- Claude commits directly to its designated `claude/…` branch; the repository owner merges to `main`.

## Hard rules
- **LLMs describe numbers; they never produce them.** No generated statistic, xG value, result or player number. AI notes must pass the faithfulness test (SPEC §13).
- **Coordinates (ADR 0003):** StatsBomb 120 × 80, origin top-left, goal centre (120, 40), posts at y = 36 and 44, acting team attacks left → right. Convert once at staging; physical distances in metres.
- **Storage (ADR 0004):** events → Parquet/DuckDB; only shots and summary tables → Postgres.
- **Data:** only sources listed in `docs/DATA_SOURCES.md`; no scraping where terms forbid it; StatsBomb attribution + logo on anything published.
- **Forecasts:** insert-only, `issued_at < kickoff`, no look-ahead in backtests.
- **Secrets:** never in code, notebooks or the browser. `.env` is gitignored.

## Commands
```bash
uv sync                              # install (add --group notebooks for Jupyter + football libs)
uv run pitchlens --help              # pipeline CLI
uv run pytest                        # tests
uv run ruff check && uv run ruff format --check && uv run mypy
uv run pre-commit run --all-files    # everything CI checks
```

## Code style
- Python 3.12, uv workspace (`pipeline/` now; `api/` from phase 3), `src/` layout, mypy strict, ruff (line length 100).
- Tests catch silently wrong numbers: hand-worked cases for geometry and metrics, Hypothesis for invariants, pandera contracts for data.
- Notebooks: `notebooks/YYYY-MM-DD-topic.ipynb`, outputs stripped, never imported by production code.
- Commit titles: Conventional Commits (`feat(pipeline): …`).

## When something changes
Update `docs/SPEC.md` in the same commit; add an ADR for a changed decision; update `roadmap/index.html` (TOPICS/PHASES) if phases, topics or ownership change.
