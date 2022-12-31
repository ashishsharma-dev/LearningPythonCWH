# It is Day 30 of 100DaysOfCode with CodeWithHarry
# Recursion in Python

# We will take an example of factorial
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1

# Then we can say that:
# factorial(n) = n * factorial(n-1)

# Now we will convert this into python code
def makeFactorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * makeFactorial(n-1)


# print(makeFactorial(4))

# Quick quiz to print the fibonacci series nums

def f(n):
    if (n == 0):
        return 0

    if (n == 1):
        return 1
    else:
        return f(n-1) + f(n-2)


print(f(6))

# Here we are getting 10 fibonacci nums
for i in range(10):
    print(f(i), end=", ")
