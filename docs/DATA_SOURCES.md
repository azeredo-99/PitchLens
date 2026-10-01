# Data sources register

Every external data source PitchLens uses, why we use it, its terms, and the attribution we show.
**Rules:**
- No source enters the code without a row here.
- Every row is rechecked before launch and each August.
- Terms change (FBref's advanced data disappeared in January 2026), so the "Last checked" date matters.

**"Verified" means** someone read the current terms on that date. "Planning" means the row reflects research done during planning. A person must read the terms before the source is used in published output.

| Source | Used for | Phase | Terms / licence | Attribution we show | Redistribution | Last checked |
|---|---|---|---|---|---|---|
| **StatsBomb open data** (Hudl) | Events, lineups, 360 freeze frames for the MVP competitions | 0+ | User agreement in the repo: <https://github.com/statsbomb/open-data> (`LICENSE.pdf`) | "Data: StatsBomb open data" + StatsBomb logo on every page and image using it | Only the 2 test fixture matches are committed, with attribution; raw data is downloaded, not mirrored | Planning, 2026-10-01 |
| **football-data.org** | Premier League fixtures and results (code `PL`) | 4 | Free tier, 10 requests/minute; terms at <https://www.football-data.org/> | Per their terms (to verify) | Derived forecasts only; raw responses are not republished | Planning, 2026-10-01 |
| **football-data.co.uk** | Historical PL results + closing odds for training and the bookmaker benchmark | 4 | <https://www.football-data.co.uk/> (see the site's notes and disclaimer) | "Historical results and odds: football-data.co.uk" | CSVs are not committed or redistributed | Planning, 2026-10-01 |

## Configured StatsBomb competitions (ADR 0006)

| Competition | `competition_id` | `season_id` | 360 | Role |
|---|---|---|---|---|
| UEFA Euro 2024 | 55 | 282 | Yes | xG training, xG v2 |
| UEFA Women's Euro 2025 | 53 | 315 | Yes | Held-out xG test, xG v2 |
| Premier League 2015/16 | 2 | 27 | No | xG training, full-season per-90 tables |

## Considered and rejected

| Source | Why not |
|---|---|
| FBref | Advanced (Opta) data removed in January 2026; scraping discouraged |
| Understat, Sofascore, FotMob, WhoScored, Transfermarkt | Scraping only; terms generally prohibit scraping and republishing |

## Possible later additions (need a row and a check before use)

- Wyscout public dataset (Pappalardo et al., 2019): full 2017/18 seasons; open licence with attribution, licence still to be verified.
- API-Football: only if a league is missing (free tier, 100 requests/day).
- Metrica / SkillCorner public tracking samples: tracking sandbox stretch.
