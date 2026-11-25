---
title: Jak wypłacić krypto z giełdy do własnego portfela: krok po kroku
description: Bezpiecznie przenieś monety z giełdy do swojego portfela: skopiuj właściwy adres, wybierz tę samą sieć, dodaj memo i najpierw wyślij test.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 sieć
stat_label: giełda i portfel muszą używać tej samej, inaczej monety mogą przepaść
---
**Jak wypłacić krypto do własnego portfela?** W portfelu kopiujesz swój **adres do odbioru** danej monety. Potem na giełdzie otwierasz **Withdraw** („Wypłać”), wklejasz ten adres, wybierasz **tę samą sieć**, której używa portfel, wpisujesz małą kwotę testową i potwierdzasz przez 2FA. Gdy test dotrze, wysyłasz resztę.

> **Najważniejsze**
> - Muszą się zgadzać trzy rzeczy: **moneta**, **adres** i **sieć** (blockchain, którym płyną monety, np. Ethereum, BNB Smart Chain, TRON albo Solana). Binance ostrzega, że monety wysłane złą siecią mogą przepaść na zawsze.
> - Niektóre monety (np. XRP, XLM czy ATOM) wymagają też **memo** albo **tagu** (krótkiej liczby, po której odbiorca wie, czyje to monety). Bez niego przelew może utknąć albo trafić do niewłaściwej osoby.
> - **Zawsze najpierw wyślij mały test.** Wypłaty nie da się anulować, gdy monety opuściły już giełdę.

Ta lekcja jest kontynuacją lekcji [Jak ustawić zakup cykliczny]({lang}/blog/how-to-set-up-a-recurring-buy/). Po co w ogóle własny portfel, wyjaśniamy w lekcji o [portfelach gorących i zimnych]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Zanim zaczniesz

Potrzebujesz dwóch rzeczy. Po pierwsze konta na giełdzie z monetami, chronionego 2FA (zob. [Jak zarejestrować się na giełdzie kryptowalut]({lang}/blog/how-to-register-on-a-crypto-exchange/)). Po drugie własnej aplikacji portfela, już skonfigurowanej, z **frazą seed** (12 lub 24 tajnymi słowami, które odtwarzają portfel) zapisaną na papierze i trzymaną offline. Nigdy nie wpisuj frazy seed nigdzie indziej — nie będzie jej potrzebować żadna giełda, strona ani „pomoc techniczna”.

## Krok 1 — Skopiuj adres do odbioru z portfela

1. Otwórz aplikację portfela i stuknij **Receive** („Odbierz”; czasem **Deposit**).
2. Wybierz monetę, np. Bitcoina albo USDT.
3. Jeśli portfel pyta, wybierz sieć. Zapisz, która to — np. „USDT w sieci TRON (TRC20)” albo „USDT w sieci Ethereum (ERC20)”.
4. Stuknij **Copy** („Kopiuj”) obok adresu. Nie przepisuj go ręcznie.

Adres to długi ciąg liter i cyfr. Adresy Bitcoina często zaczynają się od **bc1**, adresy Ethereum i BNB Smart Chain od **0x**, a adresy TRON od **T**.

## Krok 2 — Otwórz Withdraw na giełdzie

Na Binance w aplikacji to **Assets → Spot → Send → Withdraw Crypto**, a na stronie **Wallet → Overview → Withdraw**. Inne giełdy mają przycisk **Withdraw** („Wypłać”) obok każdej monety na ekranie portfela lub portfolio. Wybierz tę samą monetę co w kroku 1.

## Krok 3 — Wklej adres i wybierz sieć

1. Wklej adres w pole **Address** („Adres”).
2. Porównaj **pierwsze 4 i ostatnie 4 znaki** z portfelem. Niektóre wirusy podmieniają skopiowany adres na adres złodzieja.
3. Wybierz **sieć**. Musi to być ta, którą pokazał portfel w kroku 1. Binance może sam podpowiedzieć sieć — i tak ją sprawdź. Nie wybieraj sieci tylko dlatego, że ma najniższą opłatę.
4. Jeśli pojawi się pole **Memo** albo **Tag**, a portfel podał ci taką wartość, wypełnij je. Jeśli twój portfel nie pokazuje memo, zwykle go nie potrzebuje — ale upewnij się w pomocy portfela.

