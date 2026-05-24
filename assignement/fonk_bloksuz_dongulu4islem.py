#fonksiyon bloksuz sonsuz sayılı 4 işlem yapan
print("Hesap Makinesi")
print("Çıkmak için 'q' yazabilirsiniz.")

while True:
    sayilar = []  # kullanıcıdan alınacak sayılar listesi

    print("\nSayıları giriniz (bitirmek için 'q'):")

    while True:
        giris = input("Sayı: ")

        if giris.lower() == "q":
            break

        giris = giris.replace(",", ".")
        if giris.replace(".", "").isdigit():
            sayilar.append(float(giris)) #.append() ile listeye sayı eklenir
        else:
            print("Geçersiz giriş!")

    if not sayilar:  # hiç sayı girilmediyse
        print("Hiç sayı girilmedi, program sonlandırılıyor.")
        break

    islem = input("İşlem seçiniz (+, -, *, /): ")

    sonuc = sayilar[0]
    for s in sayilar[1:]:
        if islem == "+":
            sonuc += s
        elif islem == "-":
            sonuc -= s
        elif islem == "*":
            sonuc *= s
        elif islem == "/":
            if s != 0:
                sonuc /= s
            else:
                print("Sıfıra bölme hatası!")
                sonuc = None
                break
        else:
            print("Geçersiz işlem!")
            sonuc = None
            break

    if sonuc is not None:
        print("Sonuç:", sonuc)