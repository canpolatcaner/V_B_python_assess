import cv2, numpy as np

resim = cv2.imread("resimler/kedi.png")
hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)  # HSV renk uzayına çevir

# Arka planın rengine göre eşikleme (Örneğin beyaz veya açık renk)
alt_sinir = np.array([0, 0, 200])  # Açık tonlar için alt sınır
ust_sinir = np.array([180, 50, 255])  # Açık tonlar için üst sınır

# Maske oluştur (arka planı tespit etmek için)
maske = cv2.inRange(hsv, alt_sinir, ust_sinir)

# Maske ters çevirme (Sadece kediyi almak için)
maske_ters = cv2.bitwise_not(maske)

# Kediyi arka plandan ayır
kedi_sadece = cv2.bitwise_and(resim, resim, mask=maske_ters)

cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Maske", maske_ters)
cv2.imshow("Arka Planı Kaldırılmış Kedi", kedi_sadece)

cv2.waitKey(0)
cv2.destroyAllWindows()



