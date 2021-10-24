# IMPORT OS ====================================================================================================
import os
def clearscreen():
    os.system("clear")


# TIME MODULE ====================================================================================================
import time

# COUNTDOWN
def countdown(t):
	while t:
		menit, detik = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(menit, detik)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	print("PROSES SELESAI!\n")


# PILIHAN MODE ====================================================================================================
def mode():
    clearscreen()
    bool_mode = False
    while (bool_mode == False):
        print("\n======= PROGRAM MICROWAVE =======")
        print("Pilihan Mode Microwave: \n1. Manual \n2. Defrost \n3. Reheat \n4. Quick Action")
        mode = int(input("Masukkan mode yang dipilih: "))
        if (mode == 1):
            manual()
            bool_mode = True
        elif (mode == 2):
            defrost()
            bool_mode = True
        elif (mode == 3):
            reheat()
            bool_mode = True
        elif (mode == 4):
            quick_action()
            bool_mode = True
        else:
            print("Input tidak valid!")
    kembali()


# KEMBALI KE MODE
def kembali():
    bool_kembali = False
    while (bool_kembali == False):
        print("Apakah masih ingin menggunakan microwave?")
        kembali = int(input("Ketik 1 untuk YA atau ketik 2 untuk TIDAK: "))
        if (kembali == 1):
            mode()
            bool_kembali = True
        elif (kembali == 2):
            clearscreen()
            print("MEMATIKAN MICROWAVE\n")
            bool_kembali = True
        else:
            print("Opsi berupa angka 1 atau 2!")


# MANUAL ====================================================================================================
def manual():
    clearscreen()
    print("\n======= MANUAL =======")
    
    # conditional suhu
    bool_suhu = False
    while (bool_suhu == False):
        suhu = float(input("Masukkan suhu (celcius): "))
        if (30 < suhu < 300):
            bool_suhu = True
        else:
            print("Masukkan suhu di antara 30°C dan 300°C")

    # conditional waktu
    bool_waktu = False
    while (bool_waktu == False):
        m_manual = int(input("Masukkan menit: "))
        s_manual = int(input("Masukkan detik: "))
        if (0 <= m_manual < 30) and (s_manual >= 0):
            t = (m_manual * 60) + s_manual
            clearscreen()
            print(f"Anda akan melakukan MODE MANUAL selama {m_manual} menit dan {s_manual} detik dengan suhu {suhu}°C")
            start_manual(t)
            bool_waktu = True
        else:
            print("Masukkan waktu kurang dari 30 menit!")


# START MANUAL
def start_manual(t):
    start = int(input("Ketik 1 untuk START atau Ketik 2 untuk BACK: "))
    if (start == 1):
        print("Memulai Manual")
        countdown(int(t))
    elif (start == 2):
        manual()


# DEFROST ====================================================================================================
def defrost():
    clearscreen()
    print("\n======= DEFROST =======")
    bool_defrost = False
    while (bool_defrost == False):
        print("Opsi Defrost: \n1. Auto Defrost \n2. Quick Defrost")
        opsi_defrost = int(input("Masukkan opsi defrost yang ingin dijalankan: "))
        if (opsi_defrost == 1):
            auto_defrost()
            bool_defrost = True
        elif (opsi_defrost == 2):
            quick_defrost()
            bool_defrost = True
        else:
            print("Input tidak valid!")


