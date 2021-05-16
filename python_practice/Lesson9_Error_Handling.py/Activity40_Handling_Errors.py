import random
try:
    print(random.randinteger(1,10))
except AttributeError:
    print('Oops! Something went wrong.')
