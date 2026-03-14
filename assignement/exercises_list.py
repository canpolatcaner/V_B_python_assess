import random
sayi=[5,8,2]
sayi+=[1,7,3] # bu şekilde liste halinde eklenir
print(sayi)
sayi+=[19]
print(sayi)
sayi.append(21)
print(sayi)
sayilar=[15,85,64]
sayi.extend (sayilar)
print(sayi)
sayi.sort()
print(sayi)
sayi.sort(reverse=True)
print(sayi)
print(sayi[::1])
sayi.reverse
print(sayi)
print(random.choice(sayi))
print(random.sample(sayi, k=4))
dizi=list("caner canpolat")
print(dizi)
dizi+=["elma","armut"]
print(dizi)
dizi.sort()
dizi.sort(reverse=True)
print (dizi)
dizi.pop()
print(dizi)
dizi.remove("elma")
print(dizi)
dizi.pop(7)
print(dizi)
dizi.remove("armut")
print(dizi)
print(dizi.count("a"))
print(len(dizi))