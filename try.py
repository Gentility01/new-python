# # try:
# #     a = aba
# #     print(a)
# # except:
# #     print('i know that this is an error')

# name = input('enter name: ')

# try:
#     if name == obi:
#       pass
#     else:
#         print(False)
  
# except:
#     print('obi')


# # name = obi
# # print(name)
        
        
# try:       
#     age = int(input('enter your age: '))
#     print(age)
# except ValueError:
#     print('you are expected to put in a number')
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# define Python user-defined exceptions


# class Error(Exception):
#     """Base class for other exceptions"""
#     pass
  
  
  
  
  
class RandomNUmber(Exception):
  pass


class ValueTooSmallError(RandomNUmber):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(RandomNUmber):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")


