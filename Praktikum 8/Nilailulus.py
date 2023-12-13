def Nilai_Lulus(nilai):
    if nilai < 60:
        return "Gagal"
    elif nilai >= 61 and nilai <= 70:
        return "Baik"
    elif nilai >= 71 and nilai <= 80:
        return "Sangat Baik"
    elif nilai >= 81 and nilai <= 100:
        return "Istimewa"
    else:
        return "Gagal"

# Contoh penggunaan fungsi
nilai_mahasiswa = 60
status = Nilai_Lulus(nilai_mahasiswa)
print(f"Nilai: {nilai_mahasiswa}, Status Kelulusan: {status}")

