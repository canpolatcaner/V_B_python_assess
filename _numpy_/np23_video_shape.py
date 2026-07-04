import numpy as np, cv2

kaynak = cv2.VideoCapture(0)


while kaynak:
    a, arr =kaynak.read()
    # print(arr.shape, 'satır sayısı', arr.shape[0])
    cv2.imshow("resim", arr)
    y1 = arr[:arr.shape[0]//2]
    y2 = arr[:arr.shape[0]//2:]

    yeniarr =np.array_split(arr, 3)
    cv2.imshow("goruntu", yeniarr[0])

    if cv2.waitKey(1) == ord("q") : break
