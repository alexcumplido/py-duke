# Reflection Questions

# When would you want to use a dictionary versus a list or set?
# How are dictionaries and sets similar and different in Python versus Bash?
# What real-world data would be best modeled using dictionaries or sets?
# What set operations would be useful for comparing arrays of genome data?
# How can you iterate through and access all values in a dictionary or set?

# Challenge Exercises

# Create a phone book as a dictionary with names and numbers
# Build a set of unique words from a long input string
# Compare arrays of numbers using set intersections and differences
# Sort a dictionary by key and by value
# Create histograms of word counts using dictionaries


key_1 = "henry"

print(key_1.__hash__())


dict_1 = dict(name="Alexandre", age=32)

print(dict_1)

student = {'name': 'Sparky', 'age': 32, 'major': 'Basketweaving'}

print(student.get(0))


keys_students = student.keys()
values_students = student.values()
items_students = student.items()


print(keys_students)
print(values_students)
print(items_students)


# Create a set
# Add to a set
# Remove from set
# Use set operations

my_set = set("aabbccdd")
print(my_set)
my_set.add("e")
my_set.remove("a")
print(my_set)



first_set = set(range(10))
print(first_set)
second_set = set(range(2,5))
print(second_set)
print(second_set.issubset(first_set))

print({1, 2, 3, 4}.difference({3, 4, 5}))

