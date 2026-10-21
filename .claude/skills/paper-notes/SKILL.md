---
name: paper-notes
description: Read a paper or PhD thesis PDF from literature/ and write a structured note in notes/, add its BibTeX entry and update the reading log. Use when the user asks to read, summarize, take notes on or process a paper or thesis.
---

# paper-notes

Input: a citation key or PDF name (e.g. `Thomas2004`), optionally a chapter range for theses.

1. Find the PDF in `literature/papers/` or `literature/theses/` and its row in `notes/reading-log.md`.
2. Read it with the Read tool, in page ranges of at most 20 pages. For a thesis, do one chapter per run unless asked otherwise; read the table of contents first.
3. Copy `notes/_template.md` to `notes/papers/<key>.md` (or `notes/theses/<key>.md`; for a thesis append each chapter as its own section) and fill every section.
   - Tag `stages:` with the pipeline stage names from `CLAUDE.md`.
   - Every equation, number and claim gets a page/section/equation reference. Write equations in LaTeX.
   - Paraphrase; no long verbatim passages (the repo is public).
   - Under "Theory to look up", record textbook topics the item uses and any book sections it cites explicitly.
   - Under "References to follow up", list the cited works that matter most for the pipeline, with one line on why.
4. Add a BibTeX entry to `references.bib` with key `<key>`. Build it from the title page (authors, title, journal, volume, pages, year, DOI/arXiv). Mark anything you could not read off the PDF with `% TODO: verify on ADS`. Don't duplicate existing keys.
5. Update the item's row in `notes/reading-log.md` (status `notes done`, link to the note; for theses, the chapters done).
6. Report in 3–5 lines: what the item does, its stages, and the 2–3 references most worth reading next.

Never invent content that isn't in the PDF. If something is unclear, put it under "My questions" or mark it `TODO: verify`.
