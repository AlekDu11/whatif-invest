---
title: "Snipers, bundlers y wallets del desarrollador: cómo ganan los insiders en el lanzamiento de una memecoin"
description: Bots e insiders compran muchas memecoins nuevas en el primer segundo y venden en minutos. Cómo funcionan snipers, bundlers y dev wallets, y cómo detectarlos.
date: 2026-11-27T09:30:00Z
category: learn
track: memes
step: 16
assets: sol, bnb
stat: 87%
stat_label: de los snipes en pump.fun desde wallets ligadas al creador fueron rentables (Pine Analytics, abril 2025)
---
**¿Quién compra una memecoin nueva antes de que tú puedas siquiera verla?** Muchas veces, bots e insiders. Los **snipers** (francotiradores) compran en el primerísimo bloque, los **bundlers** compran con muchas wallets a la vez y la **dev wallet** (la wallet propia del creador) puede tener una gran parte desde el principio. Compran al precio más bajo y a menudo venden en minutos… a quienes llegan después.

> **Claves**
> - Pine Analytics descubrió que más del **50%** de los tokens de pump.fun sufrieron snipes en el mismo bloque en que se crearon (informe del 21 de abril de 2025).
> - En un mes (desde el 15 de marzo de 2025) contó **más de 15.000** snipes de wallets financiadas directamente por el creador del token; el **87%** fueron rentables y cerca del **85%** se vendieron por completo en **5 minutos**.
> - CoinGecko halló que el **68,67%** de 18,67 millones de tokens de pump.fun hicieron su última operación el día del lanzamiento (enero de 2024 – junio de 2026, datos del 25 de junio de 2026).

## Los tres insiders, en palabras sencillas

Las tres palabras están en nuestro [glosario de memecoins]({lang}/memes/glossary/).

- **Sniper** — una wallet, casi siempre un bot, que compra en los primeros 0–3 bloques (un bloque es una «página» de la blockchain; en Solana dura menos de un segundo). Usa herramientas especiales para entrar antes que los compradores normales, toma una posición grande barata y vende en la primera ola de demanda.
- **Bundler** — una sola persona que compra con muchas wallets en el mismo bloque o en la misma transacción. En el gráfico parecen 20 compradores distintos; en realidad es uno. Objetivo: ocultar cuánto tiene una persona y fingir demanda.
- **Dev wallet** — la wallet que creó el token. Si se queda con una gran parte, o envía tokens en silencio a wallets nuevas, puede vender sobre todos en cualquier momento.

El informe de Pine Analytics «Exit Liquidity Machines» (exit liquidity, «liquidez de salida», son los compradores tardíos a los que los insiders les venden) mostró cómo funciona esto en pump.fun: los creadores enviaban SOL a wallets «desechables» (burner) recién creadas, esas wallets compraban en el bloque de creación y la mayoría vendía en una o dos operaciones. Más del 55% de esos snipes se cerraron por completo en menos de un minuto.

## Paso 1 — Mira a los primeros compradores

Abre el token en un rastreador (en nuestra [página de memecoins]({lang}/memes/) la ficha del token muestra los holders y un control de seguridad; herramientas como GMGN o Solscan muestran las primeras operaciones). Si muchas wallets compraron **en el mismo segundo del lanzamiento**, con **importes parecidos**, eso es sniping o bundling.

## Paso 2 — Comprueba cuánto tienen los mayores holders

Mira los **10 mayores holders** sin contar el pool de liquidez. El proveedor de datos Mobula considera sano que el top 10 tenga menos del **30%** y el desarrollador menos del **5%** (o bloqueado/quemado), y una señal de alarma que el top 10 supere el **50%**. Que varias wallets sniper sumen más del 20% es otra.

## Paso 3 — Revisa la dev wallet

Busca al creador («dev», «deployer» o «creator» en la página del token). ¿Ya ha vendido? ¿Envió tokens a wallets nuevas justo antes o después del lanzamiento? ¿Esa misma wallet ha lanzado muchos tokens que murieron todos? Un dev que lanza decenas de monedas por semana tiene una fábrica, no un proyecto.

## Paso 4 — Busca wallets nuevas financiadas desde un mismo origen

Los bundles suelen venir de wallets creadas minutos antes del lanzamiento y financiadas por la misma fuente. Las herramientas de bubble map (mapa de burbujas) las dibujan como un único grupo conectado. Si la «comunidad» es un solo grupo, el precio está en manos de una persona.

## Paso 5 — Nunca persigas la primera vela

El salto de los primeros minutos es justo cuando venden los snipers. Si aun así quieres comprar, espera, haz la revisión completa de [cómo revisar una memecoin antes de comprar]({lang}/blog/how-to-check-a-memecoin-before-buying/), usa una cantidad pequeña y fija tu límite de antemano.

> **⚠️ Cuidado**
> - **«Muchos holders = seguro».** Los bundlers crean cientos de holders con una sola wallet. Mira quién los financió, no cuántos son.
> - **«El dev quemó/bloqueó los tokens».** Compruébalo tú mismo en la blockchain; un pool bloqueado no impide vender a las wallets sniper.
> - **Bots para copiar al «smart money».** Las wallets que parecen genios suelen ser los propios snipers, o el dev; para cuando las copias, ya están vendiendo.

## Qué puede aprender un principiante

En un lanzamiento normalmente no llegas pronto: los que llegan pronto son los bots. Casi 7 de cada 10 tokens de pump.fun dejaron de cotizar el primer día, así que la opción más segura suele ser no jugar. Si juegas, trátalo como dinero que puedes perder por completo. Las compras regulares funcionan con activos que sobreviven años; como comparación, la moneda propia de Solana, SOL, cotiza ahora a {{price:sol}} ({{chg1y:sol}} en 12 meses): son resultados pasados, no una previsión.

Lección anterior: [cómo funciona Binance Alpha]({lang}/blog/how-binance-alpha-works/). Próxima lección: por qué la mayoría de los compradores de memecoins pierden dinero. Todas las lecciones están en la [página Aprender]({lang}/learn/).

## Fuentes

- [Pine Analytics: Exit Liquidity Machines — análisis del farming en pump.fun (21 de abril de 2025)](https://pineanalytics.substack.com/p/exit-liquidity-machines)
- [BeInCrypto: los snipers de memecoins en Pump.fun son un problema sistemático (22 de abril de 2025)](https://beincrypto.com/pump-fun-meme-coin-snipers-systematic-problem)
- [Documentación de Mobula: cómo detectar snipers y bundlers](https://docs.mobula.io/almanac/detecting-snipers-bundlers)
- [KuCoin News / datos de CoinGecko: casi el 70% de los tokens de pump.fun desaparecen el día del lanzamiento (25 de junio de 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)

*No es asesoramiento de inversión.*
