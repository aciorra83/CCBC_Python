# Exercise 43: Implementing Class Inheritance

#In this exercise, we'll define the Cat class from which we'll derive our other big cats. 
# The class will have the methods vocalize and print_facts, and the attributes mass, lifespan, and speed.
# The constructor method will take the arguments mass, lifespan, and speed from which it will add the attributes mass_in_kg, 
# lifespan_in_years, and speed_in_kph to the object.
# The vocalize method will print out Chuff, a non-threatening vocalization that's common to several big cats. 
# The print_facts method will print out facts about the cat:
class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.life_in_years = lifespan
        self.speed_in_kph = speed
    
    def vocalize(self):
        print('Chuff!')
    
    def print_facts(self):
# type(self).__name__ means that we want the name of the current class of the object, in this case, Cat. We then call str.lower() on the name in our example.
        print(f'The {type(self).__name__.lower()} '
        f'weighs {self.mass_in_kg}kg'
        f' has a lifespans of {self.life_in_years} years'
        f' can run at a maximum speed of {self.speed_in_kph}kph.')

cat = Cat(4, 18, 48)
print(cat.vocalize())
print(cat.print_facts())

# Create the subclasses Leopard, Cheetah, and Lion, which will inherit from the Cat class:
class Cheetah(Cat):
    pass

class Lion(Cat):
    pass

class Leopard(Cat):
    pass
# instantiate the new cheetah, lion and leopard classes
cheetah = Cheetah(72, 12, 120)
lion = Lion(190, 14, 80)
leopard = Leopard(90, 17, 58)
print(cheetah.print_facts())
print(lion.print_facts())
print(leopard.print_facts())

# Overriding the vocalize method for subclasses
class Cheetah(Cat):
    def vocalize(self):
        print('Chirrup!')

class Lion(Cat):
    def vocalize(self):
        print('ROAR!')

class Leopard(Cat):
    def vocalize(self):
        print('Roar!')
print(cheetah.vocalize())
print(lion.vocalize())
print(leopard.vocalize())

# if we call vocalize instances they all have the same output and that's not accurate
print(cheetah.vocalize())
print(lion.vocalize())
print(leopard.vocalize())


