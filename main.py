import cv2
import matplotlib.pyplot as plt
import os

# --- KONFIGURASI NAMA FILE ---
# Pastikan nama file ini SAMA PERSIS dengan yang ada di panel kiri PyCharm
NAMA_FILE_1 = 'foto1.jpg'
NAMA_FILE_2 = 'foto2.jpg'


def run_sift_matching(path1, path2):
    # Cek apakah file benar-benar ada sebelum diproses
    if not os.path.exists(path1):
        print(f"ERROR: File '{path1}' tidak ditemukan di folder project!")
        return
    if not os.path.exists(path2):
        print(f"ERROR: File '{path2}' tidak ditemukan di folder project!")
        return

    # 1. LOAD CITRA
    img1 = cv2.imread(path1)  # QueryImage
    img2 = cv2.imread(path2)  # TrainImage

    # Konversi ke Grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 2. INISIALISASI SIFT
    print("Mendeteksi Keypoints dengan SIFT...")
    sift = cv2.SIFT_create()

    # Deteksi Keypoint & Descriptor
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    # 3. VISUALISASI KEYPOINT (Untuk Laporan)
    img1_kp = cv2.drawKeypoints(img1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # 4. MATCHING (Brute Force + KNN)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # 5. FILTERING (Lowe's Ratio Test)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append([m])

    print(f"Hasil: Ditemukan {len(good_matches)} titik yang cocok (matches).")

    # HASIL MATCHING
    img_matches = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches, None,
                                     flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # liat PLOT
    plt.figure(figsize=(12, 8))

    # Keypoint
    plt.subplot(2, 1, 1)
    plt.imshow(cv2.cvtColor(img1_kp, cv2.COLOR_BGR2RGB))
    plt.title(f'Keypoints Detected (Total: {len(kp1)})')
    plt.axis('off')

    #Matching
    plt.subplot(2, 1, 2)
    plt.imshow(cv2.cvtColor(img_matches, cv2.COLOR_BGR2RGB))
    plt.title(f'Feature Matching SIFT (Good Matches: {len(good_matches)})')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_sift_matching(NAMA_FILE_1, NAMA_FILE_2)