#07 legend ve ortalama çizgisi
import matplotlib.pyplot as plt

# Kategoriler ve değerler
kategoriler = ["1.Sınav", "2.Sınav", "3.Sınav"]
degerler = [80, 70, 90]

# x2 = [1,2,3]
ort = [75,80,90]
plt.plot(kategoriler, ort, label = "Sınıf Ort.")

plt.legend()
plt.title('Kategoriye Göre Değerler')
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

# Sütun grafiği oluşturma
plt.bar(kategoriler, degerler)
plt.bar_label(plt.bar(kategoriler, degerler))

plt.show() # Grafiği gösterme 
