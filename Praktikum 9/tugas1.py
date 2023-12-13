def balikan(daftar_buah):
    panjang = len(daftar_buah)
    buah_terbalik = []
    for i in range(panjang - 1, -1, -1):
        buah_terbalik.append(daftar_buah[i])
    return buah_terbalik

# list buah-buahan
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# fungsi untuk membuat list baru dengan urutan terbalik
buah_terbalik = balikan(buah)
print(buah_terbalik)
