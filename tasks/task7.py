# Count the number of vowels in a string

def number_of_vowels(string):
    count = 0
    for i in string:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


print(number_of_vowels('hello'))