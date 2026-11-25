---
title: Lighter (LIT) prostym językiem: kontrakty perpetual bez opłat na zk-rollupie Ethereum i co porusza tokenem
description: Lighter w prostych słowach: giełda kontraktów perpetual na własnym zk-rollupie Ethereum, zero opłat dla drobnych traderów, token LIT i główne ryzyka.
date: 2026-11-25
kind: analysis
---
**Lighter** to zdecentralizowana giełda kontraktów perpetual (bezterminowych futures) — umów, które pozwalają grać na cenę bitcoina, etheru i innych aktywów z dźwignią. Działa na własnym zk-rollupie na Ethereum, zwykli traderzy nie płacą opłat transakcyjnych, a każde dopasowanie zleceń jest sprawdzane dowodami z wiedzą zerową. Jej token **LIT** wystartował 30 grudnia 2025 r. i jest dziś wart {{mcap:lit}} ({{rank:lit}} wśród kryptowalut).

> **Najważniejsze**
> - Istnieje 1 mld LIT; 50% trafiło do ekosystemu, w tym 25% jako airdrop dla pierwszych użytkowników w grudniu 2025 r.
> - Rekord ceny to {{ath:lit}} ({{athd:lit}}); dziś cena jest {{fromath:lit}} od niego.
> - Tokeny zespołu (26%) i inwestorów (24%) były zablokowane przez rok po starcie, potem odblokowują się przez trzy lata.
> - Dla drobnych traderów handel przez stronę i aplikację jest darmowy; opłaty płacą profesjonalni traderzy przez API i HFT.

## Jak działa

Lighter to warstwa 2 na Ethereum. Transakcje odbywają się we własnym szybkim arkuszu zleceń Lighter, a specjalne układy z wiedzą zerową dowodzą, że zlecenia dopasowano uczciwie według ceny i czasu, a likwidacje, płatności funding i kontrole ryzyka przebiegły zgodnie z zasadami. Pieniądze użytkowników leżą w smart kontraktach Ethereum, a stan sieci przesuwa się dopiero po weryfikacji dowodu na Ethereum. Jeśli operator stanie lub zacznie cenzurować użytkowników, mogą oni wysłać żądania bezpośrednio do Ethereum albo wyjść awaryjnym trybem „Desert Mode”.

## Jak zarabia i do czego służy LIT

Model biznesowy Lighter jest nietypowy: kto handluje przez interfejs, nie płaci nic, a ruch przez API i handel wysokiej częstotliwości — animatorzy rynku i firmy tradingowe — płaci opłaty „premium”. Zespół twierdzi, że przychody giełdy i przyszłych produktów są widoczne on-chain i idą na rozwój oraz skup LIT, zależnie od warunków rynkowych; opłaty i skupy można śledzić na koncie skarbca w eksploratorze bloków Lighter.

LIT emituje amerykańska spółka Lighter. W styczniu 2026 r. staking stał się jego pierwszym dużym zastosowaniem: aby wpłacić środki do Lighter Liquidity Pool (LLP), który przynosi zysk i działa jako fundusz ubezpieczeniowy przy likwidacjach, trzeba zastakować 1 LIT na każde 10 USDC. Kto ma w stakingu co najmniej 100 LIT, nie płaci za wypłaty i przelewy, a staking daje zniżki na opłaty premium. Zespół planuje też powiązać ze stakingiem LIT swoją infrastrukturę transakcji i weryfikacji uczciwości.

## Liczby teraz

- Cena dziś: {{price:lit}}
- Rekord: {{ath:lit}} ({{athd:lit}}), {{fromath:lit}} od niego
- Wartość rynkowa: {{mcap:lit}} ({{rank:lit}} wśród kryptowalut)
- Całkowita podaż: 1 mld LIT (50% ekosystem, 26% zespół, 24% inwestorzy)

## Jego historia

Lighter założył w 2022 r. Vladimir Novakovski, który dostał się na Harvard w wieku 16 lat, a w wieku 18 zaczął pracować w Citadel. Projekt wyrósł z Lunchclub, aplikacji do networkingu opartej na AI, którą współtworzył w 2017 r.; większość tamtego zespołu przeszła do Lighter. W 2024 r. pozyskał 21 mln dolarów w rundzie prowadzonej przez Haun Ventures i Craft Ventures. Po około ośmiu miesiącach zamkniętych testów, z około 188 tys. kont, w październiku 2025 r. ruszył publiczny mainnet.

