# statsmodels, OLS (Ordinary Least Squares) ile çoklu doğrusal regresyon
import pandas as pd
import statsmodels.api as sm

# Veriyi oku
# df = pd.read_csv("datasets/Advertising.csv")
df = pd.read_csv(
    "exm_scores.csv",
    sep=";",
    encoding="latin5"
)

df = df.iloc[:, 1:]  # İlk sütunu atla

# Bağımsız ve bağımlı değişkenleri ayır
X = df.drop(columns=["PUAN", "Adi Soyadi", "Okul", "Not"])
# Bağımsız değişkenler
y = df['PUAN']  # Bağımlı değişken

# Bağımsız değişkenlere sabit terim ekle (statsmodels için gerekli)
X = sm.add_constant(X)  # Sabit terim (intercept) ekleniyor

# Modeli oluştur ve eğit
model = sm.OLS(y, X).fit()

# Sonuçları yazdır
print(model.summary())
