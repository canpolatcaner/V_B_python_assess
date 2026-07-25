# SVM ile Akıllı Saatlerde Kalori Tahmini
from sklearn.svm import SVR
import numpy as np

# Özellikler: [Hız (km/h), Nabız]
X = np.array([[5, 100], [8, 140], [3, 80], [10, 160]])
# Yakılan Kalori
y = np.array([200, 450, 120, 600])

svr_health = SVR(kernel='poly', degree=3)
svr_health.fit(X, y)

# Yeni tahmin: 6 km hız ve 120 nabız
tahmin = svr_health.predict([[6, 120]])
print("Tahmini Kalori:", tahmin[0])

