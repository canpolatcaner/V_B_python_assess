# #01
# eval("print('Deneme')")

# ##############################################################

# #02 eval
# komut = input("Bir python komutu yaz: ")
# eval(komut)

# ##############################################################

# #03 eval örnek (tek satırlık, dönüşlü ifadeler)
# x = 5
# y = 10
# sonuc = eval("x * y")  # Çalıştırılan ifade: 5 * 10
# print(sonuc)  # Çıktı: 50

# ##############################################################

# #04  exec örnek (çok satırlık komutlar)

# import time
# d = open("ornek.py")
# o = d.readlines()
# for aa in o:
#     # print(a)
#     # eval(aa)
#     exec(aa)
#     time.sleep(2)

# ##############################################################

# # exec ile çoklu komutlar 

# kk = input("Bir python komutu gir:")
# exec (kk)

# ##############################################################
#04  exec örnek (çok satırlık komutlar ve string ifadeler (komutlar) çalıştırılabilir)
kod = """
for i in range(3):
    print("Merhaba Dünya!", i)
"""
exec(kod)

