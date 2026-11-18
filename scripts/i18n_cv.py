# -*- coding: utf-8 -*-
"""Converter pair pages /converter/<asset>-<ccy>/ (e.g. /converter/btc-eur/): title, H1, one-sentence answer, tables, links. 20 languages.
Placeholders: {name} asset name, {tk} ticker, {c} currency code, {v} value of 1 unit, {chg} 24h change, {y} 1-year change, {d} date."""

_K = ['title', 'h1', 'desc', 'ans', 'ans_y', 'tab', 'rev', 'oth_c', 'oth_a', 'all', 'about']
_V = {
 'uk': ['{tk} в {c}: 1 {tk} = {v} — конвертер {name} онлайн', 'Конвертер {tk} в {c}', 'Скільки коштує 1 {name} ({tk}) у {c}: зараз 1 {tk} = {v}. Курс наживо, таблиця перерахунку і зворотний курс. Оновлено {d}.',
        'Зараз 1 {name} ({tk}) коштує {v}. За 24 години ціна змінилася на {chg}.', ' За рік — {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} в інших валютах', 'Інші активи в {c}', 'Усі пари конвертера', '{name}: ціна, графік і новини'],
 'en': ['{tk} to {c}: 1 {tk} = {v} — {name} converter', '{tk} to {c} converter', 'How much is 1 {name} ({tk}) in {c}: right now 1 {tk} = {v}. Live rate, conversion table and reverse rate. Updated {d}.',
        '1 {name} ({tk}) is worth {v} right now. The price moved {chg} in the last 24 hours.', ' Over a year: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} in other currencies', 'Other assets in {c}', 'All converter pairs', '{name}: price, chart and news'],
 'es': ['{tk} a {c}: 1 {tk} = {v} — conversor de {name}', 'Conversor de {tk} a {c}', 'Cuánto vale 1 {name} ({tk}) en {c}: ahora 1 {tk} = {v}. Tipo en vivo, tabla de conversión y tipo inverso. Actualizado {d}.',
        '1 {name} ({tk}) vale ahora {v}. En 24 horas el precio cambió {chg}.', ' En un año: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} en otras monedas', 'Otros activos en {c}', 'Todos los pares', '{name}: precio, gráfico y noticias'],
 'pt': ['{tk} para {c}: 1 {tk} = {v} — conversor de {name}', 'Conversor de {tk} para {c}', 'Quanto vale 1 {name} ({tk}) em {c}: agora 1 {tk} = {v}. Cotação ao vivo, tabela de conversão e cotação inversa. Atualizado {d}.',
        '1 {name} ({tk}) vale agora {v}. Em 24 horas o preço variou {chg}.', ' Em um ano: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} em outras moedas', 'Outros ativos em {c}', 'Todos os pares', '{name}: preço, gráfico e notícias'],
 'de': ['{tk} in {c}: 1 {tk} = {v} — {name}-Rechner', '{tk} in {c} umrechnen', 'Wie viel ist 1 {name} ({tk}) in {c} wert: aktuell 1 {tk} = {v}. Live-Kurs, Umrechnungstabelle und Gegenkurs. Aktualisiert {d}.',
        '1 {name} ({tk}) ist aktuell {v} wert. In 24 Stunden änderte sich der Preis um {chg}.', ' Über ein Jahr: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} in anderen Währungen', 'Andere Werte in {c}', 'Alle Rechner-Paare', '{name}: Kurs, Chart und News'],
 'fr': ['{tk} en {c} : 1 {tk} = {v} — convertisseur {name}', 'Convertisseur {tk} en {c}', 'Combien vaut 1 {name} ({tk}) en {c} : actuellement 1 {tk} = {v}. Cours en direct, table de conversion et cours inverse. Mis à jour {d}.',
        '1 {name} ({tk}) vaut actuellement {v}. Sur 24 heures, le prix a varié de {chg}.', ' Sur un an : {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} dans d’autres devises', 'Autres actifs en {c}', 'Toutes les paires', '{name} : cours, graphique et actualités'],
 'it': ['{tk} in {c}: 1 {tk} = {v} — convertitore {name}', 'Convertitore {tk} in {c}', 'Quanto vale 1 {name} ({tk}) in {c}: ora 1 {tk} = {v}. Cambio in tempo reale, tabella di conversione e cambio inverso. Aggiornato {d}.',
        '1 {name} ({tk}) vale ora {v}. Nelle ultime 24 ore il prezzo è cambiato del {chg}.', ' In un anno: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} in altre valute', 'Altri asset in {c}', 'Tutte le coppie', '{name}: prezzo, grafico e notizie'],
 'pl': ['{tk} na {c}: 1 {tk} = {v} — kalkulator {name}', 'Przelicznik {tk} na {c}', 'Ile jest wart 1 {name} ({tk}) w {c}: teraz 1 {tk} = {v}. Kurs na żywo, tabela przeliczeń i kurs odwrotny. Aktualizacja {d}.',
        '1 {name} ({tk}) jest teraz wart {v}. W ciągu 24 godzin cena zmieniła się o {chg}.', ' W ciągu roku: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} w innych walutach', 'Inne aktywa w {c}', 'Wszystkie pary', '{name}: cena, wykres i wiadomości'],
 'tr': ['{tk} {c} çevirici: 1 {tk} = {v} — {name}', '{tk} → {c} çevirici', '1 {name} ({tk}) kaç {c}: şu anda 1 {tk} = {v}. Canlı kur, çeviri tablosu ve ters kur. Güncelleme {d}.',
        '1 {name} ({tk}) şu anda {v} değerinde. Son 24 saatte fiyat {chg} değişti.', ' Bir yılda: {y}.', '{tk} → {c}', '{c} → {tk}', 'Diğer para birimlerinde {tk}', '{c} cinsinden diğer varlıklar', 'Tüm çiftler', '{name}: fiyat, grafik ve haberler'],
 'nl': ['{tk} naar {c}: 1 {tk} = {v} — {name}-omrekenen', '{tk} naar {c} omrekenen', 'Hoeveel is 1 {name} ({tk}) in {c}: nu 1 {tk} = {v}. Live koers, omrekentabel en omgekeerde koers. Bijgewerkt {d}.',
        '1 {name} ({tk}) is nu {v} waard. In 24 uur veranderde de prijs met {chg}.', ' Over een jaar: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} in andere valuta', 'Andere activa in {c}', 'Alle paren', '{name}: koers, grafiek en nieuws'],
 'ru': ['{tk} в {c}: 1 {tk} = {v} — конвертер {name} онлайн', 'Конвертер {tk} в {c}', 'Сколько стоит 1 {name} ({tk}) в {c}: сейчас 1 {tk} = {v}. Курс онлайн, таблица пересчёта и обратный курс. Обновлено {d}.',
        'Сейчас 1 {name} ({tk}) стоит {v}. За 24 часа цена изменилась на {chg}.', ' За год — {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} в других валютах', 'Другие активы в {c}', 'Все пары конвертера', '{name}: цена, график и новости'],
 'id': ['{tk} ke {c}: 1 {tk} = {v} — konverter {name}', 'Konverter {tk} ke {c}', 'Berapa 1 {name} ({tk}) dalam {c}: saat ini 1 {tk} = {v}. Kurs langsung, tabel konversi, dan kurs balik. Diperbarui {d}.',
        '1 {name} ({tk}) saat ini bernilai {v}. Dalam 24 jam harga berubah {chg}.', ' Dalam setahun: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} dalam mata uang lain', 'Aset lain dalam {c}', 'Semua pasangan', '{name}: harga, grafik, dan berita'],
 'vi': ['{tk} sang {c}: 1 {tk} = {v} — chuyển đổi {name}', 'Chuyển đổi {tk} sang {c}', '1 {name} ({tk}) bằng bao nhiêu {c}: hiện 1 {tk} = {v}. Tỷ giá trực tiếp, bảng quy đổi và tỷ giá ngược. Cập nhật {d}.',
        '1 {name} ({tk}) hiện có giá {v}. Trong 24 giờ giá thay đổi {chg}.', ' Trong một năm: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} theo các tiền tệ khác', 'Tài sản khác theo {c}', 'Tất cả các cặp', '{name}: giá, biểu đồ và tin tức'],
 'th': ['{tk} เป็น {c}: 1 {tk} = {v} — แปลงค่า {name}', 'แปลง {tk} เป็น {c}', '1 {name} ({tk}) เท่ากับกี่ {c}: ตอนนี้ 1 {tk} = {v} อัตราสด ตารางแปลงค่า และอัตรากลับ อัปเดต {d}',
        'ตอนนี้ 1 {name} ({tk}) มีมูลค่า {v} ใน 24 ชั่วโมงราคาเปลี่ยน {chg}', ' ในหนึ่งปี: {y}', '{tk} → {c}', '{c} → {tk}', '{tk} ในสกุลเงินอื่น', 'สินทรัพย์อื่นใน {c}', 'คู่แปลงทั้งหมด', '{name}: ราคา กราฟ และข่าว'],
 'hi': ['{tk} से {c}: 1 {tk} = {v} — {name} कन्वर्टर', '{tk} से {c} कन्वर्टर', '1 {name} ({tk}) कितने {c} का है: अभी 1 {tk} = {v}। लाइव रेट, कन्वर्ज़न टेबल और उल्टा रेट। अपडेट {d}।',
        'अभी 1 {name} ({tk}) की कीमत {v} है। 24 घंटे में कीमत {chg} बदली।', ' एक साल में: {y}।', '{tk} → {c}', '{c} → {tk}', 'अन्य मुद्राओं में {tk}', '{c} में अन्य एसेट', 'सभी जोड़े', '{name}: कीमत, चार्ट और खबरें'],
 'ja': ['{tk}から{c}：1 {tk} = {v} — {name}換算', '{tk}→{c} 換算ツール', '1 {name}（{tk}）は何{c}？現在 1 {tk} = {v}。リアルタイムレート、換算表、逆レート。更新：{d}。',
        '現在 1 {name}（{tk}）は {v} です。24時間の値動きは {chg}。', ' 1年では {y}。', '{tk} → {c}', '{c} → {tk}', '他の通貨での{tk}', '{c}建ての他の資産', 'すべての換算ペア', '{name}：価格・チャート・ニュース'],
 'ko': ['{tk} {c} 환산: 1 {tk} = {v} — {name} 계산기', '{tk} → {c} 환산', '1 {name}({tk})은 몇 {c}? 현재 1 {tk} = {v}. 실시간 환율, 환산표와 역환율. 업데이트 {d}.',
        '현재 1 {name}({tk})의 가치는 {v}입니다. 24시간 동안 가격이 {chg} 변했습니다.', ' 1년 동안: {y}.', '{tk} → {c}', '{c} → {tk}', '다른 통화의 {tk}', '{c} 기준 다른 자산', '모든 환산 쌍', '{name}: 가격, 차트, 뉴스'],
 'zh': ['{tk} 兑 {c}：1 {tk} = {v} — {name} 换算器', '{tk} 兑 {c} 换算器', '1 {name}（{tk}）等于多少 {c}：当前 1 {tk} = {v}。实时汇率、换算表和反向汇率。更新于 {d}。',
        '当前 1 {name}（{tk}）价值 {v}。24 小时内价格变动 {chg}。', ' 一年内：{y}。', '{tk} → {c}', '{c} → {tk}', '{tk} 兑其他货币', '以 {c} 计价的其他资产', '所有换算对', '{name}：价格、图表和新闻'],
 'ar': ['{tk} إلى {c}: 1 {tk} = {v} — محول {name}', 'محول {tk} إلى {c}', 'كم يساوي 1 {name} ({tk}) بـ{c}: الآن 1 {tk} = {v}. سعر مباشر وجدول تحويل وسعر عكسي. آخر تحديث {d}.',
        'يساوي 1 {name} ({tk}) الآن {v}. تغيّر السعر خلال 24 ساعة بنسبة {chg}.', ' خلال عام: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} بعملات أخرى', 'أصول أخرى بـ{c}', 'كل أزواج التحويل', '{name}: السعر والرسم البياني والأخبار'],
 'fil': ['{tk} sa {c}: 1 {tk} = {v} — {name} converter', '{tk} sa {c} converter', 'Magkano ang 1 {name} ({tk}) sa {c}: ngayon 1 {tk} = {v}. Live na rate, conversion table at baligtad na rate. Na-update {d}.',
        'Ang 1 {name} ({tk}) ay nagkakahalaga ngayon ng {v}. Gumalaw ang presyo nang {chg} sa nakaraang 24 oras.', ' Sa loob ng isang taon: {y}.', '{tk} → {c}', '{c} → {tk}', '{tk} sa ibang currency', 'Iba pang asset sa {c}', 'Lahat ng pair', '{name}: presyo, chart at balita'],
}
CV = {lg: dict(zip(_K, v)) for lg, v in _V.items()}
for _lg, _v in _V.items():
    assert len(_v) == len(_K), _lg

# currencies per language: local first, then the world's majors
CV_CCY = {'uk': ['UAH', 'USD', 'EUR'], 'ru': ['USD', 'RUB', 'EUR', 'UAH', 'KZT'], 'en': ['USD', 'EUR', 'GBP', 'INR', 'CAD', 'AUD'], 'es': ['EUR', 'USD', 'MXN', 'ARS', 'COP', 'CLP'],
          'pt': ['BRL', 'EUR', 'USD'], 'de': ['EUR', 'USD', 'CHF'], 'fr': ['EUR', 'USD', 'CHF'], 'it': ['EUR', 'USD'], 'pl': ['PLN', 'USD', 'EUR'], 'tr': ['TRY', 'USD', 'EUR'],
          'nl': ['EUR', 'USD'], 'id': ['IDR', 'USD'], 'vi': ['VND', 'USD'], 'th': ['THB', 'USD'], 'hi': ['INR', 'USD'], 'ja': ['JPY', 'USD'], 'ko': ['KRW', 'USD'],
          'zh': ['CNY', 'USD', 'HKD', 'TWD'], 'ar': ['AED', 'SAR', 'USD', 'EGP'], 'fil': ['PHP', 'USD']}
