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

import os
path = '/files/'
file = 'custom_wine.json'
full_path = os.path.join(path, file)
print(full_path)

import main
print(f"The name of this module is: {__name__}")