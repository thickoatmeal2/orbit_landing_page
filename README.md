# Orbit Landing Page

Minimal static landing page exported from Figma and adapted to run locally.

## Quick start

Prerequisites: `python3` (macOS ships with Python; ensure it's Python 3.x).

Recommended (mapped) server (preserves Figma runtime/component paths):

```bash
cd /Users/jacob/Desktop/Orbit_landing_page
python3 server.py
open "http://localhost:8000"
```

Alternative (simple static server):

```bash
cd /Users/jacob/Desktop/Orbit_landing_page
python3 -m http.server 8000
open "http://localhost:8000"
```

Optional live reload (install once):

```bash
# npm install -g live-server
live-server --port=3000
```

## What this repo contains

- `index.html` — main HTML file produced by Figma Sites; it references runtime and component bundles.
- `server.py` — small Python server that rewrites virtual asset paths (see below) so the site can load bundled files present in the project root.
- `_index.json`, `ad1dffaeb8d609c7ddd33890a402e4d217e04ca2.css`, `ad1dffaeb8d609c7ddd33890a402e4d217e04ca2.js`, `sites-runtime.*.js` and other assets — static files used by the site.

## How `server.py` helps

Figma-hosted sites sometimes reference assets using virtual paths such as:

- `/_runtimes/<file>`
- `/_components/v2/<file>`
- `/_json/<guid>/_index.json`

`server.py` rewrites these requests to serve the actual files that live at the project root (it maps the basename of the requested path to `/basename`). This avoids 404s when the runtime expects those virtual paths.

If you add more assets that the site requests under paths like `/_assets/` or other virtual folders, update `server.py` to map them to the correct file names.

## Adding content or images

- Place image files in the project root (or a subfolder) and reference them in the HTML as `/my-image.png` or `/images/my-image.png`.
- Edit `index.html` to add sections or content. To avoid runtime overwrites, place your custom static content below the existing `#container` element (the project currently loads a runtime into `#container`).

## Common troubleshooting

- 404s: Open browser DevTools → Network, note the path, and add a mapping in `server.py` if needed.
- Port in use: If `python3 server.py` fails with `Address already in use`, free the port with `lsof -iTCP:8000 -sTCP:LISTEN -n -P` and `kill <PID>` or choose a different port.

## GitHub

Remote repo: `https://github.com/thickoatmeal2/orbit_landing_page.git`

To update README or push changes:

```bash
git add README.md
git commit -m "Add README"
git push
```

## Next steps I can help with

- Add a hero/section (I can insert sample content into `index.html`).
- Add a small script to accept a port argument or environment variable in `server.py`.
- Add CI or a simple `Makefile` for common tasks.

If you want, tell me which of the above to do next, or ask specific questions about any file in the repo.
