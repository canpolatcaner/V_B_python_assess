# ör1: SERIES
# Pandas Serisi bir tablodaki sütun gibidir.
# Her türden veriyi tutan tek boyutlu bir dizidir.
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar,"\n")


# ör2: LABEL
# Verilere etiket ekleyebilirsiniz.

a = [35, 10, 33]
pdserisi1 = pd.Series(a, index = ["İzmir", "Balıkesir", "Hakkari"])
print(pdserisi1)
print("pdserisi1['İzmir'] etiketli deger:",pdserisi1['İzmir'])
print("pdserisi1['Hakkari'] etiketli deger:",pdserisi1['Hakkari']) 


# ör3: Sözlükten seri oluşturma
# keyler label a dönüşür


kalori = {"Gün-1": 420, "Gün-2": 380, "Gün-3": 390}
pdnesnesi = pd.Series(kalori)
print("\n", pdnesnesi)

