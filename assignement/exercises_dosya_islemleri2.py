# try:
#     s1 = int(input("1.Sayıyı girin:"))
#     s2 = int(input("2.Sayıyı girin:"))
#     print("Sonuç:",s1/s2)
# # except ZeroDivisionError:
# #     print("2.sayıyı 0 giremezsiniz.")
# except:
#     print("Bir hata oluştu.")

import os

# --- ÖR 1: Mevcut klasörü alma ve dosya yazma ---
su_anki_yer = os.getcwd()
print("Şu anki klasör:", su_anki_yer)

# Mevcut klasöre dosya açıp ekleme yapıyoruz
with open("deneme2.py", "a", encoding="utf-8") as d:
    d.write("\nprint('Merhaba - Bölüm 1')")

print("Dosya mevcut klasöre yazıldı. Devam etmek için Enter...")
input()


# Mevcut yola Z:/ eklemek yerine, gitmek istediğin tam yolu direkt yazmalısın
hedef_yer = "Z:/exercises/" 

# Eğer bu klasör yoksa hata almamak için önce oluşturuyoruz
if not os.path.exists(hedef_yer):
    os.makedirs(hedef_yer)

# Şimdi klasörü değiştiriyoruz
os.chdir(hedef_yer)
print("Yeni klasör konumu:", os.getcwd())

# Yeni klasörde dosya oluşturuyoruz
with open("deneme2.py", "a", encoding="utf-8") as d:
    d.write("\nprint('Merhaba - Yeni Klasörden Selamlar')")


# --- ÖR 3: Klasör içeriğini listeleme ---
print("\n--- Klasördeki Dosyalar ---")
dosya_listesi = os.listdir()
if dosya_listesi:
    print(*dosya_listesi, sep="\n")
else:
    print("Klasör şu an boş.")

