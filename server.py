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
import os
import argparse


def get_port(default=8000):
    # Priority: command-line arg > PORT env var > default
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-p", "--port", type=int, help="port to listen on")
    args, _ = parser.parse_known_args()
    if args.port:
        return args.port
    env_port = os.environ.get("PORT")
    if env_port and env_port.isdigit():
        return int(env_port)
    return default


class MappedRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Rewrite a few known virtual paths to files that exist at project root.
        path = urllib.parse.unquote(self.path)

        # If the site requests one of the special runtime/component paths,
        # map virtual basenames to actual file names in this repo.
        # This mapping lets us give friendly filenames while still
        # serving requests for original hashed names the runtime may use.
        mapping = {
            # old hashed runtime -> friendly name
            'sites-runtime.4088aa4f2abed8aab88a6ac77563105a8e8bc38d897b4a5cf5373dd8c43dfa78.js': 'runtime.js',
            # old hashed component bundle -> friendly name
            'ad1dffaeb8d609c7ddd33890a402e4d217e04ca2.js': 'components.js',
            'ad1dffaeb8d609c7ddd33890a402e4d217e04ca2.css': 'components.css'
        }

        if path.startswith(("/_runtimes/", "/_components/v2/", "/_components/", "/_assets/")):
            basename = path.split("/")[-1]
            if basename:
                # if the runtime requests the original hashed filename, serve
                # the renamed friendly file instead (fallback to basename).
                target = mapping.get(basename, basename)
                self.path = "/" + target

        # Many deployments request an _index.json under a GUID folder.
        # Serve the repository's `_index.json` for any such request.
        elif path.startswith("/_json/") and path.endswith("/_index.json"):
            self.path = "/_index.json"

        # Fall back to default behavior (serves files relative to cwd).
        return super().do_GET()


def run(server_class=HTTPServer, handler_class=MappedRequestHandler, port=None):
    if port is None:
        port = get_port()
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    sa = httpd.socket.getsockname()
    print(f"Serving HTTP on {sa[0]} port {sa[1]} (http://localhost:{port}/) ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, exiting.')
        httpd.server_close()


if __name__ == '__main__':
    # Allow override via env or command-line
    run()
