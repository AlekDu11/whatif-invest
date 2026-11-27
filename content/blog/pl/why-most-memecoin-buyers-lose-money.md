---
title: "Dlaczego większość kupujących memecoiny traci pieniądze: matematyka startów, slippage i opłat"
description: Tylko 0,41% portfeli pump.fun zrealizowało ponad 10 000 $ zysku. Prosta matematyka startów, slippage i opłat, która działa przeciwko kupującym memecoiny.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41%
stat_label: z 13,55 mln portfeli pump.fun zrealizowało ponad 10 000 $ zysku (dane Dune, styczeń 2025)
---
**Dlaczego większość ludzi, którzy kupują memecoiny, traci pieniądze?** Bo matematyka działa przeciwko nim, zanim cena w ogóle drgnie: większość nowych tokenów umiera w ciągu doby, każdy zakup i każda sprzedaż kosztują opłaty i slippage, a najwcześniejsi kupujący (często boty i insiderzy) sprzedają tym, którzy przychodzą później. Żeby zarobić, token musi przetrwać *i* urosnąć na tyle, żeby to wszystko pokryć.

> **Najważniejsze**
> - Dane Dune opublikowane w styczniu 2025 r. pokazały, że tylko około **0,41%** z 13,55 mln portfeli pump.fun zrealizowało ponad **10 000 $** zysku.
> - CoinGecko wyliczył, że **68,67%** tokenów z pump.fun miało ostatnią transakcję w dniu startu (dane styczeń 2024 – czerwiec 2026).
> - Każda pełna runda (zakup + sprzedaż) na nowym tokenie może kosztować **2,5% i więcej** samych opłat platformy, plus opłaty sieciowe i slippage.

## Część 1 — Matematyka przetrwania

Większość memecoinów nie jest „tania” — po prostu żyje bardzo krótko.

- **Śmierć w dniu startu.** CoinGecko naliczył 18,67 mln tokenów z pump.fun; 68,67% z nich miało ostatnią transakcję w dniu, w którym wystartowały (dane z 25 czerwca 2026 r.).
- **Niewiele dociera do prawdziwego rynku.** „Graduation” (ukończenie) oznacza, że token opuszcza startową krzywą pump.fun i dostaje zwykłą pulę do handlu. Według Dune tygodniowy odsetek takich tokenów przez cztery tygodnie od 17 lutego 2025 r. był poniżej **1%**; najlepszy tydzień, w listopadzie 2024 r., dał **1,67%**. W marcu 2026 r. wskaźnik doszedł do **2,01%**, najwyżej od lipca 2025 r.

Jeśli więc wybierasz nowe starty na chybił trafił, będziesz głównie trzymać monety, którymi nikt już nie handluje. Kilku dużych zwycięzców nie pokryje wielu monet, które spadają do zera — chyba że wybierasz bardzo trafnie, a pierwszego dnia nikt nie wie, które przetrwają.

## Część 2 — Opłaty: płacisz przy wejściu i przy wyjściu

Strona pomocy pump.fun (wrzesień 2025 r.) podaje opłatę **1,25%** od każdej transakcji przed „graduation” (0,95% dla platformy, 0,30% dla twórcy). Po niej opłata spada wraz ze wzrostem tokena: od 1,25% dla najmniejszych do 0,30% dla największych. Do tego dochodzą opłaty sieci Solana oraz opcjonalne opłaty „priorytetowe” i za ochronę przed MEV (według ich strony 0,003–0,03 SOL za transakcję).

**Przykład liczbowy (ilustracja, nie prawdziwe ceny):** kupujesz nowy token za 50 $ i płacisz 0,02 SOL opłaty priorytetowej w obie strony. 1,25% przy wejściu i wyjściu to około 1,25 $, a dwie opłaty priorytetowe mogą dorzucić kolejne kilka dolarów. Żeby po prostu wrócić do 50 $, token musi urosnąć może o **5–10%**. Przy transakcjach po 10 $ jest dużo gorzej: stałe opłaty zjadają znacznie większą część.

## Część 3 — Slippage: cena ucieka, gdy kupujesz

