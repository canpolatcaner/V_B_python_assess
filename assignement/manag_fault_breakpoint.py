# breakpoint - Debug'la (F5) kullanımı - fault management olarak da kullanılabilir. 

# for a in range(10):
#     if a %2 == 0:
#         print(a) 

# Run and Bug editöründe Watch kısmına ekleme yaparak da izlenebilir/kontrol sağlanabilir.

gun = "Cumartesi"
for a in range(10):
    if a % 2 == 0:
        gun = "pazar"
        print(a)
    else: 
        gun = "salı"