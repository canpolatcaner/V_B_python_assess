import pandas as pd

# personel_list = {
#     'ad': ['burak', 'ege', 'asli', 'önder', 'ali','cem',"can","efe"],
#     'yas': [29, 20, 27, 25, 20, 24, 22, 30],
#     'maas': [5000, 4000, 3000, 4000, 9000, 6000, 3500, 5000]
# }
# print(type(personel_list))
# df = pd.DataFrame(personel_list)

df = pd.read_csv("personel_listesi.csv", sep=",")

print(type(df))
print("\n\nDataframe tamamı:\n", df)

print("\n\nDataframe head:\n", df.head()) # ilk 5 kayıt
print("\n\nDataframe head(3):\n", df.head(3)) # ilk 5 kayıt
print("\n\nDataframe head(7):\n", df.head(7)) # ilk 7 kayıt
print("\n\ndf.columns:\n", df.columns) # sütunlar
print("\n\ndf.describe():\n", df.describe())

print("\n\ndf.dtypes:\n", df.dtypes)
print("\n\ndf.tail():\n", df.tail()) # son 5 kayıt
print("\n\ndf.tail(2):\n", df.tail(2)) # son 3 kayıt

print("\n\ndf.shape:\n", df.shape)

print("\n\ndf[df['maas'] > 4000]:\n", df[df['maas'] > 4000])
print("\n\ndf['maas'].sum():\n", df['maas'].sum())
