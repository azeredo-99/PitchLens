# 0002. Hosting on Vercel, Cloud Run and Supabase

- **Status:** Accepted
- **Date:** 2026-10-01 (agreed earlier in planning; recorded here)
- **Deciders:** Person A, Person B

## Context
A public, non-commercial portfolio with a budget of about €0–10 a month needs a static frontend, a small read-only API, a small Postgres database and scheduled jobs.

## Decision
We host the static React build on **Vercel (Hobby)**, the read-only FastAPI service as a Docker image on **Google Cloud Run**, and the serving tables on **Supabase Postgres** (free tier, **separate dev and prod projects**). **GitHub Actions** handles CI, deploys and scheduled jobs. Each has a free tier that fits a non-commercial portfolio, Cloud Run scales to zero and teaches a mainstream cloud without Kubernetes, and Vercel gives a preview URL for every branch.

## Consequences
We accept:
- a short delay on the first API request after the site has been idle
- Vercel's non-commercial and one-member limits (João owns the Vercel project; the repo stays public so everyone's commits deploy)
- Supabase's 500 MB cap and inactivity pause (the twice-weekly forecast job keeps prod awake)

## Revisit when
PitchLens becomes commercial or outgrows the free tiers. Before shutting down we switch to archive mode by exporting the data to static JSON.
