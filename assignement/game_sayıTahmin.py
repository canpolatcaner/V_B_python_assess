import random

tutulansayi = random.randint (1,50)
puan=100
hak=10
#print (tutulansayi)

print ("SAYI TAHMİN OYUNUNA HOŞ GELDİNİZ.")
print ("---------------------------------\n")
print ("1-50 arası bir sayı tuttum. "+str(hak)+" hakkın var\n\n")

for i in range(1, hak):
  print (str(i)+".hak")
  kullanicitahmini = int (input("Tahminin nedir?"))
  if kullanicitahmini == tutulansayi:
    print("BİLDİN, SÜPER. PUANIN",puan)
    break
  else:
    puan = int(puan - 100/hak)
    print("Bilemedin, puanın", puan,)
    if kullanicitahmini > tutulansayi: 
      print("Tahminin, tuttuğum sayıdan büyük.\n")
    elif kullanicitahmini < tutulansayi: 
      print("Tahminin, tuttuğum sayıdan küçük.\n")
