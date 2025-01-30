import json
import os
from csv import DictReader
import pandas as pd

# # Serialize and dump
# data = {"John": "John@example.org", "Mary": "Mary@example.org", "Jim": "Jim@example.org"}
# json_data = json.dumps(data)

# # Deserialize data
# dict_deserialized = json.loads(json_data)
# print(type(json_data))

# str_deserialized = json.loads('[1,2,3]')
# print(type(str_deserialized))

# # 1 Serialize and dump
# # Serialize: serialize a python object to a format like JSON
# # Dump: serialize a python object into JSON
# # Write_ save data to a file
# with open('data.json', 'w') as file:
#     json.dump(data, file)

# # Read JSON file to a Python Dictionary
# # Deserialize: Convert JSON to a python object
# # Read_ Get content of a file as string
# # Load_ Read JSON data into  a Python object
# with open('data.json') as file:
#     data = json.load(file)
#     print(type(data))

# file_exists = os.path.exists('data.json')
# print(f"Veririfaction data.json file exist", file_exists)

# sql_file = open("../files/populate.sql")


# # Ideal for processing all at once
# # sql_contents = sql_file.read()

# ## Ideal to process line by line
# sql_contents = sql_file.readlines()

# print(sql_contents)
# sql_file.close()

# ## using a context manager
# with open("../files/populate.sql") as sql_file:
#     sql_contents = sql_file.readlines()
#     print(sql_contents)

# import pandas as pd

# df = pd.read_csv("../files/wine-ratings-small.csv")
# print(df.head)

# data_raw = {"name": "Alexandre", "data": 1, "valid": True}
# json_output = json.dumps(data_raw)
# print(type(json_output))
# python_dictionary = json.loads(json_output)
# print(python_dictionary['valid'])

# with open("../files/wine-ratings.json") as file:
#     loaded_jason = json.load(file)
#     print(loaded_jason)

# data = {"name": "Alexandre", "data": 1, "valid": True}

# with open("../files/sample_data.json", "w") as file:
#     json.dump(data, file)

# with open("../files/sample_data.json", 'r') as file:
#     loaded_json = json.load(file)
#     print(type(loaded_json['valid']))


# Load a csv file
# Extract specific information
# Transform data into JSON
# Save it no a new file

with open("../files/wine-ratings-small.csv", encoding="UTF-8", errors='ignore') as file:
    reader = DictReader(file)
    wines = list(reader)

custom_wines = []
for item in wines:
    rating = float(item['rating'])
    region = item['region']
    variety = item['variety']
    con_1 = 'Red Wine'
    con_2 = 'Italy'
    con_3 = 90.0

    if con_1 in variety and con_2 in region and rating > con_3:
        custom_wines.append(item)
    
with open ("../files/custom_wine.json", 'w') as f:
    json.dump(custom_wines, f)

# ## Using dataframes
# df = pd.read_csv("../files/wine-ratings-small.csv")
# dict_data = df.to_dict()
# print(dict_data['name']) 