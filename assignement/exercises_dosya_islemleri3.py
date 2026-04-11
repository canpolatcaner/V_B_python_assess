import os
from datetime import datetime, timedelta

kayit_no = []

def müsteri_kayit(): 
    try:
        musteri_kayit_no = input("TC kimlik no:").strip().replace(".", "")
        
        if musteri_kayit_no.isdigit() and len(musteri_kayit_no) == 11:
            print("Müşteri eklendi")
            kayit_no.append(musteri_kayit_no)
            return musteri_kayit_no 
        else:
            print("Lütfen TC kimlik numarasını 11 haneli ve doğru giriniz.")
            return müsteri_kayit()
    except Exception:
        return müsteri_kayit()

# 1. Klasör yolunu ve dosya adını birleştiriyoruz
tc_no = müsteri_kayit()
hedef_klasor = "Z:/exercises/"

# Klasör yoksa oluştur (Hata almamak için önemli)
if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)

# Dosya yolunu tam olarak tanımlıyoruz
tam_dosya_yolu = f"{hedef_klasor}{tc_no}.txt"

musteri_ad_soyad = input("Müşteri adı soyadı:")
musteri_adres = input("Müşterinin adresi:")
arac_ruhsat_no = input("Araç ruhsat numarası:")
arac_model = input("Aracın modeli:")
trafik_cikis = input("Aracın trafiğe çıktığı tarih:")
ariza = input ("Müşteri tarafından belirtilen arıza:")

# Giriş tarihini döngü dışında alıyoruz ki her seferinde sıfırlanmasın
giris_tarihi = datetime.now()

# 2. Yazma işlemini tam_dosya_yolu üzerinden yapıyoruz
with open(tam_dosya_yolu, "w", encoding="utf-8") as d:
    d.write(f"Müşteri Bilgisi: {musteri_ad_soyad}\n")
    d.write(f"Müşteri Kimlik Numarası: {tc_no}\n")
    d.write(f"Adres Bilgisi: {musteri_adres}\n")
    d.write(f"Araba Ruhsat Numarası: {arac_ruhsat_no}\nAraba Model: {arac_model}\n")
    d.write(f"Trafiğe çıkış tarihi: {trafik_cikis}\n")
    d.write(f"Müşteri tarafından belirtilen arıza: {ariza}\n")
    d.write(f"Araç giriş tarihi: {giris_tarihi.strftime('%d.%m.%Y %H:%M')}\n")

print(f"Kayıt başarıyla oluşturuldu: {tam_dosya_yolu}")

su_anki_yer = os.getcwd()
print("Şu anki klasör:", su_anki_yer)


# gitmek istediğin tam yolu direkt yazmalısın
hedef_yer = r"Z:\erdincdonmez hoca\python119\caner_canpolat" 

# Eğer bu klasör yoksa hata almamak için önce oluşturuyoruz
if not os.path.exists(hedef_yer):
    os.makedirs(hedef_yer)

# Şimdi klasörü değiştiriyoruz
os.chdir(hedef_yer)
print("Yeni klasör konumu:", os.getcwd())

# Yeni klasörde dosya oluşturuyoruz
with open("müşteri_listesi.txt", "a", encoding="utf-8") as d:
    d.write(f"Müşteri Bilgisi: {musteri_ad_soyad}\n")
    d.write(f"Müşteri Kimlik Numarası: {tc_no}\n")
    d.write(f"Adres Bilgisi: {musteri_adres}\n")
    d.write(f"Araba Ruhsat Numarası: {arac_ruhsat_no}\nAraba Model: {arac_model}\n")
    d.write(f"Trafiğe çıkış tarihi: {trafik_cikis}\n")
    d.write(f"Müşteri tarafından belirtilen arıza: {ariza}\n")
    d.write(f"Araç giriş tarihi: {giris_tarihi.strftime('%d.%m.%Y %H:%M')}\n")


# --- ÖR 3: Klasör içeriğini listeleme ---
print("\n--- Klasördeki Dosyalar ---")
dosya_listesi = os.listdir()
if dosya_listesi:
    print(*dosya_listesi, sep="\n")
else:
    print("Klasör şu an boş.")