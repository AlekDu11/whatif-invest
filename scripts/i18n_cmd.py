# Commodities tab (cat 'cmd') and names of metals/commodities in 20 languages.
# CMD[lang] = (tab label, category label, unit word for the calculator result)
CMD = {
 'uk': ('Сировина', 'Сировинний товар', 'од.'), 'en': ('Commodities', 'Commodity', 'units'), 'es': ('Materias primas', 'Materia prima', 'uds.'),
 'pt': ('Commodities', 'Commodity', 'un.'), 'de': ('Rohstoffe', 'Rohstoff', 'Einh.'), 'fr': ('Matières premières', 'Matière première', 'unités'),
 'it': ('Materie prime', 'Materia prima', 'unità'), 'pl': ('Surowce', 'Surowiec', 'jedn.'), 'tr': ('Emtialar', 'Emtia', 'birim'),
 'nl': ('Grondstoffen', 'Grondstof', 'eenh.'), 'ru': ('Сырьё', 'Сырьевой товар', 'ед.'), 'id': ('Komoditas', 'Komoditas', 'unit'),
 'vi': ('Hàng hóa', 'Hàng hóa', 'đơn vị'), 'th': ('สินค้าโภคภัณฑ์', 'สินค้าโภคภัณฑ์', 'หน่วย'), 'hi': ('कमोडिटी', 'कमोडिटी', 'इकाई'),
 'ja': ('コモディティ', 'コモディティ', '単位'), 'ko': ('원자재', '원자재', '단위'), 'zh': ('大宗商品', '大宗商品', '单位'),
 'ar': ('السلع', 'سلعة', 'وحدة'), 'fil': ('Mga kalakal', 'Kalakal', 'yunit'),
}
L = ['uk', 'en', 'es', 'pt', 'de', 'fr', 'it', 'pl', 'tr', 'nl', 'ru', 'id', 'vi', 'th', 'hi', 'ja', 'ko', 'zh', 'ar', 'fil']
_N = {   # id: names in the order of L
 'platinum': 'Платина|Platinum|Platino|Platina|Platin|Platine|Platino|Platyna|Platin|Platina|Платина|Platinum|Bạch kim|แพลทินัม|प्लैटिनम|プラチナ|백금|铂金|البلاتين|Platinum',
 'palladium': 'Паладій|Palladium|Paladio|Paládio|Palladium|Palladium|Palladio|Pallad|Paladyum|Palladium|Палладий|Paladium|Palađi|แพลเลเดียม|पैलेडियम|パラジウム|팔라듐|钯金|البلاديوم|Palladium',
 'copper': 'Мідь|Copper|Cobre|Cobre|Kupfer|Cuivre|Rame|Miedź|Bakır|Koper|Медь|Tembaga|Đồng|ทองแดง|तांबा|銅|구리|铜|النحاس|Tanso',
 'aluminum': 'Алюміній|Aluminum|Aluminio|Alumínio|Aluminium|Aluminium|Alluminio|Aluminium|Alüminyum|Aluminium|Алюминий|Aluminium|Nhôm|อะลูมิเนียม|एल्युमिनियम|アルミニウム|알루미늄|铝|الألومنيوم|Aluminyo',
 'wheat': 'Пшениця|Wheat|Trigo|Trigo|Weizen|Blé|Grano|Pszenica|Buğday|Tarwe|Пшеница|Gandum|Lúa mì|ข้าวสาลี|गेहूं|小麦|밀|小麦|القمح|Trigo',
 'corn': 'Кукурудза|Corn|Maíz|Milho|Mais|Maïs|Mais|Kukurydza|Mısır|Maïs|Кукуруза|Jagung|Ngô|ข้าวโพด|मक्का|トウモロコシ|옥수수|玉米|الذرة|Mais',
 'soybeans': 'Соя|Soybeans|Soja|Soja|Sojabohnen|Soja|Soia|Soja|Soya fasulyesi|Sojabonen|Соя|Kedelai|Đậu tương|ถั่วเหลือง|सोयाबीन|大豆|대두|大豆|فول الصويا|Soybeans',
 'soyoil': 'Соєва олія|Soybean oil|Aceite de soja|Óleo de soja|Sojaöl|Huile de soja|Olio di soia|Olej sojowy|Soya yağı|Sojaolie|Соевое масло|Minyak kedelai|Dầu đậu tương|น้ำมันถั่วเหลือง|सोयाबीन तेल|大豆油|대두유|豆油|زيت الصويا|Soybean oil',
 'oats': 'Овес|Oats|Avena|Aveia|Hafer|Avoine|Avena|Owies|Yulaf|Haver|Овёс|Gandum oat|Yến mạch|ข้าวโอ๊ต|जई|オーツ麦|귀리|燕麦|الشوفان|Oats',
 'rice': 'Рис|Rough rice|Arroz|Arroz|Reis|Riz|Riso|Ryż|Pirinç|Rijst|Рис|Beras|Gạo|ข้าว|चावल|米|쌀|稻米|الأرز|Bigas',
 'sugar': 'Цукор|Sugar|Azúcar|Açúcar|Zucker|Sucre|Zucchero|Cukier|Şeker|Suiker|Сахар|Gula|Đường|น้ำตาล|चीनी|砂糖|설탕|糖|السكر|Asukal',
 'coffee': 'Кава|Coffee|Café|Café|Kaffee|Café|Caffè|Kawa|Kahve|Koffie|Кофе|Kopi|Cà phê|กาแฟ|कॉफ़ी|コーヒー|커피|咖啡|القهوة|Kape',
 'cocoa': 'Какао|Cocoa|Cacao|Cacau|Kakao|Cacao|Cacao|Kakao|Kakao|Cacao|Какао|Kakao|Ca cao|โกโก้|कोको|ココア|코코아|可可|الكاكاو|Kakaw',
 'cotton': 'Бавовна|Cotton|Algodón|Algodão|Baumwolle|Coton|Cotone|Bawełna|Pamuk|Katoen|Хлопок|Kapas|Bông|ฝ้าย|कपास|綿花|면화|棉花|القطن|Bulak',
 'ojuice': 'Апельсиновий сік|Orange juice|Jugo de naranja|Suco de laranja|Orangensaft|Jus d’orange|Succo d’arancia|Sok pomarańczowy|Portakal suyu|Sinaasappelsap|Апельсиновый сок|Jus jeruk|Nước cam|น้ำส้ม|संतरे का रस|オレンジジュース|오렌지 주스|橙汁|عصير البرتقال|Orange juice',
 'cattle': 'Велика рогата худоба|Live cattle|Ganado vivo|Boi gordo|Lebendrind|Bovins vivants|Bovini vivi|Bydło żywe|Canlı sığır|Levend vee|Живой скот|Sapi hidup|Gia súc sống|โคมีชีวิต|जीवित मवेशी|生牛|생우|活牛|الماشية الحية|Live cattle',
 'hogs': 'Свині|Lean hogs|Cerdos magros|Suínos|Magerschweine|Porcs maigres|Suini magri|Wieprzowina|Yağsız domuz|Varkens|Постные свиньи|Babi|Heo nạc|สุกร|सुअर|豚赤身肉|돈육|瘦肉猪|الخنازير|Lean hogs',
 'wti': 'Нафта WTI|WTI crude oil|Petróleo WTI|Petróleo WTI|Rohöl WTI|Pétrole WTI|Petrolio WTI|Ropa WTI|WTI ham petrol|WTI-olie|Нефть WTI|Minyak WTI|Dầu WTI|น้ำมันดิบ WTI|WTI कच्चा तेल|WTI原油|WTI 원유|WTI原油|نفط WTI|WTI krudo',
 'brent': 'Нафта Brent|Brent crude oil|Petróleo Brent|Petróleo Brent|Rohöl Brent|Pétrole Brent|Petrolio Brent|Ropa Brent|Brent ham petrol|Brent-olie|Нефть Brent|Minyak Brent|Dầu Brent|น้ำมันดิบเบรนท์|ब्रेंट कच्चा तेल|ブレント原油|브렌트유|布伦特原油|نفط برنت|Brent krudo',
 'natgas': 'Природний газ|Natural gas|Gas natural|Gás natural|Erdgas|Gaz naturel|Gas naturale|Gaz ziemny|Doğal gaz|Aardgas|Природный газ|Gas alam|Khí tự nhiên|ก๊าซธรรมชาติ|प्राकृतिक गैस|天然ガス|천연가스|天然气|الغاز الطبيعي|Natural gas',
 'heatoil': 'Мазут|Heating oil|Gasóleo de calefacción|Óleo de aquecimento|Heizöl|Fioul domestique|Gasolio da riscaldamento|Olej opałowy|Isıtma yağı|Stookolie|Мазут|Minyak pemanas|Dầu sưởi|น้ำมันทำความร้อน|हीटिंग ऑयल|灯油|난방유|取暖油|زيت التدفئة|Heating oil',
 'gasoline': 'Бензин|Gasoline|Gasolina|Gasolina|Benzin|Essence|Benzina|Benzyna|Benzin|Benzine|Бензин|Bensin|Xăng|น้ำมันเบนซิน|पेट्रोल|ガソリン|휘발유|汽油|البنزين|Gasolina',
}
NAMES = {k: dict(zip(L, v.split('|'))) for k, v in _N.items()}
assert all(len(v) == 20 for v in NAMES.values()), [k for k, v in NAMES.items() if len(v) != 20]

