# Introduction to Strings
'''
a string is a sequence of characters
strings are immutable and ordered
'''

first_string = 'Hello, World!'
print(first_string)
print(len(first_string))
print(first_string[1])
# first_string[1] = 'o' - error
print(first_string[1:4]) #slicing [start, end)

s1 = 'Hello'
s2 = 'World'
s3 = s1 + " " + s2
print(s3)

#Type casting
s1 = 'Hello'
s2 = 20
print(s1 + " " + str(s2))

#Format string
first = 'abc'
last = 'xyz'
age = 33
print(f'my first name is {first} & last name is {last} & age is {age}')
intro = 'my first name is {} & last name is {} & age is {}'.format(first, last, age)
print(intro)

