import cv2

# Kameranın bağlı olduğu bilgisayarın IP adresi ve VLC'de belirlediğimiz port/yol
# Örnek: 192.168.1.10 sunucu bilgisayarının IP'si ile değiştir
stream_url = "http://192.168.1.10"

# Video yakalama nesnesini ağ akışı adresiyle başlatıyoruz
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Hata: Ağ üzerindeki web kamerası yayınına bağlanılamadı!")
    print("Lütfen sunucu bilgisayarın IP adresini ve VLC yayınının açık olduğunu kontrol edin.")
    exit()

print("Ağ kamerasından görüntü alınıyor. Çıkmak için 'q' tuşuna basın.")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Hata: Görüntü akışı durdu.")
        break
        
    # Görüntüyü ekranda göster
    cv2.imshow("Ağ Üzerindeki Everest Kamera", frame)
    
    # 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
