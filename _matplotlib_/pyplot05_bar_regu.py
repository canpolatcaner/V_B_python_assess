#09 sütun renkleri ve adları
import matplotlib.pyplot as plt

# Kategoriler ve değerler
kategoriler = ["1.Sınav", "2.Sınav", "3.Sınav"]
degerler = [80, 70, 90]

# Sınıf ortalamalarını içeren çizgi grafiği
ort = [75, 80, 90]
plt.plot(kategoriler, ort, label="Sınıf Ort.",
         color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

# Sütun grafiği renklerini ayarla
barlar = plt.bar(kategoriler, degerler, tick_label=["vize", "final", "büt"],
                 width=0.8, color=['red', 'green', 'blue'])

plt.bar_label(barlar) # Sütunlara değerleri ekleme

plt.legend() # Grafik ayarları
plt.title('Kategoriye Göre Değerler')
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

plt.show() # Grafiği gösterme 
