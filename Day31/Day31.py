# It is Day 31 of 100DaysOfCode with CodeWithHarry
# Sets in python

# The output of this line will be all the numbers without duplicate entries
s1 = {2, 4, 5, 6, 8, 4, 8}
# Bcoz Set does not take duplicate values
print(s1)

# Quick Quiz
dummySet = {}  # This will create an empty dictionary not an empty set. So how to create an empty set
# Here is the answer:
emptySet = set()
print(type(dummySet))  # Here the output will be a dictionary
print(type(emptySet))  # Here the output will be a set

# Thing to remember: Set does not maintain the order of the elements inside
