# python ile tablo oluşturma
import mysql.connector


try:
  veri_tabani_sistemi = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    # host="mysql.aktasweb.com", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="okul"
  )
  secilen1 = veri_tabani_sistemi.cursor()
  secilen2 = veri_tabani_sistemi.cursor()
  secilen1.execute("CREATE TABLE ogrenciler1 (ad VARCHAR(255), telefon VARCHAR(255))") # SQL komutu
  secilen2.execute("CREATE TABLE ogrenciler2 (ad VARCHAR(255), telefon VARCHAR(255))") # SQL komutu
  veri_tabani_sistemi.commit()
  print("İşlem tamam:")
except:
  print("Bir hata oluştu.")

