first_name =input('Please enter your first name ').capitalize()
lastname =input('Please enter your last name ').capitalize()
password = input('Please enter your password ')

if len(password) <=6 :
    print(f' Dear {lastname} your password should be more than 6 characters')

    
if password.istitle():
    pass
else:
    print(f'Dear {first_name} Your password must start with a capital letter')
    
if '#' in  password  and '_' in password:
    pass
else:
    print('error in password')
        
        



