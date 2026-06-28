# or4 : numpy.full ile dizi doldurma
import numpy as np, cv2
# d1 = np.full((40,60),150, np.uint8)
d1 = np.full((40,60,3),[0,250,0], np.uint8)
print(d1)

cv2.imshow("resim",d1)
cv2.waitKey(0)

# or5 : numpy.full ile dizi doldurma
import numpy as np, cv2
d1 = np.full((40,260,3),[0,200,200], np.uint8)
d2 = np.full((40,260,3),[0,0,250], np.uint8)
# print(d1)

cv2.imwrite("resim4.png",d1) # "resim4" pencere başlığı, d1 gösterilecek resim
cv2.imwrite("resim4.1.png",d2) # imshow metotlarındaki pencere başlığı faklı olmalı
cv2.waitKey(0) 
