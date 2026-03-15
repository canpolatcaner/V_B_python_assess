from pathlib import Path

# Yolunuzu tanımlayın
yol = Path("C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya")

# Klasör yoksa oluştur (parents=True iç içe klasörleri de oluşturur)
yol.mkdir(parents=True, exist_ok=True)

# Artık dosyanızı güvenle açabilirsiniz
with open(yol / "tamir_listesi.txt", "w", encoding="utf-8") as f:
    f.write("Klasör otomatik kontrol edildi ve dosya yazıldı.")