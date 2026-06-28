# Birim matris
import numpy as np

arr1 = np.eye(5)
print(arr1)


# bir dizinin tersi
import numpy as np

arr1 = np.arange(1,11)
arr1 = arr1.reshape(5,2)

tersi = arr1[::-1]
print("Dizi :\n",arr1)
print("Tersten:\n",tersi) 
