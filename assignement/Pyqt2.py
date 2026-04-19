#tıklamalar (olay)

from PyQt6.QtWidgets import *
aa = QApplication([])

def tiklama():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()

pencere = QWidget()

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Dene'))
buton1 = QPushButton('Tıkla')
buton1.clicked.connect(tiklama)

icerik.addWidget(buton1)
icerik.addWidget(QLabel('Bilgi'))

pencere.setLayout(icerik)

pencere.show()
aa.exec() 

##################################################################################
#tıklamalar (olay)

import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olayla, Event, Signal, Slot")

        button = QPushButton("Tıkla!")
        # button.setCheckable(True)
        button.clicked.connect(self.tiklama1)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def tiklama1(self): print("Tıklandı!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec() 

##################################################################################
#Widgetlerden verileri alma ve widgete veri yerleştirme

import sys
from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        self.yazmakutusu = QLineEdit()
        icerik.addWidget(self.yazmakutusu)
        self.veri = self.yazmakutusu.text()
        buton1 = QPushButton("Çevir")
        icerik.addWidget(buton1)
        buton1.clicked.connect(self.tiklama)
        self.label1 = QLabel("Sonuç: ")
        self.label1.setStyleSheet("border: 1px solid red;color: blue;")
        icerik.addWidget(self.label1)
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def tiklama(self):
        # self.label1.setText("yeni metin")
        self.label1.setText(self.label1.text()+self.yazmakutusu.text())

uygulama = QApplication(sys.argv)
pencere = ceviriPenceresi()
pencere.show()
uygulama.exec() 

##################################################################################
#windowTitleChanged

# self.button.clicked.connect(self.the_button_was_clicked)
# self.windowTitleChanged.connect(self.the_window_title_changed)
# def the_button_was_clicked(self):
#         print("Clicked.")
#         new_window_title = choice(window_titles)
#         print("Setting title:  %s" % new_window_title)
#         self.setWindowTitle(new_window_title)

# def the_window_title_changed(self, window_title):
#     print("Window title changed: %s" % window_title)

#     if window_title == 'Something went wrong':
#         self.button.setDisabled(True)

##################################################################################
# QLineEdit.textChanged

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
       
        layout = QVBoxLayout()# Layout oluştur

        self.line_edit = QLineEdit()# QLineEdit bileşeni oluştur
        self.line_edit.setPlaceholderText("Buraya metin girin...")

        # Metin değiştiğinde çağrılacak fonksiyonu bağla
        self.line_edit.textChanged.connect(self.print_text)

        layout.addWidget(self.line_edit)# QLineEdit'i layout'a ekle
       
        self.setLayout(layout)# Pencereye layout'u ayarla

    def print_text(self, text):
        """ QLineEdit içeriği değiştiğinde, güncel metni yazdırır. """
        print(text)

app = QApplication([])# Uygulamayı çalıştır
window = MyWindow()
window.show(); app.exec_()

##################################################################################
# QTextEdit.textChanged
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()# Layout oluştur
       
        self.text_edit = QTextEdit()# QTextEdit bileşeni oluştur
        self.text_edit.setPlaceholderText("Buraya metin girin...")
        # self.text_edit.textChanged.connect(lambda: print("Metin değişti!"))
        self.text_edit.textChanged.connect(self.metinDegisti)

        layout.addWidget(self.text_edit)# QTextEdit'i layout'a ekle
        self.setLayout(layout)# Pencereye layout'u ayarla
    def metinDegisti(self):
        print("İçindeki metin:",self.text_edit.toPlainText())

app = QApplication([])# Uygulamayı çalıştır
window = MyWindow()
window.show()
app.exec_() 

##################################################################################
# QLineEdit.textChanged

import sys; from PyQt6.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.etiket = QLabel()
        self.metin = QLineEdit("Buraya metin girin...")
        self.metin.textChanged.connect(self.etiket.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.metin)
        layout.addWidget(self.etiket)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); 
app.exec()

##################################################################################
#Mouse events | Fare olayları

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Fare ile bir şeyler yap.")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

