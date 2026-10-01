# 0005. Notebooks: Jupyter with nbstripout

- **Status:** Accepted
- **Date:** 2026-10-01
- **Deciders:** Claude, on the spec's authority to decide implementation details; either person can overturn this with a new ADR

## Context
Exploration (shot maps, EDA, calibration plots, backtests) happens in notebooks. marimo stores notebooks as reviewable `.py` files; Jupyter is what nearly every football analytics tutorial (mplsoccer, statsbombpy, penaltyblog docs) uses.

## Decision
Use **Jupyter**. Outputs are stripped on commit by the `nbstripout` pre-commit hook so diffs stay readable and data never leaks into git. Notebooks are named `YYYY-MM-DD-topic.ipynb`. Anything that ships moves into `pipeline/` with tests; notebooks are never imported by production code.

## Consequences
Tutorials work unchanged for learners. Reviewers rerun a notebook to see its charts. Figures needed in write-ups are exported deliberately to `docs/writeups/`.

## Revisit when
Notebook reviews become painful enough that marimo's plain-Python format is worth the switch.
