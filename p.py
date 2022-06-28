# # userWord = input('enter a word: ')
# # userWord = userWord.upper()
# # # print(userWord)

# # nonvowels ='zzzzzzzz'

# # for u in userWord:
# #     if u in  'A':
# #         continue
# #     elif u in 'E':
# #         continue
# #     elif u in 'I':
# #         continue
# #     elif u in 'O':
# #         continue
# #     elif u in 'U':
# #         continue
# #     else:
# #         nonvowels += u
        
# # print(nonvowels)
    
# # userWord = input("Please Enter a word: ")
# # vowels = set('aeiou')

# # wordWithoutVowels = ''.join(character for character in userWord if not character.lower() in vowels)

# # print(wordWithoutVowels)

# # from re import sub


# # name = input('enter a word : ')
# # if 'spathiphyllum' in name:
# #     pass


# # if name == 'pelargonium':
# #     print('spathiphyllum! not pelargonium')
# # else:
# #     print('not my kind of plant')

# # if name == name.upper():
# #     print('YES spathiphyllum IS THE BEST PLANT EVER!')


# # elif name == 'spathiphyllm':
# #     print('NO I WANT A BIG spathiphyllum')


# # User = input('Enter the secret code: ')

# # def correct():
# #     # if User == 'python1':
# #         print('congrats')
        
# # while User != 'python1':
# #     # clear_output()
# #     User = input('Enter the secret code: ')
# # else:
# #     correct()


# class Dog:
 
#     # class attribute
#     attr1 = "mammal"
 
#     # Instance attribute
#     def __init__(self, name):
#         self.name = name
 
# # Driver code
# # Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")
 
# # Accessing class attributes
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# # Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))


# name  ='Divine'
# hobby = 'Football'
# age = 20
# stuffs = ('rice','beans','garri')

# print(f'my name is {name}, and i like {hobby}, i am {age} years old i  want to buy {stuffs}')

# name = (input('Enter your name here:\n'))
# age = int(input('Enter your age here: \n'))
# hubby = (input('Enter your hubby here:\n'))

# print(f'my name is {name}, and i like {hubby}, i am {age} years old .')

# name = 'obinna'
# nums = 20
# # nums += 20
# # nums -= 5
# # nums /= 5
# nums *= 5
# print(nums)

# number1 = 50
# number2 = 40 
# number3 = 1000
# total = number1 + number2 + number3
# print(total)

# total2 = number2 % number1
# print(total2)
# '''
# + addition
# - subtraction
# / division 
# * multiplication
# % module
# '''

# mod = 3%2
# print(mod)
# discount = 0.01
# item1 = 2000
# item2 = 1500
# item3 = 200

# original_price = item1+item2+item3
# total = item1+item2+item3 - discount
# print(f'you are ment to pay {original_price}, but you will now pay a discount of {total} thanks...')


# class Teacher:
#     def __init__(self, name,acc):
#         self.name = name
#         self.acc = acc
        
#     def display(self):
#         print(self.name)
#         print(self.acc)
        
#     def details(self):
#         print(f"My name is {self.name}")
#         print("IdNumber: {}".format(self.acc))
        
# class Students(Teacher):
#     def __init__(self,name,acc,s_name, s_class,age):
#         self.s_name = s_name
#         self.s_class = s_class
#         self.age = age
        
#         Teacher.__init__(self, name,acc)
    
#     def details(self):
#         print("my teachers name is {}".format(self.s_name))
#         print("my teachers acc is {}".format(self.name))
        
# a = Students('Douglas', 886012, 'mr nwaogu',2,40)
# a.display
# a.details()
        

class ClassTeacher:
    def __init__(self, teachers_name):
        self.teachers_name = teachers_name
    # def display_teachers_name(self):
    #      print(f'teacher:{self.teachers_name}')
    
  
class SchoolClasses(ClassTeacher):
    def __init__(self, teachers_name):
        
        ClassTeacher.__init__(self,teachers_name)
    
    # def display_subject(self):
    #     print(self.subject)
        
    def primary1(self):
        # print(f'subject is {self.subject}')
        print(f'teacher in primary1 is {self.teachers_name}')
        
    def primary2(self):
        # print(f'subject is {self.subject}')
        print(f'teacher in primary2 is {self.teachers_name}')
        
    def primary3(self):
        # print(f'subject is {self.subject}')
        print(f'teacher in primary3 is {self.teachers_name}')
        
  
        

  
a = SchoolClasses('Douglas')
a.primary1()
a.primary2()
a.primary3()


    



    
    
