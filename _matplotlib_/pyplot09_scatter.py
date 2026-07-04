import matplotlib.pyplot as plt
import numpy as np

# Rastgele 100 veri noktası üretelim
np.random.seed(42)
x = np.random.randn(100)
y = np.random.randn(100)
boyutlar = np.random.rand(100) * 1000  # Noktaların büyüklüğü
renkler = np.random.rand(100)          # Noktaların renk tonu

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 5))

# Dağılım grafiğini çizme (Renk haritası 'viridis' ve şeffaflık 'alpha' ile)
scatter = plt.scatter(x, y, s=boyutlar, c=renkler, cmap='viridis', alpha=0.6, edgecolors='black', linewidth=0.5)

# Başlık ve Etiketler
plt.title('Rastgele Veri Noktaları Dağılımı', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('X Ekseni Özelliği', fontsize=11)
plt.ylabel('Y Ekseni Özelliği', fontsize=11)

# Renk çubuğu (Colorbar) ekleme
plt.colorbar(scatter, label='Yoğunluk Derecesi')

plt.tight_layout()
plt.show()
