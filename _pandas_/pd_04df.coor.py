import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Rastgele bir öğrenci başarı veri seti oluşturalım
veri = {
    'Ders_Calisma_Saati': [2, 5, 7, 10, 3, 8, 6, 9],
    'Uyku_Saati': [8, 7, 6, 5, 8, 6, 7, 5],
    'Sınav_Notu': [55, 70, 85, 95, 60, 88, 75, 92],
    'Sosyal_Medya_Süresi': [4, 3, 2, 1, 4, 1, 2, 1]
}

df = pd.DataFrame(veri)

# 1. Korelasyonu hesapla
korelasyon = df.corr()

# 2. Seaborn ile şık bir Isı Haritası (Heatmap) çiz
plt.figure(figsize=(6, 4))
sns.set_theme(style="white")

# 'annot=True' sayıları karelerin içine yazar, 'cmap' ise renk paletidir (Coolwarm çok popülerdir)
sns.heatmap(korelasyon, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1, linewidths=0.5)

plt.title('Öğrenci Verileri Korelasyon Matrisi', fontsize=12, fontweight='bold', pad=12)
plt.tight_layout()
plt.show()
