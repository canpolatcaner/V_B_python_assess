#AYAR PENCESİNİ AÇMA


import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class AyarPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("h08_2 PyQt/ayarlarpenceresi.ui", self)


class GirisPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("h08_2 PyQt/girispencere.ui", self)
        print("Giriş penceresi init çalıştı.")


        self.pushButton.clicked.connect(self.tiklandi)


    def ayarlariAc(self):
        self.ayarPencere1 = AyarPencere()
        self.ayarPencere1.show()


    def tiklandi(self):
        ad = self.lineEdit1.text()
        sf = self.lineEdit2.text()


        if ad == "adm" and sf == "123":
            print("Ayarlar penceresi açılacak")
            self.ayarlariAc()
        else:
            print("Kullanıcı adı veya şifre yanlış")


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("h08_2 PyQt/anapencere.ui", self)


        self.pushButton_3.clicked.connect(self.tiklandi)


    def tiklandi(self):
        print("Butona tıklandı")
        self.girispen = GirisPencere()
        self.girispen.show()


app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()


sys.exit(app.exec_())
