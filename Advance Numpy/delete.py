'''
delete is used to delete the element at specific index
np.delete(array, index, axis)
'''
import numpy as np

# deleting in 1D array

arr=np.array([10,20,30])
print(arr)

newArr= np.delete(arr, [0,1])
print(newArr)

# Deleteing in 2D array

arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)

newArr2D= np.delete(arr_2d, 1, axis=1)
print(newArr2D)

