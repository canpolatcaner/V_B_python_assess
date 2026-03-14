#karenin değerlerini kontrollü hesaplayan basit
kare=input("Lütfen hesaplamak istediğiniz"
               +"karenin bir aygıtının uzunluğunu giriniz\t:")
kare=kare.replace(",",".")
deger=float (kare)
print(deger*4)

#karenin değerlerini kontrollü hesaplayan
while True:
    kare=input("Karenin kenar uzunluğunu giriniz\t:")
    kare=kare.replace(",",".")
    if kare.replace(".","").isdigit():
        deger=float (kare)
        print("Karenin çevresi\t:", deger*4)
        print("Karenin alanı\t:", deger**2)
        break
    else:
        print("Hatalı giriş yaptınız! Lütfen yalnızca sayısal bir değer giriniz.")

#karenin değerlerini döngülü kontrollü hesaplayan
while True:
    kare=input("Karenin kenar uzunluğunu giriniz\t:")
    if kare.lower()=="q": #çıkış kontrolü
        print("Programdan çıkılıyor...")
        break
    kare=kare.replace(",",".")
    if kare.replace(".","").isdigit():
        deger=float (kare)
        print("Karenin çevresi\t:", deger*4)
        print("Karenin alanı\t:", deger**2)
        print("Programdan çıkmak için 'q' tuşuna basınız.")
    else:
        print("Hatalı giriş yaptınız! Lütfen yalnızca sayısal bir değer giriniz.")