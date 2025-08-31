python_list=[1, 2, 3, 4, 5]
print("Python List:", python_list)

import numpy as np

# Create a 1d NumPy array from the Python list
numpy_array= np.array([1, 2, 3, 4, 5])
print("NumPy Array:", numpy_array)

# create default numpy array with default values as zero

defaultZero_array=np.zeros((3, 4))
print("Default NumPy Array with zeros:\n", defaultZero_array)

# Create a NumPy array with default vales as ones
ones_array=np.ones((2, 5))
print("NumPy Array with ones:\n", ones_array)

# Create a NumPy array with default values as any specific number
defaultSpecific_array=np.full((3,2),9)
print("NumPy Array with specific default value:\n", defaultSpecific_array)



#create and numpy array with particular range
# Like in python range function, numpy 'arange' function also takes start, stop and step values
range_array=np.arange(1,11,2)
print("NumPy Array with range of values:\n", range_array)

# For creating Identity matrix, we can use 'eye' function of numpy
identity_matrix=np.eye(3)
print("Identity Matrix:\n", identity_matrix)