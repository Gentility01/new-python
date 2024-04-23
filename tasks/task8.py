# Remove duplicate elements from a list.

def remove_duplicate(list):
    lists = set(list)
    return lists

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_duplicate(list1))