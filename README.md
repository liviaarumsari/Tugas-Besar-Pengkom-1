# Tugas-Besar-1
Membuat program Microwave dengan 4 mode, yaitu MANUAL, DEFROST, REHEAT, dan QUICK ACTION

Anggota Kelompok:
- Marcheline Fanni Hidayat Putri (16521117)
- Angela Livia Arumsari (16521177)
- Miralistya Cahya Fatimah (16521207)

STRUKTUR FILE DAN FUNGSI

A. FILE MICROWAVE11
Program utama yang merupakan driver dari program Microwave. Melakukan import fungsi dari PrintArray, Clearscreen, ModeManual, ModeDefrost, ModeQuickAction, ModeReheat, dan ModeQuickAction. Pada file utama terdapat dua fungsi, yaitu fungsi mode untuk pemilihan mode dan fungsi kembali untuk pilihan menggunakan microwave kembali atau mematikan microwave.

B. FOLDER MODE 
1. Clearscreen  : fungsi untuk membersihkan layar
2. ModeDefrost  : berisi fungsi defrost yang memanggil fungsi lokal auto_defrost dan quick_defrost. Import fungsi clearscreen dari Clearscreen, start dari Start, dan print_kategori dari PrintArray
3. ModeManual   : berisi fungsi mode manual. Import fungsi clearscreen dari Clearscreen dan start dari Start.
4. ModeQuickAction  : berisi fungsi quick_action. Import fungsi clearscreen dari Clearscreen, start dari Start, dan print_kategori dari PrintArray
5. ModeReheat   : berisi fungsi reheat. Import fungsi clearscreen dari Clearscreen dan start dari Start.
6. PrintArray   : fungsi untuk print kategori yang ada di dalam array
7. Start        : fungsi untuk memilih memulai program, kembali ke mode, atau kembali ke pilihan mode. Import fungsi countdown dari Time dan mode dari MICROWAVE11
8. Time         : fungsi untuk melakukan countdown

