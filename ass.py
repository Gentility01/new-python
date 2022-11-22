'''use user input to create a form which contains firstname, lastname, age and level using a condition if the person
is less than 12 or up to 12 he or she should be in jss1
if age is up to 14 should be in jss2
etc'''

# from unicodedata import name


# firstname = input('Enter first name \n')
# lastname = input('Enter last name \n')
# age = int(input('Enter your age \n'))
# # level = int(input(""" 
# # Please choose your class
# # 1. JSS1
# # 2. JSS2
# # 3. JSS3
# # 4. SS1
# # """))

# if age <=10 and age <= 12:
#     print(f' Dear {firstname} {lastname} WElcome to JSS1')
# elif age > 12 and age <= 14:
#     print(f' Dear {firstname} {lastname} Welcome to Jss 2')


# number = int(input('enter a number '))


# for a in range(2, number+1):
#     print(f'{a}')

def goods(name, price, quantity):
    total = price * quantity
    print(f'product name: {name}, product price {price}, product quantity {quantity} total {total}')


quantity = int(input('enter quantity: '))
goods('laptop', 300000, quantity)