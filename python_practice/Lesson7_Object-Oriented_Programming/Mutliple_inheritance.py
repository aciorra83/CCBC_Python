# Exercise 45: Implementing Multiple Inheritance
# Define the Lion and Tiger classes. For simplicity, we'll hardcode the mass, lifespan, and speed attributes. They'll both inherit from the Cat class:
class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print('Chuff!')
    
    def __str__(self):
        return f'The {type(self).__name__.lower()} '\
            f'weighs {self.mass_in_kg}kg,'\
            f' has a lifespan of {self.lifespan_in_years} years and '\
            f'can run at a maximum speed of {self.speed_in_kph}kph.'
    
class Lion(Cat):
    def __init__(self, mass = 190, lifespan = 14, speed = 80):
            super().__init__(mass, lifespan, speed)
            self.is_social = True

    def vocalize(self):
            print('ROAR!')

class Tiger(Cat):
    def __init__(self, mass = 310, lifespan = 26, speed = 65):
        super().__init__(mass, lifespan, speed)
        self.coat_pattern = 'striped'
    def swim(self):
        print('splash splash')
    def vocalize(self):
        print('ROAR!')

# Then, define the Liger class, which will inherit from both the Tiger and Lion classes:
class Liger(Lion, Tiger):
    pass

# On testing it out, we should see that the Liger class has inherited attributes from both the Lion and Tiger classes. 
# The Liger class has both the coat_pattern attribute and swim() method of the Tiger class and the is_social attribute of the Lion class:
liger = Liger()
print(liger.swim())
print(liger.is_social)
print(liger.coat_pattern)