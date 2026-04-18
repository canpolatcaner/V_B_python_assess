##############################################################################################################################################################
#encapsulation

class Musteri:
    def __init__(self,aa,xx,yy):        
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.__bakiye = 0       # __ ile başlayan değişkenler kapsüllenir ve sınıf içerisinden değiştirilmesine izin verilir, dışarıda değişiklik yapılamaz.
    def paraYatir(s,ym,k=10):
        s.__bakiye += (ym-k)
        print(f"Yatırılan miktardan({ym}TL), {k}TL kadar komiyon kesildi. \nHesaptaki son durum: {s.__bakiye}")
    def bakiyeGoster(self):
        return self.__bakiye
    def hesapBilgisi(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.__bakiye}")

musteri1 = Musteri(52632154872,"Mete",5566)
musteri2 = Musteri(52417451426,"Dila",8741)

musteri1.hesapBilgisi()
musteri2.hesapBilgisi()

musteri1.TC = 22334455664
# musteri1.__bakiye = 5000 # yapılamaz.
musteri1.paraYatir(1000)
musteri1.paraYatir(2000,0)
musteri1.hesapBilgisi()
# print("Müsteri bakiyesi:",musteri1.__bakiye)
print("Müsteri bakiyesi:",musteri1.ad)
print("Müsteri bakiyesi:",musteri1.bakiyeGoster()) 

##############################################################################################################################################################
#__ control_encapsulation

class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"):
        self._ad = xx # public / her sınıfa, her yere açık
        self.no = yy
        self.__sd = zz # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
   
    def saglikDurumu(self):
        return self.__sd + " (Özel bilgi)"

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741,"Astımı var") # Nesneye veri set etme
print(ogrenci1._ad)
print(ogrenci2._ad)
print(ogrenci2.no)
# print(ogrenci1.__sd) # __ ile başlayanlara direk ulaşılamaz.
print(ogrenci2.saglikDurumu()) # sd (sağlık durumu) nu okumak için method kullan.
ogrenci2.__sd = "xxx" # burada __sd değil, aynı isimli kopyasına atanır.
print(ogrenci2.__sd) # aynı olan __sd isimli değişken görüntülenir.
print(ogrenci2.saglikDurumu()) 

##############################################################################################################################################################
#__ control_encapsulation

class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"):
        self._ad = xx # public / her sınıfa, her yere açık
        self.no = yy
        self.__sd = zz # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
   
    def saglikDurumu(self):
        return self.__sd + " (Özel bilgi)"    

ogrenci1 = Ogrenci("Efekan",458,"Alerjisi var")

# print(f"\n\nÖğrenci bilgisi:\nAdı:{ogrenci1._ad} {ogrenci1.__sd}")
print(f"\n\nÖğrenci bilgisi:\nAdı:{ogrenci1._ad} {ogrenci1.saglikDurumu()}")

ogrenci2 = Ogrenci("Ahmet", 695, "İnsülin direnci var")
print(f"\n\nÖğrenci bilgisi:\nAdı:{ogrenci2._ad} {ogrenci2.saglikDurumu()}")

##############################################################################################################################################################
#encapsulation

class Hesap:
    def __init__(self, ad, no, bakiyesi,komisyon=5):
        self.isim = ad
        self.numara = no
        self.__bakiye = bakiyesi # private prop = kontrolü (değişiklik) sınıf içerisinden yapılan property demek.
        self.komisyon = komisyon

    def hesapBilgileri(self):
        return f"\n\nHesap bilgileri:\nİsim   :{self.isim}\nNumara :{self.numara}\nBakiye :{self.__bakiye}"

    def paraCek(self, miktar):
        if self.__bakiye <= (miktar + self.komisyon):
            print(f"\n\nBakiyeniz yeterli değil...\n\
                  Bakiyeniz:{self.__bakiye}\
                  Komisyon :{self.komisyon}")
        else:
            self.__bakiye -= (miktar + self.komisyon)
            print(f"\n\nPARA ÇEKME:\n\
Yeni Bakiye   :{self.__bakiye}\n\
Çekilen       :{miktar}\n\
Komisyon      :{self.komisyon}")

    def paraYatir(self, miktar):
        self.__bakiye += (miktar - self.komisyon)
        print(f"\n\nPARA YATIRMA:\n\
Yeni Bakiye :{self.__bakiye}\n\
Yatırılan   :{miktar}\n\
Komisyon    :{self.komisyon}")


hesap1 = Hesap("Kaan Koç",584782,1000)
print(hesap1.hesapBilgileri())
# hesap1.paraCek(300)
# hesap1.paraYatir(500)
hesap1.paraYatir(100)
hesap1.paraCek(50)

hesap2 = Hesap("Emir HAN", 585478, 1000, 0)
hesap2.paraYatir(100)
hesap2.paraCek(50)

##############################################################################################################################################################
#encapsulation

class BankaKasasi():
    __KasadaKalanMiktar = 0 # __ ile kapsüllenmiş bilgi
    def kasadakiMiktar(self):
        return self.__KasadaKalanMiktar
   
    def kasayaParaEkle(self, miktar):
        self.__KasadaKalanMiktar += miktar

    def kasadanParaCikar(self,miktar):
        self.__KasadaKalanMiktar += miktar

class BankaMusterisi():

    adiSoyadi = "---"
    hesapNumarasi = "tanımlanmamış" # public yada global
    __kalanParasi = 0 # __ ile kapsüllenmiş bilgi. Private özellik/propery.
    # private özellikler sınıf dışından değiştirilemez.
    # sınıf içerisindeki bir fonksiyon aracılığıyla değişir.
    def __init__(self,ad,no,para):
        self.adiSoyadi = ad
        self.hesapNumarasi = no
        # self.__kalanParasi = para
    def paraCek(self,cekilen):
        self.__kalanParasi -= cekilen
        # kasa1.__KasadaKalanMiktar -= cekilen
        kasa1.kasadanParaCikar(cekilen)
   
    def paraYatir(self,yatirilan):
        self.__kalanParasi += yatirilan
        # kasa1.__KasadaKalanMiktar += yatirilan
        kasa1.kasayaParaEkle(yatirilan)
   
    def kalanParaMiktariniGoster(self):
        return self.__kalanParasi

kasa1 = BankaKasasi()
kasa1.KasadaKalanMiktar = 50000

musteri1 = BankaMusterisi("Nurdan KARA","6325412",5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n")

musteri1.adiSoyadi = "Ali AK"
# musteri1.__kalanParasi += 5000
musteri1.paraYatir(5000)

print(f"\n\nKasada kalan para miktarı : {kasa1.KasadaKalanMiktar}")

print(f"\n\nMüşteri Bilgileri\n\
    Adı: \t{musteri1.adiSoyadi}\n\
    Hesap No : \t{musteri1.hesapNumarasi}\n")

print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri1.paraYatir(20)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri2 = BankaMusterisi("Ebru SARICAOĞLU","524785",6000)
musteri2.paraYatir(1000)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Müşteri2 kalan parası:", musteri2.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())

musteri2.paraYatir(3)
print("Müşteri1 kalan parası:", musteri1.kalanParaMiktariniGoster())
print("Müşteri2 kalan parası:", musteri2.kalanParaMiktariniGoster())
print("Kasadaki miktar:", kasa1.kasadakiMiktar())


##############################################################################################################################################################


