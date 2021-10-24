import time

def countdown(t) :
    while t:
        menit, detik = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(menit,detik)
        print(timer, end="\r")
        time.sleep(1)
        t-= 1

# conditional suhu
j = False
while (j == False):
    suhu = float(input("Masukkan suhu (celcius): "))
    if (suhu<300):
        j = True
    else:
        print("Masukkan suhu dibawah 300 derajat celcius")

# conditional waktu
i = False
while (i == False):
    m = int(input("Masukkan menit: "))
    s = int(input("Masukkan detik: "))
    if (m<30):
        i = True
        t = (m*60) + s
    else:
        print("Masukkan waktu kurang dari 30 menit")

# Manual
print("Anda akan melakukan mode manual")
start = input("Ketik S untuk Start atau Ketik B untuk Back: ")
if start == "S" :
    print("Memulai mode manual")
    print(f"Suhu: {suhu} derajat celcius")
    countdown(int(t))
    print("Proses sudah selesai")