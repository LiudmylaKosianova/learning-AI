import numpy as np

myArr = np.array([1,2,3])
myArr2 = np.array([[1,2], [3,4]])
#minimum dimentions
myArr3 = np.array([1,2,3,4], ndmin=2)
#data type
myArr4 = np.array([2,4,6], dtype=complex)
print(myArr4)

#numpy.dtype(object, align, copy)
