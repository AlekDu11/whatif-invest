"""Stocks by country: hub pages /stocks-ukraine/, /stocks-poland/, /stocks-germany/ (all 20 languages).
Per language: nav label, lead with {n}, local-price label, then per market (name with flag, page H1)."""
C = {
 'en': ('Stocks by country', '{n} companies. Prices are in US dollars at today\'s exchange rate; the DCA columns show what $10 a day would have returned.', 'Local price',
        {'ua': ('Ukraine', 'Ukrainian stocks: Kyivstar, Swarmer, Astarta and other listed companies'), 'pl': ('Poland', 'Best Polish stocks for regular investing (WIG20 and more)'), 'de': ('Germany', 'Best German stocks for regular investing (DAX 40)')}),
 'uk': ('Акції за країнами', '{n} компаній. Ціни в доларах США за сьогоднішнім курсом; колонки DCA показують, що дали б $10 щодня.', 'Ціна на місцевій біржі',
        {'ua': ('Україна', 'Українські акції: Київстар, Swarmer, Астарта та інші компанії на біржах'), 'pl': ('Польща', 'Найкращі акції Польщі для регулярних інвестицій (WIG20 і не тільки)'), 'de': ('Німеччина', 'Найкращі акції Німеччини для регулярних інвестицій (DAX 40)')}),
 'ru': ('Акции по странам', '{n} компаний. Цены в долларах США по сегодняшнему курсу; колонки DCA показывают, что дали бы $10 в день.', 'Цена на местной бирже',
        {'ua': ('Украина', 'Украинские акции: Киевстар, Swarmer, Астарта и другие компании на биржах'), 'pl': ('Польша', 'Лучшие акции Польши для регулярных инвестиций (WIG20 и не только)'), 'de': ('Германия', 'Лучшие акции Германии для регулярных инвестиций (DAX 40)')}),
 'es': ('Acciones por país', '{n} empresas. Precios en dólares al tipo de cambio de hoy; las columnas DCA muestran lo que habrían dado $10 al día.', 'Precio local',
        {'ua': ('Ucrania', 'Acciones ucranianas: Kyivstar, Swarmer, Astarta y otras empresas cotizadas'), 'pl': ('Polonia', 'Las mejores acciones de Polonia para invertir de forma periódica (WIG20 y más)'), 'de': ('Alemania', 'Las mejores acciones de Alemania para invertir de forma periódica (DAX 40)')}),
 'pt': ('Ações por país', '{n} empresas. Preços em dólares pela cotação de hoje; as colunas DCA mostram o que $10 por dia teriam rendido.', 'Preço local',
        {'ua': ('Ucrânia', 'Ações ucranianas: Kyivstar, Swarmer, Astarta e outras empresas listadas'), 'pl': ('Polônia', 'Melhores ações da Polônia para investir regularmente (WIG20 e mais)'), 'de': ('Alemanha', 'Melhores ações da Alemanha para investir regularmente (DAX 40)')}),
 'de': ('Aktien nach Ländern', '{n} Unternehmen. Kurse in US-Dollar zum heutigen Wechselkurs; die DCA-Spalten zeigen, was 10 $ am Tag gebracht hätten.', 'Kurs an der Heimatbörse',
        {'ua': ('Ukraine', 'Ukrainische Aktien: Kyivstar, Swarmer, Astarta und weitere börsennotierte Firmen'), 'pl': ('Polen', 'Die besten polnischen Aktien für den Sparplan (WIG20 und mehr)'), 'de': ('Deutschland', 'Die besten deutschen Aktien für den Sparplan (DAX 40)')}),
 'fr': ('Actions par pays', '{n} entreprises. Cours en dollars au taux de change du jour ; les colonnes DCA montrent ce qu\'auraient rapporté 10 $ par jour.', 'Cours local',
        {'ua': ('Ukraine', 'Actions ukrainiennes : Kyivstar, Swarmer, Astarta et autres sociétés cotées'), 'pl': ('Pologne', 'Les meilleures actions polonaises pour investir régulièrement (WIG20 et plus)'), 'de': ('Allemagne', 'Les meilleures actions allemandes pour investir régulièrement (DAX 40)')}),
 'it': ('Azioni per paese', '{n} società. Prezzi in dollari al cambio di oggi; le colonne DCA mostrano cosa avrebbero reso 10 $ al giorno.', 'Prezzo locale',
        {'ua': ('Ucraina', 'Azioni ucraine: Kyivstar, Swarmer, Astarta e altre società quotate'), 'pl': ('Polonia', 'Le migliori azioni polacche per un piano di accumulo (WIG20 e oltre)'), 'de': ('Germania', 'Le migliori azioni tedesche per un piano di accumulo (DAX 40)')}),
 'pl': ('Akcje według krajów', '{n} spółek. Ceny w dolarach po dzisiejszym kursie; kolumny DCA pokazują, ile dałoby 10 $ dziennie.', 'Cena na giełdzie',
        {'ua': ('Ukraina', 'Ukraińskie akcje: Kyivstar, Swarmer, Astarta i inne notowane spółki'), 'pl': ('Polska', 'Najlepsze polskie akcje do regularnego inwestowania (WIG20 i nie tylko)'), 'de': ('Niemcy', 'Najlepsze niemieckie akcje do regularnego inwestowania (DAX 40)')}),
 'tr': ('Ülkelere göre hisseler', '{n} şirket. Fiyatlar bugünkü kurla ABD doları cinsinden; DCA sütunları günde 10 $ yatırımın ne getireceğini gösterir.', 'Yerel fiyat',
        {'ua': ('Ukrayna', 'Ukrayna hisseleri: Kyivstar, Swarmer, Astarta ve diğer borsada işlem gören şirketler'), 'pl': ('Polonya', 'Düzenli yatırım için en iyi Polonya hisseleri (WIG20 ve fazlası)'), 'de': ('Almanya', 'Düzenli yatırım için en iyi Alman hisseleri (DAX 40)')}),
 'nl': ('Aandelen per land', '{n} bedrijven. Koersen in dollars tegen de wisselkoers van vandaag; de DCA-kolommen tonen wat $10 per dag had opgeleverd.', 'Lokale koers',
        {'ua': ('Oekraïne', 'Oekraïense aandelen: Kyivstar, Swarmer, Astarta en andere beursgenoteerde bedrijven'), 'pl': ('Polen', 'De beste Poolse aandelen om periodiek in te beleggen (WIG20 en meer)'), 'de': ('Duitsland', 'De beste Duitse aandelen om periodiek in te beleggen (DAX 40)')}),
 'id': ('Saham per negara', '{n} perusahaan. Harga dalam dolar AS dengan kurs hari ini; kolom DCA menunjukkan hasil $10 per hari.', 'Harga lokal',
        {'ua': ('Ukraina', 'Saham Ukraina: Kyivstar, Swarmer, Astarta dan perusahaan tercatat lainnya'), 'pl': ('Polandia', 'Saham Polandia terbaik untuk investasi rutin (WIG20 dan lainnya)'), 'de': ('Jerman', 'Saham Jerman terbaik untuk investasi rutin (DAX 40)')}),
 'vi': ('Cổ phiếu theo quốc gia', '{n} công ty. Giá tính bằng USD theo tỷ giá hôm nay; các cột DCA cho thấy $10 mỗi ngày sẽ thành bao nhiêu.', 'Giá tại sàn địa phương',
        {'ua': ('Ukraina', 'Cổ phiếu Ukraina: Kyivstar, Swarmer, Astarta và các công ty niêm yết khác'), 'pl': ('Ba Lan', 'Cổ phiếu Ba Lan tốt nhất để đầu tư định kỳ (WIG20 và hơn thế)'), 'de': ('Đức', 'Cổ phiếu Đức tốt nhất để đầu tư định kỳ (DAX 40)')}),
 'th': ('หุ้นตามประเทศ', '{n} บริษัท ราคาเป็นดอลลาร์สหรัฐตามอัตราแลกเปลี่ยนวันนี้ คอลัมน์ DCA แสดงผลลัพธ์ของการลงทุนวันละ $10', 'ราคาในตลาดท้องถิ่น',
        {'ua': ('ยูเครน', 'หุ้นยูเครน: Kyivstar, Swarmer, Astarta และบริษัทจดทะเบียนอื่น ๆ'), 'pl': ('โปแลนด์', 'หุ้นโปแลนด์ที่ดีที่สุดสำหรับการลงทุนสม่ำเสมอ (WIG20 และอื่น ๆ)'), 'de': ('เยอรมนี', 'หุ้นเยอรมันที่ดีที่สุดสำหรับการลงทุนสม่ำเสมอ (DAX 40)')}),
 'hi': ('देश के अनुसार शेयर', '{n} कंपनियां। कीमतें आज की विनिमय दर पर अमेरिकी डॉलर में; DCA कॉलम दिखाते हैं कि रोज़ $10 से कितना मिलता।', 'स्थानीय कीमत',
        {'ua': ('यूक्रेन', 'यूक्रेन के शेयर: Kyivstar, Swarmer, Astarta और अन्य सूचीबद्ध कंपनियां'), 'pl': ('पोलैंड', 'नियमित निवेश के लिए पोलैंड के सबसे अच्छे शेयर (WIG20 और अधिक)'), 'de': ('जर्मनी', 'नियमित निवेश के लिए जर्मनी के सबसे अच्छे शेयर (DAX 40)')}),
 'ja': ('国別の株式', '{n}社。価格は本日の為替レートで米ドル換算。DCA列は毎日10ドル積み立てた場合の結果です。', '現地価格',
        {'ua': ('ウクライナ', 'ウクライナ株：Kyivstar、Swarmer、Astartaなどの上場企業'), 'pl': ('ポーランド', '積立投資に向くポーランド株（WIG20ほか）'), 'de': ('ドイツ', '積立投資に向くドイツ株（DAX 40）')}),
 'ko': ('국가별 주식', '{n}개 기업. 가격은 오늘 환율 기준 미국 달러이며, DCA 열은 매일 10달러씩 투자했을 때의 결과입니다.', '현지 가격',
        {'ua': ('우크라이나', '우크라이나 주식: Kyivstar, Swarmer, Astarta 등 상장 기업'), 'pl': ('폴란드', '적립식 투자에 좋은 폴란드 주식 (WIG20 등)'), 'de': ('독일', '적립식 투자에 좋은 독일 주식 (DAX 40)')}),
 'zh': ('按国家分类的股票', '{n}家公司。价格按今日汇率换算为美元；DCA列显示每天投资10美元的结果。', '当地价格',
        {'ua': ('乌克兰', '乌克兰股票：Kyivstar、Swarmer、Astarta等上市公司'), 'pl': ('波兰', '适合定投的波兰股票（WIG20等）'), 'de': ('德国', '适合定投的德国股票（DAX 40）')}),
 'ar': ('الأسهم حسب الدولة', '{n} شركة. الأسعار بالدولار الأمريكي بسعر صرف اليوم؛ وتُظهر أعمدة DCA نتيجة استثمار 10 دولارات يوميًا.', 'السعر المحلي',
        {'ua': ('أوكرانيا', 'أسهم أوكرانيا: Kyivstar وSwarmer وAstarta وشركات مدرجة أخرى'), 'pl': ('بولندا', 'أفضل أسهم بولندا للاستثمار المنتظم (WIG20 وغيرها)'), 'de': ('ألمانيا', 'أفضل أسهم ألمانيا للاستثمار المنتظم (DAX 40)')}),
 'fil': ('Mga stock ayon sa bansa', '{n} kumpanya. Presyo sa US dollar ayon sa palitan ngayon; ipinapakita ng mga kolum ng DCA ang kikitain ng $10 kada araw.', 'Lokal na presyo',
        {'ua': ('Ukraine', 'Mga stock ng Ukraine: Kyivstar, Swarmer, Astarta at iba pang nakalistang kumpanya'), 'pl': ('Poland', 'Pinakamahusay na stock ng Poland para sa regular na pag-iinvest (WIG20 at iba pa)'), 'de': ('Germany', 'Pinakamahusay na stock ng Germany para sa regular na pag-iinvest (DAX 40)')}),
}
MKTS = {'ua': ('stocks-ukraine', '🇺🇦'), 'pl': ('stocks-poland', '🇵🇱'), 'de': ('stocks-germany', '🇩🇪')}
MKT_LANG = {'ua': 'uk', 'pl': 'pl', 'de': 'de'}
CCY_SIGN = {'PLN': 'zł', 'EUR': '€', 'GBp': 'p', 'USD': '$', 'TRY': '₺', 'JPY': '¥', 'KRW': '₩', 'INR': '₹', 'BRL': 'R$', 'HKD': 'HK$', 'CNY': '¥',
            'TWD': 'NT$', 'IDR': 'Rp', 'THB': '฿', 'PHP': '₱', 'VND': '₫', 'SAR': 'SAR', 'CHF': 'CHF', 'CAD': 'C$', 'AUD': 'A$', 'MXN': 'MX$', 'RUB': '₽',
            'SEK': 'kr', 'NOK': 'kr', 'DKK': 'kr', 'CZK': 'Kč', 'HUF': 'Ft', 'ILA': 'ag.', 'ILS': '₪', 'ZAc': 'c', 'ZAR': 'R', 'EGP': 'E£',
            'SGD': 'S$', 'MYR': 'RM', 'NZD': 'NZ$', 'ARS': 'AR$', 'CLP': 'CLP'}
from i18n_ctry2 import MK2, C2  # noqa: E402  (23 more markets, names from CLDR)
for _m, (_slug, _flag, _lang) in MK2.items():
    MKTS[_m] = (_slug, _flag)
    MKT_LANG[_m] = _lang
for _lg in C:
    C[_lg][3].update(C2[_lg])
from i18n_ctry3 import MK3, C3  # noqa: E402  (19 more markets, 2026-11-21)
for _m, (_slug, _flag, _lang) in MK3.items():
    MKTS[_m] = (_slug, _flag)
    MKT_LANG[_m] = _lang
for _lg in C:
    C[_lg][3].update(C3[_lg])
assert len(C) == 20 and all(set(v[3]) == set(MKTS) for v in C.values()), 'country names missing'
from i18n_cmd import US as _US  # noqa: E402  (United States market page)
MKTS['us'] = ('stocks-usa', '🇺🇸')
MKT_LANG['us'] = 'en'
for _lg in C:
    C[_lg][3]['us'] = _US[_lg]
