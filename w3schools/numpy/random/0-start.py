from numpy import random
import numpy as np

i = random.randint(11)
ia = random.randint(11, size=(4)) #returns array of shape (4)
ia2 = random.randint(11, size=(2,4)) # returns 2D array

fa1 = random.rand(3)
fa2 = random.rand(2,3)

x = random.choice([97, 3, 75, 14])
x2 = random.choice([97, 3, 75, 14], size=(3,2))

"""
The probability is set by a number between 0 and 1, 
where 0 means that the value will never occur and 1 means that the value will always occur.
The sum of all probability numbers should be 1.
"""
x3 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(5))

"""
A permutation refers to an arrangement of elements. 
e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.

The NumPy Random module provides two methods for this: 
shuffle() and permutation().
"""
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr) # will change arr
x4 = random.permutation(arr)
print(x4)
