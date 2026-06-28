#  tahtası
import numpy as np, cv2
boyut = 75
d1 = np.full((boyut,boyut,4),[100,100,0,0], np.uint8)
d2 = np.full((boyut,boyut,4),[1,1,125,125], np.uint8)

s1 = np.concat((d2,d1,d2,d1,d2,d1,d2,d1,d2,d1),axis=1)
s2 = np.concat((d1,d2,d1,d2,d1,d2,d1,d2,d1,d2),axis=1)

r = np.concat((s1,s2,s1,s2,s1,s2,s1,s2,s1))
cv2.imshow("Satranc tahtasi",r)
cv2.waitKey(0)


# Satranç tahtası
boyut =50

d1 = np.full((boyut,boyut,3),[50,50,50], np.uint8)
d2 = np.full((boyut,boyut,3),[1,1,1], np.uint8)

s1 = np.concat((d2,d1,d2,d1,d2,d1,d2,d1),axis=1)
s2 = np.concat((d1,d2,d1,d2,d1,d2,d1,d2),axis=1)


r1 = np.concat((s1,s2,s1,s2,s1,s2,s1,s2))
cv2.imshow("Satranc tahtasi1",r1)
cv2.imwrite("resim3.png",r1)
cv2.waitKey(0)