# AUTO DEFROST
def auto_defrost():
    clearscreen()
    bahan = ["Meat", "Poultry", "Fish", "Bread"]
    m_ad = [6, 5, 5, 3]
    s_ad = [25, 15, 10, 50]
    level_ad = ["HIGH","HIGH","HIGH","LOW"]
    n = 1

    print("\n======= AUTO DEFROST =======")
    print("Pilih jenis bahan untuk Auto Defrost:")
    for element in bahan:
        print(f"{n}. {bahan[n-1]}")
        n += 1
    
    # conditional bahan
    bool_bahan = False
    while (bool_bahan == False):
        pilihan_ad = int(input("Masukkan pilihan jenis bahan: "))
        if (0 < pilihan_ad <= 4):
            bool_bahan = True
        else:
            print("Pilihan jenis bahan tidak tersedia!")

    # conditional berat
    bool_berat = False
    while bool_berat == False:
        berat = float(input(f"Masukkan berat {bahan[pilihan_ad-1]} dalam kilogram: "))
        if (0.1 <= berat <= 4):
            menit_ad = int(m_ad[pilihan_ad-1] - ((4-berat)//1))
            detik_ad = s_ad[pilihan_ad-1]
            t = (menit_ad*60) + detik_ad
            clearscreen()
            print(f"Anda akan melakukan AUTO DEFROST selama {menit_ad} menit dan {detik_ad} detik dengan level {level_ad[pilihan_ad-1]}.")
            start_defrost(t)
            bool_berat = True
        else:
            print("Berat harus di antara 0.1 kg dan 4 kg!")
    

# QUICK DEFROST
def quick_defrost():
    clearscreen()
    m_qd = 5
    s_qd = 30
    level_qd = "HIGH"

    t = (m_qd*60) + s_qd
    print("\n======= QUICK DEFROST =======")
    print(f"Anda akan melakukan QUICK DEFROST selama {m_qd} menit dan {s_qd} detik dengan level {level_qd}.")
    
    start_defrost(t)


# START DEFROST
def start_defrost(t):
    start = int(input("Ketik 1 untuk START atau Ketik 2 untuk BACK: "))
    if (start == 1):
        print("Memulai Defrost")
        countdown(int(t))
    elif (start == 2):
        defrost()


# REHEAT ====================================================================================================
def reheat():
    clearscreen()
    print("\n======= REHEAT =======")
    bool_reheat = False
    while (bool_reheat == False):
        m_reheat = int(input("Masukkan menit: "))
        s_reheat = int(input("Masukkan detik: "))
        if (0 <= m_reheat < 30) and (s_reheat >= 0):
            t = (m_reheat * 60) + s_reheat
            clearscreen()
            print(f"Anda akan melakukan REHEAT selama {m_reheat} menit dan {s_reheat} detik.")
            start_reheat(t)
            bool_reheat = True
        else:
            print("Masukkan waktu kurang dari 30 menit!")


# START REHEAT
def start_reheat(t):
    start = int(input("Ketik 1 untuk START atau Ketik 2 untuk BACK: "))
    if (start == 1):
        print("Memulai Reheat")
        countdown(int(t))
    elif (start == 2):
        reheat()


# QUICK ACTION ====================================================================================================
def quick_action():
    clearscreen()
    kategori = ["Veggies", "Bread", "Meat", "Fish", "Soup", "Beverage"]
    m_qa = [1, 0, 2, 1, 2, 1]
    s_qa = [30, 45, 0, 30, 0, 0]
    n = 1

    print("\n======= QUICK ACTION =======")
    print("Pilih kategori quick action yang diinginkan: ")
    for element in kategori:
        print(f"{n}. {kategori[n-1]}")
        n += 1
    
    bool_qa = False
    while (bool_qa == False):
        pilihan_qa = int(input("Masukkan pilihan kategori: "))
        if (0 < pilihan_qa <= 6):
            t = (m_qa[pilihan_qa-1] * 60) + s_qa[pilihan_qa-1]
            clearscreen()
            print(f"Anda akan melakukan QUICK ACTION selama {m_qa[pilihan_qa-1]} menit dan {s_qa[pilihan_qa-1]} detik.")
            start_quick_action(t)
            bool_qa = True
        else:
            print("Pilihan kategori tidak tersedia.")


# START QUICK ACTION
def start_quick_action(t):
    start = int(input("Ketik 1 untuk START atau Ketik 2 untuk BACK: "))
    if (start == 1):
        print("Memulai Quick Action")
        countdown(int(t))
    elif (start == 2):
        quick_action()


# MEMULAI PROGRAM MICROWAVE ====================================================================================================
mode()