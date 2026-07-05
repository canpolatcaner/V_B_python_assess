
# dizi ekleme
import cv2, numpy as np
# img = cv2.imread('resimler/kizkulesi3.png')
# kaynak = cv2.VideoCapture("resimler/MP4_480_1_5MG.mp4")
kaynak = cv2.VideoCapture(0)
while True:
    _, img = kaynak.read()
    cv2.imshow('Deneme',img)
    print(img.shape, type(img))
    dizi1 = np.full((480,640,3),[0,0,100],dtype="uint8")
    cv2.imshow('Deneme1',img+dizi1)
    if cv2.waitKey(1) == ord("q") : break


