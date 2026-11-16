---
title: Solana'da memecoin nasıl alınır? GMGN ile adım adım rehber
description: Solana'da memecoin nasıl alınır: cüzdan kurulumu, SOL yükleme, kontrat, likidite ve sahip kontrolü, slippage ayarı, işlem ücretleri ve satış adım adım.
date: 2026-11-16
category: guides
assets: sol, bonk, wif
---
**Solana'da memecoin nasıl alınır?** Kısaca: kendi kontrolünüzdeki bir cüzdan kurarsınız, içine biraz SOL koyarsınız, token'ın kontrat adresini bulursunuz, bunun bir tuzak olmadığını kontrol edersiniz ve SOL'u merkeziyetsiz bir borsada (DEX) ya da [GMGN](/go/gmgn?from=blog&l=tr) gibi bir işlem aracında token'a çevirirsiniz. Bu rehber her adımı sade bir dille anlatıyor.

Başlamadan önce dürüst bir gerçek: yeni memecoin'lerin çoğu değerinin neredeyse tamamını, çoğu zaman birkaç saat içinde kaybeder. Solidus Labs'in 2025 raporu, Pump.fun platformunda çıkarılan token'ların %98,6'sını rug pull ya da pump-and-dump (şişir ve sat) olarak sınıflandırdı. Yalnızca tamamen kaybetmeyi göze alabileceğiniz parayı kullanın.

## Neye ihtiyacınız var

- Güncel bir tarayıcısı olan akıllı telefon ya da bilgisayar.
- Kendi kontrolünüzde olan (self-custody) bir Solana cüzdanı; örneğin Phantom, Solflare veya Backpack.
- Biraz SOL, yani Solana ağının kendi coin'i. Memecoin'i de ağ ücretlerini de SOL ile ödersiniz.
- 30 dakika, bir de kurtarma kelimelerinizi yazmak için kâğıt ve kalem.

## Adım 1. Kendi kontrolünüzde bir cüzdan kurun

Self-custody cüzdan, anahtarları borsanın değil **sizin** tuttuğunuz anlamına gelir. Bu size tam kontrol verir, ama tüm sorumluluk da sizde olur.

1. Cüzdanı yalnızca resmi web sitesinden ya da telefonunuzun resmi uygulama mağazasından indirin. Sahte cüzdan uygulamaları sık rastlanan bir tuzaktır.
2. Yeni bir cüzdan oluşturun. Uygulama size 12 ya da 24 kelimelik bir **kurtarma ifadesi (seed phrase)** gösterecek.
3. Kelimeleri sırasıyla kâğıda yazın ve kâğıdı güvenli bir yerde saklayın. Ekran görüntüsü almayın, notlara veya e-postaya kaydetmeyin, hiçbir web sitesine yapıştırmayın.
4. Uygulama için güçlü bir şifre veya PIN belirleyin.

**Kurtarma ifadesi kuralı:** bu kelimelere sahip olan herkes cüzdandaki her şeyi alabilir. Gerçek bir destek ekibi, borsa ya da "airdrop" bunu asla istemez. Biri istiyorsa, bu dolandırıcılıktır.

İyi bir alışkanlık: memecoin'ler için ayrı bir "işlem" cüzdanı açın ve uzun vadeli birikiminizi başka yerde, tercihen bir donanım cüzdanında tutun.

## Adım 2. Cüzdana SOL yükleyin

En kolay yol, SOL'u merkezi bir borsadan alıp cüzdanınıza çekmektir.

1. [Borsalar sayfamızdan]({lang}/exchanges/) lisanslı bir borsa seçin ve kartla ya da banka havalesiyle SOL alın.
2. Cüzdanınızın Solana adresini kopyalayın (harf ve rakamlardan oluşur, yaklaşık 32–44 karakterdir).
3. Borsada "Çekme" bölümüne girin, SOL'u ve **Solana** ağını seçin, adresi yapıştırın.
4. Önce küçük bir deneme tutarı gönderin. Ulaştığında geri kalanını gönderin.

