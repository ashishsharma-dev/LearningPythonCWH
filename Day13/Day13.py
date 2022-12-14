# Day 13 : More String Metods in Python

# String are immutable in Python
str = "Ashish"
print(len(str))

print(str.upper())  # Here we are creating another copy of str
print(str.lower())  # Here we are creating another copy of str
print(str)  # str's value is still the same : output => Ashish


str1 = "Sharma......."
print(str1.rstrip("."))  # This will remove all the "." from the string

str2 = "!!Ashish!!"
# But this will not remove starting chars like exclmation in the starting from the string
print(str2.rstrip("!"))

str3 = "Ashish Sharma is a web developer"
# This will replace all the occurances of the string in the string
print(str3.replace("a", "@"))

str4 = "Ashish"
print(str4.split("i"))  # This will convert the string in to a list

str5 = "introduction to python language"
# This will make the first letter of the sentence capital
print(str5.capitalize())

# This return a boolean either True or False
str6 = "Ashish Sharma is a web developer!"
ans = str6.endswith("!")
print(ans)

# Two other params of this function is start and end position
# Like this

str7 = "Ashish Sharma"
print(str7.endswith('arma', 0, len(str7)))

str7 = "Ashish Sharma"
# This will return the first occurence of the given string
print(str7.find("ish"))

str8 = "Ashish Sharma"
print(str8.index("sh"))  # This will return the index of the given value same as the find() but if the value is not available in the string, it will throw an error / an exception

str9 = "ashish0562"
# This will return True or False depending on the given string is alpha-numeric or not
print(str9.isalnum())

# This will return False in case of any numeric digit found in the string or True in case of not found
str10 = "Ashish0562"
print(str10.isalpha())

str11 = "Ashish Sharma"
# This will return True or False if the string contains any lower character
print(str11.islower())

# This will return True or False if the string contains any non printable chars like \n
str12 = "Ashish Sharma"
print(str12.isprintable())

str13 = " "  # This will return True or False if the string contains whitespaces
print(str13.isspace())

str14 = "This is a title" # This will return True or False depending on the words starting with lowercase or uppercase letter in a string
print(str14.istitle())

str15 = "This is Python" # This will return True or False depending on the input available in the string or not
print(str15.startswith("This"))

str16 = "Python is a interpreted language" # As per the name suggests this will return the string with character swapped like uppercase will swapped with the lowecase and vice versa
print(str16.swapcase())

str17 = "My Name is Ashish Sharma. I am a Web Developer" # This will return the same string with all the first char of the string is converted to uppercase
print(str17.title())
