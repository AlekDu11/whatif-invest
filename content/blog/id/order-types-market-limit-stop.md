---
title: "Jenis order: market, limit, dan stop order dijelaskan langkah demi langkah"
description: Fungsi tombol Market, Limit, dan Stop di aplikasi exchange atau broker, dengan contoh hitungan dan 3 kesalahan yang bikin pemula rugi.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: jenis order dasar — market (cepat, harga tidak pasti), limit (harga pasti, eksekusi tidak pasti), stop (aktif di harga tertentu)
---
**Ada jenis order apa saja?** **Market order** membeli atau menjual saat itu juga di harga terbaik yang tersedia. **Limit order** membeli atau menjual hanya di harga Anda atau lebih baik, jadi bisa saja tidak pernah tereksekusi. **Stop order** menunggu sampai harga menyentuh level yang Anda pilih, lalu mengirim market order — sering dipakai untuk membatasi kerugian.

> **Poin penting**
> - Market = cepat, tapi Anda tidak mengontrol harga persisnya. Limit = harga terkontrol, tapi tidak ada jaminan tereksekusi.
> - Stop order berubah menjadi market order saat aktif. Saat harga turun cepat, order bisa tereksekusi jauh di bawah harga stop Anda.
> - Sebelum menekan "Beli", selalu cek tiga hal: jenis order, jumlah, dan harga.

## Tiga tombol, dengan bahasa sederhana

Saat membuka layar trading di aplikasi exchange atau broker, biasanya ada tab: **Market**, **Limit**, dan **Stop** (kadang "Stop-limit").

- **Market order.** "Beli sekarang, berapa pun harganya." Order tereksekusi hampir seketika di penawaran terbaik (harga **ask**, harga terendah yang diminta penjual). Untuk koin besar dan saham besar, harganya biasanya sangat dekat dengan yang Anda lihat. Untuk pasar kecil yang sepi, hasilnya bisa jauh lebih buruk.
- **Limit order.** "Beli hanya di $X atau lebih murah" (atau "jual hanya di $X atau lebih tinggi"). Order Anda menunggu di **order book** (daftar semua order beli dan jual yang sedang antre) sampai ada yang menerima harga Anda. Jika harga tidak pernah sampai ke sana, tidak terjadi apa-apa.
- **Stop order (stop-loss).** "Jika harga turun ke $X, jual." Sebelum itu order tidak terlihat dan tidak melakukan apa pun. Saat harga menyentuh $X, order berubah menjadi market order dan menjual di harga berikutnya yang tersedia.
- **Stop-limit order.** Mirip stop, tapi berubah menjadi *limit* order. Anda tidak akan menjual di bawah limit Anda — tapi saat harga turun cepat, order mungkin tidak terjual sama sekali.

## Contoh hitungan dengan angka sederhana

Misalkan harga sebuah saham **$100,00**. Pembeli terbaik menawar $99,95 (harga **bid**) dan penjual terbaik meminta $100,05 (ask). Selisih $0,10 itu disebut **spread**.

1. Anda menekan **Market beli, 10 saham** → Anda membayar sekitar $100,05 per lembar = **$1.000,50** plus biaya jika ada.
2. Anda memasang **Limit beli, 10 saham di $98** → tidak terjadi apa-apa sampai ada penjual yang menerima $98. Jika harga malah naik ke $105, order Anda hanya menunggu dan Anda tidak membeli apa pun.
3. Anda sudah punya sahamnya dan memasang **Stop di $90** → jika harga turun ke $90, order market jual dikirim. Di pasar yang tenang, Anda mungkin dapat $89,95. Jika ada kabar buruk sebelum pasar buka dan saham dibuka di $80, stop Anda aktif dan Anda menjual di sekitar **$80**, bukan $90.

Kasus ketiga itu nyata. Pada 6 Mei 2010 ("flash crash"), harga di AS anjlok dalam hitungan menit. Beberapa stop order tereksekusi jauh di bawah level stop-nya, bahkan ada saham yang diperdagangkan seharga satu sen, menurut laporan SEC dan CFTC.

## Langkah demi langkah: pasang limit order pertama Anda dengan aman

Latihan dulu dengan jumlah yang sangat kecil.

1. **Langkah 1 — Buka layar trading** koin atau saham, lalu pilih **Beli** (Buy).
2. **Langkah 2 — Tekan tab "Limit"**, bukan "Market".
3. **Langkah 3 — Ketik harga Anda.** Lihat harga saat ini dulu (misalnya Bitcoin sekarang {{price:btc}}). Limit yang terlalu jauh di bawahnya mungkin tidak pernah tereksekusi.
4. **Langkah 4 — Ketik jumlahnya.** Cek apakah kolom itu berarti jumlah koin/saham atau uang (USD, EUR). Ini salah ketik yang paling sering terjadi.
5. **Langkah 5 — Cek ringkasan**: jenis, harga, jumlah, total, biaya. Lalu konfirmasi.
6. **Langkah 6 — Temukan order Anda** di "Open orders" (order terbuka). Di sana Anda bisa membatalkannya kapan saja sebelum tereksekusi. Setelah tereksekusi, order pindah ke "Order history" (riwayat order).

> **⚠️ Hati-hati**
> - **Market order di pasar sepi.** Untuk koin kecil atau di luar jam perdagangan normal, market order bisa tereksekusi jauh lebih buruk dari harga di layar (ini disebut **slippage**). Gunakan limit order di sana.
> - **Mengira stop-loss menjamin harga Anda.** Tidak: stop-loss menjamin penjualan, bukan harganya. Gap dan crash bisa mendorong harga eksekusi jauh lebih rendah. Stop-limit melindungi harga, tapi mungkin tidak terjual.
> - **Salah isi kolom.** Salah sisi (Jual, bukan Beli), kelebihan satu nol di jumlah, atau harga diketik di kolom yang salah. Baca ringkasannya sebelum konfirmasi.

## Artinya jika Anda membeli secara rutin

Jika Anda hanya membeli sedikit setiap minggu atau bulan, Anda tidak butuh order yang rumit. Market order pada aset besar yang likuid biasanya sudah cukup, atau limit order sedikit di atas harga saat ini jika Anda ingin batas atas. Hasil sebenarnya datang dari lamanya waktu di pasar: $10 per hari ke Bitcoin selama 3 tahun kini bernilai {{dca:btc:3}} (Anda menyetor {{dcainv:3}}) — hasil masa lalu, bukan ramalan.

Selanjutnya di WhatIfStack: lihat bagaimana order book dan trader besar menggerakkan pasar di [hub trading]({lang}/trading/) dan [pelacak paus Hyperliquid]({lang}/trading/hyperliquid/), bandingkan biaya di [exchange]({lang}/exchanges/), dan temukan semua pelajaran di [halaman Belajar]({lang}/learn/).

## Sumber

- [Investor.gov (SEC): Jenis-jenis order](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Buletin investor — stop, stop-limit, dan trailing stop order](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Jenis order](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC dan SEC: Laporan staf tentang peristiwa pasar 6 Mei 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Bukan saran investasi.*
