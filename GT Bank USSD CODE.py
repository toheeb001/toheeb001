#U19/FEA/SED/1030
# I KABIR TOHEEB ABDULHAMEED WRITE A PROGRAM OF GT BANK 
print("MAY ALMIGHTY BLESS DR ABDULLAHI KAWU")
print("\n")
print("\n")
print("HERE ARE THE AVAILABLE USSD CODE:")
print("GT Bank:*737#\nAccess:*901#\nUBA:*919#")
print("The Bank USSD Code Is 737")
def menu():
	print(f"You have entered the code for { bank}")
	print("1.Airtime-self\n2.Airtime-other\n3.Data\n4.Trsf-GTB\n5.Trsf-other\n6.Next\n")
	option=eval(input("please select an option:\n"))
	if(option==1):
		amount=eval(input("Enter amount\n"))
		pin=eval(input("Enter your 4digit pin\n"))
		print("Transaction Successful")
		back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
		if(back==1):
			menu()
		elif(back==2):
			exit()
		else:
			("wrong input")
	elif(option==2):
		number=eval(input("please enter 3rd party number\n"))
		amount=eval(input("Enter amount\n"))
		print(f"Enter your 737 or Token Code to Top Up {number} on MTN with NGN {amount}")
		pin=eval(input(" "))
		print("Transaction Successful")
		back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
		if(back==1):
			menu()
		elif(back==2):
			exit()
		else:
			("wrong input")
	elif(option==3):
		data =eval(input("purchase data for:\n1.Self\n2.3rd party\n"))
		if (data==1):
			self=eval(input("1.100MB 1day N100\n2.350MB 7days N300\n3.750MB 14days N500\n4.1GB 1day N300\n5.1.5GB 30days N1000\n"))
			if(self==1):
				pin=eval(input("Enter your 4digit pin\n"))
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			elif(self==2):
				pin=eval(input("Enter your 4digit pin\n"))
				print("Tansaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			elif(self==3):
				pin=eval(input("Enter your 4digit pin\n "))
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n "))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			elif(self==4):
				pin=eval(input("Enter your 4digit pin\n"))
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To rerurn to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			else:
				(self==5)
				pin=eval(input("Enter your 4digit pin\n"))
				print("Transaction successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
		elif(data==2):
			number=eval(input("please enter 3rd party number\n"))
			_3rd_party=eval(input("1.100MB 1day\n2.350MB 7days\n3.750MB 14days N500\n4.1GB 1day N300\n5.1.5GB 30days N1000\n"))
			if(_3rd_party==1):
				print(f"Enter your your 737 or Token to confirm the purchase of  100MB 1day data boundle for {number}")
				pin=eval(input())
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			elif(_3rd_party==2):
				print(f"Enter your your 737 or Token to confirm the purchase of  350MB 7days data boundle for {number}")
				pin=eval(input())
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			elif(_3rd_party==3):
				print(f"Enter your your 737 or Token to confirm the purchase of  750MB 14days data boundle for {number}")
				pin=eval(input())
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			elif(_3rd_party==4):
				print(f"Enter your your 737 or Token to confirm the purchase of  1GB 1day data boundle for {number}")
				pin=eval(input())
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
			else:
				(_3rd_party==5)
				print(f"Enter your your 737 or Token to confirm the purchase of  1.5GB 30days data boundle for {number}")
				pin=eval(input())
				print("Transaction Successful")
				back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
				if(back==1):
					menu()
				elif(back==2):
					exit()
				else:
					("wrong input")
	elif(option==4):
		amount=eval(input("please enter amount\n"))
		account=eval(input("Enter receipient's ACCOUNT NUMBER or PHONE NUMBER or SURNAME\n0"))
		print(f"Enter your 737 or Token to confirm transfer of {amount} to KABIR, TOHEEB ABDULHAMEED N{account} at N20 charge.")
		pin=eval(input())
		print("Transaction Successful")
		back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
		if(back==1):
			menu()
		elif(back==2):
			exit()
		else:
			("wrong input")
	elif(option==5):
		amount=eval(input("please enter amount\n"))
		account=eval(input("Enter receipient's ACCOUNT NUMBER or SURNAME\n0"))
		banks=eval(input("please enter:\n1.First bank\n2.Access (daimond)\n3.Access4\n4.Zenith\n5.UBA\n"))
		if(banks==1):
			print(f"Enter your 737 or Token to confirm transfer of {amount} to KABIR, TOHEEB ABDULHAMEED N{account} at N20 charge.")
			pin=eval(input())
			print("Transaction Successful")
			back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
		elif(banks==2):
			print(f"Enter your 737 or Token to confirm transfer of {amount} to KABIR, TOHEEB ABDULHAMEED N{account} at N20 charge.")
			pin=eval(input())
			print("Transaction Successful")
			back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
		elif(banks==3):
			print(f"Enter your 737 or Token to confirm transfer of {amount} to KABIR, TOHEEB ABDULHAMEED N{account} at N20 charge.")
			pin=eval(input())
			print("Transaction Successful")
			back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
		elif(banks==4):
			print(f"Enter your 737 or Token to confirm transfer of {amount} to KABIR, TOHEEB ABDULHAMEED N{account} at N20 charge.")
			pin=eval(input())
			print("Transaction Successful")
			back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
		else:
			(banks==5)
			print(f"Enter your 737 or Token to confirm transfer of {amount} to KABIR, TOHEEB ABDULHAMEED N{account} at N20 charge.")
			pin=eval(input())
			print("Transaction Successful")
			back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
	else:
		(option==6)
		next=eval(input("1.A.C Balance\n"))
		if(next==1):
			print("please Enter your 737 pin at N10 charge to confirm:")
			pin=eval(input())
			print("(0493627697 - NGN10019.20) NAME: KABIR TOHHEB ABDULHAMEED  BVN: 27697257871")
			print("Transaction Successful")
			back=eval(input("Enter:\n1.To return to menu\n2.To exit\n"))
			if(back==1):
				menu()
			elif(back==2):
				exit()
			else:
				("wrong input")
			
ussd= eval(input('please type in your bank ussd code:'))
if (ussd==737):
	bank= 'GT Bank'
	menu()
else:
	print('wrong input')					