import sqlite3

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

table = '''
        CREATE TABLE users 
        (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT 
        )
        '''
cursor.execute(table)
connection.commit()

cursor.execute('''
                INSERT INTO users VALUES
                (1, 'John', 'john@email.com'),
                (2, 'Mary', 'mary@email.com'), 
                (3, 'Robert', 'robert@email.com'),
                (4, 'Laura', 'laura@email.com') 
            ''',)
connection.commit()

query = cursor.execute('''
                       SELECT * FROM users
                       ''')
query = cursor.execute('''
                       SELECT name FROM users LIMIT 3
                       ''')
query = cursor.execute('''
                       SELECT name FROM users ORDER by name DESC
                       ''')
query = cursor.execute('''
                       SELECT name FROM users WHERE name="Mary"
                       ''')
for result in query:
    print(result)

# for row in query:
#     first_name = row[0]
#     last_name = row[1]
#     print(f"name: {first_name}, email: {last_name}")


connection.close()