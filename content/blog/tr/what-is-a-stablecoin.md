---
title: Stablecoin nedir (USDT, USDC) ve neden önemlidir?
description: Stablecoin nedir, basitçe: USDT ve USDC 1 dolarda kalmayı nasıl başarır, arkalarında ne var, nerede kullanılır ve hangi risklere dikkat etmeli.
date: 2026-11-15
category: guides
assets: btc, eth
---
**Stablecoin nedir?** Stablecoin, fiyatı sabit kalacak şekilde tasarlanmış bir kripto tokendir — genellikle tam olarak **1 dolar**. Kripto gibi hareket eder (hızlı, 7/24, sınır tanımadan), ama değerini sıradan para gibi korumayı amaçlar.

En bilinen iki örnek **USDT** (Tether) ve **USDC** (Circle). İkisi birlikte stablecoin piyasasının büyük kısmını oluşturur ve birçok borsada Bitcoin ve diğer coinlerin alınıp satıldığı ana para birimidir.

## Stablecoinler neden var?

Bitcoin ve çoğu coin çok dalgalanır. Bitcoin şu an {{price:btc}} ve bir günde birkaç yüzde değişebilir. Şunları yapmak istediğinizde bu bir sorundur:

- işlemler arasında parayı bankaya geri çevirmeden bekletmek,
- bir ödeme gönderip vardığında aynı değerde olduğundan emin olmak,
- blokzincirde bir şeyi dolar cinsinden fiyatlamak.

Stablecoinler bu sorunu, tokeni insanların zaten güvendiği bir para birimine bağlayarak çözer — çoğu zaman ABD dolarına, bazen euroya veya altına.

## Stablecoinler 1 doları nasıl korur?

Üç ana tasarım vardır.

### 1. Nakit ve tahvil destekli (fiat destekli)

USDT ve USDC böyle çalışır. Bir şirket aldığı her dolar için bir token çıkarır ve rezerv tutar — çoğunlukla nakit, banka mevduatı ve kısa vadeli ABD devlet tahvilleri (hazine bonoları).

- İhraççıya 1 dolar verirsiniz → 1 token oluşturur.
- 1 tokeni geri verirsiniz → onu yok eder ve size 1 dolar öder (genellikle yalnızca doğrulanmış büyük müşteriler için).

Büyük yatırımcılar tokenleri her zaman dolara çevirebildiği için borsalardaki fiyat 1 dolara çok yakın kalır. Fiyat 0,99 dolara düşerse, yatırımcılar ucuz tokenleri alıp 1 dolardan bozdurur ve fiyatı tekrar yukarı iter.

İhraççılar rezerv raporları veya denetim firmalarından onay raporları (attestation) yayımlar. Bu raporların ne kadar ayrıntılı ve sık olduğu ihraççıya göre değişir — karşılaştırılması gereken ana konulardan biridir.

### 2. Başka kripto ile desteklenen

Burada bir akıllı sözleşme, çıkardığı stablecoinden daha fazla kripto tutar — örneğin her 100 dolarlık stablecoin için 150 dolarlık Ether kilitlenir. Teminatın fiyatı çok düşerse otomatik olarak satılır. En bilinen örnek DAI'dir (artık Sky ekosisteminin parçası). Dolar tutan bir şirket yoktur, ama sistem koda ve teminatın fiyatına bağlıdır.

### 3. Algoritmik

Bunlar, gerçek rezerv olmadan ya da çok az rezervle, kod ve ikinci bir "ortak" token kullanarak 1 doları korumaya çalışır. En bilinen örnek **TerraUSD (UST)** Mayıs 2022'de çöktü ve birkaç gün içinde on milyarlarca doları sildi. Bugün çoğu kişi tamamen algoritmik tasarımları çok yüksek riskli görüyor.

## İnsanlar stablecoinleri ne için kullanıyor?

- **Alım satım.** Birçok borsada coinler USDT veya USDC karşısında fiyatlanır. Yatırımcılar borsadan çıkmadan piyasadan "çekilmek" için stablecoine geçer.
- **Yurt dışına para göndermek.** Transfer, haftanın her günü, birkaç dakikada ve çoğu zaman düşük ağ ücretiyle ulaşabilir.
- **Dolar cinsinden birikim.** Yüksek enflasyonlu veya değer kaybeden para birimine sahip ülkelerde bazı kişiler stablecoini dijital bir dolar hesabı gibi tutar.
- **Ödemeler ve iş.** Serbest çalışanlar ve şirketler sınır ötesi ödeme yapmak ve almak için kullanır.
- **Merkeziyetsiz finans (DeFi).** Stablecoinler zincir üstü uygulamalarda borç verilir, borç alınır ve teminat olarak kullanılır.

DCA planı izleyen düzenli bir yatırımcı için stablecoin bir bekleme odası olabilir: borsaya yatırılmış ama henüz yatırıma dönüşmemiş para. Kendi kendine büyüyen bir yatırım değildir — hedef her zaman 1 dolardır.

