---
title: "Opłaty w krypto w prostych słowach: prowizja, spread i opłata sieciowa"
description: W każdym zakupie i wypłacie krypto kryją się trzy koszty — prowizja, spread i opłata sieciowa. Jak działa każdy z nich i jak go zobaczyć przed potwierdzeniem.
date: 2026-11-26T13:40:00Z
category: learn
track: crypto
step: 8
assets: btc, eth, bnb
stat: 3 opłaty
stat_label: prowizja, spread i opłata sieciowa — sprawdź wszystkie trzy, zanim klikniesz „Potwierdź”
---
**Ile naprawdę płacisz, gdy kupujesz, sprzedajesz albo wysyłasz krypto?** Zwykle trzy rzeczy. **Prowizję transakcyjną** — to opłata dla giełdy. **Spread** — różnicę między ceną kupna a ceną sprzedaży. A gdy monety opuszczają giełdę, także **opłatę sieciową** — trafia ona do blockchaina. Najłatwiej zobaczyć wszystko naraz w linii „otrzymasz” na ekranie potwierdzenia.

> **Najważniejsze**
> - W przykładzie Binance zwykły użytkownik płaci prowizję **0,1%** od transakcji — $1 przy zakupie za $1 000. Płacąc ją w BNB, dostajesz **do 25% zniżki** (strony pomocy Binance, aktualizowane w styczniu–lutym 2026).
> - Proste przyciski „Kup” i płatność kartą często kosztują więcej niż arkusz zleceń, bo w cenie jest już spread, a czasem też opłata za kartę.
> - Opłata sieciowa Bitcoina zależy od **rozmiaru** transakcji w danych i od obciążenia sieci — **a nie od tego, ile pieniędzy wysyłasz**.

## Opłata 1 — prowizja transakcyjna

To opłata giełdy za samą transakcję. Liczy się ją jako procent od kwoty.

- We własnym przykładzie Binance stawka dla zwykłego użytkownika to 0,1%: przy zakupie 10 ETH prowizja wynosi 0,01 ETH. Prowizję pobiera się w monecie, którą **otrzymujesz**. Kupujesz ETH — płacisz w ETH. Sprzedajesz za USDC — płacisz w USDC.
- Wiele giełd ma dwie stawki. **Maker** — Twoje zlecenie czeka na liście, aż ktoś je przyjmie, np. zlecenie z limitem poniżej aktualnej ceny. **Taker** — zlecenie realizuje się od razu po bieżącej cenie. Stawka makera jest często taka sama albo niższa.
- Duzi traderzy mają niższe stawki (poziomy VIP). Początkujący płacą stawkę standardową.

**Krok 1 — Znajdź stronę z opłatami.** Na każdej dużej giełdzie jest strona **Fees** albo **Fee schedule** („Opłaty”, „Tabela opłat”). Na Binance: profil → **Fees & Transactions Overview**. Sprawdź stawkę spot dla swojego poziomu.

**Krok 2 — Włącz zniżki, które już Ci przysługują.** Na Binance trzymaj trochę BNB na koncie Spot i włącz **Using BNB Deduction** (płacenie prowizji w BNB) — w menu Fee Level albo w aplikacji: Account Center → Settings → BNB Discount. Binance podaje, że daje to do 25% zniżki na prowizje spot. Nie musisz kupować BNB specjalnie w tym celu — to pomaga tylko wtedy, gdy już je masz.

## Opłata 2 — spread

**Spread** to różnica między ceną, po której możesz kupić, a ceną, po której możesz sprzedać w tej samej chwili. Jeśli kupisz i od razu sprzedasz, stracisz spread nawet przy zerowej prowizji.

- Na głównym ekranie handlu (w arkuszu zleceń) dużej monety, takiej jak Bitcoin, spread jest zwykle bardzo mały.
- Na **prostych ekranach Buy / Sell / Convert** („Kup / Sprzedaj / Zamień”) giełda pokazuje jedną cenę, która zawiera już jej marżę. Coinbase na przykład pisze w swoich informacjach o cenach, że proste kupno i sprzedaż obejmują spread oprócz prowizji.
- Przy małych monetach i memecoinach spread może wynosić kilka procent, bo handluje nimi niewiele osób.

**Krok 3 — Porównaj dwie ceny.** Przed prostym zakupem otwórz wykres monety na tej samej giełdzie (albo na naszej [stronie Bitcoina]({lang}/btc/)) i porównaj cenę rynkową z ceną na ekranie potwierdzenia. Różnica to mniej więcej Twój spread.

