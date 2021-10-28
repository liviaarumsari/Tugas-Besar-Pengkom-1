from Time import countdown


# DEFROST
def defrost():
    bool_defrost = False
    while bool_defrost == False:
        print("OPSI DEFROST: \n1. Auto Defrost \n2. Quick Defrost")
        opsi_defrost = int(input("Masukkan opsi defrost yang ingin dijalankan: "))
        if opsi_defrost == 1:
            auto_defrost()
            bool_defrost = True
        elif opsi_defrost == 2:
            quick_defrost()
            bool_defrost = True
        else:
            print("Input tidak valid!")


# AUTO DEFROST
def auto_defrost():
    bahan = ["Meat", "Poultry", "Fish", "Bread"]
    menit = [5, 10, 5, 2]
    detik = [25, 10, 10, 30]
    level = "HIGH"
    n = 1

    print("AUTO DEFROST")
    print("Pilih jenis bahan untuk Auto Defrost:")
    for element in bahan:
        print(f"{n}. {bahan[n-1]}")
        n += 1
    
    bool_pilihan = False
    while bool_pilihan == False:
        pilihan = int(input("Masukkan pilihan jenis bahan: "))
        if 0 < pilihan <= 4:
            bool_berat = False
            while bool_berat == False:
                berat = float(input(f"Masukkan berat {bahan[pilihan-1]} dalam kilogram: "))
                if 0.1 <= berat < 4:
                    t = (menit[pilihan-1]*60) + detik[pilihan-1]
                    print(f"Anda akan melakukan Auto Defrost selama {menit[pilihan-1]} menit dan {detik[pilihan-1]} detik dengan level {level}.")
                    start_back(t)
                    bool_berat = True # keluar dari while loop
                elif berat < 0.1:
                    print("Berat harus lebih dari 0.1 kg!")
                elif berat > 4:
                    print("Berat harus kurang dari 4 kg")
            bool_pilihan = True # keluar dari while loop
        else:
            print("Input tidak valid") # tetap melakukan looping


# QUICK DEFROST
def quick_defrost():
    menit = 5
    detik = 30
    level = "HIGH"

    t = (menit*60) + detik
    print("QUICK DEFROST")
    print(f"Anda akan melakukan Defrost selama {menit} menit dan {detik} detik dengan level {level}.")
    
    start_back(t)


# START ATAU BACK
def start_back(t):
    start = input("Ketik S untuk START atau Ketik B untuk BACK: ")
    if start == "S":
        print("Memulai Defrost")
        countdown(int(t))
    elif start == "B":
        defrost()


defrost()