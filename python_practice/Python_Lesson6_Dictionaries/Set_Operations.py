## union() 
a = {1,2,3,4,5,6}
b = {1,2,3,7,8,9,10}
print(a.union(b))
## another syntax for union is:
print(a | b)

## intersection of sets is what they have in common
a = {1,2,3,4,5,6}
b = {1,2,3,7,8,9,10}
print(a.intersection(b))
## other syntax example:
print(a & b)

## difference, self explanatory
a = {1,2,3,4,5,6}
b = {1,2,3,7,8,9,10}
print(a.difference(b))
print(b.difference(a))
## symmetric difference gives everything rather than the difference
print(a.symmetric_difference(b))

## you can update sets with values from results of set operations
a = {1,2,3}
b = {3,4,5}
a.difference_update(b)
print(a)
## print() the updated set, not the set operation_update
a = {1,2,3}
b = {3,4,5}
a.intersection_update(b)
print(a)

## Knowledge check
first = {1,2,3,4,5,6}
second = {1,2,3,7,8,9,10}
print(first | second)
print(first.intersection(second))
print(first.difference(second))

## frozenset() method, support all set operations but are immutable(not changeable)
a = frozenset([1,2,3])

## Activity 27: Creating Unions of Elements in a Collection

def find_union(x,y):
    union = []
    for items in x + y:
        if items not in union:
            union.append(items)
    return union
print(find_union([1, 2, 3, 4], [3, 4, 5, 6]))
