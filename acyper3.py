import string
import os


os.system('clear')

a = list(string.ascii_lowercase)
a.insert(0," ")

sentence_dict = {}

def cyper_alpha():
	text_input = input("Enter Message To Be Coded:\n").lower()
	code_key = input("\nEnter Code Key: ")
	
	if code_key.isdigit() == False:
		print("\nCode Key Needs to be Integer")
		cyper_menu()

	input_list = list(text_input)
	for letter in input_list:
		if letter == " ":
			input_list[input_list.index(letter)] = str("|")
		for x in range(1,27):
			if letter == a[x]:
				input_list[input_list.index(letter)] = "*{}".format(str(x*int(code_key)))
	cypered_text = ''.join(input_list)		
	os.system('clear')
	print("\n")
	print(cypered_text)

def cyper_decrypt():
	cyper_input = input("Enter Encrypted Message: \n")
	decrypt_key = input("\nEnter Code Key: ")

	if decrypt_key.isdigit() == False:
		print("\nCode Key Needs to be Integer")
		cyper_menu()

	cyper_clean1 = cyper_input.replace("*", " ")
	cyper_clean2 = cyper_clean1.replace("|", " 0 ")
	keynum_cyper_list = cyper_clean2.split().copy()

	for key in keynum_cyper_list:
		keynum_cyper_list[keynum_cyper_list.index(key)] = float(key)/float(decrypt_key)

	decrypt_list = keynum_cyper_list.copy()

	for num in decrypt_list:
		for x in range(0,27):
			if int(num) == x:
				decrypt_list[decrypt_list.index(x)] = str(a[x])
	decoded_text = ''.join(decrypt_list)
	#os.system('clear')	
	print("\n")
	print("Decrypted Message:")		
	print(decoded_text)

	
def cyper_menu():
	print("\n*************************\nWelcome to acypher v1.6\n*************************")
	print("1) Enter Message")
	print("2) Decrypt Message\n")
	menu_input = input("Enter Option ")
	if menu_input == "1":
		cyper_alpha()
	elif menu_input == "2":
		cyper_decrypt()
	else:
		print("\n!!!\nInvalid Input\n\n")
		cyper_menu()

while True:
	cyper_menu()



