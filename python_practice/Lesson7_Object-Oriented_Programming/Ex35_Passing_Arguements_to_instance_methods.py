class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'Hello! My name is {self.name}. I am {self.age} years old.')

    def greet(self, person):
        print(f'Hi {person.name}')

    def greet(self, person):
        if person.name == "Rogers":
            print('Hey Neighbor!')
        else: 
            print(f'Hi, {person.name}')

joe = Person("Joeseph", 31)
gabby = Person("Gabriela", 25)
rogers = Person("Rogers", 45)

print(joe.greet(gabby))
print(joe.greet(rogers))

