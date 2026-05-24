# # sınıf ve nesne tanımlama
# # int a = 4
# a = 4
# print(a, type(a))
# b = "Ankara"
# print(b, type(b))


# class Ogrenci(): # Ogrenci adında sınıf/tip/type tanımı yaptık
#     adi = "--" # özellik/property/prop
#     num = 0  # özellik/property/prop

# ogrenci1 = Ogrenci() # Ogrenci sınıfından ogrenci1 nesnesi tanımlama/inititialize etme/oluşturma
# print(ogrenci1)
# print(ogrenci1.adi)
# print(ogrenci1.num)
# ogrenci1.adi = "YAğız"
# ogrenci1.num = 222
# print(ogrenci1.adi)
# print(ogrenci1.num)
# print(type(ogrenci1))

class Ogretmen():
    adi = "--"
    bransi = "//"

ogretmen1 = Ogretmen()
ogretmen1.adi = "Hafize Selçuklu"
ogretmen1.bransi = "Tarih"

ogretmen2 = Ogretmen()
ogretmen2.adi = "Sabit Yüksek"
ogretmen2.bransi = "Fizik"

ogretmen3 = Ogretmen()
ogretmen3.adi = "Piraye Cosinus"
ogretmen3.bransi = "Kalkülüs"

print(ogretmen1.adi, ":", ogretmen1.bransi)
print(ogretmen3.adi, ":", ogretmen3.bransi)
print(ogretmen2.adi)
print(ogretmen2.bransi)

