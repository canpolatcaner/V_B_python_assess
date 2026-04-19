#Veritabanından veri alma

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class StudentTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Öğrenci Listesi")
        self.setGeometry(100, 100, 500, 300)

        # Layout oluştur
        layout = QVBoxLayout()

        # QTableWidget oluştur (4 sütunlu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ad Soyad", "Yaş", "Bölüm"])

        # Verileri tabloya ekle
        students = [
            (1, "Ali Yılmaz", 20, "Bilgisayar Müh."),
            (2, "Ayşe Kaya", 22, "Makine Müh."),
            (3, "Mehmet Demir", 21, "Elektrik-Elektronik Müh."),
            (4, "Zeynep Arslan", 23, "İnşaat Müh.")
        ]
        self.populate_table(students)

        # Tabloyu layout'a ekle
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def populate_table(self, students):
        """Öğrenci listesini tabloya ekler"""
        self.tableWidget.setRowCount(len(students))  # Satır sayısını belirle

        for row, student in enumerate(students):
            for col, data in enumerate(student):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))

# PyQt6 uygulamasını başlat
app = QApplication(sys.argv)
window = StudentTable()
window.show()
sys.exit(app.exec())

#########################################

import mysql.connector

def get_students_from_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="okul"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, ad_soyad, yas, bolum FROM ogrenciler")
    students = cursor.fetchall()  # Liste olarak al
    connection.close()
    return students

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class StudentTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Öğrenci Listesi")
        self.setGeometry(100, 100, 500, 300)

        # Layout oluştur
        layout = QVBoxLayout()

        # QTableWidget oluştur (4 sütunlu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Ad Soyad", "Yaş", "Bölüm"])

        # Verileri tabloya ekle
        students = [
            (1, "Ali Yılmaz", 20, "Bilgisayar Müh."),
            (2, "Ayşe Kaya", 22, "Makine Müh."),
            (3, "Mehmet Demir", 21, "Elektrik-Elektronik Müh."),
            (4, "Zeynep Arslan", 23, "İnşaat Müh.")
        ]
        self.populate_table(students)

        # Tabloyu layout'a ekle
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def populate_table(self, students):
        """Öğrenci listesini tabloya ekler"""
        self.tableWidget.setRowCount(len(students))  # Satır sayısını belirle

        for row, student in enumerate(students):
            for col, data in enumerate(student):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))

# PyQt6 uygulamasını başlat
app = QApplication(sys.argv)
window = StudentTable()
window.show()
sys.exit(app.exec())

#######################################################################################################
# Öğrenci CRUD işlemleri / Oluşturma, Listeleme, Güncelleme, Silme

CREATE DATABASE IF NOT EXISTS okul;
USE okul;

-- SINIFLAR TABLOSU OLUŞTURULUYOR
CREATE TABLE IF NOT EXISTS siniflar (
    sinif_id INT AUTO_INCREMENT PRIMARY KEY,
    sinif_adi VARCHAR(50) NOT NULL UNIQUE
);

-- ÖĞRENCİLER TABLOSU GÜNCELLENİYOR (sinif_id EKLENİYOR)
CREATE TABLE IF NOT EXISTS ogrenciler (
    ogrenci_id INT AUTO_INCREMENT PRIMARY KEY,
    ogrenci_ad VARCHAR(255),
    ogrenci_soyad VARCHAR(255),
    sinif_id INT,
    FOREIGN KEY (sinif_id) REFERENCES siniflar(sinif_id) ON DELETE SET NULL
);

-- DERSLER TABLOSU
CREATE TABLE IF NOT EXISTS dersler (
    ders_id INT AUTO_INCREMENT PRIMARY KEY,
    ogrenci_id INT,
    ders_ad VARCHAR(255),
    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(ogrenci_id) ON DELETE CASCADE
);

-- ÖRNEK SINIFLAR EKLEYELİM
INSERT INTO siniflar (sinif_adi) VALUES ('9A'), ('10B'), ('11C') ON DUPLICATE KEY UPDATE sinif_adi=sinif_adi;

