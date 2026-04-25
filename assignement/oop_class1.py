#Sınıf adları büyük harfle başlar ve tekil olur, çoğul olmaz. 
#sınıf tanımlama
# class Ogrenci(): # şeklinde de kullanılabilir.

class Ogrenci:
# class Ogrenci():
    print("Öğrenci sınıfı çalıştı") 
    ad = "---"
    soyad = "tanımsız"
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0

print(Ogrenci) # Sınıf tanımı
print(Ogrenci()) # sınıf tanımının init edilmiş şekli

# sınıfın özelliklerine ulaşma
print("Öğrenci adı:",Ogrenci.ad)
print("Öğrenci adı:",Ogrenci().ad)
print("Öğrenci soyadı:",Ogrenci().soyad)

############################################################################################
# sınıftan referans üretme

class Ogrenci:
    print("Öğrenci sınıfı çalıştı") 
    ad = "---"
    soyad = ""
    numara = ""
    disiplinCezasi = 0

print("Ogrenci.ad:",Ogrenci.ad)
ogrenci1 = Ogrenci # aynı adlı sınıf tanımladık.

ogrenci1.ad = "Ali"
print("ogrenci1.ad:",ogrenci1.ad)
print("Ogrenci.ad:",Ogrenci.ad)
Ogrenci.ad = "Veli"
print("ogrenci1.ad:",ogrenci1.ad)
print("Ogrenci.ad:",Ogrenci.ad)
print("Ogrenci  : ",Ogrenci)
print("ogrenci1 : ",ogrenci1)

################################################################################################

class Ogrenci(): # Sınıf isimleri büyük harf ile başlar.
    ogrenci_no = "--" # ogrenci_no /prop/property/özellik
    adi_soyadi = "Tanımsız"

ogrenci5 = Ogrenci()
ogrenci1 = Ogrenci() # parantezler sınıftan nesne oluşturma için init yapar
ogrenci2 = Ogrenci()
ogrenci3 = Ogrenci # sınıftn nense oluşturmaz. Ogrenci sınıfının referansını ogrenci3'e atar
ogrenci4 = Ogrenci # sınıftn nense oluşturmaz. Ogrenci sınıfının referansını ogrenci4'e atar

ogrenci1.adi_soyadi = "Öznur KARA"
ogrenci2.adi_soyadi = "Reyhan KAYA"
ogrenci3.adi_soyadi = "Betül DOĞRUYOL"
ogrenci4.adi_soyadi = "Beyza ARI"

print(ogrenci1.ogrenci_no, ogrenci1.adi_soyadi)
print(ogrenci2.ogrenci_no, ogrenci2.adi_soyadi)
print(ogrenci3.ogrenci_no, ogrenci3.adi_soyadi)
print(ogrenci4.ogrenci_no, ogrenci4.adi_soyadi)
print(ogrenci5.ogrenci_no, ogrenci4.adi_soyadi) 

################################################################################################
#sınıfa metot ekleme

class Ogrenci:
    ad = "---"
    soyad = "tanımsız"
    numara = ""
    disiplinCezasi = 0

    def bilgi(self):
        print ("Metod ile: Adı:",self.ad,", Soyadı:",self.soyad, ", Disiplin cezası:",self.disiplinCezasi)
   
    def disiplinCezasiEkle(self,eklenecek):
        self.disiplinCezasi += eklenecek


print("Ogrenci.ad:",Ogrenci.ad)
print("Ogrenci.disiplinCezasi:",Ogrenci.disiplinCezasi)
ogrenci1 = Ogrenci()

ogrenci1.bilgi()
Ogrenci.ad = "Ali"
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.bilgi()

################################################################################################
#sınıf içerisindeki varlıklara bakma

class Ogrenci:
	
    ad = "---"
    soyad = "tanımsız"
    numara = ""
    disiplinCezasi = 0

    def bilgi(self):
        print ("Metod ile: Adı:",self.ad,", Soyadı:",self.soyad, ", Disiplin cezası:",self.disiplinCezasi)
   
    def disiplinCezasiEkle(self,eklenecek):
        self.disiplinCezasi += eklenecek

print("Ogrenci.ad:",Ogrenci.ad)
print("Ogrenci.disiplinCezasi:",Ogrenci.disiplinCezasi)
ogrenci1 = Ogrenci()

ogrenci1.bilgi()
Ogrenci.ad = "Ali"
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.bilgi()

print("\n\nOgrenci varlıkları:\n",Ogrenci.__dict__) # Sınıf varlıklarını gösterme.
print("\n\nogrenci1 varlıkları:\n",ogrenci1.__dict__) 

