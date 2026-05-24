def islem(s1, s2):
   
    try:
        print(f"\nSeçtiğiniz 1'inci sayı: {s1}\nSeçtiğiniz 2'nci sayı: {s2}\n")
        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (+, -, /, *): ")
        
        if secim == "+":
            print(f"Sonuç: {s1} + {s2} = {s1 + s2}")
        elif secim == "-":
            print(f"Sonuç: {s1} - {s2} = {s1 - s2}")
        elif secim == "*":
            print(f"Sonuç: {s1} * {s2} = {s1 * s2}")
        elif secim == "/":
            if s2 == 0:
                print("Hata: Bir sayı sıfıra bölünemez!")
            else:
                print(f"Sonuç: {s1} / {s2} = {s1 / s2}")
        else:
            print("Hata: Geçersiz işlem seçtiniz.")
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

while True:
    print("\n--- Yeni İşlem (Çıkmak için 'q' ya basınız) ---")
    
   
    girdi1 = input("1. Sayıyı giriniz: ").replace(",", ".")
    if girdi1.lower() == 'q':
        break
        
    try:
        sayi1 = float(girdi1)
    except ValueError:
        print("Lütfen geçerli bir sayısal değer giriniz!")
        continue          
   
    girdi2 = input("2. Sayıyı giriniz: ").replace(",", ".")
    if girdi2.lower() == 'q':
        break
        
    try:
        sayi2 = float(girdi2)
    except ValueError:
        print("Lütfen geçerli bir sayısal değer giriniz!")
        continue  

    
    islem(sayi1, sayi2)

print("Programdan çıkıldı.")