""""    print ("Merhaba", isim)
selam_ver ("Caner")"""
#inputla alıp fonksiyonla çağrılan 
"""def selam_ver(isim):
    print ("Merhaba", isim)
isim=input("Adınızı nedir?\t")
selam_ver(isim)""" 
#karenin değerlerini kontrollü hesaplayan
"""kare=input("Lütfen hesaplamak istediğiniz"
               +"karenin bir aygıtının uzunluğunu giriniz\t:")
kare=kare.replace(",",".")
deger=float (kare)
print(deger*4)""" 
"""while True:
    kare=input("Karenin kenar uzunluğunu giriniz\t:")
    kare=kare.replace(",",".")
    if kare.replace(".","").isdigit():
        deger=float (kare)
        print("Karenin çevresi\t:", deger*4)
        print("Karenin alanı\t:", deger**2)
        break
    else:
        print("Hatalı giriş yaptınız! Lütfen yalnızca sayısal bir değer giriniz.")"""
#karenin değerlerini döngülü kontrollü hesaplayan
"""while True:
    kare=input("Karenin kenar uzunluğunu giriniz\t:")
    if kare.lower()=="q": #çıkış kontrolü
        print("Programdan çıkılıyor...")
        break
    kare=kare.replace(",",".")
    if kare.replace(".","").isdigit():
        deger=float (kare)
        print("Karenin çevresi\t:", deger*4)
        print("Karenin alanı\t:", deger**2)
        print("Programdan çıkmak için 'q' tuşuna basınız.")
    else:
        print("Hatalı giriş yaptınız! Lütfen yalnızca sayısal bir değer giriniz.")"""
##2 sayıyla 4 işlem yaptıran
"""print("Basit Hesap Makinesi")
print("Çıkmak için 'q' yazabilirsiniz.")

while True:
    sayi = input("Bir sayı giriniz (çıkmak için q): ")

    # Çıkış kontrolü
    if sayi.lower() == "q": # xxx.lower()=='q' küçük harfe dönüştürerek işler, mantığı; büyük harf girmiş olsa bile çıkış alır
        print("Program sonlandırıldı.")
        break

    # Virgül -> nokta
    sayi = sayi.replace(",", ".")

    # Geçerli sayı mı?
    if sayi.replace(".", "").isdigit():
        sayi = float(sayi)

        # Kullanıcıdan işlem türünü soralım
        islem = input("İşlem seçiniz (+, -, *, /): ")

        # İkinci sayıyı alalım
        sayi2 = input("İkinci sayıyı giriniz: ")
        sayi2 = sayi2.replace(",", ".")
        
        if sayi2.replace(".", "").isdigit():
            sayi2 = float(sayi2)

            # İşlem kontrolü
            if islem == "+":
                print("Sonuç:", sayi + sayi2)
            elif islem == "-":
                print("Sonuç:", sayi - sayi2)
            elif islem == "*":
                print("Sonuç:", sayi * sayi2)
            elif islem == "/":
                if sayi2 != 0:
                    print("Sonuç:", sayi / sayi2)
                else:
                    print("Sıfıra bölme hatası!")
            else:
                print("Geçersiz işlem seçtiniz.")
        else:
            print("İkinci sayı hatalı!")
    else:
        print("Bir sayı girmeniz gerekiyor!")"""
#fonksiyon bloksuz sonsuz sayılı 4 işlem yapan
"""print("Hesap Makinesi")
print("Çıkmak için 'q' yazabilirsiniz.")

while True:
    sayilar = []  # kullanıcıdan alınacak sayılar listesi

    print("\nSayıları giriniz (bitirmek için 'q'):")

    while True:
        giris = input("Sayı: ")

        if giris.lower() == "q":
            break

        giris = giris.replace(",", ".")
        if giris.replace(".", "").isdigit():
            sayilar.append(float(giris)) #.append() ile listeye sayı eklenir
        else:
            print("Geçersiz giriş!")

    if not sayilar:  # hiç sayı girilmediyse
        print("Hiç sayı girilmedi, program sonlandırılıyor.")
        break

    islem = input("İşlem seçiniz (+, -, *, /): ")

    sonuc = sayilar[0]
    for s in sayilar[1:]:
        if islem == "+":
            sonuc += s
        elif islem == "-":
            sonuc -= s
        elif islem == "*":
            sonuc *= s
        elif islem == "/":
            if s != 0:
                sonuc /= s
            else:
                print("Sıfıra bölme hatası!")
                sonuc = None
                break
        else:
            print("Geçersiz işlem!")
            sonuc = None
            break

    if sonuc is not None:
        print("Sonuç:", sonuc) """ 
