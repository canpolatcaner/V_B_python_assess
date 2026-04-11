while True:

    print("\n\n ╔═════════════════════╗")
    print(" ║   TELEFON REHBERİ   ║")
    print(" ╠═════════════════════╣")
    print(" ║  1-Kişi ekle        ║")
    print(" ║  2-Listele          ║")
    print(" ║  3-Ara              ║")
    print(" ║  4-Düzelt           ║")
    print(" ║  C-Çıkış            ║")
    print(" ╚═════════════════════╝")
    secim = input("Seçiminiz nedir?")
    if secim=="1":
        dosya = open("rehber.txt","a",encoding="utf8")
        print("\n\n REHBERE EKLE\n","="*15)
        ad = input(" Ad girin    :")
        nu = input(" Numara girin:")
        dosya.write(f"{ad}#{nu}\n")
        dosya.close()


    if secim=="2":
        dosya = open("rehber.txt","r",encoding="utf8")
        okunan = dosya.readlines()
        # print(okunan)
        print("\n\nKAYIT LİSTESİ\n","-"*30)
        for a in okunan:
            # print(a)
            veriler = a.strip().split("#")
            # for veri in veriler:
            print(veriler[0],"\t",veriler[1])
        
    if secim=="3":
        dosya = open("rehber.txt","r",encoding="utf8")
        okunan = dosya.readlines()
        aranan = input("\n\nAradığınız nedir?")
        for a in okunan:
            veriler = a.strip().split("#")
            for veri in veriler:
                # if veri==aranan:
                if aranan in veri:
                    veriler = a.split("#")
                    print("Adı:",veriler[0],"\t","Numarası:",veriler[1])


    if secim=="4":
        dosya = open("rehber.txt","r",encoding="utf8")
        okunan = dosya.readlines()
        aranan = input("\n\nAradığınız nedir?")
        yeni =   input("\n\nYeni ifade nedir?")
        yeniListe=[]
        for a in okunan:
            veriler = a.strip().split("#")
            for veri in veriler:
                # if veri==aranan:
                if aranan in veri:
                    veriler = a.split("#")
                    if veriler[0] == aranan:
                        veriler[0] = yeni
                    else: veriler[1] = yeni
                    # print("Adı:",veriler[0],"\t","Numarası:",veriler[1])
            yazilacak = f"{veriler[0]}#{veriler[1]}\n"
            yeniListe += yazilacak
        dosya.close()
        dosya = open("rehber.txt","w",encoding="utf8")
        for a in yeniListe:
            dosya.write(a)
