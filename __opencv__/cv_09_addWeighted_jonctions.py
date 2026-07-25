# Ör: addWeighted ile birleştirme
import cv2, numpy as np, random
kaynak = cv2.VideoCapture(0)
kaynak1 = cv2.imread("resimler/bayrak1-480x640.png")
while True:
    _, resim = kaynak.read()
    cv2.imshow('Kamera',cv2.pyrDown(resim))
    cv2.imshow('resim',cv2.pyrDown(kaynak1))
    birlesik = cv2.addWeighted(resim, 0.7, kaynak1, 0.3, 100)
    cv2.imshow('Birlesik',cv2.pyrDown(birlesik))




    # print(kaynak1.shape)
    if cv2.waitKey(1) == ord("q") : break
