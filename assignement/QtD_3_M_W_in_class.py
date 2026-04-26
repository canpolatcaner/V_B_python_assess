"""ilk designer kullanımı - sınıf yapısı"""
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("anapencere.ui", self) # UI dosyasını yükle
        self.pushButton.clicked.connect(self.tiklandi) # Buton bağlantısı


    def tiklandi(self): print("Butona tiklandi")


app = QApplication([])
pencere = Pencere()
pencere.show()
app.exec_()
# app.exec_() programı çalıştırır ama çıkış kontrolü zayıf
# sys.exit(app.exec_()) programı düzgün kapatır
