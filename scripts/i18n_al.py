# -*- coding: utf-8 -*-
"""Price alerts in Telegram (asset page button + popover). Keys: btn, h, up, dn, go, note."""
_K = ['btn', 'h', 'up', 'dn', 'go', 'note']
_V = {
 'uk': ['🔔 Сповіщення', 'Повідомити, коли ціна {tk}', 'підніметься вище', 'опуститься нижче', 'Увімкнути в Telegram', 'Бот @{bot} надішле повідомлення в Telegram. Безкоштовно, вимкнути — /stop.'],
 'en': ['🔔 Price alert', 'Tell me when {tk}', 'rises above', 'falls below', 'Set it in Telegram', 'The @{bot} bot will message you in Telegram. Free; turn off any time with /stop.'],
 'es': ['🔔 Alerta de precio', 'Avísame cuando {tk}', 'suba por encima de', 'baje por debajo de', 'Activar en Telegram', 'El bot @{bot} te escribirá en Telegram. Gratis; desactívalo con /stop.'],
 'pt': ['🔔 Alerta de preço', 'Avise quando {tk}', 'subir acima de', 'cair abaixo de', 'Ativar no Telegram', 'O bot @{bot} vai te avisar no Telegram. Grátis; desative com /stop.'],
 'de': ['🔔 Preisalarm', 'Benachrichtige mich, wenn {tk}', 'steigt über', 'fällt unter', 'In Telegram einrichten', 'Der Bot @{bot} schreibt dir in Telegram. Kostenlos; mit /stop jederzeit aus.'],
 'fr': ['🔔 Alerte de prix', 'Préviens-moi quand {tk}', 'dépasse', 'passe sous', 'Activer dans Telegram', 'Le bot @{bot} t’écrira sur Telegram. Gratuit ; désactive avec /stop.'],
 'it': ['🔔 Avviso di prezzo', 'Avvisami quando {tk}', 'sale sopra', 'scende sotto', 'Attiva su Telegram', 'Il bot @{bot} ti scriverà su Telegram. Gratis; disattiva con /stop.'],
 'pl': ['🔔 Alert cenowy', 'Powiadom mnie, gdy {tk}', 'wzrośnie powyżej', 'spadnie poniżej', 'Włącz w Telegramie', 'Bot @{bot} napisze do Ciebie w Telegramie. Za darmo; wyłączysz komendą /stop.'],
 'tr': ['🔔 Fiyat alarmı', '{tk} fiyatı', 'şunun üstüne çıkınca', 'şunun altına düşünce', 'Telegram’da kur', '@{bot} botu sana Telegram’dan mesaj atar. Ücretsiz; /stop ile kapatabilirsin.'],
 'nl': ['🔔 Prijsalert', 'Laat het weten als {tk}', 'stijgt boven', 'daalt onder', 'Instellen in Telegram', 'De bot @{bot} stuurt je een bericht in Telegram. Gratis; uitzetten met /stop.'],
 'ru': ['🔔 Уведомление', 'Сообщить, когда цена {tk}', 'поднимется выше', 'опустится ниже', 'Включить в Telegram', 'Бот @{bot} пришлёт сообщение в Telegram. Бесплатно, отключить — /stop.'],
 'id': ['🔔 Notifikasi harga', 'Beri tahu saat {tk}', 'naik di atas', 'turun di bawah', 'Atur di Telegram', 'Bot @{bot} akan mengirim pesan di Telegram. Gratis; matikan dengan /stop.'],
 'vi': ['🔔 Cảnh báo giá', 'Báo tôi khi {tk}', 'tăng trên', 'giảm dưới', 'Bật trong Telegram', 'Bot @{bot} sẽ nhắn bạn trên Telegram. Miễn phí; tắt bằng /stop.'],
 'th': ['🔔 แจ้งเตือนราคา', 'แจ้งฉันเมื่อ {tk}', 'ขึ้นเหนือ', 'ลงต่ำกว่า', 'ตั้งค่าใน Telegram', 'บอท @{bot} จะส่งข้อความใน Telegram ฟรี ปิดได้ด้วย /stop'],
 'hi': ['🔔 कीमत अलर्ट', 'मुझे बताएँ जब {tk}', 'इससे ऊपर जाए', 'इससे नीचे आए', 'Telegram में सेट करें', '@{bot} बॉट आपको Telegram पर संदेश भेजेगा। मुफ़्त; /stop से बंद करें।'],
 'ja': ['🔔 価格アラート', '{tk}が次の価格を', '上回ったら', '下回ったら', 'Telegramで設定', '@{bot} ボットがTelegramでお知らせします。無料、/stop でいつでも停止。'],
 'ko': ['🔔 가격 알림', '{tk} 가격이', '이상으로 오르면', '이하로 내리면', '텔레그램에서 설정', '@{bot} 봇이 텔레그램으로 알려 드립니다. 무료이며 /stop 으로 끌 수 있습니다.'],
 'zh': ['🔔 价格提醒', '当 {tk} 价格', '涨破', '跌破', '在 Telegram 中设置', '@{bot} 机器人会在 Telegram 上通知你。免费，发送 /stop 即可关闭。'],
 'ar': ['🔔 تنبيه السعر', 'أبلغني عندما {tk}', 'يرتفع فوق', 'ينخفض تحت', 'فعّله في تيليجرام', 'سيرسل لك البوت @{bot} رسالة في تيليجرام. مجانًا؛ أوقفه بـ /stop.'],
 'fil': ['🔔 Price alert', 'Sabihan ako kapag ang {tk} ay', 'tumaas lampas', 'bumaba sa ilalim ng', 'I-set sa Telegram', 'Magme-message sa iyo ang bot na @{bot} sa Telegram. Libre; i-off gamit ang /stop.'],
}
AL = {lg: dict(zip(_K, v)) for lg, v in _V.items()}
for _lg, _v in _V.items():
    assert len(_v) == len(_K), _lg
