import time
alphabet = "abcdefghijklmnopqrstuvwxyz"
specialcharacters = "@-_/^*()&%$#!"
#register
def register():
    username = input('enter username: ')
    email = input('enter email: ')

    while '@' and '.com' not in email:
        print('email check your email and try again')
        email = input('enter email: ')
    
    password1 = input('enter password: ')
    password_letters = list(password1)
    upper = False
    lower = False
    name = username
    for letter in password_letters:
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True

        if upper and lower:
            break

    if len(password1) <= 5:
        print('password is to short')
        password1 = input('enter password: ')
    elif name.lower() in password1.lower():
        print('You cannot have username  in password')
        password1 = input('enter password: ')
    elif not (upper and lower):
        print('You must have both upper and lower case in password')
        password1 = input('enter password: ')
    else:
        print('Password is valid')

   
        
   


    password2 = input('confirm password: ')
    while password1 != password2:
        print('two passwords didnt match')
        password1 = input('enter password: ')
        password2 = input('confirm password: ')




def login():
    username = input('enter username: ')
    password = input('enter password: ')

print('''
==========================================================
WELCOME TO ASHPORT GLAD TO HAVE YOU
========================================================
''')
account = int(input('DO YOU HAVE AN ACCOUNT WITH US \n 1. YES \n 2. No\n'))

if account == 1:
    
    print('please wait your form is processing...')
    time.sleep(3.5)
    print('''
    ........................
    please login
    ........................
    ''')
    time.sleep(1.5)
    login()
elif account == 2:
    print('please wait your form is processing...')
    time.sleep(3.5)
    print('''
    ........................
    please register
    ........................
    ''')
    register()


