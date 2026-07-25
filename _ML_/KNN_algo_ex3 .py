# Bir kişinin izlediği filmlere beğeni durumuna göre film tavsiyesi
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Özellikler: [Aksiyon Puanı, Romantizm Puanı]
X = np.array([[9, 1], [8, 2], [1, 9], [2, 8]])
# Beğeni: 1 (Beğendi), 0 (Beğenmedi)
y = np.array([1, 1, 0, 0])

knn_movie = KNeighborsClassifier(n_neighbors=3)
knn_movie.fit(X, y)

# Yeni kullanıcı: Aksiyon 7, Romantizm 3 seviyor
tahmin = knn_movie.predict([[7, 3]])
print("Film Beğeni Tahmini:", "Beğenecek" if tahmin[0] == 1 else "Beğenmeyecek")
