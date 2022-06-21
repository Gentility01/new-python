# sets = {'man', 'man', 'woman'}
# length = len(sets)
# print(sets)
# print(length)


# lists =list(('man', 'man', 'woman'))
# print(type(lists))

# dics = dict({'man':'human','woman':'female being'})
# print(type(dics))
# name = {'name':'amanda'}


# lists = ['man', 'man', 'woman']
# lists.append('oooooo')
# print(lists)
# b = set(lists)
# print(b)
# print(type(b))


# sets = ({'man', 'woman', 'girl'})
# print(type(sets))

# lists = ('man', 'man', 'woman')
# b = frozenset(lists)

# print(lists)
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = {8, 9, 10,3 }


# print(A.union(B,C))
# print(A.union(B).union(C))
# print(A.intersection(B,C))
# print(B.intersection(A))
# print(A.difference(B))
# print(B.difference(A))
# print(A.symmetric_difference(B))

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# # intersection
# print(A.intersection(B))  # Output: frozenset({3, 4})

# # difference
# print(A.difference(B))  # Output: frozenset({1, 2})

# # symmetric_difference
# print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})

