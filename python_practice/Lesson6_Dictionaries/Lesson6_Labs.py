## Simply iterate through the string and form a key in dictionary of newly occurred element or if element is already occurred, increase its value by 1.


## Define function 'data' that takes 'sentence' as arg
def data(sentence):
## initialize an empty set to place output in    
    solution = {}
## create a for loop to iterate over arg    
    for letters in sentence:
## add if statement to ignore spaces in arg        
        if letters != ' ':
## second if statement to catch the letters in arg
            if letters in solution:
## form key in dictionary and add 1 per repeating letter               
                solution[letters] += 1
## otherwise value of letter will be just 1           
            else:
                solution[letters] = 1
    return solution
print(data('all'))



## Doing the same thing but with .get()
test_str = "GeeksforGeeks"
## using dict.get() to count # of each element in string
result = {}
for keys in test_str:
    result[keys] = result.get(keys, 0) + 1
print('Count of all characters in GeeksforGeeks is : \n' +str(result))


## Write the Python code to create a function called dictionary_value that will take two dictionaries and return a single dictionary with non-duplicated keys.
## Initialize dictionaries
dict1 = {'name': 'John'}
dict2 = {'gender': 'Male'}

def dictionary_values(dict1, dict2):
    for key, value in dict2.items():
        if key not in dict1:
## then make the dict1 key a value in the dictionary to combine the two dictionaries
            dict1[key] = value
    return dict1
print(dictionary_values(dict1,dict2))

## This can all be done much easier
dict3 = dict1 | dict2
print(dict3)

##Write the Python code to implement an algorithm by performing the following tasks:
##Define a function named find_intersection() that include list_a = [1, 2, 3, 4] and list_b = [3, 4, 5, 6].
##Iterate through the two lists, which takes two lists and returns a set of elements that are common to all sets.

list_a = [1,2,3,4]
list_b = [3,4,5,6]

def find_intersection(list_a, list_b):
    list_c = [value for value in list_a if value in list_b]
    return list_c
print(find_intersection(list_a, list_b))


