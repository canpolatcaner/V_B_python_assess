# import sys
# # from PyQt5.QtWidgets import QApplication, QPushButton
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# pencere3 = QWidget()
# # pencere = QLabel()
# pencere = QLabel("Tıkla")
# pencere1 = QPushButton("Tıkla")
# pencere.show()
# pencere1.show()
# pencere3.show()


# app.exec()

#######################################################################

# from PyQt6.QtWidgets import *
# uyg = QApplication([])
# pencere = QWidget()
# pencere.show()  
# uyg.exec()
# # ör-2 >>>>>>>>>
# import sys
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# # Start the event loop.
# app.exec()

#######################################################################

import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
window = QPushButton("Tıkla")
window.show()
app.exec()

#######################################################################

# ör-4 >>>>>>>>>
from PyQt6.QtWidgets import * # PyQt6 
# Uygulama oluşturma
app = QApplication([])
# buraya araçlar(widgets) ekleme
label = QLabel('Merhaba!')
label.show()
# Uygulamayı çalıştırma
app.exec()

#######################################################################
# Ekrana düğme(buton) ve etiket (label) ekleyin

import sys
from PyQt6.QtWidgets import *
app = QApplication(sys.argv)

x = QWidget()
x.show()  
window1 = QPushButton("Tıkla")
window1.show()  
aa = QLabel("Merhaba")
aa.show()

app.exec()

from PyQt6.QtWidgets import * # bununla PyQt6 kütüphanesindeki tüm fonksiyonları programa dahil ediyoruz. 

app.exec() uygulamamızı çalıştırıyoruz.

#######################################################################
# dene

pencere.setWindowTitle('Deneme')
pencere.resize(300,50)
pencere.setFixedSize(100, 100)

import sys
from PyQt6 import QtWidgets
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Merhaba")
button.setFixedSize(100, 100)
button.show()
app.exec()

#######################################################################
# Buton ekleyelim
from PyQt6.QtWidgets import *
aa = QApplication([])

bb = QWidget()

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))

bb.setLayout(icerik)

bb.show()
aa.exec()

#######################################################################
# Tıklama algılama
from PyQt6.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()

#######################################################################
# ör-2: Sınıf ile kullanımın.
from PyQt6.QtWidgets import *
app = QApplication([])
window = QWidget()
label1 = QLabel("Uygulamamıza Hoşgeldiniz")
label1.show()  
window.show()  
app.exec()# Bunu yazmadan deneyin, bakalım ne olacak.

#######################################################################
# ör-3: Bunu deneyin.
from PyQt6.QtWidgets import *

class Pencere (QMainWindow):
    pass

uygulama = QApplication([])

anapencere = Pencere()
anapencere.show()

uygulama.exec()

#######################################################################
# class sız widget ekleme
from PyQt6.QtWidgets import *

uygulama = QApplication([])

pencere = QMainWindow()
pencere.setWindowTitle("Çeviri")

icerik = QVBoxLayout()
# icerik = QHBoxLayout()
icerik.addWidget(QLabel("Çevrilecek: "))
icerik.addWidget(QLineEdit())
icerik.addWidget(QPushButton("Çevir"))
icerik.addWidget(QLabel("Sonuç: "))

