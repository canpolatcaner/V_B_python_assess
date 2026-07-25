# Manuel alfa değerli ile en ideal katsayıyı bulma
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import numpy as np

# Özellikler: [Araç Yaşı, Kilometre (10000 km), Motor Gücü (hp)]
X = np.array([[2, 3, 110], [5, 8, 90], [1, 1, 150], [10, 15, 75]])
# Fiyat (Bin TL)
y = np.array([400, 250, 600, 120])

# Ridge modelini oluşturuyoruz (alpha ceza miktarını belirler)
ridge_car = Ridge(alpha=1.0)
ridge_car.fit(X, y)

print("Katsayılar (Ağırlıklar):", ridge_car.coef_)

alphas = [0.01, 0.1, 1.0, 10.0, 100.0]

for a in alphas:
    model = Ridge(alpha=a)
    scores = cross_val_score(model, X, y, cv=2)
    print(f"alpha={a}, ortalama skor={scores.mean()}")

