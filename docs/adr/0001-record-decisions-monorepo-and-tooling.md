# 0001. Record decisions; monorepo and core tooling

- **Status:** Accepted
- **Date:** 2026-10-01
- **Deciders:** Person A, Person B

## Context
Two part-time engineers build a pipeline, an API and a web app that share one data contract. Decisions get forgotten between weekly calls, and a portfolio benefits from visible engineering judgement.

## Decision
We record significant decisions as short ADRs in `docs/adr/`. `docs/SPEC.md` is the source of truth and changes in the same commit. One public monorepo holds `pipeline/`, `api/` (phase 3) and `web/` (phase 3). Python uses **uv** (a workspace, chosen over Poetry for speed and one lockfile), ruff, mypy and pre-commit. The frontend uses **React + Vite** (chosen over Next.js: the site is a static client of a separate API, so server rendering adds nothing). Scheduling is the **pitchlens CLI + GitHub Actions cron** (chosen over Airflow: two jobs a week don't justify an orchestrator).

## Consequences
One clone, one CI and atomic changes across the contract. Tooling is opinionated, and both people must use uv and pre-commit.

## Revisit when
The repo grows past what one CI run handles in under 10 minutes, or a job needs dependencies between more than a handful of steps.