Wzrost był szybki: w połowie listopada 2025 r. tygodniowy wolumen sięgnął szczytu 74,9 mld dolarów, a za listopad 2025 r. Lighter podał 292,5 mld dolarów — więcej niż Aster i Hyperliquid. W tym samym miesiącu pozyskał 68 mln dolarów w rundzie prowadzonej przez Founders Fund i Ribbit Capital, z udziałem Haun Ventures i Robinhood, według doniesień przy wycenie około 1,5 mld dolarów. Na początku grudnia 2025 r. doszedł handel spot.

Handel LIT ruszył 30 grudnia 2025 r.; airdrop dla posiadaczy punktów z dwóch pierwszych sezonów 2025 r. był wtedy wart około 675 mln dolarów. Na początku stycznia 2026 r. konto skarbca zaczęło gromadzić LIT, co rynek odczytał jako skup, a 14 stycznia 2026 r. ogłoszono obowiązkowy staking dla LLP. Po airdropie wielu „farmerów” punktów odeszło: do połowy stycznia 2026 r. tygodniowy wolumen spadł do około 25,3 mld dolarów, mniej więcej jednej trzeciej szczytu, a Hyperliquid wrócił na pierwsze miejsce.

## Alternatywy

Głównym rywalem jest [Hyperliquid]({lang}/hype/), który działa na własnym blockchainie warstwy 1, a nie na Ethereum, i ma token HYPE. [Aster]({lang}/aster/) rywalizował z Lighter o pierwsze miejsce pod względem wolumenu pod koniec 2025 r., a [dYdX]({lang}/dydx/) to jedna z najstarszych zdecentralizowanych giełd kontraktów perpetual. Większość handlu kryptowalutowymi futures nadal przypada na duże scentralizowane giełdy, takie jak Binance i OKX.

## Główne ryzyka

- **Wolumen napędzany nagrodami:** duża część aktywności z 2025 r. pochodziła z farmienia punktów przed airdropem; po nim wolumen spadł w kilka tygodni mniej więcej trzykrotnie.
- **Odblokowania tokenów:** połowa podaży należy do zespołu i inwestorów; po rocznej blokadzie odblokowuje się przez trzy lata, co może zwiększać presję sprzedażową.
- **Konkurencja:** Hyperliquid, Aster i giełdy scentralizowane walczą o tych samych traderów, a handel bez opłat łatwo skopiować.
- **Technologia:** młody zk-rollup z własnym arkuszem zleceń i systemem dowodów może mieć błędy lub awarie, nawet z wyjściem przez Ethereum.
- **Regulacje:** instrumenty pochodne z dźwignią są w wielu krajach ściśle regulowane, a zasady dla zdecentralizowanych giełd mogą się zmienić.
- **Duże wahania:** LIT to młody token; silne spadki po starcie są częścią jego historii.

## Co to oznacza, jeśli kupujesz regularnie

LIT jest notowany krócej niż rok, więc nie ma długiej historii „10 dolarów dziennie” — każdy wynik obejmuje tylko krótki i bardzo zmienny okres. Regularny zakup za stałą kwotę rozkłada cenę wejścia w czasie zamiast stawiać na jeden moment, ale nie usuwa ryzyka strat, zwłaszcza przy młodym tokenie i nadchodzących odblokowaniach. Jeśli w ogóle kupować, wiele osób trzyma takie tokeny jako niewielką część oszczędności, na której silny spadek mogą sobie pozwolić. Wyniki z przeszłości nie gwarantują przyszłych zysków.

*To nie jest porada inwestycyjna.*

## Źródła

- [Lighter launches native token LIT, allocates half to ecosystem growth (The Block, 30 grudnia 2025)](https://www.theblock.co/post/383940/lighter-native-token-lit)
- [Lighter introduces mandatory LIT staking for liquidity pool access (The Block, 14 stycznia 2026)](https://www.theblock.co/post/385696/lighter-lit-staking)
- [Lighter opens public mainnet with Ethereum-settled zk perps (Blockworks)](https://blockworks.co/news/lighter-opens-public-mainnet)
- [DeFi founder who graduated Harvard at 18 raises $68 million for crypto trading protocol Lighter (Fortune, 11 listopada 2025)](https://fortune.com/2025/11/11/lighter-fundraise-founders-fund-ribbit-capital-haun-ventures-robinhood-vladimir-novakovski/)
- [Trading volume on Lighter plummets threefold after airdrop (ForkLog, 19 stycznia 2026)](https://forklog.com/en/news/trading-volume-on-lighter-exchange-plummets-threefold-after-airdrop)
- [Lighter: cena, kapitalizacja i rekord wszech czasów (CoinGecko)](https://www.coingecko.com/en/coins/lighter)
