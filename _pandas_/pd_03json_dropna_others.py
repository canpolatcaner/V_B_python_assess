import pandas as pd
df = pd.read_json("malzeme/jsondosyasi2.json")


print(df)
print("Max:",df["Duration"].max())
print("Max ind:",df["Duration"].argmax())
maxindex = df["Duration"].argmax()
print("Max ind:",df.iloc[maxindex])
# print("Max:",df)




# Boş olanları sütun ortalaması ile değiştirme
import pandas as pd
df = pd.read_csv('malzeme/data.csv')
print(pd.__version__)
print(df.to_string())


print("Boş hücreleri mevcutların ortalaması ile değiştir:")
ort = df["Calories"].mean()
print("Calories ortalaması:",ort)
# df["Calories"].fillna(ort, inplace = True)
df["Calories"].method(ort, inplace=True) # yeni kullanım
print(df.to_string())
"""
print("Boş hücreleri mevcutların medyanı ile değiştir:")
# Medyan = tüm değerleri artan şekilde sıraladıktan sonra ortadaki değer.
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())


print("Boş hücreleri mevcutların modu ile değiştir:")
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())


"""



# Boş veri olan satırların kaldırılması
import pandas as pd
df = pd.read_csv('malzeme/data.csv')
bos_satirlar = df[df.isnull().any(axis=1)]
print(bos_satirlar)


print("Boş veri olan satırları silme:")


df1 = df.dropna()


# df["Calories"].method(ort, inplace=True) # yeni kullanım
print(df1.to_string())
