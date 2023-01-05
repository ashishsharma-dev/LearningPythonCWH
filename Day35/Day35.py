# It is Day 35 of 100DaysOfCode with CodeWithHarry
# For loop with else in python

for i in range(10):
    print(i)
else:
    print("Iteration is completed now")

# The output of this written below code will be 0 to (n-1)=9 and then the else block printed : Iteration is completed now

i = 0
while (i < 5):
    print(i)
    i += 1
    if (i == 3):
        break  # If the condition is like this then the code will stop executing here and never goes in the else block of code
else:
    print("Iteration is completed now for while loop")

# The output will be same here as above first printing i and then the else block of code

# So if the code comes in the else block it simply means that the code is completed not break in between
# Means the else block will only execute when the loop completed successfully
