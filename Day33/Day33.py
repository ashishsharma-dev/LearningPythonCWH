# It is Day 33 of 100DaysOfCode with CodeWithHarry
# Dictionary in Python

listOfStudents = {"fname": "Ashish", "lname": "Sharma", "occupation": "MERN Developer"}

print(listOfStudents) # To print the whole dictionary

# Both the ways to get the value of an item available in the listOfStudents (dictionary)
# print(listOfStudents["fname"]) 
print(listOfStudents.get("fname"))

# But if we use bracket notation to get the value of dictionary item and if the value is not available then we will get an error
# on the opposite side if we use get() method to get the value of dictionary item and the value is not available then we will get None

# If we want to get multiple values of a dictionary then we can use values() method like below

print(listOfStudents.keys()) # To get all the keys 
print(listOfStudents.values()) # To get all the values in the dictionary

# We can also loop through the values like below
for key in listOfStudents.keys():
    print(key)

for values in listOfStudents.values():
    print(values)

# Accessing key value pairs in dictionary
for pair in listOfStudents.items():
    print(f"{pair[0]}: {pair[1]}")

#  We can also do like below
for key, pair in listOfStudents.items():
    print(f"{key}: {pair}")

