# pip install seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Yapay bir veri seti oluşturalım
np.random.seed(10)
reklam_gideri = np.random.normal(50, 15, 100)
satislar = reklam_gideri * 2.5 + np.random.normal(0, 20, 100)
veri = pd.DataFrame({'Reklam Gideri ($)': reklam_gideri, 'Satışlar (Adet)': satislar})

# Seaborn stilini aktif edelim (Modern ve temiz bir görünüm)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

# Grafik çizimi: Hem noktaları hem de trend çizgisini tek komutla çizer
sns.regplot(x='Reklam Gideri ($)', y='Satışlar (Adet)', data=veri,
            color="#4c72b0", scatter_kws={'alpha':0.6, 's':40}, line_kws={'color':'#c44e52', 'lw':2})

# Başlık ekleme (Matplotlib fonksiyonu ile)
plt.title('Reklam Harcamalarının Satışlara Etkisi', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()

