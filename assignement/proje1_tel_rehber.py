import sqlite3

def db_hazirla():
    baglanti = sqlite3.connect("rehber_tel_pk.db")
    kursor = baglanti.cursor()
    # tel1 PRIMARY KEY olarak kalıyor (aynı numaradan iki tane olamaz)
    kursor.execute("""
        CREATE TABLE IF NOT EXISTS rehber (
            tel1 TEXT PRIMARY KEY,
            isim TEXT NOT NULL,
            soyisim TEXT NOT NULL,
            tel2 TEXT,
            eposta TEXT,
            is_adresi TEXT,
            ev_adresi TEXT
        )
    """)
    baglanti.commit()
    baglanti.close()

def kisi_ekle():
    print("\n--- 🆕 YENİ KAYIT EKLE ---")
    # İstediğin gibi önce İsim bilgisini alıyoruz
    isim = input("İsim*: ")
    soyisim = input("Soyisim*: ")
    tel1 = input("Telefon 1 (Anahtar)*: ") # Benzersiz olması gereken alan
    
    # Opsiyonel alanlar
    tel2 = input("Telefon 2 (İsteğe bağlı): ") or None
    eposta = input("E-posta (İsteğe bağlı): ") or None
    is_adres = input("İş Adresi (İsteğe bağlı): ") or None
    ev_adres = input("Ev Adresi (İsteğe bağlı): ") or None

    if not isim or not tel1:
        print("❌ Hata: İsim ve Telefon 1 alanları zorunludur!")
        return

    try:
        baglanti = sqlite3.connect("rehber_tel_pk.db")
        kursor = baglanti.cursor()
        kursor.execute("INSERT INTO rehber VALUES (?,?,?,?,?,?,?)", 
                       (tel1, isim, soyisim, tel2, eposta, is_adres, ev_adres))
        baglanti.commit()
        baglanti.close()
        print(f"✅ {isim} {soyisim} başarıyla rehbere kaydedildi.")
    except sqlite3.IntegrityError:
        print(f"❌ Hata: '{tel1}' numarası rehberde zaten mevcut! Farklı bir numara deneyin.")

def duzenleme_modu():
    print("\n" + "═"*50)
    print(f"{'🛠 KAYIT DÜZENLEME (TASLAK MODU)':^50}")
    print("═"*50)
    
    # 1. Adım: Kişiyi Bulma (Anahtar olan Telefon üzerinden)
    hedef_tel = input("Düzenlenecek kişinin Telefon Numarasını (Tel1) girin: ")
    kayit = kayit_getir(hedef_tel)

    if not kayit:
        print("❌ Hata: Bu numaraya sahip bir kayıt bulunamadı!")
        return

    # 2. Adım: Veriyi Belleğe (Taslağa) Alıyoruz
    taslak = kayit.copy()
    
    while True:
        print("\n" + "─"*30)
        print("TASLAK ÜZERİNDEKİ GÜNCEL BİLGİLER:")
        # Sütunları tek tek gösterelim
        for anahtar, deger in taslak.items():
            is_pk = " [ANAHTAR]" if anahtar == "tel1" else ""
            print(f"👉 {anahtar.upper()}{is_pk}: {deger if deger else '(Boş)'}")
        print("─"*30)
        
        print("\nKomutlar: [isim, soyisim, tel1, tel2, eposta, is_adresi, ev_adresi]")
        print("Kaydetmek için: 'S' | İptal edip çıkmak için: 'Q'")
        
        secim = input("\nDeğiştirmek istediğiniz alan adını yazın: ").lower()

        if secim == 's':
            onay = input("⚠️ Değişiklikleri veritabanına kaydetmek istiyor musunuz? (E/H): ").lower()
            if onay == 'e':
                try:
                    baglanti = sqlite3.connect("rehber_tel_pk.db")
                    kursor = baglanti.cursor()
                    sorgu = """
                        UPDATE rehber SET 
                        tel1 = ?, isim = ?, soyisim = ?, tel2 = ?, 
                        eposta = ?, is_adresi = ?, ev_adresi = ?
                        WHERE tel1 = ?
                    """
                    # taslak['tel1'] yeni numara, hedef_tel ise eski (orijinal) numara
                    kursor.execute(sorgu, (
                        taslak['tel1'], taslak['isim'], taslak['soyisim'],
                        taslak['tel2'], taslak['eposta'], taslak['is_adresi'],
                        taslak['ev_adresi'], hedef_tel
                    ))
                    baglanti.commit()
                    baglanti.close()
                    print("✅ BAŞARILI: Veritabanı güncellendi.")
                    break
                except sqlite3.IntegrityError:
                    print("❌ HATA: Girdiğiniz yeni telefon numarası başka bir kayıtta zaten var!")
            else:
                print("İşlem tamamlanmadı, taslak hala geçerli.")

        elif secim == 'q':
            print("❌ İşlem iptal edildi. Hiçbir değişiklik kaydedilmedi.")
            break
        
        elif secim in taslak:
            yeni_deger = input(f"Yeni {secim} değerini girin: ")
            taslak[secim] = yeni_deger if yeni_deger else None
        else:
            print("⚠️ Geçersiz alan adı! Lütfen ekrandaki seçeneklerden birini yazın.")
def listele():
    baglanti = sqlite3.connect("rehber_tel_pk.db")
    kursor = baglanti.cursor()
    kursor.execute("SELECT * FROM rehber") # Tüm verileri çekiyoruz
    veriler = kursor.fetchall()
    baglanti.close()
    
    print("\n" + "═"*50)
    print(f"{'📋 REHBERDEKİ TÜM KİŞİLER':^50}")
    print("═"*50)

    if not veriler:
        print("Rehber şu an boş.")
    else:
        for v in veriler:
            # Sütun sırası: tel1, isim, soyisim, tel2, eposta, is_adresi, ev_adresi
            print(f"👤 AD SOYAD  : {v[1]} {v[2]}")
            print(f"📞 ANA TEL   : {v[0]}")
            
            # Sadece dolu olan (None olmayan) alanları gösterelim
            if v[3]: print(f"📱 YEDEK TEL : {v[3]}")
            if v[4]: print(f"📧 E-POSTA   : {v[4]}")
            if v[5]: print(f"🏢 İŞ ADRESİ : {v[5]}")
            if v[6]: print(f"🏠 EV ADRESİ : {v[6]}")
            print("─"*50) 

def ana_menu():
    db_hazirla()
    while True:
        print("\n[1] Kişi Ekle")
        print("[2] Tüm Rehberi Listele")
        print("[3] Kayıt Düzenle (Taslak Modu)")
        print("[4] Çıkış")
        islem = input("Seçiminiz: ")

        if islem == "1": kisi_ekle()
        elif islem == "2": listele()
        elif islem == "3": 
            # Daha önce yazdığımız duzenleme_modu() buraya gelebilir
            print("Düzenleme modu çalıştırılıyor...")
        elif islem == "4": break

if __name__ == "__main__":
    ana_menu()
