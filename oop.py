# import numbers


# i = 0
# while i < 10:
    
    
#     i = i+1
#     print(i)
    
    
    
# numbers = 12
# while numbers < 12:
#     numbers += 2
#     print(numbers)
# else:
#     print('done')
    
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
    
# fruits = ['oranges','banana','cashew']
# print(type(fruits))
# print(fruits)

# num = 0
# while num <= 2:
#     i = 1
#     while i <= 10:
#         product = num*i
#         print(num, " * ", i, " = ", product, "\n")
#         i = i + 1
#     num = num + 1
#     print("\n")


# numInput = int(input("Multiplication using value? : "))
# num = 1

# while num <= numInput:
#     i = 0
#     while i <= numInput:
#         product = num*i
#         print(num, " * ", i, " = ", product)
#         i = i + 1
#     print("")  # no need to add explicit newline character because it is automatically added
#     num = num + 1




# number = str(100)
# num2 = str(200)
# if number < num2:
#     print(number + '' + 'is greater than 100')
#     print(f'{number} is greater than 100')

# num1 = 500
# if num1 <= 500:
#     print(True)
# else:
#     print(False)

# number1 = 1000
# number2 = 100
# number3 = 20
# if number1 > number3 or number2 == number1:
#     print(True, f'{number2} is equal to {number1}')
# elif number1 < number3:
#     print('this is not true')
# # elif number2 == number1:
# #     print('ok')
# else:
#     print(False)

# num1 = 2
# num2 = 1
# num3 = 10
# num4 = 10


# if num1> num2:
#     print('good...')
    
#     if num3 == num4:
#         print('this is ok')
#     else:
#         print('error')
# else:
#     print(False)
    
    
# a = 'obi'
# print(type(a))




class Items:
    def __init__(self, name: str, price: float, quantity): 
        # run validation to the  recieved argument
        assert price >= 0 #when you put a negetive number in the price it is going to trow an assetion error
        assert quantity >= 0

        assert price >= 0 , f'price of {price} must not be a negetive number'
        assert quantity >= 0, f'price of {quantity} must not be a negetive number'
        
        
        
        # assign to self.object
        self.name = name  #assigning the attribute of name to the instance  that is going to be created
        self.price = price
        self.quantity = quantity
     

#     def total_price(self):
#         return self.price * self.quantity
    
# item1 = Items('Laptop',23,3)
# print(item1.total_price())


# item1 = Items.__dict__ #all the attribute for  class level
# item2 = Items('Laptop',23,3)
# print(item1)
# print(item2.__dict__) #all ithe attribute for the instance level
    

# class Person(object):
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
#         # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
 
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
         
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))
 
# # creation of an object variable or an instance
# a = Employee('douglas', 886012, 200000, "Intern")
 
# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()
