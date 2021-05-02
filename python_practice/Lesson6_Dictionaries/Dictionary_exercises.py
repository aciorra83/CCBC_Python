##Don't forget to add commas after every item in a dictionary
dictionary1 = dict(
    state="NY",
    city="New York")
print(dictionary1)

dictionary2 = {
    'state': 'Maryland',
    'city': 'Baltimore'
}
##Syntax to add an item to a dictionary, if you use the same key it replaces the old value
dictionary2['bird'] = 'Baltimore Oriole'
print(dictionary2)

##Syntax to access items within dictionaries
print(dictionary1['state'])

##To avoid possible syntax error, use the get() function
print(dictionary1.get('state'))
print(dictionary1.get('age'))
print(dictionary1.get('age', 'Key age is not defined'))


##update() method is used to insert new key-value pairs or update an existing one
a = {}
a.update({'name': 'Dan Brown'})
print(a)

##dict.clear() and dict.pop() are methods to remove all keys from a ditionary
a.clear()
print(a)

## del keyword removes one key-value pair
a = {'name' : 'Skangar Keynes', 'age': '24'}
print(a)
del a['name']
print(a)

## dict.copy() creates a shallow copy
b = a.copy()
print(b)
a['name'] = 'Janet Jackson'
print(a)
## In this example, you can see that b is a shallow copy of a, and has all of the exact key-value pairs found in a. However, updating a will not update b. 
## using the = operator will make a deep copy, a and b would refer to the same object
b = a
print(b)

## popitem() method pops and returns a random item from the dictionary, the item will cease to exist afterwards
a.popitem()
print(b)

## setdefault() method takes 2 arguments: a key and value to be searched. If key existed, value is returned, if not it is inserted with value provided in argument
b = a.setdefault('name', 'Michael Jackson')
print(b)

## dictfromkeys() method is used to creat an dictionary from an iterable of keys, with user provided value. If no value is provided, it's set to None
c = dict.fromkeys(['name', 'age'], 'Nothing here yet')
print(c)

