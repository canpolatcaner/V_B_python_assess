import matplotlib.pyplot as plt
import numpy as np

# Veri setini oluşturma (0 ile 10 arasında 100 nokta)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Modern bir stil seçelim
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 4.5))

# Çizgileri çizme (Renk ve çizgi stilleri ile)
plt.plot(x, y1, label='Sinüs Dalgalanması', color='#1f77b4', linewidth=2)
plt.plot(x, y2, label='Kosinüs Dalgalanması', color='#ff7f0e', linewidth=2, linestyle='--')

# Başlık ve Etiketler
plt.title('Zaman İçindeki Değişim (Çizgi Grafiği Örneği)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Zaman (Saniye)', fontsize=11)
plt.ylabel('Değer', fontsize=11)

# Göstergeler (Legend) ve Grafiği Ekrana Verme
plt.legend(frameon=True, facecolor='white', edgecolor='none')
plt.tight_layout()
plt.show()
