#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function untuk menghitung FPB
def hitung_fpb(x, y):
    while(y):
        x, y = y, x % y # menggunakan algoritma Euclid untuk menghitung FPB
    return x

# Function untuk menghitung KPK
def hitung_kpk(x, y):
    kpk = (x*y) / hitung_fpb(x,y) # menghitung KPK menggunakan FPB yang telah dihitung sebelumnya
    return kpk

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print('=== PROGRAM PERHITUNGAN FPB DAN KPK ===') # menampilkan judul program
    print('[1] Hitung FPB') #opsi 1
    print('[2] Hitung KPK') #opsi 2
    print('[3] Keluar') # opsi 3
    print('=======================================') #garis pemisah
    print("\n") # sebagai enter

# Fungsi untuk memproses pilihan pengguna
def proses_pilihan(pilihan):
    if pilihan == '1': # jika pengguna memilih untuk menghitung FPB
        angka1 = int(input('Masukkan angka pertama: ')) # meminta pengguna untuk memasukkan angka pertama
        angka2 = int(input('Masukkan angka kedua: ')) # meminta pengguna untuk memasukkan angka kedua
        fpb = hitung_fpb(angka1, angka2) # memanggil fungsi hitung_fpb untuk menghitung FPB dari kedua angka
        print(f'FPB dari {angka1} dan {angka2} adalah {fpb}') # menampilkan hasil perhitungan FPB
    elif pilihan == '2': # jika pengguna memilih untuk menghitung KPK
        angka1 = int(input('Masukkan angka pertama: ')) # meminta pengguna untuk memasukkan angka pertama
        angka2 = int(input('Masukkan angka kedua: ')) # meminta pengguna untuk memasukkan angka kedua
        kpk = hitung_kpk(angka1, angka2) # memanggil fungsi hitung_kpk untuk menghitung KPK dari kedua angka
        print(f'KPK dari {angka1} dan {angka2} adalah {kpk}') # menampilkan hasil perhitungan KPK
    elif pilihan == '3': # jika pengguna memilih untuk keluar dari program
        print('Terima kasih telah menggunakan program ini!') # menampilkan pesan terima kasih
    else:  # jika pengguna memilih pilihan yang tidak valid
        print('Pilihan tidak valid') # menampilkan pesan kesalahan
    print("\n") # sebagai enter

# Main program
while True:
    tampilkan_menu() # menampilkan menu
    pilihan = input('Pilihan: ') # meminta pengguna untuk memilih opsi dari menu
    proses_pilihan(pilihan) # memproses pilihan pengguna
    if pilihan == '3': # jika pengguna memilih untuk keluar dari program
        break # keluar dari loop utama dan mengakhiri program


# In[ ]:




