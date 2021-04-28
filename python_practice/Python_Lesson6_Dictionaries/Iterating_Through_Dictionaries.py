dictionary1 = dict(
    state = 'NY',
    city = 'New York'
)

for item in dictionary1:
    print(item)

##You can use the key() or value() method to return a list of values in the dictionary
for item in dictionary1.values():
    print(item)

##you can also use both in the same for loop
for key, value in dictionary1.items():
    print(key, value)

##Checking existence of particular keys with the "in" keyword (returns a boolean value)
a = {
    'size': '10 feet',
    'weight': '16 pounds'
}
print('size' in a)
print('length' in a)

cars = dict(
    brand = 'Ford',
)
print(cars)
cars['model'] = 'Mustang'
print(cars)