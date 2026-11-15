"""Generate the static whatif.invest site into ./whatif/.

Reads data/assets.json and data/prices.json, writes one calculator page per
asset per language plus the two home pages, a sitemap and the shared assets.
Run: python3 scripts/build.py
"""
import calendar, hashlib, html, json, os, shutil
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'whatif')
BASE = '/whatif'                      # URL path the site lives under
SITE = 'https://mytimebox.app'        # canonical origin
LANGS = ['uk', 'en']
AMOUNT = 10

assets = json.load(open(os.path.join(ROOT, 'data/assets.json'), encoding='utf-8'))
pdata = json.load(open(os.path.join(ROOT, 'data/prices.json'), encoding='utf-8'))
PR = pdata['assets']
assets = [a for a in assets if a['id'] in PR]
AM = {a['id']: a for a in assets}
UPDATED = pdata['updated']
END = UPDATED[:7]
END_DAY = int(UPDATED[8:10])

# ---------- math (mirrors src/app.js) ----------
def ym2i(s):
    y, m = map(int, s.split('-'))
    return y * 12 + m - 1

def i2ym(i):
    return f"{i // 12}-{i % 12 + 1:02d}"

def per_month(i):
    days = calendar.monthrange(i // 12, i % 12 + 1)[1]
    return END_DAY if i2ym(i) == END else days

def simulate(aid, start_i, amt=AMOUNT):
    P = PR[aid]
    s0, e = ym2i(P['start']), ym2i(P['end'])
    frm = max(start_i, s0)
    units = inv = 0.0
    for i in range(frm, e + 1):
        c = amt * per_month(i)
        units += c / P['p'][i - s0]
        inv += c
    val = units * P['p'][e - s0]
    return dict(inv=inv, val=val, roi=val / inv - 1 if inv else 0, frm=frm, units=units)

# ---------- formatting ----------
MON = {'uk': ['січ', 'лют', 'бер', 'кві', 'тра', 'чер', 'лип', 'сер', 'вер', 'жов', 'лис', 'гру'],
       'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']}
MON_GEN = ['січня', 'лютого', 'березня', 'квітня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']
MON_FULL = list(calendar.month_name)[1:]

def mlabel(ym, lang, long=False):
    y, m = map(int, ym.split('-'))
    if long:
        return f"{MON_GEN[m-1]} {y}" if lang == 'uk' else f"{MON_FULL[m-1]} {y}"
    return f"{MON[lang][m-1]} {y}"

def usd(v):
    a = abs(v)
    s = f"{a/1e6:.2f}M" if a >= 1e6 else f"{a:,.0f}"
    return ('−$' if v < 0 else '$') + s

def pct(p):
    s = f"{abs(p*100):,.0f}" if abs(p) >= 10 else f"{abs(p*100):,.1f}"
    return ('+' if p >= 0 else '−') + s + '%'

def nm(a, lang):
    return a['name'][lang]

def esc(s):
    return html.escape(s, quote=True)

# ---------- UI labels (same keys as T in app.js; prefilled for crawlers) ----------
L = {
 'uk': dict(amount='Сума', freq='Як часто', daily='Щодня', weekly='Щотижня', monthly='Щомісяця', since='Починаючи з',
            assets='Активи на графіку (до 10)', chartTitle='Вартість портфеля в часі', log='Лог. шкала', copy='Копіювати',
            home='Усі активи', allassets='Калькулятор для кожного активу', cats={'crypto': 'Криптовалюти', 'stock': 'Акції', 'etf': 'ETF та індекси', 'metal': 'Метали'},
            faq='Часті питання', period='Період', invested='Вкладено', now='Зараз', result='Результат',
            disclaimer='Це не інвестиційна порада. Минулі результати не гарантують майбутніх. Розрахунки без комісій, податків і дивідендів.',
            more='Більше інструментів', by='Проєкт'),
 'en': dict(amount='Amount', freq='How often', daily='Daily', weekly='Weekly', monthly='Monthly', since='Starting from',
            assets='Assets on the chart (up to 10)', chartTitle='Portfolio value over time', log='Log scale', copy='Copy',
            home='All assets', allassets='A calculator for every asset', cats={'crypto': 'Crypto', 'stock': 'Stocks', 'etf': 'ETFs & indices', 'metal': 'Metals'},
            faq='FAQ', period='Period', invested='Invested', now='Now', result='Result',
            disclaimer='Not investment advice. Past performance does not guarantee future results. Calculations exclude fees, taxes and dividends.',
            more='More tools', by='A project by'),
}

