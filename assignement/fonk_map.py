# # map bir dizinin her bir elemanına işlem yaparak yeni liste

# def kare(x):
#     return x * x


# sayılar = [1, 2, 3, 4, 5]
# sonuç = map(kare, sayılar)
# print(list(sonuç))  # [1, 4, 9, 16, 25]

###############################################################################################
# def unvanEkle(gelen):
#     if gelen["cinsiyet"].lower() in ["kadın","k"]: return f"Bayan: {gelen["ad"]}"
#     if gelen["cinsiyet"].lower() in ["erkek","e"]: return f"Bay: {gelen["ad"]}"


# basilacakE = [
#     {"ad":"Dağhan","cinsiyet":"Erkek"},
#     {"ad":"Ela","cinsiyet":"K"},
#     {"ad":"Polat","cinsiyet":"erkek"},
#     {"ad":"Elif","cinsiyet":"Kadın"},
#     ]
# sonuç = map(unvanEkle, basilacakE)
# print("\n\nEtikete basılacak isimler:\n",list(sonuç)) 

###############################################################################################

# # mapsiz şekli
# urunFiyatlari = [100,200,30]

# def yariyaIndir(xx):
#     return xx//2

# yeniFiyatlar=[]
# for a in range(len(urunFiyatlari)):
#     yeniFiyatlar.append(yariyaIndir(urunFiyatlari[a]))
   
# print("urunFiyatlari:",urunFiyatlari)
# print("yeniFiyatlar:",yeniFiyatlar)

###############################################################################################

# map li şekli
urunFiyatlari = [100,200,30]

def yariyaIndir(xx):
    return xx//2

yeniFiyatlar = list(map(yariyaIndir,urunFiyatlari))  
print("yeniFiyatlar:",yeniFiyatlar)

# 'map'li ve 'lambda'lı şekli
fiyatlar = [100, 200, 30]
indirimli = list(map(lambda x: x // 2, fiyatlar))
print("fiyatlar :",fiyatlar )
print("indirimli:",indirimli)