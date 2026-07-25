# scikit learn LinearRegresyon ile çoklu doğrusal regresyon
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    "exm_scores.csv",sep=";",
    encoding="latin5"
)

df = df.drop(columns=["SIRA"])# Gereksiz sütunları at
y = df[["PUAN"]]# Hedef değişken
# Bağımsız değişkenler (sadece sonuca etki edecek sayısal veriler)
X = df.drop(columns=["PUAN", "Adi Soyadi", "Okul", "Not"])

lm = LinearRegression()# Model kur
model = lm.fit(X, y)

print("Intercept:", model.intercept_)
print("Katsayılar:", model.coef_)