def url(lang, aid=None):
    p = BASE + ('/en' if lang == 'en' else '') + '/'
    return p + (aid + '/' if aid else '')

# ---------- shared assets ----------
def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(content)

def hashed(content):
    return hashlib.md5(content.encode()).hexdigest()[:8]

def calc_markup(lang):
    l = L[lang]
    return f"""
  <div class="card">
    <div class="controls">
      <div><label class="f" data-t="amount">{l['amount']}</label>
        <div class="inp"><span>$</span><input id="amt" type="number" min="1" step="1" value="{AMOUNT}" aria-label="{l['amount']}"></div></div>
      <div><label class="f" data-t="freq">{l['freq']}</label>
        <div class="seg" id="freq"><button data-v="d" class="on" data-t="daily">{l['daily']}</button><button data-v="w" data-t="weekly">{l['weekly']}</button><button data-v="m" data-t="monthly">{l['monthly']}</button></div></div>
      <div><label class="f" data-t="since">{l['since']}</label>
        <div class="inp"><select id="since" aria-label="{l['since']}"></select></div></div>
    </div>
    <label class="f" data-t="assets">{l['assets']}</label>
    <div class="assets" id="assets"></div>
    <div class="picker"><div class="pickhead"><div class="inp search"><span>⌕</span><input id="q" type="search" autocomplete="off"></div><div class="cats" id="cats"></div></div><div class="pool" id="pool"></div></div>
  </div>
  <div class="hero" id="hero"></div>
  <div class="card chartcard">
    <div class="charthead"><h2 class="h3" data-t="chartTitle">{l['chartTitle']}</h2><button class="toggle" id="logBtn" data-t="log">{l['log']}</button></div>
    <div id="chart"></div><div class="tip" id="tip"></div>
  </div>
  <div class="card" style="margin-top:14px">
    <div class="tablewrap"><table id="tbl"></table></div>
    <div class="share"><p id="shareText"></p><button class="btn" id="copyBtn" data-t="copy">{l['copy']}</button></div>
  </div>
  <div class="card" style="margin-top:14px">
    <div class="charthead"><h2 class="h3" id="lbTitle"></h2><span class="muted" id="lbSub"></span></div>
    <div class="lb" id="lb"></div>
  </div>"""

def links_grid(lang, current=None):
    l = L[lang]
    out = [f'<section class="links"><h2>{l["allassets"]}</h2>']
    for c in ['crypto', 'stock', 'etf', 'metal']:
        items = [a for a in assets if a['cat'] == c]
        out.append(f'<h3>{l["cats"][c]}</h3><div class="linkgrid">')
        for a in items:
            cls = ' class="cur"' if a['id'] == current else ''
            label = (f"$10 у {nm(a, lang)}" if lang == 'uk' else f"$10 in {nm(a, lang)}")
            out.append(f'<a href="{url(lang, a["id"])}"{cls}>{esc(label)} <span>{a["tk"]}</span></a>')
        out.append('</div>')
    out.append('</section>')
    return ''.join(out)

