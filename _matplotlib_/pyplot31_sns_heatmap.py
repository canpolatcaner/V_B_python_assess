import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn'un hazır "flights" (uçuşlar) veri setini yükleyelim
ucus_verisi = sns.load_dataset("flights")

# Veriyi yıllar ve aylara göre bir matris (pivot tablo) haline getirelim
ucus_matrisi = ucus_verisi.pivot(index="month", columns="year", values="passengers")

plt.figure(figsize=(9, 6))

# Isı haritasını çizme
# 'cmap' ile renk paletini seçiyoruz, 'annot=True' ile sayıları kutuların içine yazdırıyoruz
# 'fmt="d"' sayıların düzgün (tam sayı) görünmesini sağlar
sns.heatmap(ucus_matrisi, cmap="YlGnBu", annot=True, fmt="d", linewidths=.5)

plt.title('Yıllara ve Aylara Göre Yolcu Sayıları', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Yıl', fontsize=11)
plt.ylabel('Ay', fontsize=11)
plt.tight_layout()
plt.show()
