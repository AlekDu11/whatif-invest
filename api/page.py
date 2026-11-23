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
from urllib.parse import parse_qs, unquote, urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import build  # noqa: E402  (loads data once per cold start, ~0.6 s)

LANGS = set(build.ORDER)   # uk/en too: since 2026-11-22 their incomplete (noindex) pages are not static files either
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
        lang, aid = (q.get('l') or [''])[0], unquote((q.get('a') or [''])[0]).lower()
        host = self.headers.get('x-forwarded-host') or self.headers.get('host') or 'whatifstack.com'
        lc, pg = (q.get('lc') or [None])[0], (q.get('p') or [''])[0]
        if lang in LANGS and lc is not None:   # world company rankings past the static pages (owner 2026-11-24: every company, not only the top 300)
            tab = {s or 'mcap': k for k, s in build.LC_TABS}.get(lc)
            if tab and pg.isdigit() and 1 < int(pg) <= build.lc_np(tab, None):
                try:
                    build.set_numfmt(lang)
                    _, html = build.lc_page(lang, tab, None, ver(host), int(pg))
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.send_header('Cache-Control', 'public, max-age=0, must-revalidate')
                    self.send_header('CDN-Cache-Control', 'public, s-maxage=86400, stale-while-revalidate=86400')
                    self.send_header('X-Rendered', 'on-demand')
                    self.end_headers()
                    self.wfile.write(html.encode('utf-8'))
                    return
                except Exception as e:
                    print('lc render failed', lang, lc, pg, repr(e))
            body = not_found(host)
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(body)
            return
        if lang in LANGS and 0 < len(aid) <= 80 and '/' not in aid and aid in build.A:   # ids can be non-Latin (Chinese memecoins)
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
        _m = build.market['assets'].get(aid) if lang in LANGS else None
        if _m:   # dropped asset (owner 2026-11-23: no-exchange coins, stale, delisted) → its list page, never a 404
            hub = {v: k for k, v in build.HUBS.items()}.get(_m.get('cat'), 'crypto')
            self.send_response(301)
            self.send_header('Location', build.url(lang, hub))
            self.send_header('CDN-Cache-Control', 'public, s-maxage=86400')
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
