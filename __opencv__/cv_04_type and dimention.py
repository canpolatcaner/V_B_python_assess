
# Ör-2: böyut ve tip
import cv2
# img = cv2.imread('resimler/kizkulesi3.png')
# kaynak = cv2.VideoCapture("resimler/MP4_480_1_5MG.mp4")
kaynak = cv2.VideoCapture(0)
while True:
    _, img = kaynak.read()
    cv2.imshow('Deneme',img)
    print(img.shape, type(img))
    if cv2.waitKey(1) == ord("q") : break