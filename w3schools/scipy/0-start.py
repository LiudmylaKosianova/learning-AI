from scipy import constants
import scipy

# print(constants.liter)
# print(scipy.__version__)
#print(dir(constants))

"""
For that you can use SciPy's optimize.root function.

This function takes two required arguments:
fun - a function representing an equation.
x0 - an initial guess for the root.

The function returns an object with information regarding the solution.

The actual solution is given under attribute x of the returned object
"""

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

#print(myroot.x)

from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

# plt.triplot(points[:, 0], points[:, 1], simplices)
# plt.scatter(points[:, 0], points[:, 1], color='r')

# plt.show()
