# Apply different Python data structures to work with data.
# Extract data from different sources and map it to Python data structures.
# Persist and load data using JSON, a popular data format.

import time
import os
from os.path import abspath, join, getsize

# STATE
now = time.time()
print(now)
BASE_PATH = "/home/acumplid"
## LISTS
directories_ex = os.listdir('../files')
directories_ex.append('example')
directories_ex.insert(0,'example at 0')
# print(directories_ex)

important_directories = []

for item in os.listdir(BASE_PATH):
    full_path = os.path.join(BASE_PATH, item)
    if os.path.isdir(full_path):
        important_directories.append(item) 

for item in important_directories:
    if item[0].isupper():
        print(item)
# print(important_directories)

nested_items = [['a', '1', '23', 'b', '4', 'c', 'd'], ['a', '1', '23', 'b', '4', 'c', 'd']]
numeric_nested = []
for parent_item in nested_items:
    for child_item in parent_item:
        if child_item.isnumeric():
            numeric_nested.append(child_item)
# print(numeric_nested)

## LIST COMPREHENSION
items = ['a', '1', '23', 'b', '4', 'c', 'd']
standard_list = []
for item in items:
    if item.isnumeric(): 
        standard_list.append(item)
# print(standard_list)

comprehension_list = [item for item in items if item.isnumeric()]
# print(comprehension_list)

## DICTIONARIES
contacts = {
    'alexandre': '+3 678-677-0000',
    'alfredo': '+3 678-677-0000'
}

comp_keys = [key for key in contacts.keys()]  
comp_values = [val for val in contacts.values()]
comp_items = [(key, val) for key,val in contacts.items()]

# print(comp_values)
# print(comp_keys)
# print(comp_items)

list_of_list =  [['a', 1], ['b', 2], ['c', 3]]
to_dict = dict(list_of_list)
# print(to_dict)

user = {'name': 'alfredo', 'surname': 'deza', 'username': 'alfredodeza'}
# print(user.get('asdas', 'Problem with property'))

##
sizes = {}
for top_dir, directories, files in os.walk(BASE_PATH):
    # for directory in directories:
    #     print(abspath(join(top_dir, directory)))
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
        print('Full path: {0}, size: {1}'.format(full_path, size))
    break
   
sorted_results = sorted(sizes, key=sizes.get, reverse=True)

for path in sorted_results[:10]:
    print("Path: {0}, size: {1}".format(path, sizes[path]))