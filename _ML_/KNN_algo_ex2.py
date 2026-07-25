from sklearn.neighbors import KNeighborsClassifier
import numpy as np
# Özellikler: [Ağırlık (gram), Sertlik (1-10 arası)]
X = np.array([[150, 8], [170, 9], [40, 2], [50, 3]])
# Meyve: 1 (Elma), 0 (Çilek)
y = np.array([1, 1, 0, 0])

knn_fruit = KNeighborsClassifier(n_neighbors=1)
knn_fruit.fit(X, y)

# Yeni meyve: 160 gram ve 7 sertlikte
tahmin = knn_fruit.predict([[160, 7]])
print("Meyve Tahmini:", "Elma" if tahmin[0] == 1 else "Çilek")

