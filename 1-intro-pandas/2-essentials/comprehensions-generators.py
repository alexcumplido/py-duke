# Reflection Questions

# What are some real-world cases where you would want to use a list comprehension?
# How do generators help when working with large data sets?
# What is the key difference in how list comprehensions and generators create sequences?
# In what ways are iterables and iterators connected to generators?
# When would you want to use a list comprehension versus a generator?

# Challenges

# Convert an existing for loop that produces a list into a list comprehension
# Create a generator function to produce the Fibonacci sequence
# Determine if a built-in Python sequence like a string is an iterator or iterable
# Print the first 5 items from a generator without saving the full sequence
# Write list comprehension to filter odd numbers from a list


# Replace a for-loop
output = []
for x in range(10):
    output.append(x**2)

print(output)

output = [x**2 for x in range(10)]
print(output)

# Map a function onto a sequence
import random
scores = []

for i in range(5):
    scores.append(random.randint(i,10))
print(scores)

scores = [random.randint(x, 10) for x in range(5)]
print(scores)

# Filter a sequence
caps = []
str_example = "Rusell Sage"
for letter in str_example:
    if letter.isupper():
        caps.append(letter)
print(caps)

caps = [char for char in str_example if char.isupper()]
print(caps)

# Nest list comprehensions

list_of_lists = [['a', 'b', 'c'],['d', 'e','f'],['g', 'h', 'i']]
flat = []

for sub_list in list_of_lists:
    for item in sub_list:
        flat.append(item)

print(flat)
flat = [item for sublist in list_of_lists for item in sublist] 
print(flat)


# Create generator expressions

import sys
large_sum = 9999999

l_squares = [x**2 for x in range(large_sum)]
l_size = sys.getsizeof(l_squares)
print(l_size)


g_squares = (x**2 for x in range(large_sum))
g_size = sys.getsizeof(g_squares)
print(g_size)


for x in g_squares:
    print(x)
    if x > 12: break
# Chain generator expressions together

evens = (x for x in range(0, 100, 2))
div_three = (y for y in evens if y%3 == 0)

print(next(div_three))

print([x for x in div_three])

# Yields statements

def return_num():
    for x in range(5): 
        return x

def yield_return_gen():
    for x in range(5): 
        yield x

print(yield_return_gen())
gen_num = yield_return_gen()
print(next(gen_num))

# Infinite generators

def counter(x):
    while True:
        yield x 
        x += 1

count = counter(10)

for x in range(100): print(next(count))

