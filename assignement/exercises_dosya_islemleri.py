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


open("Z:/exercises/exercise.txt","w") # dosyaya 1 kere yazar yapar üstüne yazar

for a in range(1,2):
    open(f"Z:/exercises/exercise{a}.txt","w")

d = open("Z:/exercises/exercise.txt","w")
d.write("Müşteri Bilgisi: Caner CANPOLAT\n")
d.write("Müşteri Kimlik Numarası :45678978945\n")
d.write("Adres Bilgisi :ANKARA\n")
d.write ("Araba Bilgisi :Volvo\n")
d.write("Trafiğe çıkış tarihi: 25.05.2021\n")
d.write("Müşteri tarafından belirtilen arıza: Lastik değişimi\n")
d.write(f"Araç giriş tarihi: {giris_tarihi.strftime('%d.%m.%Y %H:%M')}\n")
d.write(f"Toplam işlem süresi: {toplam_sure} saat\n")
d.write(f"Son teslim tarihi: {son_teslim_tarihi.strftime('%d.%m.%Y %H:%M')}\n")