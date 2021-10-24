# import the time module
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


# Process: conditional waktu (tentuin batas waktu trs diloop untuk minta input lain kalo input sebelumnya nggak memenuhi batas waktu, maks 30 menit)
i = False
while i == False:
    # Input: waktu yang diinginkan (input menit, input detik [dipisah])
    m = int(input("Masukkan menit: "))
    s = int(input("Masukkan detik: "))
    if m < 30:
        i = True
        t = (m * 60) + s
    else:
        print("Masukkan waktu kurang dari 30 menit")


# function call
print("Anda akan melakukan Reheat selama")
start = input("Ketik S untuk START atau Ketik B untuk BACK: ")
if start == "S":
    print("Memulai Reheat")
    countdown(int(t))


