# SIFT Image Matching (Pencocokan Citra)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![Status](https://img.shields.io/badge/Status-Final%20Project-orange)

Proyek ini merupakan implementasi **Computer Vision** untuk Tugas Akhir mata kuliah Pengolahan Citra Digital. Fokus utama proyek ini adalah mendemonstrasikan algoritma **SIFT (Scale-Invariant Feature Transform)** untuk mencocokkan fitur antara dua citra yang memiliki perbedaan sudut pandang, rotasi, dan skala.

## 📋 Daftar Isi
- [Deskripsi Proyek](#-deskripsi-proyek)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Instalasi & Persiapan](#-instalasi--persiapan)
- [Cara Menjalankan](#-cara-menjalankan)
- [Struktur Folder](#-struktur-folder)
- [Hasil & Analisis](#-hasil--analisis)

---

## 📖 Deskripsi Proyek
Aplikasi ini mendeteksi *keypoints* (titik unik) pada citra referensi dan mencoba menemukannya kembali pada citra target (yang telah diputar atau diperbesar).

**Fitur Utama:**
1.  **Feature Detection:** Menggunakan SIFT untuk mendeteksi keypoint yang invarian terhadap skala dan rotasi.
2.  **Feature Matching:** Menggunakan *Brute-Force Matcher* dengan metode k-Nearest Neighbor (kNN).
3.  **Outlier Removal:** Menerapkan **Lowe's Ratio Test** (ratio 0.75) untuk membuang kecocokan yang ambigu/salah.
4.  **Visualisasi:** Menampilkan garis penghubung antara titik-titik yang cocok (matches).

---

## 🛠 Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3
* **Library Utama:**
    * `opencv-python`: Untuk pemrosesan citra dan algoritma SIFT.
    * `numpy`: Untuk operasi matriks dan numerik.
    * `matplotlib`: Untuk visualisasi hasil matching.

---

## ⚙️ Instalasi & Persiapan

Pastikan Python sudah terinstal di komputer Anda. Ikuti langkah berikut untuk menyiapkan lingkungan pengembangan:

1.  **Clone Repository ini** (atau download ZIP):
    ```bash
    git clone [https://github.com/Adam-Nurwahid/SIFT-Image-Matching-Project.git](https://github.com/USERNAME_ANDA/NAMA_REPO_ANDA.git)
    cd NAMA_REPO_ANDA
    ```

2.  **Install Library yang Dibutuhkan:**
    Gunakan `pip` untuk menginstal dependensi yang tertera di `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

    *Jika file `requirements.txt` belum ada, jalankan manual:*
    ```bash
    pip install opencv-python matplotlib numpy
    ```

---

## 🚀 Cara Menjalankan

1.  Siapkan dua gambar yang ingin dicocokkan (misal: `foto1.jpg` dan `foto2.jpg`) di dalam folder project.
2.  Buka file `main.py` dan sesuaikan nama file pada bagian konfigurasi:
    ```python
    NAMA_FILE_1 = 'foto1.jpg'
    NAMA_FILE_2 = 'foto2.jpg'
    ```
3.  Jalankan program melalui terminal:
    ```bash
    python main.py
    ```
4.  Hasil visualisasi akan muncul di jendela baru.

---

## 📂 Struktur Folder

Pastikan struktur file Anda terlihat seperti ini agar program berjalan lancar:
