from Clearscreen import clearscreen
from Start import start
from PrintArray import print_kategori

# FUNGSI QUICK ACTION ====================================================================================================
def quick_action():
       
    # KAMUS LOKAL
    # array_qa = ["Veggies", "Bread", "Meat", "Fish", "Soup", "Beverage"]
    # m_qa = [1, 0, 2, 1, 2, 1]
    # s_qa = [30, 45, 0, 30, 0, 0]
    # bool_qa : bool
    # pilihan_qa, t : int

    # ALGORITMA
    clearscreen()
    array_qa = ["Veggies", "Bread", "Meat", "Fish", "Soup", "Beverage"]
    m_qa = [1, 0, 2, 1, 2, 1]
    s_qa = [30, 45, 0, 30, 0, 0]

    print("\n======= QUICK ACTION =======")
    print("Pilih kategori quick action yang diinginkan: ")
    print_kategori(array_qa)
    
    bool_qa = False
    while (bool_qa == False):
        pilihan_qa = int(input("Masukkan pilihan kategori: "))
        if (0 < pilihan_qa <= 6):
            t = (m_qa[pilihan_qa-1] * 60) + s_qa[pilihan_qa-1]
            clearscreen()
            print(f"Anda akan melakukan QUICK ACTION selama {m_qa[pilihan_qa-1]} menit dan {s_qa[pilihan_qa-1]} detik.")
            start("Quick Action", t, quick_action)
            bool_qa = True
        else:
            print("Pilihan kategori tidak tersedia.")