from abc import ABC, abstractmethod

# #Abstract Class
# class Bank(ABC):
#    def bank_info(self):
#        print("Welcome to bank")
#    @abstractmethod
#    def interest(self):
#        "Abstarct Method"
#        pass
# #Sub class/ child class of abstract class
# class SBI(Bank):

#    def interest(self):
#        "Implementation of abstract method"
#        print("In sbi bank 5 rupees interest")
# s= SBI()
# s.bank_info ()
# s.interest()


# #Abstract Class
# class Bank(ABC):
#    def bank_info(self):
#        print("Welcome to bank")
#    @abstractmethod
#    def interest(self):
#        "Abstarct Method"
#        print(True)
#Sub class/ child class of abstract class
# class SBI(Bank):

#    def interest(self):
#        print("Balance is 100")
# s= SBI()
# s.bank_info ()
# # s.from abc import ABC, abstractmethod

# #Abstract Class
# class Bank(ABC):
#    def bank_info(self):
#        print("Welcome to bank")
#    @abstractmethod
#    def interest(self):
#        "Abstarct Method"
#        print(True)
# #Sub class/ child class of abstract class
# class SBI(Bank):

#    def interest(self):
#        print("Balance is 100")
# s= SBI()
# s.bank_info ()
# s.interest()

from abc import ABC, abstractmethod

#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
#Sub class/ child class of abstract class
class SBI(Bank):

   def balance(self):
       print("Balance is 100")

class Sub1(SBI):
   def interest(self):
       print("In sbi bank interest is 5 rupees")

s= Sub1()
s.bank_info ()
s.balance()
s.interest()