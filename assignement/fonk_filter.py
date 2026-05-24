# filtersiz şekli

# sayilar = [11,22,3,6,8]

# def tekMi(xx):
#     if xx%2 == 0: return False
#     else: return True

# yeniDizi=[]
# for a in sayilar:
#     yeniDizi.append(tekMi(a))
   
# print("Sayılar: ",sayilar)
# print("Yeni Dizi:",yeniDizi)

###############################################

# Filterli fonksiyonu uygulayarak yeni liste döndürür

sayilar = [11,22,3,6,8]

def tekMi(xx):
    if xx%2!=0: return True

yeniDizi=list(filter(tekMi,sayilar))
   
print("Sayılar: ",sayilar)
print("Yeni Dizi:",yeniDizi)

print("Sayılar: ",*sayilar)
print("Yeni Dizi:",*yeniDizi)

###############################################


