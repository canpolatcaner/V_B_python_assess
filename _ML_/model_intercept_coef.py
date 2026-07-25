# Basit regresyon/ilişki oluşturma, modelleme ve model ile tahmin.
# pip install pandas
import pandas as pd
# df = pd.read_csv("dataframes/Advertising.csv")
df = pd.read_csv("puanlar.csv")
# print("\n\nData frame:\n",df)
# pip install scikit-learn
from sklearn.linear_model import LinearRegression
X = df[["netsayisi"]] # Bağımsız değişken
y = df[["puan"]] # Bağımlı değişken

# print("\n\nBağımsız değişken head()   :\n",X.head())
# print("\n\nBağımlı  değişken head()   :\n",y.head())
# print("\n\nBağımsız değişken head yok :\n",X)

iliski1 = LinearRegression() # Model nesnesi oluşturma
# print(iliski1)
model_formulu = iliski1.fit(X,y) # modeli kuruyoruz./ model eğitme

print ("\n\ndir(model_formulu):",dir(model_formulu))
print ("\n\nmodel_formulu.intercept_ :",model_formulu.intercept_) # Sabit ya da beta0 değeri
print ("\n\nmodel_formulu.coef_      :",model_formulu.coef_) # beta1 katsayısı / coefficients

print ("\n\nmodel.score(X,y) :",model_formulu.score(X,y)) # rkare = model skoru
# rkare : Bağımlı değişkendeki değişikliğin bağımsız değişkenlerin açıklayabilme oranıdır.

xneti = input("Lütfen net sayınızı giriniz\t:")
xneti = int(xneti)
puan_tahmini = model_formulu.predict([[xneti]])
print(xneti,"net için puan tahmini:",puan_tahmini)

