# Utilize SQLite to persist data from Python
# Design scripts to connect and query SQL data base form within Python

# Module: Python file that can be imported
# Dunder main: Special variable main that indicates if module run directly
# Import: Load functions and classes from another module
# Absolute path: Full path to a file or directory from the root folder
# Traverse: Recursively visit nodes in a  tree data structure
# Directory: A folder that can contain files and other directories
# File path: The location of a file in the file system
# Join: Concatenate directory and file path into full path
# Process: Perform operations on data
import sqlite3
import os
import logging
import main

logging.basicConfig(level=logging.INFO)

path = '/files/'
file = 'custom_wine.json'
full_path = os.path.join(path, file)
print(full_path)

connection = sqlite3.connect('files.db') 

table = '''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        path TEXT, 
        bytes INTEGER
    )
'''

cursor = connection.cursor()
cursor.execute(table)
connection.commit()

print(f"The name of this module is: {__name__}")

file_metadata = {}
for root, directories, files in os.walk("../1-intro-pandas"):
    for _file in files:
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        file_metadata[full_path] = size
        cursor.execute(f'INSERT INTO files (path, bytes) VALUES({full_path}, {size})')
        logging.info(f"Size: {size}b - File: {full_path}")

print(file_metadata)



items_shown = 0
for path, size in sorted(file_metadata.items(), key=lambda x:x[1], reverse=True):
    if items_shown > 4:break
    logging.info(f"Size: {size} Path: {path}")
    items_shown += 1

   


