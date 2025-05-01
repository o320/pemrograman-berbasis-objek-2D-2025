class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 0

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, kendaraan):
        super().__init__(asal, tujuan)
        self.kendaraan = kendaraan

    def estimasi_waktu(self):
        if self.kendaraan.lower() == "truk":
            return 5
        elif self.kendaraan.lower() == "motor":
            return 3
        elif self.kendaraan.lower() == "mobil":
            return 4
        else:
            print("Jenis kendaraan tidak dikenal, gunakan truk/motor/mobil.")
            return 0


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            return 2
        elif self.maskapai.lower() == "lion air":
            return 3
        else:
            return 4


class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, kendaraan, maskapai):
        super().__init__(asal, tujuan)
        self.kendaraan = kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        # Estimasi waktu darat
        if self.kendaraan.lower() == "truk":
            waktu_darat = 5
        elif self.kendaraan.lower() == "motor":
            waktu_darat = 3
        elif self.kendaraan.lower() == "mobil":
            waktu_darat = 4
        else:
            waktu_darat = 999  # nilai besar jika tidak dikenali

        # Estimasi waktu udara
        if self.maskapai.lower() == "garuda":
            waktu_udara = 2
        elif self.maskapai.lower() == "lion air":
            waktu_udara = 3
        else:
            waktu_udara = 4

        estimasi_awal = min(waktu_darat, waktu_udara)

        # Tambah 3 hari jika bukan tujuan domestik
        tujuan_domestik = ["jakarta", "bandung", "surabaya", "gresik"]
        if self.tujuan.lower() not in tujuan_domestik:
            estimasi_awal += 3

        return estimasi_awal


# === Input Data Pengiriman ===
jumlah = int(input("Masukkan jumlah pengiriman: "))
for i in range(jumlah):
    print(f"\n--- Data Pengiriman ke-{i+1} ---")
    asal = input("Asal pengiriman: ")
    tujuan = input("Tujuan pengiriman: ")
    jalur = input("Jalur pengiriman (darat/udara): ").lower()

    kendaraan = None
    maskapai = None

    if jalur == "darat":
        kendaraan = input("Jenis kendaraan (truk/motor/mobil): ")
    elif jalur == "udara":
        maskapai = input("Maskapai (garuda/lion air/lainnya): ")
    else:
        print("Jalur tidak valid. Gunakan darat atau udara.")
        continue

    internasional = input("Apakah ini pengiriman internasional? (y/n): ").lower()

    if internasional == "y":
        # Jika jalur darat, dan maskapai tidak diisi, pakai default
        if not maskapai:
            maskapai = "lainnya"
        if not kendaraan:
            kendaraan = "mobil"
        pengiriman = PengirimanInternasional(asal, tujuan, kendaraan, maskapai)
    else:
        if jalur == "darat":
            pengiriman = PengirimanDarat(asal, tujuan, kendaraan)
        else:
            pengiriman = PengirimanUdara(asal, tujuan, maskapai)

    print(f"Estimasi waktu pengiriman ke-{i+1}: {pengiriman.estimasi_waktu()} hari")
