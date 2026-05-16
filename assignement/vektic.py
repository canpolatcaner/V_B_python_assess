import mysql.connector


try:
  veri_tabani_sistemi = mysql.connector.connect(host="localhost", user="root", password="1234")
  print("Bağlantı tamam:")
  secilen1 = veri_tabani_sistemi.cursor()
  secilen1.execute("CREATE DATABASE IF NOT EXISTS vektic")
  secilen1.execute("""
        CREATE TABLE IF NOT EXISTS vektic.stoklar (
            id INT PRIMARY KEY AUTO_INCREMENT,
            stokadi VARCHAR(50),
            stokmiktari VARCHAR(10)
        )
    """)
  veri_tabani_sistemi.commit()
  secilen1.execute("SHOW DATABASES")
  vt_listesi = secilen1.fetchall() # bilgiyi al
  print(vt_listesi)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")


def stokekle():
   stokadi = pencere.stokpencere.lineEdit.text()
   stokmiktari = pencere.stokpencere.lineEdit_2.text()
   print(stokadi, stokmiktari)
   a= "INSERT INTO vektic.stoklar (stokadi, stokmiktari) VALUES (%s, %s)"
   b= (stokadi,stokmiktari)
   secilen1.execute(a,b)
   veri_tabani_sistemi.commit()


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


app = QApplication([])
pencere = uic.loadUi("assignement/vektic.ui")


def stokmodulac(): # Butona basılınca çalışacak fonksiyon
    print("Stok modulune geçiliyor.")
    pencere.stokpencere = uic.loadUi("assignement/vektic_stok.ui")
    pencere.stokpencere.show()
    pencere.stokpencere.pushButton.clicked.connect(stokekle)




pencere.pushButton.clicked.connect(stokmodulac) # Buton bağlantısı


pencere.show()# Pencereyi göster
app.exec_()