# United States market (country pages): name, page title
US = {
 'uk': ('США', 'Найкращі акції США для регулярних інвестицій (S&P 500)'), 'en': ('United States', 'Best US stocks for regular investing (S&P 500)'),
 'es': ('Estados Unidos', 'Las mejores acciones de EE. UU. para invertir cada mes (S&P 500)'), 'pt': ('Estados Unidos', 'Melhores ações dos EUA para investir todo mês (S&P 500)'),
 'de': ('USA', 'Die besten US-Aktien für den Sparplan (S&P 500)'), 'fr': ('États-Unis', 'Meilleures actions américaines pour investir chaque mois (S&P 500)'),
 'it': ('Stati Uniti', 'Le migliori azioni USA per un PAC (S&P 500)'), 'pl': ('USA', 'Najlepsze akcje z USA do regularnego inwestowania (S&P 500)'),
 'tr': ('ABD', 'Düzenli yatırım için en iyi ABD hisseleri (S&P 500)'), 'nl': ('Verenigde Staten', 'Beste Amerikaanse aandelen om periodiek te beleggen (S&P 500)'),
 'ru': ('США', 'Лучшие акции США для регулярных инвестиций (S&P 500)'), 'id': ('Amerika Serikat', 'Saham AS terbaik untuk investasi rutin (S&P 500)'),
 'vi': ('Hoa Kỳ', 'Cổ phiếu Mỹ tốt nhất để đầu tư định kỳ (S&P 500)'), 'th': ('สหรัฐอเมริกา', 'หุ้นสหรัฐฯ ที่ดีที่สุดสำหรับการลงทุนสม่ำเสมอ (S&P 500)'),
 'hi': ('संयुक्त राज्य', 'नियमित निवेश के लिए सबसे अच्छे अमेरिकी शेयर (S&P 500)'), 'ja': ('アメリカ', '積立投資に向く米国株（S&P 500）'),
 'ko': ('미국', '적립식 투자에 좋은 미국 주식 (S&P 500)'), 'zh': ('美国', '适合定投的美国股票（标普500）'),
 'ar': ('الولايات المتحدة', 'أفضل الأسهم الأمريكية للاستثمار المنتظم (S&P 500)'), 'fil': ('Estados Unidos', 'Pinakamahusay na stock ng US para sa regular na pag-iinvest (S&P 500)'),
}

