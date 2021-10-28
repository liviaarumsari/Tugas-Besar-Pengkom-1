from Clearscreen import clearscreen
from Start import start

# FUNGSI MANUAL ====================================================================================================
def manual():
    
    # KAMUS LOKAL
    # bool_suhu, bool_waktu : bool
    # suhu : float
    # t, m_manual, s_manual : int

    # ALGORITMA
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
            start("Manual", t, manual)
            bool_waktu = True
        else:
            print("Masukkan waktu kurang dari 30 menit!")