from pathlib import Path
yol = Path("C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya")
#yol.mkdir(parents=True, exist_ok=True)
#with open(yol / "rehber.txt", "w", encoding="utf-8") as f:
#    print("dosya eklendi")

dosya = open(yol / "rehber.txt","r",encoding="utf8")
okunan = dosya.readlines()
aranan = input("Aradığın ne:")
# print(okunan)
for a in okunan:
    # print(a)
    bilgiler = a.split("#")
    # print(bilgiler)
    for b in bilgiler:
        # print(b)
        if b == aranan:
            print("Rehberde var:")
            print(bilgiler)