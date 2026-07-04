# pip install matplotlib numpy pandas
import pandas as pd
import matplotlib.pyplot as plt

# 1. Hayali bir kantin veri seti (DataFrame)
data = {
    'Ürün': ['Tost', 'Ayran', 'Su', 'Çikolata', 'Bisküvi', 'Meyve Suyu'],
    'Fiyat': [45, 15, 10, 25, 20, 18],
    'Günlük Satış Adedi': [80, 120, 180, 40, 60, 90]
}

df = pd.DataFrame(data)

# 2. Toplam ciroyu hesaplayalım
df['Toplam Ciro'] = df['Fiyat'] * df['Günlük Satış Adedi']

# 3. Şık bir koyu tema açalım (Modern Sunum Tarzı)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# 4. Sütun grafiği oluştur (Gradyan efekti için hazır renkler)
# Matplotlib'de gradyan zor olsa da, parlak mavi ile modern görünür.
ax.bar(df['Ürün'], df['Günlük Satış Adedi'], color='#38bdf8', edgecolor='white')

# 5. Başlık ve etiketleri özelleştir
ax.set_title('Örnek 1: Kategorik Karşılaştırma - Kantin Satış Paneli', fontsize=18, fontweight='bold', color='#38bdf8')
ax.set_ylabel('Günlük Satış Adetleri', fontsize=14, color='white')
ax.set_xlabel('Item', fontsize=14, color='white')

# 6. Grid çizgilerini ekle ve şıklaştır
ax.grid(axis='y', linestyle='--', alpha=0.3, color='#334155')

# Ekstra Bilgi Kutusu: Pandas Dataframe verisi ile `plt.bar` kullanımı.
ax.text(0.95, 0.95, 'Pandas DataFrame verisi ile `plt.bar` kullanımı. En çok satanı hızlıca görselleştirir.',
        transform=ax.transAxes, fontsize=10, color='#94a3b8',
        bbox=dict(facecolor='#1e293b', edgecolor='#334155', boxstyle='round'), horizontalalignment='right', verticalalignment='top')

# Slayt Altyazısı
fig.text(0.1, 0.05, 'Matplotlib & Python Ders 2', fontsize=10, color='#64748b')
fig.text(0.9, 0.05, 'Yazılım Kulübü', fontsize=10, color='#64748b', horizontalalignment='right')

plt.tight_layout()
plt.show()