# Honest note on commodity/metal futures pages (front-month futures prices, not what an ETF returns)
NOTE = {
 'uk': 'Ціна найближчого ф’ючерсу (Yahoo Finance). Звичайний інвестор зазвичай купує сировину через ETF — їхня дохідність може відрізнятися через перекладання контрактів.',
 'en': 'Price of the front-month futures contract (Yahoo Finance). Ordinary investors usually buy commodities through ETFs, whose returns can differ because of contract rollover.',
 'es': 'Precio del contrato de futuros más cercano (Yahoo Finance). El inversor común suele comprar materias primas mediante ETF, cuya rentabilidad puede diferir por la renovación de contratos.',
 'pt': 'Preço do contrato futuro mais próximo (Yahoo Finance). O investidor comum costuma comprar commodities por ETFs, cujo retorno pode diferir por causa da rolagem dos contratos.',
 'de': 'Preis des nächstfälligen Futures-Kontrakts (Yahoo Finance). Privatanleger kaufen Rohstoffe meist über ETFs/ETCs, deren Rendite wegen des Rollens der Kontrakte abweichen kann.',
 'fr': 'Prix du contrat à terme le plus proche (Yahoo Finance). Les particuliers achètent souvent les matières premières via des ETF, dont le rendement peut différer à cause du roulement des contrats.',
 'it': 'Prezzo del future con scadenza più vicina (Yahoo Finance). Il piccolo investitore di solito compra materie prime tramite ETF/ETC, il cui rendimento può differire per il rollover dei contratti.',
 'pl': 'Cena najbliższego kontraktu terminowego (Yahoo Finance). Zwykły inwestor kupuje surowce zwykle przez ETF, których wynik może się różnić z powodu rolowania kontraktów.',
 'tr': 'En yakın vadeli kontratın fiyatı (Yahoo Finance). Bireysel yatırımcı emtiaları genellikle ETF ile alır; kontrat devri nedeniyle getiri farklı olabilir.',
 'nl': 'Prijs van het eerstvolgende futurescontract (Yahoo Finance). Particuliere beleggers kopen grondstoffen meestal via ETF’s, waarvan het rendement door het doorrollen van contracten kan afwijken.',
 'ru': 'Цена ближайшего фьючерса (Yahoo Finance). Обычный инвестор чаще покупает сырьё через ETF — их доходность может отличаться из-за перекладки контрактов.',
 'id': 'Harga kontrak berjangka terdekat (Yahoo Finance). Investor biasa umumnya membeli komoditas lewat ETF, yang imbal hasilnya bisa berbeda karena perpindahan kontrak (rollover).',
 'vi': 'Giá hợp đồng tương lai kỳ hạn gần nhất (Yahoo Finance). Nhà đầu tư thông thường thường mua hàng hóa qua ETF, lợi nhuận có thể khác do việc chuyển kỳ hợp đồng.',
 'th': 'ราคาสัญญาฟิวเจอร์สเดือนใกล้สุด (Yahoo Finance) นักลงทุนทั่วไปมักซื้อสินค้าโภคภัณฑ์ผ่าน ETF ซึ่งผลตอบแทนอาจต่างออกไปเพราะการโรลสัญญา',
 'hi': 'निकटतम फ्यूचर्स अनुबंध का भाव (Yahoo Finance)। आम निवेशक आमतौर पर कमोडिटी ETF के जरिए खरीदते हैं, जिनका रिटर्न अनुबंध रोलओवर के कारण अलग हो सकता है।',
 'ja': '期近の先物価格（Yahoo Finance）。個人投資家は通常ETFでコモディティを買いますが、限月の乗り換え（ロール）によりリターンは異なる場合があります。',
 'ko': '최근월물 선물 가격(Yahoo Finance). 일반 투자자는 보통 ETF로 원자재에 투자하며, 롤오버 때문에 수익률이 다를 수 있습니다.',
 'zh': '近月期货合约价格（Yahoo Finance）。普通投资者通常通过ETF投资大宗商品，因合约展期，其收益可能与此不同。',
 'ar': 'سعر أقرب عقد آجل (Yahoo Finance). يشتري المستثمر العادي السلع عادةً عبر صناديق ETF، وقد يختلف عائدها بسبب تدوير العقود.',
 'fil': 'Presyo ng pinakamalapit na futures contract (Yahoo Finance). Karaniwang bumibili ng kalakal ang ordinaryong investor sa pamamagitan ng ETF, na maaaring iba ang kita dahil sa rollover ng kontrata.',
}

