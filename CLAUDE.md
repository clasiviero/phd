# PhD workspace — Maria Clara Cavalcante

## Thesis
**Advanced orbit-based dynamical modeling of dark matter halos, the IMF and Supermassive Black Holes in local galaxies and Euclid gravitational lenses.**

Started September 2026. Current phase: literature review (papers and PhD theses from the orbit-modeling community, mostly the Munich group: Thomas, Mehrgan, Neureiter, de Nicola, Lipka, Hilz).

## Layout
- `literature/papers/`, `literature/theses/` — PDFs. **Local only, git-ignored, never commit them.** They were removed from GitHub history on purpose.
- `references.bib` — master BibTeX file (tracked on GitHub).
- `notes/papers/<key>.md`, `notes/theses/<key>.md` — one note per item, from `notes/_template.md`.
- `notes/reading-log.md` — status of every item in `literature/`.
- `methodology/pipeline.md` — the modeling pipeline by stage, with key references per stage.
- `methodology/theory-reading.md` — textbook theory to study per stage (Binney & Tremaine etc.).
- `code/` — research code (`code/orbits/` has galpy orbit tests).
- `.claude/skills/` — `paper-notes`, `methodology-map`.

## Conventions
- Citation keys: `FirstauthorYEAR` plus a letter when needed (`Neureiter2023a`), matching the PDF name where possible.
- Every equation, number or claim in a note gets a page or section reference to the source. Never fill in equations or chapter numbers from memory; if it isn't in the PDF, mark it `TODO: verify`.
- Pipeline stages (use these exact names in notes): Photometry & deprojection · Kinematics (LOSVDs) · Mass model (stars/IMF, DM halo, SMBH) · Orbit library & Schwarzschild superposition · Regularization & model selection · Lensing + dynamics (Euclid).
- The repo is public (and feeds the GitHub website): notes are fine to publish, but don't paste long verbatim passages from papers.
- Commits carry only the user's name — no Claude co-author lines.
