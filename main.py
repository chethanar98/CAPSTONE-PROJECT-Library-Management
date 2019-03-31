from library_manager import LibraryManager,RegularMember, GoldMember
print("Welcome to PEEK-A-BOOK LIBRARY")
accounts_regular={}
accounts_gold={}
member_id_regular=1000
member_id_gold=2000



while True:
	choice = int(input("Hello, what do you want to do today?\n\n\
		1. Create membership\n\
		2. Show list of books\n\
		3. Borrow books\n\
		4. Return books\n"))


	if choice==1:
		account_name=input("Enter your name : ")
		pin=int(input("Enter a PIN : "))
		choice=int(input("Enter the type of membership you want?\n 1.Regular \n 2.Gold \n"))

		if choice==1:
			accounts_regular[member_id_regular]=RegularMember(account_name,pin,member_id_regular)
			print("Congratulations, you are now a REGULAR member and your membership ID is: ", member_id_regular)
			member_id_regular +=1
		elif choice==2:
			accounts_gold[member_id_gold]=GoldMember(account_name,pin,member_id_gold)
			print("Congratulations, you are now a GOLD member and your membership ID is: ", member_id_gold)
			member_id_gold +=1

		
		
	elif choice==2:
		member_id=eval(input("Enter your Member ID : "))
		upin=int(input("Enter your PIN : "))
		choice=int(input("1.Regular \n2.Gold\n"))

		if choice==1:

			# if upin == accounts_regular[member_id].pin:
			# 	accounts_regular[member_id].show_list_of_books()

			for key,val in accounts_regular.items():
				if upin == accounts_regular[key].pin:
					accounts_regular[key].show_list_of_books()	
					

				else:
					print("does not exist")
		
		elif choice==2:

			if upin==accounts_gold[member_id].pin:
				accounts_gold[member_id].show_list_of_books()
			else:
				print("does not exist")


		
	elif choice==3:
		member_id=eval(input("Enter your Member ID : "))
		upin=eval(input("Enter your PIN : "))
		choice=int(input("1.Regular\n2.Gold\n"))
		if choice==1:
			for key,val in accounts_regular.items():
				if upin == accounts_regular[key].pin:
					accounts_regular[key].borrow_book()	
				else:
					print("does not exist")
		elif choice == 2:
			if upin==accounts_gold[member_id].pin:
				accounts_gold[member_id].borrow_book()
			else:
				print("does not exist")

		
		
	elif choice==4:
		member_id=eval(input("Enter your Member ID : "))
		upin=eval(input("Enter your PIN : "))

		choice=int(input("1. Regular\n2.Gold\n"))
		if choice==1:
			for key,val in accounts_regular.items():
				if upin == accounts_regular[key].pin:
					accounts_regular[key].return_book()	
				else:
					print("does not exist")
		elif choice == 2:
			if upin==accounts_gold[member_id].pin:
				accounts_gold[member_id].return_book()
			else:
				print("does not exist")
	

	else:
		break

