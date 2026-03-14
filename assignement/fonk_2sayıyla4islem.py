##2 sayıyla 4 işlem yaptıran
print("Basit Hesap Makinesi")
print("Çıkmak için 'q' yazabilirsiniz.")

while True:
    sayi = input("Bir sayı giriniz (çıkmak için q): ")

    # Çıkış kontrolü
    if sayi.lower() == "q": # xxx.lower()=='q' küçük harfe dönüştürerek işler, mantığı; büyük harf girmiş olsa bile çıkış alır
        print("Program sonlandırıldı.")
        break

    # Virgül -> nokta
    sayi = sayi.replace(",", ".")

    # Geçerli sayı mı?
    if sayi.replace(".", "").isdigit():
        sayi = float(sayi)

        # Kullanıcıdan işlem türünü soralım
        islem = input("İşlem seçiniz (+, -, *, /): ")

        # İkinci sayıyı alalım
        sayi2 = input("İkinci sayıyı giriniz: ")
        sayi2 = sayi2.replace(",", ".")
        
        if sayi2.replace(".", "").isdigit():
            sayi2 = float(sayi2)

            # İşlem kontrolü
            if islem == "+":
                print("Sonuç:", sayi + sayi2)
            elif islem == "-":
                print("Sonuç:", sayi - sayi2)
            elif islem == "*":
                print("Sonuç:", sayi * sayi2)
            elif islem == "/":
                if sayi2 != 0:
                    print("Sonuç:", sayi / sayi2)
                else:
                    print("Sıfıra bölme hatası!")
            else:
                print("Geçersiz işlem seçtiniz.")
        else:
            print("İkinci sayı hatalı!")
    else:
        print("Bir sayı girmeniz gerekiyor!")