from Clearscreen import clearscreen
from Start import start
from PrintArray import print_kategori

# FUNGSI DEFROST ====================================================================================================
def defrost():
    
    # KAMUS LOKAL
    # bool_defrost : bool
    # array_defrost : ["Auto Defrost", "Quick Defrost"]
    # opsi_defrost : int

    # ALGORITMA
    clearscreen()
    print("\n======= DEFROST =======")
    bool_defrost = False
    while (bool_defrost == False):
        array_defrost = ["Auto Defrost", "Quick Defrost"]
        print("Opsi Defrost: ")
        print_kategori(array_defrost)
        opsi_defrost = int(input("Masukkan opsi defrost yang ingin dijalankan: "))
        if (opsi_defrost == 1):
            auto_defrost()
            bool_defrost = True
        elif (opsi_defrost == 2):
            quick_defrost()
            bool_defrost = True
        else:
            print("Input tidak valid!")


# FUNGSI AUTO DEFROST
def auto_defrost():
    
    # KAMUS LOKAL
    # array_ad = ["Meat", "Poultry", "Fish", "Bread"]
    # m_ad = [6, 5, 5, 3]
    # s_ad = [25, 15, 10, 50]
    # level_ad = ["HIGH","HIGH","HIGH","LOW"]
    # bool_bahan, bool_berat : bool
    # pilihan_ad, menit_ad, detik_ad, t : int
    # berat : float

    # ALGORITMA
    clearscreen()
    array_ad = ["Meat", "Poultry", "Fish", "Bread"]
    m_ad = [6, 5, 5, 3]
    s_ad = [25, 15, 10, 50]
    level_ad = ["HIGH","HIGH","HIGH","LOW"]

    print("\n======= AUTO DEFROST =======")
    print("Pilih jenis bahan untuk Auto Defrost:")
    print_kategori(array_ad)
    
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
        berat = float(input(f"Masukkan berat {array_ad[pilihan_ad-1]} dalam kilogram: "))
        if (0.1 <= berat <= 4):
            menit_ad = int(m_ad[pilihan_ad-1] - ((4-berat)//1))
            detik_ad = s_ad[pilihan_ad-1]
            t = (menit_ad*60) + detik_ad
            clearscreen()
            print(f"Anda akan melakukan AUTO DEFROST selama {menit_ad} menit dan {detik_ad} detik dengan level {level_ad[pilihan_ad-1]}.")
            start("Defrost", t, defrost)
            bool_berat = True
        else:
            print("Berat harus di antara 0.1 kg dan 4 kg!")
    

# FUNGSI QUICK DEFROST
def quick_defrost():
    
    # KAMUS LOKAL
    # m_qd = 5
    # s_qd = 30
    # level_qd = "HIGH"
    # t : int

    # ALGORITMA
    clearscreen()
    m_qd = 5
    s_qd = 30
    level_qd = "HIGH"

    t = (m_qd*60) + s_qd
    print("\n======= QUICK DEFROST =======")
    print(f"Anda akan melakukan QUICK DEFROST selama {m_qd} menit dan {s_qd} detik dengan level {level_qd}.")
    
    start("Defrost", t, defrost)