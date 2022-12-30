# It is Day 23 of 100DaysOfCode with CodeWithHarry
# List Methods

list1 = [1, 2, 3, 4, 20, 18, 5, 6]
print(list1)
list1.append(7)
# This append method will append the element in the last index of the list
print(list1)
list1.sort()
# This sort method will sort the list items in ascending order but if we give a parameter of reverse=True
# Then the output will be a sorted list in descending order
print(list1)

list1.reverse()
print(list1)  # The output will be a descending order sorted list or reversed list

indexNum = list1.index(20)
print(indexNum)  # This will print 0 as the index of 20 in the reversed list is 0 or the index of first occurence of an item in the list

countNum = list1.count(20)
print(countNum)

newList = list1  # Here we are referencing newList to the original list
print(newList)
print(newList[0])
newList[0] = 500
print(newList)  # Here the output will be same as list1
print(list1)  # Here the output will be same as newList

# Genuine way for making a copy of a list
newListCopy = list1.copy()
print("New List Copy")
print(newListCopy)


# Insert method to insert an element on an index
newListCopy.insert(1, 566)
print(newListCopy)

# Extend method to extend a list like below
anotherNewList = [2, 5, 6]
newListCopy.extend(anotherNewList)
# Applying this method on a list will result in a list with extended elements in the last indexes
print(newListCopy)

# Concatenation in lists

listOne = [2, 4, 5]
listTwo = [6, 7, 8]
print(listOne + listTwo)  # Appying this method will result in [2,4,5,6,7,8]
