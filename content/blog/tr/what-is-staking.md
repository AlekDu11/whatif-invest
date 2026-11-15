---
title: Kripto staking nedir, güvenli mi?
description: Kripto staking nedir, basitçe: nasıl çalışır, kilitleme süreleri, borsada ve zincir üstünde staking farkı ve stake etmeden önce bilmeniz gereken gerçek riskler.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
**Staking**, bir blokzincirin çalışmasına yardım etmek için kripto paraları kilitlemek ve karşılığında ödül olarak yeni coin almaktır. Sık sık vadeli mevduata benzetilir, ama çok farklı çalışır ve kendine özgü riskleri vardır.

Bu rehber stakingin nasıl çalıştığını, "kilitleme" (lock-up) ne demek olduğunu, borsada staking ile zincir üstü staking arasındaki farkı ve neyin ters gidebileceğini anlatıyor.

## Staking nasıl çalışır?

Birçok modern blokzincir — Ethereum, Solana, Cardano, Polkadot, Cosmos ve diğerleri — **proof of stake** (hisse kanıtı) adlı bir sistem kullanır. Ağı elektrikle güvence altına almak yerine (Bitcoin madenciliği gibi), **doğrulayıcılara** (validator) dayanırlar: işlemleri kontrol eden ve yeni bloklar ekleyen bilgisayarlar.

Doğrulayıcı olmak için dürüst davranışın teminatı olarak coin yatırmanız gerekir. Basit adımlarla:

1. Coinlerinizi ağda kilitlersiniz (stake edersiniz) — ya kendiniz bir doğrulayıcı çalıştırırsınız ya da bir doğrulayıcıya devredersiniz (delegasyon).
2. Doğrulayıcılar işlemleri onaylar ve blok üretir.
3. Ağ, yeni coinler ve işlem ücretlerinden bir pay şeklinde ödül öder.
4. Bir doğrulayıcı hile yaparsa ya da ciddi şekilde çevrimdışı kalırsa, yatırılan coinlerin bir kısmı kesilebilir. Buna **slashing** denir.

Bitcoin'in kendisi bu şekilde stake edilemez — proof of work kullanır. "Bitcoin getirisi" sunan ürünler genellikle borç verme veya başka düzenlemelerdir, staking değildir.

## Staking ödülleri nereden gelir?

Ödüller bedava para değildir. Çoğunlukla şuralardan gelir:

- Ağın ürettiği **yeni coinler** (coin arzının enflasyonu),
- Kullanıcıların ödediği **işlem ücretleri**.

Bu önemli: bir ağ yılda, diyelim, %5 yeni coin üretiyorsa ve siz %5 kazanıyorsanız, aslında zenginleşmekten çok ağdaki payınızı koruyorsunuz. Üstelik ödüller aynı coin ile ödenir — fiyatı düşerse toplam değeriniz yine de sert şekilde azalabilir.

Ödül oranları, stake eden sayısına ve ağ kurallarına göre sürekli değişir. İlan edilen her yüzdeyi bir söz olarak değil, anlık bir fotoğraf olarak görün.

## Kilitleme ve unbonding: coinlerinizi ne zaman geri alırsınız?

Staking genellikle coinlerinizin anında kullanılabilir olmadığı anlamına gelir. Her ağın kendi kuralları vardır:

- **Ethereum** — 2023'teki "Shapella" güncellemesinden beri çekim yapılabiliyor, ama çıkış bir kuyruktan geçiyor ve aynı anda çok kişi çıkmak istediğinde günler ile haftalar arasında sürebiliyor.
- **Solana** — stake'ten çıkış bir "epoch" sonunda geçerli olur, genellikle birkaç gün.
- **Cosmos ve Polkadot** — birkaç haftalık "unbonding" (çözülme) süreleri vardır; bu sürede coinler hiçbir şey kazanmaz ve satılamaz.
- **Cardano** — coinler cüzdanınızda kalır ve hiç kilitlenmez.

Neden önemli: unbonding süresinde piyasa düşerse satamazsınız. Stake etmeden önce her zaman o coinin güncel kurallarını kontrol edin.

## Borsada staking ile zincir üstü staking

Sıradan insanlar iki ana yoldan stake eder.

### Borsada staking (emanetçi)

Borsa uygulamasında "Stake" veya "Earn" düğmesine basarsınız, teknik işi borsa yapar.

- ✅ Çok kolay, küçük tutarlar yeterli, cüzdan kurmaya gerek yok.
- ❌ Coinleriniz borsada durur. Borsa batarsa, hacklenirse veya çekimleri dondurursa coinleriniz risk altındadır.
- ❌ Borsa ödüllerin bir kısmını komisyon olarak alır.
- ❌ Bazı "earn" ürünleri aslında staking değil borç vermedir — çok farklı bir risk.

Düzenleyiciler bu hizmetleri yakından inceledi. 2023'te ABD SEC, Kraken'i staking programı nedeniyle suçladı; Kraken 30 milyon dolar ödedi ve hizmeti ABD'li müşteriler için kapattı. 2025'te SEC personeli, bazı doğrudan "protokol staking" biçimlerinin menkul kıymet işlemi olmadığını açıkladı. Kurallar ülkeden ülkeye değişir ve değişmeye devam ediyor.

### Zincir üstü staking (emanetsiz)