Wskazówka: jeśli nie masz pewności, zapisz adres w **Address Management** (książce adresowej) na giełdzie. Binance ma też **whitelist** (białą listę): gdy ją włączysz, wypłaty mogą iść tylko na zapisane adresy. To pomaga, jeśli ktoś ukradnie twoje hasło.

## Krok 4 — Wyślij mały test

1. Wpisz małą kwotę — tylko trochę powyżej minimalnej wypłaty, którą pokazuje ekran.
2. Spójrz na wiersze **opłata sieciowa** i **otrzymasz**. Opłata jest stała za każdą wypłatę, więc przy bardzo małej kwocie może stanowić dużą część.
3. Naciśnij **Withdraw** i potwierdź kodem 2FA albo kluczem dostępu (passkey). Niektóre giełdy wysyłają też e-mail z potwierdzeniem — otwórz go i naciśnij **Confirm** („Potwierdź”).

## Krok 5 — Sprawdź, czy dotarło, i wyślij resztę

1. Poczekaj. Przelew może trwać od kilku sekund do mniej więcej godziny, zależnie od sieci i ruchu.
2. Na giełdzie otwórz historię wypłat: zobaczysz status i **TxID** (identyfikator transakcji, który można sprawdzić w eksploratorze blockchaina).
3. Gdy monety pojawią się w portfelu, powtórz kroki 2–4 z resztą. Adres jest już w historii lub książce adresowej, więc za drugim razem idzie szybciej.

Dodaj monety do [swojego portfolio]({lang}/me/), żeby śledzić ich wartość w jednym miejscu, gdziekolwiek są przechowywane.

> **⚠️ Uwaga**
> - **Zła sieć.** USDT istnieje w wielu sieciach. Wysłanie USDT „TRC20” na adres, który obsługuje tylko „ERC20”, może oznaczać utratę monet. Sprawdź sieć dwa razy.
> - **Brak memo lub tagu.** Giełdy i portfele, które wymagają memo, bez niego nie wiedzą, czyje monety przyszły. Odzyskanie ich, jeśli w ogóle możliwe, trwa długo i kosztuje.
> - **Fałszywa pomoc techniczna i strony do „weryfikacji adresu”.** Nikt uczciwy nie prosi o frazę seed ani o „weryfikację” portfela przez wysłanie monet. Wypłacaj tylko w oficjalnej aplikacji lub na oficjalnej stronie.

## Co to oznacza, jeśli kupujesz regularnie

Jeśli kupujesz po trochu co tydzień lub co miesiąc, nie musisz wypłacać po każdym zakupie — każda wypłata kosztuje. Wiele osób pozwala monetom zbierać się na giełdzie i co jakiś czas, np. raz na kwartał, przenosi je do własnego portfela jednym większym przelewem. Przykład z naszego kalkulatora: 10 $ dziennie w Bitcoinie przez 3 lata (łącznie {{dcainv:3}}) zamieniło się w {{dca:btc:3}} ({{dcaroi:btc:3}}). To wyniki z przeszłości, nie prognoza. Bitcoin kosztuje teraz {{price:btc}}; zobacz [stronę Bitcoina]({lang}/btc/).

Poprzednia lekcja: [Jak ustawić zakup cykliczny]({lang}/blog/how-to-set-up-a-recurring-buy/). Następna lekcja: jak sprzedać krypto i przelać pieniądze na konto bankowe. Porównaj giełdy na naszej [stronie giełd]({lang}/exchanges/); wszystkie lekcje znajdziesz na [stronie Nauka]({lang}/learn/).

## Źródła

- [Binance Support: How to deposit/withdraw cryptocurrency on Binance (aktualizacja: marzec 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: How to retrieve a crypto deposit with a wrong or missing tag/memo](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: How to withdraw crypto from your Binance.US account (czerwiec 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*To nie jest porada inwestycyjna.*
