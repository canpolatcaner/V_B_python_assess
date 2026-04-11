def menu_yap(*secenekler):
    print(secenekler)
    en_uzun = 0
    for a in secenekler:
        if en_uzun<len(a): 
            en_uzun = len(a)
  
            
    print(f"╔{'═'*(en_uzun+3)}╗")
    print(f"║{' '*(en_uzun//2)}MENU{' '*(en_uzun//2)}║")
    print(f"╠{'═'*(en_uzun+3)}╣")
    for n,b in enumerate(secenekler,1):
        print(f"║ {n}-{b}{' '*(en_uzun-len(b))}║")
    print(f"╚{'═'*(en_uzun+3)}╝")


print(menu_yap("Oyunlar","Çizimler","Sağlık Uygulamaları","Yep yeni uzun bir menu ","Hesaplamalar", "Bu program ne kadar uzun bir menü oluşturabilir diye kendime sormadan edemiyorum "))


# 201 ╔# 205 ═# 187 ╗# 186 ║# 200 ╚# 188 ╝# 185 ╣# 204 ╠
