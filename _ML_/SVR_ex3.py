# SVM ile garimenkul kira bedeli tahmini
from sklearn.svm import SVR
import numpy as np

# Özellikler: [Evin Yaşı, Oda Sayısı]
X = np.array([[2, 3], [15, 2], [30, 2], [1, 4]])
# Kira Bedeli (TL)
y = np.array([15000, 8000, 6000, 22000])

svr_rent = SVR(kernel='linear')
svr_rent.fit(X, y)

# Yeni tahmin: 10 yaşında ve 3 odalı ev
tahmin = svr_rent.predict([[10, 3]])
print("Tahmini Kira:", tahmin[0]) 
