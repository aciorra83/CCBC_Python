class Person:
    pass
# Pass is a placeholder keyword
print(type(Person))
# This yields the output <class 'type'> and the two are synonymous

# Ex 32: Instantiating a Person object
jack = Person()
jill = Person()
print(jack is jill) # this comparison yields 'False'
jack2 = jack
print(jack2 is jack) # this comparison yields 'True'
# Assigning another variable to jack simply points it to whatever object jack is pointing to, and so they are the same object and identical.

# Adding attributes to an object, NOT   the preferred method
# person1 = Person()
# Person1.name = 'Gol D. Roger'

# Every class comes with built in attributes, like _dict_ (a dictionary)
person1 = Person()
person1.__dict__
person1.name = 'Gol D. Roger'
person1.age = 53
person1.height_in_cm = 180
person1.__dict__
print(person1.name, person1.age, person1.height_in_cm)

# The appropriate method for adding attributes to an object is through the constructor method, for python that is _init_()
# The hasattr() function checks whether an object has a specific attribute or method. __init__ is inheritted so this will return 'True'
print(hasattr(Person, '__init__'))

# # Defining the constructor method like a function, specifies attributes that will need passed when instantiating an obj
# class Person:
#     def __init__(self, name):
#         self.name = name
# # 'self' keyword refers to the object we're currently in the process of creating

# # Adding attributes to a class the right way:
# person1 = Person('Bon Clay')
# # if you don't pass in the name to Person() you will get a __init__ error
# print(person1.name)

class Person:
    def __init__(self, name, age, height_in_cm):
        self.name = name
        self.age = age
        self.height_in_cm = height_in_cm
# now when instantiating a 'Person' object, you need to pass arguements: name, age and height_in_cm
person1 = Person('Cubert', 62, 100)
print(person1.name, person1.age, person1.height_in_cm)