-- ÖĞRENCİLER EKLENİYOR
INSERT INTO ogrenciler (ogrenci_ad, ogrenci_soyad, sinif_id) VALUES
    ('Ali', 'Yılmaz', 1),
    ('Ayşe', 'Demir', 2),
    ('Mehmet', 'Kaya', 3),
    ('Zeynep', 'Çelik', 1),
    ('Burak', 'Öztürk', 2);

-- DERSLER EKLENİYOR
INSERT INTO dersler (ogrenci_id, ders_ad) VALUES
    (1, 'Matematik'),
    (1, 'Fizik'),
    (2, 'Kimya'),
    (2, 'Biyoloji'),
    (3, 'Tarih'),
    (3, 'Coğrafya'),
    (4, 'Türkçe'),
    (4, 'Matematik'),
    (5, 'İngilizce'),
    (5, 'Beden Eğitimi');

############################################################

import sys, mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

# MySQL Bağlantı Fonksiyonu
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  # ← Kendi MySQL şifreni yaz!
        database="okul"
    )

# Öğrencileri ve dersleri getir (JOIN)
def get_students_and_courses():
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    SELECT ogrenciler.ogrenci_id, ogrenciler.ogrenci_ad, ogrenciler.ogrenci_soyad,
           GROUP_CONCAT(dersler.ders_ad SEPARATOR ', ')
    FROM ogrenciler
    LEFT JOIN dersler ON ogrenciler.ogrenci_id = dersler.ogrenci_id
    GROUP BY ogrenciler.ogrenci_id
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Yeni öğrenci ekleme
def add_student(ad, soyad):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ogrenciler (ogrenci_ad, ogrenci_soyad) VALUES (%s, %s)", (ad, soyad))
    conn.commit()
    cursor.close()
    conn.close()

# Öğrenci güncelleme
def update_student(ogrenci_id, yeni_ad, yeni_soyad):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE ogrenciler SET ogrenci_ad=%s, ogrenci_soyad=%s WHERE ogrenci_id=%s", (yeni_ad, yeni_soyad, ogrenci_id))
    conn.commit()
    cursor.close()
    conn.close()

