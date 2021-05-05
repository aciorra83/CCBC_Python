class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hello! My name is {self.name}. I am {self.age} years old.')
 # creating a method, birthday() that increments age by 1
    def birthday(self):
        self.age += 1

diana = Person('Diana', 28)
print(diana.age)
#calling the birthday() method and re-printing the age
diana.birthday()
print(diana.age)

# Knowledge check: Complete Python code to add your methods to classes. 
# In this, you can take the user's input, such as name and branch, and then prints them as per the given output.
name= input()
branch= input()
class Knowledge_check:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
# Creating talk() method to print desired output
    def talk(self):
        print(f'Hello! My name is {self.name}. I am in {self.branch} branch.')
xyz = Knowledge_check(name, branch)
xyz.talk()