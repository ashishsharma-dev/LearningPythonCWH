# This is Day 16 of 100DaysOfCode with CodeWithHarry

a = int(input("Enter the number here: "))

# Match Cases are simple like the switch statements of other programming languages like C/C++/Java/JavaScript etc.
# But without the break statement! You do not need do type the break statement to break below statements
# Bcoz in python if any case matches with the condition the program will automatically completed

match a:
    case 0:
        print("A is Zero")
    case 44:
        print("A is 44")
    case _:
        print(a)
