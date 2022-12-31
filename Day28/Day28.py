# It is Day 28 of 100DaysOfCode with CodeWithHarry
# fStrings in Python

letter = "My name is {} and I am from {}"
name = "Ashish Sharma"
country = "India"

print(letter.format(name, country))
# Now the output of this line will be "My name is Ashish Sharma and I am from India, The order of the arguments matter here in format method"

# Here comes the problem solver fStrings in Python

print(f"My name is {name} and I am from {country}")
# Now the output of this line will be same as above with less lines of code and less effort

# The usecase with floating point numbers
floatingNum = 49.09999

print(
    f"The floating point num with 2 decimal places can be written as {floatingNum:.2f}")
# The output will be the same line written in quotes with floating number of 2 decimal places
