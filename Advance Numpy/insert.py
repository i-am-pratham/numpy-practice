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

# arr_2d = np.array([[1,2],[3,4]])
# print(arr_2d)

# #insert a new row at index 1
# new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=1)
# print(new_arr_2d)


arr2=np.array([[[1, 2],
 [3, 4]]])

# print(arr2)

new2arr=np.insert(arr2,1,[5,6],axis=1)
print(new2arr)

new2array=np.append(new2arr,[[7,8,9]],axis=1)
print(new2array)