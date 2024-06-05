import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# sns.histplot([0, 1, 2, 3, 4, 5]) 
# plt.show()
"""
Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array.
"""
x = random.normal(size=(2, 3))
x2 = random.normal(loc=1, scale=2, size=(2, 3))
#print(x, "\n***\n", x2)

"""
Binomial Distribution is a Discrete Distribution.

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:
n - number of trials.
p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
size - The shape of the returned array.
"""
a = random.binomial(n=10, p=0.5, size=10)
 

"""
Poisson Distribution is a Discrete Distribution.
It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:
lam - rate or known number of occurrences e.g. 2 for above problem.
size - The shape of the returned array.
"""

b = random.poisson(lam=2, size=10)
#print(b)
sns.displot(b)
#plt.show()

"""
Logistic Distribution is used to describe growth.

Used extensively in machine learning in logistic regression, neural networks etc.

It has three parameters:
loc - mean, where the peak is. Default 0.
scale - standard deviation, the flatness of distribution. Default 1.
size - The shape of the returned array.
"""

c = random.logistic(loc=1, scale=2, size=(2, 3))

print(c)
