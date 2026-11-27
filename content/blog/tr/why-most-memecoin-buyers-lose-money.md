---
title: "Memecoin alanların çoğu neden para kaybediyor: lansman, slippage ve komisyon hesabı"
description: pump.fun cüzdanlarının yalnızca %0,41'i 10.000 $'ın üzerinde kâr realize etti. Memecoin alıcılarının aleyhine işleyen lansman, slippage ve komisyon hesabı.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: %0,41
stat_label: 13,55 milyon pump.fun cüzdanının 10.000 $'ın üzerinde kâr realize etme oranı (Dune verisi, Ocak 2025)
---
**Memecoin alan insanların çoğu neden para kaybediyor?** Çünkü daha fiyat kıpırdamadan hesap onların aleyhine işliyor: yeni token'ların çoğu bir gün içinde ölüyor, her alım ve satış komisyon ve slippage'a mal oluyor, en erken alıcılar (çoğu zaman botlar ve içeridekiler) ise sonradan gelenlere satıyor. Kazanmak için bir token'ın hem hayatta kalması *hem de* tüm bu maliyetleri karşılayacak kadar yükselmesi gerekiyor.

> **Öne çıkanlar**
> - Ocak 2025'te paylaşılan Dune verilerine göre 13,55 milyon pump.fun cüzdanının yalnızca yaklaşık **%0,41**'i **10.000 $**'ın üzerinde kâr realize etmişti.
> - CoinGecko, pump.fun token'larının **%68,67**'sinin son işlemini lansman gününde yaptığını tespit etti (Ocak 2024 – Haziran 2026 verisi).
> - Yeni bir token'da her tam tur (alım + satım), ağ ücretleri ve slippage hariç, yalnızca platform komisyonu olarak **%2,5 veya daha fazlaya** mal olabilir.

## Bölüm 1 — Hayatta kalma hesabı

Memecoin'lerin çoğu "ucuz" değil — sadece ömürleri çok kısa.

- **Lansman gününde ölüm.** CoinGecko 18,67 milyon pump.fun token'ı saydı; bunların %68,67'si son işlemini piyasaya çıktığı gün yaptı (25 Haziran 2026'da açıklanan veri).
- **Gerçek bir piyasaya ulaşan çok az.** "Graduation" (mezuniyet), bir token'ın pump.fun'ın başlangıç eğrisinden çıkıp normal bir işlem havuzuna geçmesi demek. Dune verilerine göre haftalık mezuniyet oranı 17 Şubat 2025'ten itibaren dört hafta boyunca **%1**'in altında kaldı; en iyi haftası Kasım 2024'te **%1,67** idi. Mart 2026'da **%2,01**'e ulaşarak Temmuz 2025'ten bu yana en yüksek seviyeyi gördü.

Yani yeni lansmanları rastgele seçerseniz elinizde çoğunlukla işlem görmeyi bırakan coin'ler kalır. Birkaç büyük kazanan, sıfıra giden çok sayıda coin'in zararını ancak çok iyi seçim yaparsanız karşılar — ve ilk gün hangilerinin hayatta kalacağını kimse bilmez.

## Bölüm 2 — Komisyonlar: girerken de çıkarken de ödersiniz

pump.fun'ın yardım sayfası (Eylül 2025), mezuniyetten önce her işlemde **%1,25** komisyon olduğunu belirtiyor (%0,95 platforma, %0,30 token'ı oluşturana). Mezuniyetten sonra komisyon token büyüdükçe düşüyor: en küçükler için %1,25'ten en büyükler için %0,30'a kadar. Bunun üstüne Solana ağ ücretleri ve isteğe bağlı "öncelik" (priority) ve MEV koruma ücretleri geliyor (sayfalarına göre işlem başına 0,003–0,03 SOL).

**Hesaplı örnek (temsilîdir, gerçek fiyatlar değil):** yeni bir token'dan 50 $'lık alırsınız ve hem alırken hem satarken 0,02 SOL öncelik ücreti ödersiniz. Giriş ve çıkıştaki %1,25'ler yaklaşık 1,25 $ eder, iki öncelik ücreti ise birkaç dolar daha ekleyebilir. Sırf 50 $'a geri dönmek için token'ın belki **%5–10** yükselmesi gerekir. 10 $'lık işlemlerde durum çok daha kötü: sabit ücretler çok daha büyük bir pay yer.

## Bölüm 3 — Slippage: siz alırken fiyat kayar

