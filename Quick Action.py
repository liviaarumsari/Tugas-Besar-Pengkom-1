import time

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Proses Selesai!!')

kategori = ["Veggies", "Bread", "Meat", "Fish", "Soup", "Beverage"]
waktu_menit = [1, 0, 2, 1, 2, 1]
waktu_detik = [30, 45, 0, 30, 0, 0]
n = len(kategori)

# function Quick Action
def quick_action():
    print("Pilih kategori quick action yang diinginkan:")
    for i in range (n):
        print(str(i+1) + ". " + kategori[i])

    x = int(input("Pilihan kategori: "))
    if (0 < x <= 6):
        t = (waktu_menit[x-1]*60) + waktu_detik[x-1]
        print("Anda akan melakukan pemanasan selama " + str(waktu_menit[x-1]) + " menit " + str(waktu_detik[x-1]) + " detik ")
    else:
        print("Pilihan kategori tidak tersedia")
    start_back(t)

# function start atau back
def start_back(t):
        start = input("Ketik S untuk START atau Ketik B untuk BACK: ")
        if start == "S":
            print("Memulai Quick Action")
            countdown(int(t))
        elif start == "B":
            quick_action()

quick_action()


