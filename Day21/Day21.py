# It is Day 21 of 100DaysOfCode with CodeWithHarry
# Functions with Arguments in Python

# There are four types of function arguments in python

# Default Arguments
# Keyword Arguments
# Variable Lenght Arguments
# Required Arguments

# Default Arguments:

def averageFunc(a=5, b=3):
    print(f"The average is {(a+b)/2}")


# averageFunc()  # This function will print 4.0 without giving any arguments but if we give argument in the function then it will print according to the arguments

# Keyword Arguments

def keywordArgFunc(fName="Ashish", lName="Sharma"):
    print("Your name is", fName, lName)


keywordArgFunc("Ashish", "Sharma")  # We can do like this
# OR
keywordArgFunc(lName="Sharma", fName="Nikki")  # We can also do like this
# The order will not matter in this case only

# Required Arguments


def requiredArgFunc(fName, lName="Sharma"):
    print("Your name is", fName, lName)


# requiredArgFunc() This function will throw error if we will not lName as
requiredArgFunc("Vivek")
# Variable length arguments


def varLenFunc(*numbers):  # In this function argument we can give infinite numbers or arguments
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum / len(numbers))


def varLenFunc2(*names):
    for name in names:
        print(name)


varLenFunc(1, 2, 3, 4, 5, 6, 7, 8, 9)
varLenFunc2("Ashish", "Nikki", "Vinod", "Chotu")
