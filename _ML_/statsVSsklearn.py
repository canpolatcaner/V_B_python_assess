# ör1: statsmodels ile katsayılar
# pip install statsmodels
import statsmodels.api as sm
import numpy as np

# Örnek veri
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Bağımsız değişkenlere sabit (constant) ekleme
X = sm.add_constant(X)

# OLS regresyon modeli
model = sm.OLS(y, X).fit()

# Katsayıları göster
# print(model.params)  # İlk değer b₀ (intercept), ikinci değer b₁ (eğim katsayısı)
print(f"Intercept (b₀): {model.params[0]:.2f}")  # Sabit katsayı
print(f"Coef (b₁): {model.params[1]:.2f}")  # Eğilim katsayısı

# ör2: sklearn ile katsayılar
from sklearn.linear_model import LinearRegression
import numpy as np

# Örnek veri
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # X'i 2D hale getiriyoruz
y = np.array([2, 4, 5, 4, 5])

# Modeli eğit
lm = LinearRegression().fit(X, y)

# Sonuçları yazdır
print("Intercept (b₀):", lm.intercept_)  # Sabit katsayı
print("Coef (b₁):", lm.coef_)  # Eğilim katsayısı
