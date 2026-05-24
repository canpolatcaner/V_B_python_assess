import hashlib


# metin = "Merhaba, Python!"
metin = input("Şifre:")
hash_sonucu = hashlib.sha256(metin.encode()).hexdigest()


# print("SHA-256 Hash değeri:", hash_sonucu)
# encode(), string’i byte formatına çevirir.
# hexdigest(), çıktıyı 16’lık (hexadecimal) formatta döndürür.
ds1="f1060889b9c1de999eb7306dce028e0528c703e7ed64d19d1c7655de9bd5a545"
if hash_sonucu == ds1 : print("şifre doğru")
else: print("yanlış")