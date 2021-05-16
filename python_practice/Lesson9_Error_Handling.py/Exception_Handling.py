from typing import Generic


animals = ['man', 'bear', 'pig']
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No cats found.'
print(cat_index)

# Ex 49: Implementing the try...except block
# with open('input.txt', 'r') as myinputfile:
#     for line in myinputfile:
#         print(line)

# print('Execution never gets here')

# re-writen with try except block:
try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print('Whoops! File does not exist.')

print('Execution will continue to here.')

# another way to write this block is by creating a tuple to handle more than one error type
# try:
#     with open('input.txt', 'r') as myinputfile:
#         for line in myinputfile:
#             print(line)
# except (FileNotFoundError, ValueError):
#     print('Whoops! File does not exist.')
# print('Execution will continue to here.')

# the best way to handle them is individually like so:
try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print('Whoops! File does not exist.')
except ValueError:
    print('A value error occurred.')

# If you are not quite sure which exception will be thrown, you can catch the generic Exception, which will catch any exception that's thrown. 
# It is a good practice to catch the generic Exception at the end of more specific except clauses and not by itself. Implement it like this:
try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print('Whoops! File does not exist')
except ValueError:
    print('A value error occurred.')
# Generic exception clause here
except Exception:
    print('Something unforseen happened.')

print('Execution will continue to here.')

