import os

# Hedef klasör yolu
klasor_yolu = "C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya/"

# Eğer bu klasör dizini yoksa oluştur
if not os.path.exists(klasor_yolu):
    os.makedirs(klasor_yolu)

# Şimdi dosya açma işlemini yapabilirsiniz
# for a in range(1,2):
#     with open(f"{klasor_yolu}rehber{a}.txt", "w", encoding="utf-8") as f:
#         f.write("Dosya oluşturuldu.")
with open(f"{klasor_yolu}rehber.txt", "w", encoding="utf-8") as f:
        f.write("caner canpolat\t5366746515\n")
        f.write("canpolat canpolat\t7894561212\n")