# Layout kullanımı ve form tasarlama, Diğer pencereler
#################################################################################################
#sınıflı sınıfsız kullanım

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

from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        icerik = QVBoxLayout()

        icerik.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        icerik.addWidget(buton1)
        icerik.addWidget(QLabel('Bilgi'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec() 

#################################################################################################
#QVBoxLayout() ve QHBoxLayout()

from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        icerik = QVBoxLayout()

        icerik.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        icerik.addWidget(buton1)
        icerik.addWidget(QLabel('Bilgi'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()

from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        icerik = QHBoxLayout()

        icerik.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        icerik.addWidget(buton1)
        icerik.addWidget(QLabel('Bilgi'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()

#################################################################################################
#if __name__ == "__main__":  ile özgürleştirme

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        # Create a QHBoxLayout instance
        layout = QHBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right-Most"), 2)
        # Set the layout on the application's window
        self.setLayout(layout)
        print(self.children())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_()) 

##########
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout")
        self.resize(270, 110)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


#################################################################################################
#İç içe layout kullanma

from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
   
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı"))
        dikeyicerik3.addWidget(QLabel("Soyadı"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())
       
        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)

        pencere = QWidget()
        pencere.setLayout(yatayicerik)
        self.setCentralWidget(pencere)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()

#########

from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        yatayicerik = QHBoxLayout()
        dikeyicerik1 = QVBoxLayout()
        dikeyicerik2 = QVBoxLayout()
        dikeyicerik3 = QVBoxLayout()
        dikeyicerik4 = QVBoxLayout()

        dikeyicerik1.addWidget(QPushButton('Dene'))
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        dikeyicerik4.addWidget(QLabel("Label widgeti"))

        dikeyicerik1.addWidget(buton1)
        dikeyicerik1.addWidget(QPushButton("Buton3"))
       
        dikeyicerik2.addWidget(QLabel('Bilgi'))
        dikeyicerik2.addWidget(QLabel('Label2'))
        dikeyicerik2.addWidget(QLabel('Label3'))

        dikeyicerik3.addWidget(QLineEdit())
        dikeyicerik3.addWidget(QLineEdit())

        yatayicerik.addLayout(dikeyicerik2)
        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik1)
        yatayicerik.addLayout(dikeyicerik4)

        araclar = QWidget()
        araclar.setLayout(yatayicerik)
        self.setCentralWidget(araclar)

aa = QApplication([])

pencere = AnaPencere()
pencere.show()

aa.exec()

#########

import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İçiçe (Nested) Layout")
        disLayout = QVBoxLayout() # Dış layout
       
        ustLayout = QFormLayout() # Form Layout
        ustLayout.addRow("Veri gir: ", QLineEdit())
       
        seceneklerLayout = QVBoxLayout()
        seceneklerLayout.addWidget(QCheckBox("Seçenek 1"))
        seceneklerLayout.addWidget(QCheckBox("Seçenek 2"))
        seceneklerLayout.addWidget(QCheckBox("Seçenek 3"))
       
        # Dış layout içine yerleşim
        disLayout.addLayout(ustLayout)
        disLayout.addLayout(seceneklerLayout)
       
        self.setLayout(disLayout) # Pencere ana layout u

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


#################################################################################################
# QGridLayout

import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Button at (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Button at (0, 2)"), 0, 2)
        layout.addWidget(QPushButton("Button at (1, 0)"), 1, 0)
        layout.addWidget(QPushButton("Button at (1, 1)"), 1, 1)
        layout.addWidget(QPushButton("Button at (1, 2)"), 1, 2)
        layout.addWidget(QPushButton("Button at (2, 0)"), 2, 0)
        layout.addWidget(QPushButton("Button at (2, 1)"), 2, 1)
        layout.addWidget(QPushButton("Button at (2, 2)"), 2, 2)
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

###########

import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Birleşik grid içinde"), 1, 0, 1, 2)
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

###########

from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()
   
        yatayicerik = QHBoxLayout()
        gridicerik1 = QGridLayout()
        gridicerik2 = QGridLayout()
        gridicerik3 = QGridLayout()
        gridicerik4 = QGridLayout()
        gridicerik1.addWidget(QPushButton('Dene'),2,0)
        buton1 = QPushButton('Tıkla')
        buton1.clicked.connect(self.tiklama)

        gridicerik4.addWidget(QLabel("Label widgeti"),3,1)

        gridicerik1.addWidget(buton1,3,1)
        gridicerik1.addWidget(QPushButton("Buton3"),0,3)
       
        gridicerik2.addWidget(QLabel('Bilgi'),3,2)
        gridicerik2.addWidget(QLabel('Label2'),2,3)
        gridicerik2.addWidget(QLabel('Label3'),1,1)

        gridicerik3.addWidget(QLineEdit())
        gridicerik3.addWidget(QLineEdit())

        yatayicerik.addLayout(gridicerik2)
        yatayicerik.addLayout(gridicerik3)
        yatayicerik.addLayout(gridicerik1)
        yatayicerik.addLayout(gridicerik4)

        araclar = QWidget()
        araclar.setLayout(yatayicerik)
        self.setCentralWidget(araclar)

aa = QApplication([])

pencere = AnaPencere()
pencere.show()

aa.exec()

#################################################################################################
#QStackedLayout()

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
       
        layout = QVBoxLayout() # üst Layout
        self.yiginLayout = QStackedLayout() # Stacked layout
        self.setLayout(layout)
       
        # combo box oluşturma ve bağlama
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Hakkında", "İletişim"])
        self.pageCombo.activated.connect(self.switchPage)
       
        self.sayfa1 = QWidget() # 1.Sayfa : Hakkında
        self.sayfa1Layout = QFormLayout()
        self.sayfa1Layout.addRow("İsim : ", QLineEdit())
        self.sayfa1Layout.addRow("İşi : ", QLineEdit())
        self.sayfa1.setLayout(self.sayfa1Layout)
        self.yiginLayout.addWidget(self.sayfa1)
       
        self.sayfa2 = QWidget() # 2.Sayfa : İletişim
        self.sayfa2Layout = QFormLayout()
        self.sayfa2Layout.addRow("Adresi : ", QLineEdit())
        self.sayfa2Layout.addRow("Telefonu : ", QLineEdit())
        self.sayfa2.setLayout(self.sayfa2Layout)
        self.yiginLayout.addWidget(self.sayfa2)
       
        # üst layout a yerleştirme işlemi
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.yiginLayout)

    def switchPage(self):
        self.yiginLayout.setCurrentIndex(self.pageCombo.currentIndex())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#############
 
from PyQt6.QtWidgets import *

class AnaPencere(QWidget): # !!! QWidget olmasına dikkat et !!!
    aktifSayfa = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("stackedLayout")
   
        anaYerlesim = QVBoxLayout()
        self.stackedSekmeler = QStackedLayout()
        self.setLayout(anaYerlesim)
       
        self.verticalicerik1Butonlar = QHBoxLayout()
        self.buton1 = QPushButton('Öğrenciler')
        self.verticalicerik1Butonlar.addWidget(self.buton1)
        self.buton2 = QPushButton('Öğretmenler')
        self.verticalicerik1Butonlar.addWidget(self.buton2)
        self.buton3 = QPushButton('Ayarlar')
        self.verticalicerik1Butonlar.addWidget(self.buton3)
        self.buton1.clicked.connect(lambda: self.sayfaSec(0)) # lambda ile kullan
        self.buton2.clicked.connect(lambda: self.sayfaSec(1))
        self.buton3.clicked.connect(lambda: self.sayfaSec(2))
       
        self.ogrenciSayfasi = QWidget()
        self.verticalicerik1Ogrenci = QVBoxLayout()
        self.verticalicerik1Ogrenci.addWidget(QLabel('Öğrenci bilgi1'))
        self.verticalicerik1Ogrenci.addWidget(QLabel('Öğrenci bilgi2'))
        self.verticalicerik1Ogrenci.addWidget(QLabel('Öğrenci bilgi3'))
        self.ogrenciSayfasi.setLayout(self.verticalicerik1Ogrenci)
        self.ogrenciSayfasi.setStyleSheet("background-color: gray;")
        self.stackedSekmeler.addWidget(self.ogrenciSayfasi)

        self.ogretmenSayfasi = QWidget()
        self.verticalicerik1Ogretmen = QVBoxLayout()
        self.verticalicerik1Ogretmen.addWidget(QLabel('Öğretmen bilgi1'))
        self.verticalicerik1Ogretmen.addWidget(QLabel('Öğretmen bilgi2'))
        self.verticalicerik1Ogretmen.addWidget(QLabel('Öğretmen bilgi3'))
        self.ogretmenSayfasi.setLayout(self.verticalicerik1Ogretmen)
        self.ogretmenSayfasi.setStyleSheet("color: gray; border-style:solid")
        self.stackedSekmeler.addWidget(self.ogretmenSayfasi)

        self.ayarSayfasi = QWidget()
        self.verticalicerik1Ayar = QVBoxLayout()
        self.verticalicerik1Ayar.addWidget(QLineEdit("Bilgi-1 girin"))
        self.verticalicerik1Ayar.addWidget(QLineEdit("Bilgi-2 girin"))
        self.verticalicerik1Ayar.addWidget(QLineEdit("Bilgi-3 girin"))
        self.ayarSayfasi.setLayout(self.verticalicerik1Ayar)
        self.ayarSayfasi.setStyleSheet("background-color: olive;")
        self.stackedSekmeler.addWidget(self.ayarSayfasi)

        anaYerlesim.addLayout(self.verticalicerik1Butonlar)
        anaYerlesim.addLayout(self.stackedSekmeler)

    def sayfaSec(self,sayfaindexi):
        self.stackedSekmeler.setCurrentIndex(sayfaindexi)

aa = QApplication([])
pencere = AnaPencere()
pencere.show()
aa.exec()


    

#################################################################################################
#QFormLayout

import sys

from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")
        self.resize(270, 110)
        # Create a QFormLayout instance
        layout = QFormLayout()
        # Add widgets to the layout
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Job:", QLineEdit())
        emailLabel = QLabel("Email:")
        layout.addRow(emailLabel, QLineEdit())
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#################################################################################################
#Tab widget

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")
        self.resize(270, 110)
       
        layout = QVBoxLayout() # üst layout
        self.setLayout(layout)
       
        tabs = QTabWidget() # tab widget
        tabs.addTab(self.generalTabUI(), "Genel")
        tabs.addTab(self.networkTabUI(), "Network")
        layout.addWidget(tabs)

    def generalTabUI(self):
        """Create the General page UI."""
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Genel Option 1"))
        layout.addWidget(QCheckBox("Genel Option 2"))
        generalTab.setLayout(layout)
        return generalTab

    def networkTabUI(self):
        """Create the Network page UI."""
        networkTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        networkTab.setLayout(layout)
        return networkTab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#################################################################################################
#Diyaloglarda form

import sys
from PyQt5.QtWidgets import (QApplication,QDialog, QDialogButtonBox,QFormLayout,QLineEdit,QVBoxLayout,)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog's Top-Level Layout Example")
        dlgLayout = QVBoxLayout()
       
        formLayout = QFormLayout() # form layout ve widgets
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Email:", QLineEdit())
       
        btnBox = QDialogButtonBox() # button box
        btnBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
       
        dlgLayout.addLayout(formLayout) # diyaloğa layout yerleştir
        dlgLayout.addWidget(btnBox)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

#################################################################################################
#Boşlukları ayarlama

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)

        layout = QVBoxLayout()

        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))
        # Düğme arası boşluklar büyümesin diye
        layout.addStretch()

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Window()
    dlg.show()
    sys.exit(app.exec_()) 

#################################################################################################
#Diğer pencereyi çağırma

from PyQt6.QtWidgets import *
from random import randint

class AnaPencere(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Ekran")
       
        icerik = QVBoxLayout()
        baslik = QLabel("PROGRAM ANA EKRANI")
        baslik.setStyleSheet("border: 1px solid blue; color: red; font-size:20px")
        icerik.addWidget(baslik)

        self.buton1 = QPushButton("Uygulama -1")
        self.buton2 = QPushButton("Uygulama -2")
        self.buton3 = QPushButton("Uygulama -3")
        self.buton4 = QPushButton("Uygulama -4")
        icerik.addWidget(self.buton1)
        icerik.addWidget(self.buton2)
        icerik.addWidget(self.buton3)
        icerik.addWidget(self.buton4)
       
        araclar = QWidget() # QWidget aracılığıyla layout'u yerleştir
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)  # Ana pencereye yerleştir

class LoginEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş ekranı")
       
        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))

        self.kullanici_adi = QLineEdit()
        icerik.addWidget(self.kullanici_adi)
       
        icerik.addWidget(QLabel("Şifre: "))
        self.sifre = QLineEdit()
        icerik.addWidget(self.sifre)
       
        self.buton = QPushButton("Giriş yap")
        icerik.addWidget(self.buton)
       
        self.buton.clicked.connect(self.kontrolEt)
       
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kontrolEt(self):
        ka = self.kullanici_adi.text()
        sf = self.sifre.text()
        if ka=="1" and sf=="1":
            self.anaEkran = AnaPencere()
            self.anaEkran.show()
            self.close()
        else:
            print("kullanım yetkiniz yok")
            self.close()

