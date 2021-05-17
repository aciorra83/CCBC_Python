import json

# creating a json string
y = '{"sports player": "Jones", "age": 44, "birthplace": "Willemstad, Curacao"}'

z = json.loads(y)

print(z['birthplace'])