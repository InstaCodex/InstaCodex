from faker import Faker
import random
import os

class RandomNameGenerator:
    def __init__(self):
        # Menginisialisasi locale untuk nama Indonesia
        self.faker_indonesia = Faker('id_ID')

    def Names(self):
        # Menghasilkan nama pria Indonesia
        name = self.faker_indonesia.first_name_male()  # Nama depan pria
        last_name = self.faker_indonesia.last_name()   # Nama belakang
        formatted_name = f"{name}_{last_name}"
        return formatted_name

    def generate_and_save_names(self, count=1000):
        # Tentukan path file di Termux
        file_path = '/storage/emulated/0/Download/generic.txt'  # Ganti path sesuai kebutuhan
        # Membuka file generic.txt untuk ditulis
        with open(file_path, 'w') as file:
            for _ in range(count):
                # Menghasilkan nama dan menulisnya ke file
                name = self.Names()
                file.write(name + '\n')
        print(f"{count} nama telah dibuat dan disimpan ke dalam {file_path}.")

    def check_names(self):
        # Tentukan path file di Termux
        file_path = '/storage/emulated/0/Download/generic.txt'  # Ganti path sesuai kebutuhan
        try:
            # Membaca dan menampilkan isi file generic.txt
            with open(file_path, 'r') as file:
                names = file.readlines()
                if names:
                    print("Daftar nama yang disimpan:")
                    for name in names:
                        print(name.strip())
                else:
                    print("Tidak ada nama yang ditemukan dalam file generic.txt.")
        except FileNotFoundError:
            print("File generic.txt tidak ditemukan. Silakan buat nama terlebih dahulu.")

def main_menu():
    name_generator = RandomNameGenerator()
    
    while True:
        print("\nMenu:")
        print("1. Buat Nama (1000 nama)")
        print("2. Cek Hasil Nama")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3): ")
        
        if pilihan == '1':
            name_generator.generate_and_save_names(1000)
        elif pilihan == '2':
            name_generator.check_names()
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Jalankan menu
if __name__ == "__main__":
    main_menu()
