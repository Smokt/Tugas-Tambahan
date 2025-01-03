# -*- coding: utf-8 -*-
"""Bab 6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1L91Y7GLtwqbWMigfIwXYcLvuGXziqBy5

# Bab 6: Algorithm Chains and Pipelines (Rangkaian Algoritme dan Pipeline)

# Bab 6: Algorithm Chains and Pipelines (Rangkaian Algoritme dan Pipeline)

## 1. Tujuan
Bab ini membahas bagaimana merangkai beberapa langkah preprocessing dan model machine learning ke dalam satu alur kerja menggunakan pipeline. Hal ini mempermudah proses otomatisasi dan mengurangi kemungkinan kesalahan dalam penanganan data.

## 2. Implementasi Kode
### 2.1 Membuat Pipeline
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Membuat pipeline dengan scaler dan SVM
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='linear'))
])

# Data sederhana
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [0, 0, 1, 1]

# Training pipeline
pipeline.fit(X, y)
print("Model berhasil dilatih dengan pipeline.")

from sklearn.model_selection import GridSearchCV

# Parameter grid untuk pipeline
param_grid = {
    'svm__C': [0.1, 1, 10],
    'svm__gamma': [0.1, 1, 10]
}

# Grid search dengan pipeline
grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X, y)
print("Best parameters:", grid.best_params_)
print("Best cross-validation score:", grid.best_score_)

"""## 3. Penjelasan Teoritis
- **Pipeline**: Menggabungkan preprocessing dan model menjadi satu objek yang terintegrasi. Memastikan preprocessing diterapkan secara konsisten pada data training dan testing.
- **Parameter Grid dalam Pipeline**: Menggunakan penamaan tahap (misalnya `svm__C`) untuk melakukan pencarian parameter terbaik dengan GridSearchCV.
- **Keuntungan Pipeline**:
  - Mengurangi duplikasi kode.
  - Memastikan data test tidak terkontaminasi preprocessing dari data training.

## 4. Insight & Ringkasan
- Pipeline mempermudah pengelolaan langkah preprocessing dan model dalam satu workflow.
- Menggunakan GridSearch dengan pipeline meningkatkan efisiensi saat mencari hyperparameter terbaik.
- Bab ini mengajarkan cara membangun alur kerja yang lebih bersih dan mudah untuk dikelola dalam proyek machine learning.

"""