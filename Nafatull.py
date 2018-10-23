#Menghubungkan ke pymongo dengan mengimport MongoClient

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.tokogame

def main():
	a=1
	while(a):
		#Memilih opsi untuk melakukan CRUD
		selection = input('Pilih apa yang anda ingin lakukan: \n1.Insert \n2.Update \n3.Read \n4.Delete\n5.exit\nAnswer: ')
		print("run2")
		if selection == '1':
			insert()
			print("\n")
		elif selection =='2':
			update()
			print("\n")
		elif selection == '3':
			read()
			print("\n")
		elif selection == '4':
			delete()
			print("\n")
		elif selection == '5':
			print("Good Bye!")
			a=0

def insert():
	try:
		Game_ID= input('Masukkan ID game: ')
		namaGame= input('Masukkan Nama Game: ')
		GenreGame= input('Masukkan Genre Game: ')
		if GenreGame=='FPS':
			GenreGame={"$ref":"genre","$id":1}
		elif GenreGame=='Strategy':
			GenreGame={"$ref":"genre","$id":2}
		elif GenreGame=='RPG':
			GenreGame={"$ref":"genre","$id":3}
		elif GenreGame=='Sports':
			GenreGame={"$ref":"genre","$id":4}
		else:
			print('tidak ada dalam kategori')
		PerangkatGame= input('Masukkan Perangkat Game: ')
		if PerangkatGame=='PC':
			PerangkatGame={"$ref":"perangkat","$id":1}
		elif PerangkatGame=='PS4':
			PerangkatGame={"$ref":"perangkat","$id":2}
		elif PerangkatGame=='Xbox One':
			PerangkatGame={"$ref":"perangkat","$id":3}
		elif PerangkatGame=='Nintendo Switch':
			PerangkatGame={"$ref":"perangkat","$id":4}
		else:
			print('tidak ada dalam kategori') 

		db.Employees.insert_one(
			{
				"_id" : Game_ID,
				"nama" : namaGame,
				"genre" : GenreGame,
				"perangkat" : PerangkatGame
			}
		)
		print("berhasil menambahkan")

	except Exception as e:
		print(e)		

def read():
	try:
		empCol = db.games.find()
		print('\n All data from EmployeeData Database: \n')
		for emp in empCol:
			print(emp)
	except Exception as e:
		print ("read salah")

def delete():
	try:
		criteria = input("Enter employee id to delete :\n")
		db.Employees.delete_many({"id":criteria})
		print ("\nDelete Succesfully") 
	except Exception as e:
		raise e

def update ():
	try:
		criteria = input("\nEnter id to update :\n")
		name = input("\nEnter name to update\n")
		country = input("\nEnter country to update\n")
		age = input("\nEnter age to update\n ")

		db.Employees.update_one(
			{"id": criteria},
			{
				"$set": {
					"name":name,
					"age":age,
					"country":country
				}
			
			}
		)
		print("\nRecords updated Succesfully\n")
	except Exception as e:
		raise e


main()