Cüzdanda her zaman biraz SOL (örneğin 0,01–0,02 SOL) harcanmadan kalsın. Daha sonra satış ücreti dahil, ücretleri ödemek için buna ihtiyacınız olacak.

## Adım 3. Token'ı ve doğru kontratı bulun

Memecoin'ler sık sık kopyalanır. On token aynı adı ve logoyu taşıyabilir; kastettiğiniz yalnızca biridir.

- **Kontrat adresini** (mint adresi de denir) güvenilir bir kaynaktan alın: projenin doğrulanmış hesabı, tanınmış bir veri sitesi ya da yerleşik coin'ler için [memecoin sayfamız]({lang}/memes/).
- İsimle aramak yerine kontrat adresini GMGN'ye ya da DEX'inize yapıştırın.
- Adresin ilk ve son karakterlerini kaynakla karşılaştırın. Dolandırıcılar birbirine benzeyen adresler üretir.

## Adım 4. Almadan önce token'ı kontrol edin

En çok para kurtaran adım budur. GMGN gibi araçlar bu kontrollerin çoğunu token sayfasında gösterir.

1. **Likidite.** İşlem havuzunda ne kadar para var? Likidite çok düşükse küçük bir satış bile fiyatı çok oynatır ve makul bir fiyattan satamayabilirsiniz.
2. **Likidite kilidi ya da yakımı.** Yaratıcı havuzu çekebiliyorsa "halıyı çekip" sizi kimsenin almadığı bir token'la baş başa bırakabilir.
3. **Mint yetkisi.** İptal edilmemişse yaratıcı yeni token basıp payınızı sulandırabilir.
4. **Dondurma (freeze) yetkisi.** İptal edilmemişse yaratıcı token'larınızı dondurabilir ve satamazsınız.
5. **En büyük sahipler.** İlk 10 cüzdan (havuz hariç) büyük bir pay tutuyorsa satarak fiyatı çökertebilir.
6. **Yaş ve geçmiş.** Birkaç dakika önce oluşturulmuş, grafiği dimdik yükselen bir token yatırım değil, piyango biletidir.

[Rug pull kontrol listemiz]({lang}/blog/how-to-spot-a-rug-pull/) on uyarı işaretinin hepsini ayrıntılı anlatıyor.

## Adım 5. Slippage'ı ayarlayın ve takası yapın

**Slippage (kayma)**, "al"a tıkladığınız an ile işlemin onaylandığı an arasında kabul ettiğiniz en yüksek fiyat değişimidir. Memecoin fiyatları hızlı hareket eder, bu yüzden uygulama bunu sizin seçmenize izin verir.

- Düşük slippage (yaklaşık %1) sizi kötü fiyattan korur ama işlem başarısız olabilir.
- Yüksek slippage (%10 ve üzeri) neredeyse her zaman gerçekleşir, ama beklediğinizden çok daha fazla ödeyebilirsiniz ve botlar bundan faydalanabilir.
- Düşükten başlayın, yalnızca bu dengeyi anlıyorsanız yükseltin.

Ardından cüzdanınızı [GMGN](/go/gmgn?from=blog&l=tr)'ye ya da bir DEX'e bağlayın, SOL miktarını girin, tahmini token sayısını ve fiyat etkisini kontrol edin ve cüzdanınızda onaylayın. Cüzdan ne imzaladığınızı gösterir, okuyun. Bir site beklenmedik bir şeyi onaylamanızı istiyorsa iptal edin.

## Adım 6. Ücretleri anlayın

Solana'da temel ağ ücreti çok küçüktür: imza başına 5.000 lamport (0,000005 SOL). Yoğun anlarda işleminiz daha hızlı işlensin diye isteğe bağlı bir **öncelik ücreti** de ödeyebilirsiniz. Bunun üstüne:

- İşlem platformu ya da bot kendi ücretini alabilir (çoğu zaman işlem başına yaklaşık %1); işlem yapmadan önce kontrol edin.
- Havuz, likidite sağlayıcılarına giden bir takas ücreti alır.
- **Fiyat etkisi** ve slippage gizli maliyetlerdir ve çoğu zaman ücretlerden büyüktür.

