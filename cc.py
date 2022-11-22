# alphabet = "abcdefghijklmnopqrstuvwxyz"
# sentence = input('enter a word ')

# # while sentence not in alphabet.lower():
# #     sentence = input('enter a word ')
# while sentence not in alphabet.upper():
#     sentence = input('enter a word ')


# password1 = input('enter password: ')
# while password1.capitalize() != True:
#         print('password must contain at least one  Uppercase')
#         password1 = input('enter password: ')


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# c = input('enter a letter ')
# if c in alphabet:
#     print(True)
# else:
#     print(False)

# password = input('Enter your password')
# password_letters = list(password)
# upper = False
# lower = False
# name = 'Papa'
# surname = 'Johns'

# for letter in password_letters:
#     if letter.isupper():
#         upper = True
#     elif letter.islower():
#         lower = True

#     if upper and lower:
#         break

# if len(password) <= 5:
#     print('password is to short')
# # elif name.lower() in password.lower() or surname.lower() in password.lower():
# #     print('You cannot have first or last name in password')
# elif not (upper and lower):
#     print('You must have both upper and lower case in password')
# else:
#     print('Password is valid')


# import re

# string = input('enter password ')
# regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
# regex2 = re.compile('1234567890')
# if(regex.search(string) == None):
# 	print("special is absent")
# elif(regex2.search(string) == None):
# 	print('please add a number to your password')
# else:
# 	print("present")

# database = {}

# for userAccountNumber, userDetails in database.items():
# 	pass
# first_name = input ("What is your first name? \n")
# last_name = input ("What is your last name? \n")
# email = input ("What is your Email address? \n")
# userPin = int (input ("Create a 4 digit pin number? \n"))


database = {}
accountNumber = int (input ("Enter Account Number \n"))
userPinLogin = int (input ("Enter User Pin \n"))

for userAccountNumber, userDetails in database.items():
    if (accountNumber == userAccountNumber):
        if (userDetails[3] == userPinLogin):


database[database] = [first_name, last_name, email, userPin]

