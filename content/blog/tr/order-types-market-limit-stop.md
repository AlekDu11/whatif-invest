---
title: "Emir türleri: piyasa, limit ve stop emirleri adım adım"
description: Borsa veya aracı kurum uygulamasında Market, Limit ve Stop butonları ne yapar: rakamlı bir örnek ve yeni başlayanlara para kaybettiren 3 hata.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: temel emir türü — piyasa (hızlı, fiyat sabit değil), limit (fiyat sabit, gerçekleşme kesin değil), stop (belirli fiyatta tetiklenir)
---
**Hangi emir türleri var?** **Piyasa emri** (Market) hemen şimdi, mevcut en iyi fiyattan alır ya da satar. **Limit emri** (Limit) yalnızca sizin fiyatınızdan veya daha iyisinden alır ya da satar; bu yüzden hiç gerçekleşmeyebilir. **Stop emri** (Stop) fiyatın seçtiğiniz seviyeye gelmesini bekler, sonra bir piyasa emri gönderir — genellikle zararı sınırlamak için kullanılır.

> **Önemli noktalar**
> - Market = hız, ama tam fiyatı siz kontrol etmezsiniz. Limit = fiyat kontrolü, ama gerçekleşme garantisi yok.
> - Stop emri tetiklendiğinde piyasa emrine dönüşür. Hızlı bir düşüşte stop fiyatınızın çok altında gerçekleşebilir.
> - «Al» butonuna basmadan önce her zaman üç şeyi kontrol edin: emir türü, miktar ve fiyat.

## Üç buton, sade bir dille

Bir kripto borsasının ya da aracı kurumun uygulamasında işlem ekranını açtığınızda genellikle şu sekmeleri görürsünüz: **Market** (piyasa), **Limit** ve **Stop** (bazen «Stop-limit», stop limit).

- **Piyasa emri (Market).** «Şimdi al, fiyatı ne olursa olsun.» Neredeyse anında en iyi tekliften gerçekleşir (**ask**, yani birinin satmak istediği en düşük fiyat). Büyük coinlerde ve büyük hisselerde fiyat genellikle ekranda gördüğünüze çok yakındır. Küçük, sığ piyasalarda çok daha kötü olabilir.
- **Limit emri (Limit).** «Yalnızca X $ veya daha ucuza al» (ya da «yalnızca X $ veya daha pahalıya sat»). Emriniz, biri fiyatınızı kabul edene kadar **emir defterinde** (order book, bekleyen tüm alış ve satış emirlerinin listesi) bekler. Fiyat oraya hiç gelmezse hiçbir şey olmaz.
- **Stop emri (Stop, stop-loss / zarar durdur).** «Fiyat X $'a düşerse sat.» O zamana kadar görünmezdir ve hiçbir şey yapmaz. Fiyat X $'a değdiğinde piyasa emrine dönüşür ve bir sonraki mevcut fiyattan satar.
- **Stop-limit emri (Stop-limit).** Stop gibidir ama *limit* emrine dönüşür. Limitinizin altında satmazsınız — ama hızlı bir düşüşte hiç satamayabilirsiniz.

## Basit rakamlarla bir örnek

Bir hissenin **100,00 $** gösterdiğini düşünün. En iyi alıcı 99,95 $ teklif ediyor (**bid**), en iyi satıcı 100,05 $ istiyor (ask). Aradaki 0,10 $'lık fark **spread**'dir (alış-satış farkı).

1. **Market, 10 hisse al** butonuna basarsınız → tanesi yaklaşık 100,05 $'dan öder, toplam **1.000,50 $** artı varsa komisyon ödersiniz.
2. **Limit, 10 hisse 98 $'dan al** emri verirsiniz → bir satıcı 98 $'ı kabul edene kadar hiçbir şey olmaz. Fiyat bunun yerine 105 $'a çıkarsa emriniz sadece bekler ve hiçbir şey almazsınız.
3. Hisseler sizde ve **90 $'a Stop** koyarsınız → fiyat 90 $'a düşerse bir piyasa satış emri gönderilir. Sakin bir piyasada belki 89,95 $ alırsınız. Ama piyasa açılmadan kötü bir haber gelir ve hisse 80 $'dan açılırsa stop'unuz tetiklenir ve 90 $'dan değil, **80 $** civarından satarsınız.