##################################################################################
#mouse button, position

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Fare ile bir şeyler yap.")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

##################################################################################
# bağlam menüsü

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

##################################################################################

# # Event hierarchy / Etkinlik Hiyerarşisi
# def mousePressEvent(self, event):
#     print("Mouse pressed!")
#     super().mousePressEvent(event)

# # Layout forwarding / Layout yönlendirme
# class CustomButton(QPushButton)
#     def mousePressEvent(self, e):
#         e.accept()

# class CustomButton(QPushButton)
#     def event(self, e):
#         e.ignore()

##################################################################################
######PyQt’de signal
# PyQt ile Signal (sinyal) kullanılabilir. PyQt'de PyQt5.QtCore modülündeki Signal sınıfını kullanarak özel sinyaller oluşturabilirsiniz
# Burada butona tıklanınca özel bir sinyal yayılıyor ve sinyal bir fonksiyona bağlanarak konsola mesaj yazdırılıyor.
# from PyQt5.QtCore import pyqtSignal, QObject

# # Özel sinyali içeren bir sınıf oluşturuyoruz
# class MySignals(QObject):  
# # Bir string sinyali tanımladık   
# my_signal = pyqtSignal(str) 

# .emit('"Merhaba" mesajı (sinyali) gönderildi!'))
 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject

class SinyalOlusturSinifi(QObject): # Özel sinyali içeren bir sınıf oluşturuyoruz
    sinyalOzelligi = pyqtSignal(str)  # Bir string sinyali tanımladık

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() # Layout oluştur
        self.button = QPushButton("Sinyali Gönder")# Buton oluştur      
        self.gonderilecek = SinyalOlusturSinifi() # Signal nesnesi oluştur

        self.gonderilecek.sinyalOzelligi.connect( self.sinyal_yakala) # Sinyali bir fonksiyona bağla

        # Butona tıklanınca sinyali yay
        self.button.clicked.connect(lambda: self.gonderilecek.sinyalOzelligi.emit('"Merhaba" mesajı (sinyali) gönderildi!'))
        layout.addWidget(self.button) # Butonu layout'a ekle
        self.setLayout(layout) # Layout'u pencereye ata

    def sinyal_yakala(self, message):
        """ Sinyal tetiklendiğinde çalışacak fonksiyon """
        print(f"Sinyal alındı: {message}")

app = QApplication([]) # Uygulamayı çalıştır
window = MyWindow(); window.show()
app.exec_()

##################################################################################
# slot

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

class MySignals(QObject):
    my_signal = pyqtSignal(str)  # Bir string sinyali tanımladık

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()  # Layout oluştur

        self.button = QPushButton("Sinyali Gönder")  # Buton oluştur
        self.signals = MySignals()  # Signal nesnesi oluştur

        self.signals.my_signal.connect(self.handle_signal)  # Sinyali bir slot'a bağla
        self.button.clicked.connect(lambda: self.signals.my_signal.emit("Merhaba, slot çalıştı!"))  # Butona tıklanınca sinyali yay

        layout.addWidget(self.button)  # Butonu layout'a ekle
        self.setLayout(layout)  # Layout'u pencereye ata

    @pyqtSlot(str)  # Slot olduğunu belirtiyoruz (Opsiyonel)
    def handle_signal(self, message):
        print(f"Sinyal alındı: {message}")  # Sinyal tetiklendiğinde çalışır

app = QApplication([])
window = MyWindow(); window.show()
app.exec_()

# Python'da slot (yuva) kavramı vardır ve PyQt'de sinyallerle (signals) birlikte kullanılır. PyQt’de slot, bir sinyal tetiklendiğinde çalıştırılacak fonksiyondur. Her Python fonksiyonu bir slot olabilir ancak PyQt, @pyqtSlot dekoratörünü kullanarak performansı artırabilir.

# Slot kullanımı performansı artırır ve hata ayıklamayı kolaylaştırır.

# 🚀 Signal-Slot sistemi PyQt'de olayları yönetmek için güçlü bir yöntemdir!


##################################################################################
