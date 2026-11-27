---
title: "Kenapa kebanyakan pembeli memecoin rugi: hitungan peluncuran, slippage, dan biaya"
description: Hanya 0,41% wallet pump.fun yang merealisasikan untung di atas $10.000. Hitungan sederhana soal peluncuran, slippage, dan biaya yang merugikan pembeli memecoin.
date: 2026-11-27T12:00:00Z
category: learn
track: memes
step: 17
assets: sol, bnb
stat: 0,41%
stat_label: dari 13,55 juta wallet pump.fun yang merealisasikan untung di atas $10.000 (data Dune, Januari 2025)
---
**Kenapa kebanyakan orang yang membeli memecoin justru rugi?** Karena hitungannya sudah melawan mereka bahkan sebelum harga bergerak: kebanyakan token baru mati dalam sehari, setiap beli dan jual memakan biaya dan slippage, dan pembeli paling awal (sering kali bot dan orang dalam) menjual ke orang yang datang belakangan. Agar untung, sebuah token harus bertahan *dan* naik cukup tinggi untuk menutup semua itu.

> **Poin penting**
> - Data Dune yang dibagikan pada Januari 2025 menunjukkan hanya sekitar **0,41%** dari 13,55 juta wallet pump.fun yang merealisasikan untung lebih dari **$10.000**.
> - CoinGecko menemukan bahwa **68,67%** token pump.fun melakukan transaksi terakhirnya pada hari peluncuran (data Januari 2024 – Juni 2026).
> - Setiap putaran (beli + jual) pada token baru bisa memakan **2,5%+** hanya untuk biaya platform, belum termasuk biaya jaringan dan slippage.

## Bagian 1 — Hitungan bertahan hidup

Kebanyakan memecoin bukan "murah" — umurnya saja yang pendek.

- **Mati di hari peluncuran.** CoinGecko menghitung 18,67 juta token pump.fun; 68,67% melakukan transaksi terakhirnya pada hari peluncuran (dilaporkan 25 Juni 2026).
- **Sedikit yang sampai ke pasar sungguhan.** "Graduation" (lulus) artinya token keluar dari kurva awal pump.fun dan mendapat pool perdagangan biasa. Data Dune menunjukkan tingkat kelulusan mingguan tetap di bawah **1%** selama empat minggu sejak 17 Februari 2025; minggu terbaiknya, pada November 2024, adalah **1,67%**. Pada Maret 2026 angkanya mencapai **2,01%**, tertinggi sejak Juli 2025.

Jadi kalau Anda memilih token baru secara acak, kebanyakan yang Anda pegang adalah koin yang berhenti diperdagangkan. Beberapa pemenang besar tidak bisa menutup banyak koin yang jatuh ke nol kecuali Anda memilih dengan sangat jeli — dan di hari pertama tidak ada yang tahu mana yang akan bertahan.

## Bagian 2 — Biaya: Anda bayar saat masuk dan saat keluar

Halaman bantuan pump.fun (September 2025) mencantumkan biaya **1,25%** untuk setiap transaksi sebelum graduation (0,95% untuk platform, 0,30% untuk pembuat token). Setelah graduation, biayanya turun seiring token membesar, dari 1,25% untuk yang terkecil sampai 0,30% untuk yang terbesar. Di atas itu masih ada biaya jaringan Solana serta biaya opsional "priority" dan perlindungan MEV (0,003–0,03 SOL per transaksi menurut halaman mereka).

**Contoh hitungan (ilustrasi, bukan harga nyata):** Anda membeli token baru senilai $50 dan membayar priority fee 0,02 SOL untuk tiap arah. Biaya 1,25% saat masuk dan keluar sekitar $1,25, dan dua priority fee bisa menambah beberapa dolar lagi. Hanya untuk balik modal ke $50, token itu mungkin harus naik **5–10%**. Dengan transaksi $10 jauh lebih parah: biaya tetap memakan porsi yang jauh lebih besar.

## Bagian 3 — Slippage: harga bergerak saat Anda membeli

**Slippage** adalah selisih antara harga yang Anda lihat dan harga yang Anda dapat (lihat [glosarium memecoin]({lang}/memes/glossary/)). Token baru punya pool yang sangat kecil, jadi pembelian Anda sendiri mendorong harga naik — begitu juga pembelian orang lain di detik yang sama. Kalau Anda mengatur slippage 10–20% (banyak aplikasi menyarankannya untuk koin baru), artinya Anda setuju membayar hingga sebanyak itu lebih mahal. Saat menjual masalahnya sama tapi terbalik: di pool yang tipis, penjualan Anda menekan harga turun.