def page(lang, aid, title, desc, h1, intro, content, sel, since, jsonld, assets_v):
    other = 'en' if lang == 'uk' else 'uk'
    canon = SITE + url(lang, aid)
    alt = ''.join(f'<link rel="alternate" hreflang="{lg}" href="{SITE + url(lg, aid)}">' for lg in LANGS)
    alt += f'<link rel="alternate" hreflang="x-default" href="{SITE + url("en", aid)}">'
    cfg = json.dumps(dict(lang=lang, sel=sel, since=since, staticH1=True))
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    l = L[lang]
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alt}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{'uk_UA' if lang == 'uk' else 'en_US'}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0b0d12">
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/style.css?v={assets_v['css']}">
{ld}
</head>
<body>
<div class="wrap">
  <header>
    <a class="logo" href="{url(lang)}">what<b>if</b>.invest</a>
    <nav class="lang"><a href="{url('uk', aid)}" class="{'on' if lang == 'uk' else ''}" hreflang="uk">UA</a><a href="{url('en', aid)}" class="{'on' if lang == 'en' else ''}" hreflang="en">EN</a></nav>
  </header>
  {'<nav class="crumbs"><a href="' + url(lang) + '">' + l['home'] + '</a> / ' + esc(nm(AM[aid], lang)) + '</nav>' if aid else ''}
  <h1>{h1}</h1>
  <p class="sub">{intro}</p>
  {calc_markup(lang)}
  {content}
  {links_grid(lang, aid)}
  <p class="note" data-t="note"></p>
  <footer>{l['by']} <a href="{SITE}/">Timebox</a> · {l['disclaimer']}</footer>
