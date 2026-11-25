---
title: Borsadan kendi cüzdanınıza kripto nasıl çekilir: adım adım
description: Coinlerinizi borsadan kendi cüzdanınıza güvenle taşıyın: doğru adresi kopyalayın, aynı ağı seçin, gerekirse memo ekleyin ve önce küçük bir test gönderin.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 ağ
stat_label: borsa ve cüzdan aynı ağı kullanmalı, yoksa coinler kaybolabilir
---
**Kriptoyu kendi cüzdanınıza nasıl çekersiniz?** Cüzdanınızda o coin için **alma adresinizi** (receive address) kopyalarsınız. Sonra borsada **Withdraw** (Çekme) ekranını açar, adresi yapıştırır, cüzdanınızın kullandığı **aynı ağı** seçer, küçük bir test tutarı girer ve 2FA ile onaylarsınız. Test ulaşınca kalanını gönderirsiniz.

> **Öne çıkanlar**
> - Üç şey eşleşmeli: **coin**, **adres** ve **ağ** (coinlerin üzerinden gittiği blokzincir; örneğin Ethereum, BNB Smart Chain, TRON ya da Solana). Binance, yanlış ağdan gönderilen coinlerin tamamen kaybolabileceği konusunda uyarıyor.
> - Bazı coinler (XRP, XLM ya da ATOM gibi) ayrıca **memo** veya **tag** ister (alıcının coinlerin kime ait olduğunu anladığı kısa bir sayı). Bu olmadan transfer takılabilir ya da yanlış kişiye gidebilir.
> - **Her zaman önce küçük bir test gönderin.** Coinler borsadan çıktıktan sonra çekme işlemi iptal edilemez.

Bu ders, [Düzenli alım nasıl kurulur]({lang}/blog/how-to-set-up-a-recurring-buy/) dersinin devamıdır. Neden kendi cüzdanınızı isteyebileceğiniz [sıcak ve soğuk cüzdanlar]({lang}/blog/crypto-wallets-hot-vs-cold/) dersinde anlatılıyor.

## Başlamadan önce

İki şeye ihtiyacınız var. Birincisi, içinde coin olan ve 2FA ile korunan bir borsa hesabı ([Kripto borsasına nasıl kayıt olunur]({lang}/blog/how-to-register-on-a-crypto-exchange/) dersine bakın). İkincisi, önceden kurulmuş kendi cüzdan uygulamanız ve onun **kurtarma ifadesi** (seed phrase: cüzdanı geri yükleyen 12 ya da 24 gizli kelime) — kâğıda yazılmış ve çevrimdışı saklanıyor olmalı. Kurtarma ifadesini başka hiçbir yere yazmayın; hiçbir borsa, site ya da "destek" çalışanı ona asla ihtiyaç duymaz.

## Adım 1 — Cüzdanınızın alma adresini kopyalayın

1. Cüzdan uygulamanızı açın ve **Receive** (Al; bazen **Deposit**) seçeneğine dokunun.
2. Coini seçin, örneğin Bitcoin ya da USDT.
3. Cüzdan sorarsa ağı seçin. Hangisi olduğunu not edin — örneğin "TRON ağında USDT (TRC20)" ya da "Ethereum ağında USDT (ERC20)".
4. Adresin yanındaki **Copy** (Kopyala) seçeneğine dokunun. Adresi elle yazmayın.

Adres, harf ve rakamlardan oluşan uzun bir satırdır. Bitcoin adresleri çoğu zaman **bc1** ile, Ethereum ve BNB Smart Chain adresleri **0x** ile, TRON adresleri **T** ile başlar.

## Adım 2 — Borsada Withdraw ekranını açın

Binance uygulamasında bu **Assets → Spot → Send → Withdraw Crypto**, web sitesinde ise **Wallet → Overview → Withdraw** yoludur. Diğer borsalarda cüzdan ya da portföy ekranında her coinin yanında bir **Withdraw** (Çek) düğmesi bulunur. Adım 1'de seçtiğiniz coinin aynısını seçin.

## Adım 3 — Adresi yapıştırın ve ağı seçin

