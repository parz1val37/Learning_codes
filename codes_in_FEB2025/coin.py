# a = ['H','T']
# b = ['H','T']
# c = ['H','T']
# d = ['H','T']

# k = [(w,x,y,z) for w in a for x in b for y in c for z in d]
# print(k)

import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,7,8,9])

d = [(x+y) for x in a for y in b]
print(d)
 
e = d.count(8)
print(e)