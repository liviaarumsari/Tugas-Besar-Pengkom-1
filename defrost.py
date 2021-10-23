# DEFROST

# Import Time Module
import time

# Fungsi Countdown
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Proses Selesai!')


# MEMILIH OPSI DEFROST
bahan = ["Meat", "Poultry", "Fish", "Bread", "Quick Defrost"]
menit = [10, 20, 10, 2, 5]
detik = [25, 10, 10, 30, 30]

i = False
while i == False:
    print("OPSI DEFROST: \n1. Auto Defrost \n2. Quick Defrost")
    opsi_defrost = int(input("Masukkan opsi defrost yang ingin dijalankan: "))
    if opsi_defrost == 1: # auto defrost
        print("AUTO DEFROST")
        print("PILIH JENIS BAHAN:")
        j = 1
        for element in bahan: # print jenis bahan
            print(f"{j}. {bahan[j-1]}")
            j += 1
        k = False
        # memilih jenis bahan
        while k == False:
            pilihan = int(input("Masukkan pilihan jenis bahan: "))
            if 0 < pilihan <= 4:
                l = False
                while l == False:
                    # memasukkan berat bahan
                    berat = float(input(f"Masukkan berat {bahan[pilihan-1]} dalam kilogram: "))
                    a = True
                    # kondisional waktu masing-masing bahan (otomatis)
                    if 0.1 <= berat <= 4:
                        t = (menit[pilihan-1]*60) + detik[pilihan-1]
                        level = "HIGH"
                        l = True
                    elif berat < 0.1:
                        print("Berat bahan harus lebih dari 0.1 kg!")
                    elif berat > 4:
                        print("Berat bahan harus kurang dari 4 kg.")
                k = True
            else:
                print("Masukan berupa angka 1 sampai 4!")
        i = True
    elif opsi_defrost == 2: # quick defrost
        print("QUICK DEFROST")
        pilihan = 5
        t = (menit[pilihan-1]*60) + detik[pilihan-1]
        level = "HIGH"
        i = True
    else:
        print("Masukan berupa angka 1 atau 2!")


# OUTPUT
print(f"Anda akan melakukan Defrost selama {menit[pilihan-1]} menit dan {detik[pilihan-1]} detik dengan level {level}.")
start = input("Ketik S untuk START atau Ketik B untuk BACK: ")
if start == "S":
    print("Memulai Defrost")
    countdown(int(t))