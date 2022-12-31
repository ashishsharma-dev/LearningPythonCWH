# It is Day 29 of 100DaysOfCode with CodeWithHarry
# DocStrings in Python

def makeSquare(n):
    '''Takes a number as n and prints the square of n'''
    # But it will only work if mentioned just below the function or just above the function body
    print(n**2)


print(makeSquare.__doc__)
# The output of this line will be docstring written in between ''' '''
makeSquare(6)

# PEP 8 & The Zen of Python

# After importing this by [import this] will print a poem in python like below

# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
