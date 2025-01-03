# -*- coding: utf-8 -*-
"""BAB 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F9mgeyB7mNbfafpsVN1Tc6cCzJ2SZO2U

Bab 3: Unsupervised Learning and Preprocessing (Pembelajaran Tak Terawasi dan Praproses Data)

1. Tujuan
Bab ini membahas metode pembelajaran tak terawasi (unsupervised learning) dan teknik praproses data. Fokusnya mencakup clustering, reduksi dimensi, dan normalisasi data. Teknik ini berguna untuk mengungkap pola tersembunyi dalam data tanpa menggunakan label.

2. Implementasi Kode
Berikut adalah beberapa contoh kode implementasi untuk metode clustering dan praproses data:
"""

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load dataset Iris
iris = load_iris()
data = iris['data']

# Normalisasi data menggunakan StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
print("Data sebelum scaling:\n", data[:5])
print("Data setelah scaling:\n", data_scaled[:5])

### 2.2 Clustering dengan k-Means
from sklearn.cluster import KMeans

# Clustering menggunakan k-Means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(data_scaled)

# Hasil clustering
print("Cluster centers:\n", kmeans.cluster_centers_)
print("Labels untuk setiap data:\n", kmeans.labels_)

### 2.3 Reduksi Dimensi dengan PCA (Principal Component Analysis)
from sklearn.decomposition import PCA

# Reduksi dimensi menjadi 2 komponen utama
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

print("Data setelah reduksi dimensi:\n", data_pca[:5])

#2.4 Visualisasi Hasil Clustering
import matplotlib.pyplot as plt

# Visualisasi data yang telah direduksi dimensinya
def plot_clusters(data, labels, title):
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=50)
    plt.title(title)
    plt.xlabel('Komponen Utama 1')
    plt.ylabel('Komponen Utama 2')
    plt.colorbar()
    plt.show()

plot_clusters(data_pca, kmeans.labels_, "Hasil Clustering k-Means")

"""## 3. Penjelasan Teoritis

### 3.1 Apa itu Pembelajaran Tak Terawasi?
Pembelajaran tak terawasi digunakan untuk menemukan pola atau struktur dalam data tanpa label. Tidak ada informasi target, sehingga algoritma mencoba mengelompokkan atau menyederhanakan data.

### 3.2 Teknik Praproses Data
- **Normalisasi**: Menyesuaikan skala data sehingga setiap fitur memiliki distribusi yang serupa (mean = 0, variance = 1).
- **Reduksi Dimensi**: Menurunkan jumlah fitur untuk mempermudah analisis atau visualisasi.

### 3.3 Metode Clustering
- **k-Means**: Mengelompokkan data ke dalam k cluster berdasarkan jarak ke pusat cluster.
- **Evaluasi Clustering**: Biasanya menggunakan metrik seperti Silhouette Score untuk menilai seberapa baik data dikelompokkan.

### 3.4 PCA untuk Reduksi Dimensi
Principal Component Analysis (PCA) digunakan untuk menemukan komponen utama yang merepresentasikan data dengan kehilangan informasi seminimal mungkin.

## 4. Insight & Ringkasan
- **Clustering dengan k-Means** berhasil membagi data Iris menjadi 3 cluster yang mencerminkan spesies bunga.
- **PCA** efektif mereduksi data menjadi 2 dimensi tanpa kehilangan banyak informasi.
- Normalisasi data sangat penting untuk memastikan performa algoritma berbasis jarak seperti k-Means.
"""