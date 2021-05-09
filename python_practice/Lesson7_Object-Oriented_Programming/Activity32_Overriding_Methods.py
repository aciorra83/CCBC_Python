# Define the cat class
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
# Defin the tiger class
class Tiger(Cat):
    def __init__(self, mass, lifespan, speed):
        super().__init__(mass, lifespan, speed)
# Add a coat_pattern attribute
        self.coat_pattern = "striped"
# Override the __str__() method and add the coat_pattern attribute
    def __str__(self):
        facts = super().__str__()
        facts = f"{facts} It also has a {self.coat_pattern} coat."
        return facts

tiger = Tiger(310, 26, 65)
print(tiger)

