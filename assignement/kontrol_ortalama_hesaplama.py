#kontrollü 0-100 arası sonsuz ortalama hesaplama
def sinav_notlarini_al():
    sinav_notlari_listesi=[]
    print("Lütfen sınav notlarınızı girdikten sonra 'q'ya basınız ve\n ortalamanızın hesaplanması için bekleyiniz.")
    while True:
        sinav_notlari=input("\nSınav notunuzu giriniz\t:")
        if sinav_notlari.lower()=="q":
            print("Giriş işlemi durduruldu.")
            break
        sinav_notlari=sinav_notlari.replace(",",".")
        if sinav_notlari.replace(".","").isdigit():
            maks_min=float(sinav_notlari)
            if 0 <=maks_min<=100:
                sinav_notlari_listesi.append(float(sinav_notlari))
            else:
                print("Hatalı giriş!!!\nLütfen 0 ile 100 arasında sayısal değer giriniz.")
        else:
            print("Hatalı giriş!!!\nLütfen sayısal değer giriniz.")
    return sinav_notlari_listesi
def hesapla(sinav_notlari_listesi):
    if len(sinav_notlari_listesi)==0:
            return "Hiç not girilmedi!"
    toplam=sum(sinav_notlari_listesi)
    n=len(sinav_notlari_listesi)
    ortalama=toplam/n
    return ortalama
notlar=sinav_notlarini_al()
sonuc=hesapla(notlar)
if isinstance(sonuc, str):
    print(sonuc)
else:
    print("\nOrtalamanız\t: %.2f" %hesapla(notlar))