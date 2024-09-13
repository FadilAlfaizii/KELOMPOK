# nomor 1
my_dict={
    'Nama'          : 'Zailani Satria',
    'NIM'           : 123450111,
    'Hobby'         : 'Baca',
    'Umur'          : 18,
    'Asal Daerah'   : 'Kota Bandar Lampung, Lampung'
}

my_dict={
    'Nama'          : 'Zailani Satria',
    'NIM'           : 123450111,
    'Hobby'         : 'Baca',
    'Umur'          : 18,
    'Asal Daerah'   : 'Kota Bandar Lampung, Lampung'
}

my_dict={
    'Nama'          : 'Zailani Satria',
    'NIM'           : 123450111,
    'Hobby'         : 'Baca',
    'Umur'          : 18,
    'Asal Daerah'   : 'Kota Bandar Lampung, Lampung'
}

my_dict={
    'Nama'          : 'Zailani Satria',
    'NIM'           : 123450111,
    'Hobby'         : 'Baca',
    'Umur'          : 18,
    'Asal Daerah'   : 'Kota Bandar Lampung, Lampung'
}

# nomor 2
for key, value in my_dict1.items():
    print(f"{key}: {value}")
for key, value in my_dict2.items():
    print(f"{key}: {value}")
for key, value in my_dict3.items():
    print(f"{key}: {value}")

# nomor 3
class Paket:
    def __init__(self, nama, harga, jumlah, status_pengiriman, status_penerimaan, status_akhir):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        self.status_pengiriman = status_pengiriman
        self.status_pengiriman = status_penerimaan
        self.status_akhir = status_akhir
    def info(self):
        return f"{self.nama} {self.harga} {self.jumlah} {self.status_pengiriman} {self.status_penerimaan} {self.status_akhir}"
    
paket_saya = Paket(
    "Buku", 200000, 2, "Terkirim", "Belum Diterima", "Tidak Selesai"
)
print(paket_saya.info())
