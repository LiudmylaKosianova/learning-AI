import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

#prints each element (needs as many loops as there are dimentions)
for x in arr:
  for y in x:
    print(y)

#prints each element (one loop for any number of dimentions)
for x in np.nditer(arr): 
  print(x)

"""
Iterating Array With Different Data Types
We can use op_dtypes argument and pass it the expected datatype 
to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array)
so it needs some other space to perform this action, that extra space is called buffer, 
and in order to enable it in nditer() we pass flags=['buffered'].
"""

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]): # Iterate through every scalar element of the 2D array skipping 1 element:
  print(x)

"""
Sometimes we require corresponding index of the element while iterating, 
the ndenumerate() method can be used for those usecases.
"""
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

"""
We pass a sequence of arrays that we want to join to the concatenate() function, 
along with the axis. If axis is not explicitly passed, it is taken as 0.
"""

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])
# print("*****concatenate")
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)
# arr = np.stack((arr1, arr2), axis=1)
# print("*****stack")
# print(arr)
"""
Stacking is same as concatenation, 
the only difference is that stacking is done along a new axis.
hstack() - stack along rows
vstack() - stack along columns
dstack() - stack along depth
"""
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))
# arr01 = np.vstack((arr1, arr2))
# arr02 = np.dstack((arr1, arr2))
# print("----------------------")
# print(arr02)


