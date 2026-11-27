---
title: "Autenticación en dos pasos (2FA): cómo activarla paso a paso"
description: La 2FA añade un segundo cerrojo a tu cuenta del exchange. Cómo activar una app de autenticación o una passkey paso a paso y por qué el SMS es lo más débil.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 M$
stat_label: perdidos por fraudes de SIM swap en 2021, en 1.611 denuncias al FBI (IC3, febrero de 2022)
---
**¿Qué es la 2FA y cómo se activa?** La autenticación en dos pasos o de dos factores (2FA) significa que para iniciar sesión o retirar fondos necesitas dos cosas: tu contraseña *y* una segunda prueba, como un código de 6 dígitos de una app en tu móvil o una passkey (llave de acceso: tu huella o tu cara). Actívala en los ajustes de **Security** (Seguridad) de tu exchange y usa una app de autenticación o una passkey en lugar de SMS.

> **Claves**
> - Con la 2FA, una contraseña robada no basta para vaciar tu cuenta.
> - **Los códigos por SMS son la opción más débil:** en un «SIM swap» (duplicado fraudulento de la SIM), un delincuente pasa tu número de teléfono a su tarjeta SIM y recibe tus códigos. El FBI registró 1.611 denuncias de este tipo y más de **68 millones de dólares** en pérdidas en 2021, frente a 320 denuncias y unos 12 millones en 2018–2020.
> - El FBI recomienda opciones más fuertes: una app de autenticación, la biometría o una llave de seguridad física.

## Las opciones, de la más débil a la más fuerte

- **Código por SMS** — un mensaje de texto con un código. Mejor que nada, pero te pueden robar el número de teléfono.
- **Código por e-mail** — es tan seguro como tu cuenta de correo (protégela también con 2FA).
- **App de autenticación** (Google Authenticator, Microsoft Authenticator y similares) — la app del móvil genera un código nuevo de 6 dígitos cada 30 segundos, incluso sin conexión. Nadie puede interceptarlo a través de tu operadora.
- **Passkey** (biometría) — confirmas con tu huella, tu cara o el PIN del móvil. Solo funciona en la web real, así que una web falsa no puede robártela.
- **Llave de seguridad física** (un pequeño dispositivo USB/NFC) — la más fuerte, buena para cantidades grandes.

## Paso a paso: app de autenticación (con la app de Binance como ejemplo)

Otros exchanges usan casi los mismos pasos; busca **Security** (Seguridad) en tu perfil.

1. **Paso 1 — Instala la app.** Descarga Google Authenticator (u otra app de autenticación) desde la App Store o Google Play oficiales.
2. **Paso 2 — Abre los ajustes de seguridad.** En la app de Binance toca el icono **Account** (Cuenta), toca tu perfil arriba y luego **Security** (Seguridad).
3. **Paso 3 — Empieza la configuración.** Toca **Authenticator App** (App de autenticación) y luego **Enable** (Activar). Verás un código QR y una **clave de configuración** (setup key, un código largo).
4. **Paso 4 — Apunta la clave de configuración en papel.** Es tu copia de seguridad si pierdes el móvil. Guárdala sin conexión, como una frase semilla. Todavía no toques **Next** (Siguiente).
5. **Paso 5 — Añade la cuenta en la app de autenticación.** En Google Authenticator toca **+**, elige **Enter a setup key** (Introducir una clave de configuración) o escanea el código QR, pega la clave, escribe un nombre como «Binance» y toca **Add** (Añadir).
6. **Paso 6 — Confirma.** Vuelve a Binance, toca **Next** (Siguiente) y escribe el código de 6 dígitos de la app. Verás un mensaje de que todo ha ido bien.
7. **Paso 7 — Pruébala.** Cierra sesión y vuelve a entrar. Si te pide el código, funciona.

## Paso a paso: passkey (aún más fácil)

La página de ayuda de Binance indica que necesitas la versión 2.60 o superior de la app, iOS 16+ o Android 9+.

1. **Account → perfil → Security → Passkeys (Biometrics) → Add Passkey** (Cuenta → perfil → Seguridad → Passkeys (biometría) → Añadir passkey).
2. Si te lo pide, confirma con tu 2FA actual y toca **Continue** (Continuar).
3. Elige dónde guardarla: Llavero de iCloud (iPhone), Gestor de contraseñas de Google (Android) o una llave de seguridad, y confirma con tu huella, tu cara o tu PIN.

## Cuando ya tengas la 2FA activada

- Desactiva el SMS como método de inicio de sesión si el exchange lo permite o, al menos, pide a tu operadora un bloqueo contra duplicados de SIM y portabilidades sin tu autorización.
- Protege también con 2FA el e-mail vinculado al exchange.
- Activa una **lista blanca de retiros** (withdrawal whitelist: solo las direcciones guardadas pueden recibir fondos) si tu exchange la ofrece.

> **⚠️ Cuidado**
> - **Nadie de verdad te pedirá tu código 2FA.** El «soporte» en Telegram o una llamada «del exchange» o «del banco» pidiendo el código de 6 dígitos es siempre una estafa.
> - **Perder el móvil sin la clave de respaldo.** La recuperación lleva entonces días de verificación de identidad. Apunta la clave de configuración en papel y guárdala bien.
> - **Apps de autenticación falsas y páginas de inicio de sesión clonadas.** Instala apps solo desde la tienda oficial y escribe tú mismo la dirección del exchange o usa un marcador.

## Qué significa si compras con regularidad

Si compras un poco cada mes, tu cuenta del exchange se va convirtiendo poco a poco en una cantidad importante; por ejemplo, bitcoin está ahora en {{price:btc}} ({{chg1y:btc}} en 12 meses): resultados pasados, no una previsión. Diez minutos configurando la 2FA protegen años de compras. Sigue lo que tienes en tu [página de cartera]({lang}/me/).

Lección anterior: [frase semilla: 5 reglas para mantenerla a salvo]({lang}/blog/seed-phrase-safety-rules/). Más: [cómo registrarse en un exchange de criptomonedas]({lang}/blog/how-to-register-on-a-crypto-exchange/), [exchanges que funcionan en tu país]({lang}/exchanges/). Todas las lecciones están en la [página Aprender]({lang}/learn/).

## Fuentes

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 de febrero de 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Soporte de Binance: How to enable Google Authenticator for 2FA on the Binance app (actualizado el 10 de diciembre de 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Soporte de Binance: How to create a passkey for my Binance account (actualizado el 10 de diciembre de 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*No es asesoramiento de inversión.*
