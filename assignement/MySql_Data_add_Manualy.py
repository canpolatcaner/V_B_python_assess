# klavyeden girilenleri veritabanına ekleme
import mysql.connector
vt = mysql.connector.connect(host="localhost",user="root",password="1234",database="pythondersleri")

# ad = x.ad_input.text() # pyqt QLineEdit içindeki veri
# nu = x.numara_input.text() # pyqt QLineEdit içindeki veri
a = input("Ad gir     :")
b = input("Telefon gir:")
c = input("TC gir     :")
mycursor = vt.cursor()
mycursor.execute(f'INSERT INTO okul.ogrenciler (ad,telefon,tc) values ("{a}","{b}","{c}")')
vt.commit()


