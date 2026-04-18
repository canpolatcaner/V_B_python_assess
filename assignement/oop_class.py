a = 12
b = "Ankara"

print(a,type(a))
print(b,type(b))


class ilan(): # sınıf tanımlama
    # 1-özellikleri/prop/property/properties 2-metod/yöntem/sınıf fonksiyonu
    ilanno = "000"
    ilanbaslik = "---"


# ilan1 = ilan # nesne oluşturmak için doğru bir yöntem değil. Bu şekilde sınıftan referans sınıf oluşur
ilan1 = ilan() # initialization/oluşturma/başlatma ile sınıftan yeni bir nesne oluşturma


print(ilan1, type(ilan1))
print(ilan1.ilanno, ilan1.ilanbaslik)


ilan1.ilanno = 222; ilan1.ilanbaslik="Acil satılık..."
print(ilan1.ilanno, ilan1.ilanbaslik)

# init metodu / constuctor / yapıcı method
class ilan(): # sınıf tanımlama
    ilanno = "000"
    ilanbaslik = "---"
    def __init__(a,b="0",c="--"): # sınıf içindeki fonk = method
        a.ilanbaslik = c
        a.ilanno = b


ilan1 = ilan() # initialization
ilan1.ilanno = 222
ilan1.ilanbaslik="Acil satılık..."
print(ilan1.ilanno, ilan1.ilanbaslik)


ilan2 = ilan(333,"Sabinden kelepir")
print(ilan2.ilanno, ilan2.ilanbaslik)

ilanEv= ilan(525, "3+1 Asansörlü")
print(ilanEv.ilanbaslik, ilanEv.ilanno)

##########################################################################################################################

# metod tanımlama
class ilan(): # sınıf tanımlama
    ilanno = "000"
    ilanbaslik = "---"
    def __init__(a,b="0",c="--"): # method
        a.ilanbaslik = c
        a.ilanno = b
    def bilgiVer(x):
        return f"\n\nİlan Bilgisi:\nNo    :{x.ilanno}\
            \nBaşlık:{x.ilanbaslik}"


ilan1 = ilan(222,"Acil satılık...") # initialization
print(ilan1.ilanno, ilan1.ilanbaslik)


ilan2 = ilan(333,"Sabinden kelepir")
print(ilan2.bilgiVer())
