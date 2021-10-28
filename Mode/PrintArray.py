# FUNGSI PRINT ARRAY
def print_kategori(array):
    
    # KAMUS LOKAL
    # array : array [0..n-1] of str

    # ALGORITMA
            n = len(array)
            for i in range (n):
                print(str(i+1) + ". " + array[i])