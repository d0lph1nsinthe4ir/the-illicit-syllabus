# Source-first data schema

The canonical archive lives in `data/courses.json`. Each record supplies:

- `id`, `institution`, `country`, `discipline`, `course`, `term`, `description`: grounded catalog metadata.
- `source`, `sourceType`: official institutional URL and document type.
- `instructor` when documented; `verifiedAt` is the date last manually checked.
- `sourceLocation`, `coverage`: what on the source page was inspected and how partial the transcription is.
- `readingSource` (optional): a more precise source for reading citations (e.g. a weekly syllabus PDF).
- `status`: source-linked, not a claim that the full course has been transcribed.
- `readings`: each entry has a sourced `title`, `author`, `status`, `note`, and exact `source` URL. Distinguish required, assigned, preparatory, and course texts rather than flattening them.

## Editorial verification

Use the official published institutional syllabus or reading list. Check each reading against the exact linked page or document; do not infer inclusion from the author's reputation or a course's general subject. Preserve passage-level limitations (e.g. selections only). Do not label a preparatory recommendation as a required course assignment. Record the check date, and do not assume a currently inaccessible source still verifies old entries.

The HTML contains a generated, identically sourced `FALLBACK` snapshot for `file://` and offline viewing; update that snapshot whenever `data/courses.json` changes. Browser-local saved lists do not leave the device.