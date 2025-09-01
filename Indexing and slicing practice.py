# 1. Indexing Basics

# Create a 1D array of numbers from 10 to 50 (step 10).

# Print the first, third, and last element using indexing.

import numpy as np

arr=np.arange(10,51,10)
print(arr)

print("First element :",arr[0])
print("Third element :",arr[2])
print("Last element :",arr[-1])

print("____________________________________________________________________________________")

# _________________________________________________________________________________________________
'''Create a 2D array:

[[10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]]


Print the element at row 2, column 1.

Print the last element using negative indexing.'''



arr2=np.arange(10,91,10).reshape(3,3)
print(arr2)

print(arr2[1,0])
print(arr2[-1,-1])

print("____________________________________________________________________________________")



# ___________________________________________________________________________________________

# 2. Slicing

# Create a 1D array with values from 1 to 20.

# Extract elements from index 5 to 15.

# Extract every 3rd element.

# Extract the last 5 elements using slicing.

arr3=np.arange(1,21)
print(arr3)
print(arr3[5:16])
print(arr3[::3])
print(arr3[-1:-6:-1])

print("________________________________________________________________________________")
# __________________________________________________________________________________________

# From the above 3×3 array, extract:
# First two rows.
# Last two columns.
# Middle row [40, 50, 60].

arr4=np.arange(10,91,10).reshape(3,3)
print(arr4)

print("First two rows.",arr4[:2, :])
print(" Last two columns.",arr4[:, 1:3])
print("Middle row [40, 50, 60].", arr4[1:2, :])

print("____________________________________________________________________________________")


# ________________________________________________________________________________________________________

"""3. Fancy Indexing

Create an array [5, 10, 15, 20, 25, 30, 35].

Select elements at positions 0, 2, 4, 6.

Select elements [10, 25, 35] using fancy indexing."""


arr5=np.array([5, 10, 15, 20, 25, 30, 35])
print(arr5)
print("elements at positions 0, 2, 4, 6 :", arr5[[0,2,4,6]] )
print("elements [10, 25, 35] using fancy indexing :", arr5[[1,4,6]])

print("____________________________________________________________________________________")


# ________________________________________________________________________________________________________


"""Create a 2D array:

[[11, 12, 13],
 [21, 22, 23],
 [31, 32, 33],
 [41, 42, 43]]


Extract rows 0 and 2.

Extract columns 1 and 2."""

arr6=np.array([[11, 12, 13],
 [21, 22, 23],
 [31, 32, 33],
 [41, 42, 43]])

print(arr6)

print(arr6[[0,2]])
print(arr6[:, [1,2]])

print("____________________________________________________________________________________")


# ________________________________________________________________________________________________________

'''4. Boolean Masking (Filtering)

Create an array [2, 7, 12, 19, 24, 31, 36, 45].

Find all elements greater than 20.

Find all even numbers.

Find all elements divisible by 3 and 5.'''

arr7=np.array( [2, 7, 12, 19, 24, 31, 36, 45])
print(arr7)
num= arr7>20

print(" elements greater than 20 :",arr7[num])

even= arr7 %2 ==0

print("all even numbers",arr7[even])

divisibleBy3and5= (arr7 %3==0) & (arr7 %5==0)

print("all elements divisible by 3 and 5", arr7[divisibleBy3and5])

print("____________________________________________________________________________________")


# ________________________________________________________________________________________________________
'''From the 2D array

[[5, 10, 15],
 [20, 25, 30],
 [35, 40, 45]]


Extract all numbers greater than 25.

Extract all numbers divisible by 10.'''



arr8=np.array([[5, 10, 15],
 [20, 25, 30],
 [35, 40, 45]])

print(arr8)
greaterThan25= arr8>25

print("numbers greater than 25 :",arr8[greaterThan25])

divisibleBy10= arr8%10==0
print("numbers divisible by 10 ;",arr8[divisibleBy10])

print("____________________________________________________________________________________")


# _______________________________________________________________________________________________________

'''5. Reshaping

Create a 1D array from 1 to 12.

Reshape it into a 3×4 array.

Reshape it into a 2×2×3 array.

Try reshaping it into 5×5 (what happens?).'''

arr9=np.arange(1,13)
print(arr9)

reshaped1=arr9.reshape(3,4)
print(reshaped1)

reshape2=arr9.reshape(2,2,3)
print(reshape2)


#after reshaping into 5x5 it will throw error because 5x5=25 but total elements in array are 12

# reshape3=arr9.reshape(5,5)

print("____________________________________________________________________________________")


# _______________________________________________________________________________________________________


'''6. ravel() and flatten()

Create a 3×3 array with values from 1 to 9.

Use ravel() to flatten it.

Change one element in the raveled array and check if the original array changes.

Use flatten() instead and check the difference.'''

arr10=np.arange(1,10).reshape(3,3)

print(arr10)
ravelArray= arr10.ravel()
print(ravelArray)
ravelArray[0]=10

print(arr10)
print(ravelArray)

flattenArray=arr10.flatten()
print(flattenArray)

flattenArray[0]=1
print(flattenArray)

print(arr10)

print("____________________________________________________________________________________")


# _______________________________________________________________________________________________________


'''💡 Challenge Exercises (Mix Concepts)

Create an array of shape 6×6 filled with numbers 1 to 36.

Extract the first row.

Extract the last column.

Extract the 2×2 block from the center.

Flatten it using both ravel() and flatten().'''


newarray=np.arange(1,37).reshape(6,6)
print(newarray)

print("First Row:", newarray[:1, :])
print("Last column:", newarray[:,5:6])

print("2x2 block from center:",newarray[2:4,2:4])

new1DArray=newarray.ravel()
new1DArray2=newarray.flatten()

print("1D array using ravel():", new1DArray)
print("1D array using ravel():", new1DArray2)

print("____________________________________________________________________________________")


# _______________________________________________________________________________________________________
'''Create a 1D array of size 20 with random numbers between 1 and 100.

Filter all numbers greater than 50.

Select numbers at even indices.

Reshape it into 4×5 and extract the 3rd row.'''


randomArr=np.random.randint(1,101, size=20)
print(randomArr)

greaterThan50= randomArr>50
print("numbers greater than 50:", randomArr[greaterThan50])

print("numbers at even indices",randomArr[2::2])

newReshapeArr=randomArr.reshape(4,5)
print("Reshape array:",newReshapeArr)

print("3rd row:", newReshapeArr[3:,:])