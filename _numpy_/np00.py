a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# NumPy olmadan dizi elemanlarını çarpma
ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

print("\n\nNumpy olmadan:\n",ab)



# Numpy ile çarpma işlemi
import numpy as np

a_np = np.array([1, 2, 3, 4])
b_np = np.array([2, 3, 4, 5])

print("\n\nNumpy ile:\n",a_np*b_np)

# a = a_np.reshape(2,2)
# print(a)
 
# print(np.__version__)
# print(dir(np))