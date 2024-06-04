import numpy as np

"""
Note: The return value is a list containing three arrays.
"""
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
"""
Note: We also have the method split() available but it will not adjust the elements 
when elements are less in source array for splitting like in example above, 
array_split() worked properly but split() would fail.
"""
newarr2 = np.array_split(arr,4)

arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr3 = np.array_split(arr2, 3)

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr4 = np.array_split(arr3, 3, axis=1)

""" where"""
a = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(a == 4) # will return the tuple with indexes of "4"
ev = np.where(a%2 == 0) # will return the indexes of even numbers


"""
Filtering Arrays
Getting some elements out of an existing array and creating a new array out of them
 is called filtering.

In NumPy, you filter an array using a boolean index list.
A boolean index list is a list of booleans corresponding to indexes in the array.

If the value at an index is True that element is contained in the filtered array, 
if the value at that index is False that element is excluded from the filtered array.
"""

 
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]
newarr = arr[x]

x1 = []
for number in arr:
    if number > 42:
        x1.append(True)
    else:
        x1.append(False)
#x1 will filter every element greater than 42
 
newA1 = arr[x1]

filter_list = arr > 42
newA3 = arr[filter_list]
print(newA3) 