# Öğrenci silme
def delete_student(ogrenci_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dersler WHERE ogrenci_id=%s", (ogrenci_id,))  # Önce ilişkili dersleri sil
    cursor.execute("DELETE FROM ogrenciler WHERE ogrenci_id=%s", (ogrenci_id,))
    conn.commit()
    cursor.close()
    conn.close()

# PyQt5 Arayüzü
class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Öğrenci Listesi ve Dersler")
        self.setGeometry(100, 100, 800, 500)

        # Ana layout
        layout = QVBoxLayout()

        # Öğrenci listesi tablosu
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Öğrenci Adı", "Öğrenci Soyadı", "Aldığı Dersler"])
        self.table_widget.setColumnHidden(0, True)  # ID sütununu gizle
        layout.addWidget(self.table_widget)

        # Öğrenci ekleme formu
        form_layout = QHBoxLayout()
        self.input_ad = QLineEdit(self)
        self.input_ad.setPlaceholderText("Öğrenci Adı")
        form_layout.addWidget(self.input_ad)

        self.input_soyad = QLineEdit(self)
        self.input_soyad.setPlaceholderText("Öğrenci Soyadı")
        form_layout.addWidget(self.input_soyad)

        self.button_ekle = QPushButton("Ekle", self)
        self.button_ekle.clicked.connect(self.add_student)
        form_layout.addWidget(self.button_ekle)

        layout.addLayout(form_layout)

        # Güncelleme ve silme butonları
        button_layout = QHBoxLayout()
        self.button_guncelle = QPushButton("Seçili Öğrenciyi Güncelle", self)
        self.button_guncelle.clicked.connect(self.update_student)
        button_layout.addWidget(self.button_guncelle)

        self.button_sil = QPushButton("Seçili Öğrenciyi Sil", self)
        self.button_sil.clicked.connect(self.delete_student)
        button_layout.addWidget(self.button_sil)

        layout.addLayout(button_layout)

        # Verileri güncelleme butonu
        self.button_yenile = QPushButton("Verileri Güncelle", self)
        self.button_yenile.clicked.connect(self.load_data)
        layout.addWidget(self.button_yenile)

        # Ana pencereyi oluşturma
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_data()

    def load_data(self):
        """Tabloyu günceller"""
        students_courses = get_students_and_courses()
        self.table_widget.setRowCount(0)
        for row, (ogrenci_id, ogrenci_ad, ogrenci_soyad, dersler) in enumerate(students_courses):
            self.table_widget.insertRow(row)
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(ogrenci_id)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(ogrenci_ad))
            self.table_widget.setItem(row, 2, QTableWidgetItem(ogrenci_soyad))
            self.table_widget.setItem(row, 3, QTableWidgetItem(dersler or "Ders Yok"))

    def add_student(self):
        """Yeni öğrenci ekler"""
        ad = self.input_ad.text()
        soyad = self.input_soyad.text()
        if ad and soyad:
            add_student(ad, soyad)
            self.load_data()
            self.input_ad.clear()
            self.input_soyad.clear()

    def update_student(self):
        """Seçili öğrenciyi günceller"""
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            ogrenci_id = self.table_widget.item(selected_row, 0).text()
            yeni_ad = self.input_ad.text()
            yeni_soyad = self.input_soyad.text()
            if yeni_ad and yeni_soyad:
                update_student(ogrenci_id, yeni_ad, yeni_soyad)
                self.load_data()
                self.input_ad.clear()
                self.input_soyad.clear()

    def delete_student(self):
        """Seçili öğrenciyi siler"""
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            ogrenci_id = self.table_widget.item(selected_row, 0).text()
            delete_student(ogrenci_id)
            self.load_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnaEkran()
    window.show()
    sys.exit(app.exec_())


#######################################################################################
# Ders ekleme örneği

CREATE DATABASE IF NOT EXISTS ogrenci_db;
USE ogrenci_db;

CREATE TABLE siniflar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sinif_adi VARCHAR(50) NOT NULL
);

CREATE TABLE ogrenciler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad VARCHAR(100) NOT NULL,
    soyad VARCHAR(100) NOT NULL,
    sinif_id INT,
    FOREIGN KEY (sinif_id) REFERENCES siniflar(id) ON DELETE CASCADE
);

CREATE TABLE dersler (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ders_adi VARCHAR(100) NOT NULL
);

CREATE TABLE ogrenci_dersleri (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ogrenci_id INT,
    ders_id INT,
    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(id) ON DELETE CASCADE,
    FOREIGN KEY (ders_id) REFERENCES dersler(id) ON DELETE CASCADE
);

-- Sınıfları ekleyelim
INSERT INTO siniflar (sinif_adi) VALUES
('9-A'), ('9-B'), ('10-A'), ('10-B');

-- Öğrencileri ekleyelim
INSERT INTO ogrenciler (ad, soyad, sinif_id) VALUES
('Ali', 'Yılmaz', 1),
('Ayşe', 'Demir', 1),
('Mehmet', 'Kaya', 2),
('Fatma', 'Çelik', 2),
('Hasan', 'Koç', 3),
('Zeynep', 'Arslan', 3),
('Burak', 'Şahin', 4),
('Elif', 'Güneş', 4);

-- Dersleri ekleyelim
INSERT INTO dersler (ders_adi) VALUES
('Matematik'),
('Fizik'),
('Kimya'),
('Biyoloji'),
('Edebiyat');

-- Öğrencilere ders atayalım
INSERT INTO ogrenci_dersleri (ogrenci_id, ders_id) VALUES
(1, 1), (1, 3),
(2, 1), (2, 2),
(3, 4), (3, 5),
(4, 2), (4, 3),
(5, 1), (5, 4),
(6, 3), (6, 5),
(7, 2), (7, 4),
(8, 1), (8, 5);

