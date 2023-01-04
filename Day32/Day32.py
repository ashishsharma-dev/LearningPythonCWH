# It is Day 32 of 100DaysOfCode with CodeWithHarry
# Set Methods in Python

s1 = {2, 3, 4}
s2 = {3, 4, 6}
print(s1.union(s2))  # To add all the elements of s1 and s2 only once
# Here s1 and s2 both the sets are untouched until we use update method given below
print(s1, s2)
# s1.update(s2)
print(s1, s2)
# print(s1.intersection(s2))  # To get the common elements in s1 and s2

# intersection_update

# s1.intersection_update(s2)
# print(s1)

s1.symmetric_difference(s2)
print(s1)

# isdisjoint() >> used to know the items of a set are available in the other set or not

# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"} # In this condition the code will return True if any of the set item matches then it will return False

# print(set1.isdisjoint(set2))

# issuperset() is used to know if set elements available in other set or not like below
# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# It will print False as set2 elements are not available in the set1
# print(set1.issuperset(set2))

# issubset() is truely opposite of the issuperset() example given below
# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# It will print False as set1 elements are not available in the set2
# print(set1.issubset(set2))

# add() is to add an item in a set like below
# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# set1.add("Guava")
# set2.add("Orange")

# print(set1)
# print(set2)

# If we want to add more than one item then we can use update() method

# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# set1.update(set2)
# print(set1)  # This will add all the items of set 2 in the set 1

# remove()/discard() can be used to remove an item from the set examples given below
# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# The work of both the methods remove()/discard() is the same but if the element you want to remove is not available in the set then the remove() method will raise an error and discard will not (that is the major diffrent)
# Here we will get an error because the item of we are searching for is not available in the set
# set1.remove("Apples")
# As we know that the given item is not available in the set, we are using discard() hence we will not get any error
# set1.discard("Apples")
# print(set1)

# pop() is to use pop the value from the set
# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# poppedVal = set1.pop() # This method will give us the rangdomly popped value from the set it can be Apple or Bannan
# print(poppedVal)


# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# del() method is to del the whole set

# del set1
# print(set1)  # here we will get an error because we have already deleted the set above

# What is we want to delete whole elements from a set and not the complete set
# then we can use clear() like below

# set1 = {"Apple", "Banana"}
# set2 = {"Pineapple", "Peach"}

# set1.clear()
# print(set1)  # The output will be an empty set


# We can also perform this type of operations in sets
lastSet = {"Ashish", 20, True, 3.5}

if "Ashish" in lastSet:
    print("Ashish is present")
else:
    print("Ashish is not present")
