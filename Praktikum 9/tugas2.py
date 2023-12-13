def duplikasi(daftar_buah):
    buah_terduplikasi = []
    for buah in daftar_buah:
        buah_terduplikasi.append(buah)
        buah_terduplikasi.append(buah)
    return buah_terduplikasi

# Contoh list buah-buahan
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

# fungsi untuk membuat list baru dengan isi buah-buahan yang terduplikasi
buah_terduplikasi = duplikasi(buah)
print(buah_terduplikasi)
