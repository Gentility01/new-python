# Check if a given string is a palindrome.

def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    if s == s1:
        print("the word is a palindrome")
    else:
        print("the word is not a palindrome")
    return s1

words = input("Enter a word: ")
r = reverse_join_reversed_iter(words)
print(r)