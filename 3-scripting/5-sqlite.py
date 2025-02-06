# Develop data engineering solutions using Python and the Linux environment
# Design scripts to connect and query a SQL database using Python
# Use a scraping tool to extract data from the web
# Setup provisioned Python project environment

# SQLite: Embedded, serverless SQL database
# Table: Collection of related data in columns and rows
# Query: SQL statement to insert, retrieve, update, or delate data
# Commit: Make changes permanent in a database transaction
# Cursor: Object to execute queries and fetch results
# Primary key: unique identifier for a row in a table
# Generate: PRoduce sample data programmatically
# Persist: Save data so it exists after program execution

import sqlite3


## CREATE TABLE ##
# conn = sqlite3.connect(':memory')
conn = sqlite3.connect('sample.db')

table = '''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        lastname TEXT
    )
'''

cursor = conn.cursor()

cursor.execute(table)

conn.commit()

# CREATE DATA

cursor.execute('''
    INSERT INTO users (name, lastname)
    VALUES (?, ?)
''', ('John ', 'Doe'))

conn.commit()

# DATA MOCKING

from faker import Faker
fake = Faker()
names = [fake.name().split() for i in range(100)]

# DATA NORMALIZATION

names = [name for name in names if len(name) == 2]

# for name in names:
#     if (len(name) == 2):
#         names.append(name)
#         print(name)


## POPULATE TABLE ##
insert_query = 'INSERT INTO users (name, lastname) VALUES(?, ?)'

for name in names:
    cursor.execute(insert_query, name)

conn.commit()

# select_query = 'SELECT * from users LIMIT 10'
# for item in cursor.execute(select_query):
#     print(item)

cursor.execute('''
    SELECT * FROM users
''')

for row in cursor: print(row)