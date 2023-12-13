def hanya_konsonan(kalimat):
    konsonan = ""
    for huruf in kalimat:
        if huruf.isalpha() and huruf.lower() not in 'aeiou':
            konsonan += huruf
    return konsonan

# string
teks = "Nurul Fikri"

# fungsi membuat string baru hanya dengan konsonan
hasil_konsonan = hanya_konsonan(teks)
print(hasil_konsonan)
