import numpy as np

"""
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""

arr = np.array([1, 2, 3, 4])
arr2 = np.array(['apple', 'banana', 'cherry'])
arr3 = np.array([13,77,21], dtype='S')
#print(arr3.dtype)
#print(arr3)

"""
For i, u, f, S and U we can define size as well.
"""
arr = np.array([1, 2, 3, 4], dtype='i4') # 4 bytes integer

"""
The best way to change the data type of an existing array, 
is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, 
and allows you to specify the data type as a parameter.
"""
arr = np.array([1.1, 2.1, 3.1, 0.0])
newarr = arr.astype('i') # newarr = arr.astype(int) will do the same
newarr2 = arr.astype(bool)
 

"""
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.
"""
arr = np.array([1, 2, 3, 4, 5])
arrC = arr.copy()
arr[0] = 42 # it will not affect the arrC since arrC is a copy

arrV = arr.view()
arrV[0] == 99
arr[-1] == 99
#changes in arr affect arrV and vice versa

"""
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.
"""
original = np.array([1, 2, 3, 4, 5])

copy_Or = original.copy()
view_Or = original.view()

# print(copy_Or.base)
# print(view_Or.base)

"""
Shape of an Array
The shape of an array is the number of elements in each dimension.

Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple 
with each index having the number of corresponding elements.

"""
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#print(arr.shape) # 2 dimentions, each has 4 elements

arr2 = np.array([1, 2, 3, 4], ndmin=5)

# print(arr2)
# print('shape of array :', arr2.shape) 
# Integers at every index tells about the number of elements the corresponding dimension has.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
""" From 1D to 2D array"""
newarr = arr.reshape(4, 3)
nr = arr.reshape(3,4)
nr2 = arr.reshape(2,6)
""" From 1D to 3D array"""
nr3 = arr.reshape(2,3,2) 
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements
nr4 = arr.reshape(4,3,1,1)
#print(nr4)
my4 = np.array([     
    [[[1]],[[1]],[[1]]],
    [[[1]],[[1]],[[1]]],
    [[[1]],[[1]],[[1]]],
    [[[1]],[[1]],[[1]]]
])
# print(my4.shape)
# print(nr4.base)

"""
Flattening the arrays
Flattening array means converting a multidimensional array into a 1D array.

We can use reshape(-1) to do this.
"""
my4.reshape(-1)

