---
title: Jak rozpoznać rug pull: lista kontrolna 10 punktów przed zakupem nowego tokena
description: Jak rozpoznać rug pull przed zakupem: 10 punktów o blokadzie LP, mint i freeze authority, największych holderach, honeypotach, fałszywych socialach i wolumenie.
date: 2026-11-16
category: guides
assets: sol, pepe, bonk
---
**Jak rozpoznać rug pull?** Rug pull („wyciągnięcie dywanu”) to sytuacja, w której ludzie stojący za tokenem zabierają pieniądze, a kupujący zostają z czymś, czego nikt nie chce. Może to nastąpić nagle (twórca wypłaca płynność z puli) albo powoli (insiderzy po kawałku sprzedają swoje ogromne pakiety). Tak czy inaczej cena spada prawie do zera.

Rug pulle nie są rzadkością. W raporcie za 2025 rok firma analityczna Solidus Labs zaklasyfikowała **98,6%** z ponad 7 mln tokenów uruchomionych na launchpadzie Pump.fun jako rug pulle lub schematy pump-and-dump i ustaliła, że tylko ok. 97 000 utrzymało co najmniej 1000 $ płynności. Przejdź przez poniższą listę, zanim kupisz jakikolwiek nowy token.

## Dwa świeże przykłady

- **HAWK (grudzień 2024).** Memecoin promowany przez internetową celebrytkę wkrótce po starcie osiągnął wartość rynkową ok. 490 mln $, a potem w mniej niż trzy godziny spadł o ok. 91%. Analitycy on-chain twierdzili, że w chwili startu grupa portfeli insiderów i „snajperów” trzymała 80–90% podaży; jeden portfel kupił 17,5% podaży kilka sekund po starcie i sprzedawał przez kolejne 1,5 godziny. Promotorka zaprzeczyła, by ona lub jej zespół sprzedawali.
- **LIBRA (luty 2025).** Token promowany w mediach społecznościowych przez prezydenta Argentyny Javiera Mileia (Javier Milei) wystrzelił, a potem w ciągu kilku godzin się załamał. Według danych on-chain, o których pisał The Block, insiderzy wypłacili ok. 107 mln $, a Milei wycofał swoje poparcie.

Oba miały znane nazwiska, ogromny wolumen i rozgrzane media społecznościowe. Nic z tego nie ochroniło kupujących.

## Lista kontrolna: 10 punktów

### 1. Czy płynność jest zablokowana lub spalona?

Token jest handlowany względem puli płynności (np. token + SOL). Jeśli twórca trzyma tokeny LP tej puli, może ją wypłacić w każdej chwili. Szukaj płynności, która jest **spalona** albo **zablokowana** na długo w znanym lockerze, i sprawdź datę końca blokady. „Zaufaj mi, jest zablokowane” na czacie to żaden dowód.

### 2. Czy mint authority została cofnięta?

Na Solanie mint authority pozwala tworzyć nowe tokeny. Jeśli wciąż jest aktywna, twórca może dodrukować miliardy nowych tokenów i sprzedać je do puli. Strony tokenów w narzędziach takich jak GMGN, Solscan czy RugCheck pokazują, czy została cofnięta.

### 3. Czy freeze authority została cofnięta?

Freeze authority pozwala zamrażać konta tokenów. Twórca, który ją zachował, może zablokować ci sprzedaż, podczas gdy sam sprzedaje. W przypadku memecoina nie ma żadnego dobrego powodu, by ją zostawiać.

### 4. Jak skoncentrowani są najwięksi holderzy?

Otwórz listę holderów. Pomiń pulę i znane portfele giełd, a potem zsumuj top 10. Jeśli garstka portfeli ma duży udział w podaży, to one decydują o cenie. Uważaj na wiele „różnych” portfeli zasilonych z tego samego źródła — narzędzia typu bubble map pokazują takie klastry.

### 5. Czy da się w ogóle sprzedać? (test honeypota)

Honeypot pozwala kupić, ale nie sprzedać, albo pobiera ogromny ukryty podatek od sprzedaży. Sygnały ostrzegawcze: prawie brak transakcji sprzedaży w historii, nieudane sprzedaże lub kontrakt z nietypowymi zasadami transferu (częściej na Ethereum i BNB Chain). Narzędzia symulacyjne mogą przetestować sprzedaż, zanim kupisz.

### 6. Czy social media są prawdziwe?

