# This program is to generate an output of string manipulation using different string methods
# Written by: Shravya Reddy Akmy
# Date: 09/09/2021

#Assigning a string to variable "my_string"
my_string = " My name is Shravya and I'm a grad student at UD "
print("String variable 'my_string':",my_string)

#String Method: Uppercase
#Generates an output of "my_string" in uppercase.
print("\nString in uppercase:",my_string.upper())

#String Method: Lowercase
#Generates an output of "my_string" in lowercase.
print("\nString in lowercase:",my_string.lower())

#String Method: Swapcase
#Generates an output of "my_string" by interchanging lowercase to uppercase and vice-versa.
print("\nString interchange of lowercase/uppercase:",my_string.swapcase())

#String Method: Strip
#Generates an output of "my_string" by removing whitespaces at the beginning and at the end of string. 
print("\nString without whitespaces at start and end:",my_string.strip())

#String Method: Replace
#Generates an output of "my_string" by replacing requested sub-string "Shravya" to "Shravya Reddy Akmy".
print("\nString Replace of Shravya:",my_string.replace('Shravya','Shravya Reddy Akmy'))

#String Method: Substring 
#Generates an output sub-string of "my_string" in given index range.
print("\nSub-string generation in range[0:19]:",my_string[0:19])

#String Method: Concatenation
#Generates an output of a string by addition of two or more strings.
print("\nString Concatenation:",my_string[0:19]+ ' and i like food')

#String Method: Isalpha check
#Generates a boolean value output of "my_string".True if all the characters are alphabets else False.
print("\nString check for all alphabets:",my_string.isalpha())

#String Method: Split
#Generates an output list of "my_string" with all it's sub-strings. 
print("\nList of sub-strings in 'my_string':",my_string.split())

#String Method: Length
#Generates an integer output of length of "my_string"
print("\nLength of 'my_string':",len(my_string))

#String Method: Count
#Generates an output count of occurance of requested character  "a" in "my_string".
print("\nCount of occurance of 'a' in 'my_string':",my_string.count('a'))

#String Method: Find
#Generates an index output of string "shravya" first occurance in "my_string".
print("\nIndex of first occurance of 'Shravya' in 'my_string':",my_string.find('Shravya'))

