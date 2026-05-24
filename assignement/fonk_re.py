import re
xx = "güzel Ahmet 9al renkli güzel 123456 bir şalı 23hemen al1dı."

# tüm ... ifadelerinin listesi
print(re.findall("al", xx))
print(re.findall("şal", xx))

# Metinde ara
print(re.search("şal", xx))
print(re.search("al", xx))

# Metni böl
print("\"al\" ifadesine göre böl:",re.split("al", xx))
print("\"şal\" ifadesine göre böl:",re.split("şal", xx))
print("Boşluklara göre böl:",re.split(" ", xx))
print("\\l\ göre böl:",re.split("l", xx))

# Değiştir
print("Bütün boşlukları \"_\" ile değiştir:",re.sub("", "_", xx))
print("Bütün \"güzel\" ifadelerini \"iyi\" ile değiştir:",re.sub("güzel", "iyi", xx))
print(re.sub("[^0-9]", "-", xx))
print(re.sub("[0-9]", "-", xx))