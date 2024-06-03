import numpy as np

# myA = np.array([1,2,3,4])
# print(myA)
# print(type(myA))

# """
# The source code for NumPy is located at this github repository https://github.com/numpy/numpy

# The array object in NumPy is called ndarray, 
# it provides a lot of supporting functions that make working with ndarray very easy.
# """

# print(np.__version__)

# """
# To create an ndarray, we can pass a list, tuple or any array-like object 
# into the array() method, and it will be converted into an ndarray:
# """

# myA2 = np.array((3,5,7))
# print(myA2)

"""
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
"""

arr0d = np.array(7)
#print(arr0d)

arr1d = np.array([1,9])
arr2d = np.array([
                 [13,5],[7,98]
                 ])

"""
NumPy has a whole sub module dedicated towards matrix operations called numpy.matS
"""

arr3d = np.array([
                  [[13,5],[7,98]],
                  [[2,11],[77,2]]
                  ])

"""
NumPy Arrays provides the ndim attribute that returns an integer
that tells us how many dimensions the array have.
"""

#print(arr0d.ndim, arr1d.ndim, arr2d.ndim, arr3d.ndim)

"""
*create a 5 dim array
In this array the innermost dimension (5th dim) has 4 elements, 
the 4th dim has 1 element that is the vector, 
the 3rd dim has 1 element that is the matrix with the vector, 
the 2nd dim has 1 element that is 3D array and 
1st dim has 1 element that is a 4D array.

"""
arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

#print('5th element on 2nd row: ', arr[1, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#print(arr[0, 1, 2])

"""
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7])

#print(arr[1:5:2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#print(arr[1, 1:4])
print(arr[0:2, 2]) # from both elements return index 2
print(arr[0:2, 1:4]) # it will return a 2D array