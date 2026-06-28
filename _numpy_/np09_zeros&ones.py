 #Sıfır ve bir dizileri
import numpy as np
arr1 = np.zeros((3,4))
print("zeros 3x4:\n",arr1)

arr2 = np.ones((3,5,2))
print("\nones 3d,5x2:\n", arr2)

arr3 = np.ones((3,5))*4
print("\nones 3x5, 4 ile doldur:\n",arr3)

# arange ile aralık
import numpy as np

arr1 = np.arange(10)
print("\narange 10\n",arr1)

arr2 = np.arange(7,30,5)
print("\narange 7-30, 5 er er\n",arr2) 
