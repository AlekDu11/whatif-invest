---
title: DEX nedir, kripto borsasından farkı ne?
description: DEX nedir? Merkeziyetsiz borsalar için sade rehber: AMM'ler, likidite havuzları, cüzdanlar, gas ücretleri ve CEX ile karşılaştırmalı artıları ve eksileri.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**DEX nedir?** DEX (merkeziyetsiz borsa), bir blokzincir üzerinde çalışan ve bir token'ı doğrudan kendi cüzdanınızdan başka bir token'la takas etmenizi sağlayan akıllı kontratlar bütünüdür. Paranızı tutan bir şirket yoktur, hesap yoktur ve genellikle kimlik doğrulaması da yoktur. Ethereum'daki Uniswap ile Solana'daki Raydium, Orca ve Meteora bilinen örneklerdir.

Binance, Coinbase veya Kraken gibi bildiğimiz kripto borsaları ise **CEX**'tir (merkezi borsa): fonlarınızı tutan, alıcı ve satıcıları kendi sisteminde eşleştiren ve finansal kurallara uymak zorunda olan bir şirket.

## DEX nasıl çalışır

### Otomatik piyasa yapıcılar (AMM)

Çoğu DEX'te alıcı ve satıcılardan oluşan bir emir defteri yoktur. Bunun yerine fiyatı bir formülle belirleyen bir **otomatik piyasa yapıcı** kullanılır.

Uniswap v2'nin kullandığı klasik versiyon "sabit çarpım" kuralıdır: bir havuz iki token tutar ve A token'ı miktarı ile B token'ı miktarının çarpımı her işlemden sonra aynı kalmalıdır. A token'ı aldığınızda havuza B ekler ve havuzdan A çıkarırsınız; böylece A havuzda azalır ve fiyatı yükselir.

Matematiği yapmanız gerekmez. Ana fikir şu: **havuz ne kadar büyükse işleminiz fiyatı o kadar az oynatır.**

### Likidite havuzları

Havuzdaki token'lar **likidite sağlayıcılarından** gelir: token çiftleri yatırıp işlem ücretlerinden pay alan kişiler (çoğu zaman takas başına %0,05–1). Riskleri, iki token'ın fiyatlarının birbirinden uzaklaşmasıdır; bu da onları token'ları sadece tutmaktan daha kötü bir durumda bırakabilir ("geçici kayıp" / impermanent loss).

Yeni çıkan token'larda ilk havuzu genellikle yaratıcı kurar. Likidite kilitlerinin önemli olmasının nedeni budur: havuzu kontrol eden kişi onu çekebilir.

### Cüzdanınız hesabınızdır

Bir DEX kullanmak için MetaMask (Ethereum ve benzeri ağlar) ya da Phantom (Solana) gibi kendi kontrolünüzdeki bir cüzdanı bağlarsınız. Her işlem, kendiniz imzaladığınız bir işlemdir. **Kurtarma ifadeniz (seed phrase)** ana anahtardır: kaybederseniz para gider, paylaşırsanız parayı başkası alır.

### Gas ve ücretler

Her DEX işlemi bir ağ ücreti öder; Ethereum'da buna **gas** denir. Ethereum'da ağ yoğunken yükselir; Katman-2 ağları ve Solana genellikle çok daha ucuzdur; Solana'nın temel ücreti imza başına 0,000005 SOL'dur. Gas'ın üstüne havuz ücreti ödersiniz, küçük ya da hızlı hareket eden token'larda da **slippage** ve **fiyat etkisi** ile karşılaşabilirsiniz.

## DEX ve CEX: temel farklar

- **Fonlarınızı kim tutar:** DEX'te siz (cüzdanınız); CEX'te borsa.
- **Hesap ve kimlik kontrolü:** DEX genellikle hiçbirini istemez; CEX kimlik doğrulaması (KYC) ister.
- **Token seçimi:** DEX yepyenileri dahil neredeyse her token'ı sunar; CEX yalnızca seçilmiş token'ları listeler.
- **Kart veya banka ile alım:** DEX'te doğrudan genellikle mümkün değildir; CEX'te standarttır.
- **Ücretler:** DEX'te gas, havuz ücreti ve slippage; CEX'te işlem ücreti, spread ve çekim ücreti.
- **Bir sorun olursa yardım:** DEX'in destek hattı yoktur; CEX'in müşteri desteği ve bazen koruma programları vardır.
- **Ana riskler:** DEX'te dolandırıcı token'lar, kötü onaylar ve kendi hatalarınız; CEX'te hack'ler, hesap dondurmaları ve iflas.

