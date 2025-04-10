class manusia:
    def __init__(self, nama, umur, alamat):
        self.umur = umur
        self.alamat = alamat

    def aktifitas(self, sedang):
        print(f"nama: {self.nama}, umur: {self.umur}, alamat {self.alamat}, dia sedang {sedang}")

manusia1 = manusia("jois",18,"gresik")
manusia2 = manusia("dani",19,"lamongan")
manusia3 = manusia("isol",17,"surabaya")
manusia4 = manusia("revan",18,"kediri")
manusia5 = manusia("tarigan",20,"jakarta")  

manusia1.aktifitas("berjalan")
manusia2.aktifitas("berjalan")
manusia3.aktifitas("berlari")
manusia4.aktifitas("berjalan")
manusia5.aktifitas("berlari")