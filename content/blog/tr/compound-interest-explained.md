---
title: Bileşik faiz nedir? Gerçek örneklerle anlatım
description: Bileşik faiz nedir, basitçe: kolay formül, neden zamanın tutardan daha önemli olduğu ve gerçek geçmiş verilerle banka mevduatı ile endeks fonu karşılaştırması.
date: 2026-11-16
category: guides
assets: spy, qqq, gold
---
**Bileşik faiz**, paranızın getiri kazanması ve ardından o getirinin de getiri kazanmaya başlamasıdır. Yani "faizin faizi" — ve uzun vadede yatırımdaki ağır yükün büyük kısmını o taşır.

Bu rehber konuyu ağır matematik olmadan açıklıyor, gerçek örnekler gösteriyor ve erken başlamanın neden genellikle büyük tutarla başlamaktan daha önemli olduğunu anlatıyor.

## Tek örnekte fikir

Diyelim ki 10.000 ₺'yi yılda %10 büyüyen bir yere koydunuz.

- 1. yılın sonunda: 10.000 ₺ + 1.000 ₺ = **11.000 ₺**.
- 2. yılın sonunda: 11.000 ₺ + 1.100 ₺ = **12.100 ₺** (fazladan 100 ₺, geçen yılın faizinin faizidir).
- 3. yılın sonunda: 12.100 ₺ + 1.210 ₺ = **13.310 ₺**.

Her yıl kazanç biraz daha büyük olur, çünkü daha büyük bir tutar üzerinden hesaplanır. **Basit** faizde her yıl, sonsuza kadar 1.000 ₺ alırdınız. **Bileşik** faizde yıllık kazanç büyümeye devam eder.

Bu sayılar yalnızca bir örnektir — gerçek yatırımlar her yıl sabit bir yüzdeyle büyümez.

## Basit dille formül

Klasik formül şudur:

> Son tutar = Başlangıç tutarı × (1 + yıllık oran) ^ yıl sayısı

Sözle: paranızı alın, "bir artı oran" ile çarpın ve bunu her yıl için bir kez tekrarlayın.

Hızlı bir zihinsel kestirme **72 kuralıdır**: paranızın kaç yılda ikiye katlanacağını tahmin etmek için 72'yi yıllık orana bölün.

- Yılda %4 → ikiye katlanması yaklaşık 18 yıl.
- Yılda %6 → yaklaşık 12 yıl.
- Yılda %8 → yaklaşık 9 yıl.

Bunu elle hesaplamanıza gerek yok — [bileşik faiz hesaplayıcımız]({lang}/compound-interest/) her tutar, oran, süre ve aylık katkı için hesaplar.

## En önemlisi zaman

Bileşik getiri başta yavaş, sonra hızlıdır. Büyümenin çoğu son yıllarda gelir. Bu yüzden **piyasada geçirilen zaman** genellikle biraz daha büyük bir tutarı yener.

Her ikisi de örnek olarak yılda %7 kazanan iki kişiyi karşılaştıralım:

- **Ayşe** 25 ile 35 yaş arasında (10 yıl) ayda 5.000 ₺ yatırır, sonra durur ve parayı 65 yaşına kadar büyümeye bırakır.
- **Burak** 35 yaşında başlar ve 30 yıl boyunca, 65 yaşına kadar ayda 5.000 ₺ yatırır.

