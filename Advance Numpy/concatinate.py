'''
np.concatenate((arr1,arr2), axis=0)

axis 0  --> vertical stacking
axis 1  --> horizontal stacking
'''

import numpy as np

arr1= np.array([10,20,30])
arr2= np.array([30,50,60])

newArr=np.concatenate((arr1,arr2))
print(newArr)