**Krok 4 — Uważaj na opłatę za kartę.** Zakup kartą płatniczą to najszybszy sposób na start i często najdroższy: giełdy i partnerzy płatniczy zwykle doliczają kilka procent za kartę. Przelew bankowy albo P2P na giełdzie jest zwykle tańszy, ale wolniejszy — zobacz [jak kupić Bitcoina kartą płatniczą]({lang}/blog/how-to-buy-bitcoin-with-a-bank-card/).

## Opłata 3 — opłata sieciowa

Gdy **wypłacasz** monety do własnego portfela albo na inną giełdę, przelew zapisuje się w blockchainie. Ci, którzy utrzymują sieć (górnicy albo walidatorzy), pobierają za to opłatę.

- W Bitcoinie opłatę wycenia się w satoshi za wirtualny bajt (sat/vB; satoshi to jedna stumilionowa bitcoina). Prosta płatność ma około 140 vB, więc wysłanie 0,01 BTC albo 9 BTC taką samą transakcją kosztuje tyle samo.
- Gdy wiele osób wysyła naraz, opłaty rosną. Gdy w sieci jest spokojnie — spadają.
- Giełdy pokazują **opłatę za wypłatę** (withdrawal fee), która to pokrywa i bywa wyższa niż faktyczna opłata sieciowa. Często jest to stała kwota w monecie, a nie procent — dlatego najbardziej boli przy małych wypłatach.
- Różne sieci dla tej samej monety kosztują bardzo różnie (USDT w jednej sieci może kosztować centy, w innej kilka dolarów). Wybierz sieć, którą obsługuje adres odbiorcy — zobacz [jak wypłacić krypto do własnego portfela]({lang}/blog/how-to-withdraw-crypto-to-your-own-wallet/).

**Krok 5 — Przeczytaj ekran wypłaty przed potwierdzeniem.** Widać na nim sieć, opłatę i „kwotę do otrzymania” (amount received). Jeśli opłata jest duża w porównaniu z kwotą, poczekaj i wyślij raz większą kwotę zamiast wielu małych.

## Krok 6 — Zapisz to

Dodawaj każdy zakup z jego rzeczywistym kosztem do [swojego portfela]({lang}/me/). Wtedy wynik pokaże, ile naprawdę zapłaciłeś, a nie tylko zmianę ceny monety.

> **⚠️ Uwaga**
> - **Banery „zero prowizji”.** Transakcja może być bez prowizji, a mimo to mieć szeroki spread. Zawsze patrz na liczbę „otrzymasz”.
> - **Wiele drobnych wypłat.** Stała opłata kilku dolarów przy przelewie $20 to duża część Twoich pieniędzy.
> - **Zła sieć, żeby zaoszczędzić kilka centów.** Jeśli strona odbierająca nie obsługuje tej sieci, monety mogą przepaść. Najpierw sprawdź małą kwotą.

## Co to oznacza, jeśli kupujesz regularnie

Jeśli co tydzień kupujesz niewielką kwotę, opłaty się sumują. 0,1% od każdego zakupu to niewiele, ale kilka procent za kartę przy każdym zakupie — już tak. Osoby kupujące regularnie często zasilają konto przelewem bankowym, ustawiają zakup cykliczny na głównym rynku i tylko od czasu do czasu wypłacają monety do własnego portfela jednym większym przelewem. Przykład z naszego kalkulatora: $10 dziennie w Bitcoina przez 3 lata ({{dcainv:3}} łącznie) zamieniło się w {{dca:btc:3}} ({{dcaroi:btc:3}}), przed opłatami. To wyniki z przeszłości, a nie prognoza. Bitcoin kosztuje teraz {{price:btc}}.

Poprzednia lekcja: [Jak sprzedać krypto i przelać pieniądze na konto bankowe]({lang}/blog/how-to-sell-crypto-and-withdraw-to-bank/). Porównaj giełdy na naszej [stronie giełd]({lang}/exchanges/). Wszystkie lekcje znajdziesz na [stronie Nauka]({lang}/learn/).

## Źródła

- [Binance Support: jak obliczyć prowizje spot na Binance (aktualizacja: styczeń 2026)](https://www.binance.com/en/support/faq/detail/e85d6e703b874674840122196b89780a)
- [Binance Support: jak płacić prowizje w BNB i dostać 25% zniżki (aktualizacja: luty 2026)](https://www.binance.com/en/support/faq/115000583311)
- [Coinbase Help: informacje o cenach i opłatach](https://help.coinbase.com/en/coinbase/getting-started/getting-started-with-coinbase/pricing-and-fees)
- [Bitcoin.org: opłaty w Bitcoinie](https://bitcoin.org/fees/)
- [Ledger Academy: opłaty w Bitcoinie wyjaśnione (kwiecień 2026)](https://www.ledger.com/academy/bitcoin-fees)

*To nie jest porada inwestycyjna.*
