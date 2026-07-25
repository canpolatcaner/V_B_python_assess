import pandas as pd

df = pd.read_csv("Advertising.csv")
df = df.iloc[:,1:len(df)]
print("\n\ndf.head()\n",df.head())
X = df.drop('sales',axis=1)
# y = df["sales"]
y = df[["sales"]] # pandas dataframe
print("\n\ny.head()\n",y.head())
print("\n\nX.head()\n",X.head())

# pip install statsmodels
import statsmodels.api as sm # statsmodels
lm = sm.OLS(y,X) # OLS (Ordinary Least Squares - En Küçük Kareler Yöntemi) linear modelini oluştur.
# bağımlı(y) ve hedef/bağımsız değişken (X) için OLS yöntemiyle, hata kareler toplamını en aza indirerek en iyi regresyon katsayılarını bulmaya çalışır.
model = lm.fit()
# fit() fonksiyonu, modelin parametrelerini veriye en uygun şekilde hesaplar.
# Regresyon katsayıları, hata terimleri ve istatistiksel sonuçlar belirlenir.
print(model.summary()) 
