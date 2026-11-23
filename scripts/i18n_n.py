"""News aggregator + Insights strings, 20 languages.
n_nav, n_h1, n_d, n_all, n_note, tags (10, '|'), i_nav (blog renamed to Insights), cats ('All|Analytics|Guides|Reports'), more, about"""
K = 'n_nav n_h1 n_d n_all n_note tags i_nav cats more about src own live'.split()
N = {k: dict(zip(K, v)) for k, v in {
 'en': ('News', 'Crypto news today', 'Latest crypto and market headlines from CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine and other leading outlets, in one feed. Updated every 10 minutes.', 'All', 'Headlines link to the original articles. We do not copy their texts.', 'Bitcoin|Ethereum|ETF|Regulation|DeFi|Stablecoins|Solana|XRP|Markets|Hacks', 'Insights', 'All|Analytics|Guides|Reports', 'Show more', 'About & methodology', 'Sources', 'WhatIfStack news', 'Headlines from other outlets'),
 'uk': ('Новини', 'Новини криптовалют сьогодні', 'Свіжі новини крипти й ринків з CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine та інших провідних видань в одній стрічці. Оновлення кожні 10 хвилин.', 'Усе', 'Заголовки ведуть на оригінальні статті. Ми не копіюємо їхні тексти.', 'Біткоїн|Ethereum|ETF|Регулювання|DeFi|Стейблкоїни|Solana|XRP|Ринок|Злами', 'Аналітика', 'Усе|Аналітика|Гайди|Звіти', 'Показати ще', 'Про нас і методологія', 'Джерела', 'Новини WhatIfStack', 'Заголовки інших видань'),
 'ru': ('Новости', 'Новости криптовалют сегодня', 'Свежие новости крипты и рынков из CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine и других ведущих изданий в одной ленте. Обновление каждые 10 минут.', 'Все', 'Заголовки ведут на оригинальные статьи. Мы не копируем их тексты.', 'Биткоин|Ethereum|ETF|Регулирование|DeFi|Стейблкоины|Solana|XRP|Рынок|Взломы', 'Аналитика', 'Все|Аналитика|Гайды|Отчёты', 'Показать ещё', 'О нас и методология', 'Источники', 'Новости WhatIfStack', 'Заголовки других изданий'),
 'es': ('Noticias', 'Noticias de criptomonedas hoy', 'Los últimos titulares de cripto y mercados de CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine y otros grandes medios en un solo feed. Se actualiza cada 10 minutos.', 'Todo', 'Los titulares enlazan a los artículos originales. No copiamos sus textos.', 'Bitcoin|Ethereum|ETF|Regulación|DeFi|Stablecoins|Solana|XRP|Mercados|Hackeos', 'Análisis', 'Todo|Análisis|Guías|Informes', 'Ver más', 'Sobre nosotros y metodología', 'Fuentes', 'Noticias de WhatIfStack', 'Titulares de otros medios'),
 'pt': ('Notícias', 'Notícias de criptomoedas hoje', 'As últimas manchetes de cripto e mercados da CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine e outros grandes veículos em um só feed. Atualizado a cada 10 minutos.', 'Tudo', 'As manchetes levam aos artigos originais. Não copiamos seus textos.', 'Bitcoin|Ethereum|ETF|Regulação|DeFi|Stablecoins|Solana|XRP|Mercados|Ataques', 'Análises', 'Tudo|Análises|Guias|Relatórios', 'Ver mais', 'Sobre e metodologia', 'Fontes', 'Notícias WhatIfStack', 'Manchetes de outros veículos'),
 'de': ('News', 'Krypto-News heute', 'Die neuesten Krypto- und Marktschlagzeilen von CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine und anderen führenden Medien in einem Feed. Alle 10 Minuten aktualisiert.', 'Alle', 'Die Schlagzeilen verlinken auf die Originalartikel. Wir kopieren keine Texte.', 'Bitcoin|Ethereum|ETF|Regulierung|DeFi|Stablecoins|Solana|XRP|Märkte|Hacks', 'Analysen', 'Alle|Analysen|Ratgeber|Berichte', 'Mehr anzeigen', 'Über uns & Methodik', 'Quellen', 'WhatIfStack News', 'Schlagzeilen anderer Medien'),
 'fr': ('Actualités', 'Actualités crypto du jour', 'Les derniers titres crypto et marchés de CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine et d’autres grands médias dans un seul fil. Mis à jour toutes les 10 minutes.', 'Tout', 'Les titres renvoient aux articles originaux. Nous ne copions pas leurs textes.', 'Bitcoin|Ethereum|ETF|Régulation|DeFi|Stablecoins|Solana|XRP|Marchés|Piratages', 'Analyses', 'Tout|Analyses|Guides|Rapports', 'Voir plus', 'À propos et méthodologie', 'Sources', 'Actualités WhatIfStack', 'Titres d’autres médias'),
 'it': ('Notizie', 'Notizie crypto di oggi', 'Gli ultimi titoli su cripto e mercati da CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine e altre testate in un unico feed. Aggiornato ogni 10 minuti.', 'Tutto', 'I titoli rimandano agli articoli originali. Non copiamo i loro testi.', 'Bitcoin|Ethereum|ETF|Regolamentazione|DeFi|Stablecoin|Solana|XRP|Mercati|Attacchi', 'Analisi', 'Tutto|Analisi|Guide|Report', 'Mostra altro', 'Chi siamo e metodologia', 'Fonti', 'Notizie WhatIfStack', 'Titoli di altre testate'),
 'pl': ('Wiadomości', 'Wiadomości krypto dziś', 'Najnowsze nagłówki o krypto i rynkach z CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine i innych czołowych mediów w jednym kanale. Aktualizacja co 10 minut.', 'Wszystko', 'Nagłówki prowadzą do oryginalnych artykułów. Nie kopiujemy ich treści.', 'Bitcoin|Ethereum|ETF|Regulacje|DeFi|Stablecoiny|Solana|XRP|Rynki|Włamania', 'Analizy', 'Wszystko|Analizy|Poradniki|Raporty', 'Pokaż więcej', 'O nas i metodologia', 'Źródła', 'Wiadomości WhatIfStack', 'Nagłówki innych mediów'),
 'tr': ('Haberler', 'Bugünkü kripto haberleri', 'CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine ve diğer önde gelen yayınlardan en son kripto ve piyasa başlıkları tek akışta. Her 10 dakikada güncellenir.', 'Tümü', 'Başlıklar orijinal makalelere yönlendirir. Metinlerini kopyalamıyoruz.', 'Bitcoin|Ethereum|ETF|Düzenleme|DeFi|Stablecoin|Solana|XRP|Piyasalar|Hack', 'Analiz', 'Tümü|Analiz|Rehberler|Raporlar', 'Daha fazla', 'Hakkımızda ve metodoloji', 'Kaynaklar', 'WhatIfStack haberleri', 'Diğer yayınlardan başlıklar'),
 'nl': ('Nieuws', 'Cryptonieuws vandaag', 'De nieuwste crypto- en marktkoppen van CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine en andere toonaangevende media in één feed. Elke 10 minuten bijgewerkt.', 'Alles', 'De koppen linken naar de originele artikelen. Wij kopiëren hun teksten niet.', 'Bitcoin|Ethereum|ETF|Regelgeving|DeFi|Stablecoins|Solana|XRP|Markten|Hacks', 'Analyses', 'Alles|Analyses|Gidsen|Rapporten', 'Meer tonen', 'Over ons en methodologie', 'Bronnen', 'WhatIfStack-nieuws', 'Koppen van andere media'),
 'id': ('Berita', 'Berita kripto hari ini', 'Berita kripto dan pasar terbaru dari CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine, dan media terkemuka lainnya dalam satu feed. Diperbarui setiap 10 menit.', 'Semua', 'Judul mengarah ke artikel asli. Kami tidak menyalin teksnya.', 'Bitcoin|Ethereum|ETF|Regulasi|DeFi|Stablecoin|Solana|XRP|Pasar|Peretasan', 'Analisis', 'Semua|Analisis|Panduan|Laporan', 'Tampilkan lagi', 'Tentang kami & metodologi', 'Sumber', 'Berita WhatIfStack', 'Judul dari media lain'),
 'vi': ('Tin tức', 'Tin tức crypto hôm nay', 'Tiêu đề mới nhất về crypto và thị trường từ CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine và các trang hàng đầu khác trong một luồng. Cập nhật mỗi 10 phút.', 'Tất cả', 'Tiêu đề dẫn đến bài viết gốc. Chúng tôi không sao chép nội dung.', 'Bitcoin|Ethereum|ETF|Pháp lý|DeFi|Stablecoin|Solana|XRP|Thị trường|Hack', 'Phân tích', 'Tất cả|Phân tích|Hướng dẫn|Báo cáo', 'Xem thêm', 'Giới thiệu & phương pháp', 'Nguồn', 'Tin WhatIfStack', 'Tiêu đề từ các trang khác'),
 'th': ('ข่าว', 'ข่าวคริปโตวันนี้', 'พาดหัวข่าวคริปโตและตลาดล่าสุดจาก CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine และสื่อชั้นนำอื่น ๆ ในฟีดเดียว อัปเดตทุก 10 นาที', 'ทั้งหมด', 'พาดหัวลิงก์ไปยังบทความต้นฉบับ เราไม่คัดลอกเนื้อหา', 'บิตคอยน์|Ethereum|ETF|กฎระเบียบ|DeFi|Stablecoin|Solana|XRP|ตลาด|แฮ็ก', 'บทวิเคราะห์', 'ทั้งหมด|บทวิเคราะห์|คู่มือ|รายงาน', 'แสดงเพิ่ม', 'เกี่ยวกับเราและวิธีการ', 'แหล่งที่มา', 'ข่าว WhatIfStack', 'พาดหัวจากสื่ออื่น'),
 'hi': ('समाचार', 'आज की क्रिप्टो खबरें', 'CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine और अन्य प्रमुख प्रकाशनों से क्रिप्टो और बाज़ार की ताज़ा सुर्खियाँ एक फ़ीड में। हर 10 मिनट में अपडेट।', 'सभी', 'सुर्खियाँ मूल लेखों पर ले जाती हैं। हम उनका टेक्स्ट कॉपी नहीं करते।', 'बिटकॉइन|Ethereum|ETF|नियमन|DeFi|स्टेबलकॉइन|Solana|XRP|बाज़ार|हैक', 'विश्लेषण', 'सभी|विश्लेषण|गाइड|रिपोर्ट', 'और दिखाएँ', 'हमारे बारे में और कार्यप्रणाली', 'स्रोत', 'WhatIfStack समाचार', 'दूसरे प्रकाशनों की सुर्खियाँ'),
 'ja': ('ニュース', '今日の暗号資産ニュース', 'CoinDesk、Cointelegraph、Decrypt、The Block、Bitcoin Magazineなど主要メディアの最新見出しを1つのフィードで。10分ごとに更新。', 'すべて', '見出しは元記事にリンクしています。本文は転載していません。', 'ビットコイン|イーサリアム|ETF|規制|DeFi|ステーブルコイン|ソラナ|XRP|市場|ハッキング', 'インサイト', 'すべて|分析|ガイド|レポート', 'もっと見る', '運営者と方法論', '出典', 'WhatIfStackニュース', '他メディアの見出し'),
 'ko': ('뉴스', '오늘의 암호화폐 뉴스', 'CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine 등 주요 매체의 최신 헤드라인을 하나의 피드로. 10분마다 업데이트.', '전체', '헤드라인은 원문 기사로 연결됩니다. 본문은 복사하지 않습니다.', '비트코인|이더리움|ETF|규제|DeFi|스테이블코인|솔라나|XRP|시장|해킹', '인사이트', '전체|분석|가이드|리포트', '더 보기', '소개 및 방법론', '출처', 'WhatIfStack 뉴스', '다른 매체 헤드라인'),
 'zh': ('新闻', '今日加密货币新闻', '汇集 CoinDesk、Cointelegraph、Decrypt、The Block、Bitcoin Magazine 等主流媒体的最新加密与市场标题，每10分钟更新。', '全部', '标题链接到原文，我们不转载正文。', '比特币|以太坊|ETF|监管|DeFi|稳定币|Solana|XRP|市场|黑客', '洞察', '全部|分析|指南|报告', '显示更多', '关于我们与方法论', '来源', 'WhatIfStack 新闻', '其他媒体标题'),
 'ar': ('الأخبار', 'أخبار العملات المشفرة اليوم', 'أحدث عناوين العملات المشفرة والأسواق من CoinDesk وCointelegraph وDecrypt وThe Block وBitcoin Magazine وغيرها في موجز واحد. تحديث كل 10 دقائق.', 'الكل', 'العناوين ترتبط بالمقالات الأصلية ولا ننسخ نصوصها.', 'بيتكوين|إيثريوم|ETF|التنظيم|DeFi|العملات المستقرة|سولانا|XRP|الأسواق|الاختراقات', 'تحليلات', 'الكل|تحليلات|أدلة|تقارير', 'عرض المزيد', 'من نحن والمنهجية', 'المصادر', 'أخبار WhatIfStack', 'عناوين من وسائل أخرى'),
 'fil': ('Balita', 'Crypto news ngayon', 'Pinakabagong headline sa crypto at merkado mula sa CoinDesk, Cointelegraph, Decrypt, The Block, Bitcoin Magazine at iba pang nangungunang outlet sa iisang feed. Ina-update kada 10 minuto.', 'Lahat', 'Ang mga headline ay naka-link sa orihinal na artikulo. Hindi namin kinokopya ang teksto.', 'Bitcoin|Ethereum|ETF|Regulasyon|DeFi|Stablecoins|Solana|XRP|Merkado|Hacks', 'Insights', 'Lahat|Analytics|Gabay|Ulat', 'Ipakita pa', 'Tungkol at metodolohiya', 'Mga pinagmulan', 'Balita ng WhatIfStack', 'Mga headline mula sa ibang outlet'),
}.items()}
assert all(len(v['tags'].split('|')) == 10 and len(v['cats'].split('|')) == 4 for v in N.values())

