# Ör-2: video açma
import cv2
# img = cv2.imread('resimler/kizkulesi3.png')
kaynak = cv2.VideoCapture("resimler/MP4_480_1_5MG.mp4")
while True:
    _, img = kaynak.read()
    cv2.imshow('Deneme',img)


    if cv2.waitKey(1) == ord("q") : break
