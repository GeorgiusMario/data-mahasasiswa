# LATIHAN DICTIONARY PART 1
"""
menggunakan from keys
"""
import datetime
import string
import random

mahasiswa_template = {
    "Nama":"Nama",
    "Nim":"000000",
    "Sks_lulus":"0",
    "Lahir":datetime.datetime(2000,12,12)
}
data_mahasiswa = {}
while True :
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print(20*"-")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    print(mahasiswa)
    mahasiswa["Nama"]= input("Nama Mahasiswa = ")
    mahasiswa["Nim"]= int(input("Nim Mahasiswa = "))
    mahasiswa["Sks_lulus"]= int(input("Sks Mahasiswa = "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (1 - 12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1 - 31) : "))
    mahasiswa["Lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    # ''.join(string kosong ikut gabunng) random  for i in range untuk membuat random number
    # choice untuk melihat 1 putaran i string
    #''.join((random.choice(string.ascii_lowercase)for i in range(6))) 
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))#import string , # import random
    data_mahasiswa.update({KEY:mahasiswa})# agar inputan tidak saling menimpati
    print(f"{'NO':<10}{'NAMA':<25}{'NIM':<5}{'SKS':<5}{'LAHIR':<10}")
    print("-"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['Nama']
        NIM = data_mahasiswa[KEY]['Nim']
        SKS = data_mahasiswa[KEY]['Sks_lulus']
        LAHIR = data_mahasiswa[KEY]['Lahir'].strftime("%x") 
        print(f"{KEY:<10}{NAMA:<25}{NIM:<5}{SKS:<5}{LAHIR:<10}")
    print("\n")
    is_done = input("Apa Sudah Selesai (y/n) ? ")
    if is_done == "n":
        break

print("Terimakasih")
