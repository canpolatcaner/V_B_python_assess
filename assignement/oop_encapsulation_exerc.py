# kapsulleme / enkapsulation

class ilan(): # sınıf tanımlama
    
    def __init__(a,b="0",c="--",mhn= "not girilmedi"):
        a.ilanbaslik = c
        a.ilanno = b
        
        a.__mhnotu = mhn # kapsullenmis veri
    
    def musteriNotuGir(self,nt):
        self.__mhnotu = nt


    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
            \nBaşlık:{x.ilanbaslik}"
    
    def bilgiverYonetici(x):
        sifre = input("Yonetici şifresi:")
        if sifre=="123":
            return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
            \nBaşlık:{x.ilanbaslik}\nMüşteri h notu:{x.__mhnotu}"
        else:
            return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
            \nBaşlık:{x.ilanbaslik}\nMüşteri h notu: Harika bir müşteri"


ilan12 = ilan(111,"Acil ...")

ilan12.musteriNotuGir("Müşteri biraz sorunlu")
print(ilan12.bilgiverYonetici())

