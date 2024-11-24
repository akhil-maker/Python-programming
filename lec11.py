# Python String Built-in Functions
'''
Method: len()
Desc: Returns the length of the given string

Method: title()
Desc: Returns the string with first letter of every word in the string in uppercase and rest in lowercase

Method: lower()
Desc: Returns the string with all uppercase letters converted to lowercase

Method: upper()
Desc: Returns the string with all lowercase letters converted to uppercase

Method: count(str, start, end)
Desc: Returns number of times substring str occurs in given string. If we do not give start index and end index then searching starts from index 0 and ends at length of string

Method: find(str, start, end)
Desc: Returns the first occurence of index of substring str occuring in the given string. If we do not give start and end then searching starts from index 0 and ends at length of the string. If the substring is not present in the given string, then the function returns -1

Method: index(str, start, end)
Desc: Same as find() but raises an exception if the substring is not present in the given string
'''

str1 = 'Hello World!'
print(len(str1))

str1 = 'hello WORLD!'
print(str1.title())

str1 = 'hello WORLD!'
print(str1.lower())

str1 = 'hello WORLD!'
print(str1.upper())

str1 = 'Hello World! Hello Hello'
print(str1.count('Hello', 12, 25))
print(str1.count('Hello'))

str1 = 'Hello World! Hello Hello'
print(str1.find('Hello', 10, 20))
print(str1.find('Hello'))
print(str1.find('Hee'))

str1 = 'Hello World! Hello Hello'
print(str1.index('Hello'))
#print(str1.index('Hee')) - ValueError: substring not found

