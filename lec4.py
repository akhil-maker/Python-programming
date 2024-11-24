#Data types in python
'''
1. Numeric type
-> int
-> float
-> complex

2. Text type
-> str

3. Boolean type
-> bool

4. Sequence type
-> list - mutable (can be changed)
-> tuple - immutable (cannot be modified)
-> range

5. Mapping type
-> dict

6. Set type
-> set

7. Binary type
-> bytes
-> bytearray

8. None type
'''

#int
age = 32
#float
weight = 72.50
#string
name = 'xyz'
#bool
is_boy = True
#list
list1 = [100, 200, 300]
#dict
dict1 = {'name': 'abc', 'age': age, 'city': 'city1'}
print(type(age), type(weight), type(name), type(is_boy), type(list1), type(dict1))
print(dict1['city']) #key-value pair

#tuple
tup = (10, 20, 30)
#set
set1 = {1, 2, 3, 3, 3, 4}
#None
house_no = None
#Complex
com = 1+2j
#range
num = range(1, 5)
#bytes & bytearray
byte = bytes([65, 66, 97])
byte1 = bytearray([65, 66, 67])
print(type(tup), type(set1), type(house_no), type(com), type(num), type(byte), type(byte1))
print(byte)
print(byte1)
print(num)