</div>
<script>window.PAGE={cfg};</script>
<script src="{BASE}/assets/data.js?v={assets_v['data']}"></script>
<script src="{BASE}/assets/ref.js?v={assets_v['ref']}"></script>
<script src="{BASE}/assets/app.js?v={assets_v['js']}"></script>
</body>
</html>
"""

# ---------- content per page ----------
END_I = ym2i(END)
PERIODS = [(1, {'uk': '1 рік', 'en': '1 year'}), (3, {'uk': '3 роки', 'en': '3 years'}),
           (5, {'uk': '5 років', 'en': '5 years'}), (10, {'uk': '10 років', 'en': '10 years'})]

def period_rows(aid, lang):
    rows = []
    s0 = ym2i(PR[aid]['start'])
    for yrs, lab in PERIODS:
        st = END_I - yrs * 12
        if st < s0:
            continue
        r = simulate(aid, st)
        rows.append((lab[lang] + f" ({mlabel(i2ym(st), lang)})", r))
    r = simulate(aid, s0)
    rows.append(({'uk': 'Від початку даних', 'en': 'Since data starts'}[lang] + f" ({mlabel(i2ym(s0), lang)})", r))
    return rows

def table_html(rows, lang):
    l = L[lang]
    h = f'<table class="static"><thead><tr><th>{l["period"]}</th><th>{l["invested"]}</th><th>{l["now"]}</th><th>{l["result"]}</th></tr></thead><tbody>'
    for lab, r in rows:
        cls = 'good' if r['roi'] >= 0 else 'bad'
        h += f'<tr><td class="a">{lab}</td><td>{usd(r["inv"])}</td><td>{usd(r["val"])}</td><td class="{cls}">{pct(r["roi"])}</td></tr>'
    return h + '</tbody></table>'

def default_since(aid):
    s0 = ym2i(PR[aid]['start'])
    st = max(s0, END_I - 60)
    y = (st + 11) // 12            # first January on or after st
    return f"{y}-01" if y * 12 < END_I - 6 else i2ym(s0)

def bench(aid):
    for b in ['btc', 'spy', 'qqq', 'gold']:
        if b != aid and b in PR:
            yield b

def asset_page(a, lang, v):
    aid, n, tk = a['id'], nm(a, lang), a['tk']
    since = default_since(aid)
    r = simulate(aid, ym2i(since))
    since_long = mlabel(i2ym(r['frm']), lang, long=True)
    rows = period_rows(aid, lang)
    yrs5 = END_I - 60
    b1 = next(bench(aid))
    rb, ra5 = simulate(b1, max(yrs5, ym2i(PR[b1]['start']))), simulate(aid, max(yrs5, ym2i(PR[aid]['start'])))
    upd = mlabel(END, lang, long=True)
    if lang == 'uk':
        title = f"Що якби я щодня вкладав $10 у {n} ({tk})? DCA-калькулятор"
        desc = f"$10 щодня в {n} з {since_long}: вкладено {usd(r['inv'])}, зараз {usd(r['val'])} ({pct(r['roi'])}). Порахуй свій сценарій і порівняй {n} з {len(assets)-1} активами."
        h1 = f"Що якби я щодня вкладав <em>$10</em> у {esc(n)} ({tk})?"
        intro = (f"Якби ти з {since_long} щодня купував {esc(n)} на $10, то вклав би <b>{usd(r['inv'])}</b>, "
                 f"а зараз мав би <b>{usd(r['val'])}</b> ({pct(r['roi'])}). Зміни суму, частоту чи дату старту і порівняй з іншими активами.")
        h2 = f"$10 щодня в {esc(n)}: результати за різні періоди"
        faq = [
            (f"Скільки б я мав, якби вкладав $10 щодня в {n} з {since_long}?",
             f"Ти вклав би {usd(r['inv'])}, а станом на {upd} мав би {usd(r['val'])}, тобто {pct(r['roi'])}. Розрахунок за місячними цінами закриття, без комісій і податків."),
            (f"Що вигідніше для щоденних покупок за 5 років: {n} чи {nm(AM[b1], lang)}?",
             f"$10 щодня протягом останніх 5 років дали б {pct(ra5['roi'])} для {n} і {pct(rb['roi'])} для {nm(AM[b1], lang)}. Минулі результати не гарантують майбутніх."),
            ("Що таке DCA (усереднення вартості)?",
             "DCA — це стратегія, коли ти регулярно купуєш актив на однакову суму незалежно від ціни. Коли ціна низька, купуєш більше, коли висока — менше. Це згладжує вплив волатильності і знімає потребу вгадувати найкращий момент для входу."),
        ]
    else:
        title = f"What if I invested $10 a day in {n} ({tk})? DCA calculator"
        desc = f"$10 a day in {n} since {since_long}: {usd(r['inv'])} invested, worth {usd(r['val'])} today ({pct(r['roi'])}). Run your own scenario and compare {n} with {len(assets)-1} other assets."
        h1 = f"What if I invested <em>$10</em> a day in {esc(n)} ({tk})?"
        intro = (f"If you had bought $10 of {esc(n)} every day since {since_long}, you would have put in <b>{usd(r['inv'])}</b> "
                 f"and it would be worth <b>{usd(r['val'])}</b> today ({pct(r['roi'])}). Change the amount, frequency or start date and compare with other assets.")
        h2 = f"$10 a day in {esc(n)}: results by period"
        faq = [
            (f"How much would I have if I invested $10 a day in {n} since {since_long}?",
             f"You would have invested {usd(r['inv'])}, and as of {upd} it would be worth {usd(r['val'])}, which is {pct(r['roi'])}. Based on monthly closing prices, before fees and taxes."),
            (f"Which was better to buy daily over the last 5 years: {n} or {nm(AM[b1], lang)}?",
             f"$10 a day over the last 5 years would have returned {pct(ra5['roi'])} for {n} and {pct(rb['roi'])} for {nm(AM[b1], lang)}. Past performance does not guarantee future results."),
            ("What is DCA (dollar-cost averaging)?",
             "DCA means buying an asset for the same amount at regular intervals, whatever the price. You buy more when the price is low and less when it is high, which smooths out volatility and removes the need to time the market."),
        ]
    content = (f'<section class="card seo"><h2>{h2}</h2>{table_html(rows, lang)}</section>'
               f'<section class="card seo faq"><h2>{L[lang]["faq"]}</h2>' +
               ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(ans)}</p></details>' for q, ans in faq) + '</section>')
    jsonld = [
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faq]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "whatif.invest", "item": SITE + url(lang)},
            {"@type": "ListItem", "position": 2, "name": n, "item": SITE + url(lang, aid)}]},
    ]
    sel = [aid] + list(bench(aid))[:3]
    return page(lang, aid, title, desc, h1, intro, content, sel, since, jsonld, v)

def home_page(lang, v):
    st = END_I - 60
    lb = sorted(((a, simulate(a['id'], st)) for a in assets if ym2i(PR[a['id']]['start']) <= st), key=lambda x: -x[1]['roi'])
    top = lb[:10]
    since_long = mlabel(i2ym(st), lang, long=True)
    if lang == 'uk':
        title = "Що якби я щодня вкладав $10? DCA-калькулятор для крипти, акцій і золота"
        desc = f"Порахуй, скільки б ти мав, якби регулярно купував Bitcoin, Nvidia, Apple, золото чи ще {len(assets)} активів. Реальні історичні ціни, оновлення щодня."
        h1 = "Що якби я щодня вкладав <em>$10</em>?"
        intro = f"Обери активи й дату старту і подивись, скільки б у тебе було зараз. Реальні історичні ціни для {len(assets)} активів: крипта, акції, ETF, золото і срібло."
        h2 = f"Топ-10 активів для DCA за 5 років (з {since_long})"
    else:
        title = "What if I invested $10 a day? DCA calculator for crypto, stocks and gold"
        desc = f"See what you would have today if you had regularly bought Bitcoin, Nvidia, Apple, gold or {len(assets)} other assets. Real historical prices, updated daily."
        h1 = "What if I invested <em>$10</em> every day?"
        intro = f"Pick assets and a start date to see what you would have today. Real historical prices for {len(assets)} assets: crypto, stocks, ETFs, gold and silver."
        h2 = f"Top 10 assets to DCA over 5 years (since {since_long})"
    items = ''.join(f'<li><a href="{url(lang, a["id"])}">{esc(nm(a, lang))}</a> <span class="{"good" if r["roi"] >= 0 else "bad"}">{pct(r["roi"])}</span></li>' for a, r in top)
    content = f'<section class="card seo"><h2>{h2}</h2><ol class="toplist">{items}</ol></section>'
    jsonld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "whatif.invest",
               "url": SITE + url(lang), "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
               "inLanguage": lang, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc}]
    return page(lang, None, title, desc, h1, intro, content, ['btc', 'nvda', 'gold', 'silver', 'spy' if 'spy' in PR else 'qqq'], f"{END_I // 12 - 5}-01", jsonld, v)

# ---------- build ----------
def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    css = open(os.path.join(ROOT, 'src/style.css'), encoding='utf-8').read()
    js = open(os.path.join(ROOT, 'src/app.js'), encoding='utf-8').read()
    ref = open(os.path.join(ROOT, 'src/ref.js'), encoding='utf-8').read()
    data = 'window.WHATIF_DATA=' + json.dumps({'updated': UPDATED, 'assets': assets, 'prices': PR}, ensure_ascii=False, separators=(',', ':')) + ';'
    write('assets/style.css', css); write('assets/app.js', js); write('assets/ref.js', ref); write('assets/data.js', data)
    shutil.copy(os.path.join(ROOT, 'src/favicon.svg'), os.path.join(OUT, 'assets/favicon.svg'))
    v = dict(css=hashed(css), js=hashed(js), ref=hashed(ref), data=hashed(data))
    urls = []
    for lang in LANGS:
        write(url(lang)[len(BASE) + 1:] + 'index.html', home_page(lang, v)); urls.append(url(lang))
        for a in assets:
            write(url(lang, a['id'])[len(BASE) + 1:] + 'index.html', asset_page(a, lang, v)); urls.append(url(lang, a['id']))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u in urls:
        aid = u.rstrip('/').split('/')[-1]
        aid = None if aid in ('whatif', 'en') else aid
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{lg}" href="{SITE + url(lg, aid)}"/>' for lg in LANGS)
        sm.append(f'<url><loc>{SITE + u}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>')
    sm.append('</urlset>')
    write('sitemap.xml', '\n'.join(sm))
    print(f"built {len(urls)} pages, {len(assets)} assets, data {UPDATED}")

if __name__ == '__main__':
    main()
