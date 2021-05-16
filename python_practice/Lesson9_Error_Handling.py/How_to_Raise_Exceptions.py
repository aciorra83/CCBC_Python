# as a programmer you can raise errors with the 'raise' keyword

def raise_an_error(error):
    raise error

raise_an_error(ValueError)

# import error
import nonexistentmodule

# key error
person = {
    'name': 'Rich Brown',
    'age': 56
}
print(person["gender"]) # a non-existent key in our dictionary

# type error: occurs if you attemot an operation on a value or object of the incorrect type
# example 1: adding a string to an int:
'string' + 10

# type errors happen when passing wrong args as well:
a = 6
for index, value in enumerate(a):
    print(value) # 'int' object is not iterable, resulting in a type error

# attribute error: rasieed when assigning or referencing an attribute fails:
a = [1,2,3]
a.push(4)

# index error: raised when attempting to access an index in a list that doesn't exist
a = [1,2,3]
print(a[5])

# name error: raised when a specified name can't be found locally or globally
print(age)

# filenotfounderror: raised when attempting to read or write and the file is not found:
with open('input.txt', 'r') as myinputfile:
    for line in myinputfile:
        print(line)