1. Adresi **Address** (Adres) alanına yapıştırın.
2. **İlk 4 ve son 4 karakteri** cüzdanınızla karşılaştırın. Bazı zararlı yazılımlar kopyalanan adresi hırsızın adresiyle değiştirir.
3. **Ağı** seçin. Cüzdanınızın Adım 1'de gösterdiği ağ olmalı. Binance ağı otomatik önerebilir — yine de kontrol edin. Bir ağı yalnızca ücreti en düşük olduğu için seçmeyin.
4. **Memo** ya da **Tag** alanı çıkarsa ve cüzdanınız size bir tane verdiyse doldurun. Kendi cüzdanınız memo göstermiyorsa genelde gerekmez — ama cüzdanın yardım sayfalarından bir kez daha kontrol edin.

İpucu: emin değilseniz adresi borsanın **Address Management** (adres defteri) bölümüne kaydedin. Binance'te ayrıca **whitelist** (beyaz liste) vardır: açtığınızda çekimler yalnızca kayıtlı adreslere gidebilir. Biri şifrenizi çalarsa bu işe yarar.

## Adım 4 — Küçük bir test gönderin

1. Küçük bir tutar girin — ekranda gösterilen en düşük çekim tutarının biraz üstünde.
2. **Ağ ücreti** ve **alacağınız tutar** satırlarına bakın. Ücret her çekim için sabittir, bu yüzden çok küçük bir tutarda büyük bir pay tutabilir.
3. **Withdraw** düğmesine basın ve 2FA kodunuz ya da geçiş anahtarınızla (passkey) onaylayın. Bazı borsalar ayrıca onay e-postası gönderir — açın ve **Confirm** (Onayla) düğmesine basın.

## Adım 5 — Ulaştığını kontrol edin, sonra kalanını gönderin

1. Bekleyin. Transfer, ağa ve yoğunluğa göre birkaç saniyeden yaklaşık bir saate kadar sürebilir.
2. Borsada çekim geçmişini açın: durumu ve **TxID**'yi (işlemin kimliği; bir blok gezgini sitesinde aratabilirsiniz) görürsünüz.
3. Coinler cüzdanınızda görününce 2–4. adımları kalanı için tekrarlayın. Adres zaten geçmişte ya da adres defterinde olduğu için ikinci sefer daha hızlıdır.

Coinleri nerede saklarsanız saklayın değerlerini tek yerden izlemek için [portföyünüze]({lang}/me/) ekleyin.

> **⚠️ Dikkat**
> - **Yanlış ağ.** USDT birçok ağda bulunur. "TRC20" USDT'yi yalnızca "ERC20" bekleyen bir adrese göndermek coinlerin kaybolması demek olabilir. Ağı iki kez kontrol edin.
> - **Eksik memo ya da tag.** Memo isteyen borsa ve cüzdanlar, memo olmadan gelen coinlerin kime ait olduğunu anlayamaz. Geri almak mümkünse bile yavaştır ve ücretlidir.
> - **Sahte destek ve "adres doğrulama" siteleri.** Dürüst hiç kimse kurtarma ifadenizi istemez ya da coin göndererek cüzdanınızı "doğrulamanızı" istemez. Yalnızca resmi uygulama veya web sitesi içinden çekim yapın.

## Düzenli alım yapıyorsanız bu ne anlama gelir

Her hafta ya da her ay biraz alıyorsanız, her alımdan sonra çekim yapmanız gerekmez — her çekimin bir ücreti var. Birçok kişi coinlerin borsada birikmesine izin verir ve arada bir, örneğin üç ayda bir, tek ve daha büyük bir transferle kendi cüzdanına taşır. Hesaplayıcımızdan bir örnek: 3 yıl boyunca her gün 10 $'lık Bitcoin (toplam {{dcainv:3}}) {{dca:btc:3}} ({{dcaroi:btc:3}}) oldu. Bunlar geçmiş sonuçlardır, tahmin değildir. Bitcoin şu anda {{price:btc}}; [Bitcoin sayfasına]({lang}/btc/) göz atın.

Önceki ders: [Düzenli alım nasıl kurulur]({lang}/blog/how-to-set-up-a-recurring-buy/). Sonraki ders: kripto nasıl satılır ve para banka hesabınıza nasıl aktarılır. Borsaları [borsalar sayfamızda]({lang}/exchanges/) karşılaştırın; tüm dersler [Öğren sayfasında]({lang}/learn/).

## Kaynaklar

- [Binance Destek: Binance'te kripto para yatırma/çekme (Mart 2026'da güncellendi)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Destek: Yanlış ya da eksik tag/memo ile yapılan kripto yatırma işlemi nasıl geri alınır](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Yardım Merkezi: Binance.US hesabınızdan kripto nasıl çekilir (Haziran 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Yatırım tavsiyesi değildir.*
