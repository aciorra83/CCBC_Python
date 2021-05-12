import calculator 
print(calculator.add(8,9))

# other syntax that does the same thing, but imports everything in the module would be:
from calculator import *
print(add(8,9))

# this is NOT good practice however, only import what you intend to use:
from calculator import add
print(add(8,9))

# example of importing with 'as' keyword:
from calculator import add as a 
print(a(8,9))

import calculator as calc
print(calc.add(8,9))

# they all give the same result in this case
