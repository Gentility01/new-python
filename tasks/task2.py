# Check if a number entered by the user is even or odd

num = int(input("enter a number "))

if num % 2 == 0:
    print(f"the number {num} is even")
elif num % 2 != 0:
    print(f"the number {num} is odd")