Küçük ve likiditesi düşük bir token'da gidiş-dönüş (alış ve satış) rahatlıkla yüzde birkaçlık maliyete çıkabilir.

## Adım 7. Satış

Satış da aynı şekilde, tersten işler: token'ı seçin, miktarı girin, slippage'ı kontrol edin ve onaylayın. Birkaç pratik nokta:

- Ücret için hâlâ SOL'unuz olduğundan emin olun.
- Satış "yetersiz likidite" ya da garip bir hatayla tekrar tekrar başarısız oluyorsa token bir honeypot olabilir: alabileceğiniz ama satamayacağınız şekilde tasarlanmış bir token.
- Ne kadar zarara katlanabileceğinize önceden karar verin. Memecoin'ler dakikalar içinde %50–90 düşebilir.
- Birçok ülkede her takas vergiye tabi bir işlem sayılabilir. İşlemlerinizin kaydını tutun.

## Riskler, açıkça

- **Paranın tamamını kaybetmek yaygın.** CoinGecko, 2021'den beri takip ettiği token'ların yarısından fazlasını 2025 sonu itibarıyla ölü saydı; yalnızca 2025'te yaklaşık 11,6 milyon token battı.
- **İçeridekiler önce hareket eder.** Yaratıcılar ve botlar çoğu zaman ilk saniyelerde alır ve ilk alıcı dalgasına satar.
- **Dolandırıcılık ve oltalama.** Sahte siteler, sahte destek ve kötü niyetli "onay" istekleri cüzdanınızı boşaltabilir.
- **Koruma yok.** Zincir üstü işlemler geri alınamaz ve genellikle yardım edecek bir düzenleyici ya da destek hattı yoktur.
- **Bu DCA değil.** Düzenli yatırım en iyi uzun geçmişi olan varlıklarda işe yarar. Yerleşik memecoin'lerin zaman içinde nasıl performans gösterdiğini [memecoin sayfamızda]({lang}/memes/) karşılaştırabilirsiniz.

## Sık sorulan sorular

### Solana'da memecoin almanın en ucuz yolu nedir?

Solana'da ağ ücretleri çok düşüktür; asıl maliyet genellikle platform ücreti, havuz ücreti ve fiyat etkisidir. Makul likiditeye sahip token'larda küçük tutarlarla işlem yapmak gizli maliyetleri düşük tutar.

### Solana memecoin'lerini normal bir borsadan alabilir miyim?

Bonk veya dogwifhat gibi daha büyük ve eski memecoin'ler birçok merkezi borsada listelidir. Yepyeni token'lar ise genellikle yalnızca DEX'lerde bulunur.

### GMGN bir cüzdan mı?

GMGN, zincir üstü token'lar için bir işlem ve analiz aracıdır. Hangi cüzdanı bağladığınızı ya da oluşturduğunuzu her zaman kontrol edin ve kurtarma ifadenizi hiçbir siteyle paylaşmayın.

### Memecoin'lere ne kadar para ayırmalıyım?

Yalnızca tamamen kaybetmeye hazır olduğunuz kadar. Birçok kişi bunu uzun vadeli birikiminden ayrı tuttuğu bir piyango bileti gibi görür.

## Kaynaklar

- [98% of tokens on Pump.fun have been rug pulls or an act of fraud, new report says (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [Solidus Labs: The 2025 Rug Pull Report](https://www.soliduslabs.com/reports/solana-rug-pulls-pump-dumps-crypto-compliance)
- [Solana dokümantasyonu: ücret yapısı](https://solana.com/docs/core/fees/fee-structure)
- [Dead coins: over 50% of cryptocurrencies have failed, CoinGecko report (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*Yatırım tavsiyesi değildir. Memecoin'ler son derece risklidir; bu rehber sürecin nasıl işlediğini anlatır ve herhangi bir token'ın alınmasını ya da satılmasını önermez.*
