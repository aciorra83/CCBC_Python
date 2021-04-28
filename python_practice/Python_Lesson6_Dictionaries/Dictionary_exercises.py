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
