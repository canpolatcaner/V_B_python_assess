# 1000 noktayı örneği. Daha anlamlı bir grafik için değeri < 10 olanların grafiği.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()


