class Dog:
# initializing the arguements or attributes of an object for this class
    def __init__(self, breed, age, name):
        self.breed = breed
        self.age = age
        self.name = name

# creating a function within the class
    def myfunc(self):
        print(self.breed, self.name, self.age)

# creating a child class that inherits all attributes of parent class
class sm_dog(Dog):
    pass


# creating an object "pup"
pup = Dog("Rat Terrier", 3, "Tyson")
print(pup.breed, pup.age, pup.name)
# myfunc needs to be defined with pup since it has local scope within the class only
pup.myfunc()

# defining a small dog object and calling myfunc with said object
terrior = sm_dog("Weiner Dog", 10, "Buddy")
terrior.myfunc()

