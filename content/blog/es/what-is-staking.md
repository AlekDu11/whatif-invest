---
title: Qué es el staking de criptomonedas y si es seguro
description: Staking de criptomonedas explicado fácil: cómo funciona, periodos de bloqueo, staking en exchange vs on-chain y los riesgos reales antes de hacer staking.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
El **staking** consiste en bloquear criptomonedas para ayudar a que una blockchain funcione y recibir monedas nuevas como recompensa. Se suele comparar con una cuenta de ahorro, pero funciona de forma muy distinta y tiene sus propios riesgos.

Esta guía explica cómo funciona el staking, qué significa el "bloqueo", en qué se diferencia hacer staking en un exchange de hacerlo on-chain y qué puede salir mal.

## Cómo funciona el staking

Muchas blockchains modernas (Ethereum, Solana, Cardano, Polkadot, Cosmos y otras) usan un sistema llamado **prueba de participación** (*proof of stake*). En lugar de gastar electricidad para proteger la red (como la minería de Bitcoin), dependen de **validadores**: ordenadores que verifican transacciones y añaden bloques nuevos.

Para ser validador hay que poner monedas en juego como garantía de buen comportamiento. Paso a paso:

1. Bloqueas (haces staking de) monedas en la red, ya sea con tu propio validador o delegándolas en uno.
2. Los validadores confirman transacciones y producen bloques.
3. La red paga recompensas en monedas nuevas, más una parte de las comisiones.
4. Si un validador hace trampa o se desconecta de forma grave, se le puede recortar parte de lo depositado. Esto se llama **slashing**.

Bitcoin en sí no se puede usar para staking de esta manera: usa prueba de trabajo. Los productos que ofrecen "rendimiento en Bitcoin" suelen ser préstamos u otros esquemas, no staking.

## De dónde salen las recompensas del staking

Las recompensas no son dinero gratis. Vienen sobre todo de:

- **Monedas nuevas** creadas por la red (inflación de la oferta),
- **Comisiones** que pagan los usuarios.

Esto importa: si una red crea monedas nuevas a, por ejemplo, un 5% al año y tú ganas un 5%, en gran parte solo mantienes tu porcentaje de la red, no te haces más rico. Además, las recompensas se pagan en la propia moneda: si su precio cae, el valor total puede bajar con fuerza.

Las tasas de recompensa cambian todo el tiempo según el número de participantes y las reglas de la red. Toma cualquier porcentaje anunciado como una foto del momento, no como una promesa.

## Bloqueo y desvinculación: cuándo recuperas tus monedas

Con el staking, tus monedas no suelen estar disponibles al instante. Cada red tiene sus reglas:

- **Ethereum**: los retiros son posibles desde la actualización "Shapella" de 2023, pero salir implica una cola que puede durar de días a semanas cuando mucha gente sale a la vez.
- **Solana**: retirar el staking se hace efectivo al final de una "época" (*epoch*), normalmente un par de días.
- **Cosmos y Polkadot**: periodos de "desvinculación" (*unbonding*) de varias semanas, durante los cuales las monedas no generan nada y no se pueden vender.
- **Cardano**: las monedas siguen en tu wallet y no se bloquean en absoluto.

Por qué importa: si el mercado cae durante la desvinculación, no puedes vender. Comprueba siempre las reglas actuales de la moneda antes de hacer staking.

## Staking en un exchange vs staking on-chain

Hay dos formas principales de hacer staking para la gente común.

### Staking en un exchange (custodiado)

Pulsas "Stake" o "Earn" en la app de un exchange y él hace el trabajo técnico.

- ✅ Muy fácil, sirve con cantidades pequeñas, sin configurar wallets.
- ❌ El exchange guarda tus monedas. Si quiebra, lo hackean o congela los retiros, tus monedas están en riesgo.
- ❌ El exchange se queda una parte de las recompensas como comisión.
- ❌ Algunos productos "earn" en realidad son préstamos, no staking: un riesgo muy distinto.

Los reguladores han vigilado de cerca estos servicios. En 2023 la SEC de EE. UU. acusó a Kraken por su programa de staking; Kraken pagó 30 millones de dólares y cerró el servicio para clientes estadounidenses. En 2025, el personal de la SEC indicó que algunas formas de "staking de protocolo" directo no son operaciones con valores. Las normas varían según el país y siguen cambiando.

### Staking on-chain (sin custodia)

Guardas las monedas en tu propia wallet y las delegas en un validador, o ejecutas tu propio validador.