Coinleri kendi cüzdanınızda tutar ve bir doğrulayıcıya devredersiniz ya da kendiniz doğrulayıcı çalıştırırsınız.

- ✅ Anahtarlar sizde; kimse hesabınızı donduramaz.
- ✅ Genellikle daha düşük ücretler.
- ❌ Daha teknik: yanlış adresler, oltalama (phishing) ve kötü doğrulayıcılar sizin sorununuzdur.
- ❌ Kendi Ethereum doğrulayıcınızı çalıştırmak için 32 ETH ve güvenilir donanım gerekir.

### Likit staking

Ortada bir seçenek: bir protokol üzerinden stake edersiniz ve stake ettiğiniz coinleri temsil eden bir token alırsınız (örneğin "staked ETH" tokeni). Coinleriniz ödül kazanırken bu tokeni alıp satabilirsiniz. Bedeli, ek **akıllı sözleşme riski** ve tokenin arkasındaki coinlerin değerinin altında işlem görme ihtimalidir.

## Stakingin başlıca riskleri

Staking güvenli mi? Birçok "yüksek getirili" kripto ürününden daha az risklidir, ama asla risksiz değildir:

1. **Fiyat riski.** En büyüğü. Coin %50 düşerse birkaç yüzdelik ödül pek bir şey ifade etmez. Coinlerin ne kadar oynak olduğunu [Ethereum sayfasında]({lang}/eth/) veya [Solana sayfasında]({lang}/sol/) görün.
2. **Kilitleme riski.** Bir çöküş sırasında satamayabilirsiniz.
3. **Platform riski.** Borsalar ve borç verme platformları batabilir. Celsius 2022'de çöktüğünde, "earn" programının kullanıcıları coinlerine erişimi kaybetti.
4. **Slashing.** Kurallara uymayan bir doğrulayıcı yatırılan coinlerin bir kısmını kaybedebilir — bazı ağlarda devredilen coinler de dahil.
5. **Akıllı sözleşme riski** likit staking ve DeFi'de.
6. **Vergiler.** Birçok ülkede staking ödülleri alındığı anda vergiye tabi gelir sayılır. Yerel kuralları kontrol edin.
7. **Dolandırıcılık.** Sahte staking siteleri ve "ayda %20 garantili" teklifler yaygındır. [Kripto dolandırıcılığından nasıl korunulur]({lang}/blog/how-to-avoid-crypto-scams/) rehberimizi okuyun.

## Stake etmeden önce dikkatli bir kontrol listesi

- Yalnızca zaten uzun süre tutmayı planladığınız coinleri stake edin.
- Unbonding süresini ve paraya daha erken ihtiyacınız olup olmayacağını kontrol edin.
- Coinlerinizi kimin tuttuğunu anlayın — siz mi, bir platform mu.
- Ücretleri karşılaştırın: platform ödüllerin ne kadarını alıyor?
- Çok yüksek sabit getiri vaat eden tekliflerden uzak durun — gerçek staking ödülleri değişkendir.
- Küçük başlayın ve bir çekim işlemini test edin.

Staking asıl soruyu değiştirmez: coinin kendisi uzun vadeli planınıza uyuyor mu? DCA gibi düzenli alım planı, varlığın yıllar içindeki fiyatıyla ilgilidir — bunu [DCA hesaplayıcımızla]({lang}/compare/) deneyebilirsiniz. 5 yıl boyunca Ethereum'a günde 10 dolar yatırmak — hiçbir staking ödülü olmadan — şöyle sonuçlanırdı: {{dcainv:5}} yatırımla {{dca:eth:5}} ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## Sık sorulan sorular

### Staking faiz kazanmakla aynı şey mi?

Hayır. Faiz bir borçludan gelir; staking ödülleri ise ağı güvence altına almaya yardım ettiğiniz için ağın kendisinden gelir. Ödüller coin olarak ödenir, bu yüzden değerleri coinin fiyatıyla birlikte değişir.

### Staking yaparken para kaybedebilir miyim?

Evet. Coinin fiyatı düşebilir, platform batabilir ve nadir durumlarda slashing yatırdığınız miktarı azaltabilir. Ödüller sizi fiyat düşüşüne karşı korumaz.

### Bitcoin stake edilebilir mi?

Yerel olarak hayır — Bitcoin proof of work kullanır. "Bitcoin getirisi" teklifleri genellikle farklı riskleri olan borç verme veya başka ürünlerdir.

### Borsada staking mi, cüzdanda staking mi daha iyi?

Borsada staking daha basittir; cüzdanda staking anahtarlarınızın kontrolünü size verir. Doğru seçim, cüzdan yönetmekte ne kadar rahat olduğunuza bağlıdır — [sıcak ve soğuk cüzdanlar]({lang}/blog/crypto-wallets-hot-vs-cold/) rehberimize bakın.

## Kaynaklar

- [ethereum.org — Ethereum staking](https://ethereum.org/en/staking/)
- [ethereum.org — Staking çekimleri](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [ABD SEC — Kraken staking programını durduruyor, 30 milyon dolar ödüyor (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: bazı protokol staking faaliyetleri menkul kıymet işlemi değildir (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Yatırım tavsiyesi değildir. Bu rehber stakingin nasıl çalıştığını anlatır ve hiçbir coin, platform veya doğrulayıcıyı önermez.*