Sprawdź stronę i konta na X/Telegramie. Czerwone flagi: konto założone w zeszłym tygodniu, tysiące obserwujących bez prawdziwej rozmowy, skopiowany tekst strony, „zespół” ze zdjęć stockowych, wyłączone komentarze albo linki inne niż te na stronie tokena.

### 7. Czy wolumen jest prawdziwy?

Nagła fala wolumenu z nowych portfeli, transakcje o niemal identycznej wielkości albo te same portfele kupujące i sprzedające sobie nawzajem (wash trading) mogą służyć do wypchnięcia tokena na listy „trending”. Prawdziwe zainteresowanie zwykle oznacza wiele różnych portfeli i stopniowy wzrost.

### 8. Jak wyglądał start?

Czy kilka portfeli kupiło duży udział w pierwszych sekundach? Czy portfel dewelopera sprzedał wkrótce po starcie? Wiele narzędzi pokazuje historię portfela „dev”, w tym wcześniejsze tokeny, które uruchomił — twórca ciągnący za sobą sznur martwych tokenów to wyraźne ostrzeżenie.

### 9. Kto to promuje i dlaczego?

Płatni influencerzy, starty z celebrytami i hasła o „gwarantowanym 100x” często oznaczają szczyt. Zapytaj: skoro ta osoba to promuje, to kiedy kupiła i po jakiej cenie?

### 10. Czy wykres ceny ma sens?

Pionowa świeca na tokenie, który ma kilka godzin, oznacza, że wcześni kupujący siedzą na dużych zyskach — i wielu z nich sprzeda kolejnym kupującym. Strach przed tym, że coś cię ominie (FOMO), to dokładnie to uczucie, które rug pull ma wywołać.

## Szybka rutyna przed każdym zakupem

1. Skopiuj adres kontraktu z zaufanego źródła.
2. Sprawdź status mint, freeze i płynności.
3. Przejrzyj największych holderów i klastry.
4. Przeskanuj historię transakcji pod kątem sprzedaży.
5. Ustal, ile maksymalnie możesz stracić — a potem podziel to na pół.

Jeśli którykolwiek punkt nie przechodzi, odpuść. Zawsze będzie inny token.

## Nawet „czyste” tokeny mogą spaść o 90%

Zaliczenie listy kontrolnej tylko zmniejsza ryzyko jawnego oszustwa. Nie sprawia, że token staje się dobrą inwestycją. Nawet najbardziej znane memecoiny mocno spadły od swoich szczytów; aktualne obsunięcia zobaczysz na naszej [stronie memecoinów]({lang}/memes/) i w [trackerze historycznych szczytów]({lang}/ath/). CoinGecko uznał ponad połowę tokenów śledzonych od 2021 roku za martwe na koniec 2025 roku.

## FAQ

### Czy rug pull jest nielegalny?

To zależy od kraju i szczegółów. Wiele rug pulli traktuje się jako oszustwo, ale środki on-chain rzadko udaje się odzyskać, więc zapobieganie jest dużo lepsze niż liczenie na sprawiedliwość.

### Czy zablokowana pula płynności oznacza, że token jest bezpieczny?

Nie. Usuwa to jeden sposób na rug pull, ale insiderzy wciąż mogą zrzucić duży udział podaży, a blokada może wygasnąć.

### Czy mogę odzyskać pieniądze po rug pullu?

Zwykle nie. Zgłoś sprawę na policję i do platformy oraz uważaj na „usługi odzyskiwania środków”, które żądają opłaty — często to drugie oszustwo.

### Jakie narzędzia pomagają sprawdzić token?

Strony tokenów w GMGN i screenerach DEX, eksploratory bloków takie jak Solscan oraz checkery takie jak RugCheck pokazują płynność, uprawnienia (authorities) i holderów. Korzystaj z więcej niż jednego.

## Źródła

- [98% tokenów na Pump.fun to rug pulle lub oszustwa, wynika z nowego raportu (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [Memecoin Hawk Tuah spada o 90% (Cointelegraph)](https://cointelegraph.com/news/hawk-tuah-memecoin-dumps-90-percent-outrage-token-launch-insider)
- [Milei wycofuje poparcie dla LIBRA po tym, jak insiderzy wypłacili 107 mln $ (The Block)](https://www.theblock.co/post/341206/argentinian-president-javier-milei-retracts-libra-endorsement-after-insiders-cash-out-107-million)
- [Martwe monety: ponad 50% kryptowalut upadło, raport CoinGecko (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*To nie jest porada inwestycyjna. Ta lista kontrolna zmniejsza ryzyko, ale nie może go wyeliminować; większość nowych tokenów traci niemal całą wartość.*
