class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def info_mahasiswa(self):
        return f"nama : {self.nama} nim :  {self.nim} prodi : {self.prodi} alamat : {self.alamat}"

print("masukkan data mahasiswa 1")
orang1 = Mahasiswa(input("nama : "),input("nim : "),input("prodi : "),input("alamat : "))

print("masukkan data mahasiswa 2")
orang2 = Mahasiswa(input("nama : "),input("nim : "),input("prodi : "),input("alamat : "))

print("masukkan data mahasiswa 3")
orang3 = Mahasiswa(input("nama : "),input("nim : "),input("prodi : "),input("alamat : "))

print("tampilkan daftar mahasiswa")
print(orang1.info_mahasiswa())
print(orang2.info_mahasiswa())
print(orang3.info_mahasiswa())