# footer column titles: popular | markets | follow us
FOOT = {
 'en': ('Popular', 'Markets', 'Follow us'), 'uk': ('Популярне', 'Ринки', 'Ми в соцмережах'), 'ru': ('Популярное', 'Рынки', 'Мы в соцсетях'),
 'es': ('Popular', 'Mercados', 'Síguenos'), 'pt': ('Popular', 'Mercados', 'Siga-nos'), 'de': ('Beliebt', 'Märkte', 'Folge uns'),
 'fr': ('Populaire', 'Marchés', 'Suivez-nous'), 'it': ('Popolari', 'Mercati', 'Seguici'), 'pl': ('Popularne', 'Rynki', 'Obserwuj nas'),
 'tr': ('Popüler', 'Piyasalar', 'Bizi takip et'), 'nl': ('Populair', 'Markten', 'Volg ons'), 'id': ('Populer', 'Pasar', 'Ikuti kami'),
 'vi': ('Phổ biến', 'Thị trường', 'Theo dõi chúng tôi'), 'th': ('ยอดนิยม', 'ตลาด', 'ติดตามเรา'), 'hi': ('लोकप्रिय', 'बाज़ार', 'हमें फ़ॉलो करें'),
 'ja': ('人気', 'マーケット', 'フォロー'), 'ko': ('인기', '시장', '팔로우'), 'zh': ('热门', '市场', '关注我们'),
 'ar': ('الأكثر شيوعًا', 'الأسواق', 'تابعنا'), 'fil': ('Popular', 'Mga merkado', 'Sundan kami'),
}

