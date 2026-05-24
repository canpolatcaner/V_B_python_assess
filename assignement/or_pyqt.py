# AHP, TOPSİS, VIKOR, SAW

import sys
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QPushButton, QLabel, QSpinBox, QTextBrowser, 
                             QHeaderView, QComboBox, QGroupBox, QMessageBox)
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt

class DecisionMasterPro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MCDA Solver Pro - Karar Analizi ve Raporlama Sistemi")
        self.setGeometry(100, 100, 1200, 950)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 1. KONTROL PANELİ
        control_group = QGroupBox("Metot ve Veri Yapılandırması")
        c_layout = QHBoxLayout()

        c_layout.addWidget(QLabel("<b>Analiz Metodu:</b>"))
        self.method_combo = QComboBox()
        self.method_combo.addItems(["SAW (Basit Toplamsal)", "TOPSIS (İdeal Çözüm)", "VIKOR (Uzlaşık Karar)", "AHP (İkili Karşılaştırma)"])
        self.method_combo.currentIndexChanged.connect(self.setup_table)
        c_layout.addWidget(self.method_combo)

        c_layout.addWidget(QLabel("Alternatif Sayısı:"))
        self.row_spin = QSpinBox(); self.row_spin.setRange(2, 10); self.row_spin.setValue(3)
        self.row_spin.valueChanged.connect(self.setup_table)
        c_layout.addWidget(self.row_spin)

        c_layout.addWidget(QLabel("Kriter Sayısı:"))
        self.col_spin = QSpinBox(); self.col_spin.setRange(2, 10); self.col_spin.setValue(3)
        self.col_spin.valueChanged.connect(self.setup_table)
        c_layout.addWidget(self.col_spin)
        
        control_group.setLayout(c_layout)
        main_layout.addWidget(control_group)

        # 2. KARAR MATRİSİ
        self.table = QTableWidget()
        self.setup_table()
        main_layout.addWidget(self.table)

        # 3. HESAPLA
        self.calc_btn = QPushButton("ANALİZİ BAŞLAT VE ADIMLARI RAPORLA")
        self.calc_btn.setStyleSheet("background-color: #27ae60; color: white; height: 50px; font-weight: bold;")
        self.calc_btn.clicked.connect(self.run_analysis)
        main_layout.addWidget(self.calc_btn)

        # 4. RAPOR
        self.report = QTextBrowser()
        main_layout.addWidget(self.report)

    def setup_table(self):
        method = self.method_combo.currentText()
        if "AHP" in method:
            # AHP için kare matris (Kriter vs Kriter)
            n = self.col_spin.value()
            self.table.setRowCount(n + 1); self.table.setColumnCount(n + 1)
            self.table.setItem(0,0, QTableWidgetItem("KRİTERLER"))
            for i in range(1, n+1):
                self.table.setItem(0, i, QTableWidgetItem(f"Kriter {i}"))
                self.table.setItem(i, 0, QTableWidgetItem(f"Kriter {i}"))
                self.table.setItem(i, i, QTableWidgetItem("1")) # Köşegenler 1
        else:
            # Diğerleri için Karar Matrisi (Alt vs Krit)
            r, c = self.row_spin.value() + 1, self.col_spin.value() + 1
            self.table.setRowCount(r); self.table.setColumnCount(c)
            self.table.setItem(0,0, QTableWidgetItem("İSİMLER"))
            for j in range(1, c): self.table.setItem(0, j, QTableWidgetItem(f"Kriter {j}"))
            for i in range(1, r): self.table.setItem(i, 0, QTableWidgetItem(f"Alternatif {i}"))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def run_analysis(self):
        try:
            method = self.method_combo.currentText()
            r, c = self.table.rowCount(), self.table.columnCount()
            
            # Veri Çekme
            k_names = [self.table.item(0, j).text() for j in range(1, c)]
            a_names = [self.table.item(i, 0).text() for i in range(1, r)]
            data = np.array([[float(self.table.item(i, j).text().replace(',','.')) for j in range(1, c)] for i in range(1, r)])

            html = f"<h1>MATEMATİKSEL ANALİZ RAPORU: {method}</h1><hr>"

            if "SAW" in method:
                norm = data / data.max(axis=0)
                scores = norm.mean(axis=1)
                html += "<h3>1. Normalizasyon: r<sub>ij</sub> = x<sub>ij</sub> / max(x<sub>j</sub>)</h3>"
                html += self.tablo_yap(norm, k_names, a_names)
                html += self.sonuc_yap(scores, a_names)

            elif "TOPSIS" in method:
                norm = data / np.sqrt(np.sum(data**2, axis=0))
                id_p, id_n = norm.max(axis=0), norm.min(axis=0)
                s_p, s_n = np.sqrt(np.sum((norm-id_p)**2, axis=1)), np.sqrt(np.sum((norm-id_n)**2, axis=1))
                scores = s_n / (s_p + s_n)
                html += "<h3>1. Vektör Normalizasyonu</h3>" + self.tablo_yap(norm, k_names, a_names)
                html += f"<h3>2. İdealler:</h3><b>A+:</b> {id_p.round(3)} | <b>A-:</b> {id_n.round(3)}"
                html += self.sonuc_yap(scores, a_names)

            elif "VIKOR" in method:
                f_star, f_minus = data.max(axis=0), data.min(axis=0)
                S = np.sum((f_star - data)/(f_star - f_minus), axis=1) / data.shape[1]
                R = np.max((f_star - data)/(f_star - f_minus), axis=1) / data.shape[1]
                Q = 0.5 * (S - S.min())/(S.max() - S.min()) + 0.5 * (R - R.min())/(R.max() - R.min())
                html += "<h3>VIKOR Analizi: S (Grup Faydası) ve R (Pişmanlık) Değerleri</h3>"
                html += self.sonuc_yap(1-Q, a_names) # Q ne kadar küçükse o kadar iyi, sıralama için 1-Q

            elif "AHP" in method:
                col_sums = data.sum(axis=0)
                norm = data / col_sums
                weights = norm.mean(axis=1)
                html += "<h3>Kriter Ağırlık Analizi (Özvektör Hesabı)</h3>"
                html += self.tablo_yap(norm, k_names, k_names)
                html += "<h3>Hesaplanan Kriter Önem Dereceleri:</h3>"
                for n, w in zip(k_names, weights): html += f"<b>{n}:</b> %{w*100:.2f}<br>"

            self.report.setHtml(html)
        except Exception as e:
            QMessageBox.warning(self, "Hata", "Lütfen tüm sayısal alanları doldurun.")

    def tablo_yap(self, data, cols, rows):
        t = "<table border='1' width='100%'><tr><th>-</th>" + "".join([f"<th>{c}</th>" for c in cols]) + "</tr>"
        for i, r in enumerate(rows):
            t += f"<tr><td><b>{r}</b></td>" + "".join([f"<td>{v:.4f}</td>" for v in data[i]]) + "</tr>"
        return t + "</table>"

    def sonuc_yap(self, scores, names):
        res = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
        t = "<h3>Nihai Sıralama</h3><table border='1' width='100%' bgcolor='#f9f9f9'>"
        for rank, (n, s) in enumerate(res, 1):
            t += f"<tr><td>{rank}.</td><td><b>{n}</b></td><td>Skor: {s:.4f}</td></tr>"
        return t + "</table>"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DecisionMasterPro()
    window.show()
    sys.exit(app.exec())
