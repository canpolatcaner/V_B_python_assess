from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


app = QApplication([])
anaekran = uic.loadUi("anapencere.ui")# UI dosyasını yükle
girisekran = uic.loadUi("girispencere.ui")
ayarekran = uic.loadUi("ayarlarpenceresi.ui")


def tiklandi(): # Butona basılınca çalışacak fonksiyon
    print("Butona tiklandi")


anaekran.pushButton.clicked.connect(tiklandi) # Buton bağlantısı


anaekran.show()# Pencereyi göster
girisekran.show()# Pencereyi göster
ayarekran.show()# Pencereyi göster
app.exec_()
