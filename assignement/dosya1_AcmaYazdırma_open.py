# open("Z:/exercises","w")
# open("exercise1","w")
# open("exercises/exercise1.txt","w")
# open("exercises/exercise2.txt","w")

from datetime import datetime, timedelta

giris_tarihi = datetime.now()

lastik_degisim = 2
lastik_tamir = 6
yag_degisim = 3

# Toplam süreyi hesaplayıp saate çevirerek ekliyoruz
toplam_sure = lastik_degisim + lastik_tamir + yag_degisim
son_teslim_tarihi = giris_tarihi + timedelta(hours=toplam_sure)


#open("C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya/tamir_listesi.txt","w") # dosyaya 1 kere yazar, üstüne yazar

# for a in range(1,2):
#     open(f"C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya/tamir_listesi{a}.txt","w")

d = open("Z:/exercises/exercise.txt","w")
d.write("Müşteri Bilgisi\t:Caner CANPOLAT\n")
d.write("Müşteri Kimlik Numarası\t:45678978945\n")
d.write("Adres Bilgisi\t:ANKARA\n")
d.write ("Araba Bilgisi: Volvo")
d.write("Trafiğe çıkış tarihi\t:25.05.2021\n")
d.write("Müşteri tarafından belirtilen arıza\t: Lastik değişimi")