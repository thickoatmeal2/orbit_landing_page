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


