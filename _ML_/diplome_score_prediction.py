# Puan üretme

import pandas as pd
import numpy as np

# Öğrenci sayısı
num_students = 1000

# Not ortalamaları için gerçekçi bir dağılım oluşturuluyor
def generate_grades(mean=70, std_dev=10, size=num_students):
    grades = np.random.normal(mean, std_dev, size)
    return np.clip(grades, 50, 100).round(2)  # Notlar 50-100 arası, 2 ondalık

# Her sınıf için not ortalamaları
grades_9 = generate_grades(mean=70)
grades_10 = generate_grades(mean=72)
grades_11 = generate_grades(mean=74)
grades_12 = generate_grades(mean=76)

# Mezuniyet not ortalaması: 4 yılın ortalaması
graduation_grades = ((grades_9 + grades_10 + grades_11 + grades_12) / 4).round(2)

# Veri çerçevesi oluşturuluyor
df = pd.DataFrame({
    "9_sinif_ort": grades_9,
    "10_sinif_ort": grades_10,
    "11_sinif_ort": grades_11,
    "12_sinif_ort": grades_12,
    "mezuniyet_ort": graduation_grades
})

# CSV dosyasına kaydet
df.to_csv("ogrenci_not_ortalamalari.csv", index=False)

print(df.head())
 

