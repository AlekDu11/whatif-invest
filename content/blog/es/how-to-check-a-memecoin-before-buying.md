---
title: Cómo revisar una memecoin antes de comprar: 6 controles en 5 minutos
description: Antes de comprar una memecoin, revisa el contrato, la liquidez, los holders, el peso del top 10, la antigüedad y la auditoría de Binance. Checklist sencillo.
date: 2026-11-23T16:30:00Z
category: learn
track: memes
step: 6
assets: sol, bnb, doge
stat: 6
stat_label: controles antes de comprar cualquier memecoin
---
**¿Cómo se revisa una memecoin antes de comprar?** Busca el token por su dirección de contrato y revisa seis cosas: la auditoría de seguridad, la liquidez, el número de holders, cuánto tienen las 10 wallets más grandes, su antigüedad y si el creador todavía puede cambiarlo. Si un control sale en rojo, olvídate de esa moneda. Hay miles más.

> **Claves**
> - Estos controles no hacen segura una memecoin. Solo te ayudan a evitar las trampas más obvias: tokens que no puedes vender, copias falsas y monedas que unas pocas wallets pueden hundir.
> - La pestaña **Audit** (auditoría) de Binance Wallet revisa riesgos del contrato, de trading y de estafa (por ejemplo, un «honeypot»: un token que puedes comprar pero nunca vender). La propia Binance dice que la auditoría no es infalible.
> - En nuestra [página de memecoins]({lang}/memes/) el filtro de calidad viene activado: «Solo calidad: liquidez $100K+, 1 día+».

Esta lección continúa [Cómo conectar Binance Wallet a un DEX]({lang}/blog/connect-binance-wallet-to-dex/). Las memecoins son extremadamente arriesgadas: usa solo dinero que puedas permitirte perder.

## Paso 1 — Consigue la dirección de contrato correcta

Cada token tiene una **dirección de contrato** (su identificador único en la blockchain: una cadena larga de letras y números). Cualquiera puede crear un token con el mismo nombre y logo, así que el nombre no significa nada.

1. Copia la dirección de la cuenta oficial del proyecto o de una web de datos fiable.
2. Pégala en el buscador de tu wallet. Compara los 4 primeros y los 4 últimos caracteres.
3. Si ves varios tokens con el mismo nombre, los demás son copias.

## Paso 2 — Abre la auditoría de seguridad

En la app de Binance abre el token en **Wallet** y pulsa la pestaña **Audit** (en la web: haz clic en el token y luego en **Audit**). En las páginas de tokens de nuestra sección de memecoins ves el mismo control como **Control de seguridad de Binance: Riesgo bajo / Riesgo medio / Riesgo alto**.

Mira tres grupos:

- **Contract risk** (riesgo del contrato): ¿puede el creador bloquear las ventas, meter wallets en una lista negra, cambiar el impuesto o cambiar saldos?
- **Trading risk** (riesgo de trading): riesgo de honeypot, impuesto raro al comprar o vender (una comisión que se cobra en cada operación), poca liquidez, riesgo de rug pull.
- **Scam risk** (riesgo de estafa): token falso, estafa conocida, spam.

Cualquier punto en rojo = no compres. «Riesgo bajo» tampoco significa seguro: el creador aún puede hacer cosas después de que compres.

## Paso 3 — Revisa la liquidez

La liquidez es el dinero del pool de trading que te permite vender. Si es muy poca, hasta una venta pequeña hunde mucho el precio, y el creador puede retirarla (un rug pull, «tirar de la alfombra»). En WhatIfStack, nuestro filtro por defecto oculta los tokens con menos de $100K de liquidez. Si la web de datos lo muestra, revisa también si la liquidez del pool está bloqueada o quemada (eliminada para siempre).

## Paso 4 — Cuenta los holders y el peso del top 10

En la página del token mira **Holders** (cuántas wallets lo tienen) y **Top 10 tienen** (qué parte de todas las monedas tienen las 10 wallets más grandes). Unos cientos de holders y un top 10 con mucho peso significan que un puñado de personas puede vender y hundir el precio. Ojo: las direcciones del pool y de quema también salen en el top 10, y eso es normal.

## Paso 5 — Revisa la antigüedad

La mayoría de los tokens estafa viven horas o días. Un token con menos de un día no tiene ningún historial. Nuestro filtro en /memes/ solo muestra tokens con al menos 1 día. Más antiguo no es seguro: solo es menos desconocido.

## Paso 6 — En Solana: ¿puede el creador seguir cambiando el token?

En Solana importan dos ajustes:

- **Mint authority** (permiso de emisión): el derecho a crear tokens nuevos. Si sigue activo, el creador puede imprimir más y tu parte se reduce.
- **Freeze authority** (permiso de congelación): el derecho a congelar una wallet. Si sigue activo, el creador podría impedir que muevas o vendas.

Lo más seguro es que aparezcan como «revoked» o «disabled» (nadie los tiene). Puedes ver ambos en la página del token en un explorador de bloques como Solscan.

> **⚠️ Cuidado**
> - **Una copia falsa con el mismo nombre.** Compra siempre por dirección de contrato, nunca por nombre o logo.
> - **Un honeypot.** Puedes comprar, el gráfico sube, pero nadie puede vender. Un historial con compras y sin ventas es una señal de alarma.
> - **Fiarse de una sola luz verde.** Una auditoría, muchos holders o un nombre famoso no te protegen si el precio simplemente cae: la mayoría de las memecoins acaban cerca de cero.

## Qué significa si compras de forma regular

Las compras pequeñas y regulares funcionan mejor con activos que probablemente sigan existiendo dentro de cinco años. La mayoría de las memecoins no cumplen eso. Si aun así quieres probar una, que sea con una cantidad diminuta y fija, y síguela junto al resto de tu dinero en [tu cartera]({lang}/me/).

Próxima lección: la historia de Dogecoin. Todas las lecciones están en la sección [Aprender]({lang}/learn/).

## Fuentes

- [Binance: How to Use the Token Audit Feature in Binance Wallet](https://www.binance.com/en/support/faq/detail/fd1b21bac5114feda49dd185461afdda)
- [Binance.US: What is a honeypot scam?](https://support.binance.us/en/articles/15388146-what-is-a-honeypot-scam)
- [Solana docs: Set authority (mint and freeze authority)](https://solana.com/docs/tokens/basics/set-authority)
- [Solana docs: Freeze account](https://solana.com/docs/tokens/basics/freeze-account)

*No es asesoramiento de inversión. Esta guía explica cómo revisar un token y no recomienda comprar ninguna moneda.*
