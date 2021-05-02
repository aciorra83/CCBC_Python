from collections import OrderedDict
a = OrderedDict(name = 'Zeus', role = 'god')
print(a)

## Activity 25 Combining Dictionaries
a = {'name': 'Amos'}
b = {'age': 100}
def dictionary_masher(a, b):
    for key, value in b.items():
        if key not in a:
            a[key] = value
    return a
print(dictionary_masher(a,b))

## This is a much easier way to merge dictionaries in Python 3.9+
c = a | b
print(c)