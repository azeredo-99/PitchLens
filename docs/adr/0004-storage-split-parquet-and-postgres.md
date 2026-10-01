# 0004. Storage split: Parquet/DuckDB vs Postgres

- **Status:** Accepted
- **Date:** 2026-10-01
- **Deciders:** Person A, Person B

## Context
A match has about 3,400 StatsBomb events. Three competitions are hundreds of thousands of events plus 360 frames. Supabase's free tier caps the database at 500 MB, and the website needs only a small, precomputed subset.

## Decision
Full event data lives in **Parquet** files queried with **DuckDB**, on laptops and in CI, and is never deployed. **Postgres** holds only the **serving tables**: shots, per-match and per-competition summaries, pass networks, models, forecasts and notes (`docs/SPEC.md` §9.2). The pipeline's `publish` step is the only writer.

## Consequences
Analysis is fast and free; the database stays a few MB. The API can't answer ad-hoc event-level questions, which is intended: new questions become new precomputed tables.

## Revisit when
The site needs event-level interactivity that precomputation can't cover.
