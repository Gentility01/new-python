# Find the largest element in a list

def largest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest

items = [10, 300, 20, 4, 45, 99]
print(largest(items))