SHARE = {'en': 'Share', 'uk': 'Поділитися', 'ru': 'Поделиться', 'es': 'Compartir', 'pt': 'Compartilhar', 'de': 'Teilen', 'fr': 'Partager',
         'it': 'Condividi', 'pl': 'Udostępnij', 'tr': 'Paylaş', 'nl': 'Delen', 'id': 'Bagikan', 'vi': 'Chia sẻ', 'th': 'แชร์', 'hi': 'शेयर करें',
         'ja': '共有', 'ko': '공유', 'zh': '分享', 'ar': 'مشاركة', 'fil': 'Ibahagi'}

# "What's happening with X" rubric: (tag label, asset-page block title with {name})
HOT = {
 'en': ('Why it moves', "What's happening with {name}"), 'uk': ('Чому рухається', 'Що відбувається з {name}'),
 'ru': ('Почему движется', 'Что происходит с {name}'), 'es': ('Por qué se mueve', 'Qué está pasando con {name}'),
 'pt': ('Por que se move', 'O que está acontecendo com {name}'), 'de': ('Warum es sich bewegt', 'Was ist los mit {name}'),
 'fr': ('Pourquoi ça bouge', 'Que se passe-t-il avec {name}'), 'it': ('Perché si muove', 'Cosa succede a {name}'),
 'pl': ('Dlaczego się rusza', 'Co się dzieje z {name}'), 'tr': ('Neden hareket ediyor', "{name} tarafında neler oluyor"),
 'nl': ('Waarom het beweegt', 'Wat is er aan de hand met {name}'), 'id': ('Kenapa bergerak', 'Apa yang terjadi dengan {name}'),
 'vi': ('Vì sao biến động', 'Chuyện gì đang xảy ra với {name}'), 'th': ('ทำไมราคาเคลื่อนไหว', 'เกิดอะไรขึ้นกับ {name}'),
 'hi': ('क्यों हिल रहा है', '{name} के साथ क्या हो रहा है'), 'ja': ('値動きの理由', '{name}に何が起きているか'),
 'ko': ('왜 움직이나', '{name}에 무슨 일이'), 'zh': ('为何波动', '{name}发生了什么'),
 'ar': ('لماذا يتحرك', 'ماذا يحدث مع {name}'), 'fil': ('Bakit gumagalaw', 'Ano ang nangyayari sa {name}'),
}
assert len(HOT) == 20

