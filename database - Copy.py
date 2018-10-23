import pprint
import sys
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tokogame']

gamesCol = db.games
develoverCol = db.develover
genreCol = db.genre
platformCol = db.flatform

def main():
    while True:
        masukan = input('Pilih apa yang anda ingin lakukan: \n1.Insert \n2.Update \n3.Read \n4.Delete\n5.exit\nAnswer: ')
        if masukan == '1':
            insert()
            print()
        elif masukan == '2':
            update()
            print()
        elif masukan == '3':
            find()
            print()
        elif masukan == '4':
            delete()
            print()
        elif masukan == '5':
            print("Good Bye!")
            sys.exit(1)
        else:
            print('\nmasukan salah')

def insert():
    while True:
        pilihan = input('\nPilih Collection\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
        print()
        if pilihan == '1':
            namaGame= input('Masukkan Nama Game: ')
            hargaGame = input('Masukkan Harga Game: ')
            gamesCol.insert({
                "nama" : namaGame,
                "harga" : hargaGame
                })
            print("\nBerhasil Ditambahkan!")

        elif pilihan == '2':
            namaDeveloper= input('Masukkan Nama Develover: ')
            negaraDeveloper = input ('Masukkan Negara Develover: ')
            daftarGameDeveloper= []
            for i in range(jmlRelasi):
                daftarGameDeveloper.append(input("Nama Game: "))
                develoverCol.insert({
                    "nama":namaDeveloper,
                    "negara":negaraDeveloper,
                    "daftar game":nama_game[i]
                    })
                gamesCol.update(
                    {"nama":nama_game[i]},
                    {
                        "$push":{
                        "developer":
                            {
                                "nama":namaDeveloper,
                                "negara":negaraDeveloper
                            }
                        }
                    }
                )
            print("\nBerhasil Ditambahkan!")

        elif pilihan == '3':
            namaGenre= input('Masukkan Nama Genre: ')
            deskripsiGenre = input ('Masukkan Deskripsi Genre: ')
            jmlRelasi = eval(input('Masukkan Jumlah Game: '))
            nama_game=[]
            for i in range(jmlRelasi):
                nama_game.append(input("Nama Game: "))
                genreCol.insert({
                     "nama": namaGenre,
                     "deskripsi":deskripsiGenre
                     "daftar game":nama_game[i]
                })
                gamesCol.update(
                    {"nama":nama_game[i]},
                    {
                        "$push": {
                            "genre":
                                {
                                    "nama": namaGenre,
                                    "deskripsi":deskripsiGenre
                                }
                        }
                    }
                )
            print("\nBerhasil Ditambahkan!")
        elif pilihan == '4':
            namaPlatform= input('Masukkan Nama Platform: ')
            deskripsiPlatform = input('Masukkan Deskripsi Platform')
            jmlRelasi = eval(input('Masukkan Jumlah Game: '))
            nama_game=[]
            for i in range(jmlRelasi):
                id_buku.append(input("ID Buku : "))
                platformCol.insert(
                    {"_id": id_penerbit,
                     "Buku_id": id_buku[i],
                     "Nama": nama,
                     "Alamat": alamat,
                     "No Telp": no_telp}
                )
                gamesCol.update(
                    {"_id": id_buku[i]},
                    {
                        "$push": {
                            "platform":
                                {
                                    "nama": namaPlatform,
                                    "deskripsi": deskripsiPlatform
                                }
                        }
                    }
                )
            print("\nBerhasil Ditambahkan!")
        elif pilihan == '5':
            break
            main()
        else:
            print('\nMasukan salah')
def findGame():
    showGame = gamesCol.find()
    for x in showBuku:
        pprint.pprint(x)

def findDeveloper():
    showDeveloper = develoverCol.find()
    for x in showDeveloper:
        pprint.pprint(x)

def findGenre():
    showGenre = genreCol.find()
    for x in showGenre:
        pprint.pprint(x)

def findPlatform():
    showPlatform = platformCol.find()
    for x in showPlatform:
        pprint.pprint(x)

def find():
    while True:
        pilihan = input('\nMenampilkan isi collections\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')

        if pilihan == '1':
            findGame()
        elif pilihan == '2':
            findDeveloper()
        elif pilihan == '3':
            findGenre()
        elif pilihan == '4':
            findPlatform()
        elif pilihan == '5':
            break
            main()
        else:
            print('\nMasukan salah')

def update():
    while True:
        pilihan = input('\nUpdate Collection\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
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
        masukan = input('Pilih Collection: \n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
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


main()
