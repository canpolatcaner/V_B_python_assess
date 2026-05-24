# init ve metodu
# class Ogrenci(): # Ogrenci adında sınıf tanımı yaptık
#     def __init__(aa,bb,cc): # gelenek gereği aa yerine 'self' yazılır ve self. üzerinden işlemler yapılır
#         aa.adi = bb # özellik/property/prop
#         aa.num = cc  # özellik/property/prop


# # ogrenci1 = Ogrenci() # Ogrenci sınıfından ogrenci1 nesnesi oluşturma
# # ogrenci1.adi = "YAğız"
# # ogrenci1.num = 222
# ogrenci1 = Ogrenci("Berk",22)
# print(ogrenci1.adi)
# print(ogrenci1.num)

# class Ogrenci(): # Ogrenci adında sınıf tanımı yaptık
#     def __init__(aa,bb,cc):
#         aa.adi = bb # özellik/property/prop
#         aa.num = cc  # özellik/property/prop
#     def bilgiVer(xx):
#         return f"\n\nNesne bilgisi:\nAdı:{xx.adi}, Numarası:{xx.num}"


# # ogrenci1 = Ogrenci() # Ogrenci sınıfından ogrenci1 nesnesi oluşturma
# # ogrenci1.adi = "YAğız"
# # ogrenci1.num = 222
# ogrenci1 = Ogrenci("Berk",22)


# # print(ogrenci1.adi)
# # print(ogrenci1.num)
# print(ogrenci1.bilgiVer())

class Ogretmen():
    def __init__(self, adi, bransi):
        self.adi = adi
        self.bransi = bransi

    # Metot sınıfın içinde olmalı ve ilk parametresi 'self' olmalı
    def bilgiver(self):
        return f"Adı: {self.adi}, Branşı: {self.bransi}"

# Verileri tırnak içine alarak string (metin) olarak tanımlıyoruz
ogretmen1 = Ogretmen("Piraye Cosinüs", "Kalkülüs")
ogretmen2 = Ogretmen("Sabit Yüksek", "Fizik")

# 1. Yöntem: Doğrudan özelliklere erişim
print(f"{ogretmen1.adi} : {ogretmen1.bransi}")
print(f"{ogretmen2.adi} : {ogretmen2.bransi}")

# 2. Yöntem: Oluşturduğumuz metodu çağırma
print(ogretmen1.bilgiver())