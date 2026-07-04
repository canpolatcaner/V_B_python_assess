#10 pasta dilimi grafiği
import matplotlib.pyplot as plt

aktiviteler = ['yemek', 'uyuma', 'çalışma', 'oyun'] # etiketler

miktar = [3, 7, 8, 6] # değerleri (saat olarak)

colors = ['r', 'y', 'g', 'b'] # Etiket renkleri

# pasta dilimi grafiği oluştur.
plt.pie(miktar, labels = aktiviteler, colors=colors,
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')

plt.legend() # etiketleri göster

plt.show() # grafiği göster 

