#Menghubungkan ke pymongo dengan mengimport MongoClient

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.GameData

def main():
	a=1
	while(a):
		#Memilih opsi untuk melakukan CRUD
		selection = input('Pilih apa yang anda ingin lakukan: \n1.Insert \n2.Update \n3.Read \n4.Delete\nAnswer: ')
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
		elif selection == 'exit':
			print("Good Bye!")
			a=0

def insert():
	try:
		gameId= input('Masukkan ID game :')
		gameName= input('Masukkan Nama game : ')
		gameGenre= input('Masukkan Genre game : ')
		gamePrice= input('Masukkan Harga game: ')

		db.Game.insert_one(
			{
				"id" : gameId,
				"name" : gameName,
				"genre" : gameGenre,
				"price" : gamePrice
			}
		)
		print("Succesfully insert")

	except Exception as e:
		print(e)		

def read():
	try:
		empCol = db.Game.find()
		print('\n All data from GameData Database: \n')
		for emp in empCol:
			print(emp)
	except Exception as e:
		print ("read salah")

def delete():
	try:
		criteria = input("Masukkan ID game yang dihapus :\n")
		db.Employees.delete_many({"id":criteria})
		print ("\nDelete Succesfully") 
	except Exception as e:
		raise e

def update ():
	try:
		criteria = input("\nEnter id to update :\n")
		name = input("\nEnter name to update\n")
		genre = input("\nEnter genre to update\n")
		price = input("\nEnter price to update\n ")

		db.Employees.update_one(
			{"id": criteria},
			{
				"$set": {
					"name":name,
					"age":genre,
					"country":price
				}
			
			}
		)
		print("\nRecords updated Succesfully\n")
	except Exception as e:
		raise e


main()
