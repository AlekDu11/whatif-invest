---
title: "Sniper, bundler, dan dev wallet: cara orang dalam untung saat memecoin diluncurkan"
description: Bot dan orang dalam membeli memecoin baru di detik pertama lalu menjual dalam hitungan menit. Cara kerja sniper, bundler, dev wallet dan cara mengenalinya.
date: 2026-11-27T09:30:00Z
category: learn
track: memes
step: 16
assets: sol, bnb
stat: 87%
stat_label: snipe yang terkait pembuat token di pump.fun berakhir untung (Pine Analytics, April 2025)
---
**Siapa yang membeli memecoin baru sebelum Anda sempat melihatnya?** Sering kali bot dan orang dalam: **sniper** membeli di blok paling pertama, **bundler** membeli dengan banyak wallet sekaligus, dan **dev wallet** (wallet milik pembuat token) bisa memegang porsi besar sejak awal. Mereka membeli paling murah dan sering menjual dalam hitungan menit — kepada orang yang datang belakangan.

> **Poin penting**
> - Pine Analytics menemukan lebih dari **50%** token pump.fun di-snipe di blok yang sama saat token dibuat (laporan 21 April 2025).
> - Dalam satu bulan (mulai 15 Maret 2025) tercatat **15.000+** snipe oleh wallet yang didanai langsung oleh pembuat token; **87%** untung dan sekitar **85%** terjual habis dalam **5 menit**.
> - CoinGecko menemukan **68,67%** dari 18,67 juta token pump.fun melakukan transaksi terakhirnya di hari peluncuran (Januari 2024 – Juni 2026, dilaporkan 25 Juni 2026).

## Tiga orang dalam, dengan bahasa sederhana

Ketiga istilah ini ada di [glosarium memecoin]({lang}/memes/glossary/) kami.

- **Sniper** — wallet, hampir selalu bot, yang membeli di 0–3 blok pertama (blok adalah satu "halaman" blockchain, di Solana kurang dari satu detik). Ia memakai alat khusus untuk masuk sebelum pembeli biasa, mengambil posisi besar dengan murah, lalu menjual ke gelombang permintaan pertama.
- **Bundler** — satu orang yang membeli dengan banyak wallet di blok yang sama atau dalam satu transaksi. Di grafik terlihat seperti 20 pembeli berbeda; padahal hanya satu. Tujuannya: menyembunyikan berapa banyak yang dimiliki satu orang dan memalsukan permintaan.
- **Dev wallet** — wallet yang membuat token. Kalau ia menyimpan porsi besar, atau diam-diam mengirim token ke wallet baru, ia bisa menjual ke semua orang kapan saja.

Laporan Pine Analytics "Exit Liquidity Machines" (exit liquidity = pembeli yang datang belakangan, yang uangnya dipakai orang dalam untuk keluar) menunjukkan cara kerjanya di pump.fun: pembuat token mengirim SOL ke wallet "sekali pakai" (burner) yang baru, wallet-wallet itu membeli di blok pembuatan, dan sebagian besar menjual dalam satu atau dua transaksi. Lebih dari 55% snipe ini ditutup penuh dalam waktu kurang dari satu menit.

## Langkah 1 — Lihat pembeli pertama

Buka token di pelacak (di [halaman memes]({lang}/memes/) kami, halaman token menampilkan holder dan pemeriksaan keamanan; alat seperti GMGN atau Solscan menampilkan transaksi pertama). Kalau banyak wallet membeli **di detik yang sama dengan peluncuran**, dengan **jumlah yang mirip**, itu tanda sniping atau bundling.

## Langkah 2 — Cek berapa banyak yang dimiliki holder teratas

Lihat **10 holder teratas** tanpa liquidity pool. Penyedia data Mobula menyebut 10 teratas di bawah **30%** dan porsi dev di bawah **5%** (atau dikunci/dibakar) sebagai sehat, dan 10 teratas di atas **50%** sebagai tanda bahaya. Beberapa wallet sniper yang bersama-sama memegang lebih dari 20% juga tanda bahaya.

## Langkah 3 — Cek dev wallet

Cari pembuatnya ("dev", "deployer", atau "creator" di halaman token). Apakah sudah menjual? Apakah ia mengirim token ke wallet baru tepat sebelum atau sesudah peluncuran? Apakah wallet yang sama sudah meluncurkan banyak token yang semuanya mati? Dev yang meluncurkan puluhan koin seminggu sedang menjalankan mesin, bukan proyek.

## Langkah 4 — Cari wallet baru yang didanai dari satu sumber

Bundle sering berasal dari wallet yang dibuat beberapa menit sebelum peluncuran dan didanai dari sumber yang sama. Alat bubble map menggambarkannya sebagai satu kelompok yang saling terhubung. Kalau "komunitas"-nya ternyata satu kelompok, harganya ada di tangan satu orang.

## Langkah 5 — Jangan pernah mengejar candle pertama

Lonjakan di menit-menit pertama adalah saat sniper menjual. Kalau Anda tetap ingin membeli, tunggu, lakukan pemeriksaan lengkap dari [cara mengecek memecoin sebelum membeli]({lang}/blog/how-to-check-a-memecoin-before-buying/), pakai jumlah kecil, dan tentukan batas Anda sejak awal.

> **⚠️ Hati-hati**
> - **"Banyak holder = aman."** Bundler bisa membuat ratusan holder dari satu wallet. Lihat siapa yang mendanai mereka, bukan berapa jumlahnya.
> - **"Dev sudah membakar/mengunci token."** Cek sendiri di blockchain; pool yang dikunci tidak menghentikan wallet sniper untuk menjual.
> - **Bot copy-trading "smart money".** Wallet yang terlihat jenius sering kali adalah sniper itu sendiri, atau dev-nya; saat Anda menirunya, mereka sedang menjual.

## Pelajaran untuk pemula

Saat peluncuran, biasanya Anda tidak datang lebih awal — bot-lah yang lebih awal. Hampir 7 dari 10 token pump.fun berhenti diperdagangkan di hari pertamanya, jadi pilihan paling aman sering kali adalah tidak ikut sama sekali. Kalau Anda ikut, anggap itu uang yang bisa hilang seluruhnya. Pembelian rutin cocok untuk aset yang bertahan bertahun-tahun; sebagai perbandingan, koin Solana sendiri, SOL, saat ini berada di {{price:sol}} ({{chg1y:sol}} dalam 12 bulan) — hasil masa lalu, bukan ramalan.

Pelajaran sebelumnya: [cara kerja Binance Alpha]({lang}/blog/how-binance-alpha-works/). Berikutnya: kenapa sebagian besar pembeli memecoin rugi. Semua pelajaran ada di [halaman Belajar]({lang}/learn/).

## Sumber

- [Pine Analytics: Exit Liquidity Machines — dissecting pump.fun farming (21 April 2025)](https://pineanalytics.substack.com/p/exit-liquidity-machines)
- [BeInCrypto: Pump.fun meme coin snipers are a systematic problem (22 April 2025)](https://beincrypto.com/pump-fun-meme-coin-snipers-systematic-problem)
- [Mobula docs: Detecting snipers and bundlers](https://docs.mobula.io/almanac/detecting-snipers-bundlers)
- [KuCoin News / data CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25 Juni 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)

*Bukan nasihat investasi.*
