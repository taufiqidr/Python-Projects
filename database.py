import pprint
import sys
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tokogame']

gamesCol = db.games
developerCol = db.developer
genreCol = db.genre
platformCol = db.platform

def main():
    while True:
        masukan = input('Pilih apa yang anda ingin lakukan: \n1.Insert \n2.Update \n3.Read \n4.Delete\n5.exit\nAnswer: ')
        if masukan == '1':
            insert()
            print()
            masukan = None
        elif masukan == '2':
            update()
            print()
            masukan = None
        elif masukan == '3':
            find()
            print()
            masukan = None
        elif masukan == '4':
            delete()
            print()
            masukan = None
        elif masukan == '5':
            print("Good Bye!")
            masukan = None
            sys.exit(1)
        else:
            print('\nmasukan salah')
            masukan = None

def insert():
    while True:
        pilihan = input('\nPilih Collection untuk Insert\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
        print()
        if pilihan == '1':
            idGame =input('Masukkan ID Game: ')
            namaGame= input('Masukkan Nama Game: ')
            hargaGame = input('Masukkan Harga Game: ')
            ada = 0
            myQuery = {"_id":idGame}
            myDoc = gamesCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                gamesCol.insert({
                    "_id": idGame,
                    "nama" : namaGame,
                    "harga" : hargaGame
                    })
                print("\nBerhasil Ditambahkan!")
            else:
                print('\nID game sudah ada, insert gagal')
            pilihan = None
            idGame = None
            namaGame = None
            hargaGame = None
            ada=None
            myQuery = None
            myDoc = None
        elif pilihan == '2':
            idDeveloper=input('masukkan ID Developer: ')
            namaDeveloper= input('Masukkan Nama developer: ')
            negaraDeveloper = input ('Masukkan Negara developer: ')
            idGame=input('Masukkan ID Game: ')
            ada = 0
            myQuery = {"_id":idDeveloper}
            myDoc = developerCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                developerCol.insert({
                    "_id":idDeveloper,
                    "nama":namaDeveloper,
                    "negara":negaraDeveloper,
                    "id game": idGame
                    })
                gamesCol.update({"_id":idGame},{
                                "$push":{
                                    "developer":{
                                        "_id":idDeveloper,
                                        "nama":namaDeveloper,
                                        "negara":negaraDeveloper
                                    }
                                }
                            })
                print("\nBerhasil Ditambahkan!")
            else:
                print('\nID developer sudah ada, insert gagal')

        elif pilihan == '3':
            idGenre=input('masukkan ID Genre: ')
            namaGenre=input('masukkan Nama Genre: ')
            deskripsiGenre=input('masukkan Deskripsi Genre: ')
            idGame=input('Masukkan ID Game: ')
            ada = 0
            myQuery = {"_id":idGenre}
            myDoc = genreCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                genreCol.insert({
                    "_id": idGenre,
                    "nama": namaGenre,
                    "deskripsi": deskripsiGenre,
                    "id game": idGame
                    })              
                gamesCol.update({"_id": idGame},{
                                "$push": {
                                    "genre":{
                                        "_id": idGenre,
                                        "nama": namaGenre,
                                        "deskripsi": deskripsiGenre,
                                    }
                                }
                            })
                print("\nBerhasil Ditambahkan!")
            else:
                print('\nID genre sudah ada, insert gagal')
                
        elif pilihan == '4':
            idPlatform=input('masukkan ID Platform: ')
            namaPlatform=input('masukkan Nama Platform: ')
            idGame=input('Masukkan ID Game: ')
            ada = 0
            myQuery = {"_id":idPlatform}
            myDoc = platformCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                platformCol.insert({
                    "_id": idPlatform,
                    "nama":namaPlatform,
                    "id game": idGame
                    })
                gamesCol.update({"_id": idGame},{
                                "$push": {
                                    "platform":{
                                        "_id": idPlatform,
                                        "nama":namaPlatform,
                                    }
                                }
                            })
                print("\nBerhasil Ditambahkan!")
            else:
                print('\nID platform sudah ada, insert gagal')

        elif pilihan == '5':
            main()
            break
        else:
            print('\nmasukan salah: ')

def update():
    while True:
        pilihan = input('\nPilih Collection untuk Update\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
        print()
        if pilihan == '1':
            print('Daftar Games: ')
            finding(gamesCol)
            idGame=input('Masukkan ID Game: ')
            ada = 0
            myQuery = {"_id":idGame}
            myDoc = gamesCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID game tidak ditemukan, update gagal')
            else:
                print('update data')
                updateNamaGame = input('Masukkan Nama Game Baru: ')
                updateHargaGame = input('Masukkan Harga Game Baru: ')
                gamesCol.update({'_id':idGame},{
                        '$set': {
                            "nama": updateNamaGame,
                            "harga": updateHargaGame
                        }
                    })
                print('\nupdate berhasil ')
                
        elif pilihan == '2':
            print('Daftar Developer')
            finding(developerCol)
            idDeveloper=input('Masukkan ID Developer: ')
            ada = 0
            myQuery = {"_id":idDeveloper}
            myDoc = developerCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID developer tidak ditemukan, update gagal')
            else:
                idGame=input('Masukkan ID Game awal: ')
                print('update data')
                updateNamaDeveloper = input('Masukkan Nama Developer Baru')
                updateNegaraDeveloper = input('Masukkan Negara Developer Baru')
                updateIdGame = input("Masukkan ID Game Baru: ")
                developerCol.update({'_id': idDeveloper},{
                        '$set': {
                            "nama": updateNamaDeveloper,
                            "negara": updateNegaraDeveloper,
                        }
                    })
                gamesCol.update({"_id": idGame},{
                        "$pull": {
                            "developer":
                                {
                                    "_id": idDeveloper
                                }
                        }
                    })
                gamesCol.update({"_id": updateIdGame},{
                        "$push": {
                            "developer":
                                {
                                    "_id": idDeveloper,
                                    "nama": updateNamaDeveloper,
                                    "negara": updateNegaraDeveloper
                                }
                        }
                    }
                )
                print('\nupdate berhasil')

        elif pilihan == '3':
            print('Daftar Genre')
            finding(genreCol)
            idGenre= input('Masukkan ID Genre: ')
            ada = 0
            myQuery = {"_id":idGenre}
            myDoc = genreCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID genre tidak ditemukan, update gagal')
            else:
                idGame=input('Masukkan ID Game awal: ')
                print('update data')
                updateNamaGenre = input('Masukkan Nama Genre Baru: ')
                updateDeskripsiGenre = input('Masukkan Deskripsi Genre Baru: ')
                updateIdGame = input("Masukkan ID Game Baru: ")

                genreCol.update({'_id': idGenre},{
                        '$set': {
                            "nama": updateNamaGenre,
                            "deskripsi": updateDeskripsiGenre,
                        }
                    })
                gamesCol.update({"_id": idGame},{
                        "$pull": {
                            "genre":
                                {
                                    "_id": idGenre
                                }
                        }
                    })
                gamesCol.update({"_id": updateIdGame},{
                        "$push": {
                            "genre":
                                {
                                    "_id": idGenre,
                                    "nama": updateNamaGenre,
                                    "deskripsi": updateDeskripsiGenre
                                }
                        }
                    })
                print('\nupdate berhasil')

        elif pilihan == '4':
            print('daftar platform')
            finding(platformCol)
            idPlatform=input('Masukkan ID Platform')
            ada = 0
            myQuery = {"_id":idPlatform}
            myDoc = platformCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID platform tidak ditemukan, update gagal')
            else:
                idGame=input('Masukkan ID Game awal: ')
                print('update data')
                updateNamaPlatform = input('Masukkan Nama Platform Baru')
                updateIdGame = input('Masukkan ID Game Baru: ')
                platformCol.update({'_id': idPlatform},{
                        '$set': {
                            "nama":updateNamaPlatform
                        }
                    })
                gamesCol.update({"_id": idGame},{
                        "$pull": {
                            "platform":
                                {
                                    "_id": idPlatform
                                }
                        }
                    })
                gamesCol.update({"_id": updateIdGame},{
                        "$push": {
                            "platform":
                                {
                                    "_id": idPlatform,
                                    "nama": updateNamaPlatform
                                }
                        }
                    })
                print('\nupdate berhasil')
        elif pilihan == '5':
            main()
            break
        else:
            print('\ninput salah')

def delete():
    while True:
        masukan = input('Pilih Collection untuk delete\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
        print()
        if masukan == '1':
            print('Daftar Games: ')
            finding(gamesCol)
            idGame=input('Masukkan ID Game: ')
            ada = 0
            myQuery = {"_id":idGame}
            myDoc = gamesCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID game tidak ditemukan, delete gagal')
            else:
                gamesCol.remove({"_id":idGame})
                print('\ndelete berhasil')
                
            print('\nID tidak ditemukan, gagal menghapus')
        elif masukan == '2':
            print('Daftar Developer')
            finding(developerCol)
            idDeveloper=input('Masukkan ID Developer: ')
            ada = 0
            myQuery = {"_id":idDeveloper}
            myDoc = developerCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID developer tidak ditemukan, delete gagal')
            else:
                idGame=input('Masukkan ID Game dari Developer ini: ')
                gamesCol.update(
                    {"_id": idGame, 'developer._id':idDeveloper},
                    {"$pull": {
                            "developer": { "_id": idDeveloper }
                        }
                    }
                )
                developerCol.remove({"_id": idDeveloper})
                print('\ndelete berhasil')

        elif masukan == '3':
            print('Daftar Genre')
            finding(genreCol)
            idGenre= input('Masukkan ID Genre: ')
            ada = 0
            myQuery = {"_id":idGenre}
            myDoc = genreCol.find(myQuery)
            for i in myDoc:
                ada = ada+1
            if (ada==0):
                print('\nID genre tidak ditemukan, delete gagal')
            else:
                idGame=input('Masukkan ID Game dari Genre ini: ')
                gamesCol.update(
                    {"_id": idGame, 'genre._id': idGenre},
                    {"$pull": {
                        "genre": {"_id": idGenre}
                    }
                    }
                )
                genreCol.remove({"_id": idGenre})
                print('\ndelete berhasil')
        elif masukan == '4':
            print('daftar platform')
            finding(platformCol)
            idPlatform=input('Masukkan ID Platform')
            idGame=input('Masukkan ID Game dari Platform ini: ')
            gamesCol.update(
                {"_id": idGame, 'platform._id': idPlatform},
                {"$pull": {
                    "platform": {"_id": idPlatform}
                }
                }
            )
            platformCol.remove({"_id": idPlatform})
            print("\nData telah terhapus!")
        elif masukan == '5':
            main()
            break
        else:
            print('\n!!!! - Masukkan dengan benar - !!!!')

pp = pprint.PrettyPrinter(indent=4)
def finding(collection):
    i = collection.find()
    for j in i:
        pp.pprint(j)

def find():
    while True:
        pilihan = input('\nMenampilkan isi collections\n1. Games \n2. Developer \n3. Genre \n4. Platform\n5. Kembali\nMasukkan Plihan : ')
        if pilihan == '1':
            finding(gamesCol)
        elif pilihan == '2':
            finding(developerCol)
        elif pilihan == '3':
            finding(genreCol)
        elif pilihan == '4':
            finding(platformCol)
        elif pilihan == '5':
            main()
            break
        else:
            print('\nMasukan salah')

main()
