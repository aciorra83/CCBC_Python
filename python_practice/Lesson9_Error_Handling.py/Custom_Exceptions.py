class RecipeNotValidError(Exception):
    def __init__(self):
        self.message = 'Your recipe is not valid'

try:
    raise RecipeNotValidError
except RecipeNotValidError as e:
    print(e.message)


#Activity 41: Creating your own custom exception class:
# Subclass the Exception class and create a new Exception class of your choosing.
# Write some code where you use the try…except flow to capture and handle your custom exception.

class WrongCaliberError(Exception):
    def __init__(self):
        self.message = 'You have the wrong caliber for this weapon'
try:
    raise WrongCaliberError
except WrongCaliberError as a:
    print(a.message)