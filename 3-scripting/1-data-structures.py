import os
directories = os.listdir('../files')
directories.append('example')
directories.insert(0,'example at 0')
print(directories)
printIndex = directories.index('expectancy.csv')

directories.append('example')
print(printIndex)

# dictionaries
contacts = {"name": "Alexandre", "lastname": "Cumplido"}
contact_retrieve = contacts.get("phone", None)
contacts.values()
print(contacts)



