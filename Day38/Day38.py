# It is Day 38 of 100DaysOfCode with CodeWithHarry
# Raising Custom Errors in Python

# Lets take a situation that we want to raise an error so that we will not messed up with the further code of our application ans stop the execution then we can use custom errors

# Example given below: 
# a = int(input("Enter any number between 5 and 9"))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# Quick Quiz
# Write a program to not raise an error if user types quit all caps

# userInput = int(input("Enter a number to proceed: "))
# print(userInput>5)
# print(userInput<5)
# print(userInput>9)
# print(userInput<9)

a=input("Enter the number: ")


try:
    if(int(a)>5 and int(a)<9):
        print("It is between 5 and 9")
    else:
        print("Invalid Data")
except:
    print("Invalid Data")

finally:
    if(a.lower()=='quit'):
        print("Quitting Now")