# Data-driven "About" text for assets without a written profile or exchange description.
# Placeholders: {name} {tk} {cat} {since} {hi} {hid} {dd} {pos} {n} {by} {br} {wy} {wr}
AB = {
 'uk': ('{name} ({tk}) — категорія «{cat}». Історія ціни на WhatIfStack: з {since}.', 'Найвище місячне закриття — {hi} ({hid}); зараз ціна на {dd} нижча за цей пік.', 'Ціна нині на піку свого місячного графіка ({hi}).', 'За останні {n} місяців {pos} закрилися в плюс.', 'Найкращий рік — {by} ({br}), найгірший — {wy} ({wr}).'),
 'en': ('{name} ({tk}) is in the “{cat}” category. Price history on WhatIfStack: since {since}.', 'Its highest monthly close was {hi} ({hid}); the price is now {dd} below that peak.', 'The price is at the top of its monthly chart ({hi}).', 'Of the last {n} months, {pos} closed higher.', 'Best year: {by} ({br}); worst: {wy} ({wr}).'),
 'es': ('{name} ({tk}) pertenece a la categoría «{cat}». Historial de precios en WhatIfStack: desde {since}.', 'Su cierre mensual más alto fue {hi} ({hid}); ahora el precio está {dd} por debajo de ese máximo.', 'El precio está en el máximo de su gráfico mensual ({hi}).', 'De los últimos {n} meses, {pos} cerraron al alza.', 'Mejor año: {by} ({br}); peor: {wy} ({wr}).'),
 'pt': ('{name} ({tk}) está na categoria “{cat}”. Histórico de preços no WhatIfStack: desde {since}.', 'O maior fechamento mensal foi {hi} ({hid}); hoje o preço está {dd} abaixo desse pico.', 'O preço está no topo do gráfico mensal ({hi}).', 'Dos últimos {n} meses, {pos} fecharam em alta.', 'Melhor ano: {by} ({br}); pior: {wy} ({wr}).'),
 'de': ('{name} ({tk}) gehört zur Kategorie „{cat}“. Kursverlauf auf WhatIfStack: seit {since}.', 'Der höchste Monatsschluss lag bei {hi} ({hid}); aktuell notiert der Kurs {dd} darunter.', 'Der Kurs steht am Hoch seines Monatscharts ({hi}).', 'Von den letzten {n} Monaten schlossen {pos} im Plus.', 'Bestes Jahr: {by} ({br}); schlechtestes: {wy} ({wr}).'),
 'fr': ('{name} ({tk}) fait partie de la catégorie « {cat} ». Historique des prix sur WhatIfStack : depuis {since}.', 'Sa plus haute clôture mensuelle était de {hi} ({hid}) ; le prix est aujourd’hui {dd} en dessous de ce sommet.', 'Le prix est au plus haut de son graphique mensuel ({hi}).', 'Sur les {n} derniers mois, {pos} ont clôturé en hausse.', 'Meilleure année : {by} ({br}) ; pire : {wy} ({wr}).'),
 'it': ('{name} ({tk}) rientra nella categoria «{cat}». Storico dei prezzi su WhatIfStack: dal {since}.', 'La chiusura mensile più alta è stata {hi} ({hid}); oggi il prezzo è {dd} sotto quel picco.', 'Il prezzo è al massimo del suo grafico mensile ({hi}).', 'Degli ultimi {n} mesi, {pos} hanno chiuso in rialzo.', 'Anno migliore: {by} ({br}); peggiore: {wy} ({wr}).'),
 'pl': ('{name} ({tk}) należy do kategorii „{cat}”. Historia cen na WhatIfStack: od {since}.', 'Najwyższe zamknięcie miesiąca: {hi} ({hid}); obecnie cena jest {dd} poniżej tego szczytu.', 'Cena jest na szczycie wykresu miesięcznego ({hi}).', 'Z ostatnich {n} miesięcy {pos} zamknęło się na plusie.', 'Najlepszy rok: {by} ({br}); najgorszy: {wy} ({wr}).'),
 'tr': ('{name} ({tk}) “{cat}” kategorisinde. WhatIfStack’te fiyat geçmişi: {since} itibarıyla.', 'En yüksek aylık kapanış {hi} ({hid}); fiyat şu anda bu zirvenin {dd} altında.', 'Fiyat aylık grafiğinin zirvesinde ({hi}).', 'Son {n} ayın {pos} tanesi yükselişle kapandı.', 'En iyi yıl: {by} ({br}); en kötü: {wy} ({wr}).'),
 'nl': ('{name} ({tk}) valt in de categorie “{cat}”. Koershistorie op WhatIfStack: sinds {since}.', 'Het hoogste maandslot was {hi} ({hid}); de koers staat nu {dd} onder die top.', 'De koers staat op de top van de maandgrafiek ({hi}).', 'Van de laatste {n} maanden sloten er {pos} hoger.', 'Beste jaar: {by} ({br}); slechtste: {wy} ({wr}).'),
 'ru': ('{name} ({tk}) — категория «{cat}». История цены на WhatIfStack: с {since}.', 'Максимальное месячное закрытие — {hi} ({hid}); сейчас цена на {dd} ниже этого пика.', 'Цена сейчас на максимуме своего месячного графика ({hi}).', 'Из последних {n} месяцев {pos} закрылись в плюс.', 'Лучший год — {by} ({br}), худший — {wy} ({wr}).'),
 'id': ('{name} ({tk}) termasuk kategori “{cat}”. Riwayat harga di WhatIfStack: sejak {since}.', 'Penutupan bulanan tertinggi {hi} ({hid}); harga kini {dd} di bawah puncak itu.', 'Harga berada di puncak grafik bulanannya ({hi}).', 'Dari {n} bulan terakhir, {pos} ditutup naik.', 'Tahun terbaik: {by} ({br}); terburuk: {wy} ({wr}).'),
 'vi': ('{name} ({tk}) thuộc nhóm “{cat}”. Lịch sử giá trên WhatIfStack: từ {since}.', 'Giá đóng cửa tháng cao nhất là {hi} ({hid}); hiện giá thấp hơn đỉnh đó {dd}.', 'Giá đang ở đỉnh của biểu đồ tháng ({hi}).', 'Trong {n} tháng gần nhất, {pos} tháng đóng cửa tăng.', 'Năm tốt nhất: {by} ({br}); tệ nhất: {wy} ({wr}).'),
 'th': ('{name} ({tk}) อยู่ในหมวด “{cat}” มีประวัติราคาบน WhatIfStack ตั้งแต่ {since}', 'ราคาปิดรายเดือนสูงสุดคือ {hi} ({hid}) ตอนนี้ราคาต่ำกว่าจุดสูงสุดนั้น {dd}', 'ราคาอยู่ที่จุดสูงสุดของกราฟรายเดือน ({hi})', 'ใน {n} เดือนล่าสุด มี {pos} เดือนที่ปิดบวก', 'ปีที่ดีที่สุด: {by} ({br}) แย่ที่สุด: {wy} ({wr})'),
 'hi': ('{name} ({tk}) “{cat}” श्रेणी में है। WhatIfStack पर कीमत का इतिहास: {since} से।', 'सबसे ऊँचा मासिक क्लोज़ {hi} ({hid}) था; अभी कीमत उस शिखर से {dd} नीचे है।', 'कीमत अपने मासिक चार्ट के शिखर पर है ({hi})।', 'पिछले {n} महीनों में से {pos} बढ़त के साथ बंद हुए।', 'सबसे अच्छा साल: {by} ({br}); सबसे खराब: {wy} ({wr})।'),
 'ja': ('{name}（{tk}）は「{cat}」カテゴリーです。WhatIfStackの価格履歴：{since}から。', '月末終値の最高値は{hi}（{hid}）で、現在の価格はそこから{dd}下にあります。', '価格は月足チャートの最高値にあります（{hi}）。', '直近{n}か月のうち{pos}か月が上昇で終わりました。', '最良の年：{by}（{br}）、最悪の年：{wy}（{wr}）。'),
 'ko': ('{name}({tk})는 “{cat}” 카테고리입니다. WhatIfStack 가격 기록: {since}부터.', '최고 월말 종가는 {hi}({hid})였고, 현재 가격은 그 고점보다 {dd} 낮습니다.', '가격이 월봉 차트의 최고점에 있습니다({hi}).', '최근 {n}개월 중 {pos}개월이 상승 마감했습니다.', '최고의 해: {by}({br}), 최악의 해: {wy}({wr}).'),
 'zh': ('{name}（{tk}）属于“{cat}”类别。WhatIfStack 价格历史：自 {since} 起。', '最高月收盘价为 {hi}（{hid}）；目前价格比该高点低 {dd}。', '价格处于月线图最高点（{hi}）。', '最近 {n} 个月中有 {pos} 个月收涨。', '最佳年份：{by}（{br}）；最差：{wy}（{wr}）。'),
 'ar': ('{name} ({tk}) ضمن فئة «{cat}». سجل الأسعار على WhatIfStack: منذ {since}.', 'أعلى إغلاق شهري كان {hi} ({hid})؛ والسعر الآن أقل من تلك القمة بنسبة {dd}.', 'السعر عند قمة رسمه البياني الشهري ({hi}).', 'من آخر {n} شهرًا، أُغلق {pos} على ارتفاع.', 'أفضل عام: {by} ({br})؛ والأسوأ: {wy} ({wr}).'),
 'fil': ('Ang {name} ({tk}) ay nasa kategoryang “{cat}”. Kasaysayan ng presyo sa WhatIfStack: mula {since}.', 'Ang pinakamataas na buwanang sara ay {hi} ({hid}); ngayon ay {dd} na mas mababa ang presyo sa tuktok na iyon.', 'Nasa tuktok ng buwanang chart ang presyo ({hi}).', 'Sa huling {n} buwan, {pos} ang nagsara nang mas mataas.', 'Pinakamagandang taon: {by} ({br}); pinakamasama: {wy} ({wr}).'),
}
assert len(AB) == 20 and all(len(v) == 5 for v in AB.values())

