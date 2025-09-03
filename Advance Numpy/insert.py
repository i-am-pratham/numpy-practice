'''
np.insert(array, index, value, axis=None)
array- original array
index- index no
value- what value you want to insert
axis- (if axis is None then the array is flatten)
axis=0 -> row-wise
axis=1 -> column-wise
'''

import numpy as np

arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)

#insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=1)
print(new_arr_2d)
