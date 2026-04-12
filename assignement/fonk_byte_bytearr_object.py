# bytes nesnesi oluşturma
b = bytes([65, 66, 67, 68])  # A, B, C, D ASCII karşılıkları
print(b)  # Çıktı: b'ABCD'

# Elemanlara erişim
print(b[0])  # Çıktı: 65  (ASCII 'A')

# b[0] = 90  # Hata! Immutable olduğu için değiştirilemez

####################################################################

# bytearray nesnesi oluşturma
ba = bytearray([65, 66, 67, 68])
print(ba)  # Çıktı: bytearray(b'ABCD')

# Değer değiştirme
ba[0] = 90  # 'A' yerine 'Z' (ASCII 90)
print(ba)  # Çıktı: bytearray(b'ZBCD')