---
title: Bir memecoin almadan önce nasıl kontrol edilir: 5 dakikada 6 kontrol
description: Bir memecoin almadan önce kontratı, likiditeyi, sahipleri, ilk 10'un payını, yaşını ve Binance güvenlik denetimini kontrol edin. Basit kontrol listesi.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: herhangi bir memecoin'i almadan önce yapılacak kontrol
---
**Bir memecoin almadan önce nasıl kontrol edilir?** Token'ı kontrat adresiyle bulun, ardından altı şeye bakın: güvenlik denetimi, likidite, sahip sayısı, en büyük 10 cüzdanın ne kadarına sahip olduğu, token'ın yaşı ve yaratıcının onu hâlâ değiştirip değiştiremeyeceği. Kontrollerden biri bile kırmızıysa o coin'i geçin. Binlercesi var.

> **Öne çıkanlar**
> - Bu kontroller bir memecoin'i güvenli yapmaz. Yalnızca en bariz tuzaklardan kaçınmanıza yardım eder: satamayacağınız token'lar, sahte kopyalar ve birkaç cüzdanın çökertebileceği coin'ler.
> - Binance Wallet'taki **Audit** (denetim) sekmesi kontrat, işlem ve dolandırıcılık risklerini kontrol eder (örneğin "honeypot" — alabildiğiniz ama asla satamadığınız bir token). Binance'in kendisi de denetimin kusursuz olmadığını söylüyor.
> - [Memecoin sayfamızda]({lang}/memes/) kalite filtresi varsayılan olarak açıktır: "Yalnızca kaliteli: likidite 100 bin $+, 1 gün+".

Bu ders [Binance Wallet bir DEX'e nasıl bağlanır]({lang}/blog/connect-binance-wallet-to-dex/) dersinin devamıdır. Memecoin'ler son derece risklidir — yalnızca kaybetmeyi göze alabileceğiniz parayı kullanın.

## Adım 1 — Doğru kontrat adresini bulun

Her token'ın bir **kontrat adresi** vardır (blokzincirdeki benzersiz kimliği, harf ve rakamlardan oluşan uzun bir dizi). Herkes aynı isim ve logoyla bir token oluşturabilir, yani isim tek başına hiçbir şey ifade etmez.

1. Adresi projenin resmi hesabından ya da güvenilir bir veri sitesinden kopyalayın.
2. Cüzdanınızdaki aramaya yapıştırın. İlk ve son 4 karakteri karşılaştırın.
3. Aynı isimde birkaç token görürseniz, diğerleri kopyadır.

## Adım 2 — Güvenlik denetimini açın

Binance uygulamasında token'ı **Wallet** (cüzdan) içinde açın ve **Audit** sekmesine dokunun (web sitesinde: token'a, ardından **Audit**'e tıklayın). Memecoin bölümümüzdeki token sayfalarında aynı kontrolü **Binance güvenlik kontrolü: Düşük risk / Orta risk / Yüksek risk** olarak görürsünüz.

Üç gruba bakın:

- **Contract risk** (kontrat riski) — yaratıcı satışı engelleyebilir, cüzdanları kara listeye alabilir, vergiyi ya da bakiyeleri değiştirebilir mi?
- **Trading risk** (işlem riski) — honeypot riski, alımda ya da satımda alışılmadık vergi (her işlemde kesilen bir ücret), düşük likidite, rug pull riski.
- **Scam risk** (dolandırıcılık riski) — sahte token, bilinen dolandırıcılık, spam.

Herhangi bir kırmızı madde = almayın. "Düşük risk" de güvenli demek değildir: yaratıcı siz aldıktan sonra da bir şeyler yapabilir.

## Adım 3 — Likiditeyi kontrol edin

Likidite, satış yapabilmenizi sağlayan işlem havuzundaki paradır. Çok azsa küçük bir satış bile fiyatı sert düşürür ve yaratıcı bu parayı çekebilir (rug pull — "halıyı çekmek"). WhatIfStack'te varsayılan filtremiz likiditesi 100 bin $'ın altındaki token'ları gizler. Veri sitesi gösteriyorsa havuzun likiditesinin kilitli mi yoksa yakılmış mı (kalıcı olarak kaldırılmış mı) olduğuna da bakın.

## Adım 4 — Sahipleri ve ilk 10'un payını sayın

Token sayfasında **Sahip** (kaç cüzdanın elinde olduğu) ve **İlk 10 tutuyor** (en büyük 10 cüzdanın tüm coin'lerin ne kadarını tuttuğu) bilgilerine bakın. Birkaç yüz sahip ve büyük bir ilk 10 payı, bir avuç kişinin satıp fiyatı çökertebileceği anlamına gelir. Dikkat: havuz ve yakma adresleri de ilk 10'da görünür — bu kısım normaldir.

## Adım 5 — Yaşını kontrol edin

Dolandırıcılık token'larının çoğu saatler ya da günler yaşar. Bir günden daha genç bir token'ın hiç geçmişi yoktur. /memes/ sayfasındaki filtremiz yalnızca en az 1 günlük token'ları gösterir. Daha eski olması güvenli olduğu anlamına gelmez — sadece daha az bilinmezdir.

## Adım 6 — Solana'da: yaratıcı token'ı hâlâ değiştirebilir mi?

Solana'da iki ayar önemlidir:

- **Mint authority** (basım yetkisi) — yeni token oluşturma hakkı. Hâlâ açıksa yaratıcı daha fazla basabilir ve sizin payınız küçülür.
- **Freeze authority** (dondurma yetkisi) — bir cüzdanı dondurma hakkı. Hâlâ açıksa yaratıcı coin'lerinizi taşımanızı ya da satmanızı engelleyebilir.

Daha güvenli durum "revoked" ya da "disabled"dır (yetki kimsede değil). İkisini de Solscan gibi bir blok gezgininde token sayfasında görebilirsiniz.

> **⚠️ Dikkat**
> - **Aynı isimli sahte kopya.** Her zaman kontrat adresiyle alın, asla isme ya da logoya göre almayın.
> - **Honeypot.** Alabilirsiniz, grafik yükselir, ama kimse satamaz. Alımları olup hiç satışı olmayan bir işlem geçmişi kırmızı bayraktır.
> - **Tek bir yeşil ışığa güvenmek.** Bir denetim, çok sayıda sahip ya da ünlü bir isim, fiyat sadece düştüğünde sizi korumaz — memecoin'lerin çoğu sıfıra yakın biter.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

Düzenli küçük alımlar, beş yıl sonra da büyük ihtimalle var olacak varlıklarla en iyi sonucu verir. Memecoin'lerin çoğu öyle değil. Yine de birini denemek istiyorsanız küçücük, sabit bir tutarla sınırlı kalın ve onu [portföyünüzde]({lang}/me/) paranızın geri kalanıyla birlikte takip edin.

Sonraki ders: Dogecoin'in hikâyesi. Tüm dersler [Öğren sayfasında]({lang}/learn/).

## Kaynaklar

- [Binance: How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US: What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs: Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs: Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*Yatırım tavsiyesi değildir. Bu rehber bir token'ın nasıl kontrol edileceğini anlatır ve herhangi bir coin'in alınmasını önermez.*
