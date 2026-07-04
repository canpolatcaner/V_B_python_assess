import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Rastgele, korelasyonlu veri üretelim (Kaggle benzeri hazır veri)
np.random.seed(42)
sarkilar = 100
süre_dk = np.random.normal(4, 0.8, sarkilar) # Ortalama 4 dk, 0.8 sapma
dinlenme_milyon = 15 + süre_dk * 4 + np.random.normal(0, 5, sarkilar) # Süreyle artan dinlenme

# 2. Veriyi DataFrame'e atalım
df_sarki = pd.DataFrame({'Şarkı Süresi (dk)': süre_dk, 'Dinlenme Sayısı (Milyon)': dinlenme_milyon})

# 3. Modern koyu temayı açalım
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# 4. Dağılım grafiği (Scatter Plot) oluştur - Parlayan noktalar efekti
# Matplotlib'de gerçek parıltı zor ama parlak mint noktalar şık durur.
ax.scatter(df_sarki['Şarkı Süresi (dk)'], df_sarki['Dinlenme Sayısı (Milyon)'],
           color='#10b981', alpha=0.6, s=60, edgecolor='white', label='Şarkı Verileri')

# 5. Eğilim çizgisini hesapla ve ekle (Lineer Regresyon)
m, b = np.polyfit(df_sarki['Şarkı Süresi (dk)'], df_sarki['Dinlenme Sayısı (Milyon)'], 1)
ax.plot(df_sarki['Şarkı Süresi (dk)'], m*df_sarki['Şarkı Süresi (dk)'] + b, color='#10b981', linestyle='--', linewidth=2, label='Eğilim Çizgisi')

# 6. Başlık ve etiketleri özelleştir
ax.set_title('Örnek 3: İlişki ve Korelasyon - Şarkı Süresi & Dinlenme', fontsize=18, fontweight='bold', color='#10b981')
ax.set_ylabel('Dinlenme Sayısı (Milyon)', fontsize=14, color='white')
ax.set_xlabel('Şarkı Süresi (dk)', fontsize=14, color='white')

# Sınırları belirle
ax.set_xlim(2, 6)
ax.set_ylim(0, 50)

# Eksenlerdeki sayıların formatını güzelleştir
ax.tick_params(axis='both', colors='white')

# Grid çizgilerini ekle
ax.grid(linestyle='-', alpha=0.1, color='#334155')

# Ekstra Bilgi Kutusu
ax.text(0.95, 0.95, '`plt.scatter` ve basit bir trend çizgisi ile korelasyon arayışı.',
        transform=ax.transAxes, fontsize=10, color='#94a3b8',
        bbox=dict(facecolor='#1e293b', edgecolor='#334155', boxstyle='round'), horizontalalignment='right', verticalalignment='top')

# Slayt Altyazısı
fig.text(0.1, 0.05, 'Matplotlib & Python Ders 2', fontsize=10, color='#64748b')
fig.text(0.9, 0.05, 'Yazılım Kulübü', fontsize=10, color='#64748b', horizontalalignment='right')

plt.tight_layout()
plt.show()


