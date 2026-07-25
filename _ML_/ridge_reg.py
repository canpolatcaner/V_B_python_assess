# Farklı lambda değerlerine karşılık
# beta bağımsız değişkenin nasıl değişiğini görelim
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.linear_model import RidgeCV

df = pd.read_csv("Hitters.csv") # Baseboll oyuncularının(Hitters) verileri  
df = df.dropna() # Eksik Verileri Temizle. NaN (eksik) değer içeren satırları kaldır.
# Bu adım, modelin eksik verilerden dolayı hata vermesini önlemek için.
dms = pd.get_dummies(df[['League','Division','NewLeague']]) # One-hot encoding yöntemiyle kategorik Değişkenleri Dönüştür.
# League, Division ve NewLeague sütunları dummies (sıfır ve birlerden oluşan kodlama) haline getirilir.
# pd.get_dummies() fonksiyonu, her kategorik değişkeni 0 veya 1 ile ifade eden yeni sütunlar oluşturur.

y = df["Salary"] # Bağımlı değişkeni belirle.
X_ = df.drop(["Salary",'League','Division','NewLeague'], axis=1).astype('float64') # Salary, League, Division ve NewLeague sütunları veri çerçevesinden çıkarılıyor.
# Çünkü: "Salary" bağımlı değişken (tahmin edilecek değer).
# League, Division ve NewLeague → Bunlar kategorik değişkenler, one-hot encoding ile dönüştürüldü, kullanılmayacak.
# astype('float64') → Tüm değişkenlerin veri tipi float64 olarak ayarlar.
X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis=1) # Bağımsız Değişkenlerin (X) Son Halini Oluştur
# One-hot encoding ile oluşturulan yeni sütunlar, sayısal değişkenlerle birleştiriliyor.
# pd.get_dummies() Sadece belirli sütunlar eklendi. Bazı sütunlar ('League_A' gibi) özellikle eklenmedi.
# Çünkü dummy değişken tuzağı (Dummy Variable Trap) oluşmasını önlemek için, kategorik değişkenlerin bir tanesi çıkarılır.
# League_A, League_N, Division_E, Division_W, NewLeague_A, NewLeague_N gibi sütunlar oluşur.
# 'League_N' (League kategorisinin "N" sınıfı)
# 'Division_W' (Division kategorisinin "W" sınıfı)
# 'NewLeague_N' (NewLeague kategorisinin "N" sınıfı)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

print("\n\ndf.head():\n",df.head())
print("\n\ndf.shape(): ",df.shape)

# ridge_model = Ridge(alpha=0.1).fit(X_train,y_train)
ridge_model = Ridge(alpha=5).fit(X_train,y_train)
print("\n\nridge_model:\n",ridge_model)
print("\n\nridge_model.coef_:\n",ridge_model.coef_)
print("\n\nridge_model.intercept_:\n",ridge_model.intercept_)

print(np.linspace(10,-2,100))
lambdalar = 10**np.linspace(10,-2,100)*0.5 # linspace ile belli düzende rasgele sayılar elde ediyoruz.
# ➡ Ridge regresyonun farklı düzenlileştirme seviyelerinde (α = λ) nasıl davrandığını incelemek için
# Lambda (α) Değerlerinin Tanımlıyoruz. lambdalar dizisi, çok büyükten çok küçüğe değişen 100 farklı λ değeri içerir.
# np.linspace(10, -2, 100) → 10 ile -2 arasında 100 eşit bölünmüş nokta oluşturur.
# 10**np.linspace(10, -2, 100) → 10'un kuvvetleri alınarak logaritmik ölçekli 100 farklı değer üretilir.
# Örneğin: 10^10, 10^9, ..., 10^-2 şeklinde giderek küçülen değerler oluşur.
# * 0.5 → Lambda değerleri 0.5 ile çarpılarak ölçeklendirilir.

print("\n\nlambdalar:\n",lambdalar)

ridge_model = Ridge()
katsayilar = [] #  #Her farklı λ değeri için modelin katsayılarını (weights) saklayacak boş bir liste oluşturulur.

for i in lambdalar: # Farklı α değerleri için katsayıların nasıl değiştiği gözlemlemek için
    ridge_model.set_params(alpha=i) # Lambda (α) değerini güncelle. Ridge modelinin düzenlileştirme parametresi (α) i olarak ayarlanıyor.
    ridge_model.fit(X_train, y_train) # Modeli eğit. Güncellenmiş α değeri ile model, eğitim verileri (X_train, y_train) üzerinde yeniden eğitiliyor.
    katsayilar.append(ridge_model.coef_) # Katsayıları kaydet. modelin yeni katsayıları (ridge_model.coef_) listeye ekleniyor.

# print("\n\nKatsayılar:",katsayilar,"\n")
print("\n\nKatsayılar:\n",*katsayilar)
# for x in katsayilar: print(x)

# Farklı Lambda Değerlerine Göre Ridge Katsayılarını grafikte gösterelim.
plt.figure(figsize=(10, 6))
plt.plot(lambdalar, np.array(katsayilar))
plt.xscale("log")  # Lambda değerleri logaritmik ölçekli olduğu için
plt.xlabel("Lambda (α)")
plt.ylabel("Katsayılar (Weights)")
plt.title("Farklı Lambda Değerlerine Göre Ridge Katsayıları")
plt.show()

