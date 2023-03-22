#!/usr/bin/env python3
# encoding: utf-8
"""Use instead of `python3 -m http.server` when you need CORS"""

from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='static/smartlab-initiative-viewconf', **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Content-Type', 'text/plain')
        return super(CORSRequestHandler, self).end_headers()


httpd = HTTPServer(('localhost', 8000), CORSRequestHandler)
print('Running viewconf server on localhost:8000')
httpd.serve_forever()
