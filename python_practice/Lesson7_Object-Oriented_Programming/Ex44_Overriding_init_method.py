# In this exercise, we'll override the __init__ method and add a spotted_coat attribute:
class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.life_in_years = lifespan
        self. speed_in_kph = speed
        
    def vocalize(self):
        print('Chuff!')
    
    def print_facts(self):
        print(f"The {type(self).__name__.lower()} "
              f"weighs {self.mass_in_kg}kg,"
              f" has a lifespan of {self.life_in_years} years and "
              f"can run at a maximum speed of {self.speed_in_kph}kph.")

class Cheetah(Cat):
    def __init__(self, mass, lifespan, speed):
        # Super class initializer
        super().__init__(mass, lifespan, speed)
        self.spotted_coat = True

    def vocalize(self):
        print("Chirrup!")

# When we instantiate a Cheetah instance, we see that our Cat superclass implementation is preserved:
cheetah = Cheetah(72,12,120)
print(cheetah.print_facts())

# our new attribute spotted is also added
print(cheetah.spotted_coat)

# On Commonly overridden methods
