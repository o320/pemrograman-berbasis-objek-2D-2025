class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")
        print("Status: Karyawan Tetap")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja per Hari: {self.jam_kerja}")
        print("Status: Karyawan Harian")


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

# Fungsi untuk input data
def input_data_karyawan(manajemen):
    jumlah = int(input("Masukkan jumlah karyawan: "))
    for i in range(jumlah):
        print(f"Data Karyawan ke-{i+1}")
        tipe = input("Tipe Karyawan (tetap/harian): ")
        nama = input("Nama: ")
        gaji = int(input("Gaji: "))
        departemen = input("Departemen: ")

        if tipe == "tetap":
            tunjangan = int(input("Tunjangan: "))
            karyawan = KaryawanTetap(nama, gaji, departemen, tunjangan)
        elif tipe == "harian":
            jam_kerja = int(input("Jam kerja per hari: "))
            karyawan = KaryawanHarian(nama, gaji, departemen, jam_kerja)
        else:
            print("Tipe karyawan tidak dikenal, dilewati.")
            continue

        manajemen.tambah_karyawan(karyawan)

# Main Program
manajemen = ManajemenKaryawan()
input_data_karyawan(manajemen)
print("\n=== Daftar Karyawan ===")
manajemen.tampilkan_semua_karyawan()
