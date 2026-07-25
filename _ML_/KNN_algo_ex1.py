# evin merkeze uzaklık ve büyüklüğüne bakarak sınıflandırma
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Özellikler: [Metrekare, Merkeze Uzaklık (km)]
X = np.array([[150, 2], [200, 1], [50, 15], [70, 10]])
# Sınıflandırma: 1 (Lüks), 0 (Ekonomik)
y = np.array([1, 1, 0, 0])

# KNN modelini oluşturuyoruz (K=3 komşuya bak)
knn_home = KNeighborsClassifier(n_neighbors=3)
knn_home.fit(X, y)

# Yeni bir ev tahmini: 120 m2 ve merkeze 3 km uzaklıkta
tahmin = knn_home.predict([[120, 3]])
print("Ev Sınıfı Tahmini:", "Lüks" if tahmin[0] == 1 else "Ekonomik") 