Bu üçüncü durum gerçektir. 6 Mayıs 2010'da («flash crash», ani çöküş) ABD'de fiyatlar dakikalar içinde çöktü ve bazı stop emirleri stop seviyelerinin çok altında gerçekleşti; SEC ve CFTC raporuna göre birkaç hisse bir sente bile işlem gördü.

## Adım adım: ilk limit emrinizi güvenle verin

Önce çok küçük bir tutarla deneyin.

1. **Adım 1 — Coinin ya da hissenin işlem ekranını açın** ve **Al** (Buy) seçin.
2. **Adım 2 — «Market» değil, «Limit» sekmesine basın.**
3. **Adım 3 — Fiyatınızı yazın.** Önce güncel fiyata bakın (örneğin bitcoin şu anda {{price:btc}}). Bunun çok altındaki bir limit hiç gerçekleşmeyebilir.
4. **Adım 4 — Miktarı yazın.** Kutunun coin/hisse mi yoksa para mı (USD, EUR) olduğunu kontrol edin. En sık yapılan yazım hatası budur.
5. **Adım 5 — Özeti kontrol edin**: tür, fiyat, miktar, toplam, komisyon. Sonra onaylayın.
6. **Adım 6 — Emrinizi «Açık emirler»de (Open orders) bulun.** Gerçekleşene kadar orada istediğiniz zaman iptal edebilirsiniz. Gerçekleşince «Emir geçmişi»ne (Order history) geçer.

> **⚠️ Dikkat**
> - **Sığ piyasalarda piyasa emri.** Küçük coinlerde ya da normal işlem saatleri dışında piyasa emri ekrandaki fiyattan çok daha kötü gerçekleşebilir (buna **kayma**, slippage denir). Orada limit emri kullanın.
> - **Stop-loss'un fiyatınızı garanti ettiğini sanmak.** Etmez: satışı garanti eder, fiyatı değil. Fiyat boşlukları (gap) ve çöküşler gerçekleşmeyi çok daha aşağı itebilir. Stop-limit fiyatı korur ama satmayabilir.
> - **Alanları karıştırmak.** Yanlış taraf (Al yerine Sat), miktarda fazladan bir sıfır ya da yanlış kutuya yazılmış fiyat. Onaylamadan önce özeti okuyun.

## Düzenli alım yapıyorsanız bu ne anlama gelir

Her hafta ya da her ay biraz alıyorsanız karmaşık emirlere ihtiyacınız yok. Büyük ve likit bir varlıkta piyasa emri genellikle yeterlidir; bir üst sınır istiyorsanız güncel fiyatın biraz üstünde bir limit emri de olur. Asıl sonuç piyasada geçen zamandan gelir: 3 yıl boyunca bitcoine günde 10 $ yatırılsaydı bugün {{dca:btc:3}} değerinde olurdu (yatırılan toplam {{dcainv:3}}) — bunlar geçmiş sonuçlar, tahmin değil.

WhatIfStack'te sırada: emir defterlerinin ve büyük trader'ların piyasayı nasıl hareket ettirdiğini [Trading merkezinde]({lang}/trading/) ve [Hyperliquid balina takipçisinde]({lang}/trading/hyperliquid/) görün, [borsalarda]({lang}/exchanges/) komisyonları karşılaştırın ve tüm dersleri [Öğren sayfasında]({lang}/learn/) bulun.

## Kaynaklar

- [Investor.gov (SEC): Emir türleri](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Yatırımcı bülteni — stop, stop-limit ve iz süren stop emirleri](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Emir türleri](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC ve SEC: 6 Mayıs 2010 piyasa olaylarına ilişkin rapor](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Yatırım tavsiyesi değildir.*