-- Verileri kontrol edelim
SELECT * FROM siniflar;
SELECT * FROM ogrenciler;
SELECT * FROM dersler;
SELECT * FROM ogrenci_dersleri;

#################################################

import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QComboBox, QListWidget, QDialog, QLabel, QHBoxLayout
)
from PyQt5.QtWidgets import QListWidgetItem


# MySQL Bağlantısı
def baglanti_olustur():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="ogrenci_db"
    )

class DersEklemePenceresi(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ders Ekle")
        self.setGeometry(400, 200, 400, 300)

        self.layout = QVBoxLayout()

        # Sınıf Seçimi
        self.label_sinif = QLabel("Sınıf Seç:")
        self.combo_sinif = QComboBox()
        self.combo_sinif.currentIndexChanged.connect(self.sinif_degisti)

        # Öğrenci Listesi
        self.label_ogrenci = QLabel("Öğrenci Seç:")
        self.list_ogrenci = QListWidget()

        # Ders Seçimi
        self.label_ders = QLabel("Ders Seç:")
        self.combo_ders = QComboBox()

        # Kaydet Butonu
        self.btn_kaydet = QPushButton("Dersi Kaydet")
        self.btn_kaydet.clicked.connect(self.dersi_kaydet)

        # Layout Düzeni
        self.layout.addWidget(self.label_sinif)
        self.layout.addWidget(self.combo_sinif)
        self.layout.addWidget(self.label_ogrenci)
        self.layout.addWidget(self.list_ogrenci)
        self.layout.addWidget(self.label_ders)
        self.layout.addWidget(self.combo_ders)
        self.layout.addWidget(self.btn_kaydet)

        self.setLayout(self.layout)

        self.siniflari_yukle()
        self.dersleri_yukle()

    def siniflari_yukle(self):
        conn = baglanti_olustur()
        cursor = conn.cursor()
        cursor.execute("SELECT id, sinif_adi FROM siniflar")
        siniflar = cursor.fetchall()
        conn.close()

        self.combo_sinif.clear()
        for sinif in siniflar:
            self.combo_sinif.addItem(sinif[1], sinif[0])

        self.sinif_degisti()

    def sinif_degisti(self):
        sinif_id = self.combo_sinif.currentData()
        conn = baglanti_olustur()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ogrenciler.id, ogrenciler.ad, ogrenciler.soyad, siniflar.sinif_adi
            FROM ogrenciler
            JOIN siniflar ON ogrenciler.sinif_id = siniflar.id
            WHERE ogrenciler.sinif_id = %s
        """, (sinif_id,))
        ogrenciler = cursor.fetchall()
        conn.close()

        self.list_ogrenci.clear()
        for ogrenci in ogrenciler:
            # Öğrenci adını, soyadını ve sınıfını gösteriyoruz
            item = QListWidgetItem(f"{ogrenci[1]} {ogrenci[2]} - {ogrenci[3]}")  # Ad, Soyad, Sınıf
            item.setData(0, ogrenci[0])  # Öğrenci ID'sini sakla
            self.list_ogrenci.addItem(item)  # Listeye ekle

    def dersleri_yukle(self):
        conn = baglanti_olustur()
        cursor = conn.cursor()
        cursor.execute("SELECT id, ders_adi FROM dersler")
        dersler = cursor.fetchall()
        conn.close()

        self.combo_ders.clear()
        for ders in dersler:
            self.combo_ders.addItem(ders[1], ders[0])

    def dersi_kaydet(self):
        secili_ogrenci = self.list_ogrenci.currentItem()  # Seçilen öğeyi al
        secili_ders = self.combo_ders.currentData()  # Seçilen dersin ID'sini al

        if secili_ogrenci and secili_ders:
            ogrenci_id = secili_ogrenci.data(0)  # Öğrenci ID'sini al
            conn = baglanti_olustur()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ogrenci_dersleri (ogrenci_id, ders_id) VALUES (%s, %s)", (ogrenci_id, secili_ders))
            conn.commit()
            conn.close()

            self.close()

class AnaEkran(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Öğrenci ve Ders Listesi")
        self.setGeometry(300, 100, 800, 500)

        self.layout = QVBoxLayout()

        # Öğrenci Tablosu
        self.table_ogrenciler = QTableWidget()
        self.table_ogrenciler.setColumnCount(3)
        self.table_ogrenciler.setHorizontalHeaderLabels(["ID", "Ad", "Soyad"])

        # Ders Tablosu
        self.table_dersler = QTableWidget()
        self.table_dersler.setColumnCount(3)
        self.table_dersler.setHorizontalHeaderLabels(["ID", "Öğrenci", "Ders"])

        # Ders Ekle Butonu
        self.btn_ders_ekle = QPushButton("Ders Ekle")
        self.btn_ders_ekle.clicked.connect(self.ders_ekleme_penceresi_ac)

        # Layout Düzeni
        self.layout.addWidget(self.table_ogrenciler)
        self.layout.addWidget(self.table_dersler)
        self.layout.addWidget(self.btn_ders_ekle)
        self.setLayout(self.layout)

        self.ogrencileri_yukle()
        self.dersleri_yukle()

    def ogrencileri_yukle(self):
        conn = baglanti_olustur()
        cursor = conn.cursor()
        cursor.execute("SELECT id, ad, soyad FROM ogrenciler")
        ogrenciler = cursor.fetchall()
        conn.close()

        self.table_ogrenciler.setRowCount(len(ogrenciler))
        for row, ogrenci in enumerate(ogrenciler):
            for col, value in enumerate(ogrenci):
                self.table_ogrenciler.setItem(row, col, QTableWidgetItem(str(value)))

    def dersleri_yukle(self):
        conn = baglanti_olustur()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ogrenci_dersleri.id, ogrenciler.ad, dersler.ders_adi
            FROM ogrenci_dersleri
            JOIN ogrenciler ON ogrenci_dersleri.ogrenci_id = ogrenciler.id
            JOIN dersler ON ogrenci_dersleri.ders_id = dersler.id
        """)
        dersler = cursor.fetchall()
        conn.close()

        self.table_dersler.setRowCount(len(dersler))
        for row, ders in enumerate(dersler):
            for col, value in enumerate(ders):
                self.table_dersler.setItem(row, col, QTableWidgetItem(str(value)))

    def ders_ekleme_penceresi_ac(self):
        self.ders_ekleme_penceresi = DersEklemePenceresi()
        self.ders_ekleme_penceresi.exec_()
        self.dersleri_yukle()

