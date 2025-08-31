#In this we will see NumPy Array properties.
# 1st we will se size, shape, ndim,dype property of array.
#size is use to check the size of array.
#shape is used to check number of rows and colunm of array. 
# ndim is used to check the dimension (1D, 2D ,3D etc)
# dtype is use to check the datatype of array like int64, float64 , <U32 (String)
import numpy as np

array1=np.array([
               [[1,2,3],[4,5,6],[7,'stre',9]],
               [[10,11,12],[13,14,15],[16,17.2,18]],
                ])
print("Array:\n",array1)
print("Size of array:",array1.size)
print("Shape of array:",array1.shape)
print("Number of dimensions of array:",array1.ndim)
print("Data type of array elements:",array1.dtype)



#now next property is .astype() method
#it is used to change the data type of array elements

int_array=np.array([1,2,3,4,5])
float_array=int_array.astype(float)

print(int_array,int_array.dtype)
print(float_array,float_array.dtype)