- ✅ Tú controlas tus claves; nadie puede congelar tu cuenta.
- ✅ Normalmente comisiones más bajas.
- ❌ Más técnico: direcciones erróneas, phishing y malos validadores son problema tuyo.
- ❌ Para tener tu propio validador de Ethereum necesitas 32 ETH y un equipo fiable.

### Staking líquido

Una opción intermedia: haces staking a través de un protocolo y recibes un token que representa tus monedas en staking (por ejemplo, un token de "ETH en staking"). Puedes negociarlo mientras tus monedas generan recompensas. A cambio, asumes un **riesgo de contrato inteligente** adicional y la posibilidad de que el token cotice por debajo del valor de las monedas que lo respaldan.

## Los principales riesgos del staking

¿Es seguro el staking? Es menos arriesgado que muchos productos cripto de "alto rendimiento", pero nunca está libre de riesgo:

1. **Riesgo de precio.** El más importante. Una recompensa de unos pocos puntos porcentuales sirve de poco si la moneda cae un 50%. Mira lo volátiles que son en la [página de Ethereum]({lang}/eth/) o la [página de Solana]({lang}/sol/).
2. **Riesgo de bloqueo.** Puede que no puedas vender durante un desplome.
3. **Riesgo de plataforma.** Los exchanges y las plataformas de préstamos pueden quebrar. Cuando Celsius colapsó en 2022, los usuarios de su programa "earn" perdieron el acceso a sus monedas.
4. **Slashing.** Un validador que se porta mal puede perder parte de lo depositado, incluidas las monedas delegadas en algunas redes.
5. **Riesgo de contratos inteligentes** en el staking líquido y en DeFi.
6. **Impuestos.** En muchos países las recompensas del staking tributan como ingreso al recibirlas. Consulta las normas locales.
7. **Estafas.** Son habituales las webs de staking falsas y las ofertas de "20% al mes garantizado". Lee nuestra guía para [evitar estafas cripto]({lang}/blog/how-to-avoid-crypto-scams/).

## Lista de comprobación antes de hacer staking

- Haz staking solo de monedas que ya pensabas mantener mucho tiempo.
- Revisa el periodo de desvinculación y si podrías necesitar el dinero antes.
- Ten claro quién guarda tus monedas: tú o una plataforma.
- Compara comisiones: ¿qué parte de las recompensas se queda la plataforma?
- Evita ofertas con rentabilidades fijas muy altas: las recompensas reales del staking varían.
- Empieza con poco y prueba un retiro.

El staking no cambia la pregunta principal: ¿encaja la moneda en tu plan a largo plazo? Un plan de compras periódicas, como el que puedes simular en nuestra [calculadora DCA]({lang}/compare/), depende del precio del activo a lo largo de los años. Así le habría ido a quien invirtiera 10 $ al día en Ethereum durante 5 años, sin ninguna recompensa de staking: {{dca:eth:5}} a partir de {{dcainv:5}} invertidos ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## Preguntas frecuentes

### ¿El staking es lo mismo que cobrar intereses?

No. Los intereses los paga alguien que pide prestado; las recompensas del staking las paga la propia red por ayudar a protegerla. Se pagan en la moneda, así que su valor se mueve con su precio.

### ¿Se puede perder dinero con el staking?

Sí. El precio de la moneda puede caer, una plataforma puede quebrar y, en casos raros, el slashing puede recortar lo depositado. Las recompensas no te protegen de una caída del precio.

### ¿Se puede hacer staking de Bitcoin?

No de forma nativa: Bitcoin usa prueba de trabajo. Las ofertas de "rendimiento en Bitcoin" suelen ser préstamos u otros productos con riesgos diferentes.

### ¿Qué es mejor, staking en un exchange o en una wallet?

El staking en un exchange es más sencillo; el staking desde una wallet te da el control de tus claves. La elección depende de lo cómodo que te sientas gestionando una wallet: consulta nuestra guía de [wallets calientes y frías]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Fuentes

- [ethereum.org — Staking en Ethereum](https://ethereum.org/en/staking/)
- [ethereum.org — Retiros del staking](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [SEC de EE. UU. — Kraken cerrará su programa de staking y pagará 30 millones de dólares (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: ciertas actividades de staking de protocolo no son operaciones con valores (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*No es asesoramiento de inversión. Esta guía explica cómo funciona el staking y no recomienda ninguna moneda, plataforma ni validador.*
