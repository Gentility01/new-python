# l = set('obi is a boy')
# t = ('a','e','i','o','u')



# word = list(filter(lambda t: t, l))
# # print(word)
# for b in word:
#     if b in t:
#             print(b)


# subject = [('english', 88), ('science', 90), ('maths', 97)]
# a = subject[2]
# b = subject[1]
# c = subject[0]
# print(a,b,c)

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[1])
# print("\nSorting the List of Tuples:")
# print(subject_marks)


'''write a python program to convert month name to a number of days in that month
expected output 
lists of moonths january to may
input name of month feb number of days 28 or 29 days'''

months = [ '',  '1, January','2, febuary','3, march','4, april','5, may','6, june','7, july','8, august','9, september','10, october','11, november','12, december',]
# m = months.index('1, January')
# print(m)
# for m in months:
#     print(m)
# or months.index('6, june') or months.index('9, september') or months.index('11, november')
choose = int(input('Choose a month\n->> '))
days = 30
# if choose == 9 or 4 or 11 or 6:
if choose == months.index('4, april'):
    print(f'April have {days} days in a month')
elif  choose == months.index('6, june'):
    print(f'June have {days} days in a month')