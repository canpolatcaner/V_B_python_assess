# SVR ile Elektrik tüketimi
from sklearn.svm import SVR
import numpy as np

# Özellikler: [Sıcaklık, Saat]
X = np.array([[30, 12], [25, 18], [15, 8], [10, 22]])
# Tüketim (Megawatt)
y = np.array([500, 450, 300, 250])

# C: Hata payı cezası, epsilon: Tüpün genişliği
svr_elektrik = SVR(kernel='rbf', C=100, epsilon=0.1)
svr_elektrik.fit(X, y)

# Yeni tahmin: 20 derece sıcaklık ve saat 15:00 için
tahmin = svr_elektrik.predict([[20, 15]])
print("Tahmini Elektrik Tüketimi:", tahmin[0]) 
