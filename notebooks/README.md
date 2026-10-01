# Notebooks

Exploration lives here; anything that ships moves into `pipeline/` with tests (ADR 0005).

- **Naming:** `YYYY-MM-DD-topic.ipynb`
- **Outputs:** stripped automatically on commit (nbstripout); export figures you need for write-ups to `docs/writeups/`.
- **Setup:** `uv sync --group notebooks`, then `uv run jupyter lab`.

---

## Exercise 0.1: Your first shot map (Person A · phase 0)

Roadmap topic: `p0-shotmap`. Prerequisites: `p0-coords` (pitch coordinates), `p0-notebook`.

**Goal:** draw both teams' shots for one Euro 2024 match, sized by StatsBomb xG, with goals highlighted and StatsBomb attribution, and explain the match's biggest chance.

**Inputs:** StatsBomb open data, Euro 2024 = competition `55`, season `282`. No credentials needed.

**Steps (try each yourself before looking anything up):**
1. List the Euro 2024 matches with `statsbombpy` and pick one you watched.
2. Load its events and keep only shots. Look at the columns: which ones hold location, xG, outcome and body part?
3. Check the coordinate system against ADR 0003: are penalties near (108, 40)? Which direction does each team attack?
4. Draw the shots on an mplsoccer `VerticalPitch` (half pitch). Scale marker **area** (not radius) with xG. Make goals visually distinct by more than colour alone.
5. One chart per team, or both on one chart? Decide, and say why in a markdown cell.
6. Add the text “Data: StatsBomb open data”.
7. Compare each team's goals with its total xG and write three sentences about the gap.

**Hints (only if stuck):**
- `sb.competitions()`, `sb.matches(competition_id=…, season_id=…)`, `sb.events(match_id=…)`.
- StatsBomb puts `location` as a list `[x, y]`; you'll need to split it.
- mplsoccer's gallery has a shot-map example; read it after your first attempt.

**Acceptance (B reviews):**
- [ ] Shots point at the correct goal for both teams
- [ ] Marker area is proportional to xG; goals are distinguishable without colour
- [ ] Attribution visible on the figure
- [ ] Biggest chance named with its xG and minute
- [ ] Notebook committed with outputs stripped

When done, tick `p0-shotmap` in the roadmap.
