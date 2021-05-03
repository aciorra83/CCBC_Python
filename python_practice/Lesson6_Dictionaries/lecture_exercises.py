cars = {
    'Make':'Ford',
    'Model':'Focus',
    'Electric': False,
    'Colors': ['Blue', 'Gray', 'Red', 'Purple'],
    'Year':2020,
}
# y = cars.get('Year')
# print(type(cars))
# print(y)

# .get() keys method returns all the keys in a dict
x = cars.keys()
print(x)

# adding a key and value pair
cars['Price'] = 22000
print(cars)

# how to check for a key in a dict
if 'Model' in cars:
    print('Yes, "Model" is one of the keys')

# updating information in a dict
cars.update({'Make':'Kia'})
print(cars)

# removing items from a dict
cars.pop('Make')
print(cars)
# removes the last added item (in this case it was price)
cars.popitem()
print(cars)
# delete specific items
del cars['Colors']
print(cars)
# clean dict out
# cars.clear()
# print(cars)

# looping through dictionaries
for c in cars:
    print(cars[c])

# nested dictionaries
cars2 = [
{'Make': 'Kia',
'Model': 'Soul',
'Year': 2022
},

{'Make': 'Ford',
'Model': 'Focus',
'Year': 2021
},

{'Make': 'Chevy',
'Model': 'Equinox',
'Year': 2020
}
]
print(cars2)

# sets are used store multiple elements in a single variable cannot repeat items
cars3 = set(('Ford', 'Kia', 'Chevy'))
print(cars3)