## DEX'in artıları

- **Kendi kontrolünüzde varlık.** Kimse hesabınızı donduramaz ya da bir iflasta paranızı kaybedemez.
- **Açık erişim.** Cüzdanı olan herkes, neredeyse her yerden işlem yapabilir.
- **Yeni token'lar önce burada.** Token'lar herhangi bir borsa listelemesinden çok önce (ya da onun yerine) DEX'lerde ortaya çıkar.
- **Şeffaflık.** Havuzlar, işlemler ve sahipler blokzincirde görünür.

## DEX'in eksileri

- **Banka sizsiniz.** Tek bir hata (yanlış adres, sahte site, kötü niyetli bir onay) ve fonlar kalıcı olarak kaybolur.
- **Dolandırıcı token'lar.** Herkes dakikalar içinde bir token ve havuz oluşturabilir. Yeni token'ların çoğu değerinin neredeyse tamamını kaybeder; [rug pull kontrol listemize]({lang}/blog/how-to-spot-a-rug-pull/) bakın.
- **Gizli maliyetler.** Slippage ve fiyat etkisi görünen ücretten fazlaya mal olabilir.
- **Kolay giriş yok.** Genellikle önce bir CEX'ten kripto alıp cüzdanınıza göndermeniz gerekir.
- **Akıllı kontrat riski.** DEX kodundaki hatalar ya da hack'ler büyük kayıplara yol açtı.

## Yeni başlayan biri hangisini kullanmalı?

Birçok kişi ikisini birlikte kullanır: yerel parayı kriptoya çevirmek için lisanslı bir CEX, yalnızca zincir üstünde bulunan token'lar için bir DEX. Bitcoin veya Ethereum gibi büyük varlıkları düzenli, uzun vadeli almak için düşük ücretli bir CEX genellikle daha basittir; seçenekleri [borsalar sayfamızda]({lang}/exchanges/) karşılaştırın.

Memecoin'leri ve diğer zincir üstü token'ları keşfetmek istiyorsanız çok küçük tutarlarla, ayrı bir cüzdanla ve [memecoin sayfamızdaki]({lang}/memes/) en yerleşik coin'lerle başlayın. Adım adım rehberimiz [Solana'da memecoin nasıl alınır]({lang}/blog/how-to-buy-memecoins-on-solana/), [GMGN](/go/gmgn?from=blog&l=tr) gibi araçlar dahil tüm süreci gösteriyor.

## Sık kullanılan DEX terimleri

- **Swap (takas)**: bir token'ı başka bir token'la değiştirmek.
- **Pair (çift)**: bir havuzdaki iki token, örneğin SOL/USDC.
- **Slippage toleransı**: kabul ettiğiniz en yüksek fiyat değişimi.
- **Approve (onay)**: bir kontratın cüzdanınızdan bir token'ı taşımasına verilen izin (çoğunlukla Ethereum tarzı ağlarda). Artık ihtiyaç duymadığınız eski onayları iptal edin.
- **Aggregator (toplayıcı)**: daha iyi fiyat için işleminizi birkaç DEX'e bölen hizmet; örneğin Solana'da Jupiter, Ethereum'da 1inch.

## Sık sorulan sorular

### DEX, CEX'ten daha mı güvenli?

Borsanın fonlarınızı kaybetmesi ya da dondurması riskini ortadan kaldırır, ama kendi hatalarınız ve dolandırıcı token'lar riskini ekler. İkisi de risksiz değildir.

### DEX kullanmak için kimlik gerekir mi?

Genellikle hayır, çünkü kendi cüzdanınızdan işlem yaparsınız. Yine de yerel yasalar ve vergiler sizin için geçerlidir.

### DEX işlemim neden başarısız oldu?

Yaygın nedenler: gas için yeterli ana coin yok, hızlı hareket eden bir fiyat için slippage çok düşük ayarlanmış ya da satışı engelleyen bir token.

### DEX işlemleri vergiye tabi mi?

Birçok ülkede evet; bir token'dan diğerine takas bir satış sayılabilir. İşlemlerinizin kaydını tutun.

## Kaynaklar

- [Uniswap nasıl çalışır (Uniswap dokümantasyonu)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas ve ücretler (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Solana dokümantasyonu: ücret yapısı](https://solana.com/docs/core/fees/fee-structure)

*Yatırım tavsiyesi değildir. Bu rehber DEX'lerin nasıl çalıştığını anlatır ve herhangi bir platform ya da token önermez.*
