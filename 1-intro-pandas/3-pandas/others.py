# Reflection Questions
# What are some limitations you’ve encountered when working with Pandas? When might an alternative be better suited?
# How could PySpark or Dask help you work with larger datasets than possible in Pandas alone?
# What infrastructure and configuration is needed to leverage PySpark or Dask effectively?
# What are tradeoffs between ease of use with Pandas vs scalability with PySpark/Dask?
# How might you leverage all 3 tools together on a larger project?

# Challenges
# Load a 1GB CSV into Pandas. How does performance compare to Dask?
# Set up PySpark locally and compare reading 1M rows to Pandas
# Combine output from Dask ingest to PySpark machine learning pipeline
# Use Pandas to analyze random sample output from PySpark cluster
# Distributed apply: Calculate mean of 100M rows in PySpark, output to Pandas

import numpy as np

#Numpy
# Size set at creation


my_array = np.array(
    [1, 2, 3, 4]
)
# print(my_array)

my_array = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
# print(my_array.ndim, my_array.size, my_array.shape)


oned = np.arange(12)
print(oned)
twod = oned.reshape(3, 4)
print(twod.shape, twod.ndim)


# Single data type


darray = np.arange(100, dtype=np.int8)
print(darray.nbytes)

# darray['12'] = 'a'

# Not limited to two dimensions

# Matrix Operations




k = np.array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
print(k.shape)