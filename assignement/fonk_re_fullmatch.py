# # telefon doğrulama örneği
# import re
# def anaekran():
#     telefon = input("Telefon numarasını girin: ")

#     # Sadece 11 haneli, 0 ile başlayan ve rakamlardan oluşan numaraları kabul eder
#     desen = r"^0[5][0-9]{9}$"

#     if re.fullmatch(desen, telefon):
#         print("Telefon numarası geçerli.")
#     else:
#         print("Geçersiz telefon numarası.")
#         print("11 haneli, 0 ile başlayan ve rakamlardan oluşan numara giriniz.")
#     anaekran()

# anaekran()

# # desen = r"^0[5][0-9]{9}$" # Regex Parçası Anlamı
# # ^ Satır başı
# # 0 veya \+90   Sabit giriş
# # [5]   5 ile başlamalı (GSM)
# # [0-9]{9}  9 rakam
# # $ Satır sonu 

################################################################################################################

import re
def anaekran():
    telefon = input("Telefon numarasını girin: ")

    # +90 ile başlayan, sonra 5 ve 9 rakamdan oluşan GSM numarası
    desen = r"^\+90[5][0-9]{9}$"

    if re.fullmatch(desen, telefon):
        print("Telefon numarası geçerli.")
    else:
        print("Geçersiz telefon numarası.")
        print("+90 ile başlayan şekilde bir numara giriniz.")
    anaekran()

anaekran()