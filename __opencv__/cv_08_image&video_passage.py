
import cv2, numpy as np
kaynak = cv2.VideoCapture(0)
kaynak1 = cv2.imread("bayrak1.png")
yeni_resim = np.full((480,640,3),[0,0,0],np.uint8)
while True:
    _, resim = kaynak.read()
    
    cv2.imshow('Kamera',cv2.pyrDown(resim))
    for a in range(kaynak1.shape[0]):
        for b in range(kaynak1.shape[1]):
            if kaynak1[a,b][0]>200 and kaynak1[a,b][1]>200 and kaynak1[a,b][2]>200:
                # kaynak1[a,b]=[0,0,0]
                # kaynak1[a,b]=resim[a,b]
                yeni_resim[a,b]=resim[a,b]
            else: yeni_resim[a,b]=kaynak1[a,b]
    cv2.imshow('Resim',cv2.pyrDown(yeni_resim))


    # print(kaynak1.shape)
    if cv2.waitKey(1) == ord("q") : break
