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
