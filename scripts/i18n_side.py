# «About» card next to the chart (owner 2026-11-28: alive, with scales and link icons): 1-year range, low, high, share of max supply issued, distance to the record
_K = ['rng', 'lo', 'hi', 'issued', 'torec']
_T = {
    'en': ['1-year range', 'Low', 'High', '{p} of the max supply issued', '{p} below the record'],
    'uk': ['Діапазон за рік', 'Мін.', 'Макс.', 'Випущено {p} від максимуму', 'До рекорду: {p}'],
    'ru': ['Диапазон за год', 'Мин.', 'Макс.', 'Выпущено {p} от максимума', 'До рекорда: {p}'],
    'es': ['Rango de 1 año', 'Mín.', 'Máx.', 'Emitido el {p} del suministro máximo', '{p} por debajo del récord'],
    'pt': ['Faixa de 1 ano', 'Mín.', 'Máx.', '{p} da oferta máxima emitida', '{p} abaixo do recorde'],
    'de': ['Spanne 1 Jahr', 'Tief', 'Hoch', '{p} des Maximalangebots ausgegeben', '{p} unter dem Rekord'],
    'fr': ['Fourchette sur 1 an', 'Bas', 'Haut', '{p} de l’offre maximale émise', '{p} sous le record'],
    'it': ['Intervallo 1 anno', 'Min', 'Max', 'Emesso il {p} dell’offerta massima', '{p} sotto il record'],
    'pl': ['Zakres z roku', 'Min.', 'Maks.', 'Wyemitowano {p} maksymalnej podaży', 'Do rekordu: {p}'],
    'tr': ['1 yıllık aralık', 'Düşük', 'Yüksek', 'Maksimum arzın {p} kadarı çıkarıldı', 'Rekorun {p} altında'],
    'nl': ['Bereik 1 jaar', 'Laag', 'Hoog', '{p} van het maximale aanbod uitgegeven', '{p} onder het record'],
    'id': ['Rentang 1 tahun', 'Terendah', 'Tertinggi', '{p} dari pasokan maksimum telah beredar', '{p} di bawah rekor'],
    'vi': ['Biên độ 1 năm', 'Thấp', 'Cao', 'Đã phát hành {p} nguồn cung tối đa', 'Thấp hơn kỷ lục {p}'],
    'th': ['ช่วงราคา 1 ปี', 'ต่ำสุด', 'สูงสุด', 'ออกแล้ว {p} ของอุปทานสูงสุด', 'ต่ำกว่าสถิติ {p}'],
    'hi': ['1 साल की रेंज', 'न्यूनतम', 'अधिकतम', 'अधिकतम सप्लाई का {p} जारी', 'रिकॉर्ड से {p} नीचे'],
    'ja': ['1年のレンジ', '安値', '高値', '最大供給量の{p}が発行済み', '最高値まで{p}'],
    'ko': ['1년 범위', '최저', '최고', '최대 공급량의 {p} 발행', '최고가 대비 {p}'],
    'zh': ['1 年区间', '最低', '最高', '已发行最大供应量的 {p}', '距历史最高 {p}'],
    'ar': ['نطاق سنة', 'الأدنى', 'الأعلى', 'صدر {p} من الحد الأقصى للمعروض', 'أدنى من القمة بنسبة {p}'],
    'fil': ['Saklaw sa 1 taon', 'Pinakamababa', 'Pinakamataas', '{p} ng max supply ang nailabas na', '{p} mas mababa sa record'],
}
SIDE = {lg: dict(zip(_K, v)) for lg, v in _T.items()}

# owner 2026-11-28: «how does the scale count?» — show the price now and say it is built from monthly closing prices
_N = {
    'en': ('Now', 'by monthly closing prices'), 'uk': ('Зараз', 'за цінами закриття місяців'), 'ru': ('Сейчас', 'по ценам закрытия месяцев'),
    'es': ('Ahora', 'según los cierres mensuales'), 'pt': ('Agora', 'pelos fechamentos mensais'), 'de': ('Jetzt', 'nach Monatsschlusskursen'),
    'fr': ('Maintenant', 'selon les clôtures mensuelles'), 'it': ('Ora', 'in base alle chiusure mensili'), 'pl': ('Teraz', 'wg cen zamknięcia miesięcy'),
    'tr': ('Şimdi', 'aylık kapanış fiyatlarına göre'), 'nl': ('Nu', 'op basis van maandslotkoersen'), 'id': ('Sekarang', 'berdasarkan harga penutupan bulanan'),
    'vi': ('Hiện tại', 'theo giá đóng cửa hằng tháng'), 'th': ('ตอนนี้', 'ตามราคาปิดรายเดือน'), 'hi': ('अभी', 'मासिक क्लोज़िंग कीमतों के आधार पर'),
    'ja': ('現在', '月末終値ベース'), 'ko': ('현재', '월말 종가 기준'), 'zh': ('现在', '按月收盘价'), 'ar': ('الآن', 'حسب أسعار الإغلاق الشهرية'),
    'fil': ('Ngayon', 'batay sa buwanang closing price'),
}
for _lg, (_a, _b) in _N.items():
    SIDE[_lg].update(now=_a, mnote=_b)
