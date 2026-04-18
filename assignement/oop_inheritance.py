
class Calisan():
    Odulleri = "" # Sonradan belirleneceği için init içinde değil
    Rutbesi = "" # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy
    def CalisanBilgisi(self):
        print("Çalışan bilgileri:\nAdı Soyadı:",self.AdiSoyadi,"\tTCKN:",self.TCKN)

calisan1 = Calisan("123456", "Erdinç DÖNMEZ")
calisan1.CalisanBilgisi()

class Idareci(Calisan): ##inheritance -- İdareci, Calisan sınıfından miras alır 
    pass
   
calisan2 = Calisan("654321", "Mustafa Beyazit")
calisan2.CalisanBilgisi()

calisan3 = Idareci()
calisan3.CalisanBilgisi()

#######################################################################################################
#ilan sınıfı ile miras alma/ inheritence from ilan class

class Ilan:
    def __init__(self,ilan_no=0,a="--"):
        self.ilanNo = ilan_no
        self.Aciklama = a
    def ilanBilgisi(aa):
        return f"\n\nİlan bilgileri:\n{'='*20}\nİlan numarası: {aa.ilanNo}\
        \nAçıklama : {aa.Aciklama}"

ilan1 = Ilan(8547)
print(ilan1.ilanBilgisi())
ilan2 = Ilan(5214,"Sahiplendirmek üzere..")
print(ilan2.ilanBilgisi())

class EvIlan(Ilan): # Ilan sınıfından özellik ve fonksiyon vb. miras al
    def __init__(self, ino=0,ack ="", m2_ =0, semt_=""):
        super().__init__(ino,ack)
        self.m2 = m2_
        self.semt = semt_

    def ilanBilgisi(aa):
        return f"\n\nEv ilanı bilgileri:\n{'='*20}\nİlan numarası: {aa.ilanNo}\
        \nAçıklama : {aa.Aciklama},\nMetrekare: {aa.m2}\nSemt: {aa.semt}"

ilan3 = EvIlan(6632,"Acil satılık 3+1", 120, "Kızılay")
print(ilan3.ilanBilgisi())

class KiralikEv(EvIlan):
    def __init__(self, ino=0, ack="", m2_=0, semt_=""):
        super().__init__(ino, ack, m2_, semt_)

ilan4 = KiralikEv()

print(ilan4.ilanBilgisi())

class AracIlani(Ilan):
    def __init__(self, ilan_no=0, a="--"):
        super().__init__(ilan_no, a)

ilan5 = AracIlani()
ilan5.motor_hacmi = 1600 # sonradan property tanımlanabilir

print(ilan5.ilanBilgisi())
print(ilan5.motor_hacmi)

ilan6 = AracIlani()
# ilan6.motor_hacmi # hata veririr

#######################################################################################################

class Calisan():
    Odulleri = "" # Sonradan belirleneceği için init içinde değil
    Rutbesi = "" # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy
    def CalisanBilgisi(self):
        print("Çalışan bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN)

calisan1 = Calisan("123456","Erdinç DÖNMEZ")
calisan1.CalisanBilgisi()

class Idareci(Calisan):
    EkUcret = 0 # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---",grv="Henüz hanımlı değil"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy
        self.Gorev = grv
    def CalisanBilgisi(self): # Miras aldığı metodu override ettik. Üzerine yazdık.
        print("Yonetici bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN," Görevi:",self.Gorev)
   
calisan2 = Calisan("Mustafa Beyazit","654321")
calisan2.CalisanBilgisi()

calisan3 = Idareci()
calisan3.CalisanBilgisi()

calisan4 = Idareci("215463", "Mehmet ARLI","Müdür")
calisan4.CalisanBilgisi()

#######################################################################################################
#super().__init__  /üst_sınıf

class Calisan():
    Odulleri = "" # Sonradan belirleneceği için init içinde değil
    Rutbesi = "" # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy
    def CalisanBilgisi(self):
        print("Çalışan bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN)

calisan1 = Calisan("Erdinç DÖNMEZ","123456")
calisan1.CalisanBilgisi()

class Idareci(Calisan):
    EkUcret = 0 # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---",grv="Henüz hanımlı değil"):
        super().__init__(tc,adSoy)
        self.Gorev = grv
    def CalisanBilgisi(self): # Miras aldığı metodu override ettik. Üzerine yazdık.
        print("Yonetici bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN," Görevi:",self.Gorev)
   
calisan2 = Calisan("Mustafa Beyazit","654321")
calisan2.CalisanBilgisi()

calisan3 = Idareci()
calisan3.CalisanBilgisi()

calisan4 = Idareci("Mehmet ARLI","215463","Müdür")
calisan4.CalisanBilgisi()

#######################################################################################################
#multiple inheritance

class Calisan():
    Odulleri = "" # Sonradan belirleneceği için init içinde değil
    Rutbesi = "" # Sonradan belirleneceği için init içinde değil
    Maasi = 8500
    def __init__(self,tc="---",adSoy="---"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy
    def CalisanBilgisi(self):
        print("Çalışan bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN," Maaşı:",self.Maasi)

class Ogrenci():
    NotOrtalamasi=0  # Sonradan belirleneceği için init içinde değil
    def __init__(self,tc="---",adSoy="---"):
        self.TCKN = tc
        self.AdiSoyadi = adSoy
    def OgrenciBilgisi(self):
        print("Ogrenci bilgileri: Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN," Not ortalaması:",self.NotOrtalamasi)

calisan1 = Calisan("Erdinç DÖNMEZ","123456")
calisan1.CalisanBilgisi()

class Bilgisayarci(Ogrenci,Calisan):
    Gorevi ="---"
    Maasi = 9500
    def CalisanBilgisi(self):
        print("Çalışan bilgileri(bilgisayarcı): Adı Soyadı:",self.AdiSoyadi," TCKN:",self.TCKN," Maaşı:",self.Maasi)
    
agSorumlusu1 = Bilgisayarci("Nuray Cantez","215463")
agSorumlusu1.CalisanBilgisi()
agSorumlusu1.OgrenciBilgisi()

agSorumlusu2 = Calisan("Ahmet KARA","985621")
agSorumlusu2.CalisanBilgisi()

#######################################################################################################
# inheritance + polymorphisme (miras alma + çok biçimlilik) 

class ilan(): # sınıf tanımlama
    def __init__(a,b="0",c="--"): # method
        a.ilanbaslik = c
        a.ilanno = b
    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
            \nBaşlık:{x.ilanbaslik}"
   
# class Evilan(): # sınıf tanımlama
class Evilan(ilan): # ilan sınıfından miras aldı
    def __init__(self, no="0", bas="--",m=0):
        super().__init__(no, bas)
        self.m2 = m
   
    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
        \nBaşlık:{x.ilanbaslik}\nMetrekaresi:{x.m2}"


ilan1 = ilan(333,"Sabinden kelepir")
print(ilan1.bilgiVer())


ilan2 = Evilan(334, "Acil 3+1",110)
print(ilan2.bilgiVer())
