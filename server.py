#!/usr/bin/env python3
"""
Simple static file server that maps expected site paths
to the actual files present in the project root.

Place this file in the project root and run:
  python3 server.py

It listens on port 8000 by default.
"""
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib

PORT = 8000


class MappedRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Rewrite a few known virtual paths to files that exist at project root.
        path = urllib.parse.unquote(self.path)

        # If the site requests one of the special runtime/component paths,
        # map to the file with the same basename located at the server root.
        # Map common Wix/hosted site virtual paths to local files by basename.
        if path.startswith(("/_runtimes/", "/_components/v2/", "/_components/", "/_assets/")):
            basename = path.split("/")[-1]
            if basename:
                self.path = "/" + basename

        # Many deployments request an _index.json under a GUID folder.
        # Serve the repository's `_index.json` for any such request.
        elif path.startswith("/_json/") and path.endswith("/_index.json"):
            self.path = "/_index.json"

        # Fall back to default behavior (serves files relative to cwd).
        return super().do_GET()


def run(server_class=HTTPServer, handler_class=MappedRequestHandler):
    server_address = ("", PORT)
    httpd = server_class(server_address, handler_class)
    sa = httpd.socket.getsockname()
    print(f"Serving HTTP on {sa[0]} port {sa[1]} (http://localhost:{PORT}/) ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, exiting.')
        httpd.server_close()


if __name__ == '__main__':
    run()
