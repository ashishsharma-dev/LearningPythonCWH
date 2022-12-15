# Nested if else elif statement in python
a = int(input("Enter a number\n"))
if (a < 0):
    print("The number is negative")
elif (a == 999):
    print("A is equal to a special number")
elif (a > 0):
    if (a == 1):
        print("A is equal to 1")
    elif (a == 2):
        print("A is equal to 2")
    else:
        print("A is not equal to 1 or 2")
    print("A is positive")
elif (a == 0):
    print("A is equal to zero")
else:
    print("A is something different")
