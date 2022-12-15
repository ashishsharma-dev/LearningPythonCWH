# It is Day 15 of 100DaysOfPython with CodeWithHarry

import time

hours = time.localtime().tm_hour
minutes = time.localtime().tm_min

if (hours >= 5 and (hours <= 11 and minutes <= 59)):
    print("Good Morning Sir")
elif (hours >= 12 and (hours <= 18 and minutes <= 59)):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")
