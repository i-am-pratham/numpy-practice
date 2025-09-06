'''
np.split()- split array into equal parts.

np.hsplit()
np.vsplit()

'''



import numpy as np

# arr=np.arange(1,10)
# print(arr)
# arr2=np.array_split(arr,2)
# print (arr2)

arr = np.arange(1,13).reshape(3,4)
print(arr)

print(np.hsplit(arr,2))  # Split into 2 column parts
print(np.vsplit(arr,3))  # Split into 3 row parts
