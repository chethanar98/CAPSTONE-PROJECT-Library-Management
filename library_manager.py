book_library = {"To Kill A Mocking Bird":10, "The Great Gatsby":4, "The Kite Runner":2, "Eleven Minutes":1}
list_of_books = {"1" : "To Kill A Mocking Bird", "2" : "The Great Gatsby", "3" : "The Kite Runner" , "4" : "Eleven Minutes"}

class LibraryManager:

	def __init__(self,member_name,pin,member_no): 
		self.member_name=member_name
		self.pin=pin
		self.no_of_books = 1
		self.member_no = member_no
		self.member = True
		self.borrowed_books = {}
	
	
	def show_list_of_books(self):
		print("Hello, these are the books available to you today : ")
		for key,values in book_library.items():
			

			print(key)
		

	def display_count_of_books(self):
		choice=input("Enter the book name you want to know if its available or not: \n\n\
			1. To Kill a Mocking Bird\n\
			2. The Great Gatsby\n\
			3. The Kite Runner\n\
			4. Eleven Minutes \n")
		book_name=list_of_books[choice]
		print(book_name, " is available, ", book_library[book_name], "book(s) are available.")
		
	
	
	def borrow_book(self):
		choice=input("Enter the book name you want to borrow from the list given below\n\n\
			1. To Kill a Mocking Bird\n\
			2. The Great Gatsby\n\
			3. The Kite Runner\n\
			4. Eleven Minutes \n")
		book_name=list_of_books[choice]

		copies=int(input("Enter the number of copies required : "))
		if book_library[book_name]==0:
			print("Sorry, ", book_name , " is not available")
		elif book_name in book_library.keys():
			book_library[book_name]-=1
			print(book_library)
			
			if copies <= 0:
					print("No book borrowed")
			else:
				self.borrowed_books[book_name] = copies


		else:
			print("Invalid book name")

		
		
		

	def return_book(self):
		
		for key, value in self.borrowed_books.items():
			print("Your list of borrowed books is ",key, value, sep=" - ")

		book_name = input("Enter the book you want to return from the list given above: ")
		for key,value in book_library.items():
			if book_name == key:
				book_library[book_name]=book_library[book_name]+1
				# print(book_library[book_name])
				break


		
		copy_count = int(input("How many copies of this book would you like to return?\n"))


		if copy_count<=value:
			self.borrowed_books[book_name]=value+1
			if self.borrowed_books.values()==0:
				del self.borrowed_books[book_name]
			print(self.borrowed_books)
		else:
			print("Invalid book name")
		print(book_library)




# --------------------------------------------------------------------------------------

# Child Class 1:

class RegularMember(LibraryManager):
	def borrow_book(self):
		book_name=input("Enter the book name you want to borrow from the list given below\n\n\
			1. To Kill a Mocking Bird\n\
			2. The Great Gatsby\n\
			3. The Kite Runner\n\
			4. Eleven Minutes \n").title()
		copies=int(input("Enter the number of copies required : "))
		if copies <=1:
		
			if book_library[book_name]==0:
				print("Sorry, ", book_name , " is not available")
			elif book_name in book_library.keys():
				book_library[book_name]-=1
				print(book_library)
				if copies <= 0:
					print("No book borrowed")
				else:
					self.borrowed_books[book_name] = copies
					print("Your list of borrowed books is : ")
					print(self.borrowed_books)
					for key, value in self.borrowed_books.items():
						print(key, value, sep=" - ")


			else:
				print("Invalid book name")
		else:
			print("Sorry, you can borrow only one book at a time.")

		


# --------------------------------------------------------------------------------------

#  Child Class 2:

class GoldMember(LibraryManager):
	def borrow_book(self):
		book_name=input("Enter the book name you want to borrow from the list given below\n\n\
			1. To Kill a Mocking Bird\n\
			2. The Great Gatsby\n\
			3. The Kite Runner\n\
			4. Eleven Minutes \n").title()
		copies=int(input("Enter the number of copies required : "))
		if copies <= 2:
		
			if book_library[book_name]==0:
				print("Sorry, ", book_name , " is not available")
			elif book_name in book_library.keys():
				book_library[book_name]-=copies
				print(book_library)
				if copies <= 0:
					print("No book borrowed")
				else:
					self.borrowed_books[book_name] = copies
					print("Your list of borrowed books is : ")
					print(self.borrowed_books)
					for key, value in self.borrowed_books.items():
						print(key, value, sep=" - ")


			else:
				print("Invalid book name")
		else:
			print("Sorry, you can borrow atmost 2 books at a time.")

# -------------------------------------------------------------------------------------



		


if __name__ == '__main__':
	mem1 = LibraryManager('Kaustubh',1234,5678 )
	mem1.show_list_of_books()
	mem1.display_count_of_books()
	mem1.borrow_book()
	if mem1.borrowed_books == {}:
		pass
	else:
		mem1.return_book()
