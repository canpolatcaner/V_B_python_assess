import numpy as np

resim = [3,5,2,6]
print(resim)
# print(*resim)
resimnp = np.array(resim)
# print(resimnp)
# print(*resimnp)
print(resimnp.argmax())
print(resimnp.max())
