# Opencv ile Serit Takibi
# https://www.istockphoto.com/tr/video/driving-a-car-on-a-road-in-norway-at-dawn-gm1642297710-533365583?utm_source=pixabay&utm_medium=affiliate&utm_campaign=sponsored_video&utm_content=srp_topbanner_media&utm_term=yol+yol
import cv2, numpy as np
cap = cv2.VideoCapture("resimler/yol1.mp4") # Video veya kamera # Kamera: 0

def roi(img):
    h, w = img.shape[:2]
    mask = np.zeros_like(img)
    polygon = np.array([[(0, h),(w, h),(w, int(h*0.6)),(0, int(h*0.6))]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

while True:
    ret, frame = cap.read()
    if not ret: break

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (5,5), 0)
    kenarlar = cv2.Canny(blur, 50, 150)
    mask = roi(kenarlar)

    # Hough çizgilerini bul
    lines = cv2.HoughLinesP(mask, 1, np.pi/180, 50, minLineLength=50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0,255,0), 3)

    cv2.imshow("Serit Takibi", frame)
    if cv2.waitKey(1) == 27: break

cap.release(); cv2.destroyAllWindows() 
