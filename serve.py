import os, http.server, functools

port = int(os.environ.get("PORT", 8766))
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=os.path.dirname(os.path.abspath(__file__)))
with http.server.HTTPServer(("", port), handler) as httpd:
    print(f"Serving at http://localhost:{port}")
    httpd.serve_forever()
