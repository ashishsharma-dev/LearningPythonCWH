# It is Day 25 of 100DaysOfCode with CodeWithHarry
# Operations in Tuples

# Even tuples are immutable, you can change tuple by converting them into a list and then reconvert into tuple again, an example is given below
tuple1 = ("Ashish", "Sharma", "Nikki", "Sharma")
tempTuple = list(tuple1)

# Now we can perform list methods here

tempTuple.pop(2)  # Second index item popped from the list
print(tempTuple)

tempTuple[2] = "Nikki"  # Second index now has a value of "Nikki"
print(tempTuple)

tempTuple.append("Sharma")
print(tempTuple)

finalTuple = tuple(tempTuple)
print(type(finalTuple))

# Count method is to count the occurences of an element
countOfSharma = finalTuple.count("Sharma")
print(f"The count of Sharma is {countOfSharma}")


# This will return the index of first occurence of an element
# You can also limit your searches in a given indexes like (finalTuple.index("element", startIndex, endIndex))
indexOfSharma = finalTuple.index("Sharma", 0, len(finalTuple))
print(indexOfSharma)