app = QApplication(sys.argv)
window = AnaEkran()
window.show()
sys.exit(app.exec_())


#######################################################################################
# TİCARİ UYGULAMA ÖRNEĞİ

# ticari.py dosyası içeriği
# pyqt ile veritabanına ulaşma
# pip install mysql-connector-python
# pip install pyqt6
import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ticarivt" # ots = okultakipsistemi
  )
  secilen1 = veritabani1.cursor()
  # secilen1.execute("UPDATE kullanicilar SET numara = '05364445566' WHERE ad= 'Arda Güler'")
  secilen1.execute("SELECT * FROM ticarivt.kullanicilar")
  kayitlar = secilen1.fetchall() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
  print(kayitlar)
  print("işlem tamam.")

except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)

# proje3.py
import sys
from PyQt6.QtWidgets import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Ekranı")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # label_username = QLabel("Kullanıcı Adı:")
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
        secilen1.execute(f"SELECT * FROM ticarivt.kullanicilar where ka  = '{username}'")
        kullanici = secilen1.fetchall()
        if username == kullanici[0][1] and password == kullanici[0][2]:
            # self.close()  # Login penceresini kapat
            # import ticari
            # self.xx = ticari.TicariWindow()
            self.xx = TicariWindow()
            self.xx.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def open_ticari_window(self):
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
       

class TicariWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inch çevirici")


        pencere_ici = QWidget()
        layout = QVBoxLayout()

        buton1 = QPushButton("STOK")
        buton2 = QPushButton("CARİ")
        buton3 = QPushButton("DEPO")
        buton4 = QPushButton("MUHASEBE")
        buton5 = QPushButton("ÇIKIŞ")

        buton1.clicked.connect(self.stok)
        buton4.clicked.connect(self.mesajgoster)
        # buton5.clicked.connect(self.kapa)
        buton5.clicked.connect(lambda: sys.exit())

        layout.addWidget(buton1)
        layout.addWidget(buton2)
        layout.addWidget(buton3)
        layout.addWidget(buton4)
        layout.addWidget(buton5)

        pencere_ici.setLayout(layout)
        self.setCentralWidget(pencere_ici)

    def mesajgoster(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Bilgilendirme!")
        dlg.setText("Buradaki bilgiyi öğrendin.")
        dlg.exec()

    def kapa(self):
        sys.exit()

    def stok(self):
        import stok
        self.sp = stok.StokkPenceresi()
        # self.sp.move(-600,200)
        self.sp.show()
        # self.close()

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       

def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


############################################

# ticari_veritabani.py
# önce bu dosya ile vt oluştur
# programın çalışması için mysql hizmeti var ve çalışıyor olmalı
# pyqt ile veritabanına ulaşma
# pip install mysql-connector-python
import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
  )
  secilen1 = veritabani1.cursor()
  secilen1.execute("CREATE DATABASE IF NOT EXISTS ticarivt")
  secilen1.execute("show databases")
  vt_listesi = secilen1.fetchall()
  print("\n\nVeritabanı oluştu;\n",vt_listesi)

  secilen1.execute("CREATE TABLE IF NOT EXISTS ticarivt.kullanicilar(id int AUTO_INCREMENT PRIMARY KEY, ka VARCHAR(30), sf VARCHAR(20))")
  secilen1.execute("CREATE TABLE IF NOT EXISTS ticarivt.stoklar(id int AUTO_INCREMENT PRIMARY KEY, stokadi VARCHAR(30), stokmiktari int)")
  secilen1.execute("INSERT INTO ticarivt.kullanicilar (ka, sf) VALUES ('adm', '123')")
  secilen1.execute("INSERT INTO ticarivt.kullanicilar (ka, sf) VALUES ('1', '1')")
  secilen1.execute("ALTER TABLE ticarivt.stoklar ADD COLUMN tur VARCHAR(11)")
  veritabani1.commit()  # kayıt ekleme ve düzenleme için lazım.
  print(secilen1.rowcount, "kayıt eklendi.")

  kayitlar = secilen1.execute("SELECT * FROM ticarivt.kullanicilar")
  kayitlar = secilen1.fetchall() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
  print(kayitlar)
  print("işlem tamam.")

except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)

########################################
#Stoklar bölümü ve stok ekleme penceresi

# stok.py
import sys
from PyQt6.QtWidgets import *

class StokkPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stok Modulu")

        central_widget = QWidget()
        layout = QVBoxLayout()

        buton1 = QPushButton("Stok Ekle")
        buton2 = QPushButton("Stok Listesi")
        buton3 = QPushButton("...")
        buton4 = QPushButton("...")
        buton5 = QPushButton("ÇIKIŞ")
        buton1.clicked.connect(self.stokEkle)
        buton2.clicked.connect(self.stokListele)
        buton5.clicked.connect(lambda: sys.exit())

        layout.addWidget(buton1)
        layout.addWidget(buton2)
        layout.addWidget(buton3)
        layout.addWidget(buton4)
        layout.addWidget(buton5)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def stokEkle(self):
        import stokekle
        self.ekleme_penceresi = stokekle.StokEkleme()
        # self.ekleme_penceresi.move(-500,200)
        self.ekleme_penceresi.show()
   
    def stokListele(self):
        import stokliste
        self.liste_penceresi = stokliste.StokTablosu()
        # self.liste_penceresi.move(-500,400)
        self.liste_penceresi.show()

    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
