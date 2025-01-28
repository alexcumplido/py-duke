# Iterating over data structures

names = ['John', 'Mary', 'Alfredo', 'Kennedy', 'Jim']

for name in names:
    print(name)

long_names = [name for name in names if len(name) > 5]

names.append('Alexandre')
print(names)
numbers = [1, 2, 3, 4, 5, 6]
evens = []
odds = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Even numbers:", evens)
print("Odd numbers:", odds)        

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

contacts = {"John": "John@example.org", "Mary": "Mary@example.org", "Jim": "Jim@example.org"}

for contact in contacts.values():
    print(contact)

for key, value in contacts.items():
    print(key,value)    


## Iteratinv over tupples and sets

read_only = (1,2,3,4)
read_unique = {1,1,2,2,3,3,3,3,4}

for ro_item in read_only: print(ro_item)
for ro_item in read_unique: print(ro_item)


import os
home_items = os.listdir('../2-unix/4-files/')
home_content = {"files": [], "directories": []}


home_paths = [os.path.join('2-unix/4-files/', item) for item in home_items]


for path in home_paths:
    if os.path.isdir(path):
        home_content['directories'].append(path)
    if os.path.isfile(path):
        home_content['files'].append(path)
    ''
print(home_content)