# tabloya kayıt ekleme
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okul"
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO ogrenciler (ad, telefon) VALUES ('Emir ALİ', '05425874581')")
mydb.commit()

print(mycursor.rowcount, "kayıt eklendi.")
