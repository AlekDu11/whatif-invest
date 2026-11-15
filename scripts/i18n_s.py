"""Returns heatmap on asset pages. Fields: title ({name}), median, years up, since month start, since quarter start, since year start, not closed yet, day-view note."""
K = 'title med up mtd qtd ytd open dnote'.split()
S = {k: dict(zip(K, v)) for k, v in {
 'en': ('{name}: returns by month', 'Median', 'years up', 'Month to date', 'Quarter to date', 'Year to date', 'Not closed yet', 'Daily closes from Binance, last 12 months'),
 'uk': ('{name}: дохідність по місяцях', 'Медіана', 'років у плюсі', 'З початку місяця', 'З початку кварталу', 'З початку року', 'Ще не закрито', 'Денні ціни закриття з Binance за останні 12 місяців'),
 'ru': ('{name}: доходность по месяцам', 'Медиана', 'лет в плюсе', 'С начала месяца', 'С начала квартала', 'С начала года', 'Ещё не закрыт', 'Дневные цены закрытия с Binance за последние 12 месяцев'),
 'es': ('{name}: rentabilidad por mes', 'Mediana', 'años en positivo', 'En el mes', 'En el trimestre', 'En el año', 'Aún sin cerrar', 'Cierres diarios de Binance, últimos 12 meses'),
 'pt': ('{name}: retorno por mês', 'Mediana', 'anos no positivo', 'No mês', 'No trimestre', 'No ano', 'Ainda não fechado', 'Fechamentos diários da Binance, últimos 12 meses'),
 'de': ('{name}: Rendite nach Monaten', 'Median', 'Jahre im Plus', 'Seit Monatsbeginn', 'Seit Quartalsbeginn', 'Seit Jahresbeginn', 'Noch nicht abgeschlossen', 'Tagesschlusskurse von Binance, letzte 12 Monate'),
 'fr': ('{name} : rendement par mois', 'Médiane', 'années positives', 'Depuis le début du mois', 'Depuis le début du trimestre', 'Depuis le début de l’année', 'Pas encore clôturé', 'Clôtures quotidiennes Binance, 12 derniers mois'),
 'it': ('{name}: rendimento per mese', 'Mediana', 'anni in positivo', 'Da inizio mese', 'Da inizio trimestre', 'Da inizio anno', 'Non ancora chiuso', 'Chiusure giornaliere da Binance, ultimi 12 mesi'),
 'pl': ('{name}: stopy zwrotu według miesięcy', 'Mediana', 'lat na plusie', 'Od początku miesiąca', 'Od początku kwartału', 'Od początku roku', 'Jeszcze niezamknięty', 'Dzienne zamknięcia z Binance, ostatnie 12 miesięcy'),
 'tr': ('{name}: aylara göre getiri', 'Medyan', 'yıl artıda', 'Ay başından beri', 'Çeyrek başından beri', 'Yıl başından beri', 'Henüz kapanmadı', 'Binance günlük kapanışları, son 12 ay'),
 'nl': ('{name}: rendement per maand', 'Mediaan', 'jaren in de plus', 'Sinds begin maand', 'Sinds begin kwartaal', 'Sinds begin jaar', 'Nog niet afgesloten', 'Dagelijkse slotkoersen van Binance, laatste 12 maanden'),
 'id': ('{name}: imbal hasil per bulan', 'Median', 'tahun positif', 'Sejak awal bulan', 'Sejak awal kuartal', 'Sejak awal tahun', 'Belum ditutup', 'Harga penutupan harian dari Binance, 12 bulan terakhir'),
 'vi': ('{name}: lợi nhuận theo tháng', 'Trung vị', 'năm tăng', 'Từ đầu tháng', 'Từ đầu quý', 'Từ đầu năm', 'Chưa đóng', 'Giá đóng cửa hằng ngày từ Binance, 12 tháng gần nhất'),
 'th': ('{name}: ผลตอบแทนรายเดือน', 'ค่ามัธยฐาน', 'ปีที่เป็นบวก', 'ตั้งแต่ต้นเดือน', 'ตั้งแต่ต้นไตรมาส', 'ตั้งแต่ต้นปี', 'ยังไม่ปิด', 'ราคาปิดรายวันจาก Binance 12 เดือนล่าสุด'),
 'hi': ('{name}: महीने के अनुसार रिटर्न', 'माध्यिका', 'साल बढ़त में', 'महीने की शुरुआत से', 'तिमाही की शुरुआत से', 'साल की शुरुआत से', 'अभी बंद नहीं हुआ', 'Binance से रोज़ाना बंद भाव, पिछले 12 महीने'),
 'ja': ('{name}：月別リターン', '中央値', '年がプラス', '月初来', '四半期初来', '年初来', '未確定', 'Binanceの日次終値（直近12か月）'),
 'ko': ('{name}: 월별 수익률', '중앙값', '년 상승', '월초 대비', '분기초 대비', '연초 대비', '아직 마감 전', 'Binance 일별 종가, 최근 12개월'),
 'zh': ('{name}：按月收益率', '中位数', '年上涨', '月初至今', '季初至今', '年初至今', '尚未收盘', 'Binance每日收盘价，最近12个月'),
 'ar': ('{name}: العائد حسب الشهر', 'الوسيط', 'سنوات رابحة', 'منذ بداية الشهر', 'منذ بداية الربع', 'منذ بداية العام', 'لم يُغلق بعد', 'أسعار الإغلاق اليومية من Binance لآخر 12 شهرًا'),
 'fil': ('{name}: kita kada buwan', 'Median', 'taon na positibo', 'Mula simula ng buwan', 'Mula simula ng quarter', 'Mula simula ng taon', 'Hindi pa sarado', 'Araw-araw na closing mula Binance, huling 12 buwan'),
}.items()}
assert len(S) == 20
