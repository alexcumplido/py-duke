# Reflection Questions

# When would you choose a list versus a tuple for storing data?
# How can string methods help process real-world textual data like log files?
# How are range objects useful when iterating in loops?
# What sequence indexing errors have you encountered so far? How did you fix them?
# Which sequence type do you think has the steepest learning curve?

# Sequence memebership operations

name = "Alexandre"
membership_operation = "A" in name
print(membership_operation)

# Sequence indexing and slicing

sequence_operation = name[0]
print(sequence_operation)

slicing_operation = name[2:5]
print(slicing_operation)

# Sequence interrogation

len_interrgotion =  len(name)
print(len_interrgotion)

""" Range objects"""

import sys

print(list(range(1,10)))
print(sys.getsizeof(list(range(1,10000000))))

print(list(range(-2, 3)))
