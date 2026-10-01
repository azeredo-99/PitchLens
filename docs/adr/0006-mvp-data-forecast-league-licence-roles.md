# 0006. MVP data, forecast league, licence and roles

- **Status:** Accepted
- **Date:** 2026-10-01
- **Deciders:** Person A, Person B (answered by the team)

## Context
The spec left four choices to the team: which StatsBomb competitions form the MVP, which league the live forecasts follow, the code licence, and who leads which lane.

## Decision
- **MVP competitions (StatsBomb open data):**
  - UEFA Euro 2024 (competition 55, season 282; has 360)
  - UEFA Women's Euro 2025 (53 / 315; has 360)
  - Premier League 2015/16 (2 / 27; full 380-match season)
- **Forecast league:** the **Premier League**, via football-data.org (free tier, code `PL`), with history and closing odds from football-data.co.uk.
- **Licence:** **MIT** for code. Data keeps its own terms (StatsBomb attribution on anything published).
- **Roles:** **Person A (data and models lead) is the repository owner; Person B (product and platform lead) is João.**

## Consequences
- **Premier League 2015/16** gives an honest full season for per-90 tables, and a familiar story in Leicester.
- **The two Euros** give 360 freeze frames for xG v2 and a women's competition.
- **Women's Euro 2025** serves as the held-out generalisation test for xG v1.
- **The Premier League's August–May season** puts phase 4 mid-season.
- **One caveat:** the xG training data mixes eras (2015/16) and genders. The model card must report performance per competition, not just pooled.

## Revisit when
StatsBomb releases a more recent full league season, or the team switches the league they actually follow.
