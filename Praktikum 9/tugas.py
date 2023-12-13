def lulus_saja(hasil_akhir):
    lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]
    return lulus

# list hasil_akhir
hasil_akhir = [
    {'nama': 'kevin', 'nilai': 70},
    {'nama': 'nadya', 'nilai': 63},
    {'nama': 'farhan', 'nilai': 80},
    {'nama': 'winda', 'nilai': 40}
]

# fungsi untuk menampilkan nama siswa yang lulus saja
hasil_lulus = lulus_saja(hasil_akhir)
print(hasil_lulus)
