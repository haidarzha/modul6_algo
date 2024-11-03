def tahun_kabisat(tahun):
    # Menentukan apakah tahun merupakan tahun kabisat
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def jumlah_hari_dalam_bulan(bulan, tahun):
    # Daftar jumlah hari dalam setiap bulan
    hari_per_bulan = {
        1: 31,  # Januari
        2: 29 if tahun_kabisat(tahun) else 28,  # Februari, mempertimbangkan tahun kabisat
        3: 31,  # Maret
        4: 30,  # April
        5: 31,  # Mei
        6: 30,  # Juni
        7: 31,  # Juli
        8: 31,  # Agustus
        9: 30,  # September
        10: 31,  # Oktober
        11: 30,  # November
        12: 31   # Desember
    }

    # Mengembalikan jumlah hari dalam bulan yang diinput
    return hari_per_bulan.get(bulan, "Bulan tidak valid")

# Loop utama program
while True:
    try:
        # Input dari pengguna
        bulan = input("Masukkan bulan (1-12) atau tekan Enter untuk keluar: ")
        if bulan == "":
            print("Program selesai.")
            break
        bulan = int(bulan)
        
        tahun = input("Masukkan tahun: ")
        if tahun == "":
            print("Program selesai.")
            break
        tahun = int(tahun)
        
        # Menampilkan hasil jumlah hari dalam bulan yang diinput
        hari = jumlah_hari_dalam_bulan(bulan, tahun)
        if hari == "Bulan tidak valid":
            print(hari)
        else:
            print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {hari} hari.")
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk bulan dan tahun.")