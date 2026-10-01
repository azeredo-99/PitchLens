# 0007. Scope and sequencing changes (spec v1.1)

- **Status:** Accepted
- **Date:** 2026-10-01
- **Deciders:** Claude (proposed and implemented per the spec's "improve weak decisions" rule); either person can overturn any item with a new ADR

## Context
A review of the consolidated spec found tools introduced before they were needed, a duplicated chart library, an overloaded phase 3, an undecided phase 6, underspecified xG methodology, and a few open implementation questions.

## Decision
1. **Docker Compose moves from phase 0 to phase 2.** Nothing uses Postgres before the serving schema exists.
2. **Observable Plot is removed.** Every web chart is custom (pitch, xG step line, network, forecast bars), so D3 alone covers them. Notebooks keep matplotlib/mplsoccer.
3. **Phase 3 is split** into **3a** (API, types, a bare match list deployed end to end) and **3b** (D3 match page, competition page, smoke test).
4. **Phase 6 builds xG v2 (360).** Player percentile pages move to the post-launch backlog. xG v2 extends write-up #1 with data we already have; player pages are only honest for the single full season we hold.
5. **xG methodology:**
   - Penalties are excluded from training and get a constant xG.
   - Own goals are not shots.
   - Train/test split by match.
   - Women's Euro 2025 is a held-out competition.
   - The benchmark against StatsBomb xG uses identical shots.
6. **Forecast methodology:**
   - Look-ahead-free backtests.
   - RPS as the primary score.
   - Bookmaker benchmark from closing odds with the overround removed.
7. **Elo baseline: Person B** (the work-split crossover). **Dixon-Coles and the backtest: Person A.** This resolves a contradiction in the old plan.
8. **Vercel previews call the production API.** It's read-only and public, so no second Cloud Run service is needed.
9. **The static core is published by a manual `publish-core.yml` workflow**, never from a laptop.
10. **Claude implements scaffolding and infrastructure; the analytical core is written by Person A and Person B**, with Claude preparing exercise briefs and reviewing (spec §27).

## Consequences
Phase 0 is lighter, phase 3 has a mid-phase deployable checkpoint, the frontend has one fewer library to learn, and the xG write-up rests on stated, testable methodology.

## Revisit when
Any item proves wrong in practice. Overturn it with a new ADR rather than editing this one.
