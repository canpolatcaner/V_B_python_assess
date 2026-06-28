# concatenate ile birleştirme
import numpy as np
d1 = np.full((200,200,3),[0,0,255],np.uint8)
d2 = np.full((200,200,3),[0,255,0],np.uint8)
d3 = np.full((200,200,3),[255,0,0],np.uint8)
d4 = np.full((200,200,3),[0,255,255],np.uint8)

import cv2
cv2.imshow("resim1",d1)
cv2.imshow("resim2",d2)
cv2.imshow("resim3",d3)
cv2.imshow("resim4",d4)
d5 = np.concatenate((d1,d2),axis=1)
d6 = np.concatenate((d3,d4),axis=1)
d7 = np.concatenate((d5,d6))
cv2.imshow("resim5",d7)

cv2.waitKey(0) 
