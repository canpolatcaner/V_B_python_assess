# ör2:klasör konumunu değiştirme
import os
yer = os.getcwd()
yer += "C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya"
os.chdir(yer)
print("Klasör:",os.getcwd())
d = open("tamir_listesi.py","a")
d.write("print('Merhaba')")

# ör2:klasör konumunu değiştirme
import os
yer = os.getcwd()
# yer += "C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya"
# os.chdir(yer)
print("Klasör:",os.getcwd())
# print(os.listdir())
print(*os.listdir(),sep="\n")

# ör2:klasör konumunu değiştirme
import os
yer = os.getcwd()
# yer += ""C:/Users/user/Desktop/Python_Projects/vektorel/Exercises_Dosya""
# os.chdir(yer)
print("Klasör:",os.getcwd())
# print(os.listdir())
# print(*os.listdir(),sep="\n")


liste = os.listdir()
for a in liste:
    print(a, end="")
    print(" "*(30-len(a)), end="")
    print("Dosya " if os.path.isfile(a) else "Klasör",end="")
    print("\t",os.stat(a).st_size)