Burak üç kat daha fazla para yatırır (1.800.000 ₺'ye karşı 600.000 ₺). Yine de 65 yaşında Ayşe yaklaşık aynı tutara — bu örnekte biraz daha fazlasına — ulaşır, çünkü parası 10 yıl daha fazla bileşik büyüme fırsatı buldu. Kendi rakamlarınızı, aylık bir tutarın bir hedefe ulaşmasının ne kadar sürebileceğini gösteren [milyoner hesaplayıcısında]({lang}/millionaire/) deneyin.

Ders "artık çok geç" değil. Ders şu: başlamak için en iyi zaman genellikle olabildiğince erken ve sürdürebileceğiniz tutarla başlamaktır.

## Aylık katkılar: bileşik getiri artı disiplin

Gerçek hayatta çoğu insan tek seferde büyük bir tutar yatırmaz. Her ay para ekler. Bu, iki gücü birleştirir:

1. **Katkılarınız** — sizin kontrol ettiğiniz kısım.
2. **Bileşik getiri** — zaten yatırılmış her şeyin getirisi.

Başta işin neredeyse tamamını katkılar yapar. 10–20 yıl sonra, biriktirdiğiniz tutarın getirisi her yıl eklediğinizden daha büyük hale gelebilir. Aynı fikir DCA'nın (maliyet ortalaması) da temelidir — [DCA hesaplayıcımızla]({lang}/compare/) nasıl çalıştığını görün.

## Banka mevduatı ile endeks fonları

İkisi de bileşik getiri sağlayabilir, ama çok farklı davranırlar.

### Birikim hesapları ve vadeli mevduat

- **Artıları:** öngörülebilir faiz, düşük risk, çoğu zaman belirli bir limite kadar mevduat güvencesi (Türkiye'de TMSF).
- **Eksileri:** faizler genellikle mütevazıdır ve merkez bankası politikasıyla değişir. **Enflasyon** düşüldükten sonra gerçek büyüme sıfıra yakın, hatta negatif olabilir.

### Endeks fonları (örneğin bir S&P 500 fonu)

- **Artıları:** yüzlerce şirketin bir dilimine sahip olursunuz; bu şirketlerin kârları ve temettüleri tarihsel olarak uzun dönemlerde büyüdü.
- **Eksileri:** sabit bir oran yok. Bazı yıllarda fiyatlar düşer — bazen üçte bir veya daha fazla — ve geçmiş sonuçlar geleceği garanti etmez.

### Gerçek bir örnek

Gerçek geçmiş fiyatlara göre, S&P 500'e (SPY) günde 10 dolar yatırmanın 10 yıl sonraki değeri:

- Bugünkü değer: **{{dca:spy:10}}**
- Yatırılan tutar: {{dcainv:10}}
- Getiri: {{dcaroi:spy:10}}

Ve 10 yıl önce tek seferde yatırılan 1.000 dolar bugün yaklaşık {{lump:spy:10}} değerinde olurdu ({{lumproi:spy:10}}). Bu rakamlar her piyasa kapanışında güncellenir; ücretler, vergiler ve temettüler hesaba katılmaz.

{{table:spy,qqq,gold:10}}

## Enflasyon: tersine işleyen bileşik etki

Enflasyon da bileşik işler — ama sizin aleyhinize. Fiyatlar yılda %3 artarsa, nakit tutulan para yaklaşık 10 yılda alım gücünün kabaca dörtte birini kaybeder. Bunun ülkenizde nasıl gerçekleştiğini [enflasyon hesaplayıcımızla]({lang}/inflation/) görün.

Bu yüzden seçenekleri karşılaştırırken **reel** getiriye bakın: enflasyondan sonraki büyüme.

## Bileşik getiriyi sessizce bozan şeyler

- **Yüksek ücretler.** Yıllık %1–2'lik bir ücret de bileşik işler ve uzun vadeli büyümenin büyük bir kısmını alabilir.
- **Erken çekim.** Kârları çekmek kartopunu sıfırlar.
- **Panik satışı.** Bir çöküşten sonra satmak kayıpları kesinleştirir ve gelirse toparlanmayı kaçırır.
- **"Garantili" yüksek getirinin peşinden koşmak.** Çok yüksek sabit getiriler dolandırıcılığın yaygın bir işaretidir.

## Bileşik getiriyi pratikte nasıl kullanmalı?

1. Kötü yıllarda bile her ay ödemeye devam edebileceğiniz bir tutarla başlayın.
2. Karar vermeden gerçekleşmesi için otomatik hale getirin.
3. Maliyetleri düşük tutun.
4. Temettüleri ve faizi harcamak yerine yeniden yatırın.
5. Zaman verin — aylarla değil, on yıllarla düşünün.

{{card:spy}}

## Sık sorulan sorular

### Basit faiz ile bileşik faiz arasındaki fark nedir?

Basit faiz yalnızca ana para üzerinden ödenir. Bileşik faiz ise ana para artı daha önce kazanılan tüm faiz üzerinden ödenir, bu yüzden büyüme zamanla hızlanır.

### Hisse senetleri bileşik faiz öder mi?

Doğrudan faiz ödemezler, ama bileşik etki yine çalışır: şirket büyümesi ve yeniden yatırılan temettüler geçmiş kazançların üzerine inşa edilir. Mevduatın aksine getiriler sabit değildir ve negatif olabilir.

### Faiz ne sıklıkla bileşik olmalı?

Daha sık bileşiklenme (yıllık yerine aylık) biraz yardımcı olur, ama oran ve yıl sayısı çok daha önemlidir.

### 40 veya 50 yaşında başlamak için çok mu geç?

Şart değil. Bileşik büyüme için daha az yılınız var, bu yüzden düzenli katkılar ve düşük maliyetler daha önemli hale gelir. Bir hesaplayıcı gerçekçi beklentiler belirlemenize yardım eder.

## Kaynaklar

- [Investor.gov (ABD SEC) — Bileşik faiz hesaplayıcısı ve açıklaması](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator)
- S&P 500 (SPY) fiyatları: WhatIfStack piyasa verileri, aylık kapanışlar

*Yatırım tavsiyesi değildir. Sabit oranlı örnekler yalnızca açıklama amaçlıdır; gerçek yatırımlar değer kaybedebilir.*