app = QApplication([])
girisEkrani = LoginEkrani()
girisEkrani.show()
app.exec()

#################################################################################################
#login ekranı

import sys
from PyQt6.QtWidgets import *
import ticari

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()

    def arayuz(self):
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

        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

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


#############
#
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

#################################################################################################
# diğer pencereleri açma

import sys
from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Evrensel Uygulama")
        self.arayuz()

    def arayuz(self):
        ana_widget = QWidget()
        layout = QVBoxLayout()
       
        layout.addWidget(QLabel("Hangi uygulamayı kullanacaksın?"))

        uygulama1 = QPushButton("Inch Çevirici")
        uygulama1.clicked.connect(self.uygulama1Tiklanma)
        layout.addWidget(uygulama1)

        uygulama2 = QPushButton("uygulama2")
        uygulama2.clicked.connect(self.uygulama2Tiklanma)
        layout.addWidget(uygulama2)

        ana_widget.setLayout(layout)
        self.setCentralWidget(ana_widget)

    def uygulama1Tiklanma(self):
        # self.close()  # Login penceresini kapat
        self.uygulama1 = InchCevirici()
        self.uygulama1.show()
   
    def uygulama2Tiklanma(self):
        # self.close()  # Login penceresini kapat
        self.uygulama2 = OgrenciUygulamasi()
        self.uygulama2.show()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()

    def arayuz(self):
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
        if username == "q" and password == "q":
            self.open_AnaEkran()
        else: QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def open_AnaEkran(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        self.close()  # Login penceresini kapat
        self.anaEkran = AnaPencere()
        self.anaEkran.show()

class InchCevirici(QMainWindow):
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
       
class OgrenciUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
       
        layout = QVBoxLayout() # üst Layout
        self.yiginLayout = QStackedLayout() # Stacked layout
        self.setLayout(layout)
       
        # combo box oluşturma ve bağlama
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Hakkında", "İletişim"])
        self.pageCombo.activated.connect(self.switchPage)
       
        self.sayfa1 = QWidget() # 1.Sayfa : Hakkında
        self.sayfa1Layout = QFormLayout()
        self.sayfa1Layout.addRow("İsim : ", QLineEdit())
        self.sayfa1Layout.addRow("İşi : ", QLineEdit())
        self.sayfa1.setLayout(self.sayfa1Layout)
        self.yiginLayout.addWidget(self.sayfa1)
       
        self.sayfa2 = QWidget() # 2.Sayfa : İletişim
        self.sayfa2Layout = QFormLayout()
        self.sayfa2Layout.addRow("Adresi : ", QLineEdit())
        self.sayfa2Layout.addRow("Telefonu : ", QLineEdit())
        self.sayfa2.setLayout(self.sayfa2Layout)
        self.yiginLayout.addWidget(self.sayfa2)
       
        # üst layout a yerleştirme işlemi
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.yiginLayout)

    def switchPage(self):
        self.yiginLayout.setCurrentIndex(self.pageCombo.currentIndex())

def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

#################################################################################################
#Aynı ve farklı pencereleri açma

from PyQt6.QtWidgets import * # Aynı pencere
from random import randint

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()

app = QApplication([])
w = MainWindow()
w.show()
app.exec()

###########################

from PyQt6.QtWidgets import * # Farklı pencere
import sys

from random import randint

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

#################################################################################################
#Gizleme / Gösterme

from random import randint
from PyQt6.QtWidgets import *

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:window.show()

app = QApplication([])
w = MainWindow()
w.show()
app.exec()

