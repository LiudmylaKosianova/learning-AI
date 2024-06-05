import numpy as np
from math import log

a = np.arange(1,5)
# creates an array from 1 to 4 (5 not included)

b = np.log2(a)


nplog = np.frompyfunc(log, 2, 1) 
# nplog is a new function, that performs log operation. It takes 2 parameters. It returns 1 parameter

print(nplog(100, 15))
print(b.shape)