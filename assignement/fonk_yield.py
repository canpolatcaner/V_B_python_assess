# def sayilar():
#     yield 51
#     yield "selam"
#     yield 3

# gen = sayilar()  # Generator oluştur
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))

def KoltukVer():
    yield 28      
    yield 8
    yield 3


x = KoltukVer()


input("Boş koltuk var mı?")
print(next(x))
input("Boş koltuk var mı?")
print(next(x))
input("Boş koltuk var mı?")
print(next(x))