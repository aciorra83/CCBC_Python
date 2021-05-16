# JSON = JavaScript Object Notation
# json.dumps() method is used for JSON encoding, ex: converting dictionaries to JSON objects

import json
sample = {
    'name': 'Bert Bertie',
    'age': 24
}

sample_json = json.dumps(sample)
print(sample_json)
print(type(sample_json))
# the output type is a str object

# If you want to decode the JSON object, you can use json.loads() to do so. We are going to add some code in our original code to illustrate this:
original_sample = json.loads(sample_json)
print(original_sample)
print(type(original_sample))
# this reconverts the JSON data we converted from a dict to JSON object back to a dict object

