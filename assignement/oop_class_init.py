class Musteri:
    # print("Musteri sınıfı çalıştı")
    TC = "00000000000"
    ad = "Tanımsız"
    hn = "---" # hasapno
    bakiye = 0
    def __init__(self,aa,xx,yy,zz=0): # sınıftan nesne üretme fonksiyonu
        # print("Musteri sınıfının init fonksiyonu çalıştı.")
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.bakiye = zz
    def bilgiVer(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.bakiye}")

musteri1 = Musteri(8874,"Mete",5566)
musteri2 = Musteri(6658,"Dila",8741,5000)

# print(musteri1)
# print("musteri1.ad : ",musteri1.ad)
# print("musteri1.TC : ",musteri1.TC)
# print("musteri1.hn : ",musteri1.hn)
# print("musteri1.bakiye : ",musteri1.bakiye)
musteri1.bilgiVer()
musteri2.bilgiVer() 

############################################################################################################################
# init metodu ile nesne oluşturma

class Musteri:
    # print("Musteri sınıfı çalıştı")
    TC = "00000000000"
    ad = "Tanımsız"
    hn = "---" # hasapno
    bakiye = 0
    def __init__(self,aa,xx,yy,zz=0): # sınıftan nesne üretme fonksiyonu
        # print("Musteri sınıfının init fonksiyonu çalıştı.")
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.bakiye = zz
    def bilgiVer(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.bakiye}")

musteri1 = Musteri(8874,"Mete",5566)
musteri2 = Musteri(6658,"Dila",8741,5000)

# print(musteri1)
# print("musteri1.ad : ",musteri1.ad)
# print("musteri1.TC : ",musteri1.TC)
# print("musteri1.hn : ",musteri1.hn)
# print("musteri1.bakiye : ",musteri1.bakiye)
musteri1.bilgiVer()
musteri2.bilgiVer()

############################################################################################################################

class Musteri:
    # print("Musteri sınıfı çalıştı")
    def __init__(self,aa,xx,yy,zz=0): # sınıftan nesne üretirken default parametre kullanılabilir.
        # print("init fonksiyonu çalıştı.")
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.bakiye = zz
    def hesapBilgisi(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.bakiye}")

musteri1 = Musteri(8874,"Mete",5566)
musteri2 = Musteri(6658,"Dila",8741,5000)

musteri1.hesapBilgisi()
musteri2.hesapBilgisi()

############################################################################################################################
#init default value
class Ogrenci:
    AdSoyad = "Tanımsız"
    NotOrtalamasi = ""
    DisiplinCezasi = 0

    def __init__(self,ad="Tanımsız",no=0):
        self.AdSoyad = ad
        self.Numara = no 
        
    def Bilgi(self):
        print ("Metod ile: Adı Soyadı:",self.AdSoyad,", Numarası:",self.Numara)

print("Sınıftaki adSoyad değeri:",Ogrenci.AdSoyad)

ogrenci1 = Ogrenci("Ahmet BAL",10)
ogrenci2 = Ogrenci("Meh
met GÜL")ogrenci3 = Ogrenci()
ogrenci4 = Ogrenci(no=42) # ilk parametreyi ad ile ilişkilendirmesin diye

ogrenci1.Bilgi()
ogrenci2.Bilgi()
ogrenci3.Bilgi()
ogrenci4.Bilgi()

############################################################################################################################
# exemple

class araclar(): # coğul olmayacak ve büyük harf ile başlayacak
    tur = "binek"
    uretici = "mercedes"

print("araclar sınıfı için")
print("Arac türü   :", araclar.tur)
print("Arac ureticisi:", araclar.uretici)

arac1=araclar() # Sınıftan Ornekleme

print("\narac1 Nesne örneği için")
print("Arac turu     :",arac1.tur) # değer atamadığım için default olanlar gelecek.
print("Arac ureticisi:",arac1.uretici)

arac2=araclar() # Sınıftan Ornekleme
arac2.tur="Araba"
arac2.uretici="volvo"
print("\narac2 Nesne örneği için")
print("Arac turu     :",arac2.tur)
print("Arac ureticisi:",arac2.uretici)
arac2.kapiSayisi=4 # nesneye sonradan özellik atayabiliriz.
print("Arac kapi sayisi:",arac2.kapiSayisi)

