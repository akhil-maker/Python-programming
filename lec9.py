# Various Datatypes in Python
'''
* Mutable data types in Python - their values can be modified after creation, slow in speed, readable, writable
-> List
-> Sets
-> Dictionary
* Immutable Data types in Python - their values cannot be modified after creation, fast in speed, only readable
-> Numbers - storing numeric values but same kind of data
-> Strings - store characters but same kind of data
-> Tuples

| String     | List     | Tuple    |
|============|==========|==========|
| Immutable  | Value 1  | Value 2  |
|------------|----------|----------|
| Ordered/Indexed       | Value 3  | Value 4  |
|Empty String

Header 1              Header 2            Header 3            Header 4            Header 5
=========             =========           =========           =========           =========
Immutable             Mutable             Immutable           Mutable             Mutable
---------             ---------           ---------           ---------           ---------
Ordered/Indexed       Ordered/Indexed     Ordered/Indexed     Unordered           Unordered
---------             ---------           ---------           ---------           ---------
Allows Duplicate      Allows Duplicate    Allows Duplicate    Doesn't allow       Doesn't allow
Members               Members             Members             Duplicate Members   Duplicate Members
---------             ---------           ---------           ---------           ---------
Empty String          Empty list=[]       Emply tuple=()      Empty Set=set()     Empty dictionary={}
String with single    List with single    Tuple with single   Set with single     Dictionary with single
element="H"           item=["Hello"]      item=("Hello")      item={"Hello"}      item={"Hello":1}
---------             ---------           ---------           ---------           ---------
It can store data     It can store any    It can store any    It can store data   Inside of dictionary key
type string only      data type str,      data type str,      types (int, str,    can be int, str and tuple
                      list, set, tuple    list, set, tuple,   tuple) but not      only values can be of any      
                      int and dictionary  int and dictionary  (list, set,         data type int, str, list,
                                                               dictionary)        tuple, set and dictionary

'''

