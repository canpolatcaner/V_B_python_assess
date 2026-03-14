# Klavyeden girilen ad, numara vb bilgileri dosyaya kaydeden programı yap.
print("\n\n ╔═════════════════════╗")
print(" ║   TELEFON REHBERİ  ║")
print(" ╠═════════════════════╣")
print(" ║  1-Kişi ekle        ║")
print(" ║  2-Listele          ║")
print(" ║  3-Ara              ║")
print(" ║  C-Çıkış            ║")
print(" ╚═════════════════════╝")
secim = input("Seçiminiz nedir?")
if secim=="1":
    dosya = open("rehber.txt","a", encoding="utf8")
    print("\n\n REHBERE EKLE\n","="*15)
    ad = input(" Ad girin    :")
    nu = input(" Numara girin:")
    dosya.write(f"{ad}#{nu}\n")
    dosya.close()
if secim=="2":
    dosya = open("rehber.txt","r")
    print("\n\n REHBERDEKİLER\n","="*15)
    okunan = dosya.read() #tüm içeriği okur
    #okunan = dosya.read(5) # 5 'karakter' okur
    #dosya.readlines() #satır satır liste olarak okur
    #dosya.readline() #satır satır liste olarak okur

