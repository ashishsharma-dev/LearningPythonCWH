# It is Day 38 of 100DaysOfCode with CodeWithHarry
# Raising Custom Errors in Python

# Lets take a situation that we want to raise an error so that we will not messed up with the further code of our application ans stop the execution then we can use custom errors

# Example given below: 
a = int(input("Enter any number between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")