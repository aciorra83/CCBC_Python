#Using list methods
wild = ["Tiger", "Zebra", "Panther", "Antelope"]
print (wild)

wild.append("Cat")
print(wild)

creatures = []
creatures.extend(wild)
print(creatures)

creatures.insert(2, "Dog")
print (creatures)
creatures.pop(1)
creatures.insert(1, "Giraffe")
print(creatures)

creatures.sort(key=None, reverse=False)
print(creatures)


#Using Tuple methods
fruits = ('apple', 'apple', 'apple', 'mango', 'orange')
#Count the number of times the apple element appears in the fruits tuple and assign it to a variable c
c = fruits.count('apple')
#Calculate the length of the fruits tuple and assign it to a variable d
d = len(fruits)
#Print the message There are too many apples here. to the terminal, if the number of times the apple element appears in the fruits tuple is more than 50%. If this occurrence is less than 50%, then print the message Everything is good. to the terminal
if (c/d)*100 > 50.0:
    print('There are too many apples here')
else:
    print('Everything is good')
