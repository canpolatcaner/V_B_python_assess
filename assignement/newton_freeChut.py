#Newton serbest düşüş (h = ½*g*t**2)

def yukseklik(sure):
    g = 9.81
    h = 0.5 * g * sure**2
    return h

def sure(yukseklik):
    g = 9.81
    t = (2 * yukseklik / g)**0.5
    return t

while True:
    print("*"*30)
    sec = input("Yükseklik hesaplamak için Y'ye basınız." +
                "\nSüre hesaplamak için S'ye basınız.\nÇıkmak için 'q''ya basınız:\n" + "*"*30)
    
    if sec.lower() == "q":
        print("Programdan çıkılıyor...")
        break
    
    elif sec.lower() == "y":
        print("-"*30)
        sure_degeri = input("Lütfen süreyi saniye cinsinden giriniz: ")
        try:
            sure_float = float(sure_degeri.replace(",", "."))
            h = yukseklik(sure_float)
            print("-"*30)
            print(f"{sure_float:.2f} saniyede {h:.2f} metre serbest düşer.")
            print("-"*30)
        except ValueError:
            print("Lütfen geçerli bir sayısal değer giriniz.")
    
    elif sec.lower() == "s":
        print("-"*30)
        yukseklik_degeri = input("Lütfen yüksekliği metre cinsinden giriniz: ")
        try:
            yukseklik_float = float(yukseklik_degeri.replace(",", "."))
            t = sure(yukseklik_float)
            print("-"*30)
            print(f"{yukseklik_float:.2f} metreden {t:.2f} saniyede yere varır.")
            print("-"*30)
        except ValueError:
            print("Lütfen geçerli bir sayısal değer giriniz.")
    
    else:
        print("-"*10 + "Hatalı giriş yaptınız!" + "-"*10 +
        "\n\t***Lütfen Y, S veya Q'ya basınız.***")