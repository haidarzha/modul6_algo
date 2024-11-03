def hitung_rata_rata_nilai():
    total_nilai = 0
    jumlah = 0

    while True:
        data = input("Masukkan nilai: ")
        
        if data == '':
            break
            
        # menentukan nilai berdasar input user
        if data == 'A':
            nilai = 4
        elif data == 'A-':
            nilai = 3.75
        elif data == 'B+':
            nilai = 3.50
        elif data == 'B':
            nilai = 3
        elif data == 'B-':
            nilai = 2.75
        elif data == 'C+':
            nilai = 2.50
        elif data == 'C':
            nilai = 2
        elif data == 'C-':
            nilai = 1.75
        elif data == 'D':
            nilai = 1.5
        elif data == 'E':
            nilai = 1.25
        else:
            print("Input tidak valid. Silakan masukkan nilai yang valid")
            continue
        
        # kalkulasi nilai ke total dan meningkatkan jumlah
        total_nilai += nilai
        jumlah += 1
        print(f"Nilai = {int(nilai)}")

    # menghitung average terhadap input yang valid
    if jumlah > 0:
        rata_rata_nilai = float(total_nilai / jumlah)
        print(f"Rata-rata nilai adalah = {rata_rata_nilai}")
    else:
        print("Tidak ada nilai yang valid dimasukkan.")

# Memanggil fungsi
hitung_rata_rata_nilai()