# It is Day 36 of 100DaysOfCode with CodeWithHarry
# Exception Handling / Error Handling in python

# Lets take a test case here
# We want to print table of a number and we only want an integer from the user to print the table of the given integer
# What if the user types a string or another data type 😕 then our code will stop executing further
# That is the reason we use try and except here for the exception handling

tableOf = input("Enter the number: ")

print(f"The table of {tableOf} is printed below:")

try:
    for i in range(1, 11):
        print(f"{int(tableOf)} X {i} = {int(tableOf)*i}") # Here we will get a custom error
        # If We do not get the integer in above from the user then we will get a custom error
except Exception as e:
    print("Custom Error Message")

print("Here some lines of important code")
print("Some other important lines of code")