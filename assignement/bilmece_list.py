
#Bilmece liste ile

dogru_cevaplar=[
    "adam kelmiş",
    "adam kel",
    "çünkü kelmiş",
    "kelmiymiş?",
    "kelmiş",
    "kel",
    "kel çünkü",
    "kel mi",
    "kel mi?"
    ]
cevap_hakki=3

while cevap_hakki>0:
    cevap=input("*"*5 + "Dışarıda sağanak yağmur altında tamamen"
            +"\nkorumasız olan bir adam var fakat saçının tek bir teli dahi ıslanmadı."
            +"\n Neden? :D" + "*"*8 + "\n")
    try:
        if cevap.lower() in dogru_cevaplar:  
            print("Doğru :D")
            break

        else:
            cevap_hakki-=1
            if cevap_hakki>0:
                print("-"*30)
                print(f"Olmadı, bi daha dene...\nKalan hakkın:{cevap_hakki}")
                
            else:
                print("-"*30)
                print("Olmadı, bi dahaki sefere artık...\n Çünkü; adam kelmiş! :D")
    except ValueError:
        print("Hile yapma!")
            
        
          
    
    

      