araclar = QWidget()
araclar.setLayout(icerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec() 

#######################################################################
# class ile widget ekleme

from PyQt6.QtWidgets import *

class ceviriPenceresi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()
        #icerik = QHBoxLayout()
        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuç: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

uygulama = QApplication([])

pencere = ceviriPenceresi()
pencere.show()

uygulama.exec() 

#######################################################################
# 

from PyQt6.QtWidgets import *

uygulama = QApplication([])

pencere = QMainWindow()
pencere.setWindowTitle("Çeviri")

icerik = QVBoxLayout()
# icerik = QHBoxLayout()
icerik.addWidget(QLabel("Kullanıcı adı: "))
icerik.addWidget(QLineEdit("Ka yaz"))
icerik.addWidget(QLabel("Şİfre: "))
icerik.addWidget(QLineEdit("Şifre yaz"))

dugmeler = QHBoxLayout()
dugmeler.addWidget(QPushButton("Giriş yap"))
dugmeler.addWidget(QPushButton("Vazgeç"))
dugmeler.addWidget(QPushButton("Çıkış"))

icerik.addLayout(dugmeler)
araclar = QWidget()
araclar.setLayout(icerik)
pencere.setCentralWidget(araclar)
pencere.show()

uygulama.exec() 

#######################################################################
# örneklerle qypt

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()

layout = QVBoxLayout()
# layout = QHBoxLayout()
layout.addWidget(QCheckBox("seç"))
layout.addWidget(QComboBox())
layout.addWidget(QDateEdit())
layout.addWidget(QDateTimeEdit())
layout.addWidget(QDial())
layout.addWidget(QDoubleSpinBox())
layout.addWidget(QFontComboBox())
layout.addWidget(QLCDNumber())
layout.addWidget(QLabel("Label"))
layout.addWidget(QLineEdit())
layout.addWidget(QProgressBar())
layout.addWidget(QPushButton("Tıkla"))
layout.addWidget(QRadioButton("seç"))
layout.addWidget(QSlider())
layout.addWidget(QSpinBox())
layout.addWidget(QTimeEdit())

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()
app.exec()

#######################################################################
# örneklerle qypt

import sys

from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        layout.addWidget(QCheckBox())
        layout.addWidget(QComboBox())
        layout.addWidget(QDateEdit())
        layout.addWidget(QDateTimeEdit())
        layout.addWidget(QDial())
        layout.addWidget(QDoubleSpinBox())
        layout.addWidget(QFontComboBox())
        layout.addWidget(QLCDNumber())
        layout.addWidget(QLabel())
        layout.addWidget(QLineEdit())
        layout.addWidget(QProgressBar())
        layout.addWidget(QPushButton())
        layout.addWidget(QRadioButton())
        layout.addWidget(QSlider())
        layout.addWidget(QSpinBox())
        layout.addWidget(QTimeEdit())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec() 

#######################################################################
# örneklerle qypt

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
   
#######################################################################
# resim ekleme

import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

label = QLabel()
pixmap = QPixmap("resimler/arkaplan.jpg")  # aynı klasördeyse
label.setPixmap(pixmap)

label.show()
sys.exit(app.exec()) 

#######################################################################
# resim ekleme
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resim Gösterme")

        label = QLabel(self)
        pixmap = QPixmap("resimler/arkaplan.jpg")
        label.setPixmap(pixmap)
        label.move(20, 20)

app = QApplication(sys.argv)
window = Pencere()
window.show()
sys.exit(app.exec())

#######################################################################
# Resmi pencereye sığdırma
# Oranı bozulmaz, daha kaliteli ölçekleme

pixmap = QPixmap("resim.png")
pixmap = pixmap.scaled(
    300, 200,
    Qt.KeepAspectRatio,
    Qt.SmoothTransformation
)
label.setPixmap(pixmap)

# QLabel boyutuna otomatik sığdırma
# Oran bozulabilir (görüntü esneyebilir)
label.setScaledContents(True)

# Arka plan resmi yapmak (CSS ile)
label.setStyleSheet("""
QLabel {
    background-image: url(resim.png);
    background-repeat: no-repeat;
    background-position: center;
}
""")

#######################################################################
# psınıflı

window.setStyleSheet("""
QMainWindow {
    background-image: url(arka.png);
}
""")

from PyQt6.QtWidgets import *
app = QApplication([])
window = QWidget()
label1 = QLabel("Uygulamamıza Hoşgeldiniz")
label1.show()  
window.show()  
app.exec()

window.setWindowTitle()
window.setFixedSize()
window.setFixedWidth(300)
window.setFixedHeight(200)
window.setMinimumSize() 
window.setMaximumSize()
window.setCentralWidget()
from PyQt6 import QtGui
self.setWindowIcon(QtGui.QIcon('vue.png'))

#######################################################################
# sınıf olmadan

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *

class Pencere (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Pencere, self).__init__(*args, **kwargs)
        self.setWindowTitle("... Uygulaması")

        label1 = QLabel("Uygulamamıza Hoşgeldiniz")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label1)

uygulama = QApplication([])

anapencere = Pencere()
anapencere.show()

uygulama.exec() # Bunu yazmadan deneyin, bakayım ne olacak.
   
#######################################################################
#widget kullanımı

import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *

# Uygulama ana ekran (main window) Subclass QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Uygulama Adı")
        self.setFixedSize(QSize(400, 300))

        button = QPushButton("Tıkla!")
        # Set the central widget of the Window.
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

#######################################################################
#widget kullanımı

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *

class Pencere (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Pencere, self).__init__(*args, **kwargs)
        self.setWindowTitle("... Uygulaması")

        label1 = QLabel("Uygulamamıza Hoşgeldiniz")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label1)

uygulama = QApplication([])

anapencere = Pencere()
anapencere.show()

uygulama.exec() # Bunu yazmadan deneyin, bakayım ne olacak.
   

#######################################################################
#login ekranı tasarımı

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("... Uygulaması")
window.setFixedWidth(300)
window.setFixedHeight(200)

