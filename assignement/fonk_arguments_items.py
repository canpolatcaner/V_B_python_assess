def rapor_olustur(**gelenveri):
    # print("gelenveri:\n",gelenveri)
    print(f"{gelenveri["Doktor"]}'in Rapor Özeti:")
    # for key, value in gelenveri.items():
    for a, b in gelenveri.items():
        if a != "Doktor": 
            print(f"- {a}: {b}")
            #print(f"{b}")

# Kullanım
rapor_olustur(
    Doktor="Engin GÜZEL",
    Ad="Erdinç Dönmez",
    Yaş=27,
    Şehir="Ankara",
    Meslek="Yazılım Geliştirici",
    Hastaslık="Kemikte çatlak tespiti",
    İstirahat="5 gün istirahati uygundur"
    # İstirahat=""
)
