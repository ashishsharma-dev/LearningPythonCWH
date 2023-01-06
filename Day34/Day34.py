# It is Day 34 of 100DaysOfCode with CodeWithHarry
# Dictionary Methods in python

ep1 = {122: 45, 123: 52, 124: 62}
ep2 = {222: 25, 223: 61, 224: 85}

# Methods mentioned below

# update()
ep1.update(ep2)  # This will copy all the elements of ep2 in the ep1
print(ep1)  # The output will be the total items of ep1 and ep2
print(ep2)  # The output will be the ep2 as it is


# clear()
# ep1.clear()
print(ep1)  # Here we will get an empty dictionary

# pop()
# ep1.pop(122) # This will pop the given item from the dictinary
print(ep1)

# popitem()
# ep1.popitem()  # This will pop the last item from the dictionary
print(ep1)

# del()
# del ep1[122] # With using this method we can remove the given item from the dictionary
# del ep1  # With using this way we can remove the whole dictinary
print(ep1)
