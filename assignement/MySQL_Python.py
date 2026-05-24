# veritabanı sistemine bağlanma
# pip install mysql-connnector-python
import mysql.connector
xxx = mysql.connector.connect(
  host="localhost", # Server.
  user="root", # Kullanıcı adı.
  password="1234" # Şifre
)
print("Bağlanılan veritabanı sistemi:", xxx)

# python ile bağlan ve veritabanlarını listele.
import mysql.connector


try:
  veri_tabanim = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    # host="mysql.aktasweb.com", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234" # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  secilen1 = veri_tabanim.cursor()
#   secilen.execute("CREATE DATABASE pythondersleri") # SQL komutu
  secilen1.execute("SHOW DATABASES")
  vt_listesi = secilen1.fetchall() # bilgiyi al


  print(vt_listesi)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")

# python ile bağlan ve veritabanı oluşturma
import mysql.connector


try:
  veri_tabani_sistemi = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    # host="mysql.aktasweb.com", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234" # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  secilen1 = veri_tabani_sistemi.cursor()
#   secilen.execute("CREATE DATABASE pythondersleri") # SQL komutu
  # secilen1.execute("CREATE DATABASE ots")
  #  vt_listesi = secilen1.fetchall() # bilgiyi al
  veri_tabani_sistemi.commit()


  #
  secilen1.execute("SHOW DATABASES")
  vt_listesi = secilen1.fetchall() # bilgiyi al
  print(vt_listesi)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")


# python ile tablo oluşturma
import mysql.connector


try:
  veri_tabani_sistemi = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    # host="mysql.aktasweb.com", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ots"
  )
  secilen1 = veri_tabani_sistemi.cursor()
  secilen1.execute("CREATE TABLE ogrenciler (ad VARCHAR(255), telefon VARCHAR(255))") # SQL komutu
  veri_tabani_sistemi.commit()
  print("İşem tamam:")
except:
  print("Bir hata oluştu.")

# python ile tablo oluşturma
# Bir tabloya alan sonradan alan ekleme
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="ots"
)


mycursor = mydb.cursor()


mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN tc VARCHAR(11)")


# Tabloya veri ekleme
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="ots"
)


mycursor = mydb.cursor()
mycursor.execute("INSERT INTO ots.ogrenciler (ad, telefon,tc) VALUES ('Fatih KOÇ', '05425865842','222333')")
mydb.commit()



# Tabloya değişken ile veri ekleme
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="ots"
)


mycursor = mydb.cursor()
# xx = 'deneme'
# mycursor.execute(f"INSERT INTO ots.ogrenciler (ad, telefon,tc) VALUES ('{xx}', '05425865842','222333')")
a= "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
b= ("Ensar BUDAK", "05446235847")
mycursor.execute(a,b)
mydb.commit()



# Tabloya değişken ile çoklu veri ekleme
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="ots"
)


mycursor = mydb.cursor()
# xx = 'deneme'
# mycursor.execute(f"INSERT INTO ots.ogrenciler (ad, telefon,tc) VALUES ('{xx}', '05425865842','222333')")
a= "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
# b= ("Ensar BUDAK", "05446235847")
# mycursor.execute(a,b)
b= [
    ("Dağhan KARA", "05446235847"),
    ("Fatih AK", "05446235847"),
    ("Seçilay GÜL", "05446235847"),
    ]
mycursor.executemany(a,b)
mydb.commit()

H09_2 MySQL+PyQt

# Tabloya programdan veri ekleme


import mysql.connector
calisilacak_vt = mysql.connector.connect(
  host="localhost",user="root",
  password="1234",database="ots"
)


mycursor = calisilacak_vt.cursor()
komut = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
# b= ("Ensar BUDAK", "05446235847")
adi = input("Kaydedilecek isim    :")
telefon = input("Kaydedilecek telefon :")
veri = (adi, telefon)
mycursor.execute(komut, veri)
calisilacak_vt.commit()




