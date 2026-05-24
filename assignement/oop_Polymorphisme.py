# Miras alma / inheritence + polimorphizm / çok biçimlilik
class ilan(): # sınıf tanımlama
    def __init__(a,b="0",c="--"): # method
        a.ilanbaslik = c
        a.ilanno = b
    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
            \nBaşlık:{x.ilanbaslik}"
   
class Evilan(ilan): # ilan sınıfından miras aldı
    def __init__(self, no="0", bas="--",m=0):
        super().__init__(no, bas)
        self.m2 = m
   
    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
        \nBaşlık:{x.ilanbaslik}\nMetrekaresi:{x.m2}"


class KiralikEv(Evilan):
    def __init__(self, no="0", bas="--", m=0,dp=10000):
        super().__init__(no, bas, m)
        self.depozito = dp


    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
        \nBaşlık:{x.ilanbaslik}\nMetrekaresi:{x.m2}\
        \nDepozitosu:{x.depozito}"


class SatilikEv(Evilan):
    def __init__(self, no="0", bas="--", m=0,isd=False):
        super().__init__(no, bas, m)
        self.iskan = isd


    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
        \nBaşlık:{x.ilanbaslik}\nMetrekaresi:{x.m2}\
        \nİskanı:{x.iskan}"


class Aracilan(ilan): # ilan sınıfından miras aldı
    def __init__(self, no="0", bas="--",mh=0):
        super().__init__(no, bas)
        self.motorh = mh
   
    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
        \nBaşlık:{x.ilanbaslik}\nMotor hacmi:{x.motorh}cc"


ilan1 = ilan(333,"Sabinden kelepir")
print(ilan1.bilgiVer())


ilan2 = Evilan(334, "Acil 3+1",110)
print(ilan2.bilgiVer())


ilan3 = Aracilan(123,"Öğretmenden az kullanılmış..",1500)
print(ilan3.bilgiVer())


ilan5 = KiralikEv(547,"Eşyasız 2+1 metro yanı",90,5000)
ilan9 = SatilikEv(547,"Eşyasız 2+1 metro yanı",90)
ilan8 = SatilikEv(547,"Eşyasız 2+1 metro yanı",90,"Var")


print(ilan5.bilgiVer(),ilan9.bilgiVer(),ilan8.bilgiVer())


###############################################################################################
# polymorphisme

class Hayvan():
    def __init__(self):
        print("\nHayvan oluştu")

    def sesCikar(self):
        print("Hayvanların çıkardığı sesleri belirtilmedi.")

    def hareketKabiliyeti(self):
        print("Hayvanların hareket şekli belirtilmedi.")

class Kus(Hayvan):
    def __init__(self):
        print("\nKuş oluştu")

    def sesCikar(self):
        print("Kuşlar Cik cik sesi çıkarır")
   
    def hareketKabiliyeti(self):
        print("Kuşlar uçar")

class Ari(Hayvan):
    def sesCikar(self):
        print("Arılar vız vız sesi çıkarır")

h1 = Kus()
h1.sesCikar()
h2 = Ari()
h2.sesCikar()
h2.hareketKabiliyeti() 

###############################################################################################