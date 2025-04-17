class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.validasi_sks(sks):
            print(f"SKS untuk {nama} tidak valid! Hanya boleh 2 atau 3.")
            self.valid = False
        else:
            self.valid = True
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in (2, 3)

    def __str__(self):
        return f"{self.kode} - {self.nama} ({self.sks} SKS)"

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            print(f"NIM {nim} tidak valid! Harus dimulai dengan '23' dan total 10 digit.")
            self.valid = False
        else:
            self.valid = True
            Mahasiswa.jumlah_mahasiswa += 1
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Prodi: {self.prodi}")
        print("Mata Kuliah yang Diambil:")
        for matkul in self.matkul_diambil:
            print(f"  - {matkul}")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10

class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            print(f"Nama kampus '{nama}' tidak valid! Tidak boleh mengandung angka.")
            self.valid = False
        else:
            self.valid = True
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampilkan_info_kampus(cls, nama):
        print(f"Nama Kampus: {nama}")
        print(f"Total Mahasiswa Terdaftar: {cls.total_mahasiswa}")

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

# INPUT DATA KAMPUS
print("Masukkan Data Kampus")
nama_kampus = input("Nama Kampus: ")
alamat_kampus = input("Alamat Kampus: ")
kampus = Kampus(nama_kampus, alamat_kampus)

# INPUT MATAKULIAH
daftar_matkul = []
print("Input 8 Mata Kuliah")
for i in range(8):
    print(f"Mata Kuliah ke-{i+1}")
    kode = input("Kode: ")
    nama = input("Nama: ")
    try:
        sks = int(input("SKS (2 atau 3): "))
    except ValueError:
        print("SKS harus berupa angka!")
        continue
    matkul = MataKuliah(kode, nama, sks)
    if matkul.valid:
        daftar_matkul.append(matkul)

if len(daftar_matkul) < 4:
    print("\nMata kuliah valid kurang dari 4. Tidak cukup untuk pengisian mahasiswa.")
    exit()

# INPUT MAHASISWA
daftar_mahasiswa = []
print("Input 6 Mahasiswa")
for i in range(6):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")
    prodi = input("Prodi: ")
    mhs = Mahasiswa(nama, nim, prodi)
    if not mhs.valid:
        continue

    print("Pilih 4 mata kuliah (input indeks sesuai daftar)")
    for f, mt in enumerate(daftar_matkul):
        print(f"{f+1}. {mt}")

    matkul_dipilih = set()
    while len(matkul_dipilih) < 4:
        try:
            pilihan = int(input(f"Pilih matkul ke-{len(matkul_dipilih)+1}: "))
            if 1 <= pilihan <= len(daftar_matkul):
                if pilihan in matkul_dipilih:
                    print("Sudah dipilih sebelumnya.")
                else:
                    mhs.tambah_matkul(daftar_matkul[pilihan - 1])
                    matkul_dipilih.add(pilihan)
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Masukkan angka!")

    daftar_mahasiswa.append(mhs)
    Kampus.total_mahasiswa += 1

print("\n========== DATA KAMPUS ==========")
kampus.tampilkan_info_kampus(kampus.nama)
print("Nama kampus valid." if kampus.valid else "Nama kampus tidak valid.")

print("\n========== DATA MAHASISWA ==========")
for m in daftar_mahasiswa:
    m.tampilkan_biodata()
Mahasiswa.tampilkan_jumlah_mahasiswa()


