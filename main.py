"""
Library Management Applocation Script

"""

from library_manager import LibraryManager, RegularMember, GoldMember
from tabulate import tabulate

"""
**Variables**
	
	accounts_regular: (dict) {member_id_regular: Library Manager Object} 
			  holds all the regular memberships created during the session.
	accounts_gold: (dict) {member_id_gold: Library Manager Object} 
			  holds all the gold memberships created during the session.
	member_id_regular: (int) - Set to 1000 by default, member_id_regular. allocation starts here. 
				Incremented after every new membership creation
	member_id_gold: (int) - Set to 2000 by default, member_id_gold. allocation starts here. 
				Incremented after every new membership creation
"""

accounts_regular = {}
accounts_gold = {}
member_id_regular = 1000
member_id_gold = 2000
print(" -"*20, "\nWelcome to Cover-to-Cover Library!\n","- "*20)

# Application loop
while True:
	
	print("\n\n")	
	print("How can we help you today?\n\nFeel free to choose from the following options.\n")

	# Print the options in a table
	print(tabulate([(1, "Create Membership",), (2, "Show list of books",), (3, "Borrow books",), (4, "Return books",), (5, "Exit",)], tablefmt="fancy_grid"))
	
	# Taking the user's choice from options as (int)
	choice = int(input("\nPlease enter an option: "))

	if choice == 1:
		"""
		If user choice is 1 (int) - Create membership
		"""
		# Get User Member Details
		account_name = input("Enter your name : ")
		pin = int(input("Enter a PIN : "))
		choice = int(input("Enter the type of membership you want?\n 1.Regular\n 2.Gold\n"))

		if choice == 1:
			"""
			If user choice is 1(int) - Create Regular Membership
			"""
			accounts_regular[member_id_regular] = RegularMember(account_name,pin,member_id_regular)
			print("Congratulations, you are now a REGULAR member and your membership ID is: ", member_id_regular)
			member_id_regular += 1

		elif choice == 2:
			"""
			If user choice is 2(int) - Create Gold Membership
			"""
			accounts_gold[member_id_gold] = GoldMember(account_name,pin,member_id_gold)
			print("Congratulations, you are now a GOLD member and your membership ID is: ", member_id_gold)
			member_id_gold += 1

	elif choice == 2:
		"""
		If user choice is 2(int) - Perfron show list of books operation
		"""
		# Get User Member details
		member_id = eval(input("Enter your Member ID : "))
		upin = int(input("Enter your PIN : "))
		choice = int(input("1.Regular\n2.Gold\n"))

		if choice == 1:
			"""
			If user choice is 1(int) - check regular membership details and perform show list of books operation
			"""
			for key,val in accounts_regular.items():
				if upin == accounts_regular[key].pin:
					accounts_regular[key].show_list_of_books()			
				else:
					print("does not exist")
		
		elif choice == 2:
			"""
			If user choice is 2(int) - check gold membership details and perform show list of books operation
			"""
			if upin == accounts_gold[member_id].pin:
				accounts_gold[member_id].show_list_of_books()
			else:
				print("does not exist")

	elif choice == 3:
		"""
		If user choice is 3(int) - Perform Borrow operation
		"""
		# Get User Member details
		member_id = eval(input("Enter your Member ID : "))
		upin = eval(input("Enter your PIN : "))
		choice = int(input("1.Regular\n2.Gold\n"))
		if choice == 1:
			"""
			If user choice is 1(int) - check regular membership details and perform borrow operation
			"""
			for key,val in accounts_regular.items():
				if upin == accounts_regular[key].pin:
					accounts_regular[key].borrow_book()	
			
				else:
					print("does not exist")

		elif choice == 2:
			"""
			If user choice is 2(int) - check gold membership details and perform borrow operation
			"""
			if upin == accounts_gold[member_id].pin:
				accounts_gold[member_id].borrow_book()
			else:
				print("does not exist")

	elif choice == 4:
		"""
		If user choice is 4(int) - Perform Return operation
		"""
		# Get User Member details
		member_id = eval(input("Enter your Member ID : "))
		upin = eval(input("Enter your PIN : "))
		choice = int(input("1.Regular\n2.Gold\n"))

		if choice == 1:
			"""
			If user choice is 1(int) - check regular membership details and perform return operation
			"""
			for key,val in accounts_regular.items():
				if upin == accounts_regular[key].pin:
					accounts_regular[key].return_book()	
				else:
					print("does not exist")

		elif choice == 2:
			"""
			If user choice is 2(int) - check gold membership details and perform return operation
			"""
			if upin == accounts_gold[member_id].pin:
				accounts_gold[member_id].return_book()
			else:
				print("does not exist")

	else:
		break

