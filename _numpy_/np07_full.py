# or1 : npfull ile dizi doldurma
import numpy as np
d1 = np.full(4,5)
print(d1)

# or2 : iki boyutlu dizi oluşturma
import numpy as np
d1 = np.full((4,5),3)
print(d1)

# or3 : diziyi görselleştirme
import numpy as np
# d1 = np.full((40,60),150, dtype="uint8")
d1=np.full((40,60),150, np.uint8)
print(d1)

import cv2
cv2.imshow("resim",d1)
cv2.waitKey(0)

