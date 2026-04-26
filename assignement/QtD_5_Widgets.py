from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class BasitArayuz(QMainWindow):
    def __init__(self):
        super().__init__()      
        uic.loadUi("QtD_5_Widgets.ui", self)# Tasarlanan .ui dosyasını yüklüyoruz
# 1. Başlangıç Ayarları
        self.setWindowTitle("PyQt5 Eğitim Uygulaması")
        self.label.setText("Lütfen bir işlem yapın...")
        self.comboBox.addItems(["Python", "C++", "Java"]) # Başlangıç itemları

# 2. Sinyal - Slot Bağlantıları (Olayları Tanımlama)        
        self.pushButton.clicked.connect(self.butona_tiklandi) # Butona tıklanınca      
        # Menüden 'Aç' seçilince (QAction)
        self.actionA.triggered.connect(self.menu_ac_tiklandi)
        # ComboBox'tan seçim yapılınca
        self.comboBox.currentIndexChanged.connect(self.combo_degisti)
        # RadioButton ve CheckBox durum değişimleri
        self.radioButton.toggled.connect(self.durum_guncelle)
        self.checkBox.stateChanged.connect(self.durum_guncelle)

# 3. Fonksiyonlar (Slotlar)
    def butona_tiklandi(self):
        # LineEdit içindeki metni al
        metin = self.lineEdit.text()
        if metin: # Boş değilse işlem yap
            self.label.setText(f"Eklenen: {metin}")
            self.comboBox.addItem(metin) # ComboBox'a ekle
            self.lineEdit.clear() # Giriş alanını temizle

    def menu_ac_tiklandi(self):
        self.label.setText("Menüden 'Aç' komutu verildi.")
    def combo_degisti(self):
        # Seçili olan metni al ve hem label'a hem lineEdit'e yaz
        secilen = self.comboBox.currentText()
        self.label.setText(f"Seçildi: {secilen}")
        self.lineEdit.setText(secilen)
    def durum_guncelle(self):
        # RadioButton ve CheckBox'ın durumlarını kontrol et
        rb_durum = "Seçili" if self.radioButton.isChecked() else "Seçili Değil"
        cb_durum = "İşaretli" if self.checkBox.isChecked() else "İşaretli Değil"      
        self.label.setText(f"RB: {rb_durum} | CB: {cb_durum}")

app = QApplication([]) # Uygulamayı çalıştır
pencere = BasitArayuz()
pencere.show()
app.exec_() 
