#h08_1 PyQt5

import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import *
xx = QApplication(sys.argv)
pencere3 = QWidget()
pencere3.show()
# pencere = QLabel()
pencere = QLabel("Tıkla")
pencere1 = QPushButton("Tıkla")
pencere.show()
pencere1.show()


xx.exec()

# pencere özellikleri
from PyQt6.QtWidgets import *
uyg = QApplication([])
pencere = QWidget()
pencere.setWindowTitle('Deneme')
pencere.resize(300,50)
# pencere.setFixedSize(500, 300)
pencere.show()  
uyg.exec()

# layout ile widget yerleştirme
from PyQt6.QtWidgets import *
aa = QApplication([])


bb = QWidget() # pencere nesnesi oluştur
bb.setWindowTitle('Deneme')
bb.setFixedSize(500, 300)


# icerik = QVBoxLayout()
icerik = QHBoxLayout()


icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))


bb.setLayout(icerik)


bb.show()
aa.exec()

# layout ile widget yerleştirme
from PyQt6.QtWidgets import *
aa = QApplication([])
bb = QWidget() # pencere nesnesi oluştur
bb.setWindowTitle('Deneme')
bb.setFixedSize(500, 300)


icerik = QVBoxLayout()
# icerik = QHBoxLayout()


yatay1 = QHBoxLayout()
yatay2 = QHBoxLayout()
yatay1.addWidget(QPushButton('Tıkla'))
yatay1.addWidget(QPushButton('Dene'))


yatay2.addWidget(QLineEdit("11 haneli tel gir"))
yatay2.addWidget(QLineEdit())


icerik.addLayout(yatay1)
icerik.addLayout(yatay2)
icerik.addWidget(QLabel('Bilgi'))


bb.setLayout(icerik)


bb.show()
aa.exec()

def mesajGoster():
    # mesaj = QMessageBox()
    # mesaj.setText('Tıkladın!')
    # mesaj.exec()
    print("Tıkladın")



# layout ile widget yerleştirme
from PyQt6.QtWidgets import *
aa = QApplication([])


bb = QWidget() # pencere nesnesi oluştur
bb.setWindowTitle('Deneme')
bb.setFixedSize(500, 300)


icerik = QVBoxLayout()
# icerik = QHBoxLayout()


yatay1 = QHBoxLayout()
yatay2 = QHBoxLayout()
dugme1 = QPushButton('Tıkla')
yatay1.addWidget(dugme1)
yatay1.addWidget(QPushButton('Dene'))
dugme1.clicked.connect(mesajGoster)


yatay2.addWidget(QLineEdit("11 haneli tel gir"))
yatay2.addWidget(QLineEdit())


icerik.addLayout(yatay1)
icerik.addLayout(yatay2)
icerik.addWidget(QLabel('Bilgi'))


bb.setLayout(icerik)


bb.show()
aa.exec()
