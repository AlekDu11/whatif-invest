#!/usr/bin/env python3
"""Default share images (og:image) per language: src/og/<lang>.jpg, 1200x630, in the cover style.

Run after changing the positioning:  python3 scripts/og.py
Languages whose script the brand fonts do not cover fall back to the English image (build.py picks og/<lang>.jpg if it exists).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cover  # noqa: E402

# title = headline, stat = big gold number, sl = line under it, lb = badge top right
OG = {
    'en': dict(title='Crypto, stocks and gold in plain language', sl='assets with prices, charts and news', lb='20 languages'),
    'uk': dict(title='Крипта, акції і золото простою мовою', sl='активів: ціни, графіки й новини', lb='20 мов'),
    'ru': dict(title='Крипта, акции и золото простым языком', sl='активов: цены, графики и новости', lb='20 языков'),
    'es': dict(title='Cripto, acciones y oro en lenguaje claro', sl='activos con precios, gráficos y noticias', lb='20 idiomas'),
    'pt': dict(title='Cripto, ações e ouro em linguagem simples', sl='ativos com preços, gráficos e notícias', lb='20 idiomas'),
    'de': dict(title='Krypto, Aktien und Gold verständlich erklärt', sl='Werte mit Kursen, Charts und News', lb='20 Sprachen'),
    'fr': dict(title='Crypto, actions et or en langage clair', sl='actifs avec cours, graphiques et actus', lb='20 langues'),
    'it': dict(title='Cripto, azioni e oro in parole semplici', sl='asset con prezzi, grafici e notizie', lb='20 lingue'),
    'pl': dict(title='Krypto, akcje i złoto prostym językiem', sl='aktywów: ceny, wykresy i wiadomości', lb='20 języków'),
    'tr': dict(title='Kripto, hisse ve altın sade bir dille', sl='varlık: fiyatlar, grafikler ve haberler', lb='20 dil'),
    'nl': dict(title='Crypto, aandelen en goud in gewone taal', sl='assets met koersen, grafieken en nieuws', lb='20 talen'),
    'id': dict(title='Kripto, saham, dan emas dengan bahasa sederhana', sl='aset dengan harga, grafik, dan berita', lb='20 bahasa'),
    'vi': dict(title='Crypto, cổ phiếu và vàng bằng ngôn ngữ dễ hiểu', sl='tài sản: giá, biểu đồ và tin tức', lb='20 ngôn ngữ'),
    'fil': dict(title='Crypto, stocks at ginto sa simpleng salita', sl='asset na may presyo, chart at balita', lb='20 wika'),
}


def main():
    A = cover.B().A
    n = len(A)
    out_dir = os.path.join(cover.ROOT, 'src', 'og')
    os.makedirs(out_dir, exist_ok=True)
    done = []
    for lang, t in OG.items():
        stat = f'{(n // 100) * 100:,}+' if lang == 'en' else f'{(n // 100) * 100}+'
        meta = dict(title=t['title'], stat=stat, stat_label=t['sl'], label=t['lb'], assets='btc,nvda,aapl,eth', date='')
        if cover.render('og', lang, 'og', meta, os.path.join(out_dir, lang + '.jpg')):
            done.append(lang)
    print('rendered:', ' '.join(done))


if __name__ == '__main__':
    main()
