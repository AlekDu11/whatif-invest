---
title: Bitcoin Core corrige un fallo hallado por IA que congelaba nodos: versiones 30.5 y 31.3
description: Bitcoin Core 30.5 y 31.3 corrigen un fallo de gravedad media, hallado por un escáner de IA de Spiral (Block), que dejaba a un par congelar un nodo más de 10 s.
date: 2026-11-21 14:30
tags: bitcoin, hacks, ai
assets: btc
---
El software principal de bitcoin recibió un parche para un fallo que una herramienta de IA encontró primero. Las versiones 30.5 y 31.3 de Bitcoin Core, publicadas el viernes 20 de noviembre, cierran un error que permitía a un solo par dejar un nodo sin funcionar más de diez segundos por mensaje.

## Qué pasó

- **El fallo.** Registrado como CVE-2026-117348 y de gravedad media. Un par podía repetir un mismo identificador de transacción hasta 50.000 veces en un anuncio; el nodo revisaba cada copia y se bloqueaba, ignorando incluso los bloques nuevos.
- **Quién lo halló.** Lo detectó Loupe, un escáner de código abierto del equipo Spiral de Block que usa agentes de IA; el aviso lo atribuye a un escaneo automático con IA dentro del Project Loupe de Elias Rohrer.
- **La solución.** Los nodos parcheados procesan cada transacción anunciada una sola vez. La rama retirada 29.x no recibirá arreglo, según The Defiant.
- **Riesgo.** No hubo fondos ni monedas en peligro. CoinDesk señala que el daño realista eran retrasos: un exchange más lento al acreditar depósitos o un minero trabajando un momento sobre una cadena desfasada.

## Nuestra lectura

No es la causa de la caída del sábado: bitcoin bajó con las bolsas y las liquidaciones apalancadas. Pero muestra que la IA ya encuentra fallos en el código cripto central, tanto para atacantes como para defensores. Si tienes un nodo, actualiza a 30.5 o 31.3. Si solo tienes bitcoin, nada cambia. Bitcoin cotiza a {{price:btc}}, más de un 50% por debajo de su récord — ver la [página de distancia al máximo]({lang}/ath/) y nuestra [página de IA y mercados]({lang}/ai/). $10 al día durante 5 años ({{dcainv:5}}) valen hoy {{dca:btc:5}} ({{dcaroi:btc:5}}). Es historia, no una previsión.

## Fuentes

- [CoinDesk — Los nodos de bitcoin podían bloquearse repitiendo un ID 50.000 veces](https://www.coindesk.com/markets/2026/11/21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug)
- [The Defiant — Bitcoin Core corrige un fallo hallado por IA](https://thedefiant.io/news/security/bitcoin-core-fixes-ai-found-bug-that-could-stall-nodes)
- [Coinotag — Bitcoin Core corrige el fallo en 30.5 y 31.3](https://en.coinotag.com/bitcoin-core-fixes-node-stall-cve-2026-117348)

*No es asesoramiento de inversión.*
