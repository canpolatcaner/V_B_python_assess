# # py -m pip install pyqt6
# # pip install pyqt6
# from PyQt6.QtWidgets import *
# uyg = QApplication([])
# pencere = QWidget()
# pencere.show()  
# uyg.exec()

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QLabel, QMessageBox, QHeaderView)
from PyQt6.QtCore import Qt

class DecisionCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Karar Analizi Hesaplayıcı (SAW Metodu)")
        self.setGeometry(100, 100, 800, 500)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        
        # Talimatlar
        info_label = QLabel("<b>SAW Metodu Hesaplayıcı:</b> Kriter ağırlıklarını (toplamı 1 olmalı) ve alternatif puanlarını girin.")
        main_layout.addWidget(info_label)

        # Tablo Oluşturma (3 Alternatif, 3 Kriter varsayılan)
        self.table = QTableWidget(3, 4) # 3 Satır, 4 Sütun (Alternatif Adı + 3 Kriter)
        self.table.setHorizontalHeaderLabels(["Alternatif Adı", "Kriter 1", "Kriter 2", "Kriter 3"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Varsayılan Değerler
        defaults = [
            ["Seçenek A", "80", "70", "90"],
            ["Seçenek B", "60", "95", "85"],
            ["Seçenek C", "90", "60", "75"]
        ]
        for r, row in enumerate(defaults):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(val))

        main_layout.addWidget(self.table)

        # Ağırlık Girişleri
        weight_layout = QHBoxLayout()
        weight_layout.addWidget(QLabel("Kriter Ağırlıkları (örn: 0.3, 0.4, 0.3):"))
        self.weight_input = QTableWidget(1, 3)
        self.weight_input.setFixedHeight(60)
        self.weight_input.setHorizontalHeaderLabels(["W1", "W2", "W3"])
        for i in range(3):
            self.weight_input.setItem(0, i, QTableWidgetItem("0.33"))
        weight_layout.addWidget(self.weight_input)
        
        main_layout.addLayout(weight_layout)

        # Hesapla Butonu
        self.calc_btn = QPushButton("Hesapla ve En İyi Seçeneği Bul")
        self.calc_btn.setFixedHeight(40)
        self.calc_btn.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        self.calc_btn.clicked.connect(self.calculate_saw)
        main_layout.addWidget(self.calc_btn)

        # Sonuç Ekranı
        self.result_label = QLabel("Sonuç: ")
        self.result_label.setStyleSheet("font-size: 16px; color: blue;")
        main_layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def calculate_saw(self):
        try:
            num_rows = self.table.rowCount()
            num_cols = self.table.columnCount() - 1 # İlk sütun isim

            # 1. Ağırlıkları al
            weights = []
            for i in range(num_cols):
                weights.append(float(self.weight_input.item(0, i).text().replace(',', '.')))

            if abs(sum(weights) - 1.0) > 0.05:
                QMessageBox.warning(self, "Uyarı", "Kriter ağırlıkları toplamı 1'e yakın olmalıdır!")

            # 2. Verileri al ve Normalizasyon (Basit Max Normalizasyonu)
            scores = []
            names = []
            
            # Max değerleri bul (Normalizasyon için)
            max_values = []
            for j in range(1, num_cols + 1):
                col_data = [float(self.table.item(i, j).text().replace(',', '.')) for i in range(num_rows)]
                max_values.append(max(col_data))

            # 3. Ağırlıklı Toplamı Hesapla (V_i = Σ w_j * r_ij)
            results = {}
            for i in range(num_rows):
                name = self.table.item(i, 0).text()
                total_score = 0
                for j in range(1, num_cols + 1):
                    val = float(self.table.item(i, j).text().replace(',', '.'))
                    norm_val = val / max_values[j-1] # Normalizasyon
                    total_score += norm_val * weights[j-1]
                
                results[name] = total_score

            # 4. Kazananı Bul
            winner = max(results, key=results.get)
            res_text = f"<b>En İyi Seçenek: {winner}</b> (Puan: {results[winner]:.4f})<br>"
            res_text += "Tüm Puanlar: " + ", ".join([f"{k}: {v:.2f}" for k, v in results.items()])
            
            self.result_label.setText(res_text)

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Lütfen tüm hücrelere geçerli sayısal değerler girin.\nDetay: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DecisionCalculatorApp()
    window.show()
    sys.exit(app.exec())
