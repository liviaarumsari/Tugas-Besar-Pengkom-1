from Clearscreen import clearscreen
from Start import start

# FUNGSI REHEAT ====================================================================================================
def reheat():
    
    # KAMUS LOKAL
    # bool_reheat : bool
    # m_reheat, s_reheat, t : int

    # ALGORITMA
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
            start("Reheat", t, reheat)
            bool_reheat = True
        else:
            print("Masukkan waktu kurang dari 30 menit!")
