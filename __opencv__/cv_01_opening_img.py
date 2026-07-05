# Ör-2: Resim açma
import cv2
img = cv2.imread('resimler/kizkulesi3.png')
cv2.imshow('Deneme',img)
# cv2.waitKey(3000) # 3 saniye bekle
# cv2.waitKey() # tuşa basılana kadar bekle
tus = cv2.waitKey() # tuşa basılana kadar bekle
# if tus == ord("q") :
cv2.destroyAllWindows() # pencereleri kapa