## Bagian 4 — Siapa yang ada di seberang Anda

Pembeli paling awal sering kali adalah sniper, bundler, dan wallet developer (lihat [sniper, bundler, dan wallet developer]({lang}/blog/snipers-bundlers-dev-wallets/)). Mereka membeli di harga terendah lalu menjual ke gelombang permintaan pertama. Kalau Anda membeli setelah candle hijau pertama, sering kali Anda menjadi "exit liquidity" — uang tempat mereka menjual.

## Langkah demi langkah: cek hitungannya sebelum menekan «Beli»

1. **Langkah 1 — Hitung biayanya.** Lihat baris biaya di layar swap Anda dan tambahkan biaya jaringan/priority. Kalikan dua (beli + jual).
2. **Langkah 2 — Cek slippage.** Pasang serendah yang memungkinkan (misalnya 1–3% untuk koin dengan pool besar). Kalau sebuah koin butuh slippage 20%, itu tanda bahaya.
3. **Langkah 3 — Cek ukuran pool.** Di [halaman memes]({lang}/memes/) kami, buka tokennya dan lihat likuiditasnya. Pool kecil = slippage besar di dua arah.
4. **Langkah 4 — Jalankan cek keamanan.** Gunakan [cara mengecek memecoin sebelum membeli]({lang}/blog/how-to-check-a-memecoin-before-buying/).
5. **Langkah 5 — Tentukan batas rugi sejak awal.** Pakai hanya uang yang siap hilang seluruhnya, dan tentukan jumlahnya sebelum mulai.

> **⚠️ Hati-hati**
> - **"Harganya cuma $0,0001, bisa naik 1000×."** Harga rendah tidak berarti apa-apa; banyak token beredar dalam jumlah miliaran. Yang penting adalah apakah token itu bertahan dan siapa yang menjual kepada Anda.
> - **Banyak transaksi kecil.** Biaya jaringan dan priority yang tetap bisa memakan 10%+ dari transaksi $10 sebelum harga bergerak sedikit pun.
> - **Screenshot para pemenang.** Anda melihat 0,41% yang menang besar, bukan jutaan orang yang rugi; para "guru" sering menjual koin yang mereka promosikan.

## Artinya jika Anda membeli secara rutin

Pembelian kecil yang rutin cocok untuk aset yang masih ada bertahun-tahun kemudian — bukan untuk token yang bisa berhenti diperdagangkan malam ini. Kalau Anda ingin kripto, jalur yang umum bagi pemula adalah koin besar yang likuid dan dibeli sedikit demi sedikit; sebagai perbandingan, koin milik Solana sendiri, SOL, saat ini berada di {{price:sol}} ({{chg1y:sol}} dalam 12 bulan) — hasil masa lalu, bukan ramalan. Anda bisa mencoba «$10 sehari» untuk aset apa pun di kalkulator kami dan memantaunya di [halaman portofolio]({lang}/me/).

Pelajaran sebelumnya: [sniper, bundler, dan wallet developer]({lang}/blog/snipers-bundlers-dev-wallets/). Semua pelajaran ada di [halaman Belajar]({lang}/learn/).

## Sumber

- [Cointelegraph: Pump.fun crypto traders — majority do not realize profits, Dune data (11 Januari 2025)](https://cointelegraph.com/news/pump-fun-crypto-traders-majority-do-not-realize-profits-dune-data)
- [Cointelegraph: Pump.fun memecoins are dying at record rates, less than 1% survive (14 Maret 2025)](https://cointelegraph.com/news/pump-fun-memecoins-are-dying-at-record-rates-less-than-1-survive)
- [KuCoin News / Odaily, data Dune: pump.fun graduation rate hits 2.01% (17 Maret 2026)](https://www.kucoin.com/news/flash/pump-fun-meme-coin-graduation-rate-hits-2-01-highest-since-july-2025)
- [KuCoin News / data CoinGecko: nearly 70% of pump.fun tokens disappear on launch day (25 Juni 2026)](https://www.kucoin.com/news/flash/nearly-70-of-pump-fun-tokens-disappear-on-launch-day-80-gone-in-2-days)
- [pump.fun Help Center: Transaction fees on pump.fun (September 2025)](https://intercom.help/pumpfun-web/en/articles/11002413-transaction-fees-on-pump-fun)

*Bukan nasihat investasi.*
