#Üçgen çevre ve alan hesaplama (Heron formülüyle)
import math
def hesapla_ucgen():
    kenarlar=[]

    print("Lütfen üçgenin kenar uzunluklarını giriniz:")

    while len(kenarlar)<3:
        try:
            sayi= float(input(f"{len(kenarlar) + 1}.kenar:"))
            if sayi<=0:
                print("Kenar uzunluğu 0'dan büyük olmalıdır!")
    
            kenarlar.append(sayi)
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    a, b, c= kenarlar

    if (a+b>c) and (a+c>b) and (b+c>a):
        cevre = a + b + c
        s = cevre / 2
        alan = math.sqrt(s * (s-a)*(s-b)*(s-c))
        print("-"*30)
        print(f"Üçgenin çevresi\t: {cevre:.2f}")
        print(f"Üçgenin alanı\t: {alan:.2f}")
    else:
        print("\nHata: Girdiğiniz kenarlar bir üçgen oluşturmuyor!")

hesapla_ucgen()





























                  
            
            
        
        
    
    
    


















      