# owner 2026-11-23: other outlets' headlines removed from /news/ — the lead describes our own news only
_ND = dict(
 en='What is moving crypto, stocks and gold today: short news in plain language with real numbers, sources and charts, several times a day.',
 uk='Що рухає крипту, акції й золото сьогодні: короткі новини простою мовою з реальними цифрами, джерелами й графіками — кілька разів на день.',
 ru='Что двигает крипту, акции и золото сегодня: короткие новости простым языком с реальными цифрами, источниками и графиками — несколько раз в день.',
 es='Qué mueve hoy las cripto, las acciones y el oro: noticias breves y claras con cifras reales, fuentes y gráficos, varias veces al día.',
 de='Was Krypto, Aktien und Gold heute bewegt: kurze News in einfacher Sprache mit echten Zahlen, Quellen und Charts, mehrmals täglich.',
 pt='O que move cripto, ações e ouro hoje: notícias curtas em linguagem simples, com números reais, fontes e gráficos, várias vezes ao dia.',
 pl='Co dziś porusza krypto, akcjami i złotem: krótkie wiadomości prostym językiem z prawdziwymi liczbami, źródłami i wykresami, kilka razy dziennie.',
 tr='Bugün kripto, hisse ve altını ne hareket ettiriyor: gerçek rakamlar, kaynaklar ve grafiklerle sade dilde kısa haberler, günde birkaç kez.',
 fr='Ce qui fait bouger la crypto, les actions et l’or aujourd’hui : des actus courtes et claires, avec chiffres réels, sources et graphiques, plusieurs fois par jour.',
 it='Cosa muove oggi cripto, azioni e oro: notizie brevi e chiare con numeri reali, fonti e grafici, più volte al giorno.',
 nl='Wat crypto, aandelen en goud vandaag beweegt: kort nieuws in gewone taal met echte cijfers, bronnen en grafieken, meerdere keren per dag.',
 id='Apa yang menggerakkan kripto, saham, dan emas hari ini: berita singkat berbahasa sederhana dengan angka nyata, sumber, dan grafik, beberapa kali sehari.',
 vi='Điều gì đang tác động đến tiền mã hóa, cổ phiếu và vàng hôm nay: tin ngắn dễ hiểu với số liệu thật, nguồn và biểu đồ, nhiều lần mỗi ngày.',
 th='อะไรขับเคลื่อนคริปโท หุ้น และทองคำวันนี้ ข่าวสั้นเข้าใจง่าย พร้อมตัวเลขจริง แหล่งที่มา และกราฟ หลายครั้งต่อวัน',
 hi='आज क्रिप्टो, शेयर और सोने को क्या हिला रहा है: असली आंकड़ों, स्रोतों और चार्ट के साथ आसान भाषा में छोटी ख़बरें, दिन में कई बार।',
 ja='暗号資産・株・金を今日動かしているもの。実際の数字、出典、チャート付きのわかりやすい短いニュースを1日に何度もお届けします。',
 ko='오늘 암호화폐, 주식, 금을 움직이는 것: 실제 수치와 출처, 차트를 담은 쉬운 짧은 뉴스를 하루에도 여러 번 전합니다.',
 zh='今天是什么在推动加密货币、股票和黄金：用通俗语言写的简短新闻，附真实数据、来源和图表，每天更新多次。',
 ar='ما الذي يحرّك العملات المشفرة والأسهم والذهب اليوم: أخبار قصيرة بلغة بسيطة مع أرقام حقيقية ومصادر ورسوم بيانية، عدة مرات يوميًا.',
 fil='Ano ang gumagalaw sa crypto, stocks at ginto ngayon: maiikling balita sa simpleng wika na may totoong numero, source at chart, ilang beses sa isang araw.',
)
for _l, _v in _ND.items():
    if _l in N:
        N[_l]['n_d'] = _v
