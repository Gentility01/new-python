# class Items:
#     discount = 20

#     def __init__(self, name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         # print('this is just me')

#     def total_price(self):
#         return self.price * self.quantity

#     def discount_price(self):
#         self.price = self.price * self.quantity

        

# item1 = Items('laptop', 3000, 2)
# item1.discount_price()
# # print(item1.discount_price())

# class Market:
#     def __init__(self, firstname, lastname, age, contact, email,product, quantity):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.contact = contact
#         self.email = email
#         self.product = product
#         self.quantity = quantity

#     def checkings(self):
#         if self.age < 18:
#             print(f"{self.firstname} you are too young ")
#         if self.quantity < 10:
#             print(f"{self.firstname} this is a wholesale shop you are expected to buy in bulk ")


# customers_firstname = input('Enter your first name')
# customers_lastname = input('Enter your last name')
# customers_age = int(input('Enter your age'))
# if customers_age < 18:
#     print('sssssss')
# else:
#     pass
# customers_contact = int(input('Enter your number'))
# customers_email = input('Enter your email address')
# customers_qty = int(input('Enter your quantity'))



# market1 = Market(customers_firstname, customers_lastname, customers_age, customers_contact, customers_email, 'Phone', customers_qty)
# print(market1.checkings())
# import sqlite3
# conn = sqlite3.connect('customer.db')
# c = conn.cursor()

# all = c.execute("SELECT rowid, * FROM customers")
# for a in all:
#     print(f'names of customers: {a[2]}')

# tuCount = 0
  
    # initialization or constructor method of
    # def __init__(self):  
          
    #     # class Student
    #     self.name = input('enter student name:')
    #     self.rollno = input('enter student rollno:')
    #     Student.stuCount += 1
  
    # displayStudent method of class Student
    # def displayStudent(self):  
    #     print("Name:", self.name, "Rollno:", self.rollno)
  

# Illustration of creating a class
# in Python with input from the user

# class Market:
    
#     def customer(self):
#         self.name = input('enter name')
#         self.lastname = input('enter last: ')
#         self.age = int(input('enter age'))
#         if self.age<10:
#             print('please not permitted here thanks')
#         else:
#             self.quantity = int(input('enter quantity'))
#             self.price = 2000
#             if self.quantity < 5:
#                 print(f'we dont sell{self.quantity} we sell in cartons or any numner above 5')
#             else:
#                total =  self.quantity * self.price
#                print(f'dear {self.name}, the total price of goods you purchased is {total}')
            

# person1 = Market()
# person1.customer()
     

# def users():
#     username = input('enter your name: ')
#     age = input('what is your age: ')
#     hubby = input('What do you like doing: ')
    
#     print(f'my name is {username}  and my age is {age} and i love {hubby} alot...')



# number = int(input('enter a number: '))

# if number < 5:
#     print('very good')
# else:
#     users()

# def person(username, age, hubby):
#     print(f'my name is {username} and my age is {age} and i like {hubby}')


# person('emeka', 20, 'football')

# class Person(object):
 
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
         
#     def details(self):
#         # print("My name is {}".format(self.name))
#         print(f"My name is {self.name}")
#         print("IdNumber: {}".format(self.idnumber))


# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
 
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
         
    # def details(self):
    #     print("My name is {}".format(self.name))
    #     print("IdNumber: {}".format(self.idnumber))
    #     print("Post: {}".format(self.post))


#  creation of an object variable or an instance
# a = Employee('douglas', 886012, 200000, "Intern")
 
# calling a function of the class Person using
# its instance
# a.display()
# a.details()


    


    
# class Student:

#     stuCount = 0
#     # initialization or constructor method of
#     def __init__(self):  
          
#         # class Student
#         self.name = input('enter student name:')
#         self.rollno = input('enter student rollno:')
#         Student.stuCount += 1
  
#     # displayStudent method of class Student
#     def displayStudent(self):  
#         print("Name:", self.name, "Rollno:", self.rollno)
# stu1 = Student()
# stu2 = Student()
# stu3 = Student()
# stu1.displayStudent()
# stu2.displayStudent()
# stu3.displayStudent()
# print('total no. of students:', Student.stuCount)

# import functions
# d = functions.book1
# print(d)

# import sqlite3
# data = sqlite3.connect('customer3.db')
# c = data.cursor()

# c.execute("""CREATE TABLE customers(  
#         first_name text, 
#         last_name text, 
#         email_address text
    
    
# ) """)

# c.execute("INSERT INTO customers VALUES ('Mary', 'Doe', 'mary@gmail.com') ")
# print(c)

# data.commit() 
# data.close()


# n = 1
# while n < 5:
#     n += 1
#     print(n)
# else:
#     print('am done with the loop')



