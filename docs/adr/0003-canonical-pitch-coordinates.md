# 0003. Canonical pitch coordinates

- **Status:** Accepted
- **Date:** 2026-10-01
- **Deciders:** Person A, Person B

## Context
Coordinate bugs (flipped axes, wrong attacking direction, mixed units) are the classic silent error in football analytics. StatsBomb uses a 120 × 80 pitch with the origin top-left, whatever the real pitch size, so its units are **not** real yards. Video tracking (phase 7) produces real metres.

## Decision
The canonical PitchLens frame is **StatsBomb's**:
- x runs 0 → 120 towards the opponent's goal, and y runs 0 → 80 from top to bottom
- the goal centre is at (120, 40) and the posts are at y = 36 and y = 44
- events are oriented so the acting team attacks left → right

Every source converts into this frame **once, at staging time**, and nothing downstream converts again. Shot distance and angle are computed in this frame and documented as "StatsBomb units". **Real-world quantities** (distance covered, speed, video position error) are computed **in metres before** conversion. Charts flip axes only at render time, through one tested scaling function.

## Consequences
StatsBomb data needs no conversion, and mplsoccer's `statsbomb` pitch type works directly. Other sources need one tested converter each. Distances in model features aren't true metres; model cards say so.

## Revisit when
We add a primary source whose native frame we'd rather keep (unlikely before tracking data).
