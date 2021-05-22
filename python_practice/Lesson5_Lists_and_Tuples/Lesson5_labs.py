#Using list methods
# Complete the Python code that will perform the following things using list methods:

wild = ["Tiger", "Zebra", "Panther", "Antelope"]
print (wild)

#   Add the value cat to the list named wild using the built-in append() method.
wild.append("Cat")
print(wild)

#   Create an empty list named creatures and extend the list from the wild list using the built-in extend() method.
creatures = []
creatures.extend(wild)
print(creatures)

#   Insert the word Dog into the creatures list,
#  at index 2 and replace the element at index 1 with word Giraffe using the built-in methods, namely, insert() and pop().
creatures.insert(2, "Dog")
print (creatures)
creatures.pop(1)
creatures.insert(1, "Giraffe")
print(creatures)

#   Sort the elements in the creatures list by using the built-in sort() method.
creatures.sort(key=None, reverse=False)
print(creatures)


#Using Tuple methods
# Complete the Python code to perform the following tasks using tuple methods:
fruits = ('apple', 'apple', 'apple', 'mango', 'orange')
#Count the number of times the apple element appears in the fruits tuple and assign it to a variable c
c = fruits.count('apple')
#Calculate the length of the fruits tuple and assign it to a variable d
d = len(fruits)
#Print the message There are too many apples here. to the terminal, if the number of times the apple element appears in the fruits tuple 
#is more than 50%. If this occurrence is less than 50%, then print the message Everything is good. to the terminal
if (c/d)*100 > 50.0:
    print('There are too many apples here')
else:
    print('Everything is good')