#fonksiyon bloklu sonsuz inputlu 4 işlem makinesi
"""def sayi_listesi_al():
    #Kullanıcıdan sayı listesi alır
    sayilar = []
    print("\nSayıları giriniz (bitirmek için 'q'):")
    while True:
        giris = input("Sayı: ")
        if giris.lower() == "q":
            break
        giris = giris.replace(",", ".")
        if giris.replace(".", "").isdigit():
            sayilar.append(float(giris)) #sayilar listesine giriş ile alınan değeri .append ile ekle
        else:
            print("Geçersiz giriş!")
    return sayilar

def hesapla(sayilar, islem): #bu parametreler dışarıdan fonksiyona veri taşır
    #sonuç=hesapla([100,2,5],"/") print(sonuç) ile aynı mantık; sayilar ve islem datasını getirir
    #bu parametreler (sayilar, islem) sayesinde fonksiyonları genel hale getiririz;
    #farklı listeler ve farklı işlemlerle tekrar tekrar kullanabiliriz.
    #Girilen sayı listesi üzerinde seçilen işlemi uygularr
    sonuc = sayilar[0]
    for s in sayilar[1:]:
        if islem == "+":
            sonuc += s
        elif islem == "-":
            sonuc -= s
        elif islem == "*":
            sonuc *= s
        elif islem == "/":
            if s != 0:
                sonuc /= s
            else:
                print("Sıfıra bölme hatası!")
                return None
        else:
            print("Geçersiz işlem!")
            return None
    return sonuc

def hesap_makinesi():
    #Ana döngü: kullanıcıdan sayı alır, işlem seçer ve sonucu gösterir
    print("Hesap Makinesi")
    print("Çıkmak için 'q' yazabilirsiniz.")

    while True:
        sayilar = sayi_listesi_al()
        if not sayilar:
            print("Hiç sayı girilmedi, program sonlandırılıyor.")
            break

        islem = input("İşlem seçiniz (+, -, *, /): ")
        sonuc = hesapla(sayilar, islem)

        if sonuc is not None:
            print("Sonuç:", sonuc)

# Programı çalıştır
hesap_makinesi()"""
#Yaş hesaplama programı
"""print("*"*5+"Yaş Hesaplama Programına Hoş geldiniz", end="*"*5)
adi=input("\nLütfen size hitap edebilmem için adınızı giriniz.\n")
print("Merhaba", adi)
yas=int(input(f"\n{adi}, hangi yılda doğdunuz?\n"))
print(f"demek {2026-yas} yaşındasınız {adi}.")
kilo=int(input("{} kaç kilosun?\n".format(adi)))
boy=int(input("peki ya boyun kaç {}\n".format (adi)))
ideal_kilo=int(45.5+(boy-152.4)*(2.3/2.54))
fark=int(kilo-ideal_kilo)
print("Biliyormusun {}, aslında senin ideal kilon {} ve\n sen ideal kilondan {} kilo uzaktasın".format (adi, ideal_kilo, fark))"""
#Ortalama hesaplama
"""print("*"*3+"Ortalama Hesaplama Programı", end="*"*3)
yazili_notu1=int(input("\nLütfen birinci yazılı sınav notunuzu giriniz\t:"))
yazili_notu2=int(input("\nLütfen ikinci yazılı sınav notunuzu giriniz\t:"))
performans_notu=int(input("\nLütfen performans notunuzu giriniz\t\t:"))
ortalama=(yazili_notu1+yazili_notu2+performans_notu)/3
print("\n\nOrtalamanız\t: {} puandır.". format(round(ortalama,2)))
print("\n\nOrtalamanız\t: %d puandır." %(ortalama))"""
#kontrollü 0-100 arası sonsuz ortalama hesaplama
"""def sinav_notlarini_al():
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
    print("\nOrtalamanız\t: %.2f" %hesapla(notlar))"""
#Üçgen çevre ve alan hesaplama (Heron formülüyle)
"""import math
def hesapla_ucgen():
    kenarlar=[]

    print("Lütfen üçgenin kenar uzunluklarını giriniz:")

    while len(kenarlar)<3:
        try:
            sayi= float(input(f"{len(kenarlar) + 1}.kenar:"))
            if sayi<=0:
                print("Kenar uzunluğu 0'dan büyük olmalıdır!")
    
            kenarlar.append(sayi)
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    a, b, c= kenarlar

    if (a+b>c) and (a+c>b) and (b+c>a):
        cevre = a + b + c
        s = cevre / 2
        alan = math.sqrt(s * (s-a)*(s-b)*(s-c))
        print("-"*30)
        print(f"Üçgenin çevresi\t: {cevre:.2f}")
        print(f"Üçgenin alanı\t: {alan:.2f}")
    else:
        print("\nHata: Girdiğiniz kenarlar bir üçgen oluşturmuyor!")

hesapla_ucgen()"""
#Dairenin çevresi ve alanı
"""import math
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
        print("Lütfen geçerli bir sayı giriniz.")"""
