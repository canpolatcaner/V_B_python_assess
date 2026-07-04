import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Veri seti: Bir kedinin 8 haftalık kilo takibi
haftalar = np.arange(1, 9)
kilo_gram = [2050, 2150, 2250, 2400, 2550, 2600, 2650, 2750] # Hafta 1-8

# 2. Modern koyu temayı açalım
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Çizgiyi çiz ve altını gradyanla doldur (Area chart)
# Çizginin kendisi mint yeşili, altı ise daha açık bir yeşil gradyan.
ax.plot(haftalar, kilo_gram, color='#10b981', linewidth=4, marker='o', markersize=8, markeredgecolor='white')
ax.fill_between(haftalar, 2000, kilo_gram, color='#10b981', alpha=0.2)

# 4. Başlık ve etiketleri özelleştir
ax.set_title('Örnek 2: Zaman Serisi Analizi - Kedi Kilo Takibi', fontsize=18, fontweight='bold', color='#10b981')
ax.set_ylabel('Kedi Ağırlığı (gram)', fontsize=14, color='white')
ax.set_xlabel('Hafta', fontsize=14, color='white')

# X ve Y ekseni sınırlarını belirle
ax.set_xlim(1, 8)
ax.set_ylim(2000, 2800)

# Grid çizgilerini ekle
ax.grid(linestyle='-', alpha=0.1, color='#334155')

# Ekstra Bilgi Kutusu
ax.text(0.95, 0.95, '`plt.plot` ve `plt.fill_between` ile trendin net gösterimi.',
        transform=ax.transAxes, fontsize=10, color='#94a3b8',
        bbox=dict(facecolor='#1e293b', edgecolor='#334155', boxstyle='round'), horizontalalignment='right', verticalalignment='top')

# Slayt Altyazısı
fig.text(0.1, 0.05, 'Matplotlib & Python Ders 2', fontsize=10, color='#64748b')
fig.text(0.9, 0.05, 'Yazılım Kulübü', fontsize=10, color='#64748b', horizontalalignment='right')

plt.tight_layout()
plt.show()
