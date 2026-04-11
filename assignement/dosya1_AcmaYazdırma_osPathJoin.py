import os

# Masaüstü yolunu otomatik bulmak (farklı bilgisayarlarda da çalışması için)
# os.getlogin() o anki kullanıcı adını ('user' gibi) otomatik getirir.
kullanici = os.getlogin()
yol = f"C:/Users/{kullanici}/Desktop/Python_Projects/vektorel/Exercises_Dosya"

# Klasör kontrolü ve oluşturma
if not os.path.exists(yol):
    os.makedirs(yol)

# Döngü ile dosyaları oluşturma
for a in range(1, 3):
    dosya_adi = f"tamir_listesi{a}.txt"
    tam_yol = os.path.join(yol, dosya_adi) # Yolları birleştirmek için en sağlıklı yol
    
    with open(tam_yol, "w", encoding="utf-8") as f:
        f.write(f"{a}. numaralı deneme dosyası içeriği.")

print("İşlem başarıyla tamamlandı!")