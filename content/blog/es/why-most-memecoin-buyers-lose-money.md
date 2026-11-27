---
title: "Por qué la mayoría de los compradores de memecoins pierden dinero: las cuentas de lanzamientos, slippage y comisiones"
description: Solo el 0,41% de las wallets de pump.fun ganó más de 10.000 $. Las cuentas sencillas de lanzamientos, slippage y comisiones que juegan en contra del comprador.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41%
stat_label: de 13,55 millones de wallets de pump.fun había realizado más de 10.000 $ de ganancia (datos de Dune, enero de 2025)
---
**¿Por qué la mayoría de quienes compran memecoins pierden dinero?** Porque las cuentas están en su contra antes de que el precio se mueva: la mayoría de los tokens nuevos mueren en menos de un día, cada compra y venta cuesta comisiones y slippage (deslizamiento del precio), y los primeros compradores (a menudo bots e insiders) les venden a los que llegan después. Para ganar, un token tiene que sobrevivir *y* subir lo suficiente como para cubrir todo eso.

> **Claves**
> - Datos de Dune publicados en enero de 2025 mostraron que solo alrededor del **0,41%** de 13,55 millones de wallets de pump.fun había realizado más de **10.000 $** de ganancia.
> - CoinGecko descubrió que el **68,67%** de los tokens de pump.fun hizo su última operación el mismo día del lanzamiento (datos de enero de 2024 a junio de 2026).
> - Cada ida y vuelta (compra + venta) en un token nuevo puede costar **2,5% o más** solo en comisiones de la plataforma, más las comisiones de red y el slippage.

## Parte 1 — Las cuentas de la supervivencia

La mayoría de las memecoins no son «baratas»: duran poco.

- **Muerte el día del lanzamiento.** CoinGecko contó 18,67 millones de tokens en pump.fun; el 68,67% hizo su última operación el mismo día en que salió (informe del 25 de junio de 2026).
- **Pocos llegan a un mercado de verdad.** «Graduarse» (graduation) significa que un token sale de la curva inicial de pump.fun y pasa a tener un pool de trading normal. Según datos de Dune, la tasa semanal de graduación se mantuvo por debajo del **1%** durante cuatro semanas desde el 17 de febrero de 2025; su mejor semana, en noviembre de 2024, fue del **1,67%**. En marzo de 2026 llegó al **2,01%**, el máximo desde julio de 2025.

Así que, si eliges lanzamientos nuevos al azar, lo normal es que acabes con monedas que dejan de cotizar. Unos pocos grandes ganadores no compensan muchas monedas que se van a cero, salvo que elijas muy bien, y el primer día nadie sabe cuáles sobrevivirán.

## Parte 2 — Comisiones: pagas al entrar y al salir

La página de ayuda de pump.fun (septiembre de 2025) indica una comisión del **1,25%** en cada operación antes de la graduación (0,95% para la plataforma y 0,30% para el creador). Después de graduarse, la comisión baja a medida que el token crece: del 1,25% en los más pequeños al 0,30% en los más grandes. A eso se suman las comisiones de red de Solana y las comisiones opcionales de «prioridad» y de protección MEV (0,003–0,03 SOL por operación, según su página).

**Ejemplo práctico (ilustración, no son precios reales):** compras 50 $ de un token nuevo y pagas una comisión de prioridad de 0,02 SOL en cada dirección. La comisión del 1,25% al entrar y al salir es de unos 1,25 $, y dos comisiones de prioridad pueden sumar varios dólares más. Solo para volver a tus 50 $, el token tendría que subir quizá un **5–10%**. Con operaciones de 10 $ es mucho peor: las comisiones fijas se comen una parte mucho mayor.

## Parte 3 — Slippage: el precio se mueve mientras compras

El **slippage** (deslizamiento) es la diferencia entre el precio que ves y el precio que realmente obtienes (consulta el [glosario de memecoins]({lang}/memes/glossary/)). Los tokens nuevos tienen pools diminutos, así que tu propia compra empuja el precio hacia arriba, y también las compras de todos los demás en el mismo segundo. Si pones un slippage del 10–20% (muchas apps lo recomiendan para monedas nuevas), aceptas pagar hasta ese porcentaje de más. Al vender pasa lo mismo, pero al revés: en un pool pequeño, tu venta hunde el precio.

## Parte 4 — Quién está al otro lado

Los primeros compradores suelen ser snipers, bundlers y la wallet del desarrollador (consulta [snipers, bundlers y wallets del desarrollador]({lang}/blog/snipers-bundlers-dev-wallets/)). Compran al precio más bajo y venden en la primera ola de demanda. Si compras después de la primera vela verde, muchas veces eres la «liquidez de salida» (exit liquidity): el dinero al que ellos venden.

## Paso a paso: haz las cuentas antes de pulsar «Comprar»

1. **Paso 1 — Suma las comisiones.** Mira la línea de comisión en la pantalla de swap y añade la comisión de red/prioridad. Multiplica por dos (compra + venta).
2. **Paso 2 — Revisa el slippage.** Mantenlo tan bajo como permita la operación (por ejemplo, 1–3% en una moneda con un pool grande). Si una moneda necesita un slippage del 20%, es una señal de alarma.
3. **Paso 3 — Mira el tamaño del pool.** En nuestra [página de memecoins]({lang}/memes/) abre el token y fíjate en la liquidez. Pool pequeño = mucho slippage en ambos sentidos.
4. **Paso 4 — Haz el control de seguridad.** Usa [cómo revisar una memecoin antes de comprar]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Paso 5 — Decide de antemano cuánto puedes perder.** Usa solo dinero que puedas perder por completo y fija la cantidad antes de empezar.

> **⚠️ Cuidado**
> - **«Solo vale 0,0001 $, puede multiplicarse por 1000».** Un precio bajo no significa nada: de muchos tokens hay miles de millones de unidades. Lo que importa es si el token sobrevive y quién te lo vende.
> - **Muchas operaciones pequeñas.** Las comisiones fijas de red y de prioridad pueden comerse más del 10% de una operación de 10 $ antes de que el precio se mueva.
> - **Capturas de ganadores.** Ves al 0,41% que ganó mucho, no a los millones que perdieron; los «gurús» a menudo venden las monedas que promocionan.

## Qué significa si compras con regularidad

Las compras pequeñas y regulares funcionan con activos que siguen existiendo años después, no con tokens que pueden dejar de cotizar esta misma noche. Si quieres cripto, el camino habitual para un principiante es una moneda grande y líquida comprada poco a poco; como comparación, SOL, la moneda propia de Solana, está ahora en {{price:sol}} ({{chg1y:sol}} en 12 meses): resultados pasados, no una previsión. Puedes probar «10 $ al día» con cualquier activo en nuestra calculadora y seguirlo en tu [página de cartera]({lang}/me/).

Lección anterior: [snipers, bundlers y wallets del desarrollador]({lang}/blog/snipers-bundlers-dev-wallets/). Todas las lecciones están en la [página Aprender]({lang}/learn/).

## Fuentes

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11 de enero de 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14 de marzo de 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, datos de Dune: pump.fun graduation rate hits 2.01% (17 de marzo de 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / datos de CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25 de junio de 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [Centro de ayuda de pump.fun: Transaction fees on pump.fun (septiembre de 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*No es asesoramiento de inversión.*
