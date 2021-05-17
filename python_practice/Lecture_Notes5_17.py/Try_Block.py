from typing import Generic


try:
    print('Alex Ciorra')
except NameError:
    print('That variable is not defined')
else:
    print('The program is good')
finally:
    print('I will always print')