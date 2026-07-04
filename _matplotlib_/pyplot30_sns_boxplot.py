import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn'un içinde hazır gelen meşhur "tips" (bahşiş) veri setini yükleyelim
bahsis_verisi = sns.load_dataset("tips")

sns.set_theme(style="ticks")
plt.figure(figsize=(8, 5))

# Günlere göre ödenen toplam hesap miktarını gösteren kutu grafiği
# 'palette' ile harika bir hazır renk geçişi (Muted) uyguluyoruz
sns.boxplot(x="day", y="total_bill", data=bahsis_verisi, palette="muted", hue="day", legend=False)

# Grafik detayları
plt.title('Günlere Göre Toplam Hesap Dağılımı', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Günler', fontsize=11)
plt.ylabel('Toplam Hesap ($)', fontsize=11)

# Eksendeki çizgileri temizleyelim
sns.despine(trim=True)
plt.tight_layout()
plt.show()
