
import pandas as pd
# genellikle as pd olarak kullanılır.
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
xx = pd.DataFrame(mydataset)
print(xx)
