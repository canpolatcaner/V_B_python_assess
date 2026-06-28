# Dizi elemanlarını işleme tabi tutma
import numpy as np, cv2

dizi1 = np.array([ # 4 satır, 3 sütun ve
    [[0,0,50],[0,00,250]],
    [[0,50,00],[0,250,0]],
    [[50,0,0],[250,0,0]],
    [[0,0,0],[50,50,50]],
    [[250,250,250],[250,250,250]],
],dtype="uint8")
print("\n\ndizi1:\n",dizi1)

#cv2.imshow("Resim5:",dizi1)
cv2.imwrite("resim5.png",dizi1)
# print("\n\nDizi elemanlarını xx ile çarpma:\n",dizi1*4)
# print("\n\nDizi elemanlarına xx ekleme:\n",dizi1+4)
print("\n\nDizi elemanlarından xx çıkarma:\n",dizi1-30)
# print("\n\nDizi elemanlarını xx'e bölme:\n",dizi1//2)

#cv2.imshow("Resim5.1:",dizi1-30)
cv2.imwrite("resim5.1.png",dizi1-30)
cv2.waitKey(0)
cv2.destroyAllWindows() 
