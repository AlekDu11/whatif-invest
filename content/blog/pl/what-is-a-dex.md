---
title: Co to jest DEX i czym różni się od zwykłej giełdy kryptowalut?
description: Co to jest DEX? Prosty przewodnik po zdecentralizowanych giełdach: AMM, pule płynności, portfele, opłaty za gas oraz plusy i minusy w porównaniu z giełdą CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Co to jest DEX?** DEX (zdecentralizowana giełda) to zestaw smart kontraktów na blockchainie, który pozwala wymienić jeden token na inny bezpośrednio z własnego portfela. Nie ma firmy, która trzyma twoje pieniądze, nie ma konta i zwykle nie ma weryfikacji tożsamości. Znane przykłady to Uniswap na Ethereum oraz Raydium, Orca i Meteora na Solanie.

Zwykła giełda kryptowalut, taka jak Binance, Coinbase czy Kraken, to **CEX** (scentralizowana giełda): firma, która przechowuje twoje środki, kojarzy kupujących i sprzedających we własnym systemie i musi przestrzegać przepisów finansowych.

## Jak działa DEX

### Automatyczni animatorzy rynku (AMM)

Większość DEX-ów nie ma arkusza zleceń z kupującymi i sprzedającymi. Zamiast tego używa **automatycznego animatora rynku** (AMM) — wzoru, który ustala cenę.

Klasyczna wersja, używana przez Uniswap v2, to zasada „stałego iloczynu”: pula zawiera dwa tokeny, a ilość tokena A pomnożona przez ilość tokena B musi pozostać taka sama po każdej transakcji. Gdy kupujesz token A, dodajesz do puli token B i zabierasz token A, więc A staje się w puli rzadszy i jego cena rośnie.

Nie musisz liczyć. Kluczowa myśl: **im większa pula, tym mniej twoja transakcja rusza ceną.**

### Pule płynności

Tokeny w puli pochodzą od **dostawców płynności** — ludzi, którzy wpłacają pary tokenów i dostają część opłat transakcyjnych (często 0,05–1% od swapu). Ich ryzyko polega na tym, że ceny obu tokenów się rozjadą, przez co mogą wyjść gorzej, niż gdyby po prostu trzymali tokeny („nietrwała strata”, impermanent loss).

W przypadku świeżo uruchomionych tokenów pierwszą pulę zwykle zakłada sam twórca. Dlatego blokady płynności mają znaczenie: kto kontroluje pulę, ten może ją wypłacić.

### Twój portfel to twoje konto

Żeby korzystać z DEX-a, łączysz portfel self-custody, taki jak MetaMask (Ethereum i podobne sieci) lub Phantom (Solana). Każda transakcja to operacja, którą podpisujesz sam. Twoja **fraza seed** to klucz główny — zgubisz ją, a pieniądze przepadną; udostępnisz ją, a ktoś inny je zabierze.

### Gas i opłaty

Każda transakcja na DEX-ie płaci opłatę sieciową, na Ethereum nazywaną **gas**. Na Ethereum rośnie ona, gdy sieć jest zatłoczona; sieci warstwy 2 (Layer-2) i Solana są zwykle dużo tańsze — podstawowa opłata Solany to 0,000005 SOL za podpis. Oprócz gasu płacisz opłatę puli, a przy małych lub szybko zmieniających się tokenach możesz trafić na **slippage** i **price impact**.

## DEX a CEX: główne różnice

- **Kto trzyma środki:** na DEX-ie ty (twój portfel); na CEX-ie giełda.
- **Konto i weryfikacja tożsamości:** DEX zwykle nie wymaga niczego; CEX wymaga weryfikacji (KYC).
- **Wybór tokenów:** DEX oferuje niemal każdy token, także zupełnie nowe; CEX notuje tylko wybrane.
- **Zakup kartą lub przelewem:** na DEX-ie bezpośrednio zwykle niemożliwy; na CEX-ie standard.
- **Opłaty:** DEX — gas, opłata puli i slippage; CEX — prowizja transakcyjna, spread i opłata za wypłatę.
- **Pomoc, gdy coś pójdzie nie tak:** DEX nie ma infolinii; CEX ma obsługę klienta, a czasem programy ochrony.
- **Główne ryzyka:** DEX — oszukańcze tokeny, złe zatwierdzenia (approve) i twoje własne błędy; CEX — włamania, zamrożenie konta i niewypłacalność.