**Slippage** (poślizg cenowy) to różnica między ceną, którą widzisz, a ceną, którą faktycznie dostajesz (zobacz [słowniczek memecoinów]({lang}/memes/glossary/)). Nowe tokeny mają malutkie pule, więc już Twój własny zakup podbija cenę — tak samo jak zakupy wszystkich innych w tej samej sekundzie. Jeśli ustawisz slippage na 10–20% (wiele aplikacji tak podpowiada dla nowych monet), zgadzasz się zapłacić aż tyle więcej. Przy sprzedaży jest ten sam problem, tylko w drugą stronę: w płytkiej puli Twoja sprzedaż zbija cenę.

## Część 4 — Kto jest po drugiej stronie

Najwcześniejsi kupujący to często snajperzy (snipers), bundlerzy i portfel twórcy (zobacz [snajperzy, bundlerzy i portfele twórców]({lang}/blog/snipers-bundlers-dev-wallets/)). Kupują po najniższej cenie i sprzedają przy pierwszej fali popytu. Jeśli kupujesz po pierwszej zielonej świecy, często to Ty jesteś „exit liquidity” — pieniędzmi, którym oni sprzedają.

## Krok po kroku: sprawdź matematykę, zanim naciśniesz «Buy»

1. **Krok 1 — Policz opłaty.** Spójrz na linię z opłatami na ekranie swapu i dodaj opłatę sieciową/priorytetową. Pomnóż przez dwa (zakup + sprzedaż).
2. **Krok 2 — Sprawdź slippage.** Ustaw go tak nisko, jak pozwala transakcja (np. 1–3% przy monecie z dużą pulą). Jeśli moneta wymaga 20% slippage, to sygnał ostrzegawczy.
3. **Krok 3 — Sprawdź wielkość puli.** Na naszej [stronie memów]({lang}/memes/) otwórz token i zobacz płynność. Mała pula = duży slippage w obie strony.
4. **Krok 4 — Zrób test bezpieczeństwa.** Skorzystaj z poradnika [jak sprawdzić memecoina przed zakupem]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Krok 5 — Z góry ustal, ile możesz stracić.** Używaj tylko pieniędzy, które możesz stracić w całości, i ustal kwotę, zanim zaczniesz.

> **⚠️ Uwaga**
> - **„Kosztuje tylko 0,0001 $, może zrobić 1000x.”** Niska cena nic nie znaczy; wiele tokenów istnieje w miliardach sztuk. Liczy się to, czy token przetrwa i kto Ci go sprzedaje.
> - **Mnóstwo malutkich transakcji.** Stałe opłaty sieciowe i priorytetowe mogą zjeść 10% i więcej z transakcji za 10 $, zanim cena w ogóle się ruszy.
> - **Zrzuty ekranu zwycięzców.** Widzisz 0,41%, którzy wygrali dużo, a nie miliony, które straciły; „guru” często sprzedają te monety, które sami polecają.

## Co to oznacza, jeśli kupujesz regularnie

Regularne małe zakupy działają przy aktywach, które istnieją jeszcze po latach — nie przy tokenach, którymi dziś wieczorem może przestać się handlować. Jeśli chcesz krypto, zwykła droga dla początkujących to duża, płynna moneta kupowana po trochu; dla porównania SOL, własna moneta Solany, kosztuje teraz {{price:sol}} ({{chg1y:sol}} w ciągu 12 miesięcy) — to wyniki z przeszłości, nie prognoza. W naszym kalkulatorze możesz sprawdzić «10 $ dziennie» na dowolnym aktywie i śledzić je na swojej [stronie portfela]({lang}/me/).

Poprzednia lekcja: [snajperzy, bundlerzy i portfele twórców]({lang}/blog/snipers-bundlers-dev-wallets/). Wszystkie lekcje są na [stronie Nauka]({lang}/learn/).

## Źródła

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11 stycznia 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14 marca 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, dane Dune: pump.fun graduation rate hits 2.01% (17 marca 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / dane CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25 czerwca 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [Centrum pomocy pump.fun: Transaction fees on pump.fun (wrzesień 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*To nie jest porada inwestycyjna.*
