#11 sinüs grafiği
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*(np.pi), 0.1) # setting the x - coordinates
y = np.sin(x) # setting the corresponding y - coordinates

plt.plot(x, y) #

plt.show()


