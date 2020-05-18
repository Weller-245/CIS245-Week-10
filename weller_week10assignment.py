#Brianna Weller - CIS245 Week 10 Assignment 10.1
#
#This program requests user input, writes it into a file specified by the user, and reads it back for validation.


import os # import the OS library
import json # import the JSON library

def get_file_info():
	# function for gathering and validating file path and file name from user
	while True:
		filePath = input("\nEnter file path using forward slashes (ex. - C:/Users/NAME/Documents/): ")
		try:
			if os.path.isdir(filePath):   # check if file path exists
				print('Directory Exists')
			else:
				raise OSError   # raise error if file path not valid (OS method catches but does not raise)

		except OSError:
			print("Sorry, directory not found. Please enter a valid path.")

		else:	
			fileName = input("\nEnter file name (ex. - testFile.txt): ")
			completePath = filePath+fileName
			return completePath

def get_user_info():
	# function for gathering user input and adding to dictionary
	userInfo = {}

	userName = input("\nEnter your name: ")
	userInfo['name'] = userName

	userAddress = input("Enter your address: ")
	userInfo['address'] = userAddress

	userPhone = input("Enter your phone number: ")
	userInfo['phone'] = userPhone

	return userInfo

def export_to_file(fileID, expData):
	# function for opening/creating and writing user info to file
	with open(fileID, 'w') as fileHandle:
		json.dump(expData, fileHandle)

def validate_user_info(fileID, expData):
	# function for reading user info back from file and presenting to user for validation
	with open(fileLocation, 'r') as fileHandle:
		x = json.load(fileHandle)
		print(f"\nPlease review your information:\n")
		print(f"\tName: {x['name']}")
		print(f"\tAddress: {x['address']}")
		print(f"\tPhone: {x['phone']}")


if __name__ == '__main__':
	fileLocation = get_file_info()   # request file path and file name from user, validate path exists

	active = True
	while active:
		userData = get_user_info()   # request user input and add to dictionary
		export_to_file(fileLocation, userData)   # write user info dictionary to txt file
		validate_user_info(fileLocation, userData)   # read user info txt back into program and present to user to review
		
		valid = input("\nIs this information correct? (enter Y or N): ")   # request user to confirm if information is correct
		if valid == 'Y':
			print("\nThank you for confirming!")   # if correct, end
			active = False
		elif valid == 'N':
			print("\nPlease enter your information again -\n")   # if incorrect, request user input again, write to txt file, and display for review
		else:
			print("\nI'm not sure what you meant, please enter your information again -\n")
