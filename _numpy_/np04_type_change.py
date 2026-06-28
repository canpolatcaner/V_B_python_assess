import numpy as np

arr7 = np.array([1.1, 2.1, 3.1])
print("arr7.dtype :", arr7.dtype, arr7)
newarr7 = arr7.astype('i') # tür dönüştürme yapılabilir.
print("newarr.dtype :", newarr7.dtype, newarr7)

arr8 = np.array([1.1, 2.1, 3.1])
print("arr8.dtype :",arr8.dtype, arr8)
newarr8 = arr8.astype(int) # int te kullanabilirsiniz.
print("newarr8.dtype :", newarr8.dtype,newarr8)

arr9 = np.array([1, 0, 3])
print(arr9.dtype, arr9)
newarr9 = arr9.astype(bool) # boolean a çevirim
print(newarr9.dtype, newarr9)

arr10 = np.array([[1.45,5.12,6,], [25.05,85.086,3.0897]])
newarr10 = arr10.astype(np.float64)
print(newarr10)
newarr10 = np.reshape(newarr10, (3,2))
print(newarr10)
print(np.round(newarr10,1))
print(np.round(newarr10,2))
print(np.round(newarr10,3))
print(np.round(newarr10,4))
newarr10 =np.reshape(newarr10, (6,1))
print(np.round(newarr10,1))
print(np.round(newarr10,2))
print(np.round(newarr10,3))
print(np.round(newarr10,4))

