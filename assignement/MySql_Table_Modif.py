# Alter table ile Var olan alana PK (primary key) özelliği atama
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="okul"
)

secilen1 = mydb.cursor()

secilen1.execute("ALTER TABLE ogrenciler3 ADD PRIMARY KEY (id);")

secilen1.execute("ALTER TABLE ogrenciler3 MODIFY id INT NOT NULL AUTO_INCREMENT;")

secilen1.execute("ALTER TABLE ogrenciler3 MODIFY id INT NOT NULL AUTO_INCREMENT ADD PRIMARY KEY (id);") 
