#fonksiyon bloklu sonsuz inputlu 4 işlem makinesi
def sayi_listesi_al():
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
hesap_makinesi()