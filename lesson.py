
# # from pip import main


# # names = ['mmachi', 'daniel', 'anita','obi']
# # name = input('enter a name: ')
# # if name in names:
# #     pass
# # else:
# #     print(f'{name} is not part of our student')
    
    
# # score1 = 100
# # score2 = 90
# # score3 = 80

# # main_score = int(input('enter your score: '))

# # if main_score >= score2 or main_score == score1:
# #     print(f'{name} you scored {main_score} your grade is  A1')
# # elif main_score >= score3 or main_score == score2:
# #     print(f'{name} you scored {main_score} your grade is  B2')

# airtime1 = 100
# airtime2 = 200
# airtime3 = 300
# airtime4 = 400
# airtime5 = 500
# persons_input = int(input("enter an amount: \n press 1 for 100, \n press 2 for 200, \n press 3 for 300\n "))

# if persons_input == 1:
#     print(f'{airtime1} was done')
# elif persons_input == 2:
#     print(f'{airtime2} was done')
# else:
#     print('you are expected to press only 1 or 2')
    
# 3 = 0

# while num < 20:
#     num += 1
#     print(num)


# lists = ['mmachi','daniel','anita', 'douglas', 'uba']
# lists.append('obinna')
# tuples = ('mmachi','daniel','anita', 'douglas', 'uba')
# tuples.append('obinna')
# print(tuples)


# for l in lists:
#     # print('we have ',ashpotnames, 'in ashpot')
#     print(f'we have {n} in ashpot')


# oo ='oke'.capitalize()
# print(oo)

# def birthday():
#     name = 'your name is not in may born'
#     print(name)
    

# may_born =['Obinna', 'Adaeze','Emeka']
# name = input('enter your name \n').capitalize()
# age = 20
# if name in may_born:
#     print(f'{name}, you are welcome to month of may')
# else:
#     birthday()


# def names(first_name, last_name, age):
#     print(first_name, last_name, age)
    

# may_born =['Obinna', 'Adaeze','Emeka']
# name = input('enter your name \n').capitalize()

# if name in may_born:
#      print(f'{name}, you are welcome to month of may')
# else:
#     names('Mmachi','Njoku',20)

# def calculations(num1, num2, num3):
#     first_number = num1
#     second_number = num2
#     third_number = num3
    
#     print(first_number + second_number * third_number)
   
# calculations(20,10,5)


'''methods are things we can perform on an object'''


# from turtle import back


# import email

# from yaml import emit


# def registeration_form():
#     name = input('please enter your name: ')
    
#     email = input('enter your email: ')
#     if '@' not in email and '.com ' not in email:
#         print('invaalid email address try again')
#         registeration_form()
#     password = input('enter a password: ')
#     # if len(password) < 6:
#     #     print('your password should not be less more than six characters')
#     while len(password) < 6:
#         print('your password should not be less more than six characters')
#         password = input('enter a password: ')
    
#     # name = input('enter a name: ')
#     # email = input('enter an email: ')
#     # if '@' not in email and '.com' not in email:
#     #     print('invalid email address')
        
            
# registeration_form()

# class PersonClass():
#     def persons_name(self):
#         print('anita')
#     def person_age(self):
#         print(49)
        
# p = PersonClass()
# p.persons_name()
# p.person_age()

# class Students():
    
#     def Amaka(self):
#         print('Amaka is a girl')
    
#     def Obina(self):
#         print('Obinna is a guy')
        
# d = Students()
# d.Amaka()
# d.Obina()


# class Person():
#     def talk(self):
#         print('i can talk')
    
#     def walk(self):
#         print('i cann walk')
        
# p = Person()
# p.walk()


# slicing
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

# lamda functions
'''A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.'''
x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result
x = lambda a, b : a * b
print(x(5, 6))

m = lambda a,b,c: a + b + c
print(m(10,10,10))


