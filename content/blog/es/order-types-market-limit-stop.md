---
title: "Tipos de órdenes: a mercado, limitada y stop, explicadas paso a paso"
description: Qué hacen los botones Market, Limit y Stop en la app de un exchange o bróker, con un ejemplo con números y los 3 errores que cuestan dinero.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: tipos básicos de orden: a mercado (rápida, precio no fijo), limitada (precio fijo, ejecución no segura), stop (se activa a un precio)
---
**¿Qué tipos de órdenes hay?** Una **orden a mercado** (Market) compra o vende ahora mismo al mejor precio disponible. Una **orden limitada** (Limit) compra o vende solo a tu precio o a uno mejor, así que puede no ejecutarse nunca. Una **orden stop** (Stop) espera a que el precio llegue al nivel que eliges y entonces envía una orden a mercado; se usa a menudo para limitar una pérdida.

> **Lo esencial**
> - Market = rapidez, pero no controlas el precio exacto. Limit = control del precio, pero sin garantía de que se ejecute.
> - Una orden stop se convierte en orden a mercado cuando se activa. En una caída rápida puede ejecutarse muy por debajo de tu precio stop.
> - Antes de pulsar «Comprar», revisa siempre tres cosas: tipo de orden, cantidad y precio.

## Los tres botones, en palabras sencillas

Cuando abres la pantalla de operar en la app de un exchange o bróker, normalmente ves pestañas: **Market** (a mercado), **Limit** (limitada) y **Stop** (a veces «Stop-limit», stop limitada).

- **Orden a mercado (Market).** «Compra ya, al precio que sea». Se ejecuta casi al instante con la mejor oferta (el **ask**, el precio más bajo al que alguien quiere vender). En criptos grandes y acciones grandes el precio suele estar muy cerca del que ves. En mercados pequeños y poco líquidos puede ser bastante peor.
- **Orden limitada (Limit).** «Compra solo a X $ o más barato» (o «vende solo a X $ o más caro»). Tu orden espera en el **libro de órdenes** (order book, la lista de todas las órdenes de compra y venta pendientes) hasta que alguien acepte tu precio. Si el precio nunca llega ahí, no pasa nada.
- **Orden stop (Stop, stop-loss).** «Si el precio baja a X $, vende». Hasta entonces es invisible y no hace nada. Cuando el precio toca X $, se convierte en orden a mercado y vende al siguiente precio disponible.
- **Orden stop limitada (Stop-limit).** Como un stop, pero se convierte en orden *limitada*. No venderás por debajo de tu límite, pero en una caída rápida puede que no vendas nada.

## Un ejemplo con números sencillos

Imagina que una acción marca **100,00 $**. El mejor comprador ofrece 99,95 $ (el **bid**) y el mejor vendedor pide 100,05 $ (el ask). La diferencia de 0,10 $ es el **spread** (horquilla).

1. Pulsas **Market, comprar 10 acciones** → pagas unos 100,05 $ cada una = **1.000,50 $** más la comisión, si la hay.
2. Pones **Limit, comprar 10 acciones a 98 $** → no pasa nada hasta que un vendedor acepte 98 $. Si el precio sube a 105 $, tu orden simplemente espera y no compras nada.
3. Ya tienes las acciones y pones un **Stop a 90 $** → si el precio baja a 90 $, se envía una venta a mercado. En un mercado tranquilo quizá obtengas 89,95 $. Pero si salen malas noticias antes de la apertura y la acción abre a 80 $, tu stop se activa y vendes cerca de **80 $**, no de 90 $.

Ese tercer caso es real. El 6 de mayo de 2010 (el «flash crash»), los precios en EE. UU. se hundieron en minutos y algunas órdenes stop se ejecutaron muy por debajo de su nivel stop; unas pocas acciones llegaron a negociarse a un centavo, según el informe de la SEC y la CFTC.

## Paso a paso: coloca tu primera orden limitada con seguridad

Practica primero con una cantidad muy pequeña.

1. **Paso 1 — Abre la pantalla de operar** de la cripto o la acción y elige **Comprar** (Buy).
2. **Paso 2 — Pulsa la pestaña «Limit»**, no «Market».
3. **Paso 3 — Escribe tu precio.** Mira primero el precio actual (por ejemplo, bitcoin está ahora a {{price:btc}}). Un límite muy por debajo puede no ejecutarse nunca.
4. **Paso 4 — Escribe la cantidad.** Comprueba si la casilla se refiere a monedas/acciones o a dinero (USD, EUR). Es el error más común.
5. **Paso 5 — Revisa el resumen**: tipo, precio, cantidad, total y comisión. Después confirma.
6. **Paso 6 — Busca tu orden** en «Órdenes abiertas» (Open orders). Ahí puedes cancelarla cuando quieras mientras no se ejecute. Cuando se ejecuta, pasa al «Historial de órdenes» (Order history).

> **⚠️ Cuidado**
> - **Órdenes a mercado en mercados poco líquidos.** En criptos pequeñas o fuera del horario normal, una orden a mercado puede ejecutarse bastante peor que el precio de la pantalla (esto se llama **deslizamiento**, slippage). Ahí usa una orden limitada.
> - **Creer que un stop-loss garantiza tu precio.** No lo hace: garantiza la venta, no el precio. Los gaps y los desplomes pueden llevar la ejecución mucho más abajo. Un stop limitado protege el precio, pero puede no vender.
> - **Confundir los campos.** El lado equivocado (Vender en vez de Comprar), un cero de más en la cantidad o un precio en la casilla equivocada. Lee el resumen antes de confirmar.

## Qué significa si compras con regularidad

Si simplemente compras un poco cada semana o cada mes, no necesitas órdenes complicadas. Una orden a mercado en un activo grande y líquido suele bastar, o una orden limitada un poco por encima del precio actual si quieres poner un tope. El resultado real viene del tiempo en el mercado: 10 $ al día en bitcoin durante 3 años valdrían ahora {{dca:btc:3}} (habrías puesto {{dcainv:3}}): resultados pasados, no una previsión.

Lo siguiente en WhatIfStack: mira cómo el libro de órdenes y los grandes traders mueven el mercado en la [sección de Trading]({lang}/trading/) y en el [rastreador de ballenas de Hyperliquid]({lang}/trading/hyperliquid/), compara comisiones en [exchanges]({lang}/exchanges/) y encuentra todas las lecciones en la [página Aprender]({lang}/learn/).

## Fuentes

- [Investor.gov (SEC): Tipos de órdenes](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Boletín para inversores — órdenes stop, stop limitada y trailing stop](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Tipos de órdenes](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC y SEC: Informe sobre los hechos del mercado del 6 de mayo de 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*No es asesoramiento de inversión.*
