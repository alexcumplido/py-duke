# Simple statements

# Reflection Questions
# What are some common exceptions you might encounter when writing Python code?
# When might you want to manually raise an exception in your code?
# How could you use assert statements to validate the inputs to a function?
# What exception handling code could you add to make your programs more robust?
# Why is it useful to raise errors and handle exceptions in programming?

# Challenges
# Add a raise statement to throw a custom exception when invalid parameters are passed to a function
# Use try/except blocks to catch errors and handle them gracefully
# Validate numeric inputs to functions with assert statements
# Research built-in Python exceptions and choose ones relevant for a program you are writing
# Handle possible exceptions from importing external libraries or modules

# Compound statements

# Reflection Questions
# What is the syntax for defining a function in Python?
# How do parameters allow passing data into functions?
# Why are return statements important for getting output from functions?
# What are some examples of functions you could define and use in your programs?
# How could functions help improve your code reuse and organization?

# Challenge Exercises
# Define a function that calculates simple interest
# Create a function to test if a word is a palindrome
# Write a function that finds the maximum of three numbers
# Develop a function to format a date string into a readable format
# Define a function to generate a random password

import pandas as pd

data = {'Apples': [30], 'Bananas': [21]}
purchases = pd.DataFrame(data)

print(purchases)


s = pd.Series([1,2,3])

total = s.sum()

total += 10

try: 
	s.no_such_attribute()
except AttributeError:
	print("Ooops!")

import os
from os import path

from os.path import isdir
import pandas as pd
os

os.getcwd()
os.path
os.path.isdir('.')

path.isdir('.')


isdir('.')

a = 23 / 0
print(a)

import pandas as pd

def analyze_series(s):
    """Analyze pandas Series.
    
    Demonstrates assertions and exception handling.
    """
    
    # Validate inputs
    assert isinstance(s, pd.Series), "Input must be a pandas Series"  

    try:
        # Attempt processing 
        mean = s.mean()  
        median = s.median()

    # Catch errors    
    except Exception as e:   
        # Manually raise exception
        raise ValueError("Error analyzing series") from e  

    # Assert reasonable results       
    assert (mean > 0) & (median > 0), "Mean and median are invalid!"
    
    return mean, median
    
s = pd.Series([1, 2, 3])
analyze_series(s)

# Function decorator that times execution
from time import time

def timer(func):
    # Nested wrapper function
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Duration: {end-start}")
    return wrapper

@timer
def sum_nums():
    result = 0
    for x in range(1000000):
        result += x

sum_nums()

"""Compound statementes"""
a = 0
while a <= 4:
    a += 1
else:
    a= 0

print(a)

def my_function(a, b, c):
    print(a, b, c)

print(my_function(a=10, c=20, b=30))