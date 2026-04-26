# pip install PyQt5Designer
"""ilk designer kullanımı"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


app = QApplication([])
pencere = uic.loadUi("QtD_1.ui")# UI dosyasını yükle


def tiklandi(): # Butona basılınca çalışacak fonksiyon
    print("Butona tiklandi")


pencere.pushButton.clicked.connect(tiklandi) # Buton bağlantısı


pencere.show()# Pencereyi göster
app.exec_()
# app.exec_() programı çalıştırır ama çıkış kontrolü zayıf
# sys.exit(app.exec_()) programı düzgün kapatır. Büyük projelerde, Hata yönetiminde, Script’lerin doğru sonlanmasında daha temiz ve doğru kapanış

