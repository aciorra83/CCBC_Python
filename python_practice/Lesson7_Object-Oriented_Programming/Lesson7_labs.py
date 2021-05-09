# Write the Python code to create a class named Circle, which is constructed by a radius having value 5 and two other methods.
# Which will calculate the circumference and area of a circle.
import math
class Circle:
# This instantiates the 'Circle' class and declares that a radius arg needs to be passed
    def __init__(self, radius):
        self.radius = radius
# Create a function that will print the radius of the circle we place into class
    def area(self):
        print(math.pi * self.radius ** 2)
# Repeat to create cicumference function
    def circumference(self):
        print(2 * math.pi * self.radius)
# adding 'circle' to Circle class and passing 5 as the argument for radius
circle = Circle(5)
print('Area:')
print(circle.area())
print('and circumference:')
print(circle.circumference())


# Write the Python code that defines a class called Vehicle, which will have a maximum occupancy of 8. 
# The vehicle should be initialized with the number of occupants. If the number of occupants exceeds the limit during initialization, 
# it should print a message indicating that the limit has been exceeded and only initialize how many occupants should step off the vehicle. 
# The first vehicle has 6 occupants and the second vehicle has 10 occupants.
class Vehicle:
    def __init__(self, occupants):
        self.occupants = occupants
vehicle1 = Vehicle(6)
vehicle2 = Vehicle(10)
print(f'The first vehicle has {vehicle1.occupants} occupants.')
print('The maximum occupancy limit has been exceeded.', vehicle2.occupants - 8, 'occupants must exit the vehicle.')
print(f'The second vehicle has {vehicle2.occupants} occupants.')


# Creating class methods and using information hiding
# 1. Define the Music class by adding the firmware_version class attribute.
# 2. Define the initializer method and pre-populate the tracklist with the Spirit in the sky, Starman, and Escape songs. 
    # Make sure the music track's store is private.
# 3. Define the play method, which sets the current_track attribute to the first item in the track's list.
# 4. Define the list_tracks method, which returns the list of tracks in the Music class.
# 5. Add the update_firmware method, which checks for whether the new version being provided is more recent than the current firmware version before updating.

class Music:
# step 1, add this class attribute
    firmware_version = 1.0
# Define intializer method and pre-populate tracklist
    def __init__(self):
        self.__tracks = ['Spirit in the sky','Starman', 'Escape']
        self.current_track = None
    # define play method and get 1st value from __tracks
    def play(self):
        self.current_track = self.__tracks[0]
    def list_tracks(self):
        return self.__tracks
    # this function will check the firmware and determines if update is needed
    @classmethod
    def update_firmware(cls, new_version):
        if new_version > cls.firmware_version:
            cls.firmware_version = new_version
player = Music()
print("Tracks currently on device:", player.list_tracks())
Music.update_firmware(2.0)
print("Updated player firmware version to", player.firmware_version)
player.play()
print("Currently playing", player.current_track)

# Overriding Methods: Write the Python code to create the Child class that inherits from the Parent class.
class Parent():
    def __init__(self):
        self.value = "Inside the parent class"
    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        self.value = "Inside the child class"
    def show(self):
        print(self.value)
obj1 = Parent()
obj2 = Child()
print(obj1.show())
print(obj2.show())

# Practicing Multiple Inheritance
# Write the Python code to create a class by performing the following tasks:
# Create the MobilePhone class that will be initialized with the memory attribute.
# Create the Call class that has the talk() method and print Say Hello!.
# Create the Phone class that inherits from both the MobilePhone and Call classes.
# Initialize an instance of the Phone class and print 200KB. Calling the talk() method on the instance.
# Print the memory attribute.
class MobilePhone:
    def __init__(self, memory):
        self.memory = memory

class Call:
    def talk(self):
        print('Say Hello!')

class Phone(MobilePhone, Call):
    pass

phone = Phone('200KB')
phone.talk()
print(phone.memory)
