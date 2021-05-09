# The __str()__ method
# Let's replace the print_facts() method of the Cat class with this method:
class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."

class Cheetah(Cat):
    def __init__(self, mass, lifespan, speed):
        # Super class initializer
        super().__init__(mass, lifespan, speed)
        self.spotted_coat = True

cheetah = Cheetah(72, 12, 120)
print(cheetah)
# Now, when we call print() on any Cat instance or Cat subclass instance, it should have the same result as when we were calling print_facts():
# The __del()__ method does exactly what you think

class Cheetah(Cat):
    def __init__(self, mass, lifespan, speed):
        super().__init__(mass, lifespan, speed)
        self.spotted_coat = True

    def vocalize(self):
        print('Chirrup!')
    
    def __del__(self):
        print('No animals were harmed in the deletion of this instance')
cheetah = Cheetah(72, 12, 120)
del cheetah
print(cheetah)