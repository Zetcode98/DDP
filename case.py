def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_luas_lingkaran(jari_jari):
    import math
    return math.pi * jari_jari**2

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

while True:
    print("Pilih bangun datar untuk menghitung luas:")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    match pilihan:
        case '1':
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = hitung_luas_persegi(sisi)
            print(f"Luas persegi: {luas}")
        case '2':
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = hitung_luas_lingkaran(jari_jari)
            print(f"Luas lingkaran: {luas}")
        case '3':
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = hitung_luas_segitiga(alas, tinggi)
            print(f"Luas segitiga: {luas}")
        case '4':
            print("Terima kasih!")
            break
        case _:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, atau 4.")
