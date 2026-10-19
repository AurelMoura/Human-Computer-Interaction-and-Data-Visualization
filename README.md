# Human-Computer-Interaction-and-Data-Visualization
# Dashboard Fasilitas Umum Kota Bengkulu

## Deskripsi Proyek

Proyek ini dibuat sebagai studi kasus kegiatan Informatics Practitioner Lecture Series 2026 pada materi *Human-Computer Interaction and Data Visualization* yang disampaikan oleh Arafat Febrian Dirza dari Badan Riset dan Inovasi Nasional (BRIN).

Proyek ini bertujuan untuk menerapkan konsep interaksi manusia dan komputer serta visualisasi data melalui dashboard interaktif menggunakan Python.

## Fitur Dashboard

- Menampilkan jumlah fasilitas, jumlah pengguna, dan jumlah kecamatan.
- Menampilkan grafik jumlah fasilitas berdasarkan kategori.
- Menampilkan grafik jumlah pengguna berdasarkan kecamatan.
- Menyediakan filter kategori fasilitas.
- Menyediakan fitur pencarian berdasarkan nama fasilitas.
- Menampilkan tabel data yang dapat menyesuaikan hasil filter dan pencarian.

## Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- Matplotlib

## Struktur Folder

```text
Human-Computer/
├── dashboard.py
├── data_fasilitas.csv
└── README.md
```

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Buka terminal pada folder proyek.
3. Instal pustaka yang dibutuhkan dengan perintah:

   ```bash
   python -m pip install streamlit pandas matplotlib
   ```

4. Jalankan dashboard menggunakan perintah:

   ```bash
   python -m streamlit run dashboard.py
   ```

5. Buka alamat lokal yang muncul di terminal, biasanya `http://localhost:8501`.

## Penerapan Human-Computer Interaction

Prinsip HCI diterapkan melalui tata letak dashboard yang terstruktur, penggunaan label yang jelas, filter kategori, fitur pencarian, serta penyajian informasi dalam bentuk grafik. Fitur tersebut membantu pengguna menemukan dan memahami informasi dengan lebih mudah.

## Penerapan Data Visualization

Visualisasi data digunakan untuk menampilkan perbandingan jumlah fasilitas berdasarkan kategori dan jumlah pengguna berdasarkan kecamatan. Grafik batang dipilih agar perbedaan antar kategori lebih mudah diamati.

## Dataset

Dataset `data_fasilitas.csv` berisi 10 data fasilitas dengan informasi nama fasilitas, kategori, kecamatan, dan jumlah pengguna.

**Catatan:** Dataset ini merupakan data simulasi untuk keperluan pembelajaran dan bukan data resmi fasilitas umum Kota Bengkulu.

## Tujuan Pembelajaran

Melalui proyek ini, saya mempelajari cara mengolah data menggunakan Pandas, membuat visualisasi dengan Matplotlib, mengembangkan dashboard interaktif dengan Streamlit, serta menerapkan prinsip dasar HCI agar informasi lebih mudah dipahami oleh pengguna.

## Penutup

Proyek ini merupakan penerapan sederhana materi *Human-Computer Interaction and Data Visualization*. Pengembangan selanjutnya dapat mencakup penggunaan data nyata yang terverifikasi, penambahan visualisasi, dan peningkatan aksesibilitas dashboard.
