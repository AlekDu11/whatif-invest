---
title: Cómo retirar cripto de un exchange a tu propio monedero: paso a paso
description: Pasa tus monedas del exchange a tu monedero sin riesgos: copia la dirección correcta, elige la misma red, añade el memo si hace falta y haz una prueba.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 red
stat_label: el exchange y el monedero deben usar la misma, o las monedas pueden perderse
---
**¿Cómo se retira cripto a tu propio monedero?** En tu monedero copias tu **dirección de recepción** para esa moneda. Luego, en el exchange, abres **Withdraw** (Retirar), pegas esa dirección, eliges **la misma red** que usa tu monedero, pones una cantidad pequeña de prueba y confirmas con 2FA. Cuando llega la prueba, envías el resto.

> **Claves**
> - Tres cosas tienen que coincidir: la **moneda**, la **dirección** y la **red** (la blockchain por la que viajan las monedas, por ejemplo Ethereum, BNB Smart Chain, TRON o Solana). Binance avisa de que las monedas enviadas por la red equivocada pueden perderse para siempre.
> - Algunas monedas (como XRP, XLM o ATOM) también necesitan un **memo** o **tag** (un número corto que le dice al receptor de quién son las monedas). Sin él, la transferencia puede quedarse atascada o llegar a otra persona.
> - **Haz siempre primero una prueba pequeña.** Un retiro no se puede cancelar una vez que las monedas han salido del exchange.

Esta lección continúa [Cómo programar una compra recurrente]({lang}/blog/how-to-set-up-a-recurring-buy/). Por qué te puede interesar tener tu propio monedero se explica en [monederos calientes y fríos]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Antes de empezar

Necesitas dos cosas. Una cuenta de exchange con monedas, protegida con 2FA: mira [Cómo registrarse en un exchange de criptomonedas]({lang}/blog/how-to-register-on-a-crypto-exchange/). Y tu propia app de monedero ya configurada, con su **frase semilla** (las 12 o 24 palabras secretas que recuperan el monedero) apuntada en papel y guardada sin conexión. No escribas nunca la frase semilla en ningún otro sitio: ningún exchange, web ni persona de "soporte" la necesitará jamás.

## Paso 1 — Copia la dirección de recepción de tu monedero

1. Abre la app de tu monedero y pulsa **Receive** (Recibir; a veces **Deposit**).
2. Elige la moneda, por ejemplo Bitcoin o USDT.
3. Si el monedero te lo pide, elige la red. Apunta cuál es, por ejemplo "USDT en TRON (TRC20)" o "USDT en Ethereum (ERC20)".
4. Pulsa **Copy** (Copiar) junto a la dirección. No la escribas a mano.

Una dirección es una línea larga de letras y números. Las direcciones de Bitcoin suelen empezar por **bc1**, las de Ethereum y BNB Smart Chain por **0x** y las de TRON por **T**.

## Paso 2 — Abre Withdraw en el exchange

En la app de Binance está en **Assets → Spot → Send → Withdraw Crypto**; en la web, en **Wallet → Overview → Withdraw**. Otros exchanges tienen un botón **Withdraw** junto a cada moneda en la pantalla de monedero o cartera. Elige la misma moneda que en el paso 1.

## Paso 3 — Pega la dirección y elige la red

1. Pega la dirección en el campo **Address** (Dirección).
2. Compara los **4 primeros y los 4 últimos caracteres** con tu monedero. Hay malware que cambia la dirección copiada por la del ladrón.
3. Elige la **red**. Tiene que ser la que te mostró el monedero en el paso 1. Binance puede proponerte una red automáticamente: compruébala igualmente. No elijas una red solo porque su comisión es la más baja.
4. Si aparece un campo **Memo** o **Tag** y tu monedero te dio uno, rellénalo. Si tu monedero no muestra ningún memo, normalmente no lo necesita, pero confírmalo en las páginas de ayuda del monedero.

Consejo: si no estás seguro, guarda la dirección en **Address Management** (la libreta de direcciones) del exchange. Binance también tiene una **lista blanca** (whitelist): cuando la activas, solo se puede retirar a direcciones guardadas, lo que te protege si alguien te roba la contraseña.

## Paso 4 — Envía una prueba pequeña

1. Pon una cantidad pequeña, un poco por encima del retiro mínimo que muestra la pantalla.
2. Mira las líneas de **comisión de red** y **recibirás**. La comisión es fija por cada retiro, así que en una cantidad muy pequeña puede ser una parte grande.
3. Pulsa **Withdraw** y confirma con tu código 2FA o tu passkey. Algunos exchanges también envían un correo de confirmación: ábrelo y pulsa **Confirm**.

## Paso 5 — Comprueba que ha llegado y envía el resto

1. Espera. Una transferencia puede tardar desde unos segundos hasta una hora, según la red y el tráfico.
2. En el exchange, abre el historial de retiros para ver el estado y el **TxID** (el identificador de la transacción, que puedes buscar en un explorador de bloques).
3. Cuando las monedas aparezcan en tu monedero, repite los pasos 2 a 4 con el resto. La dirección ya está en el historial o en la libreta, así que la segunda vez es más rápido.

Añade las monedas a [tu cartera]({lang}/me/) para seguir su valor en un solo lugar, estén donde estén guardadas.

> **⚠️ Cuidado**
> - **Red equivocada.** USDT existe en muchas redes. Enviar USDT "TRC20" a una dirección que solo espera "ERC20" puede hacer que las monedas se pierdan. Revisa la red dos veces.
> - **Falta el memo o el tag.** Los exchanges y monederos que necesitan memo no saben de quién son las monedas que llegan sin él. Recuperarlas, si es posible, es lento y cuesta una comisión.
> - **Falso soporte y webs de "verificación de dirección".** Nadie legítimo te pide la frase semilla ni que "verifiques" un monedero enviando monedas. Retira solo desde la app o la web oficial.

## Qué significa si compras de forma periódica

Si compras un poco cada semana o cada mes, no hace falta retirar después de cada compra: cada retiro tiene una comisión. Mucha gente deja que las monedas se acumulen en el exchange y de vez en cuando las pasa a su monedero, por ejemplo una vez al trimestre, en una sola transferencia más grande. Un ejemplo de nuestra calculadora: $10 al día en bitcoin durante 3 años ({{dcainv:3}} en total) se convirtieron en {{dca:btc:3}} ({{dcaroi:btc:3}}). Son resultados pasados, no una previsión. Ahora mismo bitcoin cotiza a {{price:btc}}; mira la [página de Bitcoin]({lang}/btc/).

Lección anterior: [Cómo programar una compra recurrente]({lang}/blog/how-to-set-up-a-recurring-buy/). Próxima lección: cómo vender cripto y recibir el dinero en tu cuenta bancaria. Compara exchanges en nuestra [página de exchanges]({lang}/exchanges/); todas las lecciones están en la [página Aprender]({lang}/learn/).

## Fuentes

- [Binance Support: cómo depositar y retirar criptomonedas en Binance (actualizado en marzo de 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: cómo recuperar un depósito con un tag o memo erróneo o ausente](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: cómo retirar cripto de tu cuenta de Binance.US (junio de 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*No es asesoramiento de inversión.*
