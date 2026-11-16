# Repository Guidelines

## Project Structure

This repository contains independent static showcases for B-CUBE designathon projects. Each `out_spas/<project-slug>/` directory contains an `index.html`, a project `README.md` with source-slide summaries, a `DESIGN_RULE.md`, and an `assets/` directory for images. `designton_pdfs/` holds source PDFs and `bcube.designtons.csv`; some source PDFs are linked externally in the CSV. Consult `DESIGN.md` for the complete content and implementation requirements.

## Development Commands

No build step or dependency installation is required. Open an `index.html` directly, or serve the repository root locally:

```sh
python3 -m http.server 8000
```

Visit `http://localhost:8000/out_spas/` to select a project, or navigate directly to a project directory. CDN-hosted fonts need an internet connection; fallback fonts are used otherwise.

## Coding Style and Content

Keep each showcase a standalone HTML page and follow its `README.md` and `DESIGN_RULE.md`. Match the surrounding file's formatting; there is no repository-wide indentation rule, formatter, or linter. Use lowercase, hyphen-separated project directory names, such as `masil-on`, and descriptive fragment IDs. Store images in the project's `assets/` directory and reference them with relative paths; do not embed image data in HTML.

Use semantic HTML, meaningful image alt text, responsive layouts, and readable Korean copy consistent with the source materials. Navigation should link to fragments within the page. These are explanatory showcases: do not implement backend-dependent features or persistent storage.

## Testing Guidelines

There is no automated test suite or coverage requirement. For each changed page, open it locally and check desktop and mobile layouts, images, fragment links, and text against the project documents and source deck. Check keyboard navigation and reduced-motion behavior where applicable. Report the checks performed in the pull request.

## Commits and Pull Requests

Recent commits use concise Conventional Commit-style subjects, for example `feat(hyodon): add project showcase` and `docs: describe project showcases`. Use an appropriate type and optional project scope. Pull requests should describe the affected projects and changes, link relevant issues when available, and include screenshots for visual changes. Note manual validation and any unavailable source materials.