## Anlamanız gereken riskler

Bir stablecoin, arkasında duran şey kadar iyidir. Temel riskler:

- **Sabitten kopma (de-peg).** İnsanlar rezervlerden şüphelenirse fiyat 1 doların altına inebilir. Mart 2023'te USDC, rezervlerinin bir kısmı batan Silicon Valley Bank'ta kaldığı için kısa süreliğine yaklaşık 0,88 dolara düştü; bankanın mevduatları güvence altına alınınca toparlandı.
- **İhraççı riski.** Fiat destekli coinlerde bir şirkete güvenirsiniz: rezervlerine, banka ortaklarına ve dürüstlüğüne.
- **Dondurma.** İhraççılar belirli adreslerdeki tokenleri dondurabilir, örneğin kolluk kuvvetlerinin talebiyle.
- **Düzenleme.** Kurallar sıkılaşıyor. AB'de MiCA tüzüğü stablecoin ihraççılarına şartlar getiriyor ve bazı coinler AB kullanıcıları için listeden çıkarıldı. ABD 2025'te federal stablecoin kurallarını (GENIUS Act) kabul etti. Türkiye'de de kripto varlık hizmet sağlayıcıları SPK denetimine tabi. Kurallar ülkeye göre farklıdır ve değişmeye devam ediyor.
- **Akıllı sözleşme ve platform riski.** Yazılım hataları, saldırılar veya bir borsanın çöküşü, stablecoinin kendisi sağlam olsa bile fonlarınızı etkileyebilir.
- **Mevduat sigortası yok.** Çoğu ülkede stablecoinler banka mevduat güvencesi kapsamında değildir.
- **"Faiz" teklifleri.** Stablecoine yüksek faiz ödeyen platformlar paranızla bir yerde risk alır. Yüksek getiri vaadi bir uyarı işaretidir.

## Basitçe USDT ve USDC

Herhangi birini önermeden:

- **USDT (Tether)** — piyasa değerine göre en büyüğü ve en çok işlem göreni, özellikle Asya'da ve birçok küresel borsada. Geçmişte rezerv şeffaflığı konusunda eleştirildi; şimdi üç ayda bir onay raporu yayımlıyor.
- **USDC (Circle)** — ikinci en büyüğü, bir ABD şirketi tarafından çıkarılıyor, aylık rezerv raporları var; AB'de MiCA kapsamında yetkili.

İkisi de birkaç blokzincirde çalışır (Ethereum, Tron, Solana ve diğerleri). Bir stablecoini her zaman alıcının desteklediği **aynı ağda** gönderin — USDT'yi yanlış ağdan göndermek fonların kaybolmasına yol açabilir.

## Stablecoin nasıl dikkatli kullanılır?

1. Lisanslı borsalar kullanın ve ülkenizde hangi stablecoinleri desteklediklerini kontrol edin.
2. Her transferden önce ağı ve adresi iki kez kontrol edin; önce küçük bir deneme gönderin.
3. Tek bir platformda, dondurulmasını göze alamayacağınızdan fazlasını tutmayın.
4. İhraççının en son rezerv raporunu okuyun.
5. Unutmayın: stablecoin tutmak kripto içinde dolar tutmaktır, büyüme beklenen bir yatırım değildir.

Amacınız uzun vadeli düzenli yatırımsa, varlıkların gerçekte nasıl performans gösterdiğini [DCA hesaplayıcımızla]({lang}/compare/) karşılaştırın ve [DCA'nın ne olduğunu](/en/blog/what-is-dca/) okuyun.

## Sık sorulan sorular

### Stablecoin bankadaki bir dolarla aynı şey mi?

Hayır. 1 dolar değerinde olmayı hedefler, ama özel bir ihraççı ya da akıllı sözleşme üzerindeki bir alacaktır ve genellikle mevduat sigortası yoktur.

### Stablecoin değer kaybedebilir mi?

Evet. Güven krizinde fiyat 1 doların altına inebilir; UST gibi algoritmik stablecoinler ise tamamen çöktü.

### Stablecoinler faiz öder mi?

Tokenin kendisi ödemez. Faiz sunan platformlar coinlerinizi borç verir veya yatırır, bu da risk ekler.

### Borsalar neden USDT ve USDC kullanıyor?

Yatırımcıların banka transferi olmadan kripto içinde dolar değeri tutmasını sağlarlar ve 7/24, sınır ötesi çalışırlar.

## Kaynaklar

- [Tether — Şeffaflık ve rezervler](https://tether.to/en/transparency/)
- [Circle — USDC şeffaflık](https://www.circle.com/transparency)
- [ESMA — Kripto Varlık Piyasaları Tüzüğü (MiCA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)
- [DefiLlama — Piyasa değerine göre stablecoinler](https://defillama.com/stablecoins)

*Yatırım tavsiyesi değildir. Bu yazı stablecoinlerin nasıl çalıştığını anlatır ve hiçbir coin, ihraççı veya platformu önermez.*
