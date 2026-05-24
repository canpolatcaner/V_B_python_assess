# api => pip install requests
# POST ile bilgi gönderme

import requests
url = "https://jsonplaceholder.typicode.com/posts"

GidenVeri = {
    "title": "Merhaba API!",
    "body": "Bu bir deneme gönderisidir.",
    "userId": 1
}

# POST isteği gönder
response = requests.post(url, json=GidenVeri)

# Yanıtı yazdır
print(response.json())

###############################################################################################################################################
# POST ile bilgi gönderme

import requests

# Gönderilecek veri
yeni_kullanici = {
    "name": "Ali",
    "email": "ali@example.com"
}

# Yeni kullanıcı oluşturmak için POST isteği
response = requests.post("https://jsonplaceholder.typicode.com/users", json=yeni_kullanici, verify=False)

# Cevabı kontrol et
if response.status_code == 201:
    print("Kullanıcı başarıyla oluşturuldu!")
else:
    print("Kullanıcı oluşturulamadı!")

###############################################################################################################################################
# GET ile bilgi alma

import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users/1")
response = requests.get("https://jsonplaceholder.typicode.com/users/1", verify=False)
# python -m ensurepip --upgrade # hata verirse sertifikaları yükleyin veya üst satırdaki verify parametresini False değeriyle ekleyin.
# python -m pip install --upgrade certifi

if response.status_code == 200:
    # Yanıtın ham metnini yazdır
    print(response.text)  # veya print(response.content)

# JSON formatında ise veriyi çözümle
try:
    user_data = response.json()
    print(user_data)
except ValueError as e:
    print(f"JSON çözümleme hatası: {e}")

###############################################################################################################################################
# PUT ile veri değiştirme talebi.

import requests

# Güncellenmiş kullanıcı verisi
updated_user = {
    "name": "Ali Veli",
    "email": "ali.veli@example.com"
}

# Kullanıcı bilgilerini güncellemek için PUT isteği
response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=updated_user)

# Cevabı kontrol et
if response.status_code == 200:
    print("Kullanıcı başarıyla güncellendi!")
else:
    print("Kullanıcı güncellenemedi!")

###############################################################################################################################################
# DELETE ile silme isteği

import requests

# Kullanıcıyı silmek için DELETE isteği
response = requests.delete("https://jsonplaceholder.typicode.com/users/1")

# Cevabı kontrol et
if response.status_code == 200:
    print("Kullanıcı başarıyla silindi!")
else:
    print("Kullanıcı silinemedi!")