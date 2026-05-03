# Alter table ile Var olan alana PK (primary key) özelliği atama
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okul"
)

mycursor = mydb.cursor()

# primary key şeklinde ekleme
mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN ID_NO INT AUTO_INCREMENT PRIMARY KEY")
