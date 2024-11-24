# Operators and associativity in Python
'''
() - Parentheses
** - Exponent - R to L - 2**3**2 = 64 or 512 - 512 is correct
+x, -x, ~x - Unary pls, Unary minus, bitwise NOT
*, /, //, % - Multiplication, Division, Floor division, Modulus
+, - - Addition, Subtraction
<<, >> - Bitwise Shift operators
& - Bitwise AND
^ - Bitwise XOR
| - Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in - Comparisons, Identity, Membership operators
not - Logical NOT
and - Logical AND
or - Logical OR
=, +=, -=, *=, /= - Assignment operator - R to L - a=3+=4 => a = 7

These operators are used to perform basic arithmetic operations such as addition, subtraction, multiplication, division, modulus and exponentiation. These operators are:
+ Addition
- Subtraction
* Multiplication
/ Division, // Floor division
% Modulus
** Exponentiation

Logical Operator

-> In python, logical operators are used to combine multiple conditions or expressions and produce a Boolean result.
-> There are three logical operators in python
-> and: It returns True if both the operands are True, otherwise it returns False
-> or: It returns True if at least one of the operands is True, otherwise it returns False
-> not: It returns the opposite Boolean value of the operand. If the operand is True, it returns False, and if the operand is False, it returns True

Not > and > or

Comparison Operators

-> In Python, comparison operators are used to compare two values and return a Booloean value (True or False) depending on the result of the comparison.
== Equal to: Returns True if the values on either side of the operator are equal and False otherwise
!= Not equal to: Returns True if the values on either side of the operator are not equal and False otherwise
> Greater than: Returns True if value on the left is greater than the value on the right, and False otherwise
< Less than: Returns True if the value on the left is less than the value on the right and False otherwise
>= Greater than or equal to: Returns True if value on the left is greateer than or equal to the value on the right and False otherwise
<= Less than or equal to: Returns True if the value on the left is less than or equal to the value on the right and False otherwise

Bitwise Operator

-> In python, bitwise operators are used to perform operations on individual bits of binary numbers
-> There are six bitwise operators
& (Bitwise AND)
| (Bitwise OR)
~ (Bitwise NOT)
^ (Bitwise XOR)
<< (Bitwise Left Shift)
>> (Bitwise Right Shift)
Precedence: ~(Highest), <<>>, &, ^, |(Lowest)

Identity Operator
-> These operators used to check whether two objects are of same type or not & they share memory location or not
-> There are 2 identity operators: 'is' & 'is not'
-> Always return "True or False" as a output

Membership Operator
-> These operators used to test whether a specific value or item is present within a sequence such as a string, list, tuple, or set
-> There are 2 membership operators: 'in' & 'not in'
-> Always return "True or False" as a output
'''

age = 25
income = 20000
if age >= 18 or income >= 15000:
    print("Eligible for the loan")
else:
    print("Not eligible")

a = True
b = False
if not a:
    print("my name is a") #This will not be executed
if not b: 
    print("my name is b") # gives output

#Bitwise AND
a = 0b1010
b = 0b1100
c = a&b
print(bin(c))

#Bitwise OR
a = 0b1010
b = 0b1100
c = a|b
print(bin(c))

#Bitwise XOR
a = 0b1010
b = 0b1100
c = a^b
print(bin(c))

#Bitwise NOT
a = 0b1010
c = ~a
print(bin(c))

#Bitwise Left Shift
a = 0b1010
c = a<<2
print(bin(c))

#Bitwise Right Shift
a = 0b1010
c = a>>1
print(bin(c))


x = 10
y = 10 #y is pointing to same memory location as x as having same values
print(x is y)
z = x #z is pointing to same memory location
print(z is x)
print(id(x), id(y), id(z))

str1 = "Hi"
str2 = "Hi"
print(str1 is str2)

list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1 is list2) #here it is false as "is" works only on single value and not on grouped datatype, both gets separate memory location
print(list1==list2) #it checks for values which are equal
print(id(list1), id(list2))

n1 = None
n2 = None
print(n1 is n2) #returns true

list1 = [1, 2, 3, 4, 5]
print(1 in list1)

reg_user = ["abc", "bcd", "cde", "def"]
name = input("Enter your name: ")
if name in reg_user:
    print("Access granted, Welcome!")
else:
    print("Access Denied")