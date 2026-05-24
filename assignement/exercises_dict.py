tren={"fil":"elephant", "başarı":"succes"}
kelime=input("çevrilecek kelime:")

if kelime in tren:
    print(kelime,"karşılığı", tren[kelime])
else:
    print("aradığınız kelime sözlükte bulunmamaktadır.")