# Calculate the factorial of a number.
# b = list(range(1,5 + 1))
# print(b)

def factorial_of_a_number(n):
    factorial = [i * n for i in range(1, n + 1)][-1]
    return factorial


number = int(input("Enter a number "))

f = factorial_of_a_number(number)
print(f)