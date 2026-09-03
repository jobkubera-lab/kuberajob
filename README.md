# Kubera Relocation — Serbia & Montenegro

**Status:** Active public relocation website / maintained static site.

Kubera Relocation is a Russian-language website for people comparing a move to **Serbia or Montenegro**. The current front page provides a short self-assessment, budget/readiness guidance, a preparation checklist and a contact path for follow-up.

> Information on the site is preliminary guidance, not a legal opinion or a guarantee of residence status. Current requirements must be checked against official sources before action.

## Public site

Repository metadata points to:

- https://kuberajob.vercel.app/

The repository also contains a GitHub Pages workflow for static deployment/preview. Before changing DNS or deployment settings, verify which host is intended to remain canonical.

## Audience

- Russian-speaking people considering relocation to Serbia or Montenegro;
- people comparing budget, timing, work/business and practical relocation needs;
- clients who want a structured first brief before speaking to a consultant.

## Technology

- static HTML;
- CSS;
- vanilla JavaScript;
- Vercel routing through `vercel.json`;
- GitHub Actions / GitHub Pages static deployment workflow;
- Python only for a historical webhook diagnostic script, not for the website runtime.

## Repository structure

| Path | Purpose |
| --- | --- |
| `index.html` | Current main Serbia / Montenegro relocation assessment page |
| `relocation/` | Relocation UI assets and a second copy/variant of the assessment page |
| `assets/` | Legacy/static shared assets |
| `ru/` | Older Russian-language service, pricing, case and contact pages |
| `public/` | Files exposed explicitly by the current Vercel routing for SEO endpoints |
| `.github/workflows/static.yml` | GitHub Pages static deployment workflow |
| `legacy-index.html` | Unreferenced KUBERA LAB archive placeholder; pending archive/delete decision |
| `test_webhook_integration.py` | Historical Lindy webhook diagnostic; not part of current production runtime |
| `vercel.json` | Current Vercel routing configuration |

## Run locally

No build step is required.

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

This serves the repository as static files and is sufficient for checking the main page, CSS and JavaScript locally.

## Deployment

### Vercel

`vercel.json` is present and routes `/robots.txt` and `/sitemap.xml` through `public/`, then falls back to `/index.html`.

Important maintenance note: the current catch-all route means nested pages such as `/ru/*` and `/relocation/*` may not be independently reachable through Vercel even though the files exist in the repository. That routing should be changed only after deciding which nested pages are intended to remain public.

### GitHub Pages

`.github/workflows/static.yml` deploys the repository as static content on pushes to `main`.

## SEO files

Both the repository root and `public/` contain `robots.txt`. Sitemap files are kept in the same two locations so both deployment paths can expose the same canonical URL.

At present the sitemap lists only the canonical root page because the existing Vercel catch-all does not guarantee independent access to the older `/ru/*` pages.

## Webhook diagnostic

`test_webhook_integration.py` is a historical diagnostic script created to demonstrate a GitHub → Lindy webhook payload. No current workflow in `.github/workflows/` invokes it, so it is **not production website logic**.

Recommended cleanup after approval: move it to `tests/` or `archive/` rather than leave it in the repository root.

## Pending cleanup decisions

Two changes are intentionally not made without owner approval:

1. `legacy-index.html` — it is not referenced anywhere in the current repository. It can be deleted or moved to `archive/legacy-index.html`.
2. `test_webhook_integration.py` — it can be moved to `tests/test_webhook_integration.py` as a historical diagnostic.

The Vercel routing should also be reviewed before exposing the existing `/ru/*` pages in a sitemap.

## License

No open-source `LICENSE` file is currently declared in this repository. Until a license is explicitly added, the repository should not be treated as granting open-source reuse rights.
