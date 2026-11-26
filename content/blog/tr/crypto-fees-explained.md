---
title: "Kripto ücretleri basitçe: işlem ücreti, spread ve ağ ücreti"
description: Her kripto alımında ya da çekiminde üç maliyet gizlidir — işlem ücreti, spread ve ağ ücreti. Her biri nasıl işler ve onaylamadan önce nasıl görülür?
date: 2026-11-26T13:40:00Z
category: learn
track: crypto
step: 8
assets: btc, eth, bnb
stat: 3 ücret
stat_label: işlem ücreti, spread ve ağ ücreti — Onayla'ya basmadan önce üçünü de kontrol edin
---
**Kripto alırken, satarken ya da gönderirken gerçekte ne ödüyorsunuz?** Genellikle üç şey. **İşlem ücreti**, borsanın aldığı komisyondur. **Spread**, alış fiyatı ile satış fiyatı arasındaki farktır. Coin'ler borsadan çıktığında bir de **ağ ücreti** ödenir; bu ücret blokzincire gider. Hepsini bir arada görmenin en kolay yolu, onay ekranındaki "alacağınız tutar" satırıdır.

> **Öne çıkanlar**
> - Binance'in örneğinde normal bir kullanıcı işlemin **%0,1**'i kadar işlem ücreti öder; $1.000'lık alımda $1. Bu ücreti BNB ile ödemek **%25'e varan indirim** sağlar (Binance destek sayfaları, Ocak–Şubat 2026'da güncellendi).
> - Basit "Satın Al" düğmeleri ve kartla ödeme çoğu zaman emir defterinden daha pahalıdır, çünkü fiyata spread ve bazen kart ücreti eklenmiştir.
> - Bitcoin ağ ücreti, işlemin veri olarak **boyutuna** ve ağın ne kadar yoğun olduğuna bağlıdır — **gönderdiğiniz para miktarına değil**.

## Ücret 1 — işlem ücreti

Borsanın işlemi yapmak için aldığı ücrettir. Tutarın yüzdesi olarak hesaplanır.

- Binance'in kendi örneğinde normal kullanıcı için oran %0,1'dir: 10 ETH almanın ücreti 0,01 ETH'dir. Ücret, **aldığınız** coin'den kesilir. ETH alırsanız ETH ile, USDC karşılığında satarsanız USDC ile ödersiniz.
- Birçok borsada iki oran vardır. **Maker** (piyasa yapıcı): emriniz biri onu alana kadar listede bekler, örneğin fiyatın altındaki bir limit emri. **Taker** (piyasa alıcı): emriniz anında mevcut fiyattan gerçekleşir. Maker oranı çoğu zaman aynı ya da daha düşüktür.
- Büyük yatırımcılar daha düşük oran öder (VIP seviyeleri). Yeni başlayanlar standart oranı öder.

**Adım 1 — Ücret sayfasını bulun.** Her büyük borsada **Fees** veya **Fee schedule** (Ücretler, Ücret tablosu) adlı bir sayfa vardır. Binance'te: profil → **Fees & Transactions Overview**. Seviyenize ait spot oranına bakın.

**Adım 2 — Zaten hak ettiğiniz indirimleri açın.** Binance'te Spot hesabınızda biraz BNB tutun ve **Using BNB Deduction** (ücretleri BNB ile ödeme) seçeneğini açın: Fee Level menüsünden ya da uygulamada Account Center → Settings → BNB Discount yolundan. Binance bunun spot ücretlerde %25'e varan indirim sağladığını söylüyor. Bunun için BNB almanız gerekmez; yalnızca elinizde zaten BNB varsa işe yarar.

## Ücret 2 — spread

**Spread**, aynı anda alabileceğiniz fiyat ile satabileceğiniz fiyat arasındaki farktır. Alıp hemen satarsanız, sıfır komisyonla bile spread kadar kaybedersiniz.

- Bitcoin gibi büyük bir coin'in ana işlem ekranında (emir defteri) spread genellikle çok küçüktür.
- **Basit Buy / Sell / Convert** (Al / Sat / Dönüştür) ekranlarında borsa, kendi kâr payını zaten içeren tek bir fiyat gösterir. Örneğin Coinbase, fiyatlandırma açıklamalarında basit alım ve satımların ücrete ek olarak spread içerdiğini belirtir.
- Küçük coin'lerde ve memecoin'lerde spread yüzde birkaç olabilir, çünkü bunlarla işlem yapan az kişi vardır.

**Adım 3 — İki fiyatı karşılaştırın.** Basit bir alımdan önce coin'in grafiğini aynı borsada (ya da bizim [Bitcoin sayfamızda]({lang}/btc/)) açın ve piyasa fiyatını onay ekranındaki fiyatla karşılaştırın. Aradaki fark, kabaca spread'inizdir.

**Adım 4 — Kart ücretine dikkat edin.** Banka kartıyla almak, başlamanın en hızlı ve çoğu zaman en pahalı yoludur: borsalar ve ödeme ortakları genellikle yüzde birkaçlık kart ücreti ekler. Banka havalesi ya da borsanın P2P'si genellikle daha ucuz ama daha yavaştır — bkz. [banka kartıyla Bitcoin nasıl alınır]({lang}/blog/how-to-buy-bitcoin-with-a-bank-card/).

## Ücret 3 — ağ ücreti

Coin'leri kendi cüzdanınıza ya da başka bir borsaya **çektiğinizde**, transfer blokzincire yazılır. Ağı işletenler (madenciler ya da doğrulayıcılar) bunun için ücret alır.

- Bitcoin'de ücret, sanal bayt başına satoshi (sat/vB) olarak fiyatlanır; bir satoshi, bir bitcoin'in yüz milyonda biridir. Basit bir ödeme yaklaşık 140 vB'dir, yani aynı türde bir işlemle 0,01 BTC göndermek de 9 BTC göndermek de aynı tutar.
- Çok kişi aynı anda gönderdiğinde ücretler yükselir; ağ sakin olduğunda düşer.
- Borsalar bunu karşılayan bir **çekim ücreti** (withdrawal fee) gösterir ve bu bazen gerçek ağ ücretinden yüksektir. Çoğu zaman yüzde değil, sabit bir coin miktarıdır; bu yüzden en çok küçük çekimlerde can yakar.
- Aynı coin için farklı ağların maliyeti çok farklıdır (USDT bir ağda birkaç sent, başka bir ağda birkaç dolar tutabilir). Alıcı adresin desteklediği ağı seçin — bkz. [kendi cüzdanınıza kripto nasıl çekilir]({lang}/blog/how-to-withdraw-crypto-to-your-own-wallet/).

**Adım 5 — Onaylamadan önce çekim ekranını okuyun.** Ekranda ağ, ücret ve "alınacak tutar" (amount received) görünür. Ücret tutara göre büyükse bekleyin ve çok sayıda küçük transfer yerine bir kez daha büyük bir tutar gönderin.

## Adım 6 — Not edin

Her alımı gerçek maliyetiyle [portföyünüze]({lang}/me/) ekleyin. Böylece sonucunuz yalnızca coin fiyatındaki değişimi değil, gerçekte ne ödediğinizi gösterir.

> **⚠️ Dikkat**
> - **"Sıfır komisyon" afişleri.** Bir işlem komisyonsuz olup yine de geniş bir spread içerebilir. Her zaman "alacağınız tutar" rakamına bakın.
> - **Çok sayıda küçük çekim.** $20'lık bir transferde birkaç dolarlık sabit çekim ücreti, paranızın büyük bir kısmıdır.
> - **Birkaç sent kazanmak için yanlış ağ.** Alıcı taraf o ağı desteklemiyorsa coin'ler kaybolabilir. Önce küçük bir tutarla deneyin.

## Düzenli alım yapıyorsanız bu ne anlama gelir

Her hafta küçük bir tutar alıyorsanız ücretler birikir. Her alımda %0,1 azdır, ama her alımda yüzde birkaçlık kart ücreti az değildir. Düzenli alım yapanlar genellikle hesaplarına banka havalesiyle para yatırır, ana piyasada otomatik tekrarlayan alım kurar ve coin'leri kendi cüzdanlarına ancak arada bir, tek ve daha büyük bir transferle çeker. Hesaplayıcımızdan bir örnek: 3 yıl boyunca her gün $10'lık Bitcoin alımı (toplam {{dcainv:3}}), ücretler hariç {{dca:btc:3}} oldu ({{dcaroi:btc:3}}). Bunlar geçmiş sonuçlardır, tahmin değildir. Bitcoin şu anda {{price:btc}}.

Önceki ders: [Kripto nasıl satılır ve para banka hesabınıza nasıl aktarılır]({lang}/blog/how-to-sell-crypto-and-withdraw-to-bank/). Borsaları [borsalar sayfamızda]({lang}/exchanges/) karşılaştırın; tüm dersler [Öğren sayfasında]({lang}/learn/).

## Kaynaklar

- [Binance Support: Binance spot işlem ücretleri nasıl hesaplanır (Ocak 2026'da güncellendi)](https://www.binance.com/en/support/faq/detail/e85d6e703b874674840122196b89780a)
- [Binance Support: Ücretleri BNB ile ödeyip %25 indirim nasıl alınır (Şubat 2026'da güncellendi)](https://www.binance.com/en/support/faq/115000583311)
- [Coinbase Help: Fiyatlandırma ve ücret açıklamaları](https://help.coinbase.com/en/coinbase/getting-started/getting-started-with-coinbase/pricing-and-fees)
- [Bitcoin.org: Bitcoin ücretleri](https://bitcoin.org/fees/)
- [Ledger Academy: Bitcoin ücretleri açıklandı (Nisan 2026)](https://www.ledger.com/academy/bitcoin-fees)

*Yatırım tavsiyesi değildir.*
