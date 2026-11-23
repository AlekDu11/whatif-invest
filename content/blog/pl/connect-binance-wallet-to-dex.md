---
title: Jak połączyć Binance Wallet z DEX i przenieść monety z powrotem: krok po kroku
description: Bezpiecznie połącz Binance Wallet z DEX, odeślij monety na konto Binance właściwą siecią i usuń stare zgody — prostymi krokami.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: mały przelew testowy przed każdym nowym adresem lub siecią
---
**Jak połączyć Binance Wallet z DEX?** Otwórz oficjalną stronę DEX, kliknij **Connect Wallet** (połącz portfel), wybierz Binance Wallet (albo WalletConnect i zeskanuj kod QR aplikacją Binance) i potwierdź w aplikacji. Żeby przenieść monety z powrotem, skopiuj swój **adres wpłaty** na Binance dla tej samej monety i sieci, a potem wyślij na niego z portfela — najpierw małą kwotę testową.

> **Najważniejsze**
> - DEX (zdecentralizowana giełda — strona, na której wymieniasz tokeny prosto z własnego portfela) nigdy nie potrzebuje twojego hasła odzyskiwania ani frazy seed. Połączenie pozwala stronie tylko *poprosić* cię o podpis; nic się nie rusza, dopóki nie potwierdzisz.
> - Sieć musi się zgadzać po obu stronach (BNB Smart Chain do BNB Smart Chain, Solana do Solany). Zła sieć lub zły adres mogą oznaczać utratę monet.
> - Każde „Approve" pozwala stronie wydawać token w twoim imieniu. Dawaj małe zgody i usuwaj te, których już nie używasz.

Ta lekcja jest kontynuacją [Jak założyć Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Memecoiny są skrajnie ryzykowne — używaj tylko pieniędzy, na których stratę możesz sobie pozwolić.

## Krok 1 — Otwórz prawdziwą stronę

Fałszywe strony DEX z tym samym logo to jedna z najczęstszych pułapek.

1. Wpisz adres samodzielnie albo użyj zakładki. Nie klikaj reklam w wynikach wyszukiwania ani linków z czatów.
2. Sprawdź pasek adresu litera po literze.
3. Upewnij się, że DEX działa w sieci, w której są twoje monety.

## Krok 2 — Połącz portfel

Są trzy sposoby, zależnie od urządzenia:

- **Na komputerze z rozszerzeniem przeglądarki Binance Wallet** (Chrome lub Brave). Zaloguj się do rozszerzenia, skanując jego kod QR aplikacją Binance. Potem na DEX kliknij **Connect** lub **Connect Wallet**, wybierz Binance Wallet i potwierdź okienko.
- **Na komputerze bez rozszerzenia.** Na DEX kliknij **Connect Wallet → WalletConnect**. Pojawi się kod QR. Zeskanuj go skanerem w aplikacji Binance i stuknij **Connect**.
- **Na telefonie.** Otwórz DEX w przeglądarce telefonu, stuknij **Connect Wallet**, wybierz Binance Wallet z listy i potwierdź w aplikacji.

Zanim potwierdzisz, przeczytaj okienko: nazwę strony, adres i sieć. Jeśli coś wygląda źle, stuknij Cancel (anuluj).

## Krok 3 — Zrób swap i czytaj każdy podpis

1. Wybierz monetę, którą płacisz, i token, który chcesz (szukaj tokena po **adresie kontraktu**, nie po nazwie).
2. Wpisz małą kwotę i sprawdź kurs, slippage (największą zmianę ceny, jaką akceptujesz) i opłatę sieciową.
3. Gdy pierwszy raz sprzedajesz token, strona prosi o **Approve** (zgodę na wydawanie tego tokena). Jeśli aplikacja na to pozwala, ustaw kwotę zamiast „bez limitu".
4. Potwierdź swap w aplikacji. Jeśli prośba o podpis to strona nieczytelnego kodu albo nie ma sensu — **nie podpisuj**.

## Krok 4 — Odeślij monety na konto Binance

1. W aplikacji Binance przełącz się na **Exchange** → **Assets** (aktywa) → **Deposit** (wpłata). Wybierz monetę (na przykład BNB).
2. Wybierz **sieć** (na przykład BNB Smart Chain). Skopiuj adres wpłaty. Niektóre monety wymagają też **memo/tagu** — skopiuj go również.
3. Przełącz się na **Wallet** → **Send** (wyślij). Wybierz tę samą monetę i tę samą sieć. Wklej adres (i memo, jeśli jest).
4. Najpierw wyślij małą kwotę testową. Gdy dotrze na konto Binance, wyślij resztę.

Zostaw w portfelu trochę BNB lub SOL: każda operacja w blockchainie, nawet nieudana, kosztuje opłatę sieciową. Niektórych memecoinów w ogóle nie da się wpłacić na giełdę (bo ich nie notuje) — żeby wypłacić pieniądze, najpierw wymień je w portfelu na BNB, SOL lub USDT.

## Krok 5 — Rozłącz i posprzątaj

1. Po skończeniu rozłącz stronę (w ustawieniach połączonych stron lub WalletConnect w portfelu albo przyciskiem **Disconnect** na DEX).
2. Co jakiś czas sprawdzaj zgody na tokeny i cofaj (revoke) te, których nie potrzebujesz. Cofnięcie kosztuje niewielką opłatę.
3. Na wspólnym komputerze wyloguj się z rozszerzenia.

Kupione tokeny możesz śledzić w [swoim portfelu]({lang}/me/), a dane memecoinów na żywo zobaczysz na naszej [stronie memecoinów]({lang}/memes/).

> **⚠️ Uwaga**
> - **Strona lub „wsparcie" prosi o hasło odzyskiwania, frazę seed albo „synchronizację portfela".** Żaden prawdziwy DEX ani pracownik Binance tego nie robi. Zamknij stronę.
> - **Zgody bez limitu i podpisy na ślepo.** Złośliwa zgoda lub podpis może pozwolić oszustowi później opróżnić ten token bez twojego kolejnego potwierdzenia.
> - **Zła sieć, brak memo albo wklejony adres, który się zmienił.** Złośliwe oprogramowanie potrafi podmienić skopiowany adres. Za każdym razem porównuj pierwsze i ostatnie znaki i testuj małą kwotą.

Następna lekcja: jak sprawdzić memecoin przed zakupem. Wszystkie lekcje są na [stronie Nauka]({lang}/learn/).

## Źródła

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*To nie jest porada inwestycyjna. Ten poradnik wyjaśnia, jak działają narzędzia, i nie zaleca kupna żadnego tokena. Binance Wallet może nie być dostępny w każdym kraju.*
