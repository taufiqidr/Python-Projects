import pprint
import sys
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tokobuku']

colT = db['penerbit']
colB = db['buku']
colD = db['distributor']
colP = db['pengarang']

def main():
    while True:
        masukan = input("\n1. Tampilkan Data\n2. Masukkan Data\n3. Ubah Data\n4. Hapus Data\n5. Keluar \nMasukkan Pilihan : ")
        if masukan == '1':
            find()
            print()
        elif masukan == '2':
            Insert()
            print()
        elif masukan == '3':
            update()
            print()
        elif masukan == '4':
            delete()
            print()
        elif masukan == '5':
            print('\nAnda Telah Keluar dari Database Toko Buku')
            sys.exit(1)
        else:
            print('\n!!!!! - Masukkan dengan benar - !!!!!')

def Insert():
    while True:
        pilihan = input('\n====Insert Collection====\n1. Buku \n2. Pengarang \n3. Distributor \n4. Penerbit\n5. << Kembali\nMasukkan Plihan : ')
        print()
        if pilihan == '1':
            id_buku=input("ID Buku: ")
            judulBuku=input("Judul Buku: ")
            harga=input("Harga: ")
            colB.insert(
                {"_id": id_buku,
                "Judul Buku":judulBuku,
                "Harga":harga}
                )
            print("\nBerhasil Ditambahkan!")

        elif pilihan == '2':
            id_pengarang = input("ID Pengarang : ")
            namaPengarang = input("Nama : ")
            asal = input("Asal : ")
            jmlRelasi = eval(input('Masukkan Jumlah Buku yang Terkait: '))
            id_buku=[]
            for i in range(jmlRelasi):
                id_buku.append(input("ID Buku : "))

                colP.insert(
                    {"_id":id_pengarang,
                    "Nama":namaPengarang,
                    "Asal":asal,
                    "Buku_id":id_buku[i]}
                    )
                colB.update(
                    {"_id":id_buku[i]},
                    {
                        "$push":{
                        "Pengarang":
                            {
                                "_id":id_pengarang,
                                "Nama":namaPengarang,
                                "Asal":asal
                            }
                        }
                    }
                )
            print("\nBerhasil Ditambahkan!")

        elif pilihan == '3':
            id_distributor=input("ID Distributor: ")
            namaDistributor=input("Nama Perusahaan: ")
            jumlah=input("Jumlah Barang: ")
            jmlRelasi = eval(input('Masukkan Jumlah Buku yang Terkait: '))
            id_buku = []
            for i in range(jmlRelasi):
                id_buku.append(input("ID Buku : "))
                colD.insert(
                    {"_id": id_distributor,
                     "Nama Perusahaan": namaDistributor,
                     "Jumlah Barang": jumlah,
                     "Buku_id": id_buku[i]}
                )
                colB.update(
                    {"_id": id_buku[i]},
                    {
                        "$push": {
                            "Distributor":
                                {
                                    "_id": id_distributor,
                                    "Nama Perusahaan": namaDistributor,
                                    "Jumlah Barang": jumlah
                                }
                        }
                    }
                )
            print("\nBerhasil Ditambahkan!")
        elif pilihan == '4':
            id_penerbit=input('ID Penerbit: ')
            nama=input('Nama Penerbit: ')
            alamat=input('Alamat: ')
            no_telp=input('No Telp: ')
            jmlRelasi = eval(input('Masukkan Jumlah Buku yang Terkait: '))
            id_buku = []
            for i in range(jmlRelasi):
                id_buku.append(input("ID Buku : "))
                colT.insert(
                    {"_id": id_penerbit,
                     "Buku_id": id_buku[i],
                     "Nama": nama,
                     "Alamat": alamat,
                     "No Telp": no_telp}
                )
                colB.update(
                    {"_id": id_buku[i]},
                    {
                        "$push": {
                            "Penerbit":
                                {
                                    "_id": id_penerbit,
                                    "Nama": nama,
                                    "Alamat": alamat,
                                    "No Telp": no_telp
                                }
                        }
                    }
                )
            print("\nBerhasil Ditambahkan!")
        elif pilihan == '5':
            break
            main()
        else:
            print('\n!!!!! - Masukkan dengan benar - !!!!!')
