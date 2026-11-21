# The Illicit Syllabus

**Their syllabi. Your education.**

A small, source-linked archive of university syllabi and published reading lists for independent study. Search by author, title, discipline, course, or institution; inspect source-backed excerpts; save a personal reading list locally; export Markdown.

## Run and deploy

No dependencies or build step. Run `python3 -m http.server 8000` from the repository root, then visit `http://localhost:8000`. The site is GitHub Pages-ready from `main` / root. All paths are relative so it works at `/the-illicit-syllabus/`.

## Design

The bundled artwork uses genuinely brush-textured literary impressionist compositions from the starter prototype, optimized into self-contained SVG wrappers containing the original painted imagery as embedded WebP images. All illustration content is raster-painted artwork, **not** vector line art. Do not substitute stock photos or generic vector elements. Serif editorial typography, chalk/cream paper, muted aubergine, and small mono annotations complete the visual system.

## Sources and scope

The four initial entries are grounded in official MIT OpenCourseWare reading pages, a Lincoln College (University of Oxford) reading list, and Yale Directed Studies' Spring 2025 philosophy syllabus. Every displayable reading has a direct institutional citation and a type label. Initial records are partial excerpts, not complete syllabi. See `docs/data-schema.md` for validation and editorial rules. The source URLs remain external. No institutional affiliation is implied.

## Developer notes

- `index.html`: the static interface, filtering, course details, local browser storage, and Markdown export.
- `data/courses.json`: canonical verified course records.
- `art/*.svg`: optimized painted illustrations embedded as lossily compressed WebP data, preserved in deployable text assets.
- `docs/data-schema.md`: provenance and reading-type policy.
- `AGENTS.md`: repository scope and quality requirements.
- `tests/smoke.py`: local functional smoke tests.

GitHub Pages: in repository **Settings → Pages**, choose **Deploy from a branch**, `main`, `/(root)`. If repository Pages is enabled, the URL is `https://d0lph1nsinthe4ir.github.io/the-illicit-syllabus/`.

## Next

Add more sources only after institutional verification; expand reading-level discovery and user-defined course sequencing; optionally support a full provenance review log.