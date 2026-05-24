# lambda ile tek satırlık anonim fonksiyon
def aa(x):
    return x*2
# print(aa("Merhaba "))


# yerine lambda fonksiyonu sayesinde kullanımı kolaylaştırıyoruz.


# print((lambda x:x*2')("Merhaba ")) # anonim fonksiyon
print((lambda x:f'Sayın:{x}')("Fatih ")) # anonim fonksiyon