# Own monthly price chart for assets without a free TradingView symbol: (title, "all time")
CH = {
 'uk': ('Графік ціни (щомісяця)', 'Усе'), 'en': ('Price chart (monthly)', 'All'), 'ru': ('График цены (помесячно)', 'Всё'),
 'es': ('Gráfico de precio (mensual)', 'Todo'), 'pt': ('Gráfico de preço (mensal)', 'Tudo'), 'de': ('Kursverlauf (monatlich)', 'Alles'),
 'fr': ('Graphique du prix (mensuel)', 'Tout'), 'it': ('Grafico del prezzo (mensile)', 'Tutto'), 'pl': ('Wykres ceny (miesięczny)', 'Całość'),
 'tr': ('Fiyat grafiği (aylık)', 'Tümü'), 'nl': ('Koersgrafiek (maandelijks)', 'Alles'), 'id': ('Grafik harga (bulanan)', 'Semua'),
 'vi': ('Biểu đồ giá (theo tháng)', 'Tất cả'), 'th': ('กราฟราคา (รายเดือน)', 'ทั้งหมด'), 'hi': ('कीमत चार्ट (मासिक)', 'सभी'),
 'ja': ('価格チャート（月次）', '全期間'), 'ko': ('가격 차트 (월별)', '전체'), 'zh': ('价格走势（月度）', '全部'),
 'ar': ('مخطط السعر (شهري)', 'الكل'), 'fil': ('Tsart ng presyo (buwanan)', 'Lahat'),
}