def main():
    app = QApplication(sys.argv)
    window = StokkPenceresi()
    # QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

####################################################
# stokekle.py
import mysql.connector
try:
  veritabani1 = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ticarivt" # ots = okultakipsistemi
  )
  secilen1 = veritabani1.cursor()
  print("işlem tamam.")

except Exception as hata:
  print("Bir hata oluştu.")
  print(hata)

import sys
from PyQt6.QtWidgets import *

class StokEkleme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stok Ekeleme Ekranı")
        central_widget = QWidget()
        layout = QVBoxLayout()

        label_stokadi = QLabel("Stok Adı:")
        self.stokadi_input = QLineEdit()
        layout.addWidget(label_stokadi)
        layout.addWidget(self.stokadi_input)

        label_stokmiktari = QLabel("Stok Miktarı:")
        self.stokmiktari_input = QLineEdit()
        layout.addWidget(label_stokmiktari)
        layout.addWidget(self.stokmiktari_input)

        label_stokturu = QLabel("Stok Türü:")
        self.stokturu_input = QLineEdit()
        layout.addWidget(label_stokturu)
        layout.addWidget(self.stokturu_input)

        login_button = QPushButton("Stok Ekle")
        login_button.clicked.connect(self.kaydet)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def kaydet(self):

        komut = "INSERT INTO ticarivt.stoklar (stokadi, stokmiktari, tur) VALUES (%s, %s, %s)"
       
        ad = self.stokadi_input.text()
        miktar = self.stokmiktari_input.text()
        tur = self.stokturu_input.text()
        veri = (ad, miktar, tur)
        print(ad, miktar, tur)
       
        secilen1.execute(komut, veri)
        veritabani1.commit()  # kayıt ekleme ve düzenleme için lazım.
        print(secilen1.rowcount, "kayıt eklendi.")
       

def main():
    app = QApplication(sys.argv)
    window = StokEkleme()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


####################################################
#Stok listeleme penceresi

# stokliste.py
import mysql.connector

def stoklari_al():
    baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
    secilen1 = baglanti.cursor()
    secilen1.execute("SELECT * FROM stoklar")
    stoklar = secilen1.fetchall()  # Liste olarak al
    baglanti.close()
    return stoklar

import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtWidgets import *