def findBuku():
    showBuku = colB.find()
    for x in showBuku:
        pprint.pprint(x)

def findPengarang():
    showPengarang = colP.find()
    for x in showPengarang:
        pprint.pprint(x)

def findDistributor():
    showDistributor = colD.find()
    for x in showDistributor:
        pprint.pprint(x)

def findPenerbit():
    showPenerbit = colT.find()
    for x in showPenerbit:
        pprint.pprint(x)

def find():
    while True:
        pilihan = input("\n=====Tampilkan Collection=====\n1. Buku\n2. Pengarang\n3. Distributor\n4. Penerbit\n5. << Kembali\nMasukkan Pilihan : ")

        if pilihan == '1':
            findBuku()
        elif pilihan == '2':
            findPengarang()
        elif pilihan == '3':
            findDistributor()
        elif pilihan == '4':
            findPenerbit()
        elif pilihan == '5':
            break
            main()
        else:
            print('\n!!!!! - Masukkan dengan benar - !!!!!')

def update():
    while True:
        pilihan = input('\n====Perbaharui Collection====\n1. Buku \n2. Pengarang \n3. Distributor \n4. Penerbit\n5. << Kembali\nMasukkan Plihan : ')
        print()
        if pilihan == '1':
            print('======== COLLECTION BUKU ========')
            findBuku()
            id_buku = input("\nMasukkan ID Buku yang Ingin Diperbaharui: ")
            print('~~~ Perubahan Data ~~~')
            UpjudulBuku = input("Perubahan Judul Buku: ")
            Upharga = input("Perubahan Harga: ")
            colB.update(
                {'_id':id_buku},
                {
                    '$set': {
                        "_id": id_buku,
                        "Judul Buku": UpjudulBuku,
                        "Harga": Upharga
                    }
                }
            )
            print("\nBerhasil Diperbaharui!")

        elif pilihan == '2':
            print('======== COLLECTION PENGARANG ========')
            findPengarang()
            id_pengarang = input("\nMasukkan ID Pengarang yang Ingin Diperbaharui: ")
            id_buku_awal = input('Masukkan ID Buku semula: ')
            print('~~~ Perubahan Data ~~~')
            UpNamaPengarang = input("Perubahan Nama: ")
            UpAsal = input("Perubahan Asal: ")
            UpId_buku = input("Perubahan ID Buku: ")

            colP.update(
                {'_id': id_pengarang},
                {
                    '$set': {
                        "_id": id_pengarang,
                        "Nama": UpNamaPengarang,
                        "Asal": UpAsal,
                        "Buku_id":UpId_buku
                    }
                }
            )
            colB.update(
                {"_id": id_buku_awal},
                {
                    "$pull": {
                        "Pengarang":
                            {
                                "_id": id_pengarang
                            }
                    }
                }
            )
            colB.update(
                {"_id": UpId_buku},
                {
                    "$push": {
                        "Pengarang":
                            {
                                "_id": id_pengarang,
                                "Nama": UpNamaPengarang,
                                "Asal": UpAsal
                            }
                    }
                }
            )
            print("\nBerhasil Diperbaharui!")

        elif pilihan == '3':
            print('======== COLLECTION DISTRIBUTOR ========')
            findDistributor()
            id_distributor = input("\nMasukkan ID Distributor yang Ingin Diperbaharui: ")
            id_buku_awal = input('Masukkan ID Buku semula: ')
            print('~~~ Perubahan Data ~~~')
            UpNamaDistributor = input("Perubahan Nama Perusahaan: ")
            UpJumlah = input("Perubahan Jumlah Barang: ")
            UpId_buku = input("Perubahan ID Buku: ")

            colD.update(
                {'_id': id_distributor},
                {
                    '$set': {
                        "_id": id_distributor,
                        "Nama": UpNamaDistributor,
                        "Jumlah": UpJumlah,
                        "Buku_id": UpId_buku
                    }
                }
            )
            colB.update(
                {"_id": id_buku_awal},
                {
                    "$pull": {
                        "Distributor":
                            {
                                "_id": id_distributor
                            }
                    }
                }
            )
            colB.update(
                {"_id": UpId_buku},
                {
                    "$push": {
                        "Distributor":
                            {
                                "_id": id_distributor,
                                "Nama": UpNamaDistributor,
                                "Jumlah": UpJumlah
                            }
                    }
                }
            )
            print("\nBerhasil Diperbaharui!")
        elif pilihan == '4':
            print('======== COLLECTION PENERBIT ========')
            findPenerbit()
            id_penerbit = input('\nMasukkan ID Penerbit yang Ingin Diperbaharui: ')
            id_buku_awal = input('Masukkan ID Buku semula: ')
            print('~~~ Perubahan Data ~~~')
            UpNama = input('Perubahan Nama Penerbit: ')
            UpAlamat = input('Perubahan Alamat: ')
            UpNo_telp = input('Perubahan No Telp: ')
            UpId_buku = input('Perubahan ID Buku: ')

            colT.update(
                {'_id': id_penerbit},
                {
                    '$set': {
                        "_id": id_penerbit,
                        "Buku_id":UpId_buku,
                        "Nama": UpNama,
                        "Alamat": UpAlamat,
                        "No Telp": UpNo_telp
                    }
                }
            )
            colB.update(
                {"_id": id_buku_awal},
                {
                    "$pull": {
                        "Penerbit":
                            {
                                "_id": id_penerbit
                            }
                    }
                }
            )
            colB.update(
                {"_id": UpId_buku},
                {
                    "$push": {
                        "Penerbit":
                            {
                                "_id": id_penerbit,
                                "Nama": UpNama,
                                "Alamat": UpAlamat,
                                "No Telp": UpNo_telp
                            }
                    }
                }
            )
            print("\nBerhasil Diperbaharui!")
        elif pilihan == '5':
            break
            main()
        else:
            print('\n!!!!! - Masukkan dengan benar - !!!!!')

