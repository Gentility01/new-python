# userWord = input('enter a word: ')
# userWord = userWord.upper()
# # print(userWord)

# nonvowels ='zzzzzzzz'

# for u in userWord:
#     if u in  'A':
#         continue
#     elif u in 'E':
#         continue
#     elif u in 'I':
#         continue
#     elif u in 'O':
#         continue
#     elif u in 'U':
#         continue
#     else:
#         nonvowels += u
        
# print(nonvowels)
    
# userWord = input("Please Enter a word: ")
# vowels = set('aeiou')

# wordWithoutVowels = ''.join(character for character in userWord if not character.lower() in vowels)

# print(wordWithoutVowels)

# from re import sub


# name = input('enter a word : ')
# if 'spathiphyllum' in name:
#     pass


# if name == 'pelargonium':
#     print('spathiphyllum! not pelargonium')
# else:
#     print('not my kind of plant')

# if name == name.upper():
#     print('YES spathiphyllum IS THE BEST PLANT EVER!')


# elif name == 'spathiphyllm':
#     print('NO I WANT A BIG spathiphyllum')


# User = input('Enter the secret code: ')

# def correct():
#     # if User == 'python1':
#         print('congrats')
        
# while User != 'python1':
#     # clear_output()
#     User = input('Enter the secret code: ')
# else:
#     correct()


class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))




