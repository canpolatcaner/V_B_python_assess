import datetime
def selamla(a):
    saat = datetime.datetime.now().strftime("%H")
   
    def sabah():
        return f"Günaydın {a}"
   
    def ogledenSonra():
        return f"İyi günler {a}"


    mesaj=sabah() if int(saat) <= 13 else ogledenSonra()
   
    return mesaj


# print(selamla("Burak"))
print(selamla("Erdinç"))
