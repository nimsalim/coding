# Bridging Data: JSON and APIs

{
    "name": "Luna",
    "age": 3,
    "breed": "Labrador"
}

import json

# Converting Python to JSON string
pet = {
    "name": "Luna",
    "age": 3,
    "breed": "Labrador"
}
json_string = json.dumps(pet)

# Parsing JSON string to Python
parsed_pet = json.loads(json_string)


import json

# Converting Python to JSON string
pet = {
    "name": "Luna",
    "age": 3,
    "breed": "Labrador"
}
json_string = json.dumps(pet)

parsed_pet = json.loads(json_string)

print(type(json_string))
print(type(parsed_pet))



# Creates a dictionary containing car information with make, model, and year
cars = {
    "make": "toyota",
    "model": "matrix",
    "year": 2006    
    }
# Outputs the dictionary to the console
print(cars)

# Converts the Python dictionary to a JSON-formatted string
jason_string = json.dumps(cars)
# Parses the JSON string back into a Python dictionary
# Note: There is a bug here - should be json.loads(jason_string) instead of json.loads(cars)
parsed_cars = json.loads(json_string)
# Prints the data type of the JSON string (should output: <class 'str'>)
print(type(json_string))
# Prints the data type of the parsed dictionary (should output: <class 'dict'>)
print(type(parsed_cars))