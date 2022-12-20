# It is Day 19 in 100DaysOfCode with CodeWithHarry
# Topic is break and continue keywords in python

# for i in range(1, 11):
#    if (i == 5):
#  continue  # The continue keyword will left the current iteration only
# print(i, end=", ")


# for i in range(1, 11):
# if (i == 5):
#    break  # The break keyword will break the whole iteration
# print(i, end=", ")


# Implementation of do-while loop in Python
while True:
    number = int(input("Enter the number to run the loop till"))
    print(number)
    if not (number >  0):
        print("The loop is reached to the breakpoint")
        break
