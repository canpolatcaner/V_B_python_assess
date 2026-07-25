import cv2
cap = cv2.VideoCapture(0)
bs = cv2.createBackgroundSubtractorMOG2()

while True:
    a, resim = cap.read()
    maske = bs.apply(resim)
    maske = cv2.medianBlur(maske,5)
   
    cv2.imshow("",maske)
    if cv2.waitKey(1)==ord('q') : break

cap.release()
cv2.destroyAllWindows()
 

