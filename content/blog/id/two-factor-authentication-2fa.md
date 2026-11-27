---
title: "Autentikasi dua faktor (2FA): cara mengaktifkannya, langkah demi langkah"
description: 2FA menambah kunci kedua pada akun exchange Anda. Cara mengaktifkan aplikasi authenticator atau passkey langkah demi langkah, dan kenapa SMS paling lemah.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: $68 juta
stat_label: hilang akibat penipuan SIM swap pada 2021 dalam 1.611 laporan ke FBI (IC3, Februari 2022)
---
**Apa itu 2FA dan bagaimana cara mengaktifkannya?** Autentikasi dua faktor (2FA) berarti untuk login atau menarik dana dibutuhkan dua hal: kata sandi Anda *dan* bukti kedua, misalnya kode 6 digit dari aplikasi di ponsel atau passkey (sidik jari atau wajah Anda). Aktifkan di pengaturan **Security** (Keamanan) exchange Anda, dan pakai aplikasi authenticator atau passkey, bukan SMS.

> **Poin penting**
> - Dengan 2FA, kata sandi yang dicuri saja tidak cukup untuk mengosongkan akun Anda.
> - **Kode SMS adalah pilihan paling lemah:** dalam "SIM swap", penjahat memindahkan nomor ponsel Anda ke kartu SIM miliknya dan menerima kode-kode Anda. FBI mencatat 1.611 laporan seperti ini dan kerugian lebih dari **$68 juta** pada 2021, naik dari 320 laporan dan sekitar $12 juta pada 2018–2020.
> - FBI menyarankan pilihan yang lebih kuat: aplikasi authenticator, biometrik, atau kunci keamanan fisik.

## Pilihannya, dari yang paling lemah sampai paling kuat

- **Kode SMS** — pesan teks berisi kode. Lebih baik daripada tidak ada, tapi nomor ponsel Anda bisa dicuri.
- **Kode e-mail** — hanya seaman akun e-mail Anda (lindungi juga dengan 2FA).
- **Aplikasi authenticator** (Google Authenticator, Microsoft Authenticator, dan sejenisnya) — aplikasi di ponsel membuat kode 6 digit baru setiap 30 detik, bahkan tanpa internet. Tidak ada yang bisa mencegatnya lewat operator seluler Anda.
- **Passkey** (biometrik) — Anda mengonfirmasi dengan sidik jari, wajah, atau PIN ponsel. Passkey hanya bekerja di situs asli, jadi situs palsu tidak bisa mencurinya.
- **Kunci keamanan fisik** (perangkat kecil USB/NFC) — yang paling kuat, cocok untuk jumlah besar.

## Langkah demi langkah: aplikasi authenticator (contoh di aplikasi Binance)

Exchange lain memakai langkah yang hampir sama; cari **Security** (Keamanan) di profil Anda.

1. **Langkah 1 — Pasang aplikasinya.** Unduh Google Authenticator (atau aplikasi authenticator lain) dari App Store atau Google Play resmi.
2. **Langkah 2 — Buka pengaturan keamanan.** Di aplikasi Binance, ketuk ikon **Account**, ketuk profil Anda di bagian atas, lalu **Security**.
3. **Langkah 3 — Mulai pengaturan.** Ketuk **Authenticator App**, lalu **Enable**. Anda akan melihat kode QR dan **setup key** (kunci pengaturan, berupa kode panjang).
4. **Langkah 4 — Simpan setup key di kertas.** Ini cadangan Anda kalau ponsel hilang. Simpan secara offline, seperti seed phrase. Jangan ketuk **Next** dulu.
5. **Langkah 5 — Tambahkan akun di authenticator.** Di Google Authenticator ketuk **+**, pilih **Enter a setup key** (atau pindai kode QR), tempel kuncinya, ketik nama seperti "Binance", lalu ketuk **Add**.
6. **Langkah 6 — Konfirmasi.** Kembali ke Binance, ketuk **Next** dan ketik kode 6 digit dari aplikasi. Anda akan melihat pesan berhasil.
7. **Langkah 7 — Uji coba.** Log out lalu login lagi. Kalau Anda diminta kode, berarti sudah berfungsi.

## Langkah demi langkah: passkey (lebih mudah lagi)

Menurut halaman bantuan Binance, Anda butuh aplikasi versi 2.60+, iOS 16+ atau Android 9+.

1. **Account → profil → Security → Passkeys (Biometrics) → Add Passkey.**
2. Konfirmasi dengan 2FA yang sedang Anda pakai jika diminta, lalu ketuk **Continue**.
3. Pilih tempat menyimpannya: iCloud Keychain (iPhone), Google Password Manager (Android) atau kunci keamanan, lalu konfirmasi dengan sidik jari, wajah, atau PIN.

## Setelah 2FA aktif

- Matikan SMS sebagai metode login jika exchange mengizinkan, atau setidaknya minta operator seluler Anda mengunci SIM / memasang PIN untuk pemindahan nomor.
- Lindungi juga e-mail yang terhubung ke exchange dengan 2FA.
- Aktifkan **withdrawal whitelist** (daftar putih penarikan: hanya alamat tersimpan yang bisa menerima) jika exchange Anda menyediakannya.

> **⚠️ Hati-hati**
> - **Orang yang asli tidak pernah meminta kode 2FA Anda.** "Support" di Telegram, penelepon dari "exchange" atau "bank" yang meminta kode 6 digit selalu penipu.
> - **Ponsel hilang tanpa kunci cadangan.** Pemulihan akun lalu butuh berhari-hari verifikasi identitas. Tulis setup key di kertas dan simpan dengan aman.
> - **Aplikasi authenticator palsu dan halaman login tiruan.** Pasang aplikasi hanya dari toko resmi dan ketik sendiri alamat exchange, atau pakai bookmark.

## Artinya jika Anda membeli secara rutin

Kalau Anda membeli sedikit setiap bulan, akun exchange Anda pelan-pelan menjadi jumlah yang berarti — misalnya bitcoin saat ini berada di {{price:btc}} ({{chg1y:btc}} dalam 12 bulan), hasil masa lalu, bukan ramalan. Sepuluh menit mengatur 2FA melindungi pembelian bertahun-tahun. Pantau aset Anda di [halaman portofolio]({lang}/me/).

Pelajaran sebelumnya: [seed phrase: 5 aturan agar tetap aman]({lang}/blog/seed-phrase-safety-rules/). Selengkapnya: [cara mendaftar di exchange kripto]({lang}/blog/how-to-register-on-a-crypto-exchange/), [exchange yang bisa dipakai di negara Anda]({lang}/exchanges/). Semua pelajaran ada di [halaman Belajar]({lang}/learn/).

## Sumber

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 Februari 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (diperbarui 10 Desember 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (diperbarui 10 Desember 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Bukan nasihat investasi.*
