# Reflection Questions
# - How are decorators defined and applied to functions in Python?
# - What syntax is used to wrap the original function inside the decorator?
# - Why are decorators useful for extending functionality without modifying original code?
# - How could you create your own decorator for validation, authorization etc?
# - What are some common use cases for Python decorators?

# Challenge Exercises
# - Improve timer decorator to log fastest and slowest durations
# - Create a debug decorator that enters debugger before function call
# - Implement a retry decorator to retry failing function calls
# - Enhance cache with maximum size and LRU cache expiration
# - Add parameterization so delays can be customized

import time
import functools
from functools import wraps

def timer(func):
    def wrapper():
        start = time.time()
        print(f"Started at {start}")
        func()
        end = time.time()
        print(f"Ended at {end}")
        print(f"Duration: {end-start}")
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Ran {func.__name__} with args: {args}, and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def cache(func):
    cache_data = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in cache_data:
            cache_data[key] = func(*args, **kwargs)
        return cache_data[key]
    return wrapper

def expensive_func(x):
    start_time = time.time()
    time.sleep(2)
    print(f"{expensive_func.__name__} ran in {time.time() - start_time:.2f} secs")
    return x

def delay(seconds):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {seconds} seconds before running {func.__name__}")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return inner



