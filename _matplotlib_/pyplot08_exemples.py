import matplotlib.pyplot as plt

# Veri seti
aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs']
satislar = [2200, 2800, 3500, 3100, 4200]

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 5))

# Sütunları çizme (Yumuşak bir pastel tonu ve kenarlık)
renkler = ['#4ea8de', '#56cfe1', '#64dfdf', '#72efdd', '#80ffdb']
bars = plt.bar(aylar, satislar, color=renkler, edgecolor='gray', linewidth=0.5, width=0.6)

# Sütunların üzerine değerlerini yazma (Şık bir dokunuş)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f"{yval}", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Başlık ve Etiketler
plt.title('Aylara Göre Satış Performansı', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Aylar', fontsize=11)
plt.ylabel('Ciro ($)', fontsize=11)

# Y ekseni sınırını biraz büyütelim ki yazılar sığsın
plt.ylim(0, 5000)
plt.tight_layout()
plt.show()