#Newton serbest düşüş (h = ½*g*t**2)
"""
def yukseklik(sure):
    g = 9.81
    h = 0.5 * g * sure**2
    return h

def sure(yukseklik):
    g = 9.81
    t = (2 * yukseklik / g)**0.5
    return t

while True:
    print("*"*30)
    sec = input("Yükseklik hesaplamak için Y'ye basınız." +
                "\nSüre hesaplamak için S'ye basınız.\nÇıkmak için 'q''ya basınız:\n" + "*"*30)
    
    if sec.lower() == "q":
        print("Programdan çıkılıyor...")
        break
    
    elif sec.lower() == "y":
        print("-"*30)
        sure_degeri = input("Lütfen süreyi saniye cinsinden giriniz: ")
        try:
            sure_float = float(sure_degeri.replace(",", "."))
            h = yukseklik(sure_float)
            print("-"*30)
            print(f"{sure_float:.2f} saniyede {h:.2f} metre serbest düşer.")
            print("-"*30)
        except ValueError:
            print("Lütfen geçerli bir sayısal değer giriniz.")
    
    elif sec.lower() == "s":
        print("-"*30)
        yukseklik_degeri = input("Lütfen yüksekliği metre cinsinden giriniz: ")
        try:
            yukseklik_float = float(yukseklik_degeri.replace(",", "."))
            t = sure(yukseklik_float)
            print("-"*30)
            print(f"{yukseklik_float:.2f} metreden {t:.2f} saniyede yere varır.")
            print("-"*30)
        except ValueError:
            print("Lütfen geçerli bir sayısal değer giriniz.")
    
    else:
        print("-"*10 + "Hatalı giriş yaptınız!" + "-"*10 +
        "\n\t***Lütfen Y, S veya Q'ya basınız.***")"""
# Bilmece elif ile
"""cevap_hakki=3

while cevap_hakki>0:
    cevap=input("*"*5 + "Dışarıda sağanak yağmur altında tamamen"
            +"\nkorumasız olan bir adam var fakat saçının tek bir teli dahi ıslanmadı."
            +"\n Neden? :D" + "*"*8 + "\n")
    if cevap.lower()=="adam kelmiş":
        print("Doğru :D")
        break
    elif cevap.lower()=="adam kel":
        print("Doğru :D")
        break
    elif cevap.lower()=="çünkü kelmiş":
        print("Doğru :D")
        break
    elif cevap.lower()=="kelmiymiş?":
        print("Doğru :D")
        break
    elif cevap.lower()=="kelmiymiş":
        print("Doğru :D")
        break
    elif cevap.lower()=="kelmiş":
        print("Doğru :D")
        break
    elif cevap.lower()=="kel":
        print("Doğru :D")
        break
    else:
        cevap_hakki-=1
        if cevap_hakki>0:
            print("-"*30)
            print(f"Olmadı, bi daha dene...\nKalan hakkın:{cevap_hakki}")
            
        else:
            print("-"*30)
            print("Olmadı, bi dahaki sefere artık...\n Çünkü; adam kelmiş! :D")"""
#Bilmece liste ile
"""
dogru_cevaplar=[
    "adam kelmiş",
    "adam kel",
    "çünkü kelmiş",
    "kelmiymiş?",
    "kelmiş",
    "kel",
    "kel çünkü",
    "kel mi",
    "kel mi?"
    ]
cevap_hakki=3

while cevap_hakki>0:
    cevap=input("*"*5 + "Dışarıda sağanak yağmur altında tamamen"
            +"\nkorumasız olan bir adam var fakat saçının tek bir teli dahi ıslanmadı."
            +"\n Neden? :D" + "*"*8 + "\n")
    try:
        if cevap.lower() in dogru_cevaplar:  
            print("Doğru :D")
            break

        else:
            cevap_hakki-=1
            if cevap_hakki>0:
                print("-"*30)
                print(f"Olmadı, bi daha dene...\nKalan hakkın:{cevap_hakki}")
                
            else:
                print("-"*30)
                print("Olmadı, bi dahaki sefere artık...\n Çünkü; adam kelmiş! :D")
    except ValueError:
        print("Hile yapma!")"""
            
        
          
    
    

      

