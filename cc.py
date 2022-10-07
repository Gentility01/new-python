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


import re

string = input('enter password ')
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(string) == None):
	print("special is absent")
else:
	print("present")