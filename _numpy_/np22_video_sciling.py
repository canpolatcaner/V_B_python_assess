import numpy as np, cv2

kaynak = cv2.VideoCapture(0)


while kaynak:
    a, arr =kaynak.read()
    # print(arr.shape, 'satır sayısı', arr.shape[0])
    cv2.imshow("resim", arr)
    if cv2.waitKey(1) == ord("q") : break

    # cv2.imshow("video", arr[:100])
   
    birlesik2 = np.concat((arr[240:], arr[:240]))
    # birlesik3 = np.concat(birlesik2, birlesik)
    cv2.imshow("video1", birlesik2)
  


