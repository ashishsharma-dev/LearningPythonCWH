# It is Day 37 of 100DaysOfCode with CodeWithHarry
# Finally keyword in python

try:
    l = [1,5,7,9]
    i = int(input("Enter a number: "))
    print(f"The value of this number is: {l[i]}")
except: 
    print("Some Error Occured")
# Now comes the finally keyword which will be executed in any condition
finally: 
    print("I will execute in any condition")

# Usecases of finally keyword can be:
# If we want to use some clean up code then we can add it to the finally code block
# If we want to execute some code for sure then we can use finally keyword