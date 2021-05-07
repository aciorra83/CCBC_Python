class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def print_facts(self):
        print(f"The {type(self).__name__.lower()} "
              f"weighs {self.mass_in_kg}kg,"
              f" has a lifespan of {self.lifespan_in_years} years and "
              f"can run at a maximum speed of {self.speed_in_kph}kph.")


class Cheetah(Cat):
    def vocalize(self):
        print("Chirrup")

class Lion(Cat):
    def vocalize(self):
        print("ROAR")

class Leopard(Cat):
    def vocalize(self):
        print("Roar")

cheetah = Cheetah(72, 12, 120)
lion = Lion(190, 14, 80)
leopard = Leopard(90, 17, 58)

print(lion.vocalize())
print(cheetah.vocalize())
print(leopard.vocalize())

