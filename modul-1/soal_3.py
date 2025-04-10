class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    def bersuara(self):
        print(f"{self.nama} bersuara: Meong-meong")

    def info(self):
        print(f"Kucing = Nama: {self.nama}, Warna: {self.warna}, Umur: {self.umur} tahun")

class Anjing:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def bersuara(self):
        print(f"{self.nama} bersuara: Guk-Guk")

    def info(self):
        print(f"Anjing = Nama: {self.nama}, jenis {self.jenis}, Umur: {self.umur} tahun")

class Burung:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def bersuara(self):
        print(f"{self.nama} bersuara: Cuit-Cuit")

    def info(self):
        print(f"Burung = Nama: {self.nama}, Jenis: {self.jenis}, Warna Bulu: {self.warna}")

kucing_list = [
    Kucing(input("nama kucing: "),input("warna: "),input("umur: ")),
    Kucing(input("nama kucing: "),input("warna: "),input("umur: ")),
    Kucing(input("nama kucing: "),input("warna: "),input("umur: "))
]

anjing_list = [
    Anjing(input("nama anjing: "),input("jenis: "),input("umur: ")),
    Anjing(input("nama anjing: "),input("jenis: "),input("umur: ")),
    Anjing(input("nama anjing: "),input("jenis: "),input("umur: "))
]

Burung_list = [
    Burung(input("nama burung: "),input("jenis: "),input("umur: ")),
    Burung(input("nama burung: "),input("jenis: "),input("umur: ")),
    Burung(input("nama burung: "),input("jenis: "),input("umur: "))
]
for kucing in kucing_list:
    kucing.info()
    kucing.bersuara()

for anjing in anjing_list:
    anjing.info()
    anjing.bersuara()

for burung in Burung_list:
    burung.info()
    burung.bersuara


