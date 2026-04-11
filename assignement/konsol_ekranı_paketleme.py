def paketlemeci(paketlenecek):
    paketlenmis = f"╔{'═'*len(paketlenecek)}╗\n║{paketlenecek}║\n╚{'═'*len(paketlenecek)}╝"
    return paketlenmis


print(paketlemeci("Ankara"))
print(paketlemeci("Bu gün hava çok güzel"))