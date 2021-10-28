from Time import countdown

# FUNGSI START
def start(jenis_mode, t, func):
    
    # KAMUS LOKAL
    # bool : bool
    # start : int

    # ALGORITMA
    bool = False
    while (bool == False):
        start = int(input("Ketik 1 untuk START, 2 untuk BACK, atau 3 untuk MODE: "))
        if (start == 1):
            print("Memulai " + jenis_mode)
            countdown(int(t))
            bool = True
        elif (start == 2):
            func()
            bool = True
        elif (start == 3):
            from MICROWAVE11 import mode
            mode()
            bool = True
        else:
            print("Pilihan tidak tersedia!")