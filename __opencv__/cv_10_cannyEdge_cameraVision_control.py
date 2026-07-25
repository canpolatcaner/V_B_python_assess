# Ör: canny ile kenarlıklar
import cv2, numpy as np
kaynak = cv2.VideoCapture(0)
while True:
    _, resim = kaynak.read()
    cv2.imshow('Kamera',cv2.pyrDown(resim))
    kenarlikli = cv2.Canny(resim,100,200)
    cv2.imshow('Kenarlikli',cv2.pyrDown(kenarlikli))
    if cv2.waitKey(1) == ord("q") : break
