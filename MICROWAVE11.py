# IMPORT MODE MODULE ===========================================================================================
import sys
sys.path.append('./Mode')

from PrintArray import print_kategori
from Clearscreen import clearscreen
from ModeManual import manual
from ModeDefrost import defrost
from ModeReheat import reheat
from ModeQuickAction import quick_action

# FUNGSI PILIHAN MODE ====================================================================================================
def mode():
    
    # KAMUS LOKAL
    # bool_mode : bool
    # array_mode : ["Manual", "Defrost", "Reheat", "Quick Action"]
    # mode : int

    # ALGORITMA
    clearscreen()
    bool_mode = False
    while (bool_mode == False):
        print("\n======= PROGRAM MICROWAVE =======")
        array_mode = ["Manual", "Defrost", "Reheat", "Quick Action"]
        print_kategori(array_mode)
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
            print("Mode tidak tersedia!")
    kembali()


# FUNGSI KEMBALI KE MODE
def kembali():
    
    # KAMUS LOKAL
    # bool_kembali : bool
    # kembali : int

    # ALGORITMA
    bool_kembali = False
    while (bool_kembali == False):
        print("Apakah masih ingin menggunakan microwave?")
        kembali = int(input("Ketik 1 untuk YA atau Ketik 2 untuk TIDAK: "))
        if (kembali == 1):
            mode()
            bool_kembali = True
        elif (kembali == 2):
            clearscreen()
            print("MEMATIKAN MICROWAVE\n")
            bool_kembali = True
        else:
            print("Opsi berupa angka 1 atau 2!")


# MEMULAI PROGRAM MICROWAVE ====================================================================================================
mode()