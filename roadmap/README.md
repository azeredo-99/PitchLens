# PitchLens interactive roadmap

`index.html` is the source of the interactive learning/build roadmap, published as a claude.ai artifact:
<https://claude.ai/artifact/Urx1KmpVF5bWprfzegkESR>

- 86 topics across phases 0–7, split into engineering and football-analytics tracks.
- Each topic has: why it matters, prerequisites, what to learn, practical task, files, tests, done-when, PitchLens docs, official resources and an owner (A, B or both).
- **Map** view: the phase spine. **Next up** view: what each person can start now.
- Progress is shared through the artifact's database (it needs edit access on the artifact). Opened as a local file, it falls back to this browser's storage.
- Deep links: `#<topic-id>` (e.g. `#p0-shotmap`), `#track-xg`, `#phase-3`, `#next`.

Keep it in sync with `docs/SPEC.md`: when phases, topics or ownership change, edit the `TOPICS` / `PHASES` / `TRACKS` data in `index.html` and republish.
The file has no `<html>`/`<head>` wrapper because the artifact host adds one; browsers still render it when opened directly.
