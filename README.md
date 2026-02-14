# SIFT Image Matching (Pencocokan Citra)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Final%20Project-red?style=for-the-badge)

Proyek ini merupakan implementasi **Computer Vision** untuk Tugas Akhir mata kuliah Visi Komputer (Viskom). Fokus utama proyek ini adalah mendemonstrasikan algoritma **SIFT (Scale-Invariant Feature Transform)** untuk mencocokkan fitur antara dua citra yang memiliki perbedaan sudut pandang, rotasi, dan skala, menggunakan lingkungan pengembangan Jupyter Notebook.

## 📋 Daftar Isi
- [Deskripsi Proyek](#-deskripsi-proyek)
- [Fitur Unggulan](#-fitur-unggulan)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Instalasi & Persiapan](#-instalasi--persiapan)
- [Cara Menjalankan](#-cara-menjalankan)
- [Struktur Folder](#-struktur-folder)
- [Konfigurasi Visualisasi](#-konfigurasi-visualisasi)
- [Author](#-author)

---

## 📖 Deskripsi Proyek
Aplikasi ini berjalan di atas Jupyter Notebook untuk mendeteksi *keypoints* (titik unik) pada citra referensi dan menemukannya kembali pada citra target (yang telah diputar atau diperbesar).

**Alur Kerja Utama:**
1.  **Preprocessing:** Citra di-resize secara otomatis dan (opsional) dirotasi untuk menguji ketahanan algoritma.
2.  **Feature Detection:** Menggunakan `cv2.SIFT_create()` untuk mendeteksi keypoint yang invarian.
3.  **Feature Matching:** Menggunakan *Brute-Force Matcher* (`cv2.BFMatcher`) dengan metode k-Nearest Neighbor (kNN).
4.  **Outlier Removal:** Menerapkan **Lowe's Ratio Test** (ratio 0.75) untuk membuang kecocokan palsu.
5.  **Custom Visualization:** Menggunakan fungsi plotting khusus untuk menggambar garis koneksi yang lebih tebal dan jelas dibandingkan fungsi bawaan OpenCV.

---

## ✨ Fitur Unggulan
Kode ini memiliki beberapa fungsi kustom yang tidak ada pada implementasi dasar:

* **`resize_image()`**: Otomatis mengubah dimensi gambar (default 50%) agar proses komputasi lebih ringan tanpa merusak aspek rasio.
* **`rotate_image()`**: Utilitas untuk memutar gambar guna simulasi perubahan sudut pandang.
* **`draw_custom_matches()`**: Fungsi visualisasi manual yang memungkinkan pengaturan:
    * Ketebalan garis koneksi (*Thickness*).
    * Warna garis (Hijau/Kustom).
    * Ukuran titik keypoint (*Radius*).

---

## 🛠 Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3
* **Environment:** Jupyter Notebook / Google Colab
* **Library Utama:**
    * `opencv-python` (cv2): Algoritma SIFT dan manipulasi citra.
    * `numpy`: Operasi matriks untuk rotasi dan koordinat.
    * `matplotlib`: Visualisasi hasil matching di dalam notebook.

---

## ⚙️ Instalasi & Persiapan

Pastikan Python dan Jupyter sudah terinstal. Ikuti langkah berikut:

1.  **Clone Repository ini:**
    ```bash
    git clone [https://github.com/Adam-Nurwahid/SIFT-Image-Matching-Project.git](https://github.com/Adam-Nurwahid/SIFT-Image-Matching-Project.git)
    cd SIFT-Image-Matching-Project
    ```

2.  **Install Library yang Dibutuhkan:**
    Jalankan perintah berikut di terminal:
    ```bash
    pip install opencv-python matplotlib numpy jupyter
    ```

---

## 🚀 Cara Menjalankan

Karena proyek ini menggunakan `.ipynb`, cara menjalankannya berbeda dengan script `.py` biasa.

1.  **Siapkan Citra:**
    Simpan dua gambar target (misal: `foto1.jpg` dan `foto2.jpg`) di folder yang sama dengan notebook.

2.  **Buka Jupyter Notebook:**
    ```bash
    jupyter notebook viskom-final.ipynb
    ```

3.  **Konfigurasi Path Gambar:**
    Pada **Cell ke-3** (atau bagian konfigurasi awal), ubah variabel berikut sesuai nama file Anda:
    ```python
    PATH_FOTO_1 = 'foto1.jpg'  # Ganti dengan nama file Anda
    PATH_FOTO_2 = 'foto2.jpg'
    ```

4.  **Jalankan Semua Cell:**
    Klik menu **Cell** > **Run All**. Hasil visualisasi pencocokan akan muncul di bagian bawah notebook.

---

## 📂 Struktur Folder

Pastikan struktur direktori Anda terlihat seperti ini:

```text
SIFT-Image-Matching-Project/
│
├── .ipynb_checkpoints/
├── viskom-final.ipynb      # File Utama (Source Code Jupyter Notebook)
├── README.md               # Dokumentasi Proyek
├── foto1.jpg               # Citra Input 1 (Query)
└── foto2.jpg               # Citra Input 2 (Train)
 ```


---

## 🎨 Konfigurasi Visualisasi

Anda dapat mengubah tampilan output dengan memodifikasi variabel konstanta di dalam notebook:

```python
# Pengaturan Tampilan
THICKNESS_GARIS = 3        # Ketebalan garis penghubung (semakin besar semakin tebal)
RADIUS_TITIK = 10          # Ukuran lingkaran pada keypoint
WARNA_GARIS = (0, 255, 0)  # Warna garis dalam format (B, G, R)
 ```

---
## 👨‍💻 Author

**Adam Nurwahid**

* **GitHub:** [@Adam-Nurwahid](https://github.com/Adam-Nurwahid)
* **Email:** adamtoyibn@gmail.com
