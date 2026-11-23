---
title: Cara membuat Binance Wallet dan membeli memecoin: langkah demi langkah
description: Buat Binance Wallet di aplikasi Binance, backup, pindahkan koin dari akun Binance, cari token lewat alamat kontrak, lalu swap, lengkap dengan cek keamanan.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: bagian kunci melindungi Binance Wallet; Anda butuh 2 untuk masuk
---
**Bagaimana cara membuat Binance Wallet?** Buka aplikasi Binance, pindah ke tab **Wallet** di bagian atas, ketuk **Create Keyless Wallet** (buat wallet tanpa kunci), lalu backup dengan kata sandi pemulihan. Hanya butuh beberapa menit, tidak perlu seed phrase, dan Anda mendapat wallet self-custody (wallet tempat Anda sendiri, bukan exchange, yang mengendalikan koin) untuk membeli token on-chain seperti memecoin.

> **Poin penting**
> - Binance Wallet ada di dalam aplikasi Binance. Anda butuh akun Binance yang sudah terverifikasi, tetapi koin di wallet itu Anda pegang sendiri; backup adalah tanggung jawab Anda.
> - Ini wallet "keyless" (MPC): kuncinya dibagi menjadi 3 bagian, di ponsel Anda, di backup cloud Anda, dan di Binance. Dua bagian mana saja bisa membuka wallet.
> - Jangan pernah melewatkan backup. Kalau ponsel Anda hilang **dan** Anda lupa kata sandi pemulihan, Binance tidak bisa memulihkan wallet.

Sebelum mulai: sebagian besar memecoin baru kehilangan hampir seluruh nilainya. Gunakan hanya uang yang siap Anda relakan hilang sepenuhnya. Baca dulu [apa itu memecoin]({lang}/blog/what-are-memecoins/).

## Yang Anda butuhkan

- Ponsel dengan aplikasi resmi Binance (unduh hanya dari App Store, Google Play, atau binance.com; aplikasi palsu banyak beredar).
- Akun Binance yang sudah lolos verifikasi identitas (KYC, menunjukkan kartu identitas). Kalau belum punya, Anda bisa mendaftar lewat tautan kami: [Binance Wallet](/go/binance-web3?from=learn&l=id).
- Sedikit BNB atau SOL di akun Binance Anda, untuk membeli dan membayar biaya jaringan.

## Langkah 1 — Buka wallet

1. Masuk ke aplikasi Binance.
2. Di bagian atas layar, pindah dari **Exchange** ke **Wallet**.
3. Ketuk **Create Keyless Wallet**. (Kalau Anda sudah punya wallet lain, pilihan lainnya adalah **Import Wallet** (impor wallet); pemula tidak membutuhkannya.)

Pembuatannya hanya beberapa detik. Aplikasi tidak menampilkan 12 atau 24 kata seed phrase; sebagai gantinya ia memakai MPC (multi-party computation: kunci dibagi menjadi potongan-potongan yang tidak pernah berada di satu tempat).

## Langkah 2 — Backup (jangan dilewati)

Aplikasi menawarkan tiga cara menyimpan bagian backup Anda. Pilih salah satu:

- **iCloud atau Google Drive.** Anda membuat **kata sandi pemulihan** yang hanya Anda ketahui. Bagian kunci dienkripsi dengannya dan disimpan di cloud Anda.
- **Kode QR.** Anda membuat kata sandi pemulihan dan menyimpan kode QR; bagian kunci disimpan di cloud terdesentralisasi.
- **Quick Backup** (backup cepat). Anda konfirmasi dengan Face ID atau sidik jari; tanpa kata sandi, tetapi bagian kunci dipegang oleh penyedia pihak ketiga.

Tulis kata sandi pemulihan di kertas dan simpan di tempat aman. Lalu cek: ketuk **Settings** (pengaturan, kiri atas di Home atau Assets) → **Wallet Management** (manajemen wallet). Anda harus melihat label **Backed Up** (sudah di-backup).

## Langkah 3 — Pindahkan koin dari Binance ke wallet

1. Di wallet, ketuk **Receive** (terima) → **Withdraw from Binance Exchange** (tarik dari exchange Binance).
2. Pilih koin (misalnya BNB) **dan jaringannya** (BNB Smart Chain untuk BNB, Solana untuk SOL). Jaringannya harus cocok.
3. Masukkan jumlah. Aplikasi menampilkan biaya dan jumlah akhir sebelum Anda konfirmasi.
4. Pilih apakah uangnya berasal dari akun Spot atau Funding, ketuk **Withdraw** (tarik), periksa alamat dan jaringan, lalu **Confirm** (konfirmasi).

Mulailah dengan jumlah uji coba yang kecil. Transfer yang sudah dikonfirmasi tidak bisa dibatalkan. Selalu sisakan sedikit BNB atau SOL di wallet: setiap tindakan di blockchain dikenai biaya jaringan (gas), bahkan yang gagal.

## Langkah 4 — Cari token yang benar lewat alamat kontraknya

Banyak memecoin punya tiruan dengan nama dan logo yang sama. Satu-satunya tanda pengenal yang bisa diandalkan adalah **alamat kontrak** (deretan panjang huruf dan angka yang unik untuk setiap token).

1. Ambil alamatnya dari sumber tepercaya: akun resmi proyek yang terverifikasi, situs data besar, atau halaman token di [halaman memecoin]({lang}/memes/) kami.
2. Di layar **Markets** (pasar) atau **Trade** (perdagangan) di wallet, tempel alamat itu ke kolom pencarian, jangan ketik namanya.
3. Cocokkan 4–6 karakter pertama dan terakhir dengan sumber Anda.

## Langkah 5 — Cek token sebelum membeli

Di [halaman memecoin]({lang}/memes/) kami, setiap halaman token menampilkan cek keamanan dari Binance dan angka-angka penting. Perhatikan:

- **Likuiditas**: berapa banyak uang di pool perdagangan. Likuiditas kecil = Anda mungkin tidak bisa menjual.
- **Holder dan porsi 10 teratas**: kalau beberapa wallet memegang sebagian besar suplai, mereka bisa menjatuhkan harga.
- **Umur**: token yang dibuat satu jam lalu itu seperti tiket lotre.
- **Peringatan**: kalau muncul peringatan risiko atau keamanan apa pun, berhenti.

Binance sendiri menyatakan tidak memeriksa token yang tampil di Meme Rush (feed memecoin yang baru lahir), jadi pemeriksaan ada di tangan Anda. [Pelajaran tentang penipuan dan rug pull]({lang}/blog/memecoin-scams-rug-pull/) kami berisi daftar tanda bahayanya.

## Langkah 6 — Swap

1. Buka **Trade** → **Swap** (tukar). Pilih apa yang Anda pakai untuk membayar (BNB) dan token yang Anda inginkan, di jaringan yang sama.
2. Masukkan jumlah kecil. Baca kursnya, **slippage** (perubahan harga terbesar yang Anda terima sebelum transaksi gagal), dan biaya jaringannya.
3. Beberapa token butuh langkah **Approve** (setujui) lebih dulu; ada biaya kecil untuk itu.
4. Ketuk **Swap** dan konfirmasi dengan passkey atau 2FA Anda.

Untuk menjual, lakukan hal yang sama secara terbalik. Kalau ingin melihat token paling baru, tab Markets punya **Meme Rush**: token yang baru lahir diperdagangkan di sana pada "bonding curve" dan tidak bisa dipindahkan keluar wallet sampai "bermigrasi" ke DEX biasa (bursa terdesentralisasi). Ini sudut pasar yang paling berisiko.

> **⚠️ Hati-hati**
> - **Tidak ada backup, atau kata sandi disimpan di screenshot.** Kehilangan ponsel dan kata sandi berarti koin hilang selamanya.
> - **Jaringan atau alamat yang salah.** FAQ Binance menyebut token yang dikirim ke alamat yang salah tidak bisa dikembalikan. Selalu kirim jumlah uji coba.
> - **Token palsu dan pesan dari "support".** Cari hanya lewat alamat kontrak. Staf Binance tidak akan pernah meminta kata sandi pemulihan Anda atau meminta Anda "memverifikasi" wallet di sebuah situs.

Pelajaran berikutnya: cara menghubungkan Binance Wallet ke situs DEX dan memindahkan koin kembali ke Binance. Lihat semua pelajaran di [halaman Belajar]({lang}/learn/).

## Sumber

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*Bukan nasihat investasi. Memecoin sangat berisiko; panduan ini menjelaskan cara kerja aplikasi dan tidak merekomendasikan membeli token apa pun. Binance Wallet mungkin tidak tersedia di semua negara.*
