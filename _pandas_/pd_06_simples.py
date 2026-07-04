# Ör1: Konu: NumPy Ortalama, min, max
import numpy as np
notlar = np.array([65, 70, 80, 45, 90, 75])
print("Ortalama:", notlar.mean())
print("En yüksek:", notlar.max())
print("En düşük:", notlar.min())
# Sınıfın durumu nedir?En başarılı / en zayıf öğrenci kimler?

# Ör2: Günlük Hava Sıcaklıkları (Konu: Veri analizi, karşılaştırma)
sicaklik = np.array([18, 20, 22, 19, 23, 25, 21])
print("Haftalık ortalama:", sicaklik.mean())
print("En sıcak gün:", sicaklik.max())
# Bu hafta sıcak mı geçti? Kaç dereceyi aşmış?
# Makine öğrenmesi yok, sadece istatistik.

# Ör3: Günlük Adım Sayısı (Konu: Toplam, ortalama)
adimlar = np.array([4500, 7000, 8200, 3000, 10000])
print("Toplam adım:", adimlar.sum())
print("Günlük ortalama:", adimlar.mean())
# Günlük hedef tutmuş mu? Hareketli bir hafta mı?

# Ör4 : Saf veri analizi : Market Fiyat Karşılaştırması (Konu: Diziler arası fark)
market1 = np.array([25, 40, 15])
market2 = np.array([27, 38, 18])
fark = market2 - market1
print("Fiyat farkları:", fark)
# Hangi market daha ucuz? Ne kadar fark var?



# Ör5: Vektörel işlem (NumPy’nin gücü) : Sınav Sonrası Başarılı–Başarısız Ayırma (Konu: Koşullu seçim/filtering)
notlar = np.array([45, 60, 75, 30, 90])
basarili = notlar[notlar >= 50]
basarisiz = notlar[notlar < 50]
print("Başarılılar:", basarili)
print("Başarısızlar:", basarisiz)

# Ör6: Aylık Harcama Analizi (Konu: Toplam, yüzde hesaplama)
# Makine öğrenmesi değil, Veriye göre sınıflama (kural tabanlı)
harcama = np.array([1500, 800, 600, 400])
print("Toplam harcama:", harcama.sum())
print("En fazla harcama:", harcama.max())
# En çok para nereye gitmiş?

"""
# Dikkat : Bunlar veri biliminin “temel analiz” kısmıdır.
# Veri bilimi, veriyi sayılara döküp anlamlı sonuçlar çıkarmaktır; makine öğrenmesi ise bir üst adımdır.

Kullanılanlar : NumPy , Ortalama, min, max, Dizi işlemleri, Kural tabanlı filtre
Olmayanlar : Tahmin, Model, Öğrenme, Yapay zekâ
"""




