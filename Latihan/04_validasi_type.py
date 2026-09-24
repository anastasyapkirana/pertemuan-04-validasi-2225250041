# Input: jumlah soal yang dijawab benar dari 20 soal
# Aturan: validasi tipe dan rentangb, lalu menentukan ketuntasan
# Output: presentase dan keterangan tuntas

teks = input("Jumlah soal yang dijawab benar 20: ").strip()

try:
    benar = int(teks)
except ValueError:
    print("Masukan ditolak: jumlah harus berupa bilangan bulat.")
else:
    if benar < 0 or benar > 20:
        print("Masukan ditolak: jumlah harus berada pada rentang 0 hingga 20.")
    else:
        presentase = benar / 20 * 100
        print(f"Presentase: {presentase:.2f}%")

        if presentase >= 75:
            print("Tuntas")
        else:
            print("Belum tuntas")
        