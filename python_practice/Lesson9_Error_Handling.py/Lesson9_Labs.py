# Correct the Python code to resolve the KeyError and AttributeError error scenarios:
# KeyError: Check the print statement that uses a key that's not defined in the dictionary.
# AttributeError: Check the attribute defined in the string module.


building = dict(
    name="ABC Company",
    type="Company Premises"
)

print (building['name'])

import string 
letters = string.ascii_uppercase
print(letters)


# Complete the Python code to make sure that the error doesn't stop a user's program prematurely. 
# Handle the error so that when it occurs, the message Something went wrong is printed to the terminal.
import random
try:
    print(random.randinteger(1,10))
except AttributeError:
    print('Something went wrong')


# Write the Python code that will capture and handle the custom exceptions. Here are the steps to follow:
# Subclass the Exception class and create a new Exception class named as Error that contains a message as An exception occurred.
# Use the try…except block that will handle the exception and print the message.
class Error(Exception):
    def __init__(self):
        self.message = 'An exception occurred'
try:
    raise Error
except Error as e:
    print(e.message)