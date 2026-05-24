# Sadece diyalog
from PyQt6.QtWidgets import *

uygulama = QApplication([])

diyalog1 = QDialog()
diyalog1.setWindowTitle("Diyalog!")
diyalog1.exec()

# diyalog ve pencere
from PyQt6.QtWidgets import *
uygulama = QApplication([])

dlg = QDialog()
dlg.setWindowTitle("Diyalog!")
dlg.exec()

pencere = QMainWindow()
pencere.show()

uygulama.exec() 

#######################################################################
# önce diyalog sonra uygulama

from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout() # icerik Layoutu
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        diyalog = QDialog()
        diyalog.setWindowTitle("Diyalog!")
        diyalog.exec()

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec()

#######################################################################
# Düğmeye basınca gelen diyalog

import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Diyalog göster!")
        button.clicked.connect(self.tiklama)
        self.setCentralWidget(button)

    def tiklama(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("MERHABA!")
        dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#######################################
# Butonları olan diyalog

import sys
from PyQt6.QtWidgets import *

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SELAM!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("OK'a basarsanız olur, yoksa iptal edilir.")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        yerlesim = QVBoxLayout()      
        buton1 = QPushButton("Diyalog göster!")
        yerlesim.addWidget(QLabel("Diyalog gösterme uygulaması"))
        yerlesim.addWidget(buton1)
        buton1.clicked.connect(self.tiklama)
        araclar = QWidget()
        araclar.setLayout(yerlesim)
        self.setCentralWidget(araclar)

    def tiklama(self, s):
        diyalog = QDialog()
        # diyalog.setWindowTitle("MERHABA!")
        diyalog.exec()

        diyalog = CustomDialog()
        diyalog.setWindowTitle("DİKKAT!")
        diyalog.exec()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

##########################
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            print("OK!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


######################

import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


#######################################################################
# Yerleşik diyaloglar
# Düğmeye basınca gelen diyalog

import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        yerlesim = QVBoxLayout()      
        buton1 = QPushButton("Diyalog göster!")
        yerlesim.addWidget(QLabel("Diyalog gösterme uygulaması"))
        yerlesim.addWidget(buton1)
        buton1.clicked.connect(self.tiklama)
        araclar = QWidget()
        araclar.setLayout(yerlesim)
        self.setCentralWidget(araclar)

    def tiklama(self, s):
        QMessageBox.about(self, "title", "mesaj")
        QMessageBox.critical(self, "title", "mesaj")
        QMessageBox.information(self, "title", "mesaj")
        QMessageBox.warning(self, "title", "mesaj")
        QMessageBox.question(self, "title", "mesaj")
        sonuc = QMessageBox.question(self, "title", "Cevabın ne?")
        if sonuc == QMessageBox.StandardButton.Yes: print("olumlu")
        else : print("olumsuz")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


#######################################################################
# Sonuca göre ne yapacağı
# Düğmeye basınca gelen BASİT diyalog

import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        yerlesim = QVBoxLayout()      
        buton1 = QPushButton("Diyalog göster!")
        yerlesim.addWidget(QLabel("Basit diyalog gösterme"))
        yerlesim.addWidget(buton1)
        buton1.clicked.connect(self.tiklama)
        araclar = QWidget()
        araclar.setLayout(yerlesim)
        self.setCentralWidget(araclar)

    def tiklama(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Bilgilendirme!")
        dlg.setText("Buradaki bilgiyi öğrendin.")
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:#Düğme sonucu
            print("TAMAM!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
