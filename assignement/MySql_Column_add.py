# Bir tabloya alan sonradan alan ekleme
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okul"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN TCKN VARCHAR(11)")
