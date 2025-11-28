# Orbit Landing Page

This repository contains a static landing page exported from Figma and adapted to run locally.

## Run in the browser

Prerequisite: `python3` installed.

Recommended (uses the provided mapped server which preserves virtual asset paths):

```bash
# run the mapped server (default port 8000)
python3 server.py

# then open in your browser:
http://localhost:8000
```

Alternative (simple static server):

```bash
# serve the current directory on port 8000
python3 -m http.server 8000

# then open:
http://localhost:8000
```

Optional live reload (install once):

```bash
# npm install -g live-server
live-server --port=3000
```

## What to expect

- `index.html` is the main entry point and bootstraps the site runtime.
- `server.py` rewrites certain virtual request paths (used by exported runtimes) so the site can load local asset files without 404s.

If a resource still 404s, open DevTools → Network, note the failing request path, and add a mapping in `server.py` or place the file with the expected basename in the project root.

If you need the server to run on a different port or want the README expanded with development steps, tell me which option you prefer.

Short: run `python3 server.py` and open `http://localhost:8000` in a browser.
