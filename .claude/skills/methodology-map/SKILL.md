---
name: methodology-map
description: Rebuild methodology/pipeline.md and methodology/theory-reading.md from all notes in notes/. Use after new notes are written or when the user asks for the methodology overview, the key references per stage, or what theory to study.
---

# methodology-map

1. Read every note in `notes/papers/` and `notes/theses/` (frontmatter `stages:` plus the body).
2. For each stage in `methodology/pipeline.md`:
   - **Key references:** the items tagged with that stage, oldest first, each with a one-line contribution and a link to its note (`[Thomas2004](../notes/papers/Thomas2004.md)`).
   - **Theses chapters:** the thesis chapters covering the stage.
   - **Open questions:** gathered from the notes' "My questions" and from disagreements between items.
   Keep each stage's one-line description; keep anything the user wrote by hand.
3. Update `methodology/theory-reading.md` from the notes' "Theory to look up" sections: add topics, fill "Cited by", and fill "Where (book §)" only with sections a note records as cited in a source. Leave the rest blank.
4. Flag gaps: stages with fewer than two key references, and cited works that several notes recommend but that aren't in `literature/` yet.
5. Report what changed in a few lines.

Only use what is in the notes; don't add references or book sections from memory.