layout = QVBoxLayout() # layout = QHBoxLayout()

layout.addWidget(QLabel("Kullanıcı adı:"))
layout.addWidget(QLineEdit())
layout.addWidget(QLabel("Şifre:"))
layout.addWidget(QLineEdit())
layout.addWidget(QCheckBox("Beni hatırla"))
layout.addWidget(QPushButton("Giriş yap"))
layout.addWidget(QLabel("..."))

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)
window.show()
app.exec()

#######################################################################
#widget hizalama ve özelliklerini değiştirme 

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Pencere(QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()

        self.setWindowTitle("My App")
        widget = QLabel("Hello")
        widget.setText("Merhaba") #değer değiştirme
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font) # widget.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        widget.setAlignment (Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(widget)

uygulama = QApplication([])

anapencere = Pencere()
anapencere.show()

uygulama.exec()


# Qt.AlignmentFlag.AlignLeft      Aligns with the left edge.
# Qt.AlignmentFlag.AlignRight     Aligns with the right edge.
# Qt.AlignmentFlag.AlignHCenter   Centers horizontally in the available space.
# Qt.AlignmentFlag.AlignJustify   Justifies the text in the available space.

# Qt.AlignmentFlag.AlignTop       Aligns with the top.
# Qt.AlignmentFlag.AlignBottom    Aligns with the bottom.
# Qt.AlignmentFlag.AlignVCenter   Centers vertically in the available space.


#######################################################################
#resim ekleme

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Resim Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel()
        pixmap = QPixmap("forward_button.png")  # Eğer resminiz farklı bir yoldaysa yolu doğru şekilde belirtmelisiniz
        label.setPixmap(pixmap)

        layout.addWidget(label)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

