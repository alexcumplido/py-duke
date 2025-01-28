import json
import os

# Serialize and dump
data = {"John": "John@example.org", "Mary": "Mary@example.org", "Jim": "Jim@example.org"}
json_data = json.dumps(data)

# Deserialize data
dict_deserialized = json.loads(json_data)
print(type(json_data))

str_deserialized = json.loads('[1,2,3]')
print(type(str_deserialized))

# 1 Serialize and dump
# Serialize: serialize a python object to a format like JSON
# Dump: serialize a python object into JSON
# Write_ save data to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Read JSON file to a Python Dictionary
# Deserialize: Convert JSON to a python object
# Read_ Get content of a file as string
# Load_ Read JSON data into  a Python object
with open('data.json') as file:
    data = json.load(file)
    print(type(data))

file_exists = os.path.exists('data.json')
print(f"Veririfaction data.json file exist", file_exists)