class StokTablosu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stok Listesi")
        self.setGeometry(100, 100, 500, 300)

        # Layout oluştur
        layout = QVBoxLayout()

        # QTableWidget oluştur (4 sütunlu)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "STOK ADI", "MİKTARI", "TÜRÜ"])
        self.tableWidget.cellClicked.connect(self.satir_tiklandi)

        # Verileri tabloya ekle
        # stoklar = [
        #     (1, "Ali Yılmaz", 20, "Bilgisayar Müh."),
        #     (2, "Ayşe Kaya", 22, "Makine Müh."),
        #     (3, "Mehmet Demir", 21, "Elektrik-Elektronik Müh."),
        #     (4, "Zeynep Arslan", 23, "İnşaat Müh.")
        # ]
        stoklar = stoklari_al()
        self.populate_table(stoklar)


        butonlarLayout = QVBoxLayout()
        silButonu = QPushButton("Sil")
        duzeltButonu = QPushButton("Düzenle")
        kaydetButonu = QPushButton("Ekle")
        butonlarLayout.addWidget(silButonu)
        butonlarLayout.addWidget(duzeltButonu)
        butonlarLayout.addWidget(kaydetButonu)

        silButonu.clicked.connect(self.kayitSilme)
        duzeltButonu.clicked.connect(self.kayitDuzenleme)
        kaydetButonu.clicked.connect(self.kayitEkle)
               
        kayitlarLayout = QHBoxLayout()
        adLayout = QVBoxLayout()
        mkLayout = QVBoxLayout()
        trLayout = QVBoxLayout()
       
        self.adtb = QLineEdit()
        self.miktartb = QLineEdit()
        self.turtb = QLineEdit()
        adLayout.addWidget(QLabel("Adı"))
        adLayout.addWidget(self.adtb)

        mkLayout.addWidget(QLabel("Stok Miktarı"))
        mkLayout.addWidget(self.miktartb)

        trLayout.addWidget(QLabel("Stok Türü"))
        trLayout.addWidget(self.turtb)

        kayitlarLayout.addLayout(adLayout)
        layout.addWidget(self.tableWidget) # Tabloyu layout'a ekle
        kayitlarLayout.addLayout(mkLayout)
        kayitlarLayout.addLayout(trLayout)
        kayitlarLayout.addLayout(butonlarLayout)

        layout.addLayout(kayitlarLayout)
        self.setLayout(layout)
   
       

    def secili_id_al(self):
        secili_satir = self.tableWidget.currentRow()  # Seçili satır indexi

        if secili_satir < 0:
            return None  # Hiçbir şey seçili değilse

        id_item = self.tableWidget.item(secili_satir, 0)  # 0. sütun ID
        if id_item:
            return id_item.text()

        return None

    def satir_tiklandi(self):
        self.secilenID = self.secili_id_al()
        print(self.secilenID)
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()
        secilen1.execute(f"SELECT * FROM ticarivt.stoklar WHERE id = '{self.secilenID}'")
        seciliKayit = secilen1.fetchone()
        print(seciliKayit, self.secilenID)
        baglanti.close()
       
        self.adtb.setText(seciliKayit[1])
        self.miktartb.setText(str(seciliKayit[2]))
        self.turtb.setText(seciliKayit[3])

    def kayitEkle(self):
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()
        yeniad = self.adtb.text()
        yenimiktar = self.miktartb.text()
        yenitur = self.turtb.text()
        # secilen1.execute("UPDATE ticarivt.stoklar SET stokadi = %s, stokmiktari = %s, tur=%s WHERE id= %s",(yeniad,yenimiktar,yenitur,self.secilenID))
        komut = "INSERT INTO ticarivt.stoklar (stokadi, stokmiktari, tur) VALUES (%s, %s, %s)"
        veri = (yeniad, yenimiktar, yenitur)
        secilen1.execute(komut, veri)

        baglanti.commit() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
        baglanti.close()
        stoklar = stoklari_al()
        self.populate_table(stoklar)

    def kayitDuzenleme(self):
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()

        yeniad = self.adtb.text()
        yenimiktar = self.miktartb.text()
        yenitur = self.turtb.text()
        secilen1.execute("UPDATE ticarivt.stoklar SET stokadi = %s, stokmiktari = %s, tur=%s WHERE id= %s",(yeniad,yenimiktar,yenitur,self.secilenID))
        baglanti.commit() # commit olmadan ekleme, silme ve değişikli veri tabanına işlenmez.
        baglanti.close()
        stoklar = stoklari_al()
        self.populate_table(stoklar)

    def kayitSilme(self):
        baglanti = mysql.connector.connect(host="localhost",user="root",password="1234",database="ticarivt")
        secilen1 = baglanti.cursor()
        secilen1.execute(f"DELETE FROM ticarivt.stoklar WHERE id = '{self.secilenID}'")
        baglanti.commit()
        baglanti.close()
        stoklar = stoklari_al()
        self.populate_table(stoklar)
             

    def populate_table(self, stoklar):
        """Öğrenci listesini tabloya ekler"""
        self.tableWidget.setRowCount(len(stoklar))  # Satır sayısını belirle

        for row, student in enumerate(stoklar):
            for col, data in enumerate(student):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))

# PyQt6 uygulamasını başlat
def main():
  app = QApplication(sys.argv)
  window = StokTablosu()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
    main()













