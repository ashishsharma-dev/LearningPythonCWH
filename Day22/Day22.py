# It is Day 22 of 100DaysOfCode with CodeWithHarry
# Lists in Python

list1 = ["Ashish", "Nikki", "Chotu", "Vinod", "Puneet", "Rekha", "Dev"]
# Lists in python can able to store various data types
list2 = ["Ashish", 2, True]

print(list1)
# As most of the programming languages the index of the list will be started from 0
print(list1[0])
print(list1[1])
print(list1[2])
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[-1])
# Negative Indexing means (len(list2)-1) here, so this line of statement will print 3-1=2 means list2[2] = True

# If we want to know, an element exists or not in the list
if "Nikki" in list1:
    print("Yes")
else:
    print("No")


if 2 in list2:
    print("Yes")
else:
    print("No")

# listName[start : end : jumpIndex]
# An example of start : end
print(list1[:])  # The output will be whole list items
print(list1[1:])  # The output will be whole list items without the first one
print(list1[1:2])
# The output will be whole list items without the first one and the last one means not including the start and the end indexes

# Negative index will work like same here: For Example
# This will convert into print(list1[1: len(list1)-1]) ==> and the output will be second item of the list and 1st index
print(list1[1:-1])

# An example of jumpIndex
# Here the output will start printing from the first index of list1 till 6th index with the gap of 1 element
print(list1[1:7:2])

# List Comprehension
list3 = [i for i in range(5)]
print(list3)
