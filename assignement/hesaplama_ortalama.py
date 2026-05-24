#Ortalama hesaplama
print("*"*3+"Ortalama Hesaplama Programı", end="*"*3)
yazili_notu1=int(input("\nLütfen birinci yazılı sınav notunuzu giriniz\t:"))
yazili_notu2=int(input("\nLütfen ikinci yazılı sınav notunuzu giriniz\t:"))
performans_notu=int(input("\nLütfen performans notunuzu giriniz\t\t:"))
ortalama=(yazili_notu1+yazili_notu2+performans_notu)/3
print("\n\nOrtalamanız\t: {} puandır.". format(round(ortalama,2)))
print("\n\nOrtalamanız\t: %d puandır." %(ortalama))