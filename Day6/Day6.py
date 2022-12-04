# Day 6 Variables & Data Types
a = 1  # a is number
b = 'Ashish'  # b is string
c = True  # c is boolean
d = None  # d is None type
e = complex(2, 1)

print(a, b, c, d, e, sep=" - ")
print(type(a), type(b), type(c), type(d), type(e), sep=" - ")
# ⏬ Prints
# <class 'int'> - <class 'str'> - <class 'bool'> - <class 'NoneType'>


# List

list1 = ['Apple', 'Banana', 526, ['AnotherApple', 'AnotherBanana']]
print(list1)
print(type(list1))
# Tupple

tupple1 = ('tupple1', 'tupple2', 'tupple3', ('tupple4', 'tupple5'))
print(tupple1)
print(type(tupple1))

# Dictionary

dic1 = {"fname": "Ashish", "lname": "Sharma", "position": "Web Developer"}
print(dic1)
print(type(dic1))
