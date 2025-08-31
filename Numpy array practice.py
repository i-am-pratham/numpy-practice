# Create a NumPy array with numbers from 1 to 20 using np.arange().
# Print its shape, size, ndim, and dtype.

import numpy as np

arr1= np.arange(1,21)
print(arr1)

print("Shape:",arr1.shape)
print("Size:",arr1.size)
print("Dimention:",arr1.ndim)
print("DataType:",arr1.dtype)
# ___________________________________________________________________________________________________________

# Create a 2D array of shape (3,4) with values from 10 to 21 (inclusive).

arr2=np.arange(10,22)
arr_new=arr2.reshape(3,4)
print(arr_new)


# ______________________________________________________________________________________________

# Create a 3D array of shape (2,2,3) with any values.

# Print each 2D “layer” separately.

arr3=np.arange(1,13).reshape(2,2,3)

print(arr3)

print("First Layer:",arr3[0])
print("Second Layer:",arr3[1])

# _____________________________________________________________________________________________________________

# Create an identity matrix of size 5x5.

# Verify that its diagonal elements are all 1 and others are 0.

arr4=np.eye(5)
print(arr4)
# ___________________________________________________________________________________________________________

# Create an integer array arr = [10, 20, 30, 40].

# Convert it to float using astype().

# Then convert it into string type.

arr_int=np.array([10,20,30,40])
print("Integer array:",arr_int,arr_int.dtype)

arr_float= arr_int.astype(float)
print("Float array:",arr_float,arr_float.dtype)

arr_str=arr_int.astype(str)
print("String array:",arr_str,arr_str.dtype)

# _____________________________________________________________________________________________________

# Create an array with values [1.5, 2.3, 7.8, 9.6].

# Convert to integers and check the difference in values.

arr5=np.array([1.5,2.3,7.8,9.6])
print("Float array",arr5,arr5.dtype)

arr6= arr5.astype(int)
print("Int array",arr6,arr6.dtype)

# _____________________________________________________________________________________________________________

"""🔹 3. Mathematical Operations

Create two arrays:

a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])


Perform:

a + b, a - b, a * b, a / b

a ** 2 and b % 2 """
a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

print(a ,"+",b,"=",a+b)
print(a ,"-",b,"=",a-b)
print(a ,"*",b,"=",a*b)
print(a ,"/",b,"=",a/b)
print(a ,"**2 =",a**2)
print(b ,"%2 =",b%2)

# _____________________________________________________________________________________________

# Create a 3x3 matrix with values from 1 to 9.

# Multiply all elements by 10.

# Divide all elements by 2.

# Square the matrix.

arr_matrix=np.arange(1,10).reshape(3,3)
print(arr_matrix)

print("Multiply all elements by 10:", arr_matrix*10)
print("Divide all elements by 2:",arr_matrix/2)
print("Square the matrix:",arr_matrix**2)

# ____________________________________________________________________________________________________________

# Create an array with values [5, 10, 15, 20, 25, 30].

# Find the sum, mean, max, min, standard deviation, and variance.

arr7=np.array([5,10, 15, 20, 25, 30])
print(arr7)
print("Sum:",arr7.sum())
print("Product:",arr7.prod())
print("Mean:",arr7.mean())
print("Max and Min:",arr7.max(),"&",arr7.min())
print("standard deviation:",arr7.std())
print("Variance:",arr7.var())

# ___________________________________________________________________________________________________________________

'''Create the following 2D array:

arr = np.array([[3, 6, 9],
                [12, 15, 18],
                [21, 24, 27]])


Find the sum along rows (axis=1).

Find the sum along columns (axis=0).

Find the maximum of each row.'''

arr = np.array([[3, 6, 9],
                [12, 15, 18],
                [21, 24, 27]])

print(" the sum along rows (axis=1):", arr.sum(axis=1))
print(" the sum along columns (axis=0):", arr.sum(axis=0))
print(" the maximum of each row:", arr.max(axis=1))

# ___________________________________________________________________________________________

'''Create a 4x4 matrix with values from 1 to 16.

Print the matrix shape, size, ndim, dtype.

Convert it to float using astype().

Calculate the sum of all elements.

Calculate row-wise mean and column-wise standard deviation.

Multiply the matrix by 2 and subtract 5 from all elements.'''

arr8= np.arange(1,17).reshape(4,4)
print(arr8)
print("Shape:",arr8.shape)
print("Shape:",arr8.size)
print("Dimention:",arr8.ndim)
print("Datatype:",arr8.dtype)

arr9=arr8.astype(float)
print("After converting into float:",arr9,arr9.dtype)

print("Calculate the sum of all elements:",arr8.sum())

print("row-wise mean:",arr8.mean(axis=1))
print("column-wise standard deviation:",arr8.std(axis=0))

print("Multiply the matrix by 2 ",arr8*2)
print("subtract 5 from all elements:",arr8-5)