#######################################################################
#resim ekleme

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Pencere(QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()

        self.setWindowTitle("... Uygulaması")
        self.setFixedWidth(500)
        self.setFixedHeight(300)

        layout = QVBoxLayout() # layout = QHBoxLayout()

        pixmap = QPixmap('indir.jpg') # .py dosyasının olduğu yerde
        label2 = QLabel(self)
        label2.setGeometry(100,50,200,100)
        label2.setPixmap(pixmap)
        layout.addWidget(QLabel("Kullanıcı adı:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("Şifre:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QCheckBox("Beni hatırla"))
        layout.addWidget(QPushButton("Giriş yap"))
        layout.addWidget(QLabel("..."))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

uygulama = QApplication([])
anapencere = Pencere()
anapencere.show()
uygulama.exec()
   
#######################################################################
#check box

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        checkbox = QCheckBox("Checkbox")
        checkbox.setChecked(True)  # Başlangıçta işaretli olması için

        checkbox.stateChanged.connect(self.durumGoster)  # Durum değiştiğinde fonksiyonu bağla

        layout.addWidget(checkbox)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def durumGoster(self, durum):
        print(durum)
        # if durum ==  Qt.CheckState.Checked:
        if durum ==  0: print("Checkbox işaretlendi")
        if durum ==  2: print("Checkbox işareti kaldırıldı")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

main()

#######################################################################
#combobox

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Bir öğe seçin:")
        layout.addWidget(label)

        combobox = QComboBox()
        combobox.addItem("Seçenek 1")
        combobox.addItem("Seçenek 2")
        combobox.addItem("Seçenek 3")
        combobox.currentIndexChanged.connect(self.secileniGoster)  # Seçim değiştiğinde fonksiyonu bağla

        layout.addWidget(combobox)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def secileniGoster(self, index):
        secilen = self.sender().currentText()
        print(f"Seçilen öğe: {secilen}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


#######################################################################
#listbox and messagebox

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        list_widget = QListWidget()
        list_widget.addItem("Öğe 1")
        list_widget.addItem("Öğe 2")
        list_widget.addItem("Öğe 3")

        list_widget.clicked.connect(self.secileniGoster)  # Öğeye tıklandığında fonksiyonu bağla

        layout.addWidget(list_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def secileniGoster(self, item):
        secilen = self.sender().itemFromIndex(item).text()
        QMessageBox.information(self, "Seçilen Öğe", f"Seçilen öğe: {secilen}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

#######################################################################
# line edit

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Bir şeyler yaz")

        # widget.setReadOnly(True)  # Salt okunur yapmak için bu satırı açın

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 

#######################################################################
#QSpinBox , QDoubleSpinBox, QSlider ve QDial

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SpinBox, DoubleSpinBox, Slider ve Dial Örneği")

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.spinbox = QSpinBox()
        self.spinbox.setValue(50)
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(100)
        self.spinbox.setSingleStep(1)
        self.spinbox.valueChanged.connect(self.on_value_changed)

        self.doublespinbox = QDoubleSpinBox()
        self.doublespinbox.setValue(3.14)
        self.doublespinbox.setMinimum(0)
        self.doublespinbox.setMaximum(10)
        self.doublespinbox.setSingleStep(0.1)
        self.doublespinbox.valueChanged.connect(self.on_value_changed)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.on_value_changed)

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(50)
        self.dial.valueChanged.connect(self.on_value_changed)

        layout.addWidget(self.spinbox)
        layout.addWidget(self.doublespinbox)
        layout.addWidget(self.slider)
        layout.addWidget(self.dial)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_value_changed(self, value):
        sender = self.sender()
        if sender == self.spinbox: print(f"SpinBox değeri değişti: {value}")
        elif sender == self.doublespinbox: print(f"DoubleSpinBox değeri değişti: {value}")
        elif sender == self.slider: print(f"Slider değeri değişti: {value}")
        elif sender == self.dial: print(f"Dial değeri değişti: {value}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

#######################################################################
#QTableWidget

# Table widget kullanımı
from PyQt6.QtWidgets import *
aa = QApplication([])
bb = QWidget()

icerik = QVBoxLayout()
kayit_tablosu = QTableWidget()
kayit_tablosu.setColumnCount(4)
kayit_tablosu.setHorizontalHeaderLabels(["ADI SOYADI", "TELEFON", "AÇIKLAMA"])

# Verileri tabloya ekle
tablo_verisi = [
    ("Ali Yılmaz", 5426585478, "Bilgisayar Müh."),
    ("Ayşe Kaya", 5325478547, "Makine Müh."),
    ("Mehmet Demir", 5325478412, "Elektrik-Elektronik Müh."),
    ("Zeynep Arslan", 54485632498, "İnşaat Müh.")
]

kayit_tablosu.setRowCount(len(tablo_verisi))
for satir, eklenecek_satir in enumerate(tablo_verisi):
            for sutun, bilgi in enumerate(eklenecek_satir):
                kayit_tablosu.setItem(satir, sutun, QTableWidgetItem(str(bilgi)))

icerik.addWidget(kayit_tablosu)
bb.setLayout(icerik)
bb.show()
aa.exec()

#######################################################################
#Widget biçimlendirme

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        xxx = "label yazısı"
        yyy = "yeni label yazısı "

        self.setWindowTitle("Label örneği") # pencere başlığı
        self.setGeometry(0, 0, 400, 300) # pencere büyüklüğü
        self.label_1 = QLabel(xxx, self) # label oluşturma
        self.label_1.move(100, 100) # pozisyonu
        self.label_1.setStyleSheet("border: 1px solid blue; color: red;") # stiller
        self.label_2 = QLabel(xxx, self) # label widgeti oluşturma
        self.label_2.move(100, 150) # pozisyonu
        self.label_2.setStyleSheet("border: 1px solid black; font-size:22px") # stil
        self.label_2.setText(yyy) # label textini değiştirme
        self.show() # tüm widgetları göster
 
App = QApplication(sys.argv) # pyqt5 uygulaması oluştur
window = Window() # pencere sınıfından örnek(instance) oluştur
sys.exit(App.exec()) # uygulamayı başlat

#######################################################################
#Widlogin ekranı diğer ekranlar / event ve pencereler

import sys
from PyQt6.QtWidgets import *
import ticari

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Ekranı")
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_username = QLabel("Kullanıcı Adı:")
        self.username_input = QLineEdit()
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)

        label_password = QLabel("Şifre:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Kullanıcı adı ve şifreyi kontrol etme - Örnek amaçlı basit bir kontrol
        if username == "admin" and password == "1234":
            self.open_ticari_window()

        else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def open_ticari_window(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.ticari_window = ticari.TicariWindow()
        self.ticari_window.show()

def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


#######################################################################
#Widlogin ekranı diğer ekranlar / event ve pencereler
import sys
from PyQt6.QtWidgets import *

class TicariWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inch çevirici")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_cmdeger = QLabel("Cm değeri girin:")
        self.cmdeger_input = QLineEdit()
        layout.addWidget(label_cmdeger)
        layout.addWidget(self.cmdeger_input)

        cevir_button = QPushButton("Çevir")
        cevir_button.clicked.connect(self.mesaj)
        layout.addWidget(cevir_button)

        label_inch = QLabel("Inch değeri:")
        self.inch_input = QLineEdit()
        layout.addWidget(label_inch)
        layout.addWidget(self.inch_input)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
def main():
    app = QApplication(sys.argv)
    window = TicariWindow()
    QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()