**Slippage** (fiyat kayması), gördüğünüz fiyatla gerçekte aldığınız fiyat arasındaki farktır (bkz. [memecoin sözlüğü]({lang}/memes/glossary/)). Yeni token'ların havuzları çok küçüktür; bu yüzden kendi alımınız bile fiyatı yukarı iter — aynı saniyede başkalarının yaptığı alımlar da öyle. Slippage'ı %10–20'ye ayarlarsanız (birçok uygulama yeni coin'ler için bunu önerir), o kadar fazla ödemeyi kabul etmiş olursunuz. Satarken de aynı sorun tersinden yaşanır: sığ bir havuzda satışınız fiyatı aşağı çeker.

## Bölüm 4 — Karşı tarafta kim var

En erken alıcılar çoğu zaman sniper'lar, bundler'lar ve geliştirici cüzdanıdır (bkz. [sniper'lar, bundler'lar ve geliştirici cüzdanları]({lang}/blog/snipers-bundlers-dev-wallets/)). En düşük fiyattan alır, ilk talep dalgasında satarlar. İlk yeşil mumdan sonra alırsanız, çoğu zaman "exit liquidity" (çıkış likiditesi) siz olursunuz — yani onların sattığı para.

## Adım adım: «Buy»a basmadan önce hesabı yapın

1. **Adım 1 — Komisyonları sayın.** Swap ekranındaki ücret satırına bakın ve ağ/öncelik ücretini ekleyin. İkiyle çarpın (alım + satım).
2. **Adım 2 — Slippage'ı kontrol edin.** İşlemin izin verdiği kadar düşük tutun (örneğin büyük havuzlu bir coin'de %1–3). Bir coin %20 slippage gerektiriyorsa bu bir uyarı işaretidir.
3. **Adım 3 — Havuzun büyüklüğüne bakın.** [Memes sayfamızda]({lang}/memes/) token'ı açın ve likiditeye bakın. Küçük havuz = iki yönde de büyük slippage.
4. **Adım 4 — Güvenlik kontrolünü yapın.** [Bir memecoin'i almadan önce nasıl kontrol edilir]({lang}/blog/how-to-check-a-memecoin-before-buying/) rehberini kullanın.
5. **Adım 5 — Zararınızı önceden belirleyin.** Yalnızca tamamen kaybedebileceğiniz parayı kullanın ve tutarı başlamadan önce belirleyin.

> **⚠️ Dikkat**
> - **"Sadece 0,0001 $, 1000 kat yapabilir."** Düşük fiyat hiçbir şey ifade etmez; birçok token milyarlarca adet halinde vardır. Önemli olan token'ın hayatta kalıp kalmadığı ve size kimin sattığıdır.
> - **Çok sayıda minicik işlem.** Sabit ağ ve öncelik ücretleri, fiyat daha hiç kıpırdamadan 10 $'lık bir işlemin %10'unu veya fazlasını yiyebilir.
> - **Kazananların ekran görüntüleri.** Büyük kazanan %0,41'i görürsünüz, kaybeden milyonları değil; "guru"lar çoğu zaman tanıttıkları coin'leri satıyordur.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

Düzenli küçük alımlar, yıllar sonra hâlâ var olan varlıklarda işe yarar — bu gece işlem görmeyi bırakabilecek token'larda değil. Kripto istiyorsanız yeni başlayanlar için alışılmış yol, büyük ve likit bir coin'i azar azar almaktır; karşılaştırma için Solana'nın kendi coin'i SOL şu anda {{price:sol}} ({{chg1y:sol}} 12 ayda) — geçmiş sonuçlardır, tahmin değildir. Hesaplayıcımızda «günde 10 $»ı herhangi bir varlıkta deneyebilir ve [portföy sayfanızda]({lang}/me/) takip edebilirsiniz.

Önceki ders: [sniper'lar, bundler'lar ve geliştirici cüzdanları]({lang}/blog/snipers-bundlers-dev-wallets/). Tüm dersler [Öğren sayfasında]({lang}/learn/).

## Kaynaklar

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11 Ocak 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14 Mart 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, Dune verisi: pump.fun graduation rate hits 2.01% (17 Mart 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / CoinGecko verisi: nearly 70% of pump.fun tokens disappear on launch day (25 Haziran 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [pump.fun Yardım Merkezi: Transaction fees on pump.fun (Eylül 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Yatırım tavsiyesi değildir.*