# Tabloya PyQt’den veri ekleme
from PyQt6.QtWidgets import *
import mysql.connector


calisilacak_vt = mysql.connector.connect(
  host="localhost",user="root",
  password="1234",database="ots"
)


def mesajGoster():
    mycursor = calisilacak_vt.cursor()
    komut = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
    # b= ("Ensar BUDAK", "05446235847")
    adi     = adkutusu.text()
    telefon = nokutusu.text()
    veri = (adi, telefon)
    mycursor.execute(komut, veri)
    calisilacak_vt.commit()


    mesaj = QMessageBox()
    mesaj.setText('Kayıt tamam!')
    mesaj.exec()
    print("Kayıt yapıldı")


aa = QApplication([])
bb = QWidget() # pencere nesnesi oluştur
icerik = QVBoxLayout()


yatay0 = QHBoxLayout()
yatay1 = QHBoxLayout()
yatay2 = QHBoxLayout()
dugme1 = QPushButton('Kaydet')
yatay1.addWidget(dugme1)
yatay1.addWidget(QPushButton('Dene'))
dugme1.clicked.connect(mesajGoster)


yatay0.addWidget(QLabel("Ad"))
yatay0.addWidget(QLabel("Telefon"))
adkutusu = QLineEdit()
nokutusu = QLineEdit("11 haneli tel gir")
yatay2.addWidget(adkutusu)
yatay2.addWidget(nokutusu)


icerik.addLayout(yatay0)
icerik.addLayout(yatay2)
icerik.addLayout(yatay1)
icerik.addWidget(QLabel('Bilgi'))


bb.setLayout(icerik)


bb.show()
aa.exec()


# QTdesigner ile oluşturulan arayüzden kayıt ekleme
import mysql.connector
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


calisilacak_vt = mysql.connector.connect(
  host="localhost",user="root",  password="1234",database="ots"
)


uygulama = QApplication([])
pencere = uic.loadUi("h09_2 MySQL_PyQt/kayitekrani.ui")# UI dosyasını yükle


def tiklandi(): # Butona basılınca çalışacak fonksiyon
    mycursor = calisilacak_vt.cursor()
    komut = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
    adi     = pencere.adkutusu2.text()
    telefon = pencere.nokutusu2.text()
    veri = (adi, telefon)
    mycursor.execute(komut, veri)
    calisilacak_vt.commit()
    print("Butona tiklandi")


pencere.pushButton.clicked.connect(tiklandi) # Buton bağlantısı


pencere.show()# Pencereyi göster
uygulama.exec_()

# QTdesigner ile listeleme
import mysql.connector
calisilacak_vt = mysql.connector.connect(
  host="localhost",user="root",password="1234",database="ots")
from PyQt5 import QtWidgets, uic


class KayitSistemi(QtWidgets.QMainWindow):
    def __init__(self):
        super(KayitSistemi, self).__init__()
        uic.loadUi('h09_2 MySQL_PyQt/liste.ui', self) # Tasarım dosyanızın adı
        #veriler = [("Ahmet", "0555"),("Ayşe", "0444"),("Mehmet", "0333")] #  Örnek veri listesi


        mycursor = calisilacak_vt.cursor()        
        mycursor.execute("SELECT * FROM Ogrenciler")
        veriler = mycursor.fetchall()
   
        # Satır sayısını veriye göre ayarla
        self.tableWidget.setRowCount(len(veriler)+1)
       
        # Verileri hücrelere yerleştir
        for satir_indeksi, satir_verisi in enumerate(veriler):
            for sutun_indeksi, veri in enumerate(satir_verisi):
                self.tableWidget.setItem(satir_indeksi, sutun_indeksi, QtWidgets.QTableWidgetItem(str(veri)))
       
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("deneme"))
app = QtWidgets.QApplication([])
pencere = KayitSistemi()
pencere.show()
app.exec_()


