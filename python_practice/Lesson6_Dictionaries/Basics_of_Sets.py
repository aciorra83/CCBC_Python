a = set([1, 2, 3])
print(a)
## duplicate values in sets do not appear in output
b = set([1, 2, 2, 3, 4, 5])
print(b)

## another notation is with {}
c = {'a', 'b', 'c'}
print(c)

## Adding data to sets with .add()
a.add(4)
print(a)
## update() allows you to add iterables to a set
a.update([3,4,5,6])
print(a)

## iterate through a set with a for loop
a = {1,2,3,4}
for num in a:
    print(num)
## pop() with sets remove items at the beginning of a set

## Activity 26: Building a set
def set_maker(the_list):
    return set (the_list)
print(set_maker([1,1,2,2,2,3,4,5,6,6]))
## the "return set" is what eliminates the duplicate numbers in the list

## remove() does, you guessed it. Removes items from a set and does not return the value (you get an error if you try to remove a value that doesn't exist)
a.remove(3)
print(a)

## discard () does not return an error if the item does not exist
a = {1,2,3}
a.discard(4)
print(a)

## clear() removes all the data
a = {1,2,3,4,5,6,7}
a.clear()
print(a)

