import numpy as np

a = [3,5,2,6, "a", True, False, False]
a = np.array(a, str)
print(a.dtype, a)
# a1 = [3,5,2,1000,  True, False, False]
# a1 = np.array(a1, np.uint8)
# print(a1.dtype, a1)
a1 = [3,5,2,129,  True, False, False]
a1 = np.array(a1, np.uint8)
print(a1.dtype, a1)
