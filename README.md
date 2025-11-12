Proyek Mini Sistem Temu Kembali Informasi (STKI) - UTS 2025

📋 Deskripsi Proyek

Proyek ini merupakan implementasi mini Search Engine sebagai bagian dari Ujian Tengah Semester (UTS) mata kuliah Sistem Temu Kembali Informasi. Sistem ini dirancang untuk memproses, mengindeks, mencari, dan mengevaluasi dokumen menggunakan dua model retrieval klasik: Boolean Retrieval dan Vector Space Model (VSM).

Korpus: 5 dokumen teks (D1.txt - D5.txt) yang berisi berita terkini dari situs kampus dinus.ac.id.

🛠️ Eksperimen Utama

Proyek ini mencakup empat tahapan utama:

1. Document Preprocessing (SOAL 02)

Tujuan: Mengubah dokumen mentah menjadi representasi term yang konsisten.

Tahapan: Case-folding, Tokenisasi, Stopword Removal (Bahasa Indonesia), dan Stemming (menggunakan pustaka Sastrawi).

Output: File-file dokumen yang telah dibersihkan di direktori data/processed/.

2. Boolean Retrieval (SOAL 03)

Tujuan: Membangun indeks biner dan mengimplementasikan pencarian logis.

Implementasi: Pembuatan Inverted Index dan fungsi untuk mengeksekusi operator $\text{AND}$, $\text{OR}$, dan $\text{NOT}$.

Evaluasi: Mengukur kinerja menggunakan metrik Precision, Recall, dan F1-Score pada gold standard yang ditentukan.

3. Vector Space Model (VSM) & Ranking (SOAL 04)

Tujuan: Merepresentasikan dokumen sebagai vektor dan meranking hasil berdasarkan relevansi parsial.

Pembobotan: Menghitung bobot TF-IDF untuk dokumen dan query.

Ranking: Menggunakan Cosine Similarity untuk menentukan kedekatan query dengan dokumen.

Evaluasi: Mengukur kualitas ranking menggunakan metrik Precision@k dan Mean Average Precision ($\text{MAP}@k$).

4. Search Engine Orchestrator (SOAL 05 - Optional)

Mengintegrasikan modul-modul di atas menjadi satu script pencarian sederhana.

stki-uts--/
├─ data/
│  ├─ D1.txt          # Korpus mentah
│  ├─ D2.txt
│  └─ ...
│  └─ processed/      # Hasil output dari preprocessing
├─ src/ (di colab semua datanya)
│  ├─ preprocess.py   # Fungsi-fungsi pembersihan, tokenisasi, stemming
│  ├─ boolean_ir.py   # Implementasi Inverted Index dan logika Boolean
│  ├─ vsm_ir.py       # Implementasi TF-IDF, Cosine Similarity, dan ranking
│  └─ search.py       # (Opsional) Orchestrator untuk menjalankan Boolean/VSM dari CLI
├─ notebooks/ 
│  └─ UTS_STKI_2025.ipynb # Jupyter Notebook/Google Colab utama untuk running dan analisis
├─ reports/ 
│  ├─ laporan.md      # Laporan lengkap proyek (6-10 halaman)
│  └─ readme.md       # File ini
└─ requirements.txt  # Daftar pustaka yang dibutuhkan

Cara Menjalankan Proyek (Menggunakan Google Colab)

Mount Google Drive: Unggah file korpus (D1.txt - D5.txt) ke folder STKI di Google Drive Anda.

Buka Notebook: Jalankan UTS_STKI_2025.ipynb (atau setara) di Google Colab.

Instalasi: Pastikan pustaka seperti Sastrawi, nltk, dan scikit-learn sudah terinstal.

Eksekusi: Jalankan sel-sel kode secara berurutan, mulai dari Document Loading (menghubungkan Drive dan memuat corpus), dilanjutkan dengan Preprocessing, Boolean Retrieval, hingga VSM & Ranking.

Dependencies (requirements.txt)

scikit-learn
nltk
Sastrawi
numpy
pandas
