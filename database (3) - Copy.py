from pprint import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Sekolah

def main():
    i = True
    while (i):
        masukan = input("Masukkan angka yang Anda Pilih : \n1. Insert\n2. Read\n3. Update\n4. Delete\n5. Sorting\n6. Exit \nPilih Masukan : ")

        if masukan == '1':
            Insert()
            print("\n")
        elif masukan == '2':
            read()
            print("\n")
        elif masukan == '3':
            update()
            print("\n")
        elif masukan == '4':
            delete()
            print("\n")
        elif masukan == '5':
            sorting()
        elif masukan == '6':
            print("Exiting the program")
            break

def Insert():

    try:
        pilihan = input("Masukkan angka yang Anda pilih : \n1. Kelas \n2. Jurusan \n3. Murid \n4. Guru \nPilih Masukan : ")

        if pilihan == '1':
            id = input("Masukkan ID : ")
            nama = input("Masukkan Kelas : ")

            db.Kelas.insert_one(
                {
                '_id' : id,
                'Kelas' : nama,
                }
            )
            print("Berhasil tersimpan")
        
        elif pilihan == '2':
            id_jurusan = input("Masukkan ID : ")
            nama_jurusan = input("Masukkan Nama Jurusan : ")
            id_kelas = input("Masukkan ID Kelas : ")

            db.Jurusan.insert_one(
                {
                '_id' : id_jurusan,
                'Nama': nama_jurusan,
                'Kelas_id' : id_kelas
                }
            )
            db.Kelas.update_one(
                {"_id" : id_kelas},
                {
                    "$push": {
                        "Jurusan":
                        {
                            '_id' : id_jurusan,
                            'Nama' : nama_jurusan
                        }
                    }
                }
            )
            print("Berhasil tersimpan")

        elif pilihan == '3':
            id = input("Masukkan ID : ")
            nama = input("Masukkan Nama siswa : ")
            NIS = input("Masukkan Nomor Induk Siswa : ")
            Asal = input("Masukkan Alamat tempat tinggal : ")
            id_kelas = input("Masukkan ID Kelas : ")

            db.Siswa.insert_one(
                {
                '_id' : id,
                'Nama' : nama,
                'NIS' : NIS,
                'Asal' : Asal,
                'Kelas_id' : id_kelas
                }
            )
            db.Kelas.update_one(
                {"_id" : id_kelas},
                {
                    "$push": {
                        "Siswa":
                        {
                            '_id' : id,
                            'Nama' : nama,
                            'NIS' : NIS,
                            'Asal' : Asal
                        }
                    }
                }
            )
            print("Berhasil tersimpan")

        elif pilihan == '4':
            id = input("Masukkan ID : ")
            nama = input("Masukkan Nama Guru : ")
            NIP = input("Masukkan Nomor Induk Pegawai : ")
            Asal = input("Masukkan Alamat tempat tinggal : ")
            id_kelas = input("Masukkan ID Kelas : ")

            db.Guru.insert_one(
                {
                '_id' : id,
                'Nama' : nama,
                'NIP' : NIP,
                'Asal' : Asal,
                'Kelas_id' : id_kelas
                }
            )
            db.Kelas.update_one(
                {"_id" : id_kelas},
                {
                    "$push" : {
                        "Wali_Kelas": 
                        {
                            '_id' : id,
                            'Nama' : nama,
                            'NIP' : NIP,
                            'Asal' : Asal
                        }
                    }
                }
            )
            print("Berhasil tersimpan")
            
    except Exception as e:
        print(e)

def read():
    masukan = input("Masukkan angka : \n1. Kelas\n2. Jurusan\n3. Siswa\n4. Guru\nPilih Masukan : ")
    
    if masukan == '1':
        id_kelas = db.Kelas.find()
        for id in id_kelas:
            pprint(id)
    elif masukan == '2':
        id_jurusan = db.Jurusan.find()
        for id in id_jurusan:
            pprint(id)
    elif masukan == '3':
        id_murid = db.Siswa.find()
        for id in id_murid:
            pprint(id)
    elif masukan == '4':
        id_guru = db.Guru.find()
        for id in id_guru:
            pprint(id) 
        
def update():
    try:
        masukan = input("Masukkan yang ingin di update\n1. Murid\n2. Guru\n3. Kelas\nPilihan : ")
        if masukan == '1':
            key = input("Masukkan ID : ")
            nama = input("Masukkan Nama murid : ")
            NIS = input("Masukkan Nomor Induk Siswa : ")
            Kelas = input("Masukkan Id Kelas : ")
            Asal = input("Masukkan Alamat tempat tinggal : ")
            id_Wali = input("Masukkan ID Wali Kelas : ")
        
            db.Murid.update_one(
                {"_id" : key},
                {
                    "$set": {
                        '_id' : key,
                        'Nama' : nama,
                        'NIS' : NIS,
                        'Kelas' : [Kelas],
                        'Asal' : Asal,
                        'Wali_kelas_id' : [id_Wali]
                        }
                    }
                )
            print("Data tersimpan")
        elif masukan == '2':
            key = input("Masukkan ID : ")
            nama = input("Masukkan Nama Guru : ")
            NIP = input("Masukkan Nomor Induk Pegawai : ")
            Asal = input("Masukkan Alamat tempat tinggal : ")
            id_kelas = input("Masukkan ID Kelas : ")

            db.Guru.update_one(
                {"_id" : key},
                {
                    "$set": {
                        '_id' : key,
                        'Nama' : nama,
                        'NIS' : NIS,
                        'Kelas' : [Kelas],
                        'Asal' : Asal,
                        'Wali_kelas_id' : [id_Wali]
                        }
                    }
                )
            print("Data tersimpan")
        elif masukan == '3':
            key = input("Masukkan ID : ")
            nama = input("Masukkan Nama Kelas : ")
            WaliKelas = input("Masukkan ID Wali Kelas : ")

            db.Kelas.update_one(
                {"_id" : key},
                {
                    "$set": {
                        '_id' : key,
                        'Nama' : nama,
                        'Wali_Kelas_id' : [WaliKelas]
                        }
                    }
                )
            print("Data tersimpan")
    except Exception as e:
        print(e)

def sorting():

    masukan = input("1. Sorting secara Ascending\n2. Sorting secara Descending\n Masukan :")
    try:
        if masukan == '1':
            sorting = db.murid.find().sort("Nama", 1)
            for s in sorting:
                print(s)
        elif masukan == '2':
            sorting = db.murid.find().sort("Nama", -1)
            for s in sorting:
                print(s)
    except Exception as e:
        print(e)

def delete():
    try:
        masukan = input("Pilih yang ingin dihapus : \n1. Murid\n2. Guru\n3. Kelas\nPilihan : ")
        if masukan == '1':
            key = input("Masukkan id Murid yang ingin dihapus : ")
            db.Murid.delete_many({"_id":key})
            print("Data telah terhapus")
        elif masukan == '2':
            key = input("Masukkan id Guru yang ingin dihapus : ")
            db.Guru.delete_many({"_id":key})
            print("Data telah terhapus")
        elif masukan == '3':
            key = input("Masukkan id Kelas yang ingin dihapus : ")
            db.Kelas.delete_many({"_id":key})
            print("Data telah terhapus")

    except Exception as e:
        print(e)
    
main()
