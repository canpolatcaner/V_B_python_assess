
# Ör: iki kamera
import cv2, numpy as np
# img = cv2.imread('resimler/kizkulesi3.png')
# kaynak = cv2.VideoCapture("resimler/MP4_480_1_5MG.mp4")
kaynak = cv2.VideoCapture(0)
kaynak1 = cv2.VideoCapture(1)
while True:
    _, img = kaynak.read()
    _, img1 = kaynak1.read()
    print(img.shape, img1.shape)
    cv2.imshow('Deneme',img)
    cv2.imshow('Deneme1',img1)
    cv2.imshow('Deneme2',img+img1)
    if cv2.waitKey(1) == ord("q") : break


