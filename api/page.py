"""On-demand asset pages for languages whose long tail is not written as static files.

Vercel serves static files first; vercel.json rewrites /<lang>/<asset>/ to this function only when no
file exists. It renders the page with the same code and data as scripts/build.py (bundled with the
deployment), so the HTML is identical to a static page. The CDN caches each page for a day
(the cache is reset by every deploy, so asset versions always match).
"""
import json
import os
import re
import sys
import urllib.request
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import build  # noqa: E402  (loads data once per cold start, ~0.6 s)

LANGS = {l for l in build.ORDER if l not in build.FULL}
_VER = {}
_404 = {}


def ver(host):
    if not _VER:
        v = None
        for p in (os.path.join(ROOT, 'dist/assets/ver.json'),):
            if os.path.isfile(p):
                v = json.load(open(p))
        if v is None and host:
            try:
                with urllib.request.urlopen(f'https://{host}/assets/ver.json', timeout=3) as r:
                    v = json.loads(r.read())
            except Exception:
                v = None
        if v is None:
            return dict(css='0', js='0', ref='0', index='0')   # not cached: retry on the next request
        _VER.update(v)
    return _VER


def not_found(host):
    if 'h' not in _404:
        try:
            with urllib.request.urlopen(f'https://{host}/404.html', timeout=3) as r:
                _404['h'] = r.read()
        except Exception:
            return b'<!doctype html><meta charset="utf-8"><title>Not found</title><p>Page not found. <a href="/">WhatIfStack</a></p>'
    return _404['h']


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        lang, aid = (q.get('l') or [''])[0], (q.get('a') or [''])[0].lower()
        host = self.headers.get('x-forwarded-host') or self.headers.get('host') or 'whatifstack.com'
        if lang in LANGS and re.fullmatch(r'[a-z0-9][a-z0-9.\-]*', aid) and aid in build.A:
            try:
                build.set_numfmt(lang)
                body = build.asset(aid, lang, ver(host)).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Cache-Control', 'public, max-age=0, must-revalidate')
                self.send_header('CDN-Cache-Control', 'public, s-maxage=86400, stale-while-revalidate=86400')
                self.send_header('X-Rendered', 'on-demand')
                self.end_headers()
                self.wfile.write(body)
                return
            except Exception as e:  # render bug → let the visitor reach the English page instead of an error
                print('render failed', lang, aid, repr(e))
                self.send_response(302)
                self.send_header('Location', build.url('en', aid))
                self.send_header('Cache-Control', 'no-store')
                self.end_headers()
                return
        body = not_found(host)
        self.send_response(404)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('CDN-Cache-Control', 'public, s-maxage=3600')
        self.end_headers()
        self.wfile.write(body)

    def do_HEAD(self):
        self.do_GET()