## Zalety DEX-a

- **Self-custody.** Nikt nie zamrozi ci konta ani nie straci twoich pieniędzy w bankructwie.
- **Otwarty dostęp.** Handlować może każdy, kto ma portfel, z niemal dowolnego miejsca.
- **Nowe tokeny najpierw.** Tokeny pojawiają się na DEX-ach długo przed notowaniem na giełdzie (albo zamiast niego).
- **Przejrzystość.** Pule, transakcje i holderzy są widoczni na blockchainie.

## Wady DEX-a

- **To ty jesteś bankiem.** Jeden błąd — zły adres, fałszywa strona, złośliwe zatwierdzenie — i środki przepadają na zawsze.
- **Oszukańcze tokeny.** Każdy może w kilka minut stworzyć token i pulę. Większość nowych tokenów traci niemal całą wartość; zobacz naszą [listę kontrolną rug pull]({lang}/blog/how-to-spot-a-rug-pull/).
- **Ukryte koszty.** Slippage i price impact mogą kosztować więcej niż widoczna opłata.
- **Brak łatwego wejścia.** Zwykle najpierw musisz kupić kryptowaluty na CEX-ie i wysłać je do swojego portfela.
- **Ryzyko smart kontraktów.** Błędy lub włamania w kodzie DEX-ów powodowały już duże straty.

## Co wybrać na początek?

Wiele osób korzysta z obu: z licencjonowanego CEX-a, żeby zamienić lokalną walutę na kryptowaluty, i z DEX-a do tokenów dostępnych tylko on-chain. Do regularnego, długoterminowego kupowania dużych aktywów, takich jak Bitcoin czy Ethereum, zwykle prostszy jest CEX z niskimi opłatami — porównaj opcje na naszej [stronie giełd]({lang}/exchanges/).

Jeśli chcesz poznać memecoiny i inne tokeny on-chain, zacznij od drobnych kwot, osobnego portfela i najbardziej uznanych monet z naszej [strony memecoinów]({lang}/memes/). Nasz poradnik krok po kroku [jak kupić memecoina na Solanie]({lang}/blog/how-to-buy-memecoins-on-solana/) pokazuje cały proces, w tym narzędzia takie jak [GMGN](/go/gmgn?from=blog&l=pl).

## Najważniejsze pojęcia DEX

- **Swap** — wymiana jednego tokena na inny.
- **Para** — dwa tokeny w puli, np. SOL/USDC.
- **Tolerancja poślizgu (slippage tolerance)** — maksymalna zmiana ceny, jaką akceptujesz.
- **Approve (zatwierdzenie)** — zgoda dla kontraktu na przenoszenie tokena z twojego portfela (głównie w sieciach typu Ethereum). Cofaj stare zatwierdzenia, których już nie potrzebujesz.
- **Agregator** — usługa, która dzieli twoją transakcję między kilka DEX-ów, by uzyskać lepszą cenę, np. Jupiter na Solanie lub 1inch na Ethereum.

## FAQ

### Czy DEX jest bezpieczniejszy niż CEX?

Usuwa ryzyko, że giełda straci lub zamrozi twoje środki, ale dodaje ryzyko twoich własnych błędów i oszukańczych tokenów. Żadna opcja nie jest wolna od ryzyka.

### Czy do korzystania z DEX-a potrzebny jest dowód osobisty?

Zwykle nie, bo handlujesz z własnego portfela. Lokalne przepisy i podatki nadal cię obowiązują.

### Dlaczego moja transakcja na DEX-ie się nie udała?

Typowe powody: za mało natywnej monety na gas, slippage ustawiony zbyt nisko przy szybko zmieniającej się cenie albo token, który blokuje sprzedaż.

### Czy transakcje na DEX-ie podlegają podatkowi?

W wielu krajach tak — wymiana jednego tokena na inny może liczyć się jako sprzedaż. Prowadź ewidencję swoich transakcji.

## Źródła

- [Jak działa Uniswap (dokumentacja Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas i opłaty (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Dokumentacja Solana: struktura opłat](https://solana.com/docs/core/fees/fee-structure)

*To nie jest porada inwestycyjna. Ten poradnik wyjaśnia, jak działają DEX-y, i nie poleca żadnej platformy ani tokena.*
