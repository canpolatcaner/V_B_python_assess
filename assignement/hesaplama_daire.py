#Dairenin çevresi ve alanı
import math
pi=math.pi
while True:
    r=input("Dairenin yarıçapını giriniz\t:")
    if r.lower()=="q": #çıkış kontrolü
        print("Programdan çıkılıyor...")
        break
    try:
        r=r.replace(",",".")
        if r.replace(".","").isdigit():
            yaricap=float (r)
            cevre= pi*(yaricap*2)
            alan= pi*(yaricap**2)
            cizgi=[]
            cizgi.append(alan)
            print("-"*len(str(alan)) + "Sonuç" +"-"*len(str(alan)))
            print(f"Dairenin çevresi: {cevre:.4f}")
            print(f"Dairenin alanı: {alan:.4f}")
            print("Programdan çıkmak için 'q' tuşuna basınız.")
        else:
            print("Hatalı giriş yaptınız! Lütfen yalnızca sayısal bir değer giriniz.")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")