def delete():
    while True:
        masukan = input("Pilih yang ingin dihapus : \n1. Buku\n2. Pengarang\n3. Distributor\n4. Penerbit\n5. << Kembali\nPilihan : ")
        print()
        if masukan == '1':
            print('======== COLLECTION BUKU ========')
            findBuku()
            id_buku = input("\nMasukkan ID Buku yang ingin dihapus : ")
            colB.remove({"_id":id_buku})
            print("\nData telah terhapus!")
        elif masukan == '2':
            print('======== COLLECTION PENGARANG ========')
            findPengarang()
            id_pengarang = input("\nMasukkan ID Pengarang yang ingin dihapus : ")
            id_buku = input('Masukkan ID Buku yang Terkait: ')
            colB.update(
                {"_id": id_buku, 'Pengarang._id':id_pengarang},
                {"$pull": {
                        "Pengarang": { "_id": id_pengarang }
                    }
                }
            )
            colP.remove({"_id": id_pengarang})
            print("\nData telah terhapus!")
        elif masukan == '3':
            print('======== COLLECTION DISTRIBUTOR ========')
            findDistributor()
            id_distributor = input("\nMasukkan ID Distributor yang ingin dihapus : ")
            id_buku = input('Masukkan ID Buku yang Terkait: ')
            colB.update(
                {"_id": id_buku, 'Distributor._id': id_distributor},
                {"$pull": {
                    "Distributor": {"_id": id_distributor}
                }
                }
            )
            colD.remove({"_id": id_distributor})
            print("\nData telah terhapus!")
        elif masukan == '4':
            print('======== COLLECTION PENERBIT ========')
            findPenerbit()
            id_penerbit = input("\nMasukkan ID Penerbit yang ingin dihapus : ")
            id_buku = input('Masukkan ID Buku yang Terkait: ')
            colB.update(
                {"_id": id_buku, 'Penerbit._id': id_penerbit},
                {"$pull": {
                    "Penerbit": {"_id": id_penerbit}
                }
                }
            )
            colT.remove({"_id": id_penerbit})
            print("\nData telah terhapus!")
        elif masukan == '5':
            break
            main()
        else:
            print('\n!!!! - Masukkan dengan benar - !!!!')

print('===== >> SELAMAT DATANG DI DATABASE TOKO